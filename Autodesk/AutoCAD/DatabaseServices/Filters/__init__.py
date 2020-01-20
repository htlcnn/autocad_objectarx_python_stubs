class Filter(DBObject):
    """
    
    """
    IndexClass = None
    
    pass

class FilteredBlockIterator(DisposableWrapper):
    """
    
    """
    def Accepts(self):
        """
        Accepts -> bool
            
            ObjectId id: 
            Object ID that is being composed, typically output of a previous iterator's Accepts() method or Id property
        """
        pass
    
    
    def AddToBuffer(self):
        """
        AddToBuffer -> void
            
            ObjectId id: 
            Object ID that is being composed, typically output of a previous iterator's Accepts() method or Id property
        """
        pass
    
    
    def Seek(self):
        """
        Seek -> void
            
            ObjectId id: ObjectId to seek to
        """
        pass
    
    
    def Start(self):
        """
        Start -> void
        
        """
        pass
    
    
    BuffersForComposition = None
    
    
    EstimatedHitFraction = None
    
    
    Id = None
    
    
    Next = None
    
    pass

class Index(DBObject):
    """
    
    """
    def GetIterator(self):
        """
        GetIterator -> FilteredBlockIterator
            
            Autodesk.AutoCAD.DatabaseServices.Filters.Filter filter: 
            Input filter (query) to be applied to the index for the iterator based traversal
        """
        pass
    
    
    def RebuildFull(self):
        """
        RebuildFull -> void
            
            IndexUpdateData indexData: 
            Input IndexUpdateData object for use during the index rebuild
        """
        pass
    
    
    IsUptoDate = None
    
    
    LastUpdatedAt = None
    
    
    LastUpdatedAtU = None
    
    
    ObjectBeingIndexedId = None
    
    pass

class IndexUpdateData(DisposableWrapper):
    """
    
    """
    def AddId(self):
        """
        AddId -> void
            
            ObjectId id: 
            Object ID for which mapping data or flag data will be added later
        """
        pass
    
    
    def GetIdData(self):
        """
        GetIdData -> long
            
            ObjectId id: 
            Object ID that data is associated with
        """
        pass
    
    
    def GetIdDataPtr(self):
        """
        GetIdDataPtr -> IntPtr
            
            ObjectId id: 
            Object ID that data is associated with
        """
        pass
    
    
    def GetIdFlags(self):
        """
        GetIdFlags -> byte
            
            ObjectId id: 
            Object ID that flags is associated with
        """
        pass
    
    
    def SetIdData(self):
        """
        SetIdData(ObjectId, IntPtr) -> void
            
            ObjectId id: 
            Object ID that data is associated with
            
            IntPtr data: 
            32-bit data value associated with id
        SetIdData(ObjectId, int) -> void
            
            ObjectId id: 
            Object ID that data is associated with
            
            int data: 
            32-bit data value associated with id
        """
        pass
    
    
    def SetIdFlags(self):
        """
        SetIdFlags -> void
            
            ObjectId id: 
            Object ID that flags is associated with
            
            byte flags: 
            8-bit flag value associated with id
        """
        pass
    
    pass

class LayerFilter(Autodesk.AutoCAD.DatabaseServices.Filters.Filter):
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
    def Add(self):
        """
        Add -> void
            
            string layer: 
            Input layer name to add
        """
        pass
    
    
    def GetAt(self):
        """
        GetAt -> void
            
            int index: 
            Input index of layer to get
            
            string name: 
            Input name of layer at index index
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            string layer: 
            Input layer name to remove
        """
        pass
    
    
    IsValid = None
    
    
    LayerCount = None
    
    pass

