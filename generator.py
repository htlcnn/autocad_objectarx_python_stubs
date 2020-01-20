from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from pathlib import Path
import time

from bs4 import BeautifulSoup
import requests


def help_url(_id):
    # AutoCAD ObjectARX
    return 'https://help.autodesk.com/cloudhelp/2020/ENU/OARX-ManagedRefGuide/files/{}.html'.format(_id)


def indent(lines, levels=1):
    return '\n'.join([(4 *' '*levels + line) for line in lines.splitlines()])


def get_detail_page(api_id):
    url = help_url(api_id)
    while True:
        try:
            r = requests.Session().get(url)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        
    soup = BeautifulSoup(r.text)
    return soup


def get_child(parent, children_data_type=''):
    '''
    Get child with 'children_data_type' in parent['ttl']
    return first child if multiple children are found
    '''
    if not children_data_type:
        return parent['children'][0]
    for member in parent['children']:
        if children_data_type in member['ttl']:
            return member

        
def parse_property(prop):
    syntax = '{} = None'
    name = prop['ttl'].split('Property')[0].strip()
    return syntax.format(name)


def parse_method(method):
    bypass = ['@']
    
    syntax = []

    method_name = method['ttl'].split()[0].split('.')[-1].strip()
    for c in bypass:
        if c in method_name:
            return ''
    
    def_line = 'def {}(self):'.format(method_name)
    syntax.append(def_line)

    # docstring
    docstring = []
    docstring.append('"""')
    # if has overloads
    if method['children']:
        # parse OVERLOADS
        for overload in method['children']:
            overload_docstring = []
            soup = get_detail_page(overload['id'])

            overload_name = overload['ttl'].split('Method')[0].strip()
            if soup.select_one('.codeblock'):
                return_type = soup.select_one('.codeblock').text.splitlines()[-1].split()[-1]
            else:
                return_type = ''
            overload_line = '{} -> {}'.format(overload_name, return_type)
            overload_docstring.append(overload_line)

            parameters = []
            for tr in soup.select('table tr')[1:]:
                if not tr.select('td'):
                    continue
                p_name = tr.select('td')[0]
                p_desc = tr.select('td')[1]
                parameters.append({
                    'name': p_name.text,
                    'description': p_desc.text
                })
            parameter_lines = '\n'.join('{}: {}'.format(p['name'], p['description']) for p in parameters)
            overload_docstring.append(indent(parameter_lines))
            docstring.append('\n'.join(overload_docstring))
    else:
        soup = get_detail_page(method['id'])
        if soup.select_one('.codeblock'):
            return_type = soup.select_one('.codeblock').text.splitlines()[-1].split()[-1]
        else:
            return_type = ''
        overload_line = '{} -> {}'.format(method_name, return_type)
        docstring.append(overload_line)

        parameters = []
        for tr in soup.select('table tr')[1:]:
            if not tr.select('td'):
                continue
            p_name = tr.select('td')[0]
            p_desc = tr.select('td')[1]
            parameters.append({
                'name': p_name.text,
                'description': p_desc.text
            })
        parameter_lines = '\n'.join('{}: {}'.format(p['name'], p['description']) for p in parameters)
        docstring.append(indent(parameter_lines))

    docstring.append('"""')
    
    syntax.append(indent('\n'.join(docstring)))

    syntax.append(indent('pass'))

    return '\n'.join(syntax)


def parse_enum(enum):
    soup = get_detail_page(enum['id'])
    syntax = []   
    cs_block = soup.select('.codeblock')[-1]

    if cs_block:
        syntax.append('\n'.join(line.strip(',') for line in cs_block.text.splitlines()[1:-1]))
        
    return '\n'.join(syntax)


def get_class_parent(cls):
    soup = get_detail_page(cls['id'])
    cs = soup.select('.codeblock')[-1]
    if cs.text and cs.text.split(':')[-1]:
        return cs.text.split(':')[-1].strip('; ')
    return 'object'


