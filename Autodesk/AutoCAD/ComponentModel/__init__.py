class IPropertyProvider(object):
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

class ITypeDescriptor(object):
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

class PropertyDescriptorBase(object):
    """
    
    PropertyDescriptorBase(string)
        string name : Input name
    
    
    PropertyDescriptorBase(string, Attribute[])
        string name : Input name
        Attribute[] att : Input an attribute
    
    
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

class PropertyProviderAttribute(object):
    """
    
    PropertyProviderAttribute
        Type type : Input type of attribute
    """
     = None
    
    pass

class TypeDescriptionProvider(object):
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

class TypeDescriptor(object):
    """
    
    TypeDescriptor
        Type type : Input type of descriptor
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

class TypeManager(object):
    """
    
    TypeManager()
    """
    Instance = None
    
    pass