class LayerIndex(Index):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    I
    
    n
    
    d
    
    e
    
    x
    
    (
    
    )
    """
    def Compute(self):
        """
        Compute -> void
            
            LayerTable pLT: 
            Input layer table of the Database
            
            BlockTableRecord record: 
            Input block table record for which the filter should be generated
        """
        pass
    
    pass

class SpatialFilter(Autodesk.AutoCAD.DatabaseServices.Filters.Filter):
    """
    
    S
    
    p
    
    a
    
    t
    
    i
    
    a
    
    l
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
    (
    
    )
    """
    def ClipVolumeIntersectsExtents(self):
        """
        ClipVolumeIntersectsExtents -> bool
            
            Extents3d ext: 
            Input extents
        """
        pass
    
    
    def GetQueryBounds(self):
        """
        GetQueryBounds() -> Extents3d
        
        GetQueryBounds(BlockReference) -> Extents3d
            
            BlockReference blockReference: 
            Deprecated
        """
        pass
    
    
    def GetVolume(self):
        """
        GetVolume -> SpatialFilterVolume
        
        """
        pass
    
    
    def SetPerspectiveCamera(self):
        """
        SetPerspectiveCamera -> void
            
            Point3d fromPoint: 
            Input new base point for the camera
        """
        pass
    
    
    ClipSpaceToWorldCoordinateSystemTransform = None
    
    
    Definition = None
    
    
    HasPerspectiveCamera = None
    
    
    Inverted = None
    
    
    OriginalInverseBlockTransform = None
    
    pass

class SpatialFilterDefinition(public struct SpatialFilterDefinition {
}):
    """
    
    S
    
    p
    
    a
    
    t
    
    i
    
    a
    
    l
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
    D
    
    e
    
    f
    
    i
    
    n
    
    i
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
     
    
    d
    
    e
    
    f
    
    i
    
    n
    
    i
    
    t
    
    i
    
    o
    
    n
    
    .
    
     
    
    I
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    i
    
    s
    
     
    
    2
    
    ,
    
     
    
    t
    
    h
    
    e
    
    y
    
     
    
    a
    
    r
    
    e
    
     
    
    d
    
    i
    
    a
    
    g
    
    o
    
    n
    
    a
    
    l
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    o
    
    f
    
     
    
    a
    
     
    
    r
    
    e
    
    c
    
    t
    
    a
    
    n
    
    g
    
    l
    
    e
    
    .
    
     
    
    O
    
    t
    
    h
    
    e
    
    r
    
    w
    
    i
    
    s
    
    e
    
    ,
    
     
    
    t
    
    h
    
    e
    
    y
    
     
    
    a
    
    r
    
    e
    
     
    
    v
    
    e
    
    r
    
    t
    
    i
    
    c
    
    e
    
    s
    
     
    
    o
    
    f
    
     
    
    a
    
     
    
    p
    
    o
    
    l
    
    y
    
    g
    
    o
    
    n
    
    .
    
     
    
    T
    
    h
    
    e
    
     
    
    p
    
    o
    
    l
    
    y
    
    g
    
    o
    
    n
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    b
    
    e
    
     
    
    n
    
    o
    
    n
    
     
    
    s
    
    e
    
    l
    
    f
    
     
    
    i
    
    n
    
    t
    
    e
    
    r
    
    s
    
    e
    
    c
    
    t
    
    i
    
    n
    
    g
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    v
    
    e
    
     
    
    e
    
    x
    
    t
    
    r
    
    u
    
    s
    
    i
    
    o
    
    n
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    e
    
    l
    
    e
    
    v
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    l
    
    e
    
    v
    
    a
    
    t
    
    i
    
    o
    
    n
    
    ;
    
     
    
    a
    
    l
    
    o
    
    n
    
    g
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
    ,
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    d
    
    e
    
    f
    
    i
    
    n
    
    e
    
     
    
    a
    
    n
    
     
    
    E
    
    C
    
    S
    
     
    
    i
    
    n
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    l
    
    y
    
    g
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    a
    
    r
    
    e
    
     
    
    d
    
    e
    
    f
    
    i
    
    n
    
    e
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    f
    
    r
    
    o
    
    n
    
    t
    
    C
    
    l
    
    i
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    r
    
    o
    
    n
    
    t
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    d
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    v
    
    e
    
     
    
    e
    
    x
    
    t
    
    r
    
    u
    
    s
    
    i
    
    o
    
    n
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    b
    
    a
    
    c
    
    k
    
    C
    
    l
    
    i
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    b
    
    a
    
    c
    
    k
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    d
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    g
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    e
    
    x
    
    t
    
    r
    
    u
    
    s
    
    i
    
    o
    
    n
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    [
    
    M
    
    a
    
    r
    
    s
    
    h
    
    a
    
    l
    
    A
    
    s
    
    (
    
    U
    
    n
    
    m
    
    a
    
    n
    
    a
    
    g
    
    e
    
    d
    
    T
    
    y
    
    p
    
    e
    
    .
    
    U
    
    1
    
    )
    
    ]
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    e
    
    n
    
    a
    
    b
    
    l
    
    e
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    B
    
    o
    
    o
    
    l
    
    e
    
    a
    
    n
    
     
    
    t
    
    o
    
     
    
    m
    
    a
    
    k
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    v
    
    o
    
    l
    
    u
    
    m
    
    e
    
     
    
    e
    
    f
    
    f
    
    e
    
    c
    
    t
    
    i
    
    v
    
    e
    
    ,
    
     
    
    o
    
    r
    
     
    
    a
    
    l
    
    t
    
    e
    
    r
    
    n
    
    a
    
    t
    
    i
    
    v
    
    e
    
    l
    
    y
    
    ,
    
     
    
    b
    
    e
    
     
    
    a
    
    l
    
    l
    
     
    
    o
    
    f
    
     
    
    3
    
    D
    
     
    
    s
    
    p
    
    a
    
    c
    
    e
    """
    def GetPoints(self):
        """
        GetPoints -> Point2dCollection
        
        """
        pass
    
    
    BackClip = None
    
    
    Elevation = None
    
    
    Enabled = None
    
    
    FrontClip = None
    
    
    Normal = None
    
    pass

class SpatialFilterVolume(public struct SpatialFilterVolume {
}):
    """
    
    S
    
    p
    
    a
    
    t
    
    i
    
    a
    
    l
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
    V
    
    o
    
    l
    
    u
    
    m
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    f
    
    r
    
    o
    
    m
    
    P
    
    o
    
    i
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    f
    
    o
    
    r
    
    m
    
    e
    
    d
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
     
    
    "
    
    f
    
    r
    
    o
    
    m
    
    "
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    t
    
    o
    
    P
    
    o
    
    i
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    f
    
    o
    
    r
    
    m
    
    e
    
    d
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
     
    
    "
    
    t
    
    o
    
    "
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    u
    
    p
    
    D
    
    i
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    f
    
    o
    
    r
    
    m
    
    e
    
    d
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    2
    
    d
    
     
    
    v
    
    i
    
    e
    
    w
    
    F
    
    i
    
    e
    
    l
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    f
    
    o
    
    r
    
    m
    
    e
    
    d
    
     
    
    c
    
    l
    
    i
    
    p
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
    '
    
    s
    
     
    
    v
    
    i
    
    e
    
    w
    
     
    
    f
    
    i
    
    e
    
    l
    
    d
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    """
    FromPoint = None
    
    
    ToPoint = None
    
    
    UpDirection = None
    
    
    ViewField = None
    
    pass

class SpatialIndex(Index):
    """
    
    S
    
    p
    
    a
    
    t
    
    i
    
    a
    
    l
    
    I
    
    n
    
    d
    
    e
    
    x
    
    (
    
    )
    """

    pass