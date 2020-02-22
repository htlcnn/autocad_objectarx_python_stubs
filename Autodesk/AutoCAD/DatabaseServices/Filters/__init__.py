class Filter(object):
    """
    
    """
    IndexClass = None
    
    pass

class FilteredBlockIterator(object):
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

class Index(object):
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

class IndexUpdateData(object):
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

class LayerFilter(object):
    """
    
    LayerFilter()
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

class LayerIndex(object):
    """
    
    LayerIndex()
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

class SpatialFilter(object):
    """
    
    SpatialFilter()
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

class SpatialFilterDefinition(object):
    """
    
    SpatialFilterDefinition
        Point2dCollection pts : Input boundary definition. If the number of points is 2, they are diagonal points of a rectangle. Otherwise, they are vertices of a polygon. The polygon should be non self intersecting.
        Vector3d normal : Input positive extrusion direction vector
        double elevation : Input elevation; along with the normal, this will define an ECS in which the polygon points are defined
        double frontClip : Input front clip distance in the positive extrusion direction
        double backClip : Input back clip distance in the negative extrusion direction
        [MarshalAs(UnmanagedType.U1)] bool enabled : Input Boolean to make the clip volume effective, or alternatively, be all of 3D space
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

class SpatialFilterVolume(object):
    """
    
    SpatialFilterVolume
        Point3d fromPoint : Input the transformed clip boundary "from" point
        Point3d toPoint : Input the transformed clip boundary "to" point
        Vector3d upDir : Input the transformed clip boundary normal vector
        Vector2d viewField : Input the transformed clip boundary's view field vector
    """
    FromPoint = None
    
    
    ToPoint = None
    
    
    UpDirection = None
    
    
    ViewField = None
    
    pass

class SpatialIndex(object):
    """
    
    SpatialIndex()
    """

    pass