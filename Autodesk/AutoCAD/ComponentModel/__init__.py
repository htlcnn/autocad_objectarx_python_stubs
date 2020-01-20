class IPropertyProvider(public interface IPropertyProvider):
    """
    
    """
    def GetProperties(self):
        """
        GetProperties -> PropertyDescriptorCollection
            
            object instance: 
            Input the instance to retrieve from
        """
        pass
    
    pass

class ITypeDescriptor(ITypeDescriptor td = TypeManager.Instance[typeof(Circle)]):
    """
    
    """
    def AddPerInstancePropertyProvider(self):
        """
        AddPerInstancePropertyProvider -> void
            
            IPropertyProvider pp: 
            Input item to obtain properties from
        """
        pass
    
    
    def AddProperty(self):
        """
        AddProperty -> void
            
            PropertyDescriptor prop: 
            Input the property descriptor.
        """
        pass
    
    
    def GetPerInstancePropertyProviders(self):
        """
        GetPerInstancePropertyProviders -> ReadOnlyCollection<IPropertyProvider>
        
        """
        pass
    
    
    def ModifyPropertyCollection(self):
        """
        ModifyPropertyCollection -> PropertyDescriptorCollection
            
            PropertyDescriptorCollection defaultProps: 
            Input default properties.
            
            object instance: 
            Input instance of object.
        """
        pass
    
    
    def RemovePerInstancePropertyProvider(self):
        """
        RemovePerInstancePropertyProvider -> void
            
            IPropertyProvider pp: 
            Input per-instance property to remove
        """
        pass
    
    
    def RemoveProperty(self):
        """
        RemoveProperty -> void
            
            PropertyDescriptor prop: 
            Input property to remove
        """
        pass
    
    
    HasPerInstance = None
    
    pass

class PropertyDescriptorBase(PropertyDescriptor):
    """
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    D
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    o
    
    r
    
    B
    
    a
    
    s
    
    e
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    D
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    o
    
    r
    
    B
    
    a
    
    s
    
    e
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    [
    
    ]
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    [
    
    ]
    
     
    
    a
    
    t
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
    n
    
     
    
    a
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    """
    def CanResetValue(self):
        """
        CanResetValue -> bool
            
            object component: 
            Input the component to check
        """
        pass
    
    
    def ResetValue(self):
        """
        ResetValue -> void
            
            object component: 
            Input the component to reset
        """
        pass
    
    
    def ShouldSerializeValue(self):
        """
        ShouldSerializeValue -> bool
            
            object component: 
            Input the component to serialize
        """
        pass
    
    
    ComponentType = None
    
    
    DisplayName = None
    
    
    IsReadOnly = None
    
    
     = None
    
    pass

class PropertyProviderAttribute(Attribute):
    """
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    P
    
    r
    
    o
    
    v
    
    i
    
    d
    
    e
    
    r
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    y
    
    p
    
    e
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    o
    
    f
    
     
    
    a
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    """
     = None
    
    pass

class TypeDescriptionProvider([TypeDescriptionProviderAttribute(typeof(TypeDescriptionProvider))] class MyClass { ...):
    """
    
    """
    def GetTypeDescriptor(self):
        """
        GetTypeDescriptor -> ICustomTypeDescriptor
            
            Type objectType: 
            Input type to check
            
            object instance: 
            Input the instance which owns this object
        """
        pass
    
    pass

class TypeDescriptor(ITypeDescriptor td = TypeManager.Instance[typeof(Circle)]):
    """
    
    T
    
    y
    
    p
    
    e
    
    D
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    y
    
    p
    
    e
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    o
    
    f
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    o
    
    r
    """
    def AddPerInstancePropertyProvider(self):
        """
        AddPerInstancePropertyProvider -> void
            
            IPropertyProvider pp: 
            Input provider to add
        """
        pass
    
    
    def AddProperty(self):
        """
        AddProperty -> void
            
            PropertyDescriptor prop: 
            New property to add
        """
        pass
    
    
    def GetPerInstancePropertyProviders(self):
        """
        GetPerInstancePropertyProviders -> ReadOnlyCollection<IPropertyProvider>
        
        """
        pass
    
    
    def ModifyPropertyCollection(self):
        """
        ModifyPropertyCollection -> PropertyDescriptorCollection
            
            PropertyDescriptorCollection defaultProps: 
            Input default properties
            
            object instance: 
            Input instance of object
        """
        pass
    
    
    def RemovePerInstancePropertyProvider(self):
        """
        RemovePerInstancePropertyProvider -> void
            
            IPropertyProvider pp: 
            Input per instance property provider to remove
        """
        pass
    
    
    def RemoveProperty(self):
        """
        RemoveProperty -> void
            
            PropertyDescriptor prop: 
            Input property to remove
        """
        pass
    
    
    HasPerInstance = None
    
    pass

class TypeManager(public class TypeManager):
    """
    
    T
    
    y
    
    p
    
    e
    
    M
    
    a
    
    n
    
    a
    
    g
    
    e
    
    r
    
    (
    
    )
    """
    Instance = None
    
    pass