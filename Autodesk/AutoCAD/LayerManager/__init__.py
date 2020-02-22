class AndExpression(object):
    """
    
    """
    def GetRelationalExpressions(self):
        """
        GetRelationalExpressions -> RelationalExpression()
        
        """
        pass
    
    pass

class LayerCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ObjectId value: 
            Input object to add.
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ObjectId value: 
            Input object to be matched with this object.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectId[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index from which the array objects will be copied.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            ObjectId value: 
            Input object to be removed.
        """
        pass
    
    
    Count = None
    
    pass

class LayerFilter(object):
    """
    
    LayerFilter()
    """
    class DialogResult():
        OK = None
        Cancel = None
        UseDefault = None
    
    
    def CompareTo(self):
        """
        CompareTo -> bool
            
            LayerFilter otherFilter: 
            Input object to compare against
        """
        pass
    
    
    def Filter(self):
        """
        Filter -> bool
            
            LayerTableRecord layer: 
            Input object on which the decision is going to be made.
        """
        pass
    
    
    def GenerateNested(self):
        """
        GenerateNested -> void
        
        """
        pass
    
    
    def GetFilterExpressionTree(self):
        """
        GetFilterExpressionTree -> AndExpression()
        
        """
        pass
    
    
    def ShowEditor(self):
        """
        ShowEditor -> DialogResult
        
        """
        pass
    
    
    AllowDelete = None
    
    
    AllowNested = None
    
    
    AllowRename = None
    
    
    DisplayImages = None
    
    
    DynamicallyGenerated = None
    
    
    FilterExpression = None
    
    
    IsIdFilter = None
    
    
    IsProxy = None
    
    
    Name = None
    
    
    NestedFilters = None
    
    
    Parent = None
    
    pass

class LayerFilterCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            LayerFilter value: 
            Input object to be added.
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            LayerFilter value: 
            Input Autodesk.AutoCAD.LayerManager.LayerFilter object that matches to this collection object.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            LayerFilter[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index from which the array object will be copied.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            LayerFilter value: 
            Input object to be removed.
        """
        pass
    
    
    Count = None
    
    pass

class LayerFilterDisplayImages(object):
    """
    
    LayerFilterDisplayImages
        IntPtr imageListHandle : Input.
        int imageIndex : Input.
        int selectedImageIndex : Input.
    """
    ImageIndex = None
    
    
    ImageListHandle = None
    
    
    SelectedImageIndex = None
    
    pass

class LayerFilterTree(object):
    """
    
    LayerFilterTree
        LayerFilter root : Input root of tree
        LayerFilter current : Input current node
    """
    Current = None
    
    
    Root = None
    
    pass

class LayerGroup(object):
    """
    
    LayerGroup()
    """
    LayerIds = None
    
    pass

class RelationalExpression(object):
    """
    
    """
    Constant = None
    
    
    Variable = None
    
    pass