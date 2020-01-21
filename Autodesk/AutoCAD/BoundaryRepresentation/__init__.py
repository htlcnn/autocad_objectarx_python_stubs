class BoundaryLoop(BrepEntity):
    """
    
    B
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
    L
    
    o
    
    o
    
    p
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    l
    
    o
    
    o
    
    p
    
     
    
    f
    
    r
    
    o
    
    m
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

class Brep(BrepEntity):
    """
    
    B
    
    r
    
    e
    
    p
    
    (
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
     
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    
    
    
    
    
    
    
    
    
    B
    
    r
    
    e
    
    p
    
    (
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    b
    
    r
    
    e
    
    p
    
     
    
    f
    
    r
    
    o
    
    m
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

class BrepComplexCollection(IEnumerable<Complex>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepComplexEnumerator
        
        """
        pass
    
    pass

class BrepComplexEnumerator(EnumeratorBase, IEnumerator<Complex>):
    """
    
    """
    Current = None
    
    pass

class BrepEdgeCollection(IEnumerable<Edge>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepEdgeEnumerator
        
        """
        pass
    
    pass

class BrepEdgeEnumerator(EnumeratorBase, IEnumerator<Edge>):
    """
    
    """
    Current = None
    
    pass

class BrepEntity(RXObject):
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

class BrepFaceCollection(IEnumerable<Face>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepFaceEnumerator
        
        """
        pass
    
    pass

class BrepFaceEnumerator(EnumeratorBase, IEnumerator<Face>):
    """
    
    """
    Current = None
    
    pass

class BrepShellCollection(IEnumerable<Shell>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepShellEnumerator
        
        """
        pass
    
    pass

class BrepShellEnumerator(EnumeratorBase, IEnumerator<Shell>):
    """
    
    """
    Current = None
    
    pass

class BrepVertexCollection(IEnumerable<Vertex>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> BrepVertexEnumerator
        
        """
        pass
    
    pass

class BrepVertexEnumerator(EnumeratorBase, IEnumerator<Vertex>):
    """
    
    """
    Current = None
    
    pass

class Complex(BrepEntity):
    """
    
    C
    
    o
    
    m
    
    p
    
    l
    
    e
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    m
    
    p
    
    l
    
    e
    
    x
    
     
    
    f
    
    r
    
    o
    
    m
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

class ComplexShellCollection(IEnumerable<Shell>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> ComplexShellEnumerator
        
        """
        pass
    
    pass

class ComplexShellEnumerator(EnumeratorBase, IEnumerator<Shell>):
    """
    
    """
    Current = None
    
    pass

class Edge(BrepEntity):
    """
    
    E
    
    d
    
    g
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    a
    
    n
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
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

class EdgeLoopCollection(IEnumerable<BoundaryLoop>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> EdgeLoopEnumerator
        
        """
        pass
    
    pass

class EdgeLoopEnumerator(EnumeratorBase, IEnumerator<BoundaryLoop>):
    """
    
    """
    Current = None
    
    pass

class Element(MeshEntity):
    """
    
    """

    pass

class Element2d(Element):
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

class Element2dNodeCollection(IEnumerable<Node>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> Element2dNodeEnumerator
        
        """
        pass
    
    pass

class Element2dNodeEnumerator(EnumeratorBase, IEnumerator<Node>):
    """
    
    """
    Current = None
    
    pass

class Element2dShape():
    Default
    AllPolygons
    AllQuadrilaterals
    AllTriangles

class EnumeratorBase(RXObject, IEnumerator):
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

class Exception(System.Exception, ISerializable):
    """
    
    E
    
    x
    
    c
    
    e
    
    p
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    x
    
    c
    
    e
    
    p
    
    t
    
    i
    
    o
    
    n
    
    (
    
    A
    
    u
    
    t
    
    o
    
    d
    
    e
    
    s
    
    k
    
    .
    
    A
    
    u
    
    t
    
    o
    
    C
    
    A
    
    D
    
    .
    
    B
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
    R
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    E
    
    r
    
    r
    
    o
    
    r
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    u
    
    t
    
    o
    
    d
    
    e
    
    s
    
    k
    
    .
    
    A
    
    u
    
    t
    
    o
    
    C
    
    A
    
    D
    
    .
    
    B
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
    R
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    E
    
    r
    
    r
    
    o
    
    r
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    r
    
    r
    
    o
    
    r
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
    
    
    
    
    
    
    
    
    
    E
    
    x
    
    c
    
    e
    
    p
    
    t
    
    i
    
    o
    
    n
    
    (
    
    A
    
    u
    
    t
    
    o
    
    d
    
    e
    
    s
    
    k
    
    .
    
    A
    
    u
    
    t
    
    o
    
    C
    
    A
    
    D
    
    .
    
    B
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
    R
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    E
    
    r
    
    r
    
    o
    
    r
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    u
    
    t
    
    o
    
    d
    
    e
    
    s
    
    k
    
    .
    
    A
    
    u
    
    t
    
    o
    
    C
    
    A
    
    D
    
    .
    
    B
    
    o
    
    u
    
    n
    
    d
    
    a
    
    r
    
    y
    
    R
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    E
    
    r
    
    r
    
    o
    
    r
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    r
    
    r
    
    o
    
    r
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    e
    
    s
    
    s
    
    a
    
    g
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    r
    
    r
    
    o
    
    r
    
     
    
    m
    
    e
    
    s
    
    s
    
    a
    
    g
    
    e
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

class Face(BrepEntity):
    """
    
    F
    
    a
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    a
    
     
    
    f
    
    a
    
    c
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
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

class FaceLoopCollection(IEnumerable<BoundaryLoop>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> FaceLoopEnumerator
        
        """
        pass
    
    pass

class FaceLoopEnumerator(EnumeratorBase, IEnumerator<BoundaryLoop>):
    """
    
    """
    Current = None
    
    pass

class Hit(RXObject):
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

class LoopEdgeCollection(IEnumerable<Edge>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> LoopEdgeEnumerator
        
        """
        pass
    
    pass

class LoopEdgeEnumerator(EnumeratorBase, IEnumerator<Edge>):
    """
    
    """
    Current = None
    
    pass

class LoopType():
    LoopUnclassified
    LoopExterior
    LoopInterior
    LoopWinding

class LoopVertexCollection(IEnumerable<Vertex>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> LoopVertexEnumerator
        
        """
        pass
    
    pass

class LoopVertexEnumerator(EnumeratorBase, IEnumerator<Vertex>):
    """
    
    """
    Current = None
    
    pass

class MassProperties(public struct MassProperties {
}):
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

class Mesh(MeshEntity):
    """
    
    """

    pass

class Mesh2d(Mesh):
    """
    
    M
    
    e
    
    s
    
    h
    
    2
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    s
    
    h
    
    2
    
    d
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
     
    
    m
    
    e
    
    s
    
    h
    
    F
    
    i
    
    l
    
    t
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    m
    
    e
    
    s
    
    h
    
     
    
    f
    
    i
    
    l
    
    t
    
    e
    
    r
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

class Mesh2dControl(MeshControl):
    """
    
    """
    ElementShape = None
    
    
    MaxAspectRatio = None
    
    pass

class Mesh2dElement2dCollection(IEnumerable<Element2d>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> Mesh2dElement2dEnumerator
        
        """
        pass
    
    pass

class Mesh2dElement2dEnumerator(EnumeratorBase, IEnumerator<Element2d>):
    """
    
    """
    Current = None
    
    pass

class Mesh2dFilter(DisposableWrapper):
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

class MeshControl(RXObject):
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

class MeshEntity(RXObject):
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

class Node(MeshEntity):
    """
    
    """
    Point = None
    
    pass

class PointContainment():
    Inside
    Outside
    OnBoundary

class Shell(BrepEntity):
    """
    
    S
    
    h
    
    e
    
    l
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    a
    
     
    
    s
    
    h
    
    e
    
    l
    
    l
    
     
    
    f
    
    r
    
    o
    
    m
    """
    Complex = None
    
    
    Faces = None
    
    
    ShellType = None
    
    pass

class ShellFaceCollection(IEnumerable<Face>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> ShellFaceEnumerator
        
        """
        pass
    
    pass

class ShellFaceEnumerator(EnumeratorBase, IEnumerator<Face>):
    """
    
    """
    Current = None
    
    pass

class ShellType():
    ShellUnclassified
    ShellExterior
    ShellInterior

class ValidationLevel():
    FullValidation
    NoValidation

class Vertex(BrepEntity):
    """
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    u
    
    l
    
    l
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    P
    
    a
    
    t
    
    h
    
     
    
    f
    
    u
    
    l
    
    l
    
    P
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
     
    
    a
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    f
    
    r
    
    o
    
    m
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

class VertexEdgeCollection(IEnumerable<Edge>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> VertexEdgeEnumerator
        
        """
        pass
    
    pass

class VertexEdgeEnumerator(EnumeratorBase, IEnumerator<Edge>):
    """
    
    """
    Current = None
    
    pass

class VertexLoopCollection(IEnumerable<BoundaryLoop>):
    """
    
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> VertexLoopEnumerator
        
        """
        pass
    
    pass

class VertexLoopEnumerator(EnumeratorBase, IEnumerator<BoundaryLoop>):
    """
    
    """
    Current = None
    
    pass