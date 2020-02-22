class BoundaryLoop(object):
    """
    
    BoundaryLoop
        FullSubentityPath fullPath : Input path to construct loop from
    """
    def GetEdgesStartingFrom(self):
        """
        GetEdgesStartingFrom -> LoopEdgeCollection
            
            Edge startFrom: 
            Input edge to start collecting from
        """
        pass
    
    
    Edges = None
    
    
    Face = None
    
    
    LoopType = None
    
    
    Vertices = None
    
    pass

class Brep(object):
    """
    
    Brep(Entity)
        Entity entity : Input entity
    
    
    Brep(FullSubentityPath)
        FullSubentityPath fullPath : Input path to construct brep from
    
    
    """
    def GetComplexsStartingFrom(self):
        """
        GetComplexsStartingFrom -> BrepComplexCollection
            
            Complex startFrom: 
            Input complex to start collecting from
        """
        pass
    
    
    def GetEdgesStartingFrom(self):
        """
        GetEdgesStartingFrom -> BrepEdgeCollection
            
            Edge startFrom: 
            Input edge to start collecting from
        """
        pass
    
    
    def GetShellsStartingFrom(self):
        """
        GetShellsStartingFrom -> BrepShellCollection
            
            Shell startFrom: 
            Input shell to start collecting from
        """
        pass
    
    
    Complexes = None
    
    
    Edges = None
    
    
    Faces = None
    
    
    Shells = None
    
    
    Solid = None
    
    
    Vertices = None
    
    pass

class BrepComplexCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepComplexEnumerator
        
        """
        pass
    
    pass

class BrepComplexEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class BrepEdgeCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepEdgeEnumerator
        
        """
        pass
    
    pass

class BrepEdgeEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class BrepEntity(object):
    """
    
    """
    def CheckEntity(self):
        """
        CheckEntity -> bool
        
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetLineContainment(self):
        """
        GetLineContainment -> Hit()
            
            LinearEntity3d line: 
            Input 3D line
            
            int numHitsWanted: 
            Input maximum number of hits to find
        """
        pass
    
    
    def GetMassProperties(self):
        """
        GetMassProperties() -> MassProperties
        
        GetMassProperties(double) -> MassProperties
            
            double density: 
            Input calculating density
        GetMassProperties(double, double) -> MassProperties
            
            double density: 
            Input calculating density
            
            double tolRequired: 
            Input tolerance needed for the calculation
        GetMassProperties(double, double, out double) -> MassProperties
            
            double density: 
            Input calculating density
            
            double tolRequired: 
            Input tolerance needed for the calculation
            
            out double tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    def GetPerimeterLength(self):
        """
        GetPerimeterLength() -> double
        
        GetPerimeterLength(double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
        GetPerimeterLength(double, out double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
            
            out double tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    def GetPointContainment(self):
        """
        GetPointContainment -> BrepEntity
            
            Point3d point: 
            Input 3D point
            
            out Autodesk.AutoCAD.BoundaryRepresentation.PointContainment containment: 
            Output containment type
        """
        pass
    
    
    def GetSurfaceArea(self):
        """
        GetSurfaceArea() -> double
        
        GetSurfaceArea(double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
        GetSurfaceArea(double, out double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
            
            out double tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    def GetVolume(self):
        """
        GetVolume() -> double
        
        GetVolume(double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
        GetVolume(double, out double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
            
            out double tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    BoundBlock = None
    
    
    Brep = None
    
    
    IsBrepChanged = None
    
    
    IsNull = None
    
    
    SubentityPath = None
    
    
    ValidationLevel = None
    
    pass

class BrepFaceCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepFaceEnumerator
        
        """
        pass
    
    pass

class BrepFaceEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class BrepShellCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepShellEnumerator
        
        """
        pass
    
    pass

class BrepShellEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class BrepVertexCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepVertexEnumerator
        
        """
        pass
    
    pass

class BrepVertexEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class Complex(object):
    """
    
    Complex
        FullSubentityPath fullPath : Input path to construct a complex from
    """
    def GetShellsStartingFrom(self):
        """
        GetShellsStartingFrom -> ComplexShellCollection
            
            Shell startFrom: 
            Input the shell to start collecting from
        """
        pass
    
    
    Shells = None
    
    pass

class ComplexShellCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> ComplexShellEnumerator
        
        """
        pass
    
    pass

class ComplexShellEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class Edge(object):
    """
    
    Edge
        FullSubentityPath fullPath : Input path to construct an edge from
    """
    def GetCurveAsNurb(self):
        """
        GetCurveAsNurb() -> NurbCurve3d
        
        GetCurveAsNurb(double) -> NurbCurve3d
            
            tolRequired: 
            Input tolerance requested for the calculation
        GetCurveAsNurb(double, out double) -> NurbCurve3d
            
            tolRequired: 
            Input tolerance requested for the calculation
            
            tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    def GetLoopsStartingFrom(self):
        """
        GetLoopsStartingFrom -> EdgeLoopCollection
            
            BoundaryLoop startFrom: 
            Input loop to start collecting from
        """
        pass
    
    
    Curve = None
    
    
    IsOrientToCurve = None
    
    
    Loops = None
    
    
    Vertex1 = None
    
    
    Vertex2 = None
    
    pass

class EdgeLoopCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> EdgeLoopEnumerator
        
        """
        pass
    
    pass

class EdgeLoopEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class Element(object):
    """
    
    """

    pass

class Element2d(object):
    """
    
    """
    def GetNodesStartingFrom(self):
        """
        GetNodesStartingFrom -> Element2dNodeCollection
            
            Node startFrom: 
            Input node to start collecting from
        """
        pass
    
    
    Nodes = None
    
    
    Normal = None
    
    pass

class Element2dNodeCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> Element2dNodeEnumerator
        
        """
        pass
    
    pass

class Element2dNodeEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class Element2dShape():
    Default = None
    AllPolygons = None
    AllQuadrilaterals = None
    AllTriangles = None

class EnumeratorBase(object):
    """
    
    """
    def MoveNext(self):
        """
        MoveNext -> bool
        
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    BrepChanged = None
    
    
    IsNull = None
    
    
    ValidationLevel = None
    
    pass

class ErrorStatus():
    AmbiguousOutput = 5
    BrepChanged = 0xbc0
    DegenerateTopology = 0xbcc
    InvalidInput = 3
    InvalidObject = 0x7b
    MissingGeometry = 0x99
    MissingSubentity = 0x89
    NotApplicable = 2
    NotImplementedYet = 1
    NullObjectId = 0x10
    NullObjectPointer = 0x7b
    NullSubentityId = 0x18
    ObjectIdMismatch = 0x23
    Ok = 0
    OutOfMemory = 6
    TopologyMismatch = 0x23
    UninitialisedObject = 0xbcd
    UnsuitableGeometry = 5
    UnsuitableTopology = 0xbc5
    WrongObjectType = 0x22
    WrongSubentityType = 230

class Exception(object):
    """
    
    Exception()()
    
    
    Exception(Autodesk.AutoCAD.BoundaryRepresentation.ErrorStatus)
        Autodesk.AutoCAD.BoundaryRepresentation.ErrorStatus es : Input error status
    
    
    Exception(Autodesk.AutoCAD.BoundaryRepresentation.ErrorStatus, string)
        Autodesk.AutoCAD.BoundaryRepresentation.ErrorStatus es : Input error status
        string message : Input error message
    
    
    """
    def GetObjectData(self):
        """
        GetObjectData -> void
            
            SerializationInfo info: 
            Input serialization info
            
            StreamingContext context: 
            Input context
        """
        pass
    
    
    ErrorStatus = None
    
    pass

class Face(object):
    """
    
    Face
        FullSubentityPath fullPath : Input path to construct a face from
    """
    def GetArea(self):
        """
        GetArea() -> double
        
        GetArea(double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
        GetArea(double, out double) -> double
            
            double tolRequired: 
            Input tolerance requested for the calculation
            
            out double tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    def GetLoopsStartingFrom(self):
        """
        GetLoopsStartingFrom -> FaceLoopCollection
            
            BoundaryLoop startFrom: 
            Input loop to start collecting from
        """
        pass
    
    
    def GetSurfaceAsNurb(self):
        """
        GetSurfaceAsNurb() -> Autodesk.AutoCAD.Geometry.NurbSurface
        
        GetSurfaceAsNurb(double) -> Autodesk.AutoCAD.Geometry.NurbSurface
            
            tolRequired: 
            Input tolerance requested for the calculation
        GetSurfaceAsNurb(double, out double) -> Autodesk.AutoCAD.Geometry.NurbSurface
            
            tolRequired: 
            Input tolerance requested for the calculation
            
            tolAchieved: 
            Output tolerance achieved for the calculation
        """
        pass
    
    
    def GetSurfaceAsTrimmedNurbs(self):
        """
        GetSurfaceAsTrimmedNurbs -> ExternalBoundedSurface()
        
        """
        pass
    
    
    IsOrientToSurface = None
    
    
    Loops = None
    
    
    Shell = None
    
    
    Surface = None
    
    pass

class FaceLoopCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> FaceLoopEnumerator
        
        """
        pass
    
    pass

class FaceLoopEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class Hit(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    EntityAssociated = None
    
    
    EntityEntered = None
    
    
    EntityHit = None
    
    
    IsBrepChanged = None
    
    
    IsNull = None
    
    
    Point = None
    
    
    ValidationLevel = None
    
    pass

class LoopEdgeCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> LoopEdgeEnumerator
        
        """
        pass
    
    pass

class LoopEdgeEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class LoopType():
    LoopUnclassified = None
    LoopExterior = None
    LoopInterior = None
    LoopWinding = None

class LoopVertexCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> LoopVertexEnumerator
        
        """
        pass
    
    pass

class LoopVertexEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class MassProperties(object):
    """
    
    """
    Centroid = None
    
    
    Mass = None
    
    
    MomentsOfIntertia = None
    
    
    PrincipalMoments = None
    
    
    ProductsOfIntertia = None
    
    
    RadiiOfGyration = None
    
    
    Volume = None
    
    pass

class Mesh(object):
    """
    
    """

    pass

class Mesh2d(object):
    """
    
    Mesh2d
        Mesh2dFilter meshFilter : Input a mesh filter
    """
    def GetElement2dsStartingFrom(self):
        """
        GetElement2dsStartingFrom -> Mesh2dElement2dCollection
            
            Element2d startFrom: 
            Input element2d to start collecting from
        """
        pass
    
    
    Element2ds = None
    
    pass

class Mesh2dControl(object):
    """
    
    """
    ElementShape = None
    
    
    MaxAspectRatio = None
    
    pass

class Mesh2dElement2dCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> Mesh2dElement2dEnumerator
        
        """
        pass
    
    pass

class Mesh2dElement2dEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class Mesh2dFilter(object):
    """
    
    """
    def Insert(self):
        """
        Insert -> void
            
            BrepEntity brepEntity: 
            Input topology to associate with
            
            Mesh2dControl meshControl: 
            Input mesh 2d control
        """
        pass
    
    pass

class MeshControl(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    AngleTolerance = None
    
    
    DistanceTolerance = None
    
    
    MaxNodeSpacing = None
    
    
    MaxSubdivisions = None
    
    pass

class MeshEntity(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    EntityAssociated = None
    
    
    IsBrepChanged = None
    
    
    IsNull = None
    
    
    ValidationLevel = None
    
    pass

class Node(object):
    """
    
    """
    Point = None
    
    pass

class PointContainment():
    Inside = None
    Outside = None
    OnBoundary = None

class Shell(object):
    """
    
    Shell
        FullSubentityPath fullPath : Input path to construct a shell from
    """
    Complex = None
    
    
    Faces = None
    
    
    ShellType = None
    
    pass

class ShellFaceCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> ShellFaceEnumerator
        
        """
        pass
    
    pass

class ShellFaceEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class ShellType():
    ShellUnclassified = None
    ShellExterior = None
    ShellInterior = None

class ValidationLevel():
    FullValidation = None
    NoValidation = None

class Vertex(object):
    """
    
    Vertex
        FullSubentityPath fullPath : Input path to construct a vertex from
    """
    def GetEdgesStartingFrom(self):
        """
        GetEdgesStartingFrom -> VertexEdgeCollection
            
            Edge startFrom: 
            Input edge to start collecting from
        """
        pass
    
    
    def GetLoopsStartingFrom(self):
        """
        GetLoopsStartingFrom -> VertexLoopCollection
            
            BoundaryLoop startFrom: 
            Input loop to start collecting from
        """
        pass
    
    
    Edges = None
    
    
    Loops = None
    
    
    Point = None
    
    pass

class VertexEdgeCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> VertexEdgeEnumerator
        
        """
        pass
    
    pass

class VertexEdgeEnumerator(object):
    """
    
    """
    Current = None
    
    pass

class VertexLoopCollection(object):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> VertexLoopEnumerator
        
        """
        pass
    
    pass

class VertexLoopEnumerator(object):
    """
    
    """
    Current = None
    
    pass