def get_constructor_docstring(constructor):
    syntax = []
    # has overloads
    if constructor['children']:
        for overload in constructor['children']:
            soup = get_detail_page(overload['id'])
            name = overload['ttl'].split('Constructor')[0].strip()
            parameters = []
            for tr in soup.select('table tr')[1:]:
                if not tr.select('td'):
                    continue
                p_name = tr.select('td')[0]
                p_desc = tr.select('td')[1]
                parameters.append({
                    'name': p_name.text.strip(),
                    'description': p_desc.text.strip()
                })
            if parameters:
                syntax.append(name)
                syntax.append(
                    indent(
                        '\n'.join('{} : {}'.format(p['name'], p['description']) for p in parameters)
                    )
                )
            else:
                syntax.append('{}()'.format(name))
            syntax.append('\n')
    else:
        soup = get_detail_page(constructor['id'])
        name = constructor['ttl'].split('Constructor')[0].strip()
        parameters = []
        for tr in soup.select('table tr')[1:]:
            if not tr.select('td'):
                continue
            p_name = tr.select('td')[0]
            p_desc = tr.select('td')[1]
            parameters.append({
                'name': p_name.text.strip(),
                'description': p_desc.text.strip()
            })
        if parameters:
            syntax.append(name)
            syntax.append(
                indent(
                    '\n'.join('{} : {}'.format(p['name'], p['description']) for p in parameters)
                )
            )
        else:
            syntax.append('{}()'.format(name))

    return '\n'.join(syntax)
    
    
def get_class_docstring(cls):
    soup = get_detail_page(cls['id'])
    
    # Description
    description = soup.select_one('#mainBody>p')
    if description:
        description = description.text.strip()
    else:
        description = ''
    # Constructors
    constructor = get_child(cls, 'Constructor')
    if constructor:
        constructor_docstring = get_constructor_docstring(constructor)
    else:
        constructor_docstring = ''
        
    ### build docstring
    docstring = []
    docstring.append('"""')
    docstring.append(description)
    if constructor_docstring:
        docstring.append('\n\n'.join(constructor_docstring).strip())
    docstring.append('"""')
    
    return '\n'.join(docstring)


def parse_class(cls):
    syntax = []
    
    # def_line    
    name = cls['ttl'].split()[0].split('.')[-1].strip()
    if '<' in name:
        name = name.split('<')[0]
    elif '(' in name:
        name = name.split('(')[0]
    parent = get_class_parent(cls)
    def_line = 'class {}({}):'.format(name, parent)
    syntax.append(def_line)
    
    # docstring
    docstring = get_class_docstring(cls)
    syntax.append(indent(docstring))
    
    # children
    syntax.append(
        indent(parse_children(cls))
    )
            
    syntax.append(indent('pass'))

    return '\n'.join(syntax)


def parse_children(parent):
    singulars = ('Class', 'Enumeration', 'Structure', 'Interface', 'Type', 'Method', 'Field', 'Property')
    plurals =  ('Classes', 'Enumerations', 'Structures', 'Methods', 'Fields', 'Properties')
    syntax = []
    for child in parent['children']:
        ctype = child['ttl'].split()[-1]
        if ctype in plurals:
            syntax.append(
                parse_children(child)
            )
        elif ctype in singulars:
            syntax.append(
                parse_child(child)
            )
            syntax.append('\n')
            
    return '\n'.join(syntax)

            
def parse_child(child):
    parser_map = {
        'Class': parse_class,
        'Enumeration': parse_enum,
        'Structure': parse_class,
        'Interface': parse_class,
        'Type': parse_method,
        'Method': parse_method,
        'Field': parse_property,
        'Property': parse_property
    }
    
    name = child['ttl'].split()[-1]
    parser = parser_map[name]
    
    return parser(child)


def get_namespaces(json_url):
    r = requests.Session().get(json_url)
    for child in r.json()['books']:
        if 'ObjectARX: Managed .NET Reference Guide' in child['ttl']:
            return [c for c in child['children'] if 'Namespace' in c['ttl']]


def main():
    namespaces = get_namespaces('https://help.autodesk.com/view/OARX/2020/ENU/data/toctree.json')
    for ns in namespaces:
        name = ns['ttl'].split()[0]
        print('*'*80)
        print(name)
        folder_path = name.replace('.', '/')
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        results = []
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_result = {executor.submit(parse_child, child): child['ttl'] for child in ns['children']}
            for future in as_completed(future_result):
                print('Done {}'.format(future_result[future]))
                cls_name = future_result[future].split()[0]
                content = future.result()
                results.append({
                    'name': cls_name,
                    'content': content
                })

        results.sort(key=lambda x:x['name'])

        with open(os.path.join(folder_path, '__init__.py'), 'w') as f:
            f.write('\n\n'.join(r['content'] for r in results))
            
            
if __name__ == '__main__':
    main()