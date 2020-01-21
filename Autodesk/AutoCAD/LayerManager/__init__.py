class AndExpression(public sealed class AndExpression):
    """
    
    """
    def GetRelationalExpressions(self):
        """
        GetRelationalExpressions -> RelationalExpression()
        
        """
        pass
    
    pass

class LayerCollection(ICollection):
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

class LayerFilter(RXObject):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
    (
    
    )
    """
    class DialogResult():
        OK
        Cancel
        UseDefault
    
    
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

class LayerFilterCollection(ICollection):
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

class LayerFilterDisplayImages(public struct LayerFilterDisplayImages {
}):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
    D
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
    I
    
    m
    
    a
    
    g
    
    e
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    n
    
    t
    
    P
    
    t
    
    r
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    L
    
    i
    
    s
    
    t
    
    H
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    s
    
    e
    
    l
    
    e
    
    c
    
    t
    
    e
    
    d
    
    I
    
    m
    
    a
    
    g
    
    e
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
    .
    """
    ImageIndex = None
    
    
    ImageListHandle = None
    
    
    SelectedImageIndex = None
    
    pass

class LayerFilterTree(public struct LayerFilterTree {
}):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
    T
    
    r
    
    e
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    L
    
    a
    
    y
    
    e
    
    r
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
     
    
    r
    
    o
    
    o
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    r
    
    o
    
    o
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    r
    
    e
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    L
    
    a
    
    y
    
    e
    
    r
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
     
    
    c
    
    u
    
    r
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    u
    
    r
    
    r
    
    e
    
    n
    
    t
    
     
    
    n
    
    o
    
    d
    
    e
    """
    Current = None
    
    
    Root = None
    
    pass

class LayerGroup(LayerFilter):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    G
    
    r
    
    o
    
    u
    
    p
    
    (
    
    )
    """
    LayerIds = None
    
    pass

class RelationalExpression(public sealed class RelationalExpression):
    """
    
    """
    Constant = None
    
    
    Variable = None
    
    pass