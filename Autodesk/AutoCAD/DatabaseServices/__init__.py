class AbstractViewTable(SymbolTable, IEnumerable):
    """
    
    """

    pass

class AbstractViewTableRecord(SymbolTableRecord):
    """
    
    """
    def SetSun(self):
        """
        SetSun -> ObjectId
            
            [CallerMustClose] DBObject sun: 
            Input the sun object.
        """
        pass
    
    
    def SetUcs(self):
        """
        SetUcs(Autodesk.AutoCAD.DatabaseServices.OrthographicView) -> void
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input the object for the UCS view
        SetUcs(ObjectId) -> void
            
            ObjectId id: 
            Input the object which references a UcsTableRecord.
        SetUcs(Point3d, Vector3d, Vector3d) -> void
            
            Point3d origin: 
            Input the object to act as an origin
            
            Vector3d y: 
            Input the object to act as a Y-coordinate
        """
        pass
    
    
    def SetUcsToWorld(self):
        """
        SetUcsToWorld -> void
        
        """
        pass
    
    
    def SetViewDirection(self):
        """
        SetViewDirection -> void
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input the orthographic view
        """
        pass
    
    
    AmbientLightColor = None
    
    
    BackClipDistance = None
    
    
    BackClipEnabled = None
    
    
    Background = None
    
    
    Brightness = None
    
    
    CenterPoint = None
    
    
    Contrast = None
    
    
    DefaultLightingOn = None
    
    
    DefaultLightingType = None
    
    
    Elevation = None
    
    
    FrontClipAtEye = None
    
    
    FrontClipDistance = None
    
    
    FrontClipEnabled = None
    
    
    Height = None
    
    
    LensLength = None
    
    
    PerspectiveEnabled = None
    
    
    SunId = None
    
    
    Target = None
    
    
    ToneOperatorParameters = None
    
    
    Ucs = None
    
    
    UcsName = None
    
    
    UcsOrthographic = None
    
    
    ViewDirection = None
    
    
    ViewOrthographic = None
    
    
    ViewTwist = None
    
    
    VisualStyleId = None
    
    
    Width = None
    
    pass

class ActionsToEvaluateCallback(IDisposable):
    """
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    s
    
    T
    
    o
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
    (
    
    )
    """
    def NeedsToEvaluate(self):
        """
        NeedsToEvaluate -> void
            
            ObjectId objectId: 
            ObjectId of an AssocAction, AssocDependency or an arbitrary DBObject that needs to be evaluated.
            
            AssocStatus newStatus: 
            The new evaluation request status of the action or dependency. If it is not an evaluation request, the needsToEvaluate() implementation should not change the status of the action or dependency.
            
            [MarshalAs(UnmanagedType.U1)] bool ownedActionsAlso: 
            If the action that needs to evaluate is an AssocNetwork, this argument controls whether all the actions owned by the network also need to be evaluated. The caller usually passes true.
        """
        pass
    
    pass

class AlignedDimension(Dimension):
    """
    
    A
    
    l
    
    i
    
    g
    
    n
    
    e
    
    d
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    """
    DimLinePoint = None
    
    
    Oblique = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

  Degrees015 = 1
  Degrees030 = 2
  Degrees045 = 3
  Degrees060 = 4
  Degrees090 = 6
  DegreesAny = 0
  DegreesHorz = 12

class AngularConstraint(ExplicitConstraint):
    """
    
    A
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    A
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    A
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    S
    
    e
    
    c
    
    t
    
    o
    
    r
    
    T
    
    y
    
    p
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    S
    
    e
    
    c
    
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
    
     
    
    S
    
    e
    
    c
    
    t
    
    o
    
    r
    
    T
    
    y
    
    p
    
    e
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    s
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    i
    
    s
    
     
    
    u
    
    s
    
    e
    
    d
    
     
    
    t
    
    o
    
     
    
    m
    
    e
    
    a
    
    s
    
    u
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
    .
    """
      ParallelAntiClockwise
      AntiParallelClockwise
      ParallelClockwise
      AntiParallelAntiClockwise
    
    
    def AngleMultiplier(self):
        """
        AngleMultiplier -> double
        
        """
        pass
    
    
    def SetAngleMultiplier(self):
        """
        SetAngleMultiplier -> void
            
            double multiplier: 
            The angle multiplication factor.
        """
        pass
    
    
    SectorType = None
    
    pass

class AnnotationScale(ObjectContext):
    """
    
    A
    
    n
    
    n
    
    o
    
    t
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    c
    
    a
    
    l
    
    e
    
    (
    
    )
    """
    CollectionName = None
    
    
    DrawingUnits = None
    
    
    IsTemporaryScale = None
    
    
    Name = None
    
    
    PaperUnits = None
    
    
    Scale = None
    
    
    UniqueIdentifier = None
    
    pass

  MText
  FeatureControlFrame
  BlockRef
  NoAnnotation

  True
  False
  NotApplicable

  LoadDisabled = 0x10
  OnAutoCADStartup = 2
  OnCommandInvocation = 4
  OnLoadRequest = 8
  OnProxyDetection = 1
  TransparentlyLoadable = 0x20

class Arc(Curve):
    """
    
    A
    
    r
    
    c
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    A
    
    r
    
    c
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
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
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
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
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    i
    
    n
    
    g
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    e
    
    n
    
    d
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    n
    
    d
    
    i
    
    n
    
    g
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
    
    
    
    
    
    
    A
    
    r
    
    c
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
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
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    i
    
    n
    
    g
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    e
    
    n
    
    d
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    n
    
    d
    
    i
    
    n
    
    g
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
    .
    """
    Center = None
    
    
    EndAngle = None
    
    
    Length = None
    
    
    Normal = None
    
    
    Radius = None
    
    
    StartAngle = None
    
    
    Thickness = None
    
    
    TotalAngle = None
    
    pass

class ArcDimension(Dimension):
    """
    
    A
    
    r
    
    c
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
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
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    c
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    e
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    x
    
    L
    
    i
    
    n
    
    e
    
    1
    
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
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    e
    
    n
    
    d
    
     
    
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
    
     
    
    x
    
    L
    
    i
    
    n
    
    e
    
    2
    
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
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    e
    
    n
    
    d
    
     
    
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
    
     
    
    a
    
    r
    
    c
    
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
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    o
    
    n
    
     
    
    a
    
    r
    
    c
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    e
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    T
    
    e
    
    x
    
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
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
     
    
    t
    
    e
    
    x
    
    t
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    i
    
    n
    
    s
    
    t
    
    e
    
    a
    
    d
    
     
    
    o
    
    f
    
     
    
    c
    
    a
    
    l
    
    c
    
    u
    
    l
    
    a
    
    t
    
    e
    
    d
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    S
    
    t
    
    y
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
     
    
    s
    
    t
    
    y
    
    l
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    I
    
    D
    
    .
    """
    ArcEndParam = None
    
    
    ArcPoint = None
    
    
    ArcStartParam = None
    
    
    ArcSymbolType = None
    
    
    CenterPoint = None
    
    
    HasLeader = None
    
    
    IsPartial = None
    
    
    Leader1Point = None
    
    
    Leader2Point = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

class Assoc2dConstraintCallback(IDisposable):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
    (
    
    )
    """
    def CanBeRelaxed(self):
        """
        CanBeRelaxed -> bool
            
            ExplicitConstraint constraint: 
            The dimension constraint that is to be erased.
        """
        pass
    
    
    def ConstraintDeactivated(self):
        """
        ConstraintDeactivated -> void
            
            ExplicitConstraint constraint: 
            The constraint that is to be activated or deactivated.
            
            [MarshalAs(UnmanagedType.U1)] bool deactivated: 
            Whether to deactivate or reactivate the constraint
        """
        pass
    
    pass

class Assoc2dConstraintGroup(AssocAction):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    l
    
    a
    
    n
    
    e
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    P
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
    l
    
    y
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    d
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
     
    
    D
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    i
    
    s
    
     
    
    P
    
    l
    
    a
    
    n
    
    e
    
    :
    
    :
    
    k
    
    X
    
    Y
    
    P
    
    l
    
    a
    
    n
    
    e
    
    .
    """
      WellDefined
      UnderConstrained
      OverConstrained
      Inconsistent
      NotEvaluated
      NotAvailable
      RejectedByClient
    
    
    def Add3PointAngularConstraint(self):
        """
        Add3PointAngularConstraint -> ThreePointAngleConstraint
            
            ConstrainedPoint consPoint1: 
            Input reference of the first (angle) point which must be a kind of ConstraintPoint
            
            ConstrainedPoint consPoint2: 
            Input reference of the second point which must be a kind of ConstraintPoint
            
            ConstrainedPoint consPoint3: 
            Input reference of the third point which must be a kind of ConstraintPoint
            
            AngularConstraint.AngularSectorType sectorType: 
            Input AngularConstraint::SectorType indicating the angle sector to measure.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
            
            ObjectId dimDependencyId: 
            Input object id of the dimension dependency object.
        """
        pass
    
    
    def AddAngularConstraint(self):
        """
        AddAngularConstraint -> AngularConstraint
            
            ConstrainedLine consLine1: 
            Input reference to ConstrainedLine object
            
            ConstrainedLine consLine2: 
            Input reference to ConstrainedLine object
            
            AngularConstraint.AngularSectorType sectorType: 
            Input AngularConstraint.SectorType indicating the angle sector to measure.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
            
            ObjectId dimDependencyId: 
            Input object id of the dimension dependency object.
        """
        pass
    
    
    def AddConstrainedGeometry(self):
        """
        AddConstrainedGeometry -> ConstrainedGeometry
            
            FullSubentityPath subentPath: 
            Input FullSubentPath of the constrained entity, down to the subentity level. Only SubentityType.Edge and SubentityType.Vertex are valid subent types. The vertex subent must NOT be edge vertex.
        """
        pass
    
    
    def AddDistanceConstraint(self):
        """
        AddDistanceConstraint -> DistanceConstraint
            
            ConstrainedGeometry consGeom1: 
            Input reference to the first ConstrainedGeometry object.
            
            ConstrainedGeometry consGeom2: 
            Input reference to the second ConstrainedGeometry object.
            
            DistanceConstraint.DistanceDirectionType directionType: 
            Input DistanceConstraint::DirectionType indicating the direction type of the distance constraint to be created.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
            
            Vector3d fixedDirection: 
            Input reference to Vector3d indicating the fixed direction of the distance constraint to be created. It will be used only when the directionType is kFixedDirection. Relative to the World Coordinate System.
            
            ConstrainedLine directionLine: 
            Input reference to ConstrainedLine object indicating the relative direction of the distance constraint to be created. It will be used only when the directionType is kPerpendicularToLine or kParallelToLine.
        """
        pass
    
    
    def AddGeometricalConstraint(self):
        """
        AddGeometricalConstraint(GeometricalConstraint.ConstraintType, ConstrainedGeometry[]) -> GeometricalConstraint
            
            GeometricalConstraint.ConstraintType type: 
            Input GeometricalConstraint::GeometricalConstraintType indicating the type of constraint to be created.
            
            ConstrainedGeometry[] consGeoms: 
            Input array of the ConstrainedGeometry.
        AddGeometricalConstraint(GeometricalConstraint.ConstraintType, FullSubentityPath[]) -> GeometricalConstraint
            
            GeometricalConstraint.ConstraintType type: 
            Input GeometricalConstraint::GeometricalConstraintType indicating the type of constraint to be created.
            
            FullSubentityPath[] paths: 
            Input array of the FullSubentPath which can be mapped to ConstrainedGeometry.
        """
        pass
    
    
    def AddGlobalCallback(self):
        """
        AddGlobalCallback -> void
            
            Assoc2dConstraintCallback callback: 
            The callback to be registered.
        """
        pass
    
    
    def AddRadiusDiameterConstraint(self):
        """
        AddRadiusDiameterConstraint -> RadiusDiameterConstraint
            
            ConstrainedGeometry consGeom: 
            Input reference to ConstrainedGeometry object which must be a kind of ConstrainedCircle or ConstrainedEllipse.
            
            RadiusDiameterConstraint.RadDiaConstrType type: 
            Input RadiusDiameterConstraint::RadiusDiameterConstrType indicating the type of constraint to be created.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
        """
        pass
    
    
    def AutoConstrain(self):
        """
        AutoConstrain -> void
            
            FullSubentityPath[] paths: 
            List of subentites which are to be constrained automatically.
            
            Tolerance tol: 
            Tol to define distance tolerance as well as angle tolerance. Tolerance.EqualPoint() defines distance tolerance and Tolerance.EqualVector() defines angle tolerance. Angle tolerance is in radians of angle.
            
            AutoConstrainEvaluationCallback callback: 
            Reference to autoconstraint evaluation callback. This callback will implement constraint priority and priority override.
        """
        pass
    
    
    def ConstraintStatus(self):
        """
        ConstraintStatus -> SolutionStatusType
            
            GeometricalConstraint constraint: 
            Input reference to GeometricalConstraint indicating the constraint object to be checked.
        """
        pass
    
    
    def DeleteConstrainedGeometry(self):
        """
        DeleteConstrainedGeometry -> void
            
            ObjectId geomDependencyId: 
            Input ObjectId of the AssocGeomDependency object.
        """
        pass
    
    
    def DeleteConstraint(self):
        """
        DeleteConstraint -> void
            
            GeometricalConstraint geomConst: 
            Input GeometricalConstraint indicating the constraint to be deleted.
        """
        pass
    
    
    def GeometryMirrored(self):
        """
        GeometryMirrored -> void
            
            AssocGeomDependency geomDependency: 
            Reference to AssocGeomDependency for which implicit point needs to be updated for mirror action.
        """
        pass
    
    
    def GeometryStatus(self):
        """
        GeometryStatus -> SolutionStatusType
            
            ConstrainedGeometry consGeom: 
            Input reference to ConstrainedGeometry indicating the constrained geometry object to be checked.
        """
        pass
    
    
    def GetAllConnectedGeomDependencies(self):
        """
        GetAllConnectedGeomDependencies -> ObjectIdCollection
            
            ObjectIdCollection srcGeomDependencyIds: 
            Input ObjectIdArray indicating the source AssocGeomDependency objects.
        """
        pass
    
    
    def GetConstrainedGeometry(self):
        """
        GetConstrainedGeometry(AssocGeomDependency) -> ConstrainedGeometry
            
            AssocGeomDependency geomDependency: 
            Input reference to AssocGeomDependency of the constrained entity. The AssocGeomDependency object maybe transient, in other words, not added into the database yet.
        GetConstrainedGeometry(AssocGeomDependency, Autodesk.AutoCAD.DatabaseServices.ImplicitPointType, int, [MarshalAs(UnmanagedType.U1)] bool) -> ConstrainedGeometry
            
            AssocGeomDependency geomDependency: 
            Input reference to AssocGeomDependency of the constrained entity. The AssocGeomDependency object maybe transient, in other words, not added into the database yet.
            
            Autodesk.AutoCAD.DatabaseServices.ImplicitPointType ptType: 
            Input reference to ConstrainedImplicitPoint::ImplicitPointType indicating the implicit point type of a constrained curve. Only present when caller want to retrieve the ConstrainedImplicitPoint of a ConstrainedCurve. Default value is NULL.
            
            int defPtIndex: 
            Input integer index of define points of a parametric curve. Currently only control points of a spline are supported. It is only valid when the implicit point type is kDefineImplicit. Default value is -1(invalid index value).
            
            createArcLineMid: 
            Input Boolean indicating if create implicit midpoint of arc or line segment if it is not there. Default value is false.
        GetConstrainedGeometry(FullSubentityPath, [MarshalAs(UnmanagedType.U1)] bool) -> ConstrainedGeometry
            
            [MarshalAs(UnmanagedType.U1)] bool createArcLineMid: 
            Input Boolean indicating if create implicit midpoint of arc or line segment if it is not there. Default value is false.
            
            fullSubentPath: 
            Input FullSubentPath of the constrained entity, down to the subentity level. Only vertex or edge subentity type can be passed in.
        """
        pass
    
    
    def GetGroupNode(self):
        """
        GetGroupNode -> ConstraintGroupNode
            
            uint nodeId: 
            Input ConstraintGroupNodeId indicating the node id.
        """
        pass
    
    
    def GlobalCallback(self):
        """
        GlobalCallback -> Assoc2dConstraintCallback
        
        """
        pass
    
    
    def RegenDimensionSystem(self):
        """
        RegenDimensionSystem -> void
        
        """
        pass
    
    
    def RemoveGlobalCallback(self):
        """
        RemoveGlobalCallback -> void
            
            Assoc2dConstraintCallback callback: 
            The callback to be unregistered.
        """
        pass
    
    
    def SolutionStatus(self):
        """
        SolutionStatus -> SolutionStatusType
            
            [MarshalAs(UnmanagedType.U1)] bool alsoCheckForConstraints: 
            Input boolean indicating if need to check constraints. Default value is true.
        """
        pass
    
    
    def TransformActionBy(self):
        """
        TransformActionBy -> void
            
            Matrix3d transform: 
            The given transformation matrix.
        """
        pass
    
    
    ConstrainedGeometries = None
    
    
    Constraints = None
    
    
    GetDOF = None
    
    
    WorkPlane = None
    
    pass

class AssocAction(DBObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    """
    def AddDependency(self):
        """
        AddDependency -> void
            
            ObjectId dependencyId: 
            ObjectId of the AssocDependency being added to this action.
            
            [MarshalAs(UnmanagedType.U1)] bool setThisActionAsOwningAction: 
            If true, sets this action to be the database owner of the dependency. In this case the dependency must not be already owned by any other action.
        """
        pass
    
    
    def AddMoreObjectsToDeepClone(self):
        """
        AddMoreObjectsToDeepClone -> void
            
            IdMapping idMap: 
            The IdMapping of the current deep cloning session.
            
            ObjectIdCollection additionalObjectsToClone: 
            Additional objects that the action also wants to deep clone. It is legal to add objects that have already been cloned; they will be ignored and not cloned again.
        """
        pass
    
    
    def AreDependenciesEqual(self):
        """
        AreDependenciesEqual -> bool
            
            AssocDependency dependency1: 
            The dependency owned by this action. It needs to be open at least for read.
            
            AssocDependency dependency2: 
            Another dependency. It needs to be open at least for read.
        """
        pass
    
    
    def AreDependenciesOnTheSameThing(self):
        """
        AreDependenciesOnTheSameThing -> bool
            
            AssocDependency dependency1: 
            The dependency owned by this action. It needs to be open at least for read.
            
            AssocDependency dependency2: 
            Another dependency. It needs to be open at least for read.
        """
        pass
    
    
    def DependentObjectCloned(self):
        """
        DependentObjectCloned -> void
            
            AssocDependency dependency: 
            The AssocDependency on the DBObject that has been cloned.
            
            DBObject dbObj: 
            The original object.
            
            DBObject newObj: 
            The newly created clone.
        """
        pass
    
    
    def DragStatus(self):
        """
        DragStatus -> void
            
            Autodesk.AutoCAD.DatabaseServices.DragStatus status: 
            See the DragStatus enum.
        """
        pass
    
    
    def Evaluate(self):
        """
        Evaluate -> void
            
            AssocEvaluationCallback evaluationCallback: 
            While the action is being evaluated, it calls methods of the callback object to inform the client code about the evaluation. The callback reference must not be NULL. See the definition of AssocEvaluationCallback for more details.
        """
        pass
    
    
    def EvaluateDependencies(self):
        """
        EvaluateDependencies -> void
        
        """
        pass
    
    
    def EvaluateDependency(self):
        """
        EvaluateDependency -> void
            
            AssocDependency dependency: 
            The dependency that is to be evaluated. It needs to be open at least for read.
        """
        pass
    
    
    def EvaluationPriority(self):
        """
        EvaluationPriority -> AssocEvaluationPriority
        
        """
        pass
    
    
    def GetActionBody(self):
        """
        GetActionBody -> ObjectId
        
        """
        pass
    
    
    def GetActionsDependentOnObject(self):
        """
        GetActionsDependentOnObject(DBObject, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectIdCollection
            
            DBObject dbObj: 
            The DBObject whose actions are requested. The object needs to be open at least for read.
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Actions that depend-on the object wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Actions that modify the object wanted.
        GetActionsDependentOnObject(DBObject, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, ObjectIdCollection) -> void
        
        """
        pass
    
    
    def GetDependencies(self):
        """
        GetDependencies -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Read-type dependencies wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Write-type dependencies wanted.
        """
        pass
    
    
    def GetDependentActionsToEvaluate(self):
        """
        GetDependentActionsToEvaluate -> void
            
            ActionsToEvaluateCallback actionsToEvaluateCallback: 
            The method uses this callback to report other AssocActions, AssocDependencies and arbitrary DBObjects that should also be scheduled to evaluate when this action is evaluated.
        """
        pass
    
    
    def GetDependentObjects(self):
        """
        GetDependentObjects -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Dependent-on objects wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Modified objects wanted.
        """
        pass
    
    
    def HasDependencyCachedValue(self):
        """
        HasDependencyCachedValue -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether it has cached value. It needs to be open at least for read.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            AssocAction otherAction: 
            The other action needs to be open for read.
        """
        pass
    
    
    def IsExternalDependency(self):
        """
        IsExternalDependency -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether it is external. Needs to be open at least for read.
        """
        pass
    
    
    def IsOwnedDependency(self):
        """
        IsOwnedDependency -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether it is owned by this action. Needs to be open at least for read.
        """
        pass
    
    
    def IsRelevantDependencyChange(self):
        """
        IsRelevantDependencyChange -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether the change in the object it depends on is relevant or not. It needs to be open at least for read.
        """
        pass
    
    
    def ObjectThatOwnsNetworkInstance(self):
        """
        ObjectThatOwnsNetworkInstance -> ObjectId
        
        """
        pass
    
    
    def OwnedDependencyStatusChanged(self):
        """
        OwnedDependencyStatusChanged -> void
            
            AssocDependency ownedDependency: 
            The dependency whose status has just been changed.
            
            AssocStatus previousStatus: 
            Previous status of the dependency.
        """
        pass
    
    
    def PostProcessAfterDeepClone(self):
        """
        PostProcessAfterDeepClone -> void
            
            IdMapping idMap: 
            The IdMapping of the current deep cloning session.
        """
        pass
    
    
    def PostProcessAfterDeepCloneCancel(self):
        """
        PostProcessAfterDeepCloneCancel -> void
            
            IdMapping idMap: 
            The IdMapping of the current deep cloning session.
        """
        pass
    
    
    def RemoveActionsControllingObject(self):
        """
        RemoveActionsControllingObject(ObjectId) -> void
        
        RemoveActionsControllingObject(ObjectId, int) -> void
        
        RemoveActionsControllingObject(ObjectId, int, ObjectId) -> void
        
        """
        pass
    
    
    def RemoveAllDependencies(self):
        """
        RemoveAllDependencies -> void
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseThem: 
            Erase the AssocDependencies after removing them.
        """
        pass
    
    
    def RemoveDependency(self):
        """
        RemoveDependency -> void
            
            ObjectId dependencyId: 
            ObjectId of the AssocDependency being removed from this action.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erases the dependency after removing it.
        """
        pass
    
    
    def SetOwningNetwork(self):
        """
        SetOwningNetwork -> void
            
            ObjectId networkId: 
            The AssocNetwork logically owning this action.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoSetAsDatabaseOwner: 
            Make the network the database owner of this action.
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
            
            AssocStatus newStatus: 
            The new AssocStatus of the action.
            
            [MarshalAs(UnmanagedType.U1)] bool notifyOwningNetwork: 
            If true, and the passed-in status indicates that the action needs to be evaluated, the status of the AssocNetwork owning this dependency is set to the same status (unless the network evaluation status is already more severe than the new one).
            
            [MarshalAs(UnmanagedType.U1)] bool setInOwnedActions: 
            If true, and this action owns some other actions (such as AssocNetwork owns actions), the status is also set in all owned actions (both directly owned and recursively owned).
        """
        pass
    
    
    def TransformActionBy(self):
        """
        TransformActionBy -> void
            
            Matrix3d transform: 
            The provided transformation matrix.
        """
        pass
    
    
    ActionBody = None
    
    
    CurrentEvaluationCallback = None
    
    
    IsActionBodyAProxy = None
    
    
    IsActionEvaluationInProgress = None
    
    
    OwningNetwork = None
    
    
    Status = None
    
    pass

class AssocActionBody(DBObject):
    """
    
    """
    class ValueParam(public struct ValueParam {
    }):
        """
        
        V
        
        a
        
        l
        
        u
        
        e
        
        P
        
        a
        
        r
        
        a
        
        m
        
        (
        
        )
        """
        EvaluatorId = None
        
        
        Expression = None
        
        
        Value = None
        
        pass
    
    
    def AddDependency(self):
        """
        AddDependency -> void
        
        """
        pass
    
    
    def AddMoreObjectsToDeepCloneOverride(self):
        """
        AddMoreObjectsToDeepCloneOverride -> void
        
        """
        pass
    
    
    def AddParam(self):
        """
        AddParam -> void
        
        """
        pass
    
    
    def AreDependenciesEqualOverride(self):
        """
        AreDependenciesEqualOverride -> bool
        
        """
        pass
    
    
    def AreDependenciesOnTheSameThingOverride(self):
        """
        AreDependenciesOnTheSameThingOverride -> bool
        
        """
        pass
    
    
    def CreateActionAndActionBodyAndPostToDatabase(self):
        """
        CreateActionAndActionBodyAndPostToDatabase -> void
        
        """
        pass
    
    
    def currentEvaluationCallback(self):
        """
        currentEvaluationCallback -> AssocEvaluationCallback
        
        """
        pass
    
    
    def DependentObjectClonedOverride(self):
        """
        DependentObjectClonedOverride -> void
        
        """
        pass
    
    
    def DragStatusOverride(self):
        """
        DragStatusOverride -> void
        
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def EvaluateDependencies(self):
        """
        EvaluateDependencies -> void
        
        """
        pass
    
    
    def EvaluateDependencyOverride(self):
        """
        EvaluateDependencyOverride -> bool
        
        """
        pass
    
    
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def EvaluationPriorityOverride(self):
        """
        EvaluationPriorityOverride -> void
        
        """
        pass
    
    
    def GetActionBodiesOnObject(self):
        """
        GetActionBodiesOnObject -> void
        
        """
        pass
    
    
    def GetDependencies(self):
        """
        GetDependencies -> ObjectIdCollection
        
        """
        pass
    
    
    def GetDependenciesOverride(self):
        """
        GetDependenciesOverride -> ObjectIdCollection
        
        """
        pass
    
    
    def GetDependentActionsToEvaluateOverride(self):
        """
        GetDependentActionsToEvaluateOverride -> void
        
        """
        pass
    
    
    def GetDependentObjectsOverride(self):
        """
        GetDependentObjectsOverride -> ObjectIdCollection
        
        """
        pass
    
    
    def GetParentAction(self):
        """
        GetParentAction -> ObjectId
        
        """
        pass
    
    
    def GetValueParam(self):
        """
        GetValueParam(string) -> ValueParam
        
        GetValueParam(string, int) -> ValueParam
        
        """
        pass
    
    
    def GetValueParamArray(self):
        """
        GetValueParamArray -> ValueParam()
        
        """
        pass
    
    
    def GetValueParamUnitType(self):
        """
        GetValueParamUnitType -> Autodesk.AutoCAD.DatabaseServices.UnitType
        
        """
        pass
    
    
    def HasAnyErasedOrBrokenDependencies(self):
        """
        HasAnyErasedOrBrokenDependencies -> bool
        
        """
        pass
    
    
    def HasDependencyCachedValueOverride(self):
        """
        HasDependencyCachedValueOverride -> bool
        
        """
        pass
    
    
    def IsActionEvaluationInProgress(self):
        """
        IsActionEvaluationInProgress -> bool
        
        """
        pass
    
    
    def IsEqualToOverride(self):
        """
        IsEqualToOverride -> bool
        
        """
        pass
    
    
    def IsExternalDependencyOverride(self):
        """
        IsExternalDependencyOverride -> bool
        
        """
        pass
    
    
    def IsOwnedDependencyOverride(self):
        """
        IsOwnedDependencyOverride -> bool
        
        """
        pass
    
    
    def IsRelevantDependencyChangeOverride(self):
        """
        IsRelevantDependencyChangeOverride -> bool
        
        """
        pass
    
    
    def OwnedDependencyStatusChangedOverride(self):
        """
        OwnedDependencyStatusChangedOverride -> void
        
        """
        pass
    
    
    def OwnedValueParamNames(self):
        """
        OwnedValueParamNames -> string()
        
        """
        pass
    
    
    def ParamAtIndex(self):
        """
        ParamAtIndex -> ObjectId
        
        """
        pass
    
    
    def ParamAtName(self):
        """
        ParamAtName(string) -> ObjectId
        
        ParamAtName(string, int) -> ObjectId
        
        """
        pass
    
    
    def ParamsAtName(self):
        """
        ParamsAtName -> ObjectIdCollection
        
        """
        pass
    
    
    def PostProcessAfterDeepCloneCancelOverride(self):
        """
        PostProcessAfterDeepCloneCancelOverride -> void
        
        """
        pass
    
    
    def PostProcessAfterDeepCloneOverride(self):
        """
        PostProcessAfterDeepCloneOverride -> void
        
        """
        pass
    
    
    def RemoveAllDependencies(self):
        """
        RemoveAllDependencies -> void
        
        """
        pass
    
    
    def RemoveAllDependenciesOverride(self):
        """
        RemoveAllDependenciesOverride -> void
        
        """
        pass
    
    
    def RemoveAllParams(self):
        """
        RemoveAllParams -> void
        
        """
        pass
    
    
    def RemoveDependency(self):
        """
        RemoveDependency -> void
        
        """
        pass
    
    
    def RemoveParam(self):
        """
        RemoveParam -> void
        
        """
        pass
    
    
    def RemoveValueParam(self):
        """
        RemoveValueParam -> void
        
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
        
        """
        pass
    
    
    def SetValueParam(self):
        """
        SetValueParam(string, ValueParam, [MarshalAs(UnmanagedType.U1)] bool) -> string
        
        SetValueParam(string, ValueParam, [MarshalAs(UnmanagedType.U1)] bool, int) -> string
        
        """
        pass
    
    
    def SetValueParamArray(self):
        """
        SetValueParamArray -> string()
        
        """
        pass
    
    
    def SetValueParamUnitType(self):
        """
        SetValueParamUnitType -> void
        
        """
        pass
    
    
    def TransformActionByOverride(self):
        """
        TransformActionByOverride -> void
        
        """
        pass
    
    
    def ValueParamInputVariables(self):
        """
        ValueParamInputVariables -> ObjectIdCollection
        
        """
        pass
    
    
    OwnedParams = None
    
    
    OwningNetwork = None
    
    
    ParamCount = None
    
    
    ParentAction = None
    
    
    Status = None
    
    pass

class AssocActionParam(DBObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def DetachDependencies(self):
        """
        DetachDependencies -> void
        
        """
        pass
    
    
    def GetDependencies(self):
        """
        GetDependencies -> ObjectIdCollection
        
        """
        pass
    
    
    def MakeParamConstant(self):
        """
        MakeParamConstant -> void
        
        """
        pass
    
    
    def MakeParamEmpty(self):
        """
        MakeParamEmpty -> void
        
        """
        pass
    
    
    def TransformConstantGeometry(self):
        """
        TransformConstantGeometry -> void
        
        """
        pass
    
    
    Name = None
    
    
    ParentAction = None
    
    pass

class AssocArray(public sealed class AssocArray):
    """
    
    """
    def AddSourceEntity(self):
        """
        AddSourceEntity -> void
        
        """
        pass
    
    
    def CreateArray(self):
        """
        CreateArray -> AssocArray
        
        """
        pass
    
    
    def DeleteItem(self):
        """
        DeleteItem -> void
        
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> ObjectIdCollection
        
        """
        pass
    
    
    def GetAssociativeArray(self):
        """
        GetAssociativeArray -> AssocArray
        
        """
        pass
    
    
    def getItemLocators(self):
        """
        getItemLocators -> ItemLocator()
        
        """
        pass
    
    
    def GetItemTransform(self):
        """
        GetItemTransform -> Matrix3d
        
        """
        pass
    
    
    def GetParameters(self):
        """
        GetParameters -> AssocArrayParameters
        
        """
        pass
    
    
    def IsAssociativeArray(self):
        """
        IsAssociativeArray -> bool
        
        """
        pass
    
    
    def RemoveSourceEntity(self):
        """
        RemoveSourceEntity -> void
        
        """
        pass
    
    
    def ReplaceItems(self):
        """
        ReplaceItems -> void
        
        """
        pass
    
    
    def ResetItems(self):
        """
        ResetItems -> void
        
        """
        pass
    
    
    def TransformItemBy(self):
        """
        TransformItemBy -> void
        
        """
        pass
    
    
    EntityId = None
    
    
    SourceEntities = None
    
    pass

class AssocArrayCommonParameters(AssocArrayParameters):
    """
    
    """
    def GetLevelCount(self):
        """
        GetLevelCount -> Integer
        
        """
        pass
    
    
    def GetLevelSpacing(self):
        """
        GetLevelSpacing -> double
        
        """
        pass
    
    
    def GetRowCount(self):
        """
        GetRowCount -> Integer
        
        """
        pass
    
    
    def GetRowElevation(self):
        """
        GetRowElevation -> double
        
        """
        pass
    
    
    def GetRowSpacing(self):
        """
        GetRowSpacing -> double
        
        """
        pass
    
    
    def SetLevelCount(self):
        """
        SetLevelCount -> void
        
        """
        pass
    
    
    def SetLevelSpacing(self):
        """
        SetLevelSpacing -> void
        
        """
        pass
    
    
    def SetRowCount(self):
        """
        SetRowCount -> void
        
        """
        pass
    
    
    def SetRowElevation(self):
        """
        SetRowElevation -> void
        
        """
        pass
    
    
    def SetRowSpacing(self):
        """
        SetRowSpacing -> void
        
        """
        pass
    
    
    BaseNormal = None
    
    
    BasePlane = None
    
    
    BasePoint = None
    
    
    LevelCount = None
    
    
    LevelSpacing = None
    
    
    RowCount = None
    
    
    RowElevation = None
    
    
    RowSpacing = None
    
    pass

class AssocArrayParameters(RXObject):
    """
    
    """
    def Commit(self):
        """
        Commit -> void
        
        """
        pass
    
    
    Owner = None
    
    pass

class AssocArrayPathParameters(AssocArrayCommonParameters):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    r
    
    r
    
    a
    
    y
    
    P
    
    a
    
    t
    
    h
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    r
    
    r
    
    a
    
    y
    
    P
    
    a
    
    t
    
    h
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    (
    
    )
    """
      Divide
      Measure
    
    
    def GetEndOffset(self):
        """
        GetEndOffset -> double
        
        """
        pass
    
    
    def GetItemCount(self):
        """
        GetItemCount -> Integer
        
        """
        pass
    
    
    def GetItemSpacing(self):
        """
        GetItemSpacing -> double
        
        """
        pass
    
    
    def GetStartOffset(self):
        """
        GetStartOffset -> double
        
        """
        pass
    
    
    def SetEndOffset(self):
        """
        SetEndOffset -> void
        
        """
        pass
    
    
    def SetItemCount(self):
        """
        SetItemCount -> void
        
        """
        pass
    
    
    def SetItemSpacing(self):
        """
        SetItemSpacing -> void
        
        """
        pass
    
    
    def SetStartOffset(self):
        """
        SetStartOffset -> void
        
        """
        pass
    
    
    AlignItems = None
    
    
    EndOffset = None
    
    
    ItemCount = None
    
    
    ItemSpacing = None
    
    
    Method = None
    
    
    Path = None
    
    
    PathDirection = None
    
    
    StartOffset = None
    
    pass

class AssocArrayPolarParameters(AssocArrayCommonParameters):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    r
    
    r
    
    a
    
    y
    
    P
    
    o
    
    l
    
    a
    
    r
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    r
    
    r
    
    a
    
    y
    
    P
    
    o
    
    l
    
    a
    
    r
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    (
    
    )
    """
      Clockwise
      CounterClockwise
    
    
    def GetAngleBetweenItems(self):
        """
        GetAngleBetweenItems -> double
        
        """
        pass
    
    
    def GetFillAngle(self):
        """
        GetFillAngle -> double
        
        """
        pass
    
    
    def GetItemCount(self):
        """
        GetItemCount -> Integer
        
        """
        pass
    
    
    def GetRadius(self):
        """
        GetRadius -> double
        
        """
        pass
    
    
    def GetStartAngle(self):
        """
        GetStartAngle -> double
        
        """
        pass
    
    
    def SetAngleBetweenItems(self):
        """
        SetAngleBetweenItems -> void
        
        """
        pass
    
    
    def SetFillAngle(self):
        """
        SetFillAngle -> void
        
        """
        pass
    
    
    def SetItemCount(self):
        """
        SetItemCount -> void
        
        """
        pass
    
    
    def SetRadius(self):
        """
        SetRadius -> void
        
        """
        pass
    
    
    def SetStartAngle(self):
        """
        SetStartAngle -> void
        
        """
        pass
    
    
    AngleBetweenItems = None
    
    
    Direction = None
    
    
    FillAngle = None
    
    
    ItemCount = None
    
    
    Radius = None
    
    
    RotateItems = None
    
    
    StartAngle = None
    
    pass

class AssocArrayRectangularParameters(AssocArrayCommonParameters):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    r
    
    r
    
    a
    
    y
    
    R
    
    e
    
    c
    
    t
    
    a
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    r
    
    r
    
    a
    
    y
    
    R
    
    e
    
    c
    
    t
    
    a
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    (
    
    )
    """
    def GetAxesAngle(self):
        """
        GetAxesAngle -> double
        
        """
        pass
    
    
    def GetColumnCount(self):
        """
        GetColumnCount -> Integer
        
        """
        pass
    
    
    def GetColumnSpacing(self):
        """
        GetColumnSpacing -> double
        
        """
        pass
    
    
    def SetAxesAngle(self):
        """
        SetAxesAngle -> void
        
        """
        pass
    
    
    def SetColumnCount(self):
        """
        SetColumnCount -> void
        
        """
        pass
    
    
    def SetColumnSpacing(self):
        """
        SetColumnSpacing -> void
        
        """
        pass
    
    
    AxesAngle = None
    
    
    ColumnCount = None
    
    
    ColumnSpacing = None
    
    
    XAxisDirection = None
    
    
    YAxisDirection = None
    
    pass

class AssocAsmBodyActionParam(AssocActionParam):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    s
    
    m
    
    B
    
    o
    
    d
    
    y
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def SetBody(self):
        """
        SetBody(Entity, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        SetBody(ObjectId, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AssocBlendSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    B
    
    l
    
    e
    
    n
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetContinuityGripPoints(self):
        """
        GetContinuityGripPoints -> void
        
        """
        pass
    
    
    def GetEndEdgeBulge(self):
        """
        GetEndEdgeBulge -> double
        
        """
        pass
    
    
    def GetEndEdgeContinuity(self):
        """
        GetEndEdgeContinuity -> short
        
        """
        pass
    
    
    def GetProfiles(self):
        """
        GetProfiles -> void
        
        """
        pass
    
    
    def GetStartEdgeBulge(self):
        """
        GetStartEdgeBulge -> double
        
        """
        pass
    
    
    def GetStartEdgeContinuity(self):
        """
        GetStartEdgeContinuity -> short
        
        """
        pass
    
    
    def SetEndEdgeBulge(self):
        """
        SetEndEdgeBulge -> void
        
        """
        pass
    
    
    def SetEndEdgeContinuity(self):
        """
        SetEndEdgeContinuity -> void
        
        """
        pass
    
    
    def SetStartEdgeBulge(self):
        """
        SetStartEdgeBulge -> void
        
        """
        pass
    
    
    def SetStartEdgeContinuity(self):
        """
        SetStartEdgeContinuity -> void
        
        """
        pass
    
    
    BlendOption = None
    
    
    EndEdgeBulge = None
    
    
    EndEdgeContinuity = None
    
    
    StartEdgeBulge = None
    
    
    StartEdgeContinuity = None
    
    pass

class AssocCompoundActionParam(AssocActionParam):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def AddParam(self):
        """
        AddParam -> Integer
        
        """
        pass
    
    
    def ParamAtIndex(self):
        """
        ParamAtIndex -> ObjectId
        
        """
        pass
    
    
    def ParamAtName(self):
        """
        ParamAtName(string) -> ObjectId
        
        ParamAtName(string, int) -> ObjectId
        
        """
        pass
    
    
    def ParamsAtName(self):
        """
        ParamsAtName -> ObjectIdCollection
        
        """
        pass
    
    
    def RemoveAllParams(self):
        """
        RemoveAllParams -> void
        
        """
        pass
    
    
    def RemoveParam(self):
        """
        RemoveParam -> void
        
        """
        pass
    
    
    OwnedParams = None
    
    
    ParamCount = None
    
    pass

  NoneAssocConstraintType
  DistanceAssocConstraintType
  HorizontalDistanceAssocConstraintType
  VerticalDistanceAssocConstraintType
  Angle0AssocConstraintType
  Angle1AssocConstraintType
  Angle2AssocConstraintType
  Angle3AssocConstraintType
  RadiusAssocConstraintType
  DiameterAssocConstraintType

class AssocDependency(DBObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    (
    
    )
    """
    def AttachToObject(self):
        """
        AttachToObject -> void
            
            CompoundObjectId compoundId: 
            The CompoundObjectId to attach the dependency to. If regular ObjectId is passed in, it is automatically converted to CompoundObjectId.
        """
        pass
    
    
    def DetachFromObject(self):
        """
        DetachFromObject -> void
        
        """
        pass
    
    
    def Evaluate(self):
        """
        Evaluate -> void
        
        """
        pass
    
    
    def GetDependenciesOnObject(self):
        """
        GetDependenciesOnObject -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Read-type dependencies wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Write-type dependencies wanted.
            
            object: 
            The DBObject whose dependencies are requested. The object needs to be open at least for read.
        """
        pass
    
    
    def GetFirstDependencyOnObject(self):
        """
        GetFirstDependencyOnObject -> ObjectId
            
            object: 
            The DBObject whose first dependency is requested. The object needs to be open at least for read.
        """
        pass
    
    
    def IsDependentOnTheSameThingAs(self):
        """
        IsDependentOnTheSameThingAs -> bool
            
            AssocDependency otherDependency: 
            The other dependency needs to be open for read.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            AssocDependency otherDependency: 
            The other dependency needs to be open for read.
        """
        pass
    
    
    def NotifyDependenciesOnObject(self):
        """
        NotifyDependenciesOnObject -> void
            
            AssocStatus newStatus: 
            The new status to be set to the dependencies.
            
            object: 
            The DBObject whose dependencies are to be notified. The object needs to be open at least for read.
        """
        pass
    
    
    def SetDependentOnObject(self):
        """
        SetDependentOnObject -> void
            
            CompoundObjectId compoundId: 
            The CompoundObjectId the dependency should depend-on (may be null).
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
            
            AssocStatus newStatus: 
            The new AssocStatus of the dependency.
            
            notifyOwningAction: 
            If true, and the passed-in status indicates that the dependency needs to be evaluated, the status of the AssocAction owning this dependency is set to the same status (unless the action evaluation status is already more severe than the new one). The action then notifies its owning network.
        """
        pass
    
    
    def UpdateDependentOnObject(self):
        """
        UpdateDependentOnObject -> void
        
        """
        pass
    
    
    CurrentEvaluationCallback = None
    
    
    DependencyBody = None
    
    
    DependentOnCompoundObject = None
    
    
    DependentOnObject = None
    
    
    DependentOnObjectStatus = None
    
    
    HasCachedValue = None
    
    
    IsActionEvaluationInProgress = None
    
    
    IsAttachedToObject = None
    
    
    IsDelegatingToOwningAction = None
    
    
    IsDependentOnCompoundObject = None
    
    
    IsDependentOnObjectReadOnly = None
    
    
    IsObjectStateDependent = None
    
    
    IsReadDependency = None
    
    
    IsRelevantChange = None
    
    
    IsWriteDependency = None
    
    
    NextDependencyOnObject = None
    
    
    Order = None
    
    
    OwningAction = None
    
    
    PrevDependencyOnObject = None
    
    
    Status = None
    
    pass

class AssocDependencyBody(DBObject):
    """
    
    """
    def ClonedOverride(self):
        """
        ClonedOverride -> void
        
        """
        pass
    
    
    def currentEvaluationCallback(self):
        """
        currentEvaluationCallback -> AssocEvaluationCallback
        
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def ErasedOverride(self):
        """
        ErasedOverride -> void
        
        """
        pass
    
    
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def IsDependentOnTheSameThingAsOverride(self):
        """
        IsDependentOnTheSameThingAsOverride -> bool
        
        """
        pass
    
    
    def IsEqualToOverride(self):
        """
        IsEqualToOverride -> bool
        
        """
        pass
    
    
    def ModifiedOverride(self):
        """
        ModifiedOverride -> void
        
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
        
        """
        pass
    
    
    def UpdateDependentOnObjectOverride(self):
        """
        UpdateDependentOnObjectOverride -> void
        
        """
        pass
    
    
    DependentOnObject = None
    
    
    HasCachedValueOverride = None
    
    
    IsActionEvaluationInProgress = None
    
    
    IsAttachedToObject = None
    
    
    IsRelevantChangeOverride = None
    
    
    OwningAction = None
    
    
    ParentDependency = None
    
    
    Status = None
    
    pass

class AssocDependencyPE(RXObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    P
    
    E
    
    (
    
    )
    """
    def AllowsDependencies(self):
        """
        AllowsDependencies -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool isWriteDependency: 
            The dependency will also modify the object.
            
            object: 
            The queried object, must be open for read.
        """
        pass
    
    pass

class AssocDimDependencyBody(AssocDimDependencyBodyBase):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    i
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateAndPostToDatabase(self):
        """
        CreateAndPostToDatabase -> void
            
            ObjectId dimId: 
            ObjectId of the Dimension.
            
            ref ObjectId dimDepId: 
            ObjectId of the created AssocDependency.
            
            ref ObjectId dimDepBodyId: 
            ObjectId of the created AssocDimDependencyBody.
        """
        pass
    
    
    def UpdateDependentOnObjectOverride(self):
        """
        UpdateDependentOnObjectOverride -> void
        
        """
        pass
    
    
    EntityMeasurementOverride = None
    
    
    EntityTextOverride = None
    
    
    IsEntityAttachmentChangedOverride = None
    
    pass

class AssocDimDependencyBodyBase(AssocDependencyBody):
    """
    
    """
    class NotificationIgnorerDotNet(public class NotificationIgnorerDotNet):
        """
        
        """
        def IsIgnoringNotifications(self):
            """
            IsIgnoringNotifications -> bool
            
            """
            pass
        
        pass
    
    
    def ComposeEntityText(self):
        """
        ComposeEntityText -> string
            
            int requiredNameFormat: 
            The constraint name format display, deafault value if -1. If requiredNameFormat == -1, CONSTRAINTNAMEFORMAT sysvar is used for choosing the text format.
        """
        pass
    
    
    def Constraint(self):
        """
        Constraint -> ExplicitConstraint
        
        """
        pass
    
    
    def DeactivateConstraint(self):
        """
        DeactivateConstraint -> void
        
        """
        pass
    
    
    def DragStatus(self):
        """
        DragStatus -> void
            
            Autodesk.AutoCAD.DatabaseServices.DragStatus status: 
            The current DragStatus.
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def EntityAttachmentPointMoved(self):
        """
        EntityAttachmentPointMoved -> void
            
            SubentityGeometry[] newAttachedGeometries: 
            The new attached geometries to be updated.
            
            double measurement: 
            New measurement, default value is 0.0.
        """
        pass
    
    
    def ErasedOverride(self):
        """
        ErasedOverride -> void
            
            [MarshalAs(UnmanagedType.U1)] bool isErasing: 
            Boolean isErasing.
            
            pDbObj: 
            The controlled entity.
        """
        pass
    
    
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def FormatToCurrentPrecision(self):
        """
        FormatToCurrentPrecision -> string
            
            string expression: 
            The expression to be formatted.
            
            [MarshalAs(UnmanagedType.U1)] bool isAngular: 
            Indicates it is an angular constraint.
        """
        pass
    
    
    def GetEntityNameAndExpression(self):
        """
        GetEntityNameAndExpression -> void
            
            ref string name: 
            Name from the managed entity display text.
            
            ref string expression: 
            Expression from the managed entity display text.
        """
        pass
    
    
    def GetEraseDimensionIfDependencyIsErased(self):
        """
        GetEraseDimensionIfDependencyIsErased -> bool
        
        """
        pass
    
    
    def GetFromEntity(self):
        """
        GetFromEntity -> ObjectId
            
            ObjectId entityId: 
            The entity id of the dependent-on Entity, such as of an Dimension.
        """
        pass
    
    
    def GetNameAndExpressionFromEntityText(self):
        """
        GetNameAndExpressionFromEntityText -> void
            
            string entityText: 
            The string to extract name and expression from.
            
            [MarshalAs(UnmanagedType.U1)] bool useMeasurementIfNoText: 
            Indicates whether to use measurement value if no text is given.
            
            double measurement: 
            The provided entity measurement.
            
            [MarshalAs(UnmanagedType.U1)] bool isAngular: 
            Indicates that the constraint is angular.
            
            ref string name: 
            Name component extracted from entityText.
            
            ref string expression: 
            Expression component extracted from entityText.
        """
        pass
    
    
    def GetSubentityGeoms(self):
        """
        GetSubentityGeoms -> SubentityGeometry()
            
            Vector3d distanceDirection: 
            Direction of the distance constraint.
        """
        pass
    
    
    def GetVariableNameAndExpression(self):
        """
        GetVariableNameAndExpression -> void
            
            ref string name: 
            Variable name.
            
            ref string expression: 
            Variable expression.
            
            string value: 
            Variable value.
        """
        pass
    
    
    def ModifiedOverride(self):
        """
        ModifiedOverride -> void
            
            DBObject dbObj: 
            The controlled entity.
        """
        pass
    
    
    def ReactivateConstraint(self):
        """
        ReactivateConstraint -> void
        
        """
        pass
    
    
    def SetEntityNameAndExpression(self):
        """
        SetEntityNameAndExpression -> void
            
            string name: 
            New name the managed entity should display.
            
            string expression: 
            New expression the managed entity should display.
            
            string value: 
            New value the managed entity should display.
        """
        pass
    
    
    def SetEraseDimensionIfDependencyIsErased(self):
        """
        SetEraseDimensionIfDependencyIsErased -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool yesNo: 
            Indicates to suppress the erase behavior or not.
        """
        pass
    
    
    def SetNameAndExpression(self):
        """
        SetNameAndExpression -> void
            
            string name: 
            New name to be set.
            
            string expression: 
            New expression to be set.
        """
        pass
    
    
    def SetVariableNameAndExpression(self):
        """
        SetVariableNameAndExpression -> void
            
            string name: 
            New name of the AssocVariable.
            
            string expression: 
            New expression of the AssocVariable.
        """
        pass
    
    
    def SetVariableValueToMeasuredValue(self):
        """
        SetVariableValueToMeasuredValue -> void
        
        """
        pass
    
    
    def SubErase(self):
        """
        SubErase -> void
            
            [MarshalAs(UnmanagedType.U1)] bool erasing: 
            Boolean erasing.
        """
        pass
    
    
    def UpdateDependentOnObjectOverride(self):
        """
        UpdateDependentOnObjectOverride -> void
        
        """
        pass
    
    
    def ValidateEntityText(self):
        """
        ValidateEntityText -> string
            
            string entityTextToValidate: 
            The entity text to check.
        """
        pass
    
    
    ConstrainedGeoms = None
    
    
    EntityMeasurementOverride = None
    
    
    EntityTextOverride = None
    
    
    GetCurrentlyUsedEntityNameFormat = None
    
    
    GetMeasuredValue = None
    
    
    IsConstraintActive = None
    
    
    IsEntityAttachmentChangedOverride = None
    
    
    IsReferenceOnly = None
    
    
    IsRelevantChangeOverride = None
    
    
    SubentityConstrainedGeoms = None
    
    
    Variable = None
    
    pass

  NotDraggingAssocDraggingState
  FirstSampleAssocDraggingState
  IntermediateSampleAssocDraggingState
  LastSampleAssocDraggingState

class AssocEdgeActionParam(AssocActionParam):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    E
    
    d
    
    g
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def GetEdgeRef(self):
        """
        GetEdgeRef -> EdgeRef()
        
        """
        pass
    
    
    def SetEdgeRef(self):
        """
        SetEdgeRef(EdgeRef) -> void
        
        SetEdgeRef(EdgeRef, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AssocEdgeChamferActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    E
    
    d
    
    g
    
    e
    
    C
    
    h
    
    a
    
    m
    
    f
    
    e
    
    r
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetBaseDistance(self):
        """
        GetBaseDistance -> double
        
        """
        pass
    
    
    def GetOtherDistance(self):
        """
        GetOtherDistance -> double
        
        """
        pass
    
    
    def SetBaseDistance(self):
        """
        SetBaseDistance -> void
        
        """
        pass
    
    
    def SetOtherDistance(self):
        """
        SetOtherDistance -> void
        
        """
        pass
    
    
    BaseDistance = None
    
    
    OtherDistance = None
    
    pass

class AssocEdgeFilletActionBody(AssocSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    E
    
    d
    
    g
    
    e
    
    F
    
    i
    
    l
    
    l
    
    e
    
    t
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetRadius(self):
        """
        GetRadius -> double
        
        """
        pass
    
    
    def SetRadius(self):
        """
        SetRadius -> void
        
        """
        pass
    
    
    Radius = None
    
    pass

class AssocEvaluationCallback(IDisposable):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    i
    
    o
    
    n
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
    (
    
    )
    """
    def BeginActionEvaluation(self):
        """
        BeginActionEvaluation -> void
            
            AssocAction action: 
            The action that is being evaluated.
        """
        pass
    
    
    def BeginActionEvaluationUsingObject(self):
        """
        BeginActionEvaluationUsingObject -> void
            
            ObjectId objectId: 
            The DBObject that is going to be used or modified by the action.
            
            [MarshalAs(UnmanagedType.U1)] bool objectIsGoingToBeUsed: 
            The object contents is going to be used.
            
            [MarshalAs(UnmanagedType.U1)] bool objectIsGoingToBeModified: 
            The object contents is going to be modified.
            
            DBObject substituteObject: 
            An DBObject optionally provided by the custom evaluation callback code. The custom evaluation callback code should not assign NULL to this output argument if it does not want to provide a substitute object. It should only assign a non-NULL pointer if it intends to provide a substitute object.
            
            action: 
            The action that is being evaluated.
        """
        pass
    
    
    def CancelActionEvaluation(self):
        """
        CancelActionEvaluation -> bool
        
        """
        pass
    
    
    def DraggingState(self):
        """
        DraggingState -> AssocDraggingState
        
        """
        pass
    
    
    def EndActionEvaluation(self):
        """
        EndActionEvaluation -> void
            
            AssocAction action: 
            The action that is being evaluated.
        """
        pass
    
    
    def EndActionEvaluationUsingObject(self):
        """
        EndActionEvaluationUsingObject -> void
            
            AssocAction action: 
            The action that is being evaluated.
            
            ObjectId objectId: 
            The same DBObjectId that has been previously passed to the matching BeginActionEvaluationUsingObject() callback.
            
            object: 
            The object that has been used or modified by the action. It may be NULL if the original object couldn't be opened or if the substitute object was not of the expected type.
        """
        pass
    
    
    def EvaluationMode(self):
        """
        EvaluationMode -> AssocEvaluationMode
        
        """
        pass
    
    
    def GetTransformationType(self):
        """
        GetTransformationType -> AssocTransformationType
        
        """
        pass
    
    
    def SetActionEvaluationErrorStatus(self):
        """
        SetActionEvaluationErrorStatus(AssocAction, Autodesk.AutoCAD.Runtime.ErrorStatus) -> void
            
            AssocAction action: 
            The action that is being evaluated.
            
            Autodesk.AutoCAD.Runtime.ErrorStatus errorStatus: 
            Action evaluation error status.
        SetActionEvaluationErrorStatus(AssocAction, Autodesk.AutoCAD.Runtime.ErrorStatus, ObjectId, DBObject, IntPtr) -> void
            
            AssocAction action: 
            The action that is being evaluated.
            
            Autodesk.AutoCAD.Runtime.ErrorStatus errorStatus: 
            Action evaluation error status.
            
            ObjectId objectId: 
            The failed object id (such as of an AssocDependency).
            
            IntPtr errorInfo: 
            Additional info about the error.
            
            object: 
            The failed object pointer (such as of an AssocDependency).
        """
        pass
    
    pass

  ModifyObjectsAssocEvaluationMode
  ModifyActionAssocEvaluationMode

  CanBeEvaluatedAssocEvaluationPriority = 0x3e8
  CannotBeEvaluatedAssocEvaluationPriority = -1000
  CannotDermineAssocEvaluationPriority = 0

class AssocExtendSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    E
    
    x
    
    t
    
    e
    
    n
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetDistance(self):
        """
        GetDistance -> double
        
        """
        pass
    
    
    def SetDistance(self):
        """
        SetDistance -> void
        
        """
        pass
    
    
    Distance = None
    
    pass

class AssocExtrudedSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    E
    
    x
    
    t
    
    r
    
    u
    
    d
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetHeight(self):
        """
        GetHeight -> double
        
        """
        pass
    
    
    def GetTaperAngle(self):
        """
        GetTaperAngle -> double
        
        """
        pass
    
    
    def SetHeight(self):
        """
        SetHeight -> void
        
        """
        pass
    
    
    def SetTaperAngle(self):
        """
        SetTaperAngle -> void
        
        """
        pass
    
    
    Height = None
    
    
    TaperAngle = None
    
    pass

class AssocFaceActionParam(AssocActionParam):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    F
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def GetFaceRef(self):
        """
        GetFaceRef -> FaceRef()
        
        """
        pass
    
    
    def SetFaceRef(self):
        """
        SetFaceRef(FaceRef) -> void
        
        SetFaceRef(FaceRef, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AssocFilletSurfaceActionBody(AssocSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    F
    
    i
    
    l
    
    l
    
    e
    
    t
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetFilletHandleData(self):
        """
        GetFilletHandleData -> void
        
        """
        pass
    
    
    def GetHintPoints(self):
        """
        GetHintPoints -> Point3d()
        
        """
        pass
    
    
    def GetRadius(self):
        """
        GetRadius -> double
        
        """
        pass
    
    
    def SetHintPoints(self):
        """
        SetHintPoints -> void
        
        """
        pass
    
    
    def SetRadius(self):
        """
        SetRadius -> void
        
        """
        pass
    
    
    Radius = None
    
    
    TrimMode = None
    
    pass

class AssocGeomDependency(AssocDependency):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    (
    
    )
    """
    def DependentOnObjectMirrored(self):
        """
        DependentOnObjectMirrored -> void
        
        """
        pass
    
    
    def RedirectToAnotherSubentity(self):
        """
        RedirectToAnotherSubentity -> void
            
            ObjectId oldObjectId: 
            The DBObject whose AssocGeomDependencies are to be redirected. It will be opened for write.
            
            SubentityId oldSubentId: 
            The SubentityId of the AssocGeomDependencies that is to be redirected.
            
            ObjectId newObjectId: 
            The object to redirect the dependencies to. It will be opened for write.
            
            SubentityId newSubentId: 
            The new SubentityId in the new object.
        """
        pass
    
    
    EdgeSubentityGeometry = None
    
    
    FaceSubentityGeometry = None
    
    
    IsCachingSubentityGeometry = None
    
    
    PersistentSubentId = None
    
    
    Subentity = None
    
    
    SubentityType = None
    
    
    TransientSubentCount = None
    
    
    TransientSubentIds = None
    
    
    VertexSubentityGeometry = None
    
    pass

class AssocGlobalUtility(public sealed class AssocGlobalUtility):
    """
    
    """
    def EvaluationRequestSeverityLevel(self):
        """
        EvaluationRequestSeverityLevel -> Integer
            
            AssocStatus status: 
            The AssocStatus.
        """
        pass
    
    
    def IsDraggingProvidingSubstituteObjects(self):
        """
        IsDraggingProvidingSubstituteObjects -> bool
            
            AssocEvaluationCallback evaluationCallback: 
            The current AssocEvaluationCallback. NULL pointer is allowed.
        """
        pass
    
    
    def IsEvaluationRequest(self):
        """
        IsEvaluationRequest -> bool
            
            AssocStatus status: 
            The AssocStatus.
        """
        pass
    
    
    def IsToBeSkipped(self):
        """
        IsToBeSkipped -> bool
            
            AssocStatus status: 
            The AssocStatus.
        """
        pass
    
    pass

class AssocLoftedSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    L
    
    o
    
    f
    
    t
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
      EndCrossSection = 2
      EndGuide = 8
      StartCrossSection = 1
      StartGuide = 4
    
    
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge(ProfileType) -> double
        
        GetBulge(ProfileType, out string, out string) -> double
        
        """
        pass
    
    
    def GetContinuity(self):
        """
        GetContinuity(ProfileType) -> Integer
        
        GetContinuity(ProfileType, out string, out string) -> Integer
        
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge(ProfileType, double) -> void
        
        SetBulge(ProfileType, double, string, string) -> void
        
        """
        pass
    
    
    def SetContinuity(self):
        """
        SetContinuity(ProfileType, int) -> void
        
        SetContinuity(ProfileType, int, string, string) -> void
        
        """
        pass
    
    pass

class AssocManager(DBObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
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
    def AddGlobalEvaluationCallback(self):
        """
        AddGlobalEvaluationCallback -> void
            
            int order: 
            Specifies the ordering of the user-provided callbacks in the global AssocEvaluationMultiCallback. The lower-order callbacks are called before the higher-order callbacks. The drag callback is inserted with order 0, i.e. callbacks with negative order will be called before it and callbacks with positive order will be called after it.
            
            pCallback: 
            The user-provided evaluation callback. The callback does not become owned by the global AssocEvaluationMultiCallback, it is just referenced by it.
        """
        pass
    
    
    def AuditAssociativeData(self):
        """
        AuditAssociativeData -> void
            
            Database database: 
            Database whose associative data is to be audited.
            
            [MarshalAs(UnmanagedType.U1)] bool traverseWholeDatabase: 
            If true, all objects in the database are visited and checked, and therefore loaded into memory.
        """
        pass
    
    
    def EvaluateTopLevelNetwork(self):
        """
        EvaluateTopLevelNetwork -> bool
            
            AssocEvaluationCallback callback: 
            Optional AssocEvaluationCallback that is added to the global callback before the evaluation and removed after the evaluation is completed.
            
            int callbackOrder: 
            Order of the optional AssocEvaluationCallback.
            
            patabase: 
            Database whose top-level network is to be evaluated.
        """
        pass
    
    
    def GetGlobalEvaluationCallbacks(self):
        """
        GetGlobalEvaluationCallbacks -> void
            
            ref ArrayList callbacks: 
            The returned evaluation callbacks.
            
            ref ArrayList orders: 
            The returned evaluation callback orders.
        """
        pass
    
    
    def GlobalEvaluationMultiCallback(self):
        """
        GlobalEvaluationMultiCallback -> AssocEvaluationCallback
        
        """
        pass
    
    
    def HasAssocNetwork(self):
        """
        HasAssocNetwork -> bool
        
        """
        pass
    
    
    def Initialize(self):
        """
        Initialize -> void
        
        """
        pass
    
    
    def RemoveGlobalEvaluationCallback(self):
        """
        RemoveGlobalEvaluationCallback -> void
            
            pCallback: 
            The user-provided evaluation callback to be removed.
        """
        pass
    
    pass

class AssocNetwork(AssocAction):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    N
    
    e
    
    t
    
    w
    
    o
    
    r
    
    k
    
    (
    
    )
    """
    def AddAction(self):
        """
        AddAction -> void
            
            ObjectId actionId: 
            AssocAction being added to the network.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoSetAsDatabaseOwner: 
            Make this network the database owner of the action.
        """
        pass
    
    
    def AddActions(self):
        """
        AddActions -> void
            
            ObjectIdCollection actionIds: 
            AssocActions being added to the network.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoSetAsDatabaseOwner: 
            Make this network the database owner of the actions.
        """
        pass
    
    
    def GetInstanceFromDatabase(self):
        """
        GetInstanceFromDatabase -> ObjectId
            
            Database database: 
            Database owning the network.
            
            [MarshalAs(UnmanagedType.U1)] bool createIfDoesNotExist: 
            If it does not exist yet, create a new subdictionary under the named object dictionary of the database. Create an AssocNetwork and make it owned by this newly created subdictionary.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
        """
        pass
    
    
    def GetInstanceFromObject(self):
        """
        GetInstanceFromObject -> ObjectId
            
            ObjectId owningObjectId: 
            The Object owning the sub-dictionary that owns the AssocNetwork.
            
            [MarshalAs(UnmanagedType.U1)] bool createIfDoesNotExist: 
            If it does not exist yet, create a new subdictionary of the extension dictionary of the object. Create an AssocNetwork and make it owned by this newly created subdictionary.
            
            [MarshalAs(UnmanagedType.U1)] bool addToTopLevelNetwork: 
            If the network is newly created, it also adds it to the the top-level network of the database that owns the owningObjectId. It has no effect if the network already exists or if createIfDoesNotExist is false.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
        """
        pass
    
    
    def OwnedActionStatusChanged(self):
        """
        OwnedActionStatusChanged -> void
            
            AssocAction ownedAction: 
            The action whose status has just been changed.
            
            AssocStatus previousStatus: 
            Previous status of the action.
        """
        pass
    
    
    def RemoveAction(self):
        """
        RemoveAction -> void
            
            ObjectId actionId: 
            AssocAction being removed from the network.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erase the action after removing it.
        """
        pass
    
    
    def RemoveAllActions(self):
        """
        RemoveAllActions -> void
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseThem: 
            Erase the actions after removing them.
        """
        pass
    
    
    def RemoveInstanceFromDatabase(self):
        """
        RemoveInstanceFromDatabase -> void
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erase the network after removing it.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
            
            owningObjectId: 
            The database whose named object dictionary owns the sub-dictionary that owns the AssocNetwork.
        """
        pass
    
    
    def RemoveInstanceFromObject(self):
        """
        RemoveInstanceFromObject -> void
            
            ObjectId owningObjectId: 
            The DBObject whose extension dictionary owns the sub-dictionary that owns the AssocNetwork.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erase the network after removing it.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
        """
        pass
    
    
    GetActions = None
    
    pass

class AssocNetworkSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    N
    
    e
    
    t
    
    w
    
    o
    
    r
    
    k
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge(AssocLoftedSurfaceActionBody.ProfileType) -> double
        
        GetBulge(AssocLoftedSurfaceActionBody.ProfileType, out string, out string) -> double
        
        """
        pass
    
    
    def GetContinuity(self):
        """
        GetContinuity(AssocLoftedSurfaceActionBody.ProfileType) -> Integer
        
        GetContinuity(AssocLoftedSurfaceActionBody.ProfileType, out string, out string) -> Integer
        
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge(AssocLoftedSurfaceActionBody.ProfileType, double) -> void
        
        SetBulge(AssocLoftedSurfaceActionBody.ProfileType, double, string, string) -> void
        
        """
        pass
    
    
    def SetContinuity(self):
        """
        SetContinuity(AssocLoftedSurfaceActionBody.ProfileType, int) -> void
        
        SetContinuity(AssocLoftedSurfaceActionBody.ProfileType, int, string, string) -> void
        
        """
        pass
    
    pass

class AssocObjectTransaction(IDisposable):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    r
    
    a
    
    n
    
    s
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    e
    
    i
    
    n
    
    g
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    j
    
    u
    
    s
    
    t
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    e
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    A
    
    s
    
    s
    
    o
    
    c
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    r
    
    a
    
    n
    
    s
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    B
    
    e
    
    i
    
    n
    
    g
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    j
    
    u
    
    s
    
    t
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    e
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    A
    
    s
    
    s
    
    o
    
    c
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    r
    
    a
    
    n
    
    s
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    d
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    B
    
    e
    
    i
    
    n
    
    g
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    j
    
    u
    
    s
    
    t
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    e
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    A
    
    s
    
    s
    
    o
    
    c
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    r
    
    a
    
    n
    
    s
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    B
    
    o
    
    d
    
    y
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    B
    
    o
    
    d
    
    y
    
     
    
    d
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    B
    
    o
    
    d
    
    y
    
    B
    
    e
    
    i
    
    n
    
    g
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    j
    
    u
    
    s
    
    t
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    e
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    e
    
    d
    
    .
    """
    def IsSubstituteObject(self):
        """
        IsSubstituteObject -> bool
            
            DBObject dbObject: 
            Object for which it finds out whether there is a substitute object.
        """
        pass
    
    
    def GetDBObject(self):
        """
        GetDBObject -> DBObject
            
            ObjectId objectId: 
            ObjectId of the object that should be opened.
            
            OpenMode openMode: 
            ForRead, ForWrite, ForNotify.
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Opens the object even if it is erased.
            
            [MarshalAs(UnmanagedType.U1)] bool openOnLockedLayer: 
            Opens the object even on the locked layer.
        """
        pass
    
    pass

class AssocOffsetSurfaceActionBody(AssocSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    O
    
    f
    
    f
    
    s
    
    e
    
    t
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetDistance(self):
        """
        GetDistance -> double
        
        """
        pass
    
    
    def SetDistance(self):
        """
        SetDistance -> void
        
        """
        pass
    
    
    Distance = None
    
    pass

class AssocParamBasedActionBody(AssocActionBody):
    """
    
    """

    pass

class AssocPatchSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    P
    
    a
    
    t
    
    c
    
    h
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance(ObjectId, EdgeRef[], EdgeRef[], VertexRef[], [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        CreateInstance(ObjectId, EdgeRef[], EdgeRef[], VertexRef[], int, double, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge -> double
        
        """
        pass
    
    
    def GetContinuity(self):
        """
        GetContinuity -> Integer
        
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge -> void
        
        """
        pass
    
    
    def SetConstraintCurves(self):
        """
        SetConstraintCurves -> void
        
        """
        pass
    
    
    def SetConstraintPoints(self):
        """
        SetConstraintPoints -> void
        
        """
        pass
    
    
    def SetContinuity(self):
        """
        SetContinuity -> void
        
        """
        pass
    
    
    Bulge = None
    
    
    Continuity = None
    
    
    ContinuityGripPoint = None
    
    pass

class AssocPathActionParam(AssocCompoundActionParam):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    P
    
    a
    
    t
    
    h
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def GetEdgeRefArray(self):
        """
        GetEdgeRefArray -> EdgeRef()()
        
        """
        pass
    
    
    def SetEdgeRefArray(self):
        """
        SetEdgeRefArray -> void
        
        """
        pass
    
    
    def UpdateEdgeRef(self):
        """
        UpdateEdgeRef -> void
        
        """
        pass
    
    pass

class AssocPathBasedSurfaceActionBody(AssocSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    P
    
    a
    
    t
    
    h
    
    B
    
    a
    
    s
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def GetInputPaths(self):
        """
        GetInputPaths -> void
        
        """
        pass
    
    
    def GetInputPoints(self):
        """
        GetInputPoints -> VertexRef()
        
        """
        pass
    
    
    def MakeInputPathsDrawOnTopOfResultingSurface(self):
        """
        MakeInputPathsDrawOnTopOfResultingSurface -> void
        
        """
        pass
    
    
    def RemoveAllPathParams(self):
        """
        RemoveAllPathParams -> void
        
        """
        pass
    
    
    def SetInputPaths(self):
        """
        SetInputPaths(EdgeRef[]) -> void
        
        SetInputPaths(PathRef[]) -> void
        
        """
        pass
    
    
    def SetInputPoints(self):
        """
        SetInputPoints -> void
        
        """
        pass
    
    
    def UpdateInputPath(self):
        """
        UpdateInputPath -> void
        
        """
        pass
    
    
    InputPathParams = None
    
    pass

class AssocPersSubentityId(RXObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    P
    
    e
    
    r
    
    s
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    (
    
    )
    """
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            See the AuditInfo documentation.
        """
        pass
    
    
    def CreateObjectAndDwgInFields(self):
        """
        CreateObjectAndDwgInFields -> void
            
            Database database: 
            AcDbDatabase that is going to own the AcDbAssocPersSubentId.
            
            DwgFiler filer: 
            The filer to read the data from. The first data is the class identification.
            
            ref AssocPersSubentityId createdPersSubentId: 
            This is an in/out argument used to return the created and filled-in object of an AssocPersSubentityId-derived class. If the createdPersSubentId is passed in as not NULL, the code tries to reuse the existing object, if it is of the expected derived class. If it is passed in as NULL or is not of the expected derived type, it creates a new object (deleting the existing one, if any).
        """
        pass
    
    
    def CreateObjectAndDxfInFields(self):
        """
        CreateObjectAndDxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the data from. The first data is the class identification.
            
            ref AssocPersSubentityId createdPersSubentId: 
            This is an in/out argument used to return the created and filled-in object of an AssocPersSubentityId-derived class. If the createdPersSubentId is passed in as not NULL, the code tries to reuse the existing object, if it is of the expected derived class. If it is passed in as NULL or is not of the expected derived type, it creates a new object (deleting the existing one, if any).
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> void
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> void
            
            DwgFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> void
            
            DxfFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def GetTransientSubentIds(self):
        """
        GetTransientSubentIds -> SubentityId()
            
            Entity entity: 
            The entity needs to be open for read.
            
            subents: 
            The returned SubentityIds.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            AssocPersSubentityId other: 
            The other AssocPersSubentityId.
            
            ntity: 
            The entity owning the subentities of this and the other AssocPersSubentityId.
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> void
            
            Entity mirroredEntity: 
            The entity that has been mirrored. It needs to be open for read.
        """
        pass
    
    
    def SubentType(self):
        """
        SubentType -> SubentityType
            
            Entity entity: 
            The entity needs to be open for read.
        """
        pass
    
    
    def TransientSubentCount(self):
        """
        TransientSubentCount -> Integer
            
            Entity entity: 
            The entity needs to be open for read.
        """
        pass
    
    
    IsNull = None
    
    pass

class AssocPersSubentityIdPE(RXObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    P
    
    e
    
    r
    
    s
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    P
    
    E
    
    (
    
    )
    """
    def CreateNewPersSubent(self):
        """
        CreateNewPersSubent -> AssocPersSubentityId
            
            Entity entity: 
            The entity must be open for write, but usually no changes to the entity will be made.
            
            CompoundObjectId compId: 
            Contains full context path to entity. Can be empty for simple reference.
            
            SubentityId subentId: 
            Transient SubentityId.
        """
        pass
    
    
    def GetAllSubentities(self):
        """
        GetAllSubentities -> SubentityId()
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityType subentType: 
            The required type of the subentities.
        """
        pass
    
    
    def GetEdgeSubentityGeometry(self):
        """
        GetEdgeSubentityGeometry -> Curve3d
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId edgeSubentId: 
            Edge SubentityId whose curve is to be obtained.
        """
        pass
    
    
    def GetEdgeVertexSubentities(self):
        """
        GetEdgeVertexSubentities -> void
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId edgeSubentId: 
            Edge SubentityId whose vertex SubentityIds are to be obtained.
            
            ref SubentityId startVertexSubentId: 
            Returned SubentityId of the start vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId endVertexSubentId: 
            Returned SubentityId of the end vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId[] otherVertexSubentIds: 
            Returned other SubentityIds associated with the edge, such as the circle or arc center, spline control and fit points, etc.
        """
        pass
    
    
    def GetFaceSubentityGeometry(self):
        """
        GetFaceSubentityGeometry -> Autodesk.AutoCAD.Geometry.Surface
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId faceSubentId: 
            Face SubentityId whose surface is to be changed.
        """
        pass
    
    
    def GetRigidSetState(self):
        """
        GetRigidSetState -> Integer
            
            Entity entity: 
            The entity must be open for read.
        """
        pass
    
    
    def GetRigidSetTransform(self):
        """
        GetRigidSetTransform -> Matrix3d
            
            Entity entity: 
            The entity must be open for read.
        """
        pass
    
    
    def GetSplineEdgeVertexSubentities(self):
        """
        GetSplineEdgeVertexSubentities -> void
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId edgeSubentId: 
            Edge SubentId whose vertex SubentityIds are to be obtained.
            
            ref SubentityId startVertexSubentId: 
            Returned SubentityId of the start vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId endVertexSubentId: 
            Returned SubentityId of the end vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId[] controlPointSubentIds: 
            Returned SubentityIds identifying the spline control points. The order is the same as the order of the spline control points.
            
            ref SubentityId[] fitPointSubentIds: 
            Returned SubentityIds identifying the spline fit points (if any). The order is the same as the order of the spline fit points.
        """
        pass
    
    
    def GetSubentGeometryXform(self):
        """
        GetSubentGeometryXform -> Matrix3d
            
            Entity entity: 
            The entity must be open for read.
            
            ObjectId[] fullSubentPath: 
            Full path of the sub-entity whose collective transformation matrix is to be determined.
        """
        pass
    
    
    def GetTransientSubentityIds(self):
        """
        GetTransientSubentityIds -> SubentityId()
            
            Entity entity: 
            The entity needs to be open for read.
            
            AssocPersSubentityId perSubentId: 
            The persistent subentity id on the entity.
        """
        pass
    
    
    def GetVertexSubentityGeometry(self):
        """
        GetVertexSubentityGeometry -> Point3d
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId vertexSubentId: 
            Vertex SubentityId whose position is to be obtained.
        """
        pass
    
    
    def MirrorPersSubent(self):
        """
        MirrorPersSubent -> void
            
            Entity mirroredEntity: 
            The entity that has been mirrored. It needs to be open for read.
            
            AssocPersSubentityId persSubentIdToMirror: 
            The AssocPersSubentityId to be changed to reflect the fact that the entity has been mirrored.
        """
        pass
    
    
    def SetEdgeSubentityGeometry(self):
        """
        SetEdgeSubentityGeometry -> void
            
            Entity entity: 
            The entity must be open for write.
            
            SubentityId edgeSubentId: 
            Edge SubentityId whose curve is to be changed.
            
            Curve3d newEdgeCurve: 
            New curve of the edge subentity (copied, not reused).
        """
        pass
    
    
    def SetFaceSubentityGeometry(self):
        """
        SetFaceSubentityGeometry -> void
            
            Entity entity: 
            The entity must be open for write.
            
            SubentityId faceSubentId: 
            Face SubentityId whose surface is to be changed.
            
            Autodesk.AutoCAD.Geometry.Surface newFaceSurface: 
            New surface of the face subentity (copied, not reused).
        """
        pass
    
    
    def SetRigidSetTransform(self):
        """
        SetRigidSetTransform -> void
            
            Entity entity: 
            The entity must be open for write.
            
            Matrix3d trans: 
            New transformation matrix of the rigid set entity.
        """
        pass
    
    
    def SetVertexSubentityGeometry(self):
        """
        SetVertexSubentityGeometry -> void
            
            Entity entity: 
            The entity must be open for write.
            
            SubentityId vertexSubentId: 
            Vertex SubentityId whose position is to be changed.
            
            Point3d newVertexPosition: 
            New coordinates of the vertex subentity.
        """
        pass
    
    pass

class AssocPlaneSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    P
    
    l
    
    a
    
    n
    
    e
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    pass

class AssocRevolvedSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetRevolveAngle(self):
        """
        GetRevolveAngle -> double
        
        """
        pass
    
    
    def SetRevolveAngle(self):
        """
        SetRevolveAngle -> void
        
        """
        pass
    
    
    RevolveAngle = None
    
    pass

class AssocSimplePersSubentId(AssocPersSubentityId):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    S
    
    i
    
    m
    
    p
    
    l
    
    e
    
    P
    
    e
    
    r
    
    s
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    I
    
    d
    
    (
    
    )
    """
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            See the AuditInfo documentation.
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> void
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> void
            
            DwgFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> void
            
            DxfFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            Entity entity: 
            The entity owning the subentities of this and the other AssocPersSubentityId.
            
            AssocPersSubentityId other: 
            The other AssocSimplePersSubentityId.
        """
        pass
    
    
    def SubentId(self):
        """
        SubentId -> SubentityId
        
        """
        pass
    
    
    def SubentType(self):
        """
        SubentType -> SubentityType
        
        """
        pass
    
    
    def TransientSubentCount(self):
        """
        TransientSubentCount -> Integer
            
            Entity entity: 
            Not used.
        """
        pass
    
    
    IsNull = None
    
    pass

class AssocSingleEdgePersSubentId(AssocPersSubentityId):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    S
    
    i
    
    n
    
    g
    
    l
    
    e
    
    E
    
    d
    
    g
    
    e
    
    P
    
    e
    
    r
    
    s
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    I
    
    d
    
    (
    
    )
    """
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            Entity entity: 
            The entity owning the subentities of this and the other AssocSingleEdgePersSubentId.
            
            AssocPersSubentityId other: 
            The other AssocSingleEdgePersSubentId.
        """
        pass
    
    
    def SubentType(self):
        """
        SubentType -> SubentityType
            
            Entity entity: 
            Not used.
        """
        pass
    
    
    def TransientSubentCount(self):
        """
        TransientSubentCount -> Integer
            
            Entity entity: 
            Not used.
        """
        pass
    
    
    IsNull = None
    
    pass

  IsUpToDateAssocStatus
  ChangedDirectlyAssocStatus
  ChangedTransitivelyAssocStatus
  ChangedNoDifferenceAssocStatus
  FailedToEvaluateAssocStatus
  ErasedAssocStatus
  SuppressedAssocStatus

class AssocSurfaceActionBody(AssocParamBasedActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def FindActionsThatAffectedTopologicalSubentity(self):
        """
        FindActionsThatAffectedTopologicalSubentity -> ObjectIdCollection
        
        """
        pass
    
    
    def ResultingSurfaceDep(self):
        """
        ResultingSurfaceDep([MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        ResultingSurfaceDep([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def SetResultingSurface(self):
        """
        SetResultingSurface -> void
        
        """
        pass
    
    
    IsSemiAssociative = None
    
    
    ResultingSurface = None
    
    pass

class AssocSweptSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    S
    
    w
    
    e
    
    p
    
    t
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetAlignAngle(self):
        """
        GetAlignAngle -> double
        
        """
        pass
    
    
    def GetScaleFactor(self):
        """
        GetScaleFactor -> double
        
        """
        pass
    
    
    def GetTwistAngle(self):
        """
        GetTwistAngle -> double
        
        """
        pass
    
    
    def SetAlignAngle(self):
        """
        SetAlignAngle -> void
        
        """
        pass
    
    
    def SetScaleFactor(self):
        """
        SetScaleFactor -> void
        
        """
        pass
    
    
    def SetTwistAngle(self):
        """
        SetTwistAngle -> void
        
        """
        pass
    
    
    AlignAngle = None
    
    
    ScaleFactor = None
    
    
    TwistAngle = None
    
    pass

  NotSpecified
  Stretch
  Rotate
  Move

class AssocTrimSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    T
    
    r
    
    i
    
    m
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectIdCollection
        
        """
        pass
    
    
    def MakeTrimPermanent(self):
        """
        MakeTrimPermanent -> void
        
        """
        pass
    
    
    def SetTrimInfo(self):
        """
        SetTrimInfo -> void
        
        """
        pass
    
    
    def Untrim(self):
        """
        Untrim -> void
        
        """
        pass
    
    
    TrimmedArea = None
    
    pass

class AssocValueDependency(AssocDependency):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    V
    
    a
    
    l
    
    u
    
    e
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    (
    
    )
    """
    DependentOnObjectValue = None
    
    
    ValueName = None
    
    pass

class AssocValueProviderPE(RXObject):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    V
    
    a
    
    l
    
    u
    
    e
    
    P
    
    r
    
    o
    
    v
    
    i
    
    d
    
    e
    
    r
    
    P
    
    E
    
    (
    
    )
    """
    def CanGetValue(self):
        """
        CanGetValue -> bool
            
            string valueName: 
            The name of the queried value.
            
            object: 
            The object must be open for read.
        """
        pass
    
    
    def CanSetValue(self):
        """
        CanSetValue -> bool
            
            string valueName: 
            The name of the queried value.
            
            object: 
            The object must be open for read.
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue -> ResultBuffer
            
            string valueName: 
            The name of the queried value.
            
            object: 
            The object must be open for read.
        """
        pass
    
    
    def SetValue(self):
        """
        SetValue -> void
            
            string valueName: 
            The name of the value to be set.
            
            ResultBuffer newValue: 
            The new value.
            
            object: 
            The object must be open for write.
        """
        pass
    
    pass

class AssocVariable(AssocAction):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    V
    
    a
    
    r
    
    i
    
    a
    
    b
    
    l
    
    e
    
    (
    
    )
    """
    def AddGlobalCallback(self):
        """
        AddGlobalCallback -> void
            
            pCallback: 
            The callback to be registered.
        """
        pass
    
    
    def EvaluateExpression(self):
        """
        EvaluateExpression(ObjectIdCollection, ResultBuffer[], ResultBuffer) -> string
            
            ref ObjectIdCollection objectIds: 
            Array of ids of value-providing objects. It is an in/out argument. It is being appended during the evaluation with ids of the value-providing objects whose values have been obtained (currently these objects are only AssocVariables).
            
            ref ResultBuffer[] objectValues: 
            Array of values of value-providing objects. It is an in/out argument. It is being appended during the evaluation with values of the value-providing objects whose values have been obtained (currently these objects are only AssocVariables).
            
            ref ResultBuffer evaluatedExpressionValue: 
            Returned evaluated value of the expression.
        EvaluateExpression(ResultBuffer) -> string
            
            ref ResultBuffer evaluatedExpressionValue: 
            Returned evaluated value of the expression.
        """
        pass
    
    
    def FindObjectByName(self):
        """
        FindObjectByName -> ObjectId
            
            string objectName: 
            The name of the searched-for object.
            
            RXClass pObjectClass: 
            The class of the searched-for object (isKindOf() test is used).
        """
        pass
    
    
    def globalCallback(self):
        """
        globalCallback -> AssocVariableCallback
        
        """
        pass
    
    
    def RemoveGlobalCallback(self):
        """
        RemoveGlobalCallback -> void
            
            pCallback: 
            The callback to be unregistered.
        """
        pass
    
    
    def SetName(self):
        """
        SetName -> void
            
            string newName: 
            New name of the variable.
            
            [MarshalAs(UnmanagedType.U1)] bool updateReferencingExpressions: 
            If true, it finds all expressions referencing this variable and changes them (changes their strings) to reflect the new name of the variable.
        """
        pass
    
    
    def ValidateNameAndExpression(self):
        """
        ValidateNameAndExpression -> void
            
            string nameToValidate: 
            The variable name to validate. May be null.
            
            string expressionToValidate: 
            The variable expression to validate. May be null.
            
            ref string errorMessage: 
            Error string if the name or expression is not valid, empty otherwise.
        """
        pass
    
    
    Description = None
    
    
    EvaluatorId = None
    
    
    Expression = None
    
    
    Name = None
    
    
    Value = None
    
    pass

class AssocVariableCallback(IDisposable):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    V
    
    a
    
    r
    
    i
    
    a
    
    b
    
    l
    
    e
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
    (
    
    )
    """
    def CanBeErased(self):
        """
        CanBeErased -> bool
            
            AssocVariable variable: 
            The AcDbAssocVariable that is to be erased.
        """
        pass
    
    
    def ValidateNameAndExpression(self):
        """
        ValidateNameAndExpression -> string
            
            AssocVariable variable: 
            The variable whose name and/or expression are being validated.
            
            string nameToValidate: 
            The variable name to validate. May be null.
            
            string expressionToValidate: 
            The variable expression to validate. May be null.
        """
        pass
    
    pass

class AssocVertexActionParam(AssocActionParam):
    """
    
    A
    
    s
    
    s
    
    o
    
    c
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    P
    
    a
    
    r
    
    a
    
    m
    
    (
    
    )
    """
    def GetVertexRef(self):
        """
        GetVertexRef -> VertexRef
        
        """
        pass
    
    
    def SetVertexRef(self):
        """
        SetVertexRef -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

  BaseAlign = 13
  BaseCenter = 11
  BaseFit = 0x11
  BaseLeft = 10
  BaseMid = 0x15
  BaseRight = 12
  BottomAlign = 14
  BottomCenter = 8
  BottomFit = 0x12
  BottomLeft = 7
  BottomMid = 0x16
  BottomRight = 9
  MiddleAlign = 15
  MiddleCenter = 5
  MiddleFit = 0x13
  MiddleLeft = 4
  MiddleMid = 0x17
  MiddleRight = 6
  TopAlign = 0x10
  TopCenter = 2
  TopFit = 20
  TopLeft = 1
  TopMid = 0x18
  TopRight = 3

class AttributeCollection(ICollection, IEnumerable, ISubObject):
    """
    
    """
    def AppendAttribute(self):
        """
        AppendAttribute -> ObjectId
            
            [CallerMustClose] AttributeReference attributeToAddToBlockReference: 
            Input the attribute to add.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectId[] array: 
            Input the array to copy to.
            
            int index: 
            Input the index position to start adding at.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class AttributeDefinition(DBText):
    """
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
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
    
    (
    
    )
    
    (
    
    )
    """
    def UpdateMTextAttributeDefinition(self):
        """
        UpdateMTextAttributeDefinition -> void
        
        """
        pass
    
    
    Constant = None
    
    
    FieldLength = None
    
    
    Invisible = None
    
    
    IsMTextAttributeDefinition = None
    
    
    LockPositionInBlock = None
    
    
    MTextAttributeDefinition = None
    
    
    Preset = None
    
    
    Prompt = None
    
    
    Tag = None
    
    
    Verifiable = None
    
    pass

class AttributeReference(DBText):
    """
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    def SetAttributeFromBlock(self):
        """
        SetAttributeFromBlock(AttributeDefinition, Matrix3d) -> void
            
            AttributeDefinition definition: 
            Input the the attribute definition entity to be used as a data template
            
            Matrix3d blockTransform: 
            Input a block transformation matrix.
        SetAttributeFromBlock(Matrix3d) -> void
            
            Matrix3d blockTransform: 
            Input a block transformation matrix.
        """
        pass
    
    
    def UpdateMTextAttribute(self):
        """
        UpdateMTextAttribute -> void
        
        """
        pass
    
    
    FieldLength = None
    
    
    Invisible = None
    
    
    IsConstant = None
    
    
    IsMTextAttribute = None
    
    
    IsPreset = None
    
    
    IsVerifiable = None
    
    
    LockPositionInBlock = None
    
    
    MTextAttribute = None
    
    
    Tag = None
    
    pass

class AuditInfo(DisposableWrapper):
    """
    
    """
    def ErrorsFixed(self):
        """
        ErrorsFixed -> void
            
            int count: 
            Input the number of errors fixed
        """
        pass
    
    
    def ErrorsFound(self):
        """
        ErrorsFound -> void
            
            int count: 
            Input the number of errors found
        """
        pass
    
    
    def IncNumEntities(self):
        """
        IncNumEntities -> void
        
        """
        pass
    
    
    def PrintError(self):
        """
        PrintError(DBObject, string, string, string) -> void
            
            DBObject value: 
            Input the name string will be extracted.
            
            string value2: 
            Input a string describing the value of the bad data
            
            string validation: 
            Input a string describing the reason the data is bad
            
            string defaultValue: 
            Input a string describing the default value it is set to
        PrintError(string, string, string, string) -> void
            
            string name: 
            Input a string describing the type of erroneous data found
            
            string value: 
            Input a string describing the value of the bad data
            
            string validation: 
            Input a string describing the reason the data is bad
            
            string defaultValue: 
            Input a string describing the default value it is set to
        """
        pass
    
    
    def PrintNumEntities(self):
        """
        PrintNumEntities -> void
            
            string msg: 
            Input the string to be printed
        """
        pass
    
    
    def RequestRegen(self):
        """
        RequestRegen -> void
        
        """
        pass
    
    
    def ResetNumEntities(self):
        """
        ResetNumEntities -> void
        
        """
        pass
    
    
    AuditPass = None
    
    
    FixErrors = None
    
    
    NumEntities = None
    
    
    NumErrors = None
    
    
    NumFixes = None
    
    pass

  Pass1 = 1
  Pass2 = 2

class AutoConstrainEvaluationCallback(IDisposable):
    """
    
    A
    
    u
    
    t
    
    o
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    i
    
    o
    
    n
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
    
    
    
     
    
     
    
     
    
     
    
    A
    
    c
    
    A
    
    u
    
    t
    
    o
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    i
    
    o
    
    n
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
    *
    
     
    
    i
    
    m
    
    p
    
    O
    
    b
    
    j
    
     
    
    :
    
     
    
    U
    
    n
    
    m
    
    a
    
    n
    
    a
    
    g
    
    e
    
    d
    
     
    
    C
    
    +
    
    +
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    """
    def GetAutoConstrainPriority(self):
        """
        GetAutoConstrainPriority -> GeometricalConstraint.ConstraintType()
            
            constraintList: 
            List of constraint types to be considered for autoConstrain in decending order of priority. Constraint type not present in the list will not be considered for autoconstraint.
        """
        pass
    
    
    def GetConstraintPriorityOverride(self):
        """
        GetConstraintPriorityOverride -> Integer
            
            GeometricalConstraint.ConstraintType type: 
            Geometric constraint type that is possible between given set of constrained geometry.
            
            ConstrainedGeometry[] geometries: 
            List of constrained geometry, which are potential candidate for provided constraint type. User may
        """
        pass
    
    
    def GetTotalConstraints(self):
        """
        GetTotalConstraints -> Integer
            
            ref GeometricalConstraint[] constraints: 
            reference to array of constraints, to return list of constraints found by autoconstraint evaluation. This parameter can be null if caller doesn't want list of constraints.
        """
        pass
    
    
    IsEvaluationCancelled = None
    
    pass

class Background(DBObject):
    """
    
    """
    def GetBackgroundDictionaryId(self):
        """
        GetBackgroundDictionaryId -> ObjectId
            
            Database database: 
            Input the database from which to retrieve the background dictionary
            
            [MarshalAs(UnmanagedType.U1)] bool createIfNotPresent: 
            Input whether the function should create the background dictionary if it does not currently exists in the specified database
        """
        pass
    
    pass

class BeginInsertEventArgs(EventArgs):
    """
    
    """
    From = None
    
    pass

class BeginWblockBlockEventArgs(EventArgs):
    """
    
    """
    BlockId = None
    
    
    From = None
    
    pass

class BeginWblockEntireDatabaseEventArgs(EventArgs):
    """
    
    """
    From = None
    
    pass

class BeginWblockObjectsEventArgs(EventArgs):
    """
    
    """
    From = None
    
    
    IdMapping = None
    
    pass

class BeginWblockSelectedObjectsEventArgs(EventArgs):
    """
    
    """
    From = None
    
    
    InsertionPoint = None
    
    pass

class BlendOptions(DisposableWrapper, ICloneable):
    """
    
    B
    
    l
    
    e
    
    n
    
    d
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    (
    
    )
    """
      DriveModeFirst
      DriveModeSecond
      DriveModeBoth
    
    
    CoplanarDirection = None
    
    
    CoplanarPoint = None
    
    
    DriveMode = None
    
    
    Quality = None
    
    
    Simplify = None
    
    
    Solid = None
    
    pass

class BlendOptionsBuilder(public class BlendOptionsBuilder):
    """
    
    """
    def ToBlendOptions(self):
        """
        ToBlendOptions -> BlendOptions
        
        """
        pass
    
    
    CoplanarDirection = None
    
    
    CoplanarPoint = None
    
    
    DriveMode = None
    
    
    Quality = None
    
    
    Simplify = None
    
    
    Solid = None
    
    pass

class BlockBegin(Entity):
    """
    
    B
    
    l
    
    o
    
    c
    
    k
    
    B
    
    e
    
    g
    
    i
    
    n
    
    (
    
    )
    """

    pass

  ConnectExtents
  ConnectBase

class BlockEnd(Entity):
    """
    
    B
    
    l
    
    o
    
    c
    
    k
    
    E
    
    n
    
    d
    
    (
    
    )
    """

    pass

class BlockInsertionPointsEventArgs(EventArgs):
    """
    
    B
    
    l
    
    o
    
    c
    
    k
    
    I
    
    n
    
    s
    
    e
    
    r
    
    t
    
    i
    
    o
    
    n
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    B
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    b
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    b
    
    l
    
    o
    
    c
    
    k
    
     
    
    t
    
    a
    
    b
    
    l
    
    e
    
     
    
    r
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    a
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
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
    
     
    
    a
    
    l
    
    i
    
    g
    
    n
    
    m
    
    e
    
    n
    
    t
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
    s
    
     
    
    t
    
    o
    
     
    
    a
    
    l
    
    i
    
    g
    
    n
    
     
    
    a
    
    g
    
    a
    
    i
    
    n
    
    s
    
    t
    """
    AlignmentVectors = None
    
    
    BlockTableRecord = None
    
    
    InsertionPoints = None
    
    pass

class BlockReference(Entity):
    """
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    s
    
    i
    
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
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    .
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    b
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    t
    
    o
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    """
    def ConvertToStaticBlock(self):
        """
        ConvertToStaticBlock() -> void
        
        ConvertToStaticBlock(string) -> void
            
            string newBlockName: 
            Input the name of the new block definition
        """
        pass
    
    
    def ExplodeToOwnerSpace(self):
        """
        ExplodeToOwnerSpace -> void
        
        """
        pass
    
    
    def GeometryExtentsBestFit(self):
        """
        GeometryExtentsBestFit() -> Extents3d
        
        GeometryExtentsBestFit(Matrix3d) -> Extents3d
            
            Matrix3d parentTransform: 
            Input Autodesk.AutoCAD.Geometry.Matrix3d transformation to be applied to the block reference�s geometry
        """
        pass
    
    
    def ResetBlock(self):
        """
        ResetBlock -> void
        
        """
        pass
    
    
    AnonymousBlockTableRecord = None
    
    
    AttributeCollection = None
    
    
    BlockTableRecord = None
    
    
    BlockTransform = None
    
    
    BlockUnit = None
    
    
    DynamicBlockReference = None
    
    
    DynamicBlockTableRecord = None
    
    
    IsDynamicBlock = None
    
    
    Name = None
    
    
    Normal = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    ScaleFactors = None
    
    
    TreatAsBlockRefForExplode = None
    
    
    UnitFactor = None
    
    pass

  Any
  Uniform

class BlockTable(SymbolTable, IEnumerable):
    """
    
    """

    pass

class BlockTableRecord(SymbolTableRecord, IEnumerable):
    """
    
    B
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    )
    """
    def AppendEntity(self):
        """
        AppendEntity -> ObjectId
            
            [CallerMustClose] Entity entity: 
            Input the object to append (must not be NULL)
        """
        pass
    
    
    def AssumeOwnershipOf(self):
        """
        AssumeOwnershipOf -> void
            
            ObjectIdCollection entitiesToMove: 
            Input a collection of entities to change ownership of
        """
        pass
    
    
    def GetAnonymousBlockIds(self):
        """
        GetAnonymousBlockIds -> ObjectIdCollection
        
        """
        pass
    
    
    def GetBlockReferenceIds(self):
        """
        GetBlockReferenceIds -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool directOnly: 
            Input an indication that only those BlockReferences that directly refer to this BlockTableRecord should be included in the IDs. If this value is true and the block is nested, the parent block's references will not be included.
            
            [MarshalAs(UnmanagedType.U1)] bool forceValidity: 
            Input an indication that older drawings which have been demand loaded should be loaded completely, in order to find their BlockReferenceIds. This is because older drawings did not store this information. This parameter is only applicable if directOnly is false.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> BlockTableRecordEnumerator
        
        """
        pass
    
    
    def GetErasedBlockReferenceIds(self):
        """
        GetErasedBlockReferenceIds -> ObjectIdCollection
        
        """
        pass
    
    
    def GetXrefDatabase(self):
        """
        GetXrefDatabase -> Database
            
            [MarshalAs(UnmanagedType.U1)] bool incrementUnresolved: 
            Input an indication whether or not to return the database of an unresolved xref
        """
        pass
    
    
    def UpdateAnonymousBlocks(self):
        """
        UpdateAnonymousBlocks -> void
        
        """
        pass
    
    
    BlockBeginId = None
    
    
    BlockEndId = None
    
    
    BlockScaling = None
    
    
    Comments = None
    
    
    DrawOrderTableId = None
    
    
    Explodable = None
    
    
    HasAttributeDefinitions = None
    
    
    HasPreviewIcon = None
    
    
    Hyperlinks = None
    
    
    IncludingErased = None
    
    
    IsAnonymous = None
    
    
    IsDynamicBlock = None
    
    
    IsFromExternalReference = None
    
    
    IsFromOverlayReference = None
    
    
    IsLayout = None
    
    
    IsUnloaded = None
    
    
    LayoutId = None
    
    
    Origin = None
    
    
    PathName = None
    
    
    PreviewIcon = None
    
    
    Units = None
    
    
    XrefStatus = None
    
    pass

class BlockTableRecordEnumerator(DisposableWrapper, IEnumerator):
    """
    
    """
    def MoveNext(self):
        """
        MoveNext -> bool
        
        """
        pass
    
    pass

class Body(Entity):
    """
    
    B
    
    o
    
    d
    
    y
    
    (
    
    )
    """
    def AcisIn(self):
        """
        AcisIn -> DBObjectCollection
            
            string fileName: 
            Input the file name of ASCII ACIS SAT file to be read in.
        """
        pass
    
    
    def AcisOut(self):
        """
        AcisOut -> void
            
            string fileName: 
            Input the file name to write data to.
            
            DBObjectCollection entitiesOutToFile: 
            Input a collection containing all the Entity objects that are to be written out to the file
        """
        pass
    
    
    IsNull = None
    
    
    NumChanges = None
    
    
    UsesGraphicsCache = None
    
    pass

  BoolUnite
  BoolIntersect
  BoolSubtract

class BulgeVertex(public sealed class BulgeVertex):
    """
    
    B
    
    u
    
    l
    
    g
    
    e
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
     
    
    p
    
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
    
     
    
    2
    
    D
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    b
    
    u
    
    l
    
    g
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    b
    
    u
    
    l
    
    g
    
    e
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    .
    """
    Bulge = None
    
    
    Vertex = None
    
    pass

class BulgeVertexCollection(CollectionBase):
    """
    
    B
    
    u
    
    l
    
    g
    
    e
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
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
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> Integer
            
            BulgeVertex value: 
            Input the object to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            BulgeVertex value: 
            Input the object to check for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            BulgeVertex[] array: 
            Input the object to copy from.
            
            int index: 
            Input the index to begin copying.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            BulgeVertex value: 
            Input the object to check.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the index to insert at.
            
            BulgeVertex value: 
            Input the object to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            BulgeVertex value: 
            Input the object to remove.
        """
        pass
    
    pass

class CallerMustCloseAttribute(Attribute):
    """
    
    """

    pass

class Cell(CellRange):
    """
    
    """
    Column = None
    
    
    Row = None
    
    pass

  BottomCenter = 8
  BottomLeft = 7
  BottomRight = 9
  MiddleCenter = 5
  MiddleLeft = 4
  MiddleRight = 6
  TopCenter = 2
  TopLeft = 1
  TopRight = 3

  None
  Label
  Data

  Flow = 1
  StackedHorizontal = 2
  StackedVertical = 4

  Block = 4
  Field = 2
  Unknown = 0
  Value = 1

  BottomMask = 4
  LeftMask = 8
  RightMask = 2
  TopMask = 1

  Bottom = 4
  Left = 2
  Right = 8
  Top = 1

  None
  InheritCellFormat

  Alignment = 0x10
  AutoScale = 0x100
  BackgroundColor = 0x200
  ContentColor = 0x20
  ContentLayout = 0x4000
  DataFormat = 2
  DataType = 1
  FlowDirBtoT = 0x10000
  Invalid = 0
  MarginBottom = 0x2000
  MarginHorzSpacing = 0x20000
  MarginLeft = 0x400
  MarginRight = 0x1000
  MarginTop = 0x800
  MarginVertSpacing = 0x40000
  MergeAll = 0x8000
  Rotation = 4
  Scale = 8
  TextHeight = 0x80
  TextStyle = 0x40

class CellRange(ISubObject, IEnumerable<CellReference>):
    """
    
    C
    
    e
    
    l
    
    l
    
    R
    
    a
    
    n
    
    g
    
    e
    
    (
    
    )
    """
    def Equals(self):
        """
        Equals -> bool
            
            object pRange: 
            Input range to check against.
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    BottomRight = None
    
    
    BottomRow = None
    
    
    LeftColumn = None
    
    
    RightColumn = None
    
    
    TopLeft = None
    
    
    TopRow = None
    
    pass

  ContentLocked = 1
  ContentModifiedAfterUpdate = 8
  ContentReadOnly = 2
  FormatLocked = 0x10
  FormatModifiedAfterUpdate = 0x40
  FormatReadOnly = 0x20
  Linked = 4
  None = 0

  Unknown
  Integer
  Double
  CharPtr
  Point
  ObjectId
  HardOwnerId
  SoftOwnerId
  HardPtrId
  SoftPtrId
  Bool
  Vector

class CenterPointConstraint(ConcentricConstraint):
    """
    
    """

    pass

class Circle(Curve):
    """
    
    C
    
    i
    
    r
    
    c
    
    l
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    i
    
    r
    
    c
    
    l
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    l
    
    o
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    l
    
    e
    
    n
    
    g
    
    t
    
    h
    """
    Center = None
    
    
    Circumference = None
    
    
    Diameter = None
    
    
    Normal = None
    
    
    Radius = None
    
    
    Thickness = None
    
    pass

  Invalid
  Rectangle
  Poly

class ColinearConstraint(GeometricalConstraint):
    """
    
    C
    
    o
    
    l
    
    i
    
    n
    
    e
    
    a
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  None
  Solid

  NoColumns
  StaticColumns
  DynamicColumns

class CompositeConstraint(GeometricalConstraint):
    """
    
    """
    OwnedConstraints = None
    
    pass

class CompoundObjectId(RXObject):
    """
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    d
    
     
    
    :
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    s
    
     
    
    g
    
    o
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    d
    
     
    
    :
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    s
    
     
    
    g
    
    o
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    h
    
    o
    
    s
    
    t
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    h
    
    o
    
    s
    
    t
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    .
    
     
    
    I
    
    f
    
     
    
    n
    
    u
    
    l
    
    l
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    i
    
    s
    
     
    
    t
    
    a
    
    k
    
    e
    
    n
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    (
    
    e
    
    v
    
    e
    
    n
    
     
    
    i
    
    f
    
     
    
    i
    
    t
    
     
    
    i
    
    s
    
     
    
    i
    
    n
    
     
    
    X
    
    R
    
    E
    
    F
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    )
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
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
    
    ,
    
     
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    d
    
     
    
    :
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    s
    
     
    
    g
    
    o
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
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
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    o
    
    f
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    r
    
    e
    
    n
    
    c
    
    e
    
    s
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    l
    
    e
    
    a
    
    d
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
     
    
    T
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    r
    
    e
    
    s
    
    i
    
    d
    
    e
    
    s
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    h
    
    o
    
    s
    
    t
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    i
    
    s
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    s
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    i
    
    s
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    s
    
    ,
    
     
    
    e
    
    t
    
    c
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    p
    
    H
    
    o
    
    s
    
    t
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    h
    
    o
    
    s
    
    t
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    .
    
     
    
    I
    
    f
    
     
    
    n
    
    u
    
    l
    
    l
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    i
    
    s
    
     
    
    t
    
    a
    
    k
    
    e
    
    n
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    B
    
    l
    
    o
    
    c
    
    k
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    i
    
    d
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    (
    
    e
    
    v
    
    e
    
    n
    
     
    
    i
    
    f
    
     
    
    i
    
    t
    
     
    
    i
    
    s
    
     
    
    i
    
    n
    
     
    
    X
    
    R
    
    E
    
    F
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    )
    
    .
    """
      CouldNotResolveNonTerminal = 2
      CouldNotResolveTerminal = 3
      CouldNotResolveTooEarly = 4
      IncompatibleIdType = 0x3e8
      Valid = 0
      WasLoadedNowUnloaded = 1
    
    
    def DwgInFields(self):
        """
        DwgInFields -> void
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> void
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> void
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def IsValid(self):
        """
        IsValid -> bool
            
            int validityCheckingLevel: 
            Input the level of testing.
        """
        pass
    
    
    def NullId(self):
        """
        NullId -> CompoundObjectId
        
        """
        pass
    
    
    def Remap(self):
        """
        Remap -> bool
            
            IdMapping idMap: 
            See the description of the IdMapping class.
        """
        pass
    
    
    def Set(self):
        """
        Set(CompoundObjectId, Database) -> void
        
        Set(ObjectId, Database) -> void
            
            ObjectId id: 
            ObjectId of the Object that this CompoundObjectId is going to reference.
            
            Database hostDatabase: 
            The host database. If null, the database is taken from the ObjectId (even if it is in XREF database).
        Set(ObjectId, ObjectIdCollection, Database) -> void
            
            ObjectId id: 
            ObjectId of the DBObject that this CompoundObjectId is going to reference.
            
            ObjectIdCollection path: 
            The path of BlockRefrences that lead to the referenced object. The first BlockRefrence in the path resides in the host database, the second BlockReference is from the BlockTableRecord that the first BlockReference references, the third BlockReference is from the BlockTableRecord that the second BlockReference references, etc.
            
            Database hostDatabase: 
            The host database. If null, the database is taken from the first BlockReference id in the path (even if it is in XREF database).
        """
        pass
    
    
    def SetEmpty(self):
        """
        SetEmpty -> void
        
        """
        pass
    
    
    def SetFullPath(self):
        """
        SetFullPath -> void
            
            ObjectIdCollection fullPath: 
            The path of AcDbBlockRefrences and the leaf level object itself as the last element of the array.
            
            pHostDatabase: 
            The host database. If null, the database is taken from the first AcDbBlockReference id in the fullPath.
        """
        pass
    
    
    FullPath = None
    
    
    IsEmpty = None
    
    
    IsExternal = None
    
    
    IsSimpleObjectId = None
    
    
    LeafId = None
    
    
    Path = None
    
    
    Status = None
    
    
    TopId = None
    
    
    Transform = None
    
    pass

class ConcentricConstraint(GeometricalConstraint):
    """
    
    C
    
    o
    
    n
    
    c
    
    e
    
    n
    
    t
    
    r
    
    i
    
    c
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  TurnHeight
  Turns
  Height

class Constrained2PointsConstructionLine(ConstrainedConstructionLine):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    2
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
    i
    
    o
    
    n
    
    L
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    2
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
    i
    
    o
    
    n
    
    L
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    3
    
    D
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    .
    
     
    
    R
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    o
    
    r
    
    k
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    w
    
    n
    
    i
    
    n
    
    g
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    3
    
    D
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    .
    
     
    
    R
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    o
    
    r
    
    k
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    w
    
    n
    
    i
    
    n
    
    g
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """

    pass

class ConstrainedArc(ConstrainedCircle):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    A
    
    r
    
    c
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    A
    
    r
    
    c
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    a
    
    r
    
    c
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    """
    EndPoint = None
    
    
    MidPoint = None
    
    
    StartPoint = None
    
    pass

class ConstrainedBoundedEllipse(ConstrainedEllipse):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    B
    
    o
    
    u
    
    n
    
    d
    
    e
    
    d
    
    E
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    B
    
    o
    
    u
    
    n
    
    d
    
    e
    
    d
    
    E
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    e
    
    d
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    """
    EndPoint = None
    
    
    StartPoint = None
    
    pass

class ConstrainedBoundedLine(ConstrainedLine):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    B
    
    o
    
    u
    
    n
    
    d
    
    e
    
    d
    
    L
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    B
    
    o
    
    u
    
    n
    
    d
    
    e
    
    d
    
    L
    
    i
    
    n
    
    e
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    r
    
    a
    
    y
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    b
    
    o
    
    u
    
    n
    
    d
    
    e
    
    d
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    a
    
     
    
    r
    
    a
    
    y
    
    .
    """
    EndPoint = None
    
    
    IsRay = None
    
    
    MidPoint = None
    
    
    StartPoint = None
    
    pass

class ConstrainedCircle(ConstrainedCurve):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    C
    
    i
    
    r
    
    c
    
    l
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    C
    
    i
    
    r
    
    c
    
    l
    
    e
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    c
    
    i
    
    r
    
    c
    
    l
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    """
    CenterPoint = None
    
    
    Radius = None
    
    pass

class ConstrainedConstructionLine(ConstrainedLine):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
    i
    
    o
    
    n
    
    L
    
    i
    
    n
    
    e
    
    (
    
    )
    """

    pass

class ConstrainedCurve(ConstrainedGeometry):
    """
    
    """
    ConstrainedImplicitPoints = None
    
    
    IsBounded = None
    
    pass

class ConstrainedDatumLine(ConstrainedConstructionLine):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    D
    
    a
    
    t
    
    u
    
    m
    
    L
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    D
    
    a
    
    t
    
    u
    
    m
    
    L
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    O
    
    n
    
    L
    
    i
    
    n
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
    n
    
    y
    
     
    
    3
    
    D
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    .
    
     
    
    R
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    o
    
    r
    
    k
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    w
    
    n
    
    i
    
    n
    
    g
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
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
    
     
    
    a
    
    n
    
    y
    
     
    
    3
    
    D
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
    (
    
    m
    
    u
    
    s
    
    t
    
     
    
    n
    
    o
    
    t
    
     
    
    b
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
     
    
    l
    
    e
    
    n
    
    g
    
    t
    
    h
    
    )
    
    .
    
     
    
    R
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    o
    
    r
    
    k
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    w
    
    n
    
    i
    
    n
    
    g
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """

    pass

class ConstrainedEllipse(ConstrainedCurve):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    E
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    E
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    """
    CenterPoint = None
    
    
    Direction = None
    
    
    MajorRadius = None
    
    
    MinorRadius = None
    
    pass

class ConstrainedGeometry(ConstraintGroupNode):
    """
    
    """
    def CommonConstraints(self):
        """
        CommonConstraints -> GeometricalConstraint()
            
            ConstrainedGeometry otherConsGeom: 
            The reference to the other ConstrainedGeometry object.
        """
        pass
    
    
    ConnectedConstraints = None
    
    
    ConnectedGeometries = None
    
    
    FullSubentityPaths = None
    
    
    GeomDependencyId = None
    
    
    IsReadOnly = None
    
    
    OwningRigidSet = None
    
    pass

class ConstrainedImplicitPoint(ConstrainedPoint):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    I
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    I
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    (
    
    u
    
    i
    
    n
    
    t
    
    ,
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    I
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    T
    
    y
    
    p
    
    e
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    u
    
    i
    
    n
    
    t
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    C
    
    u
    
    r
    
    v
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
    N
    
    o
    
    d
    
    e
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    I
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    T
    
    y
    
    p
    
    e
    
     
    
    p
    
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
    
     
    
    I
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    T
    
    y
    
    p
    
    e
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
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
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    f
    
    i
    
    n
    
    e
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    .
    
     
    
    I
    
    t
    
     
    
    i
    
    s
    
     
    
    o
    
    n
    
    l
    
    y
    
     
    
    v
    
    a
    
    l
    
    i
    
    d
    
     
    
    w
    
    h
    
    e
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    i
    
    s
    
     
    
    k
    
    D
    
    e
    
    f
    
    i
    
    n
    
    e
    
    I
    
    m
    
    p
    
    l
    
    i
    
    c
    
    i
    
    t
    
    .
    
     
    
    D
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    i
    
    s
    
     
    
    -
    
    1
    
     
    
    (
    
    i
    
    n
    
    v
    
    a
    
    l
    
    i
    
    d
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
    )
    
    .
    """
    ConstrainedCurveId = None
    
    
    Point = None
    
    
    PointIndex = None
    
    
    PointType = None
    
    pass

class ConstrainedLine(ConstrainedCurve):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    L
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    L
    
    i
    
    n
    
    e
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    """
    Direction = None
    
    
    PointOnLine = None
    
    pass

class ConstrainedPoint(ConstrainedGeometry):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    P
    
    o
    
    i
    
    n
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    P
    
    o
    
    i
    
    n
    
    t
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    """
    Point = None
    
    pass

class ConstrainedRigidSet(ConstrainedGeometry):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    R
    
    i
    
    g
    
    i
    
    d
    
    S
    
    e
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    R
    
    i
    
    g
    
    i
    
    d
    
    S
    
    e
    
    t
    
    (
    
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
    
    ,
    
     
    
    M
    
    a
    
    t
    
    r
    
    i
    
    x
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    b
    
    S
    
    c
    
    a
    
    l
    
    a
    
    b
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    b
    
    o
    
    o
    
    l
    
    e
    
    a
    
    n
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    r
    
    i
    
    g
    
    i
    
    d
    
     
    
    s
    
    e
    
    t
    
     
    
    c
    
    a
    
    n
    
     
    
    b
    
    e
    
     
    
    u
    
    n
    
    i
    
    f
    
    o
    
    r
    
    m
    
    l
    
    y
    
     
    
    s
    
    c
    
    a
    
    l
    
    e
    
    d
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    t
    
    r
    
    i
    
    x
    
    3
    
    d
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    M
    
    a
    
    t
    
    r
    
    i
    
    x
    
    3
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    i
    
    t
    
    i
    
    a
    
    l
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    f
    
    o
    
    r
    
    m
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    r
    
    i
    
    g
    
    i
    
    d
    
     
    
    s
    
    e
    
    t
    
     
    
    R
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    o
    
    r
    
    k
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    w
    
    n
    
    i
    
    n
    
    g
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    def GetConstrainedGeomAt(self):
        """
        GetConstrainedGeomAt -> ConstrainedGeometry
            
            int index: 
            Input the index.
        """
        pass
    
    
    NumOfConstrainedGeoms = None
    
    
    Transform = None
    
    pass

class ConstrainedSpline(ConstrainedCurve):
    """
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    N
    
    u
    
    r
    
    b
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    g
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    G
    
    e
    
    o
    
    m
    
    D
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    c
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    h
    
    o
    
    l
    
    d
    
    i
    
    n
    
    g
    
     
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    N
    
    u
    
    r
    
    b
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    N
    
    u
    
    r
    
    b
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    c
    
    G
    
    e
    
     
    
    r
    
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
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    R
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    o
    
    r
    
    k
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    w
    
    n
    
    i
    
    n
    
    g
    
     
    
    A
    
    s
    
    s
    
    o
    
    c
    
    2
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    def DefinePointAt(self):
        """
        DefinePointAt -> Point3d
            
            int index: 
            Input the index.
        """
        pass
    
    
    NumOfDefinePoints = None
    
    
    NurbSpline = None
    
    pass

class ConstraintGroupNode(RXObject):
    """
    
    """
    NodeId = None
    
    
    OwningConstraintGroupId = None
    
    pass

  NoneContent
  BlockContent
  MTextContent
  ToleranceContent

class Curve(Entity):
    """
    
    """
    def CreateFromGeCurve(self):
        """
        CreateFromGeCurve(Curve3d) -> Curve
        
        CreateFromGeCurve(Curve3d, Tolerance) -> Curve
        
        CreateFromGeCurve(Curve3d, Vector3d) -> Curve
        
        CreateFromGeCurve(Curve3d, Vector3d, Tolerance) -> Curve
        
        """
        pass
    
    
    def Extend(self):
        """
        Extend([MarshalAs(UnmanagedType.U1)] bool, Point3d) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool extendStart: 
            Input whether to extend the curve's start or end .
            
            Point3d toPoint: 
            Input the new start or end point of the curve.
        Extend(double) -> void
            
            double newParameter: 
            Input the new start or end parameter on the curve
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Point3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input the point (in WCS coordinates) for which to find nearest point on curve
            
            Vector3d direction: 
            Input the normal vector (in WCS coordinates) for plane to project onto
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input whether or not to extend curve in search for nearest point.
        GetClosestPointTo(Point3d, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input the point (in WCS coordinates) for which to find nearest point on curve
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input whether or not to extend curve in search for nearest point.
        """
        pass
    
    
    def GetDistanceAtParameter(self):
        """
        GetDistanceAtParameter -> double
            
            double value: 
            Input the object representing the parameter.
        """
        pass
    
    
    def GetDistAtPoint(self):
        """
        GetDistAtPoint -> double
            
            Point3d point: 
            Input the object representing the point.
        """
        pass
    
    
    def GetFirstDerivative(self):
        """
        GetFirstDerivative(Point3d) -> Vector3d
            
            Point3d point: 
            Input the derivative value
        GetFirstDerivative(double) -> Vector3d
            
            double value: 
            Input the derivative value
        """
        pass
    
    
    def GetGeCurve(self):
        """
        GetGeCurve() -> Curve3d
        
        GetGeCurve(Tolerance) -> Curve3d
        
        """
        pass
    
    
    def GetOffsetCurves(self):
        """
        GetOffsetCurves -> DBObjectCollection
            
            double offsetDist: 
            Input the distance to offset the curve
        """
        pass
    
    
    def GetOffsetCurvesGivenPlaneNormal(self):
        """
        GetOffsetCurvesGivenPlaneNormal -> DBObjectCollection
            
            Vector3d normal: 
            Input the normal vector for plane in which to offset
            
            double offsetDist: 
            Input distance to offset the curve
        """
        pass
    
    
    def GetOrthoProjectedCurve(self):
        """
        GetOrthoProjectedCurve -> Curve
            
            Plane planeToProjectOn: 
            Input plane onto which the curve is to be projected
        """
        pass
    
    
    def GetParameterAtDistance(self):
        """
        GetParameterAtDistance -> double
            
            double dist: 
            Input distance along the curve from the beginning of the curve to the location for the desired parameter.
        """
        pass
    
    
    def GetParameterAtPoint(self):
        """
        GetParameterAtPoint -> double
            
            Point3d point: 
            Input point (in WCS coordinates) on the curve at which the parameter is desired Returns the parameter of the curve at point
        """
        pass
    
    
    def GetPointAtDist(self):
        """
        GetPointAtDist -> Point3d
            
            double value: 
            Input distance along the curve from the beginning of the curve to the location of the desired point
        """
        pass
    
    
    def GetPointAtParameter(self):
        """
        GetPointAtParameter -> Point3d
            
            double value: 
            Input parameter on the curve at which the point is desired
        """
        pass
    
    
    def GetProjectedCurve(self):
        """
        GetProjectedCurve -> Curve
            
            Plane planeToProjectOn: 
            Input plane onto which the curve is to be projected
            
            Vector3d projectionDirection: 
            Input direction (in WCS coordinates) of the projection
        """
        pass
    
    
    def GetSecondDerivative(self):
        """
        GetSecondDerivative(Point3d) -> Vector3d
            
            Point3d point: 
            Input the derivative value
        GetSecondDerivative(double) -> Vector3d
            
            double value: 
            Input the derivative value
        """
        pass
    
    
    def GetSplitCurves(self):
        """
        GetSplitCurves(DoubleCollection) -> DBObjectCollection
            
            DoubleCollection value: 
            Input collection of points (in WCS coordinates) on the curve
        GetSplitCurves(Point3dCollection) -> DBObjectCollection
            
            Point3dCollection points: 
            Input collection of parameters on the curve
        """
        pass
    
    
    def ReverseCurve(self):
        """
        ReverseCurve -> void
        
        """
        pass
    
    
    def SetFromGeCurve(self):
        """
        SetFromGeCurve(Curve3d) -> void
        
        SetFromGeCurve(Curve3d, Tolerance) -> void
        
        SetFromGeCurve(Curve3d, Vector3d) -> void
        
        SetFromGeCurve(Curve3d, Vector3d, Tolerance) -> void
        
        """
        pass
    
    
    Area = None
    
    
    Closed = None
    
    
    EndParam = None
    
    
    EndPoint = None
    
    
    IsPeriodic = None
    
    
    Spline = None
    
    
    StartParam = None
    
    
    StartPoint = None
    
    pass

class CustomObjectSnapMode(DisposableWrapper):
    """
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    S
    
    n
    
    a
    
    p
    
    M
    
    o
    
    d
    
    e
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
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
    
    G
    
    r
    
    a
    
    p
    
    h
    
    i
    
    c
    
    s
    
    I
    
    n
    
    t
    
    e
    
    r
    
    f
    
    a
    
    c
    
    e
    
    .
    
    G
    
    l
    
    y
    
    p
    
    h
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    M
    
    o
    
    d
    
    e
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
     
    
    m
    
    o
    
    d
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
    M
    
    o
    
    d
    
    e
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    m
    
    o
    
    d
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
    o
    
    l
    
    T
    
    i
    
    p
    
    T
    
    e
    
    x
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    t
    
    i
    
    p
    
     
    
    t
    
    e
    
    x
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    G
    
    r
    
    a
    
    p
    
    h
    
    i
    
    c
    
    s
    
    I
    
    n
    
    t
    
    e
    
    r
    
    f
    
    a
    
    c
    
    e
    
    .
    
    G
    
    l
    
    y
    
    p
    
    h
    
     
    
    g
    
    l
    
    y
    
    p
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    g
    
    l
    
    y
    
    p
    
    h
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    S
    
    n
    
    a
    
    p
    
    M
    
    o
    
    d
    
    e
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
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
    
    G
    
    r
    
    a
    
    p
    
    h
    
    i
    
    c
    
    s
    
    I
    
    n
    
    t
    
    e
    
    r
    
    f
    
    a
    
    c
    
    e
    
    .
    
    G
    
    l
    
    y
    
    p
    
    h
    
    ,
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    D
    
    r
    
    a
    
    w
    
    i
    
    n
    
    g
    
    .
    
    B
    
    i
    
    t
    
    m
    
    a
    
    p
    
    ,
    
     
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    M
    
    o
    
    d
    
    e
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
     
    
    m
    
    o
    
    d
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
    M
    
    o
    
    d
    
    e
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    m
    
    o
    
    d
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
    o
    
    l
    
    T
    
    i
    
    p
    
    T
    
    e
    
    x
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    t
    
    i
    
    p
    
     
    
    t
    
    e
    
    x
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    G
    
    r
    
    a
    
    p
    
    h
    
    i
    
    c
    
    s
    
    I
    
    n
    
    t
    
    e
    
    r
    
    f
    
    a
    
    c
    
    e
    
    .
    
    G
    
    l
    
    y
    
    p
    
    h
    
     
    
    g
    
    l
    
    y
    
    p
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    g
    
    l
    
    y
    
    p
    
    h
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    D
    
    r
    
    a
    
    w
    
    i
    
    n
    
    g
    
    .
    
    B
    
    i
    
    t
    
    m
    
    a
    
    p
    
     
    
    b
    
    i
    
    t
    
    m
    
    a
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    i
    
    c
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    """
    def Activate(self):
        """
        Activate -> void
            
            string mode: 
            Input custom OSNAP mode string
        """
        pass
    
    
    def ApplyToEntityType(self):
        """
        ApplyToEntityType -> void
            
            RXClass entity: 
            Input entity to apply to
            
            AddObjectSnapInfo callback: 
            Input callback to apply
        """
        pass
    
    
    def Deactivate(self):
        """
        Deactivate -> void
            
            string mode: 
            Input mode string
        """
        pass
    
    
    def IsActive(self):
        """
        IsActive -> bool
            
            string mode: 
            Input custom OSNAP mode string
        """
        pass
    
    
    def RemoveFromEntityType(self):
        """
        RemoveFromEntityType -> void
            
            RXClass entity: 
            Input entity to remove
        """
        pass
    
    
    Bitmap = None
    
    
    DisplayString = None
    
    
    GlobalModeString = None
    
    
    Glyph = None
    
    
    GlyphSize = None
    
    
    LocalModeString = None
    
    
    ToolTipText = None
    
    pass

class CustomScale(public struct CustomScale {
}):
    """
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    S
    
    c
    
    a
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    n
    
    u
    
    m
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    n
    
    u
    
    m
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    d
    
    e
    
    n
    
    o
    
    m
    
    i
    
    n
    
    a
    
    t
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    e
    
    n
    
    o
    
    m
    
    i
    
    n
    
    a
    
    t
    
    o
    
    r
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(CustomScale) -> bool
            
            CustomScale a: 
            Input scale to compare
        IsEqualTo(CustomScale, Tolerance) -> bool
            
            CustomScale a: 
            Input custom scale to compare
            
            Tolerance tolerance: 
            Input tolerance range
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object definition.
        """
        pass
    
    
    Denominator = None
    
    
    Numerator = None
    
    pass

class DBDictionary(DBObject, IDictionary):
    """
    
    D
    
    B
    
    D
    
    i
    
    c
    
    t
    
    i
    
    o
    
    n
    
    a
    
    r
    
    y
    
    (
    
    )
    """
    def Contains(self):
        """
        Contains(ObjectId) -> bool
            
            ObjectId objId: 
            Object to search for
        Contains(string) -> bool
            
            string entryName: 
            Name to search by
        """
        pass
    
    
    def Copy(self):
        """
        Copy -> DBDictionary
        
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DBDictionaryEntry[] array: 
            Array to receive data from
            
            int index: 
            Index to begin at
        """
        pass
    
    
    def GetAt(self):
        """
        GetAt -> ObjectId
            
            string entryName: 
            String representing the entry's search key name to look for
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> DbDictionaryEnumerator
        
        """
        pass
    
    
    def NameAt(self):
        """
        NameAt -> string
            
            ObjectId objId: 
            Object ID to search for
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ObjectId) -> void
            
            ObjectId objId: 
            Object ID of the object to remove
        Remove(string) -> ObjectId
            
            string key: 
            String representing the entry's key (or name)
        """
        pass
    
    
    def SetAt(self):
        """
        SetAt -> ObjectId
            
            string searchKey: 
            String representing the object's search key name
            
            [CallerMustClose] DBObject newValue: 
            The new object to add to the dictionary
        """
        pass
    
    
    def SetName(self):
        """
        SetName -> void
            
            string oldName: 
            String representing the entry's old key string name
            
            string newName: 
            String representing the entry's new key string name
        """
        pass
    
    
    Count = None
    
    
    IncludingErased = None
    
    
    MergeStyle = None
    
    
    TreatElementsAsHard = None
    
    pass

class DBDictionaryEntry(public struct DBDictionaryEntry {
  public string m_key;
  public ObjectId m_value;
}):
    """
    
    D
    
    B
    
    D
    
    i
    
    c
    
    t
    
    i
    
    o
    
    n
    
    a
    
    r
    
    y
    
    E
    
    n
    
    t
    
    r
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    k
    
    e
    
    y
    
     
    
    :
    
     
    
    O
    
    r
    
    i
    
    g
    
    i
    
    n
    
    a
    
    l
    
     
    
    k
    
    e
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    O
    
    r
    
    i
    
    g
    
    i
    
    n
    
    a
    
    l
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    I
    
    D
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    """
    m_key Field = None
    
    
    m_value Field = None
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object.
        """
        pass
    
    
    Key = None
    
    
    Value = None
    
    pass

class DBObject(Autodesk.AutoCAD.GraphicsInterface.Drawable):
    """
    
    """
    def AddContext(self):
        """
        AddContext -> void
            
            ObjectContext context: 
            The context to add.
        """
        pass
    
    
    def ApplyPaperOrientationTransform(self):
        """
        ApplyPaperOrientationTransform -> void
            
            Autodesk.AutoCAD.DatabaseServices.Viewport viewport: 
            The viewport in which the object is to be displayed.
        """
        pass
    
    
    def ApplyPartialUndo(self):
        """
        ApplyPartialUndo -> void
            
            DwgFiler undoFiler: 
            The undo filer containing the partial undo information to be re-instated
            
            RXClass classObj: 
            The RXClass object for the class that is expected to be handling this Undo information
        """
        pass
    
    
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            An AuditInfo object
        """
        pass
    
    
    def Cancel(self):
        """
        Cancel -> void
        
        """
        pass
    
    
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def CloseAndPage(self):
        """
        CloseAndPage -> void
            
            [MarshalAs(UnmanagedType.U1)] bool onlyWhenClean: 
            Boolean indicating to turn off or on undo recording
        """
        pass
    
    
    def CreateExtensionDictionary(self):
        """
        CreateExtensionDictionary -> void
        
        """
        pass
    
    
    def DecomposeForSave(self):
        """
        DecomposeForSave -> DecomposeForSaveReplacementRecord
            
            DwgVersion version: 
            DWG version being saved to
        """
        pass
    
    
    def DeepClone(self):
        """
        DeepClone -> DBObject
            
            DBObject ownerPointer: 
            Object to which the clones should be appended
            
            IdMapping idMap: 
            Current object ID map
            
            [MarshalAs(UnmanagedType.U1)] bool isPrimary: 
            Boolean indicating whether this object is primary or owned
        """
        pass
    
    
    def DisableUndoRecording(self):
        """
        DisableUndoRecording -> void
            
            [MarshalAs(UnmanagedType.U1)] bool disable: 
            Boolean indicating to turn off or on Undo recording
        """
        pass
    
    
    def DowngradeOpen(self):
        """
        DowngradeOpen -> void
        
        """
        pass
    
    
    def DowngradeToNotify(self):
        """
        DowngradeToNotify -> void
            
            [MarshalAs(UnmanagedType.U1)] bool wasWritable: 
            Input indicating if object was open for write when upgradeFromNotify was called
        """
        pass
    
    
    def GetBinaryDataForKey(self):
        """
        GetBinaryDataForKey -> byte()
            
            string key: 
            Input extension dictionary key under which the data is stored
        """
        pass
    
    
    def DwgIn(self):
        """
        DwgIn -> void
            
            DwgFiler filer: 
            DWG filer to be used for this filing operation
        """
        pass
    
    
    def DwgOut(self):
        """
        DwgOut -> void
            
            DwgFiler filer: 
            DWG filer to be used for this filing operation
        """
        pass
    
    
    def DxfIn(self):
        """
        DxfIn -> void
            
            DxfFiler filer: 
            DXF filer to be used for this filing operation
        """
        pass
    
    
    def DxfOut(self):
        """
        DxfOut -> void
            
            DxfFiler filer: 
            Filer to be used for this filing operation
        """
        pass
    
    
    def HandOverTo(self):
        """
        HandOverTo -> void
            
            [CallerMustClose] DBObject newPointer: 
            Object to be used to replace the current object
            
            [MarshalAs(UnmanagedType.U1)] bool keepXData: 
            Boolean indicating if xdata is to be transferred during the process
            
            [MarshalAs(UnmanagedType.U1)] bool keepExtensionDictionary: 
            Boolean indicating whether the extension dictionary is passed on from the old object to the new one. If set to kTrue, the extension dictionary will be passed on, otherwise it will be left behind.
        """
        pass
    
    
    def Erase(self):
        """
        Erase() -> void
        
        Erase([MarshalAs(UnmanagedType.U1)] bool) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool erasing: 
            Boolean indicating if object is to be erased or unerased
        """
        pass
    
    
    def GetField(self):
        """
        GetField() -> Autodesk.AutoCAD.DatabaseServices.ObjectId
        
        GetField(string) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            string propertyName: 
            Input a property name for the field you want to retrieve
        """
        pass
    
    
    def GetObjectSaveVersion(self):
        """
        GetObjectSaveVersion(DwgFiler) -> FullDwgVersion
            
            DwgFiler filer: 
            Filer to be used for this filing operation
        GetObjectSaveVersion(DxfFiler) -> FullDwgVersion
            
            DxfFiler filer: 
            DXF filer to be used for this filing operation
        """
        pass
    
    
    def GetPersistentReactorIds(self):
        """
        GetPersistentReactorIds -> ObjectIdCollection
        
        """
        pass
    
    
    def SetBinaryDataForKey(self):
        """
        SetBinaryDataForKey -> void
            
            string key: 
            Input extension dictionary key to be used
            
            byte[] chunk: 
            Input a flat array of bytes that are the binary data to save
        """
        pass
    
    
    def GetReactors(self):
        """
        GetReactors -> List<RXObject>
        
        """
        pass
    
    
    def GetTransientReactors(self):
        """
        GetTransientReactors -> List<RXObject>
        
        """
        pass
    
    
    def GetXDataForApplication(self):
        """
        GetXDataForApplication -> ResultBuffer
            
            string applicationName: 
            Name of the registered application to use when retrieving the xdata
        """
        pass
    
    
    def HasContext(self):
        """
        HasContext -> bool
            
            ObjectContext context: 
            The context to check for.
        """
        pass
    
    
    def HasPersistentReactor(self):
        """
        HasPersistentReactor -> bool
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId objId: 
            Object ID of a persistent reactor object
        """
        pass
    
    
    def IsCustomObject(self):
        """
        IsCustomObject -> bool
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId id: 
            Custom ID to check.
        """
        pass
    
    
    def ReleaseExtensionDictionary(self):
        """
        ReleaseExtensionDictionary -> void
        
        """
        pass
    
    
    def RemoveContext(self):
        """
        RemoveContext -> void
            
            ObjectContext context: 
            The context to remove from the collection.
        """
        pass
    
    
    def RemoveField(self):
        """
        RemoveField() -> Autodesk.AutoCAD.DatabaseServices.ObjectId
        
        RemoveField(Autodesk.AutoCAD.DatabaseServices.ObjectId) -> void
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId id: 
            Field ID to remove from the object
        RemoveField(string) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            string propertyName: 
            Property name whose field is to be removed
        """
        pass
    
    
    def ResetScaleDependentProperties(self):
        """
        ResetScaleDependentProperties -> void
        
        """
        pass
    
    
    def SetField(self):
        """
        SetField([CallerMustClose] Field) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            [CallerMustClose] Field field: 
            Field to set
        SetField(string, [CallerMustClose] Field) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            string propertyName: 
            Property name for which to set the field
            
            [CallerMustClose] Field field: 
            Field to set
        """
        pass
    
    
    def SetFromStyle(self):
        """
        SetFromStyle -> bool
        
        """
        pass
    
    
    def SetObjectIdsInFlux(self):
        """
        SetObjectIdsInFlux -> void
        
        """
        pass
    
    
    def SetPaperOrientation(self):
        """
        SetPaperOrientation -> void
            
            [MarshalAs(UnmanagedType.U1)] bool bPaperOrientation: 
            The new value for the paper orientation property.
        """
        pass
    
    
    def SupportsCollection(self):
        """
        SupportsCollection -> bool
            
            string collectionName: 
            The name of the collection (context type) to test for support.
        """
        pass
    
    
    def SwapIdWith(self):
        """
        SwapIdWith -> void
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId otherId: of object to swap with
            
            [MarshalAs(UnmanagedType.U1)] bool swapExtendedData: 
            Boolean indicating whether to swap extended entity data
            
            [MarshalAs(UnmanagedType.U1)] bool swapExtensionDictionary: 
            Boolean indicating whether to swap extension dictionaries
        """
        pass
    
    
    def SwapReferences(self):
        """
        SwapReferences -> void
            
            IdMapping idMap: 
            Input refedit ID map
        """
        pass
    
    
    def UpgradeFromNotify(self):
        """
        UpgradeFromNotify -> bool
        
        """
        pass
    
    
    def UpgradeOpen(self):
        """
        UpgradeOpen -> void
        
        """
        pass
    
    
    def WblockClone(self):
        """
        WblockClone -> DBObject
            
            RXObject ownerPointer: 
            Input object to which the clones should be appended. If the owner has not been cloned, then the Database must be passed in.
            
            IdMapping idMap: 
            Input current object ID map
            
            [MarshalAs(UnmanagedType.U1)] bool isPrimary: 
            Input Boolean indicating whether this object is primary or owned
        """
        pass
    
    
    def XDataTransformBy(self):
        """
        XDataTransformBy -> void
            
            Matrix3d transform: 
            Transformation matrix to be applied to the XData
        """
        pass
    
    
    Annotative = None
    
    
    ClassID = None
    
    
    Database = None
    
    
    Drawable = None
    
    
    ExtensionDictionary = None
    
    
    Handle = None
    
    
    HasFields = None
    
    
    HasSaveVersionOverride = None
    
    
    Id = None
    
    
    IsAProxy = None
    
    
    IsCancelling = None
    
    
    IsErased = None
    
    
    IsEraseStatusToggled = None
    
    
    IsModified = None
    
    
    IsModifiedGraphics = None
    
    
    IsModifiedXData = None
    
    
    IsNewObject = None
    
    
    IsNotifyEnabled = None
    
    
    IsNotifying = None
    
    
    IsObjectIdsInFlux = None
    
    
    IsPersistent = None
    
    
    IsReadEnabled = None
    
    
    IsReallyClosing = None
    
    
    IsTransactionResident = None
    
    
    IsUndoing = None
    
    
    IsWriteEnabled = None
    
    
    MergeStyle = None
    
    
    ObjectBirthVersion = None
    
    
    ObjectId = None
    
    
    OwnerId = None
    
    
    PaperOrientation = None
    
    
    UndoFiler = None
    
    
    XData = None
    
    pass

class DBObjectCollection(DisposableWrapper, IList):
    """
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
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
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> Integer
            
            DBObject value: 
            Input object to add
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
            
            DBObject value: 
            Object to look for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DBObject[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to start copying at
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            DBObject value: 
            Item to retrieve the index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Index to insert at
            
            DBObject value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            DBObject value: 
            Item to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of item to remove
        """
        pass
    
    
    Count = None
    
    pass

class DBObjectReference(public struct DBObjectReference {
}):
    """
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    k
    
    i
    
    n
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    I
    
    n
    
    t
    
    3
    
    2
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    """
    Kind = None
    
    
    ObjectId = None
    
    pass

class DBObjectReferenceCollection(CollectionBase):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            DBObjectReference value: 
            Input object to add
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            DBObjectReference value: 
            Object to look for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DBObjectReference[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to start copying at
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            DBObjectReference value: 
            Item to retrieve the index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Index to insert at
            
            DBObjectReference value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            DBObjectReference value: 
            Item to remove
        """
        pass
    
    pass

class DBPoint(Entity):
    """
    
    D
    
    B
    
    P
    
    o
    
    i
    
    n
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    B
    
    P
    
    o
    
    i
    
    n
    
    t
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    s
    
    i
    
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
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    """
    EcsRotation = None
    
    
    Normal = None
    
    
    Position = None
    
    
    Thickness = None
    
    pass

class DBText(Entity):
    """
    
    D
    
    B
    
    T
    
    e
    
    x
    
    t
    
    (
    
    )
    """
    def AdjustAlignment(self):
        """
        AdjustAlignment -> void
            
            Database alternateDatabaseToUse: 
            Database to be used if the text entity is not in a database (this argument is ignored if the text entity is in a database)
        """
        pass
    
    
    def ConvertFieldToText(self):
        """
        ConvertFieldToText -> void
        
        """
        pass
    
    
    def CorrectSpelling(self):
        """
        CorrectSpelling -> Integer
        
        """
        pass
    
    
    AlignmentPoint = None
    
    
    Height = None
    
    
    HorizontalMode = None
    
    
    IsDefaultAlignment = None
    
    
    IsMirroredInX = None
    
    
    IsMirroredInY = None
    
    
    Justify = None
    
    
    Normal = None
    
    
    Oblique = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    TextString = None
    
    
    TextStyleName = None
    
    
    Thickness = None
    
    
    VerticalMode = None
    
    
    WidthFactor = None
    
    pass

class DBVisualStyle(DBObject):
    """
    
    D
    
    B
    
    V
    
    i
    
    s
    
    u
    
    a
    
    l
    
    S
    
    t
    
    y
    
    l
    
    e
    
    (
    
    )
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            VisualStyle pSrc: 
            Input visual style source
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            VisualStyle pDest: 
            Input visual style destination.
        """
        pass
    
    
    def GetTrait(self):
        """
        GetTrait -> object
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty being queried.
        """
        pass
    
    
    def GetTraitFlag(self):
        """
        GetTraitFlag -> bool
            
            uint modopt(IsLong) flagVal: 
            Input bit flag enum unsigned long property being queried.
            
            flagProp: 
            Input bitfield enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty being queried.
        """
        pass
    
    
    def SetTrait(self):
        """
        SetTrait(VisualStyleProperty, Autodesk.AutoCAD.Colors.Color, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty being set. Valid Property values for this method are:FaceMonoColorEdgeIntersectionColorEdgeObscuredColorEdgeColorEdgeSilhouetteColor
            
            pColor: 
            Input AcCmColor property value.
            
            op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, [MarshalAs(UnmanagedType.U1)] bool, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:EdgeHidePrecision
            
            [MarshalAs(UnmanagedType.U1)] bool bVal: 
            Input boolean property value to set.
            
            op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, double, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceOpacityFaceSpecularEdgeCreaseAngleEdgeOpacityDisplayBrightness
            
            double dVal: 
            Input double property value to set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, double, double, double, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceMonoColorEdgeIntersectionColorEdgeObscuredColorEdgeColorEdgeSilhouetteColor
            
            double red: 
            Input red color value to set. Valid value is from 0.0 to 1.0.
            
            double green: 
            Input green color value to set. Valid value is from 0.0 to 1.0.
            
            double blue: 
            Input blue color value to set. Valid value is from 0.0 to 1.0.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, int, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceLightingModelFaceLightingQualityFaceColorModeFaceModifierEdgeModelEdgeStyleEdgeObscuredLinePatternEdgeIntersectionLinePatternEdgeModifierEdgeWidthEdgeOverhangEdgeJitterAmountEdgeSilhouetteWidthEdgeHaloGapEdgeIsolinesDisplayStyleDisplayShadowType
            
            int nVal: 
            Input integer property value to set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, object, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set.
            
            object val: 
            Input Autodesk.AutoCAD.GraphicsInterface.Variant property value to set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        """
        pass
    
    
    def SetTraitFlag(self):
        """
        SetTraitFlag -> void
            
            uint modopt(IsLong) flagVal: 
            Input bit flag enum unsigned long property to set.
            
            [MarshalAs(UnmanagedType.U1)] bool bEnable: 
            True to enable the flag; False to disable.
            
            flagProp: 
            Input bitfield enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set.
        """
        pass
    
    
    Description = None
    
    
    InternalUseOnly = None
    
    
    Type = None
    
    pass

class DataAdapterProvider(RXObject):
    """
    
    D
    
    a
    
    t
    
    a
    
    A
    
    d
    
    a
    
    p
    
    t
    
    e
    
    r
    
    P
    
    r
    
    o
    
    v
    
    i
    
    d
    
    e
    
    r
    
    (
    
    )
    """
    def GetDataAdapter(self):
        """
        GetDataAdapter -> DataAdapter
            
            string adapterId: 
            Input ID to check for
        """
        pass
    
    pass

class DataCell(RXObject):
    """
    
    D
    
    a
    
    t
    
    a
    
    C
    
    e
    
    l
    
    l
    
    (
    
    )
    """
    def Init(self):
        """
        Init -> void
        
        """
        pass
    
    
    def SetBool(self):
        """
        SetBool -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input System.Boolean object.
        """
        pass
    
    
    def SetDouble(self):
        """
        SetDouble -> void
            
            double value: 
            Input System.Double object.
        """
        pass
    
    
    def SetHardOwnershipId(self):
        """
        SetHardOwnershipId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object.
        """
        pass
    
    
    def SetHardPointerId(self):
        """
        SetHardPointerId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetInteger(self):
        """
        SetInteger -> void
            
            int value: 
            Input System.Int32 object.
        """
        pass
    
    
    def SetObjectId(self):
        """
        SetObjectId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetPoint(self):
        """
        SetPoint -> void
            
            Point3d value: 
            Input Autodesk.AutoCAD.Geometry.Point3d object
        """
        pass
    
    
    def SetSoftOwnershipId(self):
        """
        SetSoftOwnershipId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetSoftPointerId(self):
        """
        SetSoftPointerId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetString(self):
        """
        SetString -> void
            
            string value: 
            Input System.String object
        """
        pass
    
    
    def SetVector(self):
        """
        SetVector -> void
            
            Vector3d value: 
            Input Autodesk.AutoCAD.Geometry.Vector3d object.
        """
        pass
    
    
    CellType = None
    
    
    Value = None
    
    pass

class DataCellCollection(DisposableWrapper, IList):
    """
    
    D
    
    a
    
    t
    
    a
    
    C
    
    e
    
    l
    
    l
    
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
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> Integer
            
            DataCell value: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell object
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
            
            DataCell value: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell object.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DataCell[] array: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell[] object
            
            int index: 
            Input
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            DataCell value: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell object
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            DataCell value: 
            Input the data to be inserted
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            DataCell value: 
            Input value to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index to remove from
        """
        pass
    
    
    Count = None
    
    pass

class DataColumn(RXObject):
    """
    
    D
    
    a
    
    t
    
    a
    
    C
    
    o
    
    l
    
    u
    
    m
    
    n
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    a
    
    t
    
    a
    
    C
    
    o
    
    l
    
    u
    
    m
    
    n
    
    (
    
    D
    
    a
    
    t
    
    a
    
    C
    
    o
    
    l
    
    u
    
    m
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    a
    
    t
    
    a
    
    C
    
    o
    
    l
    
    u
    
    m
    
    n
    
     
    
    c
    
    o
    
    l
    
    u
    
    m
    
    n
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    u
    
    m
    
    n
    
     
    
    t
    
    o
    
     
    
    a
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    c
    
     
    
    t
    
    y
    
    p
    
    e
    """
    def AppendCell(self):
        """
        AppendCell -> void
            
            DataCell cell: 
            New cell to add
        """
        pass
    
    
    def Assign(self):
        """
        Assign -> void
            
            DataColumn col: 
            New column to add
        """
        pass
    
    
    def GetCellAt(self):
        """
        GetCellAt -> DataCell
            
            int index: 
            Index of cell to retrieve
        """
        pass
    
    
    def GetIndexAtCell(self):
        """
        GetIndexAtCell -> Integer
            
            DataCell cell: 
            Input cell to be matched
        """
        pass
    
    
    def InsertCellAt(self):
        """
        InsertCellAt -> void
            
            int index: 
            Position at which to insert the cell
            
            DataCell cell: 
            Cell to insert
        """
        pass
    
    
    def RemoveCellAt(self):
        """
        RemoveCellAt -> void
            
            int index: 
            Index of cell to remove from the column
        """
        pass
    
    
    def SetCellAt(self):
        """
        SetCellAt -> void
            
            int index: 
            Index of the cell to be updated
            
            DataCell cell: 
            Cell to set
        """
        pass
    
    
    ColumnName = None
    
    
    ColumnType = None
    
    
    GrowLength = None
    
    
    NumCells = None
    
    
    PhysicalLength = None
    
    pass

class DataLink(DBObject):
    """
    
    D
    
    a
    
    t
    
    a
    
    L
    
    i
    
    n
    
    k
    
    (
    
    )
    """
    def GetUpdateStatus(self):
        """
        GetUpdateStatus -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            out Autodesk.AutoCAD.DatabaseServices.UpdateDirection pDir: 
            Stores the direction of the last update.
            
            out DateTime pTime: 
            Stores the time of the last update.
            
            [Out] string errMessage: 
            Stores the error message of the last update.
        """
        pass
    
    
    def GetTargets(self):
        """
        GetTargets -> ObjectIdCollection
        
        """
        pass
    
    
    def GetSourceFiles(self):
        """
        GetSourceFiles -> ArrayList
            
            Autodesk.AutoCAD.DatabaseServices.DataLinkGetSourceContext nContext: 
            Context in which this method is called
        """
        pass
    
    
    def RepathSourceFiles(self):
        """
        RepathSourceFiles -> void
            
            string sBasePath: 
            The base path
            
            Autodesk.AutoCAD.DatabaseServices.PathOption nOption: 
            The path option
        """
        pass
    
    
    def Update(self):
        """
        Update -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Update options
        """
        pass
    
    
    ConnectionString = None
    
    
    DataAdapterId = None
    
    
    DataLinkOption = None
    
    
    Description = None
    
    
    IsValid = None
    
    
    Name = None
    
    
    ToolTip = None
    
    
    UpdateOption = None
    
    pass

  Etransmit = 1
  FileWatcher = 3
  OrignalPath = 0x100
  Other = 4
  Unknown = 0
  XrefManager = 2

class DataLinkManager(RXObject):
    """
    
    """
    def AddDataLink(self):
        """
        AddDataLink -> ObjectId
            
            DataLink dataLink: 
            Data link object to add to the manager.
        """
        pass
    
    
    def GetDataLink(self):
        """
        GetDataLink() -> ObjectIdCollection
        
        GetDataLink(string) -> ObjectId
            
            string name: 
            Name of the data link to get.
        """
        pass
    
    
    def RemoveDataLink(self):
        """
        RemoveDataLink(ObjectId) -> void
            
            ObjectId idDataLink: 
            Reference to the data link to remove.
        RemoveDataLink(string) -> ObjectId
            
            string name: 
            Key to retrieve the data link.
        """
        pass
    
    
    def Update(self):
        """
        Update(Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection direction: 
            Update direction.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Update options.
        Update(ObjectIdCollection, Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            ObjectIdCollection dataIds: 
            Data link ids to update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection direction: 
            Update direction.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Update options.
        """
        pass
    
    
    DataLinkCount = None
    
    pass

  None
  Anonymous
  PersistCache

class DataTable(DBObject):
    """
    
    D
    
    a
    
    t
    
    a
    
    T
    
    a
    
    b
    
    l
    
    e
    
    (
    
    )
    """
    def AppendColumn(self):
        """
        AppendColumn -> void
            
            Autodesk.AutoCAD.DatabaseServices.CellType type: 
            Type of the column being added
            
            string columnName: 
            Name of the column
        """
        pass
    
    
    def AppendRow(self):
        """
        AppendRow -> void
            
            DataCellCollection row: 
            Row being added
            
            [MarshalAs(UnmanagedType.U1)] bool validate: 
            Validation flag
        """
        pass
    
    
    def Assign(self):
        """
        Assign -> void
            
            DataTable other: 
            New table to assign.
        """
        pass
    
    
    def GetCellAt(self):
        """
        GetCellAt -> DataCell
            
            int row: 
            Row index of cell to access
            
            int col: 
            Column index of cell to access
        """
        pass
    
    
    def GetColumnAt(self):
        """
        GetColumnAt -> DataColumn
            
            int index: 
            Index of column
        """
        pass
    
    
    def GetColumnIndexAtName(self):
        """
        GetColumnIndexAtName -> Integer
            
            string name: 
            Name of column
        """
        pass
    
    
    def GetColumnNameAt(self):
        """
        GetColumnNameAt -> string
            
            int index: 
            Column index
        """
        pass
    
    
    def GetColumnTypeAt(self):
        """
        GetColumnTypeAt -> Autodesk.AutoCAD.DatabaseServices.CellType
            
            int index: 
            Column index
        """
        pass
    
    
    def GetRowAt(self):
        """
        GetRowAt -> DataCellCollection
            
            int index: 
            Row index
        """
        pass
    
    
    def InsertColumnAt(self):
        """
        InsertColumnAt -> void
            
            int index: 
            Column index at which to insert the new column
            
            Autodesk.AutoCAD.DatabaseServices.CellType type: 
            Type of new column
            
            string columnName: 
            Name of new column
        """
        pass
    
    
    def InsertRowAt(self):
        """
        InsertRowAt -> void
            
            int index: 
            Row index of position at which to insert the row
            
            DataCellCollection row: 
            Row of data to insert
            
            [MarshalAs(UnmanagedType.U1)] bool validate: 
            Validation flag
        """
        pass
    
    
    def RemoveColumnAt(self):
        """
        RemoveColumnAt -> void
            
            int index: 
            Index of column to remove
        """
        pass
    
    
    def RemoveRowAt(self):
        """
        RemoveRowAt -> void
            
            int index: 
            Index of row to remove
        """
        pass
    
    
    def SetCellAt(self):
        """
        SetCellAt -> void
            
            int row: 
            Row index of the cell to be replaced
            
            int col: 
            Column index of the cell to be replaced
            
            DataCell cell: 
            New cell
        """
        pass
    
    
    def SetRowAt(self):
        """
        SetRowAt -> void
            
            int index: 
            Row index of the row to be replaced
            
            DataCellCollection row: 
            New row of data
            
            [MarshalAs(UnmanagedType.U1)] bool validate: 
            Validation flag
        """
        pass
    
    
    NumColsGrowSize = None
    
    
    NumColsPhysicalSize = None
    
    
    NumColumns = None
    
    
    NumRows = None
    
    
    NumRowsGrowSize = None
    
    
    NumRowsPhysicalSize = None
    
    
    TableName = None
    
    pass

  Buffer = 0x80
  Date = 8
  Double = 2
  General = 0x200
  Long = 1
  ObjectId = 0x40
  Point = 0x10
  Point3d = 0x20
  Resbuf = 0x100
  String = 4
  Unknown = 0

class Database(void Wblock(
    Database outputDataBase,
    ObjectIdCollection outObjIds,
    Point3d basePoint,
    DuplicateRecordCloning cloning
)):
    """
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    (
    
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
    
    ,
    
     
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    b
    
    u
    
    i
    
    l
    
    d
    
    D
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
    D
    
    r
    
    a
    
    w
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    B
    
    o
    
    o
    
    l
    
    e
    
    a
    
    n
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    b
    
    u
    
    i
    
    l
    
    d
    
     
    
    a
    
    n
    
     
    
    e
    
    m
    
    p
    
    t
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    n
    
    o
    
    D
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    B
    
    o
    
    o
    
    l
    
    e
    
    a
    
    n
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    r
    
    e
    
    n
    
    t
    
     
    
    d
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    """
    def AbortDeepClone(self):
        """
        AbortDeepClone -> void
            
            IdMapping idMap: 
            Input used in the deepClone operation being aborted
        """
        pass
    
    
    def AddDBObject(self):
        """
        AddDBObject -> ObjectId
            
            [CallerMustClose] DBObject appendIt: 
            Input object to be added to the database
        """
        pass
    
    
    def ApplyPartialOpenFilters(self):
        """
        ApplyPartialOpenFilters -> void
            
            SpatialFilter spatialFilter: 
            Specifies the model space volume to be used for spatial filtering
            
            Autodesk.AutoCAD.DatabaseServices.Filters.LayerFilter layerFilter: 
            Specifies the layers to be used for filtering
        """
        pass
    
    
    def AttachXref(self):
        """
        AttachXref -> ObjectId
            
            string fileName: 
            Input xref file path name
            
            string blockName: 
            Input xref block name symbol to use
        """
        pass
    
    
    def AuditXData(self):
        """
        AuditXData -> void
            
            AuditInfo info: 
            Not implemented
        """
        pass
    
    
    def BindXrefs(self):
        """
        BindXrefs -> void
            
            ObjectIdCollection xrefIds: 
            Input collection of ObjectIds for the xref BlockTableRecords to bind.
            
            [MarshalAs(UnmanagedType.U1)] bool insertBind: 
            Input System.Boolean to indicate whether or not to convert xref symbols to insert-like bind names.
        """
        pass
    
    
    def ClassDxfName(self):
        """
        ClassDxfName -> string
            
            RXClass getMyDxfName: 
            Input Autodesk.AutoCAD.Runtime.RXClass object to get the name of.
        """
        pass
    
    
    def CloseInput(self):
        """
        CloseInput -> void
            
            [MarshalAs(UnmanagedType.U1)] bool closeFile: 
            Input System.Boolean indicating whether to close the drawing file
        """
        pass
    
    
    def CountEmptyObjects(self):
        """
        CountEmptyObjects -> Integer
            
            int flags: 
            The setting of the count mode. It is stored as a bitcode using the combination of the following enum values:ZeroLengthCurve - Count zero length curves (AcDbCurve derived objects such as LINE, POLYLINE, SPLINE, etc.)EmptyText - Count empty TEXT/MTEXT objects (which contain only spaces, tabs, enters and/or new lines)AllEmptyObj - Count all empty objects
        """
        pass
    
    
    def CountHardReferences(self):
        """
        CountHardReferences -> void
            
            ObjectIdCollection ids: 
            Input collection of objectId entities of objects to find the count of hard references to those objects
            
            int[] count: 
            Input array of the same size as ids that will be filled in with the counts for each corresponding element in ids
        """
        pass
    
    
    def DeepCloneObjects(self):
        """
        DeepCloneObjects -> void
            
            ObjectIdCollection identifiers: 
            Input collection of objects to be deep cloned
            
            ObjectId id: 
            Input Object ID of object to be the owner of the clones
            
            IdMapping mapping: 
            Returns collection of objects to be used for translating object ID relationships
            
            [MarshalAs(UnmanagedType.U1)] bool deferTranslation: 
            Input Boolean indicating whether or not ID translation should be done
        """
        pass
    
    
    def DetachXref(self):
        """
        DetachXref -> void
            
            ObjectId xrefId: 
            Input object ID of the xref block to detach
        """
        pass
    
    
    def DisablePartialOpen(self):
        """
        DisablePartialOpen -> void
        
        """
        pass
    
    
    def DisableUndoRecording(self):
        """
        DisableUndoRecording -> void
            
            [MarshalAs(UnmanagedType.U1)] bool disable: 
            Input Boolean indicating turn Undo on or off
        """
        pass
    
    
    def DxfIn(self):
        """
        DxfIn -> void
            
            string fileName: 
            Input full path of the DXF file to be read into database
            
            string logFilename: 
            Log file to record all warning/error messages from reading the DXF file
        """
        pass
    
    
    def DxfOut(self):
        """
        DxfOut(string, int, DwgVersion) -> void
            
            string fileName: 
            Input name or URL of the new DXF file to create (the .dxf extension is not added automatically)
            
            int precision: 
            Number of bits of accuracy, from 0 to 16
            
            DwgVersion version: 
            Sets the DWG version major and minor number
        DxfOut(string, int, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            string fileName: 
            Input name or URL of the new DXF file to create (the .dxf extension is not added automatically)
            
            int precision: 
            Number of bits of accuracy, from 0 to 16
            
            [MarshalAs(UnmanagedType.U1)] bool saveThumbnailImage: 
            Input Boolean indicating whether to save thumbnail
        """
        pass
    
    
    def EraseEmptyObjects(self):
        """
        EraseEmptyObjects -> Integer
            
            int flags: 
            The setting of the erase mode. It is stored as a bitcode using the combination of the following enum values:ZeroLengthCurve - Erase zero length curves (AcDbCurve derived objects such as LINE, POLYLINE, SPLINE, etc.)EmptyText - Erase empty TEXT/MTEXT objects (which contain only spaces, tabs, enters and/or new lines)AllEmptyObj - Erase all empty objects
        """
        pass
    
    
    def EvaluateFields(self):
        """
        EvaluateFields() -> FieldEvaluationResult
        
        EvaluateFields(FieldEvaluationContext) -> FieldEvaluationResult
            
            FieldEvaluationContext context: 
            Input bitwise value that determines the contexts in which fields should be evaluated. Refer to the DatabaseServices.FieldEvaluationContext enum for available context values.
        EvaluateFields(FieldEvaluationContext, string) -> FieldEvaluationResult
            
            FieldEvaluationContext context: 
            Input bitwise value that determines the contexts in which fields should be evaluated. Refer to the DatabaseServices.FieldEvaluationContext enum for available context values.
            
            string prop: 
            Input property name whose field is to be evaluated; if empty, all fields are evaluated
        """
        pass
    
    
    def ForceWblockDatabaseCopy(self):
        """
        ForceWblockDatabaseCopy -> void
        
        """
        pass
    
    
    def FromAcadDatabase(self):
        """
        FromAcadDatabase -> Database
        
        """
        pass
    
    
    def GetAllDatabases(self):
        """
        GetAllDatabases -> List<Database>
        
        """
        pass
    
    
    def GetDimensionStyleChildData(self):
        """
        GetDimensionStyleChildData -> DimStyleTableRecord
            
            RXClass classDescriptor: 
            Input object to check.
        """
        pass
    
    
    def GetDimensionStyleChildId(self):
        """
        GetDimensionStyleChildId -> ObjectId
            
            RXClass classDescriptor: 
            Input dimension class descriptor
            
            ObjectId parentStyle: 
            Input parent dimension style ID
        """
        pass
    
    
    def GetDimensionStyleParentId(self):
        """
        GetDimensionStyleParentId -> ObjectId
            
            ObjectId childStyle: 
            Input child dimension style ID
        """
        pass
    
    
    def GetDimRecentStyleList(self):
        """
        GetDimRecentStyleList -> ObjectIdCollection
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def GetHostDwgXrefGraph(self):
        """
        GetHostDwgXrefGraph -> XrefGraph
            
            [MarshalAs(UnmanagedType.U1)] bool includeGhosts: 
            If set to true, includes ghost nodes.
        """
        pass
    
    
    def GetNearestLineWeight(self):
        """
        GetNearestLineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int weight: 
            Input lineweight in hundredths of a millimeter
        """
        pass
    
    
    def GetObjectId(self):
        """
        GetObjectId -> ObjectId
            
            [MarshalAs(UnmanagedType.U1)] bool createIfNotFound: 
            Input Boolean indicating to create a objectId stub if input handle is not found
            
            Handle objHandle: 
            Input Handle object containing the handle being passed in
            
            int identifier: 
            Reserved for future use
        """
        pass
    
    
    def GetMetaObject(self):
        """
        GetMetaObject -> DynamicMetaObject
        
        """
        pass
    
    
    def GetSupportedDxfOutVersions(self):
        """
        GetSupportedDxfOutVersions -> DwgVersion()
        
        """
        pass
    
    
    def GetSupportedSaveVersions(self):
        """
        GetSupportedSaveVersions -> DwgVersion()
        
        """
        pass
    
    
    def GetViewports(self):
        """
        GetViewports -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool bGetPaperspaceVports: 
            Input flag indicating whether to return paperspace viewports associated with layouts
        """
        pass
    
    
    def GetVisualStyleList(self):
        """
        GetVisualStyleList -> StringCollection
        
        """
        pass
    
    
    def Insert(self):
        """
        Insert(Matrix3d, Database, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            Matrix3d transform: 
            Input transformation matrix applied to all objects being inserted
            
            Database dataBase: 
            Input database to insert from
            
            [MarshalAs(UnmanagedType.U1)] bool preserveSourceDatabase: 
            Input to determine whether the source database pDb will be left intact
        Insert(string, Database, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
            
            string blockName: 
            Input name to be used by the new block table record created by this function
            
            Database dataBase: 
            Input database from which to insert entities
            
            [MarshalAs(UnmanagedType.U1)] bool preserveSourceDatabase: 
            Input bool to determine whether the source database is left intact
        Insert(string, string, Database, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
            
            string sourceBlockName: 
            Input name of the blockTableRecord
            
            string destinationBlockName: 
            Input name to be used by the new block table record created by this function
            
            Database dataBase: 
            Input database from which to insert entities
            
            [MarshalAs(UnmanagedType.U1)] bool preserveSourceDatabase: 
            Input bool to determine whether the source database is left intact
        """
        pass
    
    
    def IsObjectNonPersistent(self):
        """
        IsObjectNonPersistent -> bool
            
            ObjectId id: 
            Input ID of the object to be interrogated
        """
        pass
    
    
    def IsValidLineWeight(self):
        """
        IsValidLineWeight -> bool
            
            int weight: 
            Input lineweight in hundredths of a millimeter
        """
        pass
    
    
    def LoadLineTypeFile(self):
        """
        LoadLineTypeFile -> void
            
            string lineTypeName: 
            Input linetype name string (wild cards may be used)
            
            string filename: 
            Input path/filename or URL of linetype file to load from (path is optional)
        """
        pass
    
    
    def LoadMlineStyleFile(self):
        """
        LoadMlineStyleFile -> void
            
            string mlineStyleName: 
            Input MlineStyle name string (no wild cards)
            
            string fileName: 
            Input path/filename or URL of file to load from (path is optional)
        """
        pass
    
    
    def MarkObjectNonPersistent(self):
        """
        MarkObjectNonPersistent -> void
            
            ObjectId id: 
            Input ID of the object to be modified
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input true to make the object non-persistent, or false to make it persistent
        """
        pass
    
    
    def OverlayXref(self):
        """
        OverlayXref -> ObjectId
            
            string fileName: 
            Input xref file path name
            
            string blockName: 
            Input xref block name symbol to use
        """
        pass
    
    
    def Purge(self):
        """
        Purge(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input collection of object ID entities of objects
        Purge(ObjectIdGraph) -> void
            
            ObjectIdGraph idGraph: 
            Input graph of objects in the database. The graph will be returned containing only those objects that may safely be removed from the database.
        """
        pass
    
    
    def ReadDwgFile(self):
        """
        ReadDwgFile(IntPtr, [MarshalAs(UnmanagedType.U1)] bool, string) -> void
            
            IntPtr drawingFile: 
            Input pointer to DWG file to read
            
            [MarshalAs(UnmanagedType.U1)] bool allowCPConversion: 
            Input Boolean indicating whether to allow codepage conversion
            
            string password: 
            Input string containing a DWG password
        ReadDwgFile(string, FileOpenMode, [MarshalAs(UnmanagedType.U1)] bool, string) -> void
            
            string fileName: 
            Input name or URL of file to read
            
            FileOpenMode mode: 
            Input open mode
            
            [MarshalAs(UnmanagedType.U1)] bool allowCPConversion: 
            Input Boolean indicating whether to allow codepage conversion
            
            string password: 
            Input string containing a DWG password
        ReadDwgFile(string, FileShare, [MarshalAs(UnmanagedType.U1)] bool, string) -> void
            
            string fileName: 
            Input name or URL of file to read
            
            FileShare fileSharing: 
            Input share mode
            
            [MarshalAs(UnmanagedType.U1)] bool allowCPConversion: 
            Input Boolean indicating whether to allow codepage conversion
            
            string password: 
            Input string containing a DWG password
            _SH_DENYWR: 
            Opens an existing file as read-onlyDenies write-access to the file by other sessions
            _SH_DENYRW: 
            Opens a file for reading and writingDenies read-write access to the file by other sessions
            _SH_DENYNO: 
            Opens an existing file as read-onlyPermits read-write access to the file by other sessions
        """
        pass
    
    
    def ReclaimMemoryFromErasedObjects(self):
        """
        ReclaimMemoryFromErasedObjects -> void
            
            ObjectIdCollection ids: 
            A collection of object ids whose memory is to be reclaimed by deleting their objects. All object ids in the collection must correspond to erased objects, which must be entirely closed.
        """
        pass
    
    
    def ReloadXrefs(self):
        """
        ReloadXrefs -> void
            
            ObjectIdCollection xrefIds: 
            Input collection of ObjectIds for the xref BlockTableRecords to unload
        """
        pass
    
    
    def ResolveXrefs(self):
        """
        ResolveXrefs -> void
            
            [MarshalAs(UnmanagedType.U1)] bool useThreadEngine: 
            Input Boolean indicating whether to use the thread engine for xref resolution
            
            [MarshalAs(UnmanagedType.U1)] bool doNewOnly: 
            Input Boolean indicating whether to process only newly added xrefs
        """
        pass
    
    
    def RestoreForwardingXrefSymbols(self):
        """
        RestoreForwardingXrefSymbols -> void
        
        """
        pass
    
    
    def RestoreOriginalXrefSymbols(self):
        """
        RestoreOriginalXrefSymbols -> void
        
        """
        pass
    
    
    def ResetTimes(self):
        """
        ResetTimes -> void
        
        """
        pass
    
    
    def Save(self):
        """
        Save -> void
        
        """
        pass
    
    
    def SaveAs(self):
        """
        SaveAs(string, Autodesk.AutoCAD.DatabaseServices.SecurityParameters) -> void
            
            string fileName: 
            Input file name or URL to write database out to
            
            Autodesk.AutoCAD.DatabaseServices.SecurityParameters security: 
            Input a SecurityParameters structure
        SaveAs(string, DwgVersion) -> void
            
            string fileName: 
            Input file name or URL to write database out to
            
            DwgVersion version: 
            Input dwg version to which to save the file
        SaveAs(string, [MarshalAs(UnmanagedType.U1)] bool, DwgVersion, Autodesk.AutoCAD.DatabaseServices.SecurityParameters) -> void
            
            string fileName: 
            Input file name or URL to write database out to
            
            [MarshalAs(UnmanagedType.U1)] bool bBakAndRename: 
            Input bool indicating whether or not to create a .bak file and change document name in AutoCAD
            
            DwgVersion version: 
            Input dwg version to which to save the file
            
            Autodesk.AutoCAD.DatabaseServices.SecurityParameters security: 
            Input a SecurityParameters structure
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input pointer to DimStyleTableRecord from which to copy dimension variable information
        """
        pass
    
    
    def SetTimeZoneAsUtcOffset(self):
        """
        SetTimeZoneAsUtcOffset -> Autodesk.AutoCAD.DatabaseServices.TimeZone
            
            double offset: 
            Input the offset, in hours
            
            Exceptions: 
            Description
            
            validInput: 
            Thrown if a valid time zone is not found
        """
        pass
    
    
    def SetWorldPaperspaceUcsBaseOrigin(self):
        """
        SetWorldPaperspaceUcsBaseOrigin -> void
            
            Point3d origin: 
            Input new origin point in WCS coordinates
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input view for which base point is desired
        """
        pass
    
    
    def SetWorldUcsBaseOrigin(self):
        """
        SetWorldUcsBaseOrigin -> void
            
            Point3d origin: 
            Input new origin point in WCS coordinates
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input view for which base point is desired
        """
        pass
    
    
    def TimeZoneDescription(self):
        """
        TimeZoneDescription -> string
            
            Autodesk.AutoCAD.DatabaseServices.TimeZone tz: 
            Input a value from the TimeZone enum
        """
        pass
    
    
    def TimeZoneOffset(self):
        """
        TimeZoneOffset -> double
            
            Autodesk.AutoCAD.DatabaseServices.TimeZone tz: 
            Input one of the time zones contained in the TimeZone enum
            
            Exceptions: 
            Description
            
            validInput: 
            Thrown if an invalid TimeZone is passed in
        """
        pass
    
    
    def UnloadXrefs(self):
        """
        UnloadXrefs -> void
            
            ObjectIdCollection xrefIds: 
            Input collection of ObjectIds for the xref BlockTableRecords to unload
        """
        pass
    
    
    def UpdateExt(self):
        """
        UpdateExt -> void
            
            [MarshalAs(UnmanagedType.U1)] bool doBestFit: 
            Determines whether to generate the tightest bounding box
        """
        pass
    
    
    def Wblock(self):
        """
        Wblock() -> void
        
        """
        pass
    
    
    def XBindXrefs(self):
        """
        XBindXrefs -> void
            
            ObjectIdCollection xrefSymbolIds: 
            Input collection of ObjectIds of SymbolTableRecord objects to be bound.
            
            [MarshalAs(UnmanagedType.U1)] bool insertBind: 
            Input bool to indicate whether or not to convert xref symbols to insert-like bind names.
        """
        pass
    
    
    def WblockCloneObjects(self):
        """
        WblockCloneObjects -> void
            
            ObjectIdCollection identifiers: 
            Input collection of objects to be deep cloned
            
            ObjectId id: 
            Input object ID of object to be the owner of the clones
            
            IdMapping mapping: 
            Collection of IdPair objects to be used for translating object ID relationships
            
            Autodesk.AutoCAD.DatabaseServices.DuplicateRecordCloning cloning: 
            Input action for duplicate records
            
            [MarshalAs(UnmanagedType.U1)] bool deferTranslation: 
            Input Boolean indicating whether or not ID translation should be done
        """
        pass
    
    
    def WorldPaperspaceUcsBaseOrigin(self):
        """
        WorldPaperspaceUcsBaseOrigin -> Point3d
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input desired view
        """
        pass
    
    
    def WorldUcsBaseOrigin(self):
        """
        WorldUcsBaseOrigin -> Point3d
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input view for which base point is desired
        """
        pass
    
    
    AcadDatabase = None
    
    
    AllowExtendedNames = None
    
    
    Angbase = None
    
    
    Angdir = None
    
    
    AnnoAllVisible = None
    
    
    AnnotativeDwg = None
    
    
    ApproxNumObjects = None
    
    
    Attmode = None
    
    
    Aunits = None
    
    
    Auprec = None
    
    
    BlockTableId = None
    
    
    ByBlockLinetype = None
    
    
    ByLayerLinetype = None
    
    
    CameraDisplay = None
    
    
    CameraHeight = None
    
    
    Cannoscale = None
    
    
    Cecolor = None
    
    
    Celtscale = None
    
    
    Celtype = None
    
    
    Celweight = None
    
    
    Cetransparency = None
    
    
    Chamfera = None
    
    
    Chamferb = None
    
    
    Chamferc = None
    
    
    Chamferd = None
    
    
    Clayer = None
    
    
    Cmaterial = None
    
    
    Cmljust = None
    
    
    Cmlscale = None
    
    
    CmlstyleID = None
    
    
    ColorDictionaryId = None
    
    
    ContinuousLinetype = None
    
    
    Cshadow = None
    
    
    CurrentSpaceId = None
    
    
    CurrentViewportTableRecordId = None
    
    
    DataLinkDictionaryId = None
    
    
    DataLinkManager = None
    
    
    DetailViewStyle = None
    
    
    DetailViewStyleDictionaryId = None
    
    
    DgnFrame = None
    
    
    Dimadec = None
    
    
    Dimalt = None
    
    
    Dimaltd = None
    
    
    Dimaltf = None
    
    
    Dimaltrnd = None
    
    
    Dimalttd = None
    
    
    Dimalttz = None
    
    
    Dimaltu = None
    
    
    Dimaltz = None
    
    
    Dimapost = None
    
    
    Dimarcsym = None
    
    
    Dimaso = None
    
    
    DimAssoc = None
    
    
    Dimasz = None
    
    
    Dimatfit = None
    
    
    Dimaunit = None
    
    
    Dimazin = None
    
    
    Dimblk = None
    
    
    Dimblk1 = None
    
    
    Dimblk2 = None
    
    
    Dimcen = None
    
    
    Dimclrd = None
    
    
    Dimclre = None
    
    
    Dimclrt = None
    
    
    Dimdec = None
    
    
    Dimdle = None
    
    
    Dimdli = None
    
    
    Dimdsep = None
    
    
    Dimexe = None
    
    
    Dimexo = None
    
    
    Dimfrac = None
    
    
    Dimfxlen = None
    
    
    DimfxlenOn = None
    
    
    Dimgap = None
    
    
    Dimjogang = None
    
    
    Dimjust = None
    
    
    Dimldrblk = None
    
    
    Dimlfac = None
    
    
    Dimlim = None
    
    
    Dimltex1 = None
    
    
    Dimltex2 = None
    
    
    Dimltype = None
    
    
    Dimlunit = None
    
    
    Dimlwd = None
    
    
    Dimlwe = None
    
    
    Dimpost = None
    
    
    Dimrnd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimsd1 = None
    
    
    Dimsd2 = None
    
    
    Dimse1 = None
    
    
    Dimse2 = None
    
    
    Dimsho = None
    
    
    Dimsoxd = None
    
    
    Dimstyle = None
    
    
    DimStyleTableId = None
    
    
    Dimtad = None
    
    
    Dimtdec = None
    
    
    Dimtfac = None
    
    
    Dimtfill = None
    
    
    Dimtfillclr = None
    
    
    Dimtih = None
    
    
    Dimtix = None
    
    
    Dimtm = None
    
    
    Dimtmove = None
    
    
    Dimtofl = None
    
    
    Dimtoh = None
    
    
    Dimtol = None
    
    
    Dimtolj = None
    
    
    Dimtp = None
    
    
    Dimtsz = None
    
    
    Dimtvp = None
    
    
    Dimtxsty = None
    
    
    Dimtxt = None
    
    
    Dimtzin = None
    
    
    Dimupt = None
    
    
    Dimzin = None
    
    
    DispSilh = None
    
    
    dragvs = None
    
    
    DrawOrderCtl = None
    
    
    DwfFrame = None
    
    
    DwgFileWasSavedByAutodeskSoftware = None
    
    
    DxEval = None
    
    
    Elevation = None
    
    
    EndCaps = None
    
    
    Extmax = None
    
    
    Extmin = None
    
    
    Facetres = None
    
    
    Filename = None
    
    
    Filletrad = None
    
    
    Fillmode = None
    
    
    FingerprintGuid = None
    
    
    GeoDataObject = None
    
    
    GroupDictionaryId = None
    
    
    HaloGap = None
    
    
    Handseed = None
    
    
    HideText = None
    
    
    HomeView = None
    
    
    HpInherit = None
    
    
    HpOrigin = None
    
    
    HyperlinkBase = None
    
    
    Indexctl = None
    
    
    Insbase = None
    
    
    Insunits = None
    
    
    Interferecolor = None
    
    
    Interfereobjvs = None
    
    
    Interferevpvs = None
    
    
    IntersectColor = None
    
    
    IntersectDisplay = None
    
    
    IsBeingDestroyed = None
    
    
    IsEmr = None
    
    
    Isolines = None
    
    
    IsPartiallyOpened = None
    
    
    JoinStyle = None
    
    
    LastSavedAsMaintenanceVersion = None
    
    
    LastSavedAsVersion = None
    
    
    Latitude = None
    
    
    LayerEval = None
    
    
    LayerFilters = None
    
    
    LayerNotify = None
    
    
    LayerStateManager = None
    
    
    LayerTableId = None
    
    
    LayerZero = None
    
    
    LayoutDictionaryId = None
    
    
    LensLength = None
    
    
    LightGlyphDisplay = None
    
    
    LightingUnits = None
    
    
    LightsInBlocks = None
    
    
    Limcheck = None
    
    
    Limmax = None
    
    
    Limmin = None
    
    
    LinetypeTableId = None
    
    
    LineWeightDisplay = None
    
    
    LoftAng1 = None
    
    
    LoftAng2 = None
    
    
    LoftMag1 = None
    
    
    LoftMag2 = None
    
    
    LoftNormals = None
    
    
    LoftParam = None
    
    
    Longitude = None
    
    
    Ltscale = None
    
    
    Lunits = None
    
    
    Luprec = None
    
    
    MaintenanceReleaseVersion = None
    
    
    MaterialDictionaryId = None
    
    
    Maxactvp = None
    
    
    Measurement = None
    
    
    Menu = None
    
    
    Mirrtext = None
    
    
    MLeaderscale = None
    
    
    MLeaderstyle = None
    
    
    MLeaderStyleDictionaryId = None
    
    
    MLStyleDictionaryId = None
    
    
    MsLtScale = None
    
    
    MsOleScale = None
    
    
    NamedObjectsDictionaryId = None
    
    
    NeedsRecovery = None
    
    
    NorthDirection = None
    
    
    NumberOfSaves = None
    
    
    ObjectContextManager = None
    
    
    ObscuredColor = None
    
    
    ObscuredLineType = None
    
    
    OleStartUp = None
    
    
    OriginalFileMaintenanceVersion = None
    
    
    OriginalFileName = None
    
    
    OriginalFileSavedByMaintenanceVersion = None
    
    
    OriginalFileSavedByVersion = None
    
    
    OriginalFileVersion = None
    
    
    Orthomode = None
    
    
    PaperSpaceVportId = None
    
    
    PdfFrame = None
    
    
    Pdmode = None
    
    
    Pdsize = None
    
    
    Pelevation = None
    
    
    Pextmax = None
    
    
    Pextmin = None
    
    
    Pinsbase = None
    
    
    Plimcheck = None
    
    
    Plimmax = None
    
    
    Plimmin = None
    
    
    PlineEllipse = None
    
    
    Plinegen = None
    
    
    Plinewid = None
    
    
    PlotSettingsDictionaryId = None
    
    
    PlotStyleMode = None
    
    
    PlotStyleNameDictionaryId = None
    
    
    PlotStyleNameId = None
    
    
    ProjectName = None
    
    
    Psltscale = None
    
    
    PsolHeight = None
    
    
    PsolWidth = None
    
    
    Pucs = None
    
    
    PucsBase = None
    
    
    Pucsname = None
    
    
    Pucsorg = None
    
    
    PucsOrthographic = None
    
    
    Pucsxdir = None
    
    
    Pucsydir = None
    
    
    Qtextmode = None
    
    
    RegAppTableId = None
    
    
    Regenmode = None
    
    
    RetainOriginalThumbnailBitmap = None
    
    
    Saveproxygraphics = None
    
    
    SectionManagerId = None
    
    
    SectionViewStyle = None
    
    
    SectionViewStyleDictionaryId = None
    
    
    SecurityParameters = None
    
    
    Shadedge = None
    
    
    Shadedif = None
    
    
    ShadowPlaneLocation = None
    
    
    ShowHist = None
    
    
    Sketchinc = None
    
    
    Skpoly = None
    
    
    SolidHist = None
    
    
    SortEnts = None
    
    
    Splframe = None
    
    
    Splinesegs = None
    
    
    Splinetype = None
    
    
    StepSize = None
    
    
    StepsPerSec = None
    
    
    StyleSheet = None
    
    
    SummaryInfo = None
    
    
    Surftab1 = None
    
    
    Surftab2 = None
    
    
    Surftype = None
    
    
    Surfu = None
    
    
    Surfv = None
    
    
    Tablestyle = None
    
    
    TableStyleDictionaryId = None
    
    
    Tdcreate = None
    
    
    Tdindwg = None
    
    
    Tducreate = None
    
    
    Tdupdate = None
    
    
    Tdusrtimer = None
    
    
    Tduupdate = None
    
    
    Textsize = None
    
    
    Textstyle = None
    
    
    TextStyleTableId = None
    
    
    Thickness = None
    
    
    ThumbnailBitmap = None
    
    
    TileMode = None
    
    
    TileModeLightSynch = None
    
    
    TimeZone = None
    
    
    Tracewid = None
    
    
    TransactionManager = None
    
    
    Treedepth = None
    
    
    TStackAlign = None
    
    
    TstackSize = None
    
    
    Ucs = None
    
    
    UcsBase = None
    
    
    Ucsname = None
    
    
    Ucsorg = None
    
    
    UcsOrthographic = None
    
    
    UcsTableId = None
    
    
    Ucsxdir = None
    
    
    Ucsydir = None
    
    
    UndoRecording = None
    
    
    Unitmode = None
    
    
    UpdateThumbnail = None
    
    
    Useri1 = None
    
    
    Useri2 = None
    
    
    Useri3 = None
    
    
    Useri4 = None
    
    
    Useri5 = None
    
    
    Userr1 = None
    
    
    Userr2 = None
    
    
    Userr3 = None
    
    
    Userr4 = None
    
    
    Userr5 = None
    
    
    Usrtimer = None
    
    
    VersionGuid = None
    
    
    ViewportScaleDefault = None
    
    
    ViewportTableId = None
    
    
    ViewTableId = None
    
    
    Visretain = None
    
    
    VisualStyleDictionaryId = None
    
    
    Worldview = None
    
    
    XclipFrame = None
    
    
    XrefBlockId = None
    
    
    XrefEditEnabled = None
    
    pass

class DatabaseIOEventArgs(EventArgs):
    """
    
    """
    FileName = None
    
    pass

class DatabaseSummaryInfo(public struct DatabaseSummaryInfo {
}):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input System.Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object
        """
        pass
    
    
    Author = None
    
    
    Comments = None
    
    
    CustomProperties = None
    
    
    HyperlinkBase = None
    
    
    Keywords = None
    
    
    LastSavedBy = None
    
    
    RevisionNumber = None
    
    
    Subject = None
    
    
    Title = None
    
    pass

class DatabaseSummaryInfoBuilder(public class DatabaseSummaryInfoBuilder):
    """
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    u
    
    m
    
    m
    
    a
    
    r
    
    y
    
    I
    
    n
    
    f
    
    o
    
    B
    
    u
    
    i
    
    l
    
    d
    
    e
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    u
    
    m
    
    m
    
    a
    
    r
    
    y
    
    I
    
    n
    
    f
    
    o
    
    B
    
    u
    
    i
    
    l
    
    d
    
    e
    
    r
    
    (
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    u
    
    m
    
    m
    
    a
    
    r
    
    y
    
    I
    
    n
    
    f
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    u
    
    m
    
    m
    
    a
    
    r
    
    y
    
    I
    
    n
    
    f
    
    o
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    u
    
    m
    
    m
    
    a
    
    r
    
    y
    
    I
    
    n
    
    f
    
    o
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    def ToDatabaseSummaryInfo(self):
        """
        ToDatabaseSummaryInfo -> DatabaseSummaryInfo
        
        """
        pass
    
    
    Author = None
    
    
    Comments = None
    
    
    CustomProperties = None
    
    
    Custom = None
    
    
    HyperlinkBase = None
    
    
    Keywords = None
    
    
    LastSavedBy = None
    
    
    RevisionNumber = None
    
    
    Subject = None
    
    
    Title = None
    
    pass

class DbDictionaryEnumerator(RXObject, IDictionaryEnumerator):
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
    
    
    Current = None
    
    
    Entry = None
    
    
    Key = None
    
    
    Value = None
    
    pass

class DbHomeView(DbHomeView hv = HostApplicationServices.WorkingDatabase.HomeView;
AutoCAD.Geometry.Point3d pt = new AutoCAD.Geometry.Point3d(-1, -1, -1);
hv.Center = pt;
HostApplicationServices.WorkingDatabase.HomeView = hv):
    """
    
    D
    
    b
    
    H
    
    o
    
    m
    
    e
    
    V
    
    i
    
    e
    
    w
    
    (
    
    )
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def ToggleDefaultSettings(self):
        """
        ToggleDefaultSettings -> void
        
        """
        pass
    
    
    Center = None
    
    
    Eye = None
    
    
    Height = None
    
    
    Perspective = None
    
    
    Up = None
    
    
    Width = None
    
    pass

class DecomposeForSaveReplacementRecord(public struct DecomposeForSaveReplacementRecord {
}):
    """
    
    D
    
    e
    
    c
    
    o
    
    m
    
    p
    
    o
    
    s
    
    e
    
    F
    
    o
    
    r
    
    S
    
    a
    
    v
    
    e
    
    R
    
    e
    
    p
    
    l
    
    a
    
    c
    
    e
    
    m
    
    e
    
    n
    
    t
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    r
    
    e
    
    p
    
    l
    
    a
    
    c
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    D
    
    B
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    x
    
    c
    
    h
    
    a
    
    n
    
    g
    
    e
    
    X
    
    D
    
    a
    
    t
    
    a
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    B
    
    o
    
    o
    
    l
    
    e
    
    a
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    """
    ExchangeXData = None
    
    
    ReplacementId = None
    
    
    ReplacementObject = None
    
    pass

  Block = 2
  Copy = 0
  Explode = 1
  Insert = 6
  InsertCopy = 10
  Objects = 8
  SymbolTableMerge = 4
  Wblock = 7
  WblockObjects = 11
  XrefBind = 3
  XrefInsert = 9

  OneDistantLight
  TwoDistantLights

class DetailSymbol(Entity):
    """
    
    D
    
    e
    
    t
    
    a
    
    i
    
    l
    
    S
    
    y
    
    m
    
    b
    
    o
    
    l
    
    (
    
    )
    """
    def IsOverriddenProperty(self):
        """
        IsOverriddenProperty -> bool
            
            flag: 
            Input: the NAMESPACE_ACDB::DetailViewModelEdge value to test if it is overridden
        """
        pass
    
    
    BoundarySize = None
    
    
    BoundaryType = None
    
    
    DetailViewScale = None
    
    
    Direction = None
    
    
    DisplayIdentifier = None
    
    
    Identifier = None
    
    
    IdentifierPosition = None
    
    
    ModelEdgeDirection = None
    
    
    ModelEdgeOrigin = None
    
    
    ModelEdgeType = None
    
    
    Origin = None
    
    
    OwningViewScale = None
    
    
    Scale = None
    
    
    SymbolStyleId = None
    
    pass

  CircularBoundary
  RectangularBoundary
  CustomBoundary

  IdentifierPosition = 2
  ModelEdge = 1

  OutsideBoundary
  OutsideBoundaryWithLeader
  OnBoundary
  OnBoundaryWithLeader

  Smooth
  SmoothWithBorder
  SmoothWithConnectionLine
  Jagged

class DetailViewStyle(DBObject):
    """
    
    D
    
    e
    
    t
    
    a
    
    i
    
    l
    
    V
    
    i
    
    e
    
    w
    
    S
    
    t
    
    y
    
    l
    
    e
    
    (
    
    )
    """
    def DefaultViewName(self):
        """
        DefaultViewName -> string
            
            int index: 
            The index of the default name.
        """
        pass
    
    
    def GetViewLabelPattern(self):
        """
        GetViewLabelPattern -> string
            
            Field field: 
            Input: a field object to be updated with the view label pattern master field.
        """
        pass
    
    
    def PostViewStyleToDb(self):
        """
        PostViewStyleToDb -> ObjectId
            
            Database dataBasePointer: 
            Input: database to be updated.
            
            string styleName: 
            Input: name to be used for this view style.
        """
        pass
    
    
    def SetDatabaseDefaults(self):
        """
        SetDatabaseDefaults -> void
            
            Database dataBasePointer: 
            Input: database to be used
        """
        pass
    
    
    def SetViewLabelPattern(self):
        """
        SetViewLabelPattern -> void
            
            string pattern: 
            Input: the pattern string for the view label.
            
            Field field: 
            Input: optional pointer to a Field
        """
        pass
    
    
    def ValidateViewName(self):
        """
        ValidateViewName -> bool
            
            string name: 
            Input: section name to validate.
        """
        pass
    
    
    ArrowSymbolColor = None
    
    
    ArrowSymbolId = None
    
    
    ArrowSymbolSize = None
    
    
    BorderLineColor = None
    
    
    BorderLineTypeId = None
    
    
    BorderLineWeight = None
    
    
    BoundaryLineColor = None
    
    
    BoundaryLineTypeId = None
    
    
    BoundaryLineWeight = None
    
    
    ConnectionLineColor = None
    
    
    ConnectionLineTypeId = None
    
    
    ConnectionLineWeight = None
    
    
    Description = None
    
    
    IdentifierColor = None
    
    
    IdentifierHeight = None
    
    
    IdentifierOffset = None
    
    
    IdentifierPlacement = None
    
    
    IdentifierStyleId = None
    
    
    IsModifiedForRecompute = None
    
    
    ModelEdge = None
    
    
    Name = None
    
    
    ShowArrowheads = None
    
    
    ShowViewLabel = None
    
    
    ViewLabelAlignment = None
    
    
    ViewLabelAttachment = None
    
    
    ViewLabelOffset = None
    
    
    ViewLabelPattern = None
    
    
    ViewLabelTextColor = None
    
    
    ViewLabelTextHeight = None
    
    
    ViewLabelTextStyleId = None
    
    pass

class DgnDefinition(UnderlayDefinition):
    """
    
    D
    
    g
    
    n
    
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
    
    (
    
    )
    """
    SetShowRasterRef = None
    
    
    ShowRasterRef = None
    
    
    UseMasterUnits = None
    
    
    XrefDepth = None
    
    pass

class DgnReference(UnderlayReference):
    """
    
    D
    
    g
    
    n
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    (
    
    )
    """

    pass

class DgnUnderlayItem(UnderlayItem):
    """
    
    """
    SetShowRasterRef = None
    
    
    ShowRasterRef = None
    
    
    UseMasterUnits = None
    
    pass

class DiametricDimension(Dimension):
    """
    
    D
    
    i
    
    a
    
    m
    
    e
    
    t
    
    r
    
    i
    
    c
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    """
    ChordPoint = None
    
    
    FarChordPoint = None
    
    
    LeaderLength = None
    
    pass

class DictionaryWithDefaultDictionary(DBDictionary):
    """
    
    D
    
    i
    
    c
    
    t
    
    i
    
    o
    
    n
    
    a
    
    r
    
    y
    
    W
    
    i
    
    t
    
    h
    
    D
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
    D
    
    i
    
    c
    
    t
    
    i
    
    o
    
    n
    
    a
    
    r
    
    y
    
    (
    
    )
    """
    DefaultId = None
    
    
    ObjectBirthVersion = None
    
    pass

  FirstArrow
  SecondArrow

class DimStyleTable(SymbolTable, IEnumerable):
    """
    
    """

    pass

class DimStyleTableRecord(SymbolTableRecord):
    """
    
    D
    
    i
    
    m
    
    S
    
    t
    
    y
    
    l
    
    e
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    )
    """
    def GetArrowId(self):
        """
        GetArrowId -> ObjectId
            
            DimArrowFlag whichArrow: 
            Input a dimension arrowhead
        """
        pass
    
    
    Dimadec = None
    
    
    Dimalt = None
    
    
    Dimaltd = None
    
    
    Dimaltf = None
    
    
    Dimaltrnd = None
    
    
    Dimalttd = None
    
    
    Dimalttz = None
    
    
    Dimaltu = None
    
    
    Dimaltz = None
    
    
    Dimapost = None
    
    
    Dimarcsym = None
    
    
    Dimasz = None
    
    
    Dimatfit = None
    
    
    Dimaunit = None
    
    
    Dimazin = None
    
    
    Dimblk = None
    
    
    Dimblk1 = None
    
    
    Dimblk2 = None
    
    
    Dimcen = None
    
    
    Dimclrd = None
    
    
    Dimclre = None
    
    
    Dimclrt = None
    
    
    Dimdec = None
    
    
    Dimdle = None
    
    
    Dimdli = None
    
    
    Dimdsep = None
    
    
    Dimexe = None
    
    
    Dimexo = None
    
    
    Dimfrac = None
    
    
    Dimfxlen = None
    
    
    DimfxlenOn = None
    
    
    Dimgap = None
    
    
    Dimjogang = None
    
    
    Dimjust = None
    
    
    Dimldrblk = None
    
    
    Dimlfac = None
    
    
    Dimlim = None
    
    
    Dimltex1 = None
    
    
    Dimltex2 = None
    
    
    Dimltype = None
    
    
    Dimlunit = None
    
    
    Dimlwd = None
    
    
    Dimlwe = None
    
    
    Dimpost = None
    
    
    Dimrnd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimsd1 = None
    
    
    Dimsd2 = None
    
    
    Dimse1 = None
    
    
    Dimse2 = None
    
    
    Dimsoxd = None
    
    
    Dimtad = None
    
    
    Dimtdec = None
    
    
    Dimtfac = None
    
    
    Dimtfill = None
    
    
    Dimtfillclr = None
    
    
    Dimtih = None
    
    
    Dimtix = None
    
    
    Dimtm = None
    
    
    Dimtmove = None
    
    
    Dimtofl = None
    
    
    Dimtoh = None
    
    
    Dimtol = None
    
    
    Dimtolj = None
    
    
    Dimtp = None
    
    
    Dimtsz = None
    
    
    Dimtvp = None
    
    
    Dimtxsty = None
    
    
    Dimtxt = None
    
    
    Dimtzin = None
    
    
    Dimupt = None
    
    
    Dimzin = None
    
    
    IsModifiedForRecompute = None
    
    pass

class Dimension(Entity):
    """
    
    """
    def FieldFromMText(self):
        """
        FieldFromMText -> void
            
            MText dimMText: 
            The MText object from which the text field is copied
        """
        pass
    
    
    def FieldToMText(self):
        """
        FieldToMText -> void
            
            MText dimMText: MText object to which the new field will be attached
        """
        pass
    
    
    def FormatMeasurement(self):
        """
        FormatMeasurement -> string
            
            double measurement: 
            Input measurement value.
            
            string dimensionText: 
            Input alternate value.
        """
        pass
    
    
    def GenerateLayout(self):
        """
        GenerateLayout -> void
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def RecomputeDimensionBlock(self):
        """
        RecomputeDimensionBlock -> void
            
            [MarshalAs(UnmanagedType.U1)] bool forceUpdate: 
            Boolean indicating whether or not to force an update on screen
        """
        pass
    
    
    def RemoveTextField(self):
        """
        RemoveTextField -> void
        
        """
        pass
    
    
    def ResetTextDefinedSize(self):
        """
        ResetTextDefinedSize -> void
        
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input object ID of DimStyleTableRecord from which to copy dimension variable information
        """
        pass
    
    
    AlternatePrefix = None
    
    
    AlternateSuffix = None
    
    
    AltSuppressLeadingZeros = None
    
    
    AltSuppressTrailingZeros = None
    
    
    AltSuppressZeroFeet = None
    
    
    AltSuppressZeroInches = None
    
    
    AltToleranceSuppressLeadingZeros = None
    
    
    AltToleranceSuppressTrailingZeros = None
    
    
    AltToleranceSuppressZeroFeet = None
    
    
    AltToleranceSuppressZeroInches = None
    
    
    CenterMarkSize = None
    
    
    CenterMarkType = None
    
    
    Dimadec = None
    
    
    Dimalt = None
    
    
    Dimaltd = None
    
    
    Dimaltf = None
    
    
    Dimaltrnd = None
    
    
    Dimalttd = None
    
    
    Dimalttz = None
    
    
    Dimaltu = None
    
    
    Dimaltz = None
    
    
    Dimapost = None
    
    
    Dimarcsym = None
    
    
    Dimasz = None
    
    
    Dimatfit = None
    
    
    Dimaunit = None
    
    
    Dimazin = None
    
    
    Dimblk = None
    
    
    Dimblk1 = None
    
    
    Dimblk2 = None
    
    
    DimBlockId = None
    
    
    DimBlockPosition = None
    
    
    Dimcen = None
    
    
    Dimclrd = None
    
    
    Dimclre = None
    
    
    Dimclrt = None
    
    
    Dimdec = None
    
    
    Dimdle = None
    
    
    Dimdli = None
    
    
    Dimdsep = None
    
    
    DimensionStyle = None
    
    
    DimensionStyleName = None
    
    
    DimensionText = None
    
    
    Dimexe = None
    
    
    Dimexo = None
    
    
    Dimfrac = None
    
    
    Dimfxlen = None
    
    
    DimfxlenOn = None
    
    
    Dimgap = None
    
    
    Dimjogang = None
    
    
    Dimjust = None
    
    
    Dimldrblk = None
    
    
    Dimlfac = None
    
    
    Dimlim = None
    
    
    Dimltex1 = None
    
    
    Dimltex2 = None
    
    
    Dimltype = None
    
    
    Dimlunit = None
    
    
    Dimlwd = None
    
    
    Dimlwe = None
    
    
    Dimpost = None
    
    
    Dimrnd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimsd1 = None
    
    
    Dimsd2 = None
    
    
    Dimse1 = None
    
    
    Dimse2 = None
    
    
    Dimsoxd = None
    
    
    Dimtad = None
    
    
    Dimtdec = None
    
    
    Dimtfac = None
    
    
    Dimtfill = None
    
    
    Dimtfillclr = None
    
    
    Dimtih = None
    
    
    Dimtix = None
    
    
    Dimtm = None
    
    
    Dimtmove = None
    
    
    Dimtofl = None
    
    
    Dimtoh = None
    
    
    Dimtol = None
    
    
    Dimtolj = None
    
    
    Dimtp = None
    
    
    Dimtsz = None
    
    
    Dimtvp = None
    
    
    Dimtxt = None
    
    
    Dimtzin = None
    
    
    Dimupt = None
    
    
    Dimzin = None
    
    
    DynamicDimension = None
    
    
    Elevation = None
    
    
    HorizontalRotation = None
    
    
    Measurement = None
    
    
    Normal = None
    
    
    Prefix = None
    
    
    Suffix = None
    
    
    SuppressAngularLeadingZeros = None
    
    
    SuppressAngularTrailingZeros = None
    
    
    SuppressLeadingZeros = None
    
    
    SuppressTrailingZeros = None
    
    
    SuppressZeroFeet = None
    
    
    SuppressZeroInches = None
    
    
    TextAttachment = None
    
    
    TextDefinedSize = None
    
    
    TextLineSpacingFactor = None
    
    
    TextLineSpacingStyle = None
    
    
    TextPosition = None
    
    
    TextRotation = None
    
    
    ToleranceSuppressLeadingZeros = None
    
    
    ToleranceSuppressTrailingZeros = None
    
    
    ToleranceSuppressZeroFeet = None
    
    
    ToleranceSuppressZeroInches = None
    
    
    UsingDefaultTextPosition = None
    
    pass

  Mark
  Line
  None

class DimensionStyleOverrule(Overrule):
    """
    
    """
    def DimensionStyle(self):
        """
        DimensionStyle -> ObjectId
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            DimStyleTableRecord style: 
            Existing DimStyleTableRecord to which the dimension variable data will be copied.
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetDimensionStyle(self):
        """
        SetDimensionStyle -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            ObjectId id: 
            Input the object ID of the desired DimStyleTableRecord to be used by the dimension.
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData(Dimension, DimStyleTableRecord) -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            DimStyleTableRecord style: 
            DimStyleTableRecord from which to copy the dimension variable information.
        SetDimstyleData(Dimension, ObjectId) -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            ObjectId dimstyleId: 
            Object ID of DimStyleTableRecord from which to copy dimension variable information.
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Name of dictionary entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Array of ids defining the lookup table
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Name of the registered application.
        """
        pass
    
    pass

class DistanceConstraint(ExplicitConstraint):
    """
    
    D
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
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
    
     
    
    A
    
    c
    
    G
    
    e
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    x
    
    e
    
    d
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    i
    
    s
    
     
    
    u
    
    s
    
    e
    
    d
    
     
    
    t
    
    o
    
     
    
    m
    
    e
    
    a
    
    s
    
    u
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    .
    
     
    
    T
    
    h
    
    e
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    l
    
    e
    
    n
    
    g
    
    t
    
    h
    
     
    
    m
    
    u
    
    s
    
    t
    
     
    
    n
    
    o
    
    t
    
     
    
    b
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    u
    
    i
    
    n
    
    t
    
    ,
    
     
    
    D
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    D
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    T
    
    y
    
    p
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    u
    
    i
    
    n
    
    t
    
     
    
    c
    
    o
    
    n
    
    s
    
    L
    
    i
    
    n
    
    e
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    A
    
    c
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    G
    
    r
    
    o
    
    u
    
    p
    
    N
    
    o
    
    d
    
    e
    
    I
    
    d
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    e
    
    d
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    w
    
    h
    
    o
    
    s
    
    e
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    i
    
    s
    
     
    
    u
    
    s
    
    e
    
    d
    
     
    
    t
    
    o
    
     
    
    m
    
    e
    
    a
    
    s
    
    u
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    D
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
     
    
    D
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    T
    
    y
    
    p
    
    e
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    m
    
    u
    
    s
    
    t
    
     
    
    b
    
    e
    
     
    
    e
    
    i
    
    t
    
    h
    
    e
    
    r
    
     
    
    P
    
    e
    
    r
    
    p
    
    e
    
    n
    
    d
    
    i
    
    c
    
    u
    
    l
    
    a
    
    r
    
    T
    
    o
    
    L
    
    i
    
    n
    
    e
    
     
    
    o
    
    r
    
     
    
    P
    
    a
    
    r
    
    a
    
    l
    
    l
    
    e
    
    l
    
    T
    
    o
    
    L
    
    i
    
    n
    
    e
    
    .
    """
      NotDirected
      FixedDirection
      PerpendicularToLine
      ParallelToLine
    
    
    ConstrainedLineId = None
    
    
    Direction = None
    
    
    DirectionType = None
    
    pass

  DragStart
  DragEnd
  DragAbort

  DrawLeaderHeadFirst
  DrawLeaderTailFirst

  DrawContentFirst
  DrawLeaderFirst

class DrawOrderTable(DBObject):
    """
    
    """
    def FirstEntityIsDrawnBeforeSecond(self):
        """
        FirstEntityIsDrawnBeforeSecond -> bool
            
            ObjectId first: 
            Input first object ID
            
            ObjectId second: 
            Input second object ID
        """
        pass
    
    
    def GetFullDrawOrder(self):
        """
        GetFullDrawOrder -> ObjectIdCollection
            
            byte honorSortEntitiesMask: 
            Input indicating whether to test the host database's $SORTENTS variable
        """
        pass
    
    
    def GetRelativeDrawOrder(self):
        """
        GetRelativeDrawOrder -> ObjectIdCollection
            
            byte honorSortEntitiesMask: 
            Input indicating whether to test the host database's $SORTENTS variable
        """
        pass
    
    
    def GetSortHandle(self):
        """
        GetSortHandle -> Handle
            
            ObjectId id: 
            Input object ID
        """
        pass
    
    
    def MoveAbove(self):
        """
        MoveAbove -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
            
            ObjectId target: 
            Target entity
        """
        pass
    
    
    def MoveBelow(self):
        """
        MoveBelow -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
            
            ObjectId target: 
            Target entity
        """
        pass
    
    
    def MoveToBottom(self):
        """
        MoveToBottom -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
        """
        pass
    
    
    def MoveToTop(self):
        """
        MoveToTop -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
        """
        pass
    
    
    def SetRelativeDrawOrder(self):
        """
        SetRelativeDrawOrder -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
        """
        pass
    
    
    def SwapOrder(self):
        """
        SwapOrder -> void
            
            ObjectId id1: 
            Object ID of first entity
            
            ObjectId id2: 
            Object ID of second entity
        """
        pass
    
    
    BlockId = None
    
    pass

  NotApplicable
  Ignore
  Replace
  RefMangleName
  MangleName
  UnmangleName

class DwfDefinition(UnderlayDefinition):
    """
    
    D
    
    w
    
    f
    
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
    
    (
    
    )
    """
    isDWFx = None
    
    pass

class DwfReference(UnderlayReference):
    """
    
    D
    
    w
    
    f
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    (
    
    )
    """

    pass

class DwgFiler(RXObject):
    """
    
    D
    
    w
    
    g
    
    F
    
    i
    
    l
    
    e
    
    r
    
    (
    
    )
    """
    def ReadAddress(self):
        """
        ReadAddress -> IntPtr
        
        """
        pass
    
    
    def ReadBinaryChunk(self):
        """
        ReadBinaryChunk -> byte()
        
        """
        pass
    
    
    def ReadBoolean(self):
        """
        ReadBoolean -> bool
        
        """
        pass
    
    
    def ReadByte(self):
        """
        ReadByte -> byte
        
        """
        pass
    
    
    def ReadBytes(self):
        """
        ReadBytes -> void
            
            byte[] value: 
            A pre-allocated memory area to read bytes into
        """
        pass
    
    
    def ReadDouble(self):
        """
        ReadDouble -> double
        
        """
        pass
    
    
    def ReadHandle(self):
        """
        ReadHandle -> Handle
        
        """
        pass
    
    
    def ReadHardOwnershipId(self):
        """
        ReadHardOwnershipId -> ObjectId
        
        """
        pass
    
    
    def ReadHardPointerId(self):
        """
        ReadHardPointerId -> ObjectId
        
        """
        pass
    
    
    def ReadInt16(self):
        """
        ReadInt16 -> short
        
        """
        pass
    
    
    def ReadInt32(self):
        """
        ReadInt32 -> Integer
        
        """
        pass
    
    
    def ReadInt64(self):
        """
        ReadInt64 -> long
        
        """
        pass
    
    
    def ReadPoint2d(self):
        """
        ReadPoint2d -> Point2d
        
        """
        pass
    
    
    def ReadPoint3d(self):
        """
        ReadPoint3d -> Point3d
        
        """
        pass
    
    
    def ReadScale3d(self):
        """
        ReadScale3d -> Scale3d
        
        """
        pass
    
    
    def ReadSoftOwnershipId(self):
        """
        ReadSoftOwnershipId -> ObjectId
        
        """
        pass
    
    
    def ReadSoftPointerId(self):
        """
        ReadSoftPointerId -> ObjectId
        
        """
        pass
    
    
    def ReadString(self):
        """
        ReadString -> string
        
        """
        pass
    
    
    def ReadUInt16(self):
        """
        ReadUInt16 -> ushort
        
        """
        pass
    
    
    def ReadUInt32(self):
        """
        ReadUInt32 -> UInteger
        
        """
        pass
    
    
    def ReadUInt64(self):
        """
        ReadUInt64 -> ulong
        
        """
        pass
    
    
    def ReadVector2d(self):
        """
        ReadVector2d -> Vector2d
        
        """
        pass
    
    
    def ReadVector3d(self):
        """
        ReadVector3d -> Vector3d
        
        """
        pass
    
    
    def ResetFilerStatus(self):
        """
        ResetFilerStatus -> void
        
        """
        pass
    
    
    def Seek(self):
        """
        Seek -> void
        
        """
        pass
    
    
    def WriteAddress(self):
        """
        WriteAddress -> void
            
            IntPtr value: 
            Location to write to
        """
        pass
    
    
    def WriteBinaryChunk(self):
        """
        WriteBinaryChunk -> void
            
            byte[] chunk: 
            Location to write to
        """
        pass
    
    
    def WriteBoolean(self):
        """
        WriteBoolean -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Location to write to
        """
        pass
    
    
    def WriteByte(self):
        """
        WriteByte -> void
            
            byte value: 
            Location to write to
        """
        pass
    
    
    def WriteBytes(self):
        """
        WriteBytes -> void
            
            byte[] value: 
            Location to write to
        """
        pass
    
    
    def WriteDouble(self):
        """
        WriteDouble -> void
            
            double value: 
            Location to write to
        """
        pass
    
    
    def WriteHandle(self):
        """
        WriteHandle -> void
            
            Handle handle: 
            Location to write to
        """
        pass
    
    
    def WriteHardOwnershipId(self):
        """
        WriteHardOwnershipId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteHardPointerId(self):
        """
        WriteHardPointerId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteInt16(self):
        """
        WriteInt16 -> void
            
            short value: 
            Location to write to
        """
        pass
    
    
    def WriteInt32(self):
        """
        WriteInt32 -> void
            
            int value: 
            Location to write to
        """
        pass
    
    
    def WriteInt64(self):
        """
        WriteInt64 -> void
        
        """
        pass
    
    
    def WritePoint2d(self):
        """
        WritePoint2d -> void
            
            Point2d value: 
            Location to write to
        """
        pass
    
    
    def WritePoint3d(self):
        """
        WritePoint3d -> void
            
            Point3d value: 
            Location to write to
        """
        pass
    
    
    def WriteScale3d(self):
        """
        WriteScale3d -> void
            
            Scale3d value: 
            Location to write to
        """
        pass
    
    
    def WriteSoftOwnershipId(self):
        """
        WriteSoftOwnershipId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteSoftPointerId(self):
        """
        WriteSoftPointerId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteString(self):
        """
        WriteString -> void
            
            string value: 
            Location to write to
        """
        pass
    
    
    def WriteUInt16(self):
        """
        WriteUInt16 -> void
            
            ushort value: 
            Location to write to
        """
        pass
    
    
    def WriteUInt32(self):
        """
        WriteUInt32 -> void
            
            uint value: 
            Location to write to
        """
        pass
    
    
    def WriteUInt64(self):
        """
        WriteUInt64 -> void
        
        """
        pass
    
    
    def WriteVector2d(self):
        """
        WriteVector2d -> void
            
            Vector2d value: 
            Location to write to
        """
        pass
    
    
    def WriteVector3d(self):
        """
        WriteVector3d -> void
            
            Vector3d value: 
            Location to write to
        """
        pass
    
    
    DwgVersion = None
    
    
    ExtendedMinorVersion = None
    
    
    FilerStatus = None
    
    
    FilerType = None
    
    
    Position = None
    
    pass

AC1001 = 8
AC1002 = 9
AC1003 = 10
AC1004 = 11
AC1005 = 12
AC1006 = 13
AC1007 = 14
AC1008 = 15
AC1009 = 0x10
AC1010 = 0x11
AC1011 = 0x12
AC1012 = 0x13
AC1013 = 20
AC1014 = 0x15
AC1015 = 0x17
AC1021 = 0x1b
AC1024 = 0x1d
AC1027 = 0x1f
AC1500 = 0x16
AC1800 = 0x19
AC1800a = 0x18
AC1To2 = 1
AC1To40 = 2
AC1To50 = 3
AC2100a = 0x1a
AC2400a = 0x1c
AC2700a = 30
AC2To10 = 5
AC2To20 = 4
AC2To21 = 6
AC2To22 = 7
Current = 0x1f
Max = 0x7fff
MC0To0 = 0
Newest = 0x1f
Unknown = 0x7ffe

  Alpha = 440
  Angle = 50
  ArbitraryHandle = 320
  AttributePrompt = 3
  AttributeTag = 2
  BinaryChunk = 310
  BlockName = 2
  Bool = 290
  CircleSides = 0x48
  CLShapeName = 4
  CLShapeText = 9
  Color = 0x3e
  ColorName = 430
  ColorRgb = 420
  Comment = 0x3e7
  ControlString = 0x66
  DashLength = 0x31
  Description = 3
  DimBlk1 = 6
  DimBlk2 = 7
  DimensionAlternativePrefixSuffix = 4
  DimensionBlock = 5
  DimPostString = 3
  DimStyleName = 3
  DimVarHandle = 0x69
  Elevation = 0x26
  EmbeddedObjectStart = 0x65
  End = -1
  ExtendedDataAsciiString = 0x3e8
  ExtendedDataBinaryChunk = 0x3ec
  ExtendedDataControlString = 0x3ea
  ExtendedDataDist = 0x411
  ExtendedDataHandle = 0x3ed
  ExtendedDataInteger16 = 0x42e
  ExtendedDataInteger32 = 0x42f
  ExtendedDataLayerName = 0x3eb
  ExtendedDataReal = 0x410
  ExtendedDataRegAppName = 0x3e9
  ExtendedDataScale = 0x412
  ExtendedDataWorldXCoordinate = 0x3f3
  ExtendedDataWorldXDir = 0x3f5
  ExtendedDataWorldXDisp = 0x3f4
  ExtendedDataWorldYCoordinate = 0x3fd
  ExtendedDataWorldYDir = 0x3ff
  ExtendedDataWorldYDisp = 0x3fe
  ExtendedDataWorldZCoordinate = 0x407
  ExtendedDataWorldZDir = 0x409
  ExtendedDataWorldZDisp = 0x408
  ExtendedDataXCoordinate = 0x3f2
  ExtendedDataYCoordinate = 0x3fc
  ExtendedDataZCoordinate = 0x406
  ExtendedInt16 = 400
  FirstEntityId = -2
  GradientAngle = 460
  GradientColCount = 0x1c5
  GradientColVal = 0x1cf
  GradientName = 470
  GradientObjType = 450
  GradientPatType = 0x1c3
  GradientShift = 0x1cd
  GradientTintType = 0x1c4
  GradientTintVal = 0x1ce
  Handle = 5
  HardOwnershipId = 360
  HardPointerId = 340
  HasSubentities = 0x42
  HeaderId = -2
  Int16 = 70
  Int32 = 90
  Int64 = 160
  Int8 = 280
  Invalid = -9999
  LayerLinetype = 0x3d
  LayerName = 8
  LayoutName = 410
  LinetypeAlign = 0x48
  LinetypeElement = 0x31
  LinetypeName = 6
  LinetypePdc = 0x49
  LinetypeProse = 3
  LinetypeScale = 0x30
  LineWeight = 370
  MlineOffset = 0x31
  MlineStyleName = 2
  NormalX = 210
  NormalY = 220
  NormalZ = 230
  Operator = -4
  PixelScale = 0x2f
  PlotStyleNameId = 390
  PlotStyleNameType = 380
  PReactors = -5
  Real = 40
  RegAppFlags = 0x47
  RenderMode = 0x119
  ShapeName = 2
  ShapeScale = 0x2e
  ShapeXOffset = 0x2c
  ShapeYOffset = 0x2d
  SoftOwnershipId = 350
  SoftPointerId = 330
  Start = 0
  Subclass = 100
  SymbolTableName = 2
  SymbolTableRecordComments = 4
  SymbolTableRecordName = 2
  Text = 1
  TextBigFontFile = 4
  TextFontFile = 3
  TextStyleName = 7
  Thickness = 0x27
  TxtSize = 40
  TxtStyleFlags = 0x47
  TxtStylePSize = 0x2a
  TxtStyleXScale = 0x29
  UcsOrg = 110
  UcsOrientationX = 0x6f
  UcsOrientationY = 0x70
  ViewBackClip = 0x2c
  ViewBrightness = 0x8d
  ViewContrast = 0x8e
  ViewFrontClip = 0x2b
  ViewHeight = 0x2d
  ViewLensLength = 0x2a
  ViewMode = 0x47
  ViewportActive = 0x44
  ViewportAspect = 0x29
  ViewportGrid = 0x4c
  ViewportHeight = 40
  ViewportIcon = 0x4a
  ViewportNumber = 0x45
  ViewportSnap = 0x4b
  ViewportSnapAngle = 50
  ViewportSnapPair = 0x4e
  ViewportSnapStyle = 0x4d
  ViewportTwist = 0x33
  ViewportVisibility = 0x43
  ViewportZoom = 0x49
  ViewWidth = 0x29
  Visibility = 60
  XCoordinate = 10
  XDataStart = -3
  XDictionary = -6
  XInt16 = 170
  XReal = 140
  XRefPath = 1
  XTextString = 300
  XXInt16 = 270
  YCoordinate = 20
  ZCoordinate = 30

class DxfFiler(RXObject):
    """
    
    """
    def AtSubclassData(self):
        """
        AtSubclassData -> bool
            
            string value: 
            subClassName that should be compared
        """
        pass
    
    
    def FilerStatus(self):
        """
        FilerStatus -> void
        
        """
        pass
    
    
    def HaltAtClassBoundaries(self):
        """
        HaltAtClassBoundaries -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input Boolean indicating whether or not to halt at certain key markers in the file
        """
        pass
    
    
    def PushBackItem(self):
        """
        PushBackItem -> void
        
        """
        pass
    
    
    def ReadResultBuffer(self):
        """
        ReadResultBuffer -> ResultBuffer
        
        """
        pass
    
    
    def ResetFilerStatus(self):
        """
        ResetFilerStatus -> void
        
        """
        pass
    
    
    def RewindFiler(self):
        """
        RewindFiler -> Integer
        
        """
        pass
    
    
    def SetError(self):
        """
        SetError(string, params string[]) -> void
            
            string format: 
            Input error message string
            
            params string[] values: 
            Input arguments to replace any formatting codes in the error message text
        SetError(Autodesk.AutoCAD.Runtime.ErrorStatus, string, params string[]) -> void
            
            Autodesk.AutoCAD.Runtime.ErrorStatus value: 
            Input ErrorStatus error code
            
            string format: 
            Input error message string
            
            params string[] values: 
            Input arguments to replace any formatting codes in the error message text
        """
        pass
    
    
    def WriteBool(self):
        """
        WriteBool -> void
            
            DxfCode opCode: 
            Input DXF group code to be written out
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input boolean value to be written out
        """
        pass
    
    
    def WriteBoolean(self):
        """
        WriteBoolean -> void
            
            DxfCode opCode: 
            DXF group code to be written out Boolean to be written out
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input boolean value to be written out
        """
        pass
    
    
    def WriteByte(self):
        """
        WriteByte -> void
            
            DxfCode opCode: 
            Input DXF group code to be written out
            
            byte value: 
            Input byte value to be written out
        """
        pass
    
    
    def WriteBytes(self):
        """
        WriteBytes -> void
            
            DxfCode opCode: 
            Input DXF group code to be written out
            
            byte[] chunk: 
            Input byte array to be written out
        """
        pass
    
    
    def WriteDouble(self):
        """
        WriteDouble -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            double value: 
            Double to be written out
            
            int precision: 
            _nt_
        """
        pass
    
    
    def WriteEmbeddedObjectStart(self):
        """
        WriteEmbeddedObjectStart -> void
        
        """
        pass
    
    
    def WriteHandle(self):
        """
        WriteHandle -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Handle value: 
            Input Handle value to be written out
        """
        pass
    
    
    def WriteInt16(self):
        """
        WriteInt16 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            short value: 
            Input System.Int16 value to be written out
        """
        pass
    
    
    def WriteInt32(self):
        """
        WriteInt32 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            int value: 
            Input System.Int32 value to be written out
        """
        pass
    
    
    def WriteInt64(self):
        """
        WriteInt64 -> void
        
        """
        pass
    
    
    def WriteObjectId(self):
        """
        WriteObjectId -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            ObjectId value: 
            Input object ID value to be written out
        """
        pass
    
    
    def WritePoint2d(self):
        """
        WritePoint2d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Point2d value: 
            2D point to be written out
            
            int precision: 
            Decimal places to use when writing out the coordinate double values
        """
        pass
    
    
    def WritePoint3d(self):
        """
        WritePoint3d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Point3d value: 
            3D point to be written out
            
            int precision: 
            Decimal places to use when writing out the coordinate double values
        """
        pass
    
    
    def WriteResultBuffer(self):
        """
        WriteResultBuffer -> void
            
            ResultBuffer buffer: 
            Resbuf structure to be written out
        """
        pass
    
    
    def WriteScale3d(self):
        """
        WriteScale3d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Scale3d value: Scale3d object to be written out
            
            int precision: 
            Decimal places to use when writing out the Scale3d object
        """
        pass
    
    
    def WriteString(self):
        """
        WriteString -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            string value: 
            Input System.String value to be written out
        """
        pass
    
    
    def WriteUInt16(self):
        """
        WriteUInt16 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            ushort value: 
            Input System.UInt16 value to be written out
        """
        pass
    
    
    def WriteUInt32(self):
        """
        WriteUInt32 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            uint value: 
            Input System.UInt32 value to be written out
        """
        pass
    
    
    def WriteUInt64(self):
        """
        WriteUInt64 -> void
        
        """
        pass
    
    
    def WriteVector2d(self):
        """
        WriteVector2d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Vector2d value: 
            2D vector to be written out
            
            int precision: 
            Decimal places to use when writing out the 2D vector
        """
        pass
    
    
    def WriteVector3d(self):
        """
        WriteVector3d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Vector3d value: 
            3D vector to be written out
            
            int precision: 
            Decimal places to use when writing out the 3D vector
        """
        pass
    
    
    def WriteXDataStart(self):
        """
        WriteXDataStart -> void
        
        """
        pass
    
    
    AtEmbeddedObjectStart = None
    
    
    AtEndOfFile = None
    
    
    AtEndOfObject = None
    
    
    AtExtendedData = None
    
    
    Database = None
    
    
    DwgVersion = None
    
    
    Elevation = None
    
    
    ErrorMessage = None
    
    
    ExtendedMinorVersion = None
    
    
    FilerType = None
    
    
    IncludesDefaultValues = None
    
    
    IsModifyingExistingObject = None
    
    
    Precision = None
    
    
    Thickness = None
    
    pass

class DynamicBlockReferenceProperty(public sealed class DynamicBlockReferenceProperty):
    """
    
    """
    def GetAllowedValues(self):
        """
        GetAllowedValues -> object()
        
        """
        pass
    
    
    BlockId = None
    
    
    Description = None
    
    
     = None
    
    
     = None
    
    
    ReadOnly = None
    
    
    Show = None
    
    
    UnitsType = None
    
    
    Value = None
    
    
    VisibleInCurrentVisibilityState = None
    
    pass

class DynamicBlockReferencePropertyCollection(DisposableWrapper, ICollection, IEnumerable):
    """
    
    """
    def CopyTo(self):
        """
        CopyTo -> void
            
            DynamicBlockReferenceProperty[] array: 
            Input array to copy from
            
            int index: 
            Input zero-based index to start at
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class DynamicBlockReferencePropertyCollectionEnumerator(IEnumerator):
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
    
    
    Current = None
    
    pass

  NoUnits
  Angular
  Distance
  Area

class DynamicDimensionChangedEventArgs(EventArgs):
    """
    
    D
    
    y
    
    n
    
    a
    
    m
    
    i
    
    c
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    l
    
    o
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    """
    Index = None
    
    
    Value = None
    
    pass

class DynamicDimensionData(DisposableWrapper):
    """
    
    D
    
    y
    
    n
    
    a
    
    m
    
    i
    
    c
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    D
    
    a
    
    t
    
    a
    
    (
    
    )
    
    (
    
    )
    """
    ApplicationData = None
    
    
    Dimension = None
    
    
    Editable = None
    
    
    Focal = None
    
    
    HideIfValueIsZero = None
    
    
    Visible = None
    
    pass

class DynamicDimensionDataCollection(DisposableWrapper, ICollection):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            DynamicDimensionData data: 
            A DynamicDimensionData object to add.
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DynamicDimensionData[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to begin at
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int i: 
            The position of the item to be removed.
        """
        pass
    
    
    Count = None
    
    pass

class EdgeRef(SubentRef):
    """
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    ,
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    ,
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    ,
    
     
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
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
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    (
    
    I
    
    n
    
    t
    
    P
    
    t
    
    r
    
    ,
    
     
    
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
    
    )
    
    (
    
    )
    """
    Curve = None
    
    
    FaceSubentity = None
    
    pass

class Ellipse(Curve):
    """
    
    E
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    u
    
    n
    
    i
    
    t
    
    N
    
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
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
    i
    
    n
    
    g
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
    ,
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    d
    
    e
    
    t
    
    e
    
    r
    
    m
    
    i
    
    n
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
    A
    
    x
    
    i
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    r
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    s
    
     
    
    1
    
    /
    
    2
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
     
    
    a
    
    x
    
    i
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
    R
    
    a
    
    t
    
    i
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    r
    
    a
    
    t
    
    i
    
    o
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    i
    
    n
    
    o
    
    r
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
     
    
    i
    
    n
    
     
    
    r
    
    a
    
    d
    
    i
    
    a
    
    n
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    e
    
    n
    
    d
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    n
    
    d
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
     
    
    i
    
    n
    
     
    
    r
    
    a
    
    d
    
    i
    
    a
    
    n
    
    s
    """
    def GetAngleAtParameter(self):
        """
        GetAngleAtParameter -> double
            
            double value: 
            Input parameter to evaluate
        """
        pass
    
    
    def GetParameterAtAngle(self):
        """
        GetParameterAtAngle -> double
            
            double angle: 
            Input angle (in radians) at which the parameter is desired
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            Point3d center: 
            Input center point (in WCS coordinates) for the ellipse
            
            Vector3d unitNormal: 
            Input normal vector (in WCS coordinates) which defines the plane in which the ellipse lies
            
            Vector3d majorAxis: 
            Input major axis (in WCS coordinates) for the ellipse
            
            double radiusRatio: 
            Input desired ratio of the major radius to the minor radius
            
            double startAngle: 
            Input start angle (in radians) for the ellipse
            
            double endAngle: 
            Input end angle (in radians) for the ellipse
        """
        pass
    
    
    Center = None
    
    
    EndAngle = None
    
    
    EndParam = None
    
    
    IsNull = None
    
    
    MajorAxis = None
    
    
    MajorRadius = None
    
    
    MinorAxis = None
    
    
    MinorRadius = None
    
    
    Normal = None
    
    
    RadiusRatio = None
    
    
    StartAngle = None
    
    
    StartParam = None
    
    pass

  None
  Round
  Angle
  Square

class Entity(DBObject):
    """
    
    """
    def AddSubentityPaths(self):
        """
        AddSubentityPaths -> void
            
            FullSubentityPath[] subPaths: 
            Input an array of FullSubentityPath identifiers to add to the entity.
        """
        pass
    
    
    def BoundingBoxIntersectWith(self):
        """
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Plane projectionPlane: 
            Input projection plane for the apparent intersection of the two entities
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Plane projectionPlane: 
            Input projection plane for the apparent intersection of the two entities
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        """
        pass
    
    
    def DeleteSubentityPaths(self):
        """
        DeleteSubentityPaths -> void
            
            FullSubentityPath[] subPaths: 
            Input an array of FullSubentityPath identifiers to delete from the entity
        """
        pass
    
    
    def Draw(self):
        """
        Draw -> void
        
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> void
            
            DBObjectCollection entitySet: 
            Input collection of pointers to new entities; this array may already contain pointers from other entities' explode() methods
        """
        pass
    
    
    def GetGripPoints(self):
        """
        GetGripPoints(GripDataCollection, double, int, Vector3d, GetGripPointsFlags) -> bool
        
        GetGripPoints(Point3dCollection, IntegerCollection, IntegerCollection) -> void
            
            Point3dCollection gripPoints: 
            Input pre-existing array to append the grip points to; output with the entity's grip points appended
            
            IntegerCollection snapModes: 
            not currently used
            
            IntegerCollection geometryIds: 
            not currently used
        """
        pass
    
    
    def GetGraphicsMarkersAtSubentityPathIntPtr(self):
        """
        GetGraphicsMarkersAtSubentityPathIntPtr -> IntPtrCollection
            
            FullSubentityPath subPath: 
            Input FullSubentityPath object that contains an SubentId property with the information necessary to determine the subentity (or subentities) for which the GS Marker(s) is requested.
        """
        pass
    
    
    def GetGripPointsAtSubentityPath(self):
        """
        GetGripPointsAtSubentityPath -> bool
        
        """
        pass
    
    
    def GetObjectSnapPoints(self):
        """
        GetObjectSnapPoints(ObjectSnapModes, int, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection) -> void
            
            ObjectSnapModes snapMode: 
            Input osnap mode being requested
            
            int gsSelectionMark: 
            Input GS marker of the subentity involved in the object snap operation
            
            Point3d pickPoint: 
            Input point (in WCS coordinates) picked during the object snap operation
            
            Point3d lastPoint: 
            Input point (in WCS coordinates) selected just before pickPoint
            
            Matrix3d viewTransform: 
            Input transformation matrix to transform from WCS to DCS
            
            Point3dCollection snapPoints: 
            Input pre-existing array to append osnap points to (may already contain points); output with object snap points appended
            
            IntegerCollection geometryIds: 
            Not in use
            ObjectSnapModes.ModeEnd: 
            Find the endpoint on the entity that is nearest to the pickPoint.
            ObjectSnapModes.ModeMid: 
            Find the midpoint (of any line, arc, etc., subentity) that is nearest to the pickPoint
            ObjectSnapModes.ModeCenter : 
            Find the center point (of any circle or arc subentity) that is nearest to the pickPoint
            ObjectSnapModes.ModeNode: 
            Find the node point (for example, dimension node points) that is nearest to the pickPoint
            ObjectSnapModes.ModeQuad : 
            Find the quad point (traditionally the four quadrant points on a circle) that's nearest to pickPoint
            ObjectSnapModes.ModeIns : 
            Find the intersection point of the entity and a line perpendicular to the entity that passes through lastPoint
            ObjectSnapModes.ModePerpindicular: 
            Find the intersection point of the entity and a line perpendicular to the entity that passes through lastPoint
            ObjectSnapModes.ModeTangent : 
            Find a point on the entity where a line that passes through lastPoint will be tangent to the entity
            ObjectSnapModes.ModeNear : 
            Find the point on the entity that's nearest to pickPoint. You decide what 'nearest' means
        GetObjectSnapPoints(ObjectSnapModes, int, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection, Matrix3d) -> void
            
            ObjectSnapModes snapMode: 
            Input osnap mode being requested
            
            int gsSelectionMark: 
            Input GS marker of the subentity involved in the object snap operation
            
            Point3d pickPoint: 
            Input point (in WCS coordinates) picked during the object snap operation
            
            Point3d lastPoint: 
            Input point (in WCS coordinates) selected just before pickPoint
            
            Matrix3d viewTransform: 
            Input transformation matrix to transform from WCS to DCS
            
            Point3dCollection snapPoints: 
            Input pre-existing array to append osnap points to (may already contain points); output with object snap points appended
            
            IntegerCollection geometryIds: 
            Not in use
            
            Matrix3d insertionMat: 
            Input block transformation
        """
        pass
    
    
    def GetPlane(self):
        """
        GetPlane -> Plane
        
        """
        pass
    
    
    def GetStretchPoints(self):
        """
        GetStretchPoints -> void
            
            Point3dCollection stretchPoints: 
            Input pre-existing array to append the stretch points to; output with the entity's stretch points appended
        """
        pass
    
    
    def GetSubentity(self):
        """
        GetSubentity -> Entity
            
            FullSubentityPath id: 
            Input the path to the subentity
        """
        pass
    
    
    def GetSubentityGeometricExtents(self):
        """
        GetSubentityGeometricExtents -> Extents3d
            
            FullSubentityPath subPath: 
            Input the path to the subentity
        """
        pass
    
    
    def GetSubentityPathsAtGraphicsMarker(self):
        """
        GetSubentityPathsAtGraphicsMarker(SubentityType, IntPtr, Point3d, Matrix3d, ObjectId[]) -> FullSubentityPath()
        
        GetSubentityPathsAtGraphicsMarker(SubentityType, long, Point3d, Matrix3d, int, ObjectId[]) -> FullSubentityPath()
        
        """
        pass
    
    
    def GetTransformedCopy(self):
        """
        GetTransformedCopy -> Entity
            
            Matrix3d transform: 
            Input matrix by which to transform the copy of the entity
        """
        pass
    
    
    def Highlight(self):
        """
        Highlight() -> void
        
        Highlight(FullSubentityPath, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            FullSubentityPath subId: 
            Input FullSubentityPath that identifies the subentity to highlight
            
            [MarshalAs(UnmanagedType.U1)] bool highlightAll: 
            Input Boolean indicating whether to highlight in all viewports
        """
        pass
    
    
    def HighlightState(self):
        """
        HighlightState -> HighlightStyle
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Plane projectionPlane: 
            Input plane for the projection to occur
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        """
        pass
    
    
    def JoinEntity(self):
        """
        JoinEntity -> void
            
            Entity secondaryEntity: 
            The secondary entity, which provides the data to be joined to the this entity.
            
            Exceptions: 
            Description
            
            Autodesk.AutoCAD.Runtime.Exception for ErrorStatus {InvalidInput} or {NotApplicable}: 
            _nt_
        """
        pass
    
    
    def JoinEntities(self):
        """
        JoinEntities -> IntegerCollection
            
            Entity[] otherEntities: 
            The other entities to be joined to the primary entity. Note, some implementations might require all of these entities to be of the same type as the primary entity.
            
            Exceptions: 
            Description
            
            Autodesk.AutoCAD.Runtime.Exception for ErrorStatus {InvalidInput} or {NotApplicable}: 
            _nt_
        """
        pass
    
    
    def List(self):
        """
        List -> void
        
        """
        pass
    
    
    def MoveGripPointsAt(self):
        """
        MoveGripPointsAt(GripDataCollection, Vector3d, MoveGripPointsFlags) -> void
        
        MoveGripPointsAt(IntegerCollection, Vector3d) -> void
            
            IntegerCollection indices: 
            Input array containing index values (which correspond to grip points reported by the GetGripPoints() method) that indicate which grip points are currently "hot"
            
            Vector3d offset: 
            Input vector (in WCS coordinates) indicating the direction and magnitude that the grip points have been translated
        """
        pass
    
    
    def MoveStretchPointsAt(self):
        """
        MoveStretchPointsAt -> void
            
            IntegerCollection indices: 
            Input array containing index values (which correspond to stretch points reported by the GetStretchPoints() method) that indicate which stretch points are being translated
            
            Vector3d offset: 
            Input vector (in WCS coordinates) indicating the direction and magnitude that the stretch points have been translated
        """
        pass
    
    
    def PopHighlight(self):
        """
        PopHighlight -> void
            
            FullSubentityPath subId: 
            Input AcDbFullSubentPath that identifies the subentity to unhighlight
        """
        pass
    
    
    def PushHighlight(self):
        """
        PushHighlight -> void
            
            FullSubentityPath subId: 
            Input AcDbFullSubentPath that identifies the subentity to highlight
            
            HighlightStyle highlightStyle: 
            Input AcGiHighlightStyle for this subid
        """
        pass
    
    
    def RecordGraphicsModified(self):
        """
        RecordGraphicsModified -> void
            
            [MarshalAs(UnmanagedType.U1)] bool setModified: 
            Input Boolean value to indicate if the entity's graphics should be updated on screen when the object is closed
        """
        pass
    
    
    def SaveAs(self):
        """
        SaveAs -> void
            
            WorldDraw mode: 
            Input pointer to fully initialized WorldDraw object (or an object of a class derived from WorldDraw)
            
            Autodesk.AutoCAD.DatabaseServices.SaveType st: 
            Input SaveType indicates why the saveAs is being called.
        """
        pass
    
    
    def SetDatabaseDefaults(self):
        """
        SetDatabaseDefaults() -> void
        
        SetDatabaseDefaults(Database) -> void
            
            Database sourceDatabase: 
            Input database whose defaults will be used to set the values of the entity
        """
        pass
    
    
    def SetDragStatus(self):
        """
        SetDragStatus -> void
            
            DragStatus status: 
            Value describing the status of the drag operation; one of the values from the DragStat enumeration
        """
        pass
    
    
    def SetGripStatus(self):
        """
        SetGripStatus -> void
            
            GripStatus status: 
            Value describing the status of the grip operation; one of the values from the GripStatus enumeration
        """
        pass
    
    
    def SetLayerId(self):
        """
        SetLayerId -> void
            
            ObjectId newValue: 
            Input name of the LayerTableRecord to be referenced by the entity
            
            [MarshalAs(UnmanagedType.U1)] bool allowHidden: 
            Input Boolean indicating whether to allow newValue to specify a hidden layer
        """
        pass
    
    
    def SetPropertiesFrom(self):
        """
        SetPropertiesFrom -> void
            
            Entity entityPointer: 
            Input entity from which to copy the properties
        """
        pass
    
    
    def SetSubentityGripStatus(self):
        """
        SetSubentityGripStatus -> void
            
            GripStatus status: 
            Input the status of the grip operation
            
            FullSubentityPath subentity: 
            Input the subentity on the object whose grip status changed
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
            
            Matrix3d transform: 
            Input transformation matrix to be applied to the entity
        """
        pass
    
    
    def TransformSubentityPathsBy(self):
        """
        TransformSubentityPathsBy -> void
            
            FullSubentityPath[] subPaths: 
            Input an array of one or more FullSubentityPath objects identifying the subentities to transform
            
            Matrix3d transform: 
            Input the WCS transformation to apply to each of the supplied subentities.
        """
        pass
    
    
    def Unhighlight(self):
        """
        Unhighlight() -> void
        
        Unhighlight(FullSubentityPath, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            FullSubentityPath subId: 
            Input FullSubentityPath that identifies which subentity to unhighlight
            
            [MarshalAs(UnmanagedType.U1)] bool highlightAll: 
            Input Boolean indicating whether to unhighlight in all viewports
        """
        pass
    
    
    BlockId = None
    
    
    BlockName = None
    
    
    CastShadows = None
    
    
    CloneMeForDragging = None
    
    
    CollisionType = None
    
    
    Color = None
    
    
    ColorIndex = None
    
    
    CompoundObjectTransform = None
    
    
    Ecs = None
    
    
    EdgeStyleId = None
    
    
    EntityColor = None
    
    
    FaceStyleId = None
    
    
    ForceAnnoAllVisible = None
    
    
    GeometricExtents = None
    
    
    Hyperlinks = None
    
    
    IsPlanar = None
    
    
    Layer = None
    
    
    LayerId = None
    
    
    Linetype = None
    
    
    LinetypeId = None
    
    
    LinetypeScale = None
    
    
    LineWeight = None
    
    
    Material = None
    
    
    MaterialId = None
    
    
    MaterialMapper = None
    
    
    PlotStyleName = None
    
    
    PlotStyleNameId = None
    
    
    ReceiveShadows = None
    
    
    Transparency = None
    
    
    Visible = None
    
    
    VisualStyleId = None
    
    pass

class EntityAlignmentEventArgs(EventArgs):
    """
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    A
    
    l
    
    i
    
    g
    
    n
    
    m
    
    e
    
    n
    
    t
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
     
    
    E
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    P
    
    i
    
    c
    
    k
    
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
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    .
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    N
    
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
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    .
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    C
    
    l
    
    o
    
    s
    
    e
    
    s
    
    t
    
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
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    .
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    D
    
    i
    
    r
    
    e
    
    c
    
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
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    .
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    [
    
    ]
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
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
    
    [
    
    ]
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    def GetPickedEntities(self):
        """
        GetPickedEntities -> FullSubentityPath[]
        
        """
        pass
    
    
    ClosestPoint = None
    
    
    Direction = None
    
    
    Entity = None
    
    
    Normal = None
    
    
    PickPoint = None
    
    pass

class EqualCurvatureConstraint(GeometricalConstraint):
    """
    
    E
    
    q
    
    u
    
    a
    
    l
    
    C
    
    u
    
    r
    
    v
    
    a
    
    t
    
    u
    
    r
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class EqualDistanceConstraint(GeometricalConstraint):
    """
    
    E
    
    q
    
    u
    
    a
    
    l
    
    D
    
    i
    
    s
    
    t
    
    a
    
    n
    
    c
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class EqualHelpParameterConstraint(GeometricalConstraint):
    """
    
    E
    
    q
    
    u
    
    a
    
    l
    
    H
    
    e
    
    l
    
    p
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """
    def GetEqualHelpParameters(self):
        """
        GetEqualHelpParameters -> void
            
            pHelpParameter1: 
            The returned pointer to the first AcHelpParameter object.
            
            pHelpParameter2: 
            The returned pointer to the second AcHelpParameter object.
        """
        pass
    
    pass

class EqualLengthConstraint(GeometricalConstraint):
    """
    
    E
    
    q
    
    u
    
    a
    
    l
    
    L
    
    e
    
    n
    
    g
    
    t
    
    h
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class EqualRadiusConstraint(GeometricalConstraint):
    """
    
    E
    
    q
    
    u
    
    a
    
    l
    
    R
    
    a
    
    d
    
    i
    
    u
    
    s
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class ExplicitConstraint(GeometricalConstraint):
    """
    
    """
    DimDependencyId = None
    
    
    MeasuredValue = None
    
    
    ValueDependencyId = None
    
    pass

class Extents2d(IFormattable {
}):
    """
    
    E
    
    x
    
    t
    
    e
    
    n
    
    t
    
    s
    
    2
    
    d
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
     
    
    m
    
    i
    
    n
    
    i
    
    m
    
    u
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    i
    
    n
    
    i
    
    m
    
    u
    
    m
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
     
    
    m
    
    a
    
    x
    
    i
    
    m
    
    u
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    a
    
    x
    
    i
    
    m
    
    u
    
    m
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    
    
    
    
    
    
    
    
    
    
    E
    
    x
    
    t
    
    e
    
    n
    
    t
    
    s
    
    2
    
    d
    
    (
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    m
    
    i
    
    n
    
    X
    
     
    
    :
    
     
    
    M
    
    i
    
    n
    
    i
    
    m
    
    u
    
    m
    
     
    
    X
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    m
    
    i
    
    n
    
    Y
    
     
    
    :
    
     
    
    M
    
    i
    
    n
    
    i
    
    m
    
    u
    
    m
    
     
    
    Y
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    m
    
    a
    
    x
    
    X
    
     
    
    :
    
     
    
    M
    
    a
    
    x
    
    i
    
    m
    
    u
    
    m
    
     
    
    X
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    m
    
    a
    
    x
    
    Y
    
     
    
    :
    
     
    
    M
    
    a
    
    x
    
    i
    
    m
    
    u
    
    m
    
     
    
    Y
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Extents2d) -> bool
            
            Extents2d a: 
            Object to compare
        IsEqualTo(Extents2d, Tolerance) -> bool
            
            Extents2d a: 
            Input object to compare
            
            Tolerance tolerance: 
            Input tolerance to be used
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format to display
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    MaxPoint = None
    
    
    MinPoint = None
    
    pass

class Extents3d(IFormattable {
}):
    """
    
    E
    
    x
    
    t
    
    e
    
    n
    
    t
    
    s
    
    3
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    E
    
    x
    
    t
    
    e
    
    n
    
    t
    
    s
    
    3
    
    d
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    m
    
    i
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    i
    
    n
    
    i
    
    m
    
    u
    
    m
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    m
    
    a
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    a
    
    x
    
    i
    
    m
    
    u
    
    m
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    t
    """
    def AddBlockExtents(self):
        """
        AddBlockExtents -> void
            
            BlockTableRecord pointerToBlockTableRecord: 
            Pointer to a block table record
        """
        pass
    
    
    def AddExtents(self):
        """
        AddExtents -> void
            
            Extents3d source: 
            Input another Extents3d object
        """
        pass
    
    
    def AddPoint(self):
        """
        AddPoint -> void
            
            Point3d pt: 
            Input 3D point
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare
        """
        pass
    
    
    def ExpandBy(self):
        """
        ExpandBy -> void
            
            Vector3d vector: 
            Input 3D vector
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Extents3d) -> bool
            
            Extents3d a: 
            Input object to compare
        IsEqualTo(Extents3d, Tolerance) -> bool
            
            Extents3d a: 
            Input object to compare
            
            Tolerance tolerance: 
            Input tolerance to check against
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            Point3d min: 
            Input minimum extent
            
            Point3d max: 
            Input maximum extent
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format to display
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
            
            Matrix3d mat: 
            Input 3D transformation matrix
        """
        pass
    
    
    MaxPoint = None
    
    
    MinPoint = None
    
    pass

class ExtrudedSurface(Autodesk.AutoCAD.DatabaseServices.Surface):
    """
    
    E
    
    x
    
    t
    
    r
    
    u
    
    d
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    )
    """
    def CreateExtrudedSurface(self):
        """
        CreateExtrudedSurface -> void
            
            Entity sweepEnt: 
            Input the curve, region, or planar surface to be swept
            
            Vector3d directionVec: 
            Input the vector that indicates the direction and distance of the sweep operation
            
            Autodesk.AutoCAD.DatabaseServices.SweepOptions sweepOptions: 
            Input sweep options
        """
        pass
    
    
    def SetExtrude(self):
        """
        SetExtrude -> void
            
            Vector3d sweepVec: 
            Input extrusion vector
            
            Autodesk.AutoCAD.DatabaseServices.SweepOptions sweepOptions: 
            Input sweep options
        """
        pass
    
    
    Height = None
    
    
    SweepEntity = None
    
    
    SweepOptions = None
    
    
    SweepProfile = None
    
    
    SweepVec = None
    
    
    TaperAngle = None
    
    pass

class Face(Entity):
    """
    
    F
    
    a
    
    c
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    F
    
    a
    
    c
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    3
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    4
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    o
    
    u
    
    r
    
    t
    
    h
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    1
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    2
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    3
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    4
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    f
    
    o
    
    u
    
    r
    
    t
    
    h
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
    
    
    
    
    
    
    F
    
    a
    
    c
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    3
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    c
    
    o
    
    r
    
    n
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    1
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    2
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    3
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    4
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    f
    
    o
    
    u
    
    r
    
    t
    
    h
    
     
    
    e
    
    d
    
    g
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    v
    
    i
    
    s
    
    i
    
    b
    
    l
    
    e
    """
    def GetVertexAt(self):
        """
        GetVertexAt -> Point3d
            
            short value: 
            Input vertex index number (must be 1 through 4)
        """
        pass
    
    
    def IsEdgeVisibleAt(self):
        """
        IsEdgeVisibleAt -> bool
            
            short vertexIndex: 
            Input vertex index number (must be 1 through 4)
        """
        pass
    
    
    def MakeEdgeInvisibleAt(self):
        """
        MakeEdgeInvisibleAt -> void
            
            short vertexIndex: 
            Input vertex index number of starting vertex for edge
        """
        pass
    
    
    def MakeEdgeVisibleAt(self):
        """
        MakeEdgeVisibleAt -> void
            
            short vertexIndex: 
            Input vertex index number of starting vertex for edge
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt -> void
            
            short vertexIndex: 
            Input vertex index number (must be 1 through 4)
            
            Point3d vertexPosition: 
            Input vertex position (in WCS coordinates)
        """
        pass
    
    pass

class FaceRecord(Vertex):
    """
    
    F
    
    a
    
    c
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    F
    
    a
    
    c
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    s
    
    h
    
    o
    
    r
    
    t
    
    ,
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
    ,
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
    ,
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
    0
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    a
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    a
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    a
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
    3
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    f
    
    o
    
    u
    
    r
    
    t
    
    h
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    a
    
    c
    
    e
    """
    def GetVertexAt(self):
        """
        GetVertexAt -> short
            
            short faceIndex: 
            Input face corner index number (must be 0 through 3)
        """
        pass
    
    
    def IsEdgeVisibleAt(self):
        """
        IsEdgeVisibleAt -> bool
            
            short faceIndex: 
            Input face corner index number (must be 0 through 3)
        """
        pass
    
    
    def MakeEdgeInvisibleAt(self):
        """
        MakeEdgeInvisibleAt -> void
            
            short faceIndex: 
            Input index number of starting corner for edge (must be 0 - 3)
        """
        pass
    
    
    def MakeEdgeVisibleAt(self):
        """
        MakeEdgeVisibleAt -> void
            
            short faceIndex: 
            Input index number of starting corner for edge (must be 0 - 3)
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt -> void
            
            short faceIndex: 
            Input face corner index number (must be 0 - 3)
            
            short vertexIndex: 
            Input index of vertex in PolyFaceMesh's vertex list that is to be used for this face corner
        """
        pass
    
    pass

class FaceRef(SubentRef):
    """
    
    F
    
    a
    
    c
    
    e
    
    R
    
    e
    
    f
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    F
    
    a
    
    c
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    F
    
    a
    
    c
    
    e
    
    R
    
    e
    
    f
    
    (
    
    C
    
    o
    
    m
    
    p
    
    o
    
    u
    
    n
    
    d
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    ,
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
    )
    
    (
    
    )
    """

    pass

class FeatureControlFrame(Entity):
    """
    
    F
    
    e
    
    a
    
    t
    
    u
    
    r
    
    e
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    F
    
    r
    
    a
    
    m
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    F
    
    e
    
    a
    
    t
    
    u
    
    r
    
    e
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    F
    
    r
    
    a
    
    m
    
    e
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    o
    
    d
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    e
    
    x
    
    t
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    d
    
    e
    
    s
    
     
    
    t
    
    o
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    e
    
    a
    
    t
    
    u
    
    r
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    s
    
    y
    
    m
    
    b
    
    o
    
    l
    
    s
    
     
    
    a
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
     
    
    I
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    i
    
    s
    
     
    
    N
    
    u
    
    l
    
    l
    
    ,
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    s
    
     
    
    j
    
    u
    
    s
    
    t
    
     
    
    l
    
    i
    
    k
    
    e
    
     
    
    c
    
    a
    
    l
    
    l
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
    o
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    i
    
    o
    
    n
    
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
    
     
    
    I
    
    n
    
    s
    
    e
    
    r
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    W
    
    C
    
    S
    
    )
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    F
    
    c
    
    f
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    N
    
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
    
     
    
    (
    
    W
    
    C
    
    S
    
    )
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    F
    
    c
    
    f
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    X
    
    -
    
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
    
     
    
    (
    
    W
    
    C
    
    S
    
    )
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    F
    
    c
    
    f
    """
    def GetBoundingPoints(self):
        """
        GetBoundingPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetBoundingPolyline(self):
        """
        GetBoundingPolyline -> Point3dCollection
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input objectId of the desired DimensionStyle to be used by the Fcf
        """
        pass
    
    
    def SetOrientation(self):
        """
        SetOrientation -> void
            
            Vector3d norm: 
            Input vector (in WCS) to be used to define the new plane that will contain the Fcf
            
            Vector3d dir: 
            Input X-Direction vector (WCS) for the Fcf
        """
        pass
    
    
    Dimclrd = None
    
    
    Dimclrt = None
    
    
    DimensionStyle = None
    
    
    DimensionStyleName = None
    
    
    Dimgap = None
    
    
    Dimscale = None
    
    
    Dimtxsty = None
    
    
    Dimtxt = None
    
    
    Direction = None
    
    
    Location = None
    
    
    Normal = None
    
    
    Text = None
    
    
    TextStyleId = None
    
    
    TextStyleName = None
    
    pass

class Field(DBObject):
    """
    
    F
    
    i
    
    e
    
    l
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    F
    
    i
    
    e
    
    l
    
    d
    
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
    
     
    
    f
    
    i
    
    e
    
    l
    
    d
    
    C
    
    o
    
    d
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    e
    
    l
    
    d
    
     
    
    c
    
    o
    
    d
    
    e
    
    
    
    
    
    
    
    
    
    
    F
    
    i
    
    e
    
    l
    
    d
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    f
    
    i
    
    e
    
    l
    
    d
    
    C
    
    o
    
    d
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    e
    
    l
    
    d
    
     
    
    c
    
    o
    
    d
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    e
    
    x
    
    t
    
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
    
     
    
    f
    
    l
    
    a
    
    g
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    s
    
     
    
    a
    
     
    
    t
    
    e
    
    x
    
    t
    
     
    
    f
    
    i
    
    e
    
    l
    
    d
    """
    def ConvertToTextField(self):
        """
        ConvertToTextField -> void
        
        """
        pass
    
    
    def Evaluate(self):
        """
        Evaluate() -> void
        
        Evaluate(int, Database) -> void
            
            int evaluationOptions: 
            Input context in which the field is evaluated; the context flag can be one of the predefined FieldEvaluationContext enum flags or a user-defined context flag
            
            Database database: 
            Input database to be used for the evaluation, which can be null
        """
        pass
    
    
    def FindField(self):
        """
        FindField -> bool
        
        """
        pass
    
    
    def GetChildren(self):
        """
        GetChildren -> Field()
        
        """
        pass
    
    
    def GetChildrenIds(self):
        """
        GetChildrenIds -> ObjectId()
        
        """
        pass
    
    
    def GetData(self):
        """
        GetData -> object
            
            string key: 
            Input key to get the data; the key cannot be null or an empty string
        """
        pass
    
    
    def GetFieldCode(self):
        """
        GetFieldCode() -> string
        
        GetFieldCode(FieldCodeFlags) -> string
            
            FieldCodeFlags flags: 
            Input flag, which can be one or more of the FieldCodeFlags values
        """
        pass
    
    
    def GetFieldCodeWithChildren(self):
        """
        GetFieldCodeWithChildren() -> FieldCodeWithChildren
        
        GetFieldCodeWithChildren(FieldCodeFlags) -> FieldCodeWithChildren
            
            FieldCodeFlags flags: 
            Input flag, which can be one or more of the FieldCodeFlags values
        """
        pass
    
    
    def GetStringValue(self):
        """
        GetStringValue -> string
        
        """
        pass
    
    
    def SetData(self):
        """
        SetData(string, object) -> void
            
            string key: 
            Input key to use to set and get the data; the key cannot be null or an empty string
            
            object data: 
            Input the object that contains the data
        SetData(string, object, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            string key: 
            Input key to use to set and get the data; the key cannot be null or an empty string
            
            object data: 
            Input the object that contains the data
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input true if the data is to be set in all child fields, false if it is to be set only in this field
        """
        pass
    
    
    def SetFieldCode(self):
        """
        SetFieldCode -> void
            
            string fieldCode: 
            Input field code to set
        """
        pass
    
    
    def SetFieldCodeWithChildren(self):
        """
        SetFieldCodeWithChildren(FieldCodeFlags, FieldCodeWithChildren) -> void
            
            FieldCodeFlags flag: 
            Input flag, which can be one or more of the FieldCodeFlags values
            
            FieldCodeWithChildren fieldCode: 
            Input field code to set
        SetFieldCodeWithChildren(FieldCodeWithChildren) -> void
            
            FieldCodeWithChildren fieldCode: 
            Input field code to set
        """
        pass
    
    
    DataType = None
    
    
    EvaluationOption = None
    
    
    EvaluationStatus = None
    
    
    EvaluatorId = None
    
    
    FilingOption = None
    
    
    Format = None
    
    
    HyperLink = None
    
    
    IsTextField = None
    
    
    State = None
    
    
    Value = None
    
    pass

  AddMarkers = 0x10
  EscapeBackslash = 0x20
  EvaluatedChildren = 4
  EvaluatedText = 2
  FieldCode = 1
  ObjectReference = 8
  PreserveFields = 0x80
  StripOptions = 0x40
  TextField = 0x100

class FieldCodeWithChildren(IDisposable):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            int i: 
            Index at which the new entry will be added to the array of children.
            
            Field field: 
            New child field to add to the array of children at index i.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    Children = None
    
    
    FieldCode = None
    
    pass

  Demand = 0x20
  Etransmit = 8
  Open = 1
  Plot = 4
  Preview = 0x40
  Regen = 0x10
  Save = 2

  Automatic = 0x3f
  Disable = 0
  OnDemand = 0x20
  OnEtransmit = 8
  OnOpen = 1
  OnPlot = 4
  OnRegen = 0x10
  OnSave = 2

class FieldEvaluationResult(public struct FieldEvaluationResult {
}):
    """
    
    """
    Evaluated = None
    
    
    Found = None
    
    pass

  EvaluatorNotFound = 4
  InvalidCode = 0x10
  InvalidContext = 0x20
  NotYetEvaluated = 1
  OtherError = 0x40
  Success = 2
  SyntaxError = 8

class FieldEvaluationStatusResult(public struct FieldEvaluationStatusResult {
}):
    """
    
    F
    
    i
    
    e
    
    l
    
    d
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
    R
    
    e
    
    s
    
    u
    
    l
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    F
    
    i
    
    e
    
    l
    
    d
    
    E
    
    v
    
    a
    
    l
    
    u
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    s
    
     
    
    :
    
     
    
    _
    
    n
    
    t
    
    _
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    e
    
     
    
    :
    
     
    
    _
    
    n
    
    t
    
    _
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
     
    
    :
    
     
    
    _
    
    n
    
    t
    
    _
    """
    ErrorCode = None
    
    
    ErrorMessage = None
    
    
    Status = None
    
    pass

  SkipFilingResult = 1

  Compiled = 2
  Evaluated = 8
  HasCache = 0x10
  HasFormattedString = 0x20
  Initialized = 1
  Modified = 4

  OpenForReadAndAllShare = 3
  OpenForReadAndReadShare = 1
  OpenForReadAndWriteNoShare = 2
  OpenTryForReadShare = 4

  FileFiler
  CopyFiler
  UndoFiler
  BagFiler
  IdTranslateFiler
  PageFiler
  DeepCloneFiler
  IdFiler
  PurgeFiler
  WblockCloneFiler

  TrimNone
  TrimStart
  TrimSecond
  TrimBoth

  Default
  FontFile
  CompiledShapeFile
  TrueTypeFontFile
  EmbeddedImageFile
  XRefDrawing
  PatternFile
  ArxApplication
  FontMapFile
  UnderlayFile

class FitData(Public Structure FitData
End Structure):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare with
        """
        pass
    
    
    def GetFitPoints(self):
        """
        GetFitPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(FitData) -> bool
            
            FitData other: 
            Object to compare with
        IsEqualTo(FitData, Tolerance) -> bool
            
            FitData other: 
            Object to compare with
            
            Tolerance tolerance: 
            Tolerance range
        """
        pass
    
    
    Degree = None
    
    
    EndTangent = None
    
    
    FitTolerance = None
    
    
    StartTangent = None
    
    
    TangentsExist = None
    
    pass

class FixedConstraint(GeometricalConstraint):
    """
    
    F
    
    i
    
    x
    
    e
    
    d
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  NotSet
  LeftToRight
  RightToLeft
  TopToBottom
  BottomToTop
  ByStyle

class Font(public struct Font {
}):
    """
    
    F
    
    o
    
    n
    
    t
    
    (
    
    )
    """
    IsTrueType = None
    
    
    Name = None
    
    pass

class FormattedTableData(LinkedTableData):
    """
    
    F
    
    o
    
    r
    
    m
    
    a
    
    t
    
    t
    
    e
    
    d
    
    T
    
    a
    
    b
    
    l
    
    e
    
    D
    
    a
    
    t
    
    a
    
    (
    
    )
    """
    def GetAlignment(self):
        """
        GetAlignment -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetBackgroundColor(self):
        """
        GetBackgroundColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
        """
        pass
    
    
    def GetContentColor(self):
        """
        GetContentColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetGridColor(self):
        """
        GetGridColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetGridLinetype(self):
        """
        GetGridLinetype -> ObjectId
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetGridLineWeight(self):
        """
        GetGridLineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetGridVisibility(self):
        """
        GetGridVisibility -> Autodesk.AutoCAD.DatabaseServices.Visibility
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetMargin(self):
        """
        GetMargin -> double
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            CellMargins margin: 
            Input margin type to get
        """
        pass
    
    
    def GetMergeRange(self):
        """
        GetMergeRange -> CellRange
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetRotation(self):
        """
        GetRotation -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetOverride(self):
        """
        GetOverride(int, int, int) -> CellProperties
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            int content: 
            Input content index. This can be -1. See remarks.
        GetOverride(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType) -> GridProperties
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetScale(self):
        """
        GetScale -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetTextHeight(self):
        """
        GetTextHeight -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetTextStyle(self):
        """
        GetTextStyle -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsFormatEditable(self):
        """
        IsFormatEditable -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsMerged(self):
        """
        IsMerged -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def Merge(self):
        """
        Merge -> void
            
            CellRange range: 
            Input cell range to merge
        """
        pass
    
    
    def RemoveAllOverrides(self):
        """
        RemoveAllOverrides -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
        """
        pass
    
    
    def SetAlignment(self):
        """
        SetAlignment -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.CellAlignment value: 
            Input alignment
        """
        pass
    
    
    def SetBackgroundColor(self):
        """
        SetBackgroundColor -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.Colors.Color value: 
            Input color to set
        """
        pass
    
    
    def SetContentColor(self):
        """
        SetContentColor -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.Colors.Color value: 
            Input color
        """
        pass
    
    
    def SetGridColor(self):
        """
        SetGridColor -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.Colors.Color value: 
            Input grid color to set
        """
        pass
    
    
    def SetGridLinetype(self):
        """
        SetGridLinetype -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            ObjectId value: 
            Input grid line type to set
        """
        pass
    
    
    def SetGridLineWeight(self):
        """
        SetGridLineWeight -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight value: 
            Input grid line weight to set
        """
        pass
    
    
    def SetGridVisibility(self):
        """
        SetGridVisibility -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.Visibility value: 
            Input grid visibility to set
        """
        pass
    
    
    def SetMargin(self):
        """
        SetMargin -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            CellMargins margin: 
            Input margin type to set. Multiple margin types can be combined using OR.
            
            double value: 
            Input margin value to set
        """
        pass
    
    
    def SetOverride(self):
        """
        SetOverride(int, int, int, CellProperties) -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            int content: 
            Input content index. This can be -1. See remarks.
            
            CellProperties cellProperty: 
            Input override to set
        SetOverride(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, GridProperties) -> void
            
            int row: 
            Input row index. This can be -1. See remarks
            
            int column: 
            Input column index. This can be -1. See
        """
        pass
    
    
    def SetRotation(self):
        """
        SetRotation -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            double value: 
            Input angle in radians
        """
        pass
    
    
    def SetScale(self):
        """
        SetScale -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            double value: 
            Input scale
        """
        pass
    
    
    def SetTextHeight(self):
        """
        SetTextHeight -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            double value: 
            Input text height
        """
        pass
    
    
    def SetTextStyle(self):
        """
        SetTextStyle -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId value: 
            Input text style
        """
        pass
    
    
    def Unmerge(self):
        """
        Unmerge -> void
            
            CellRange range: 
            Input cell range to unmerge
        """
        pass
    
    pass

  ImageFrameAbove = 1
  ImageFrameBelow = 2
  ImageFrameInvalid = -1
  ImageFrameOff = 0
  ImageFrameOnNoPlot = 3

class FullDwgVersion(public struct FullDwgVersion {
}):
    """
    
    F
    
    u
    
    l
    
    l
    
    D
    
    w
    
    g
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    w
    
    g
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
     
    
    v
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    M
    
    a
    
    i
    
    n
    
    t
    
    e
    
    n
    
    a
    
    n
    
    c
    
    e
    
    R
    
    e
    
    l
    
    e
    
    a
    
    s
    
    e
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
     
    
    m
    
    i
    
    n
    
    o
    
    r
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    i
    
    n
    
    o
    
    r
    
     
    
    v
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString -> string
        
        """
        pass
    
    
    MajorVersion = None
    
    
    MinorVersion = None
    
    pass

class FullSubentityPath(public struct FullSubentityPath {
}):
    """
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    [
    
    ]
    
     
    
    i
    
    d
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    I
    
    D
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    I
    
    d
    
     
    
    i
    
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
    
     
    
    s
    
    u
    
    b
    
    e
    
    n
    
    t
    
     
    
    I
    
    D
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare to
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetObjectIds(self):
        """
        GetObjectIds -> ObjectId()
        
        """
        pass
    
    
    IsNull = None
    
    
    Null = None
    
    
    SubentId = None
    
    pass

class G2SmoothConstraint(CompositeConstraint):
    """
    
    G
    
    2
    
    S
    
    m
    
    o
    
    o
    
    t
    
    h
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  Alber = 4
  Azede = 0x3b
  Azmea = 11
  Azmed = 7
  Bipolar = 0x1f
  Bonne = 0x18
  Cassini = 0x16
  Eckert4 = 0x19
  Eckert6 = 0x1a
  Edcnc = 12
  Edcyl = 20
  EdcylE = 0x43
  GaussK = 0x2e
  Gnomonic = 0x13
  Goode = 0x1c
  Hom1uv = 0x501
  Hom1xy = 0x502
  Hom2uv = 0x503
  Hom2xy = 0x504
  Krovak = 0x2f
  Krvk95 = 0x33
  LL = 1
  Lm1sp = 0x24
  Lm2sp = 0x25
  Lmblg = 0x26
  Lmbrtaf = 0x41
  Lmtan = 8
  Miller = 13
  Mndotl = 0x29
  Mndott = 0x2a
  Modpc = 10
  Mollweid = 0x1b
  Mrcat = 6
  MrcatK = 0x31
  Mstero = 15
  Neacyl = 0x1d
  Nerth = 0x37
  Nrthsrt = 0x40
  Nzealand = 0x10
  OblqM = 5
  Obqcyl = 0x38
  Ortho = 0x12
  Ostn02 = 60
  Ostn97 = 0x3a
  Ostro = 0x22
  PlateCarree = 0x44
  Plycn = 9
  Pstro = 0x21
  Pstrosl = 0x35
  PvMercator = 0x45
  Robinson = 0x17
  Rskew = 0x505
  Rskewc = 0x506
  Rskewo = 0x507
  Sinus = 0x11
  Sotrm = 0x2b
  Sstro = 0x23
  Swiss = 0x20
  Sys34 = 0x39
  Sys34_01 = 0x42
  Sys34_99 = 0x3d
  Teacyl = 30
  Tm = 3
  Trmeraf = 0x36
  Trmrkrg = 0x3e
  Trmrs = 0x2d
  Unknown = 0
  Utm = 0x2c
  Vdgrntn = 0x15
  Wccsl = 0x27
  Wccst = 40
  Winkl = 0x3f

  Unknown
  Arbitrary
  Geographic
  Projected

  BenoitChain = 0x1a
  BenoitLink = 30
  Brealey = 0x26
  CaGrid = 0x17
  CapeRood = 0x25
  Centimeter = 7
  Centisec = 0x3f2
  ClarkeChain = 0x18
  ClarkeFoot = 5
  ClarkeLink = 0x1c
  Decameter = 0x30
  Decimeter = 0x12
  Decisec = 0x3f1
  Degree = 0x3e9
  Dekameter = 20
  Foot = 2
  Furlong = 0x23
  GermanMeter = 0x16
  GoldCoastFoot = 40
  Grad = 0x3ea
  Grade = 0x3eb
  GunterChain = 0x19
  GunterLink = 0x1d
  Hectometer = 0x15
  IFoot = 4
  IInch = 6
  IMile = 13
  Inch = 3
  IndianFoot = 0x2b
  IndianFt37 = 0x2c
  IndianFt62 = 0x2d
  IndianFt75 = 0x2e
  IndianYard = 0x2a
  IndianYd37 = 0x2f
  InternationalChain = 0x31
  InternationalLink = 50
  IYard = 12
  Kilometer = 8
  Knot = 14
  Lat66 = 0x10
  Lat83 = 0x11
  MapInfo = 0x3ec
  Meter = 1
  MicroInch = 0x29
  Mil = 0x3ed
  Mile = 11
  Millimeter = 0x13
  Millisec = 0x3f3
  Minute = 0x3ee
  NautM = 15
  Perch = 0x21
  Pole = 0x22
  Radian = 0x3ef
  Rod = 0x20
  Rood = 0x24
  SearsChain = 0x1b
  SearsFoot = 0x27
  SearsLink = 0x1f
  SearsYard = 10
  Second = 0x3f0
  Unknown = 0
  Yard = 9

class GeoCoordinateCategory(DisposableWrapper):
    """
    
    """
    def CreateAll(self):
        """
        CreateAll -> GeoCoordinateCategory()
        
        """
        pass
    
    
    def GetCoordinateAt(self):
        """
        GetCoordinateAt -> GeoCoordinateSystem
        
        """
        pass
    
    
    def NumOfCoordinate(self):
        """
        NumOfCoordinate -> Integer
        
        """
        pass
    
    
    ID = None
    
    pass

class GeoCoordinateSystem(DisposableWrapper):
    """
    
    """
    def Create(self):
        """
        Create -> GeoCoordinateSystem
            
            string coordSysIdOrFullDef: 
            A coordinate system name. For example: "WORLD-MERCATOR"
        """
        pass
    
    
    def CreateAll(self):
        """
        CreateAll() -> GeoCoordinateSystem()
        
        CreateAll(GeoCoordinateCategory) -> GeoCoordinateSystem()
        
        CreateAll(ValueType modopt(Point3d) modopt(IsBoxed)) -> GeoCoordinateSystem()
            
            ValueType modopt(Point3d) modopt(IsBoxed) geoPt: 
            Input geodetic point in (longitude, latitude, altitude) format.
        """
        pass
    
    
    def GetProjectionParamList(self):
        """
        GetProjectionParamList -> GeoProjectionParam()
        
        """
        pass
    
    
    CartesianExtents = None
    
    
    Datum = None
    
    
    Description = None
    
    
    Ellipsoid = None
    
    
    EPSGcode = None
    
    
    GeodeticExtents = None
    
    
    GeoUnit = None
    
    
    ID = None
    
    
    Offset = None
    
    
    ProjectionCode = None
    
    
    Type = None
    
    
    Unit = None
    
    
    UnitScale = None
    
    
    WktRepresentation = None
    
    
    XmlRepresentation = None
    
    pass

class GeoCoordinateTransformer(DisposableWrapper):
    """
    
    """
    def Create(self):
        """
        Create -> GeoCoordinateTransformer
        
        """
        pass
    
    
    def TransformPoint(self):
        """
        TransformPoint(Point3d) -> Point3d
        
        TransformPoint(string, string, Point3d) -> Point3d
        
        """
        pass
    
    
    def TransformPoints(self):
        """
        TransformPoints(Point3dCollection) -> Point3dCollection
        
        TransformPoints(string, string, Point3dCollection) -> Point3dCollection
        
        """
        pass
    
    
    SourceCSid = None
    
    
    TargetCSid = None
    
    pass

class GeoLocationData(DBObject):
    """
    
    G
    
    e
    
    o
    
    L
    
    o
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    D
    
    a
    
    t
    
    a
    
    (
    
    )
    """
    def AddMeshPointMap(self):
        """
        AddMeshPointMap -> void
            
            int index: 
            Input the index to insert at
            
            Point2d sourcePt: 
            Input the source point
            
            Point2d destPt: 
            Input the destination point
        """
        pass
    
    
    def EraseFromDb(self):
        """
        EraseFromDb -> void
        
        """
        pass
    
    
    def GetMeshPointMap(self):
        """
        GetMeshPointMap -> MeshPointMap
            
            int index: 
            Input the index to insert at
        """
        pass
    
    
    def GetMeshPointMaps(self):
        """
        GetMeshPointMaps -> MeshPointMaps
        
        """
        pass
    
    
    def PostToDb(self):
        """
        PostToDb -> ObjectId
        
        """
        pass
    
    
    def ResetMeshPointMaps(self):
        """
        ResetMeshPointMaps -> void
        
        """
        pass
    
    
    def SetMeshPointMaps(self):
        """
        SetMeshPointMaps -> void
            
            Point2dCollection sourcePts: 
            Input source points collection
            
            Point2dCollection destPts: 
            Input destination points collection
        """
        pass
    
    
    def TransformFromLonLatAlt(self):
        """
        TransformFromLonLatAlt -> Point3d
        
        """
        pass
    
    
    def TransformToLonLatAlt(self):
        """
        TransformToLonLatAlt(Point3d) -> Point3d
            
            Point3d dwgPt: 
            Input dwg point (x, y, z)
        TransformToLonLatAlt(double, double, double) -> GeoDataLonLatAltInfo
            
            double y: 
            Input y coordinate of dwg point
            
            double z: 
            Input z coordinate of dwg point
        """
        pass
    
    
    def UpdateTransformationMatrix(self):
        """
        UpdateTransformationMatrix -> void
        
        """
        pass
    
    
    BlockTableRecordId = None
    
    
    CoordinateProjectionRadius = None
    
    
    DoSeaLevelCorrection = None
    
    
    GeoRSSTag = None
    
    
    NorthDirection = None
    
    
    NorthDirectionVector = None
    
    
    NumMeshPoints = None
    
    
    ScaleEstimationMethod = None
    
    
    ScaleFactor = None
    
    
    SeaLevelElevation = None
    
    
    UpDirection = None
    
    pass

class GeoPositionMarker(Entity):
    """
    
    G
    
    e
    
    o
    
    P
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
    M
    
    a
    
    r
    
    k
    
    e
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    G
    
    e
    
    o
    
    P
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
    M
    
    a
    
    r
    
    k
    
    e
    
    r
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    (
    
    )
    """
    EnableFrameText = None
    
    
    GeoPosition = None
    
    
    LandingGap = None
    
    
    MText = None
    
    
    MTextVisible = None
    
    
    Normal = None
    
    
    Notes = None
    
    
    Position = None
    
    
    Radius = None
    
    
    Text = None
    
    
    TextAlignmentType = None
    
    
    TextStyle = None
    
    pass

class GeomRef(RXObject):
    """
    
    """
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    IsEmpty = None
    
    
    IsValid = None
    
    pass

class GeomapImage(RasterImage):
    """
    
    G
    
    e
    
    o
    
    m
    
    a
    
    p
    
    I
    
    m
    
    a
    
    g
    
    e
    
    (
    
    )
    """
    def GetImageVertices(self):
        """
        GetImageVertices -> Point3dCollection
        
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices -> Point3dCollection
        
        """
        pass
    
    
    def ImageSize(self):
        """
        ImageSize -> Vector2d
        
        """
        pass
    
    
    def UpdateMapImage(self):
        """
        UpdateMapImage -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool Reset: 
            Input Boolean to indicate whether to recapture the image in optimal resolution to the screen. If true, the L
        """
        pass
    
    
    BottomLeftPoint = None
    
    
    Brightness = None
    
    
    Contrast = None
    
    
    Fade = None
    
    
    Height = None
    
    
    ImageBottomLeftPoint = None
    
    
    ImageHeight = None
    
    
    ImageWidth = None
    
    
    IsOutOfDate = None
    
    
    LOD = None
    
    
    MapType = None
    
    
    Resolution = None
    
    
    Width = None
    
    pass

class GeometricalConstraint(ConstraintGroupNode):
    """
    
    """
      Horizontal
      Vertical
      Parallel
      Perpendicular
      Normal
      Collinear
      Coincident
      Concentric
      Tangent
      EqualRadius
      EqualLength
      Symmetric
      Smooth
      Fix
    
    
    def Deactivate(self):
        """
        Deactivate -> void
        
        """
        pass
    
    
    def GetConnectedHelpParameterFor(self):
        """
        GetConnectedHelpParameterFor -> HelpParameter
            
            ConstrainedGeometry consGeom: 
            The reference to ConstrainedGeometry object.
        """
        pass
    
    
    def Reactivate(self):
        """
        Reactivate -> void
        
        """
        pass
    
    
    ConnectedGeometries = None
    
    
    ConnectedHelpParameters = None
    
    
    IsActive = None
    
    
    IsEnabled = None
    
    
    IsImplied = None
    
    
    IsInternal = None
    
    
    OwningCompositeConstraint = None
    
    pass

class GeometryOverrule(Overrule):
    """
    
    """
    def GetGeomExtents(self):
        """
        GetGeomExtents -> Extents3d
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(Entity, Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, IntPtr, IntPtr) -> void
        
        IntersectWith(Entity, Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, IntPtr, IntPtr) -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class GradientBackground(Background):
    """
    
    G
    
    r
    
    a
    
    d
    
    i
    
    e
    
    n
    
    t
    
    B
    
    a
    
    c
    
    k
    
    g
    
    r
    
    o
    
    u
    
    n
    
    d
    
    (
    
    )
    """
    ColorBottom = None
    
    
    ColorMiddle = None
    
    
    ColorTop = None
    
    
    Height = None
    
    
    Horizon = None
    
    
    Rotation = None
    
    pass

class GradientColor(public struct GradientColor {
}):
    """
    
    G
    
    r
    
    a
    
    d
    
    i
    
    e
    
    n
    
    t
    
    C
    
    o
    
    l
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    l
    
    o
    
    r
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
     
    
    m
    
    a
    
    k
    
    i
    
    n
    
    g
    
     
    
    u
    
    p
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    f
    
    l
    
    o
    
    a
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    l
    
    o
    
    a
    
    t
    
     
    
    r
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    t
    
    e
    
    r
    
    p
    
    o
    
    l
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    s
    
     
    
    d
    
    e
    
    f
    
    i
    
    n
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    g
    
    r
    
    a
    
    d
    
    i
    
    e
    
    n
    
    t
    """
    def get_Color(self):
        """
        get_Color -> Color
        
        """
        pass
    
    
    def get_Value(self):
        """
        get_Value -> float
        
        """
        pass
    
    pass

  PreDefinedGradient
  UserDefinedGradient

class Graph(DisposableWrapper):
    """
    
    G
    
    r
    
    a
    
    p
    
    h
    
    
    
    
     
    
     
    
     
    
     
    
    G
    
    r
    
    a
    
    p
    
    h
    
    N
    
    o
    
    d
    
    e
    
     
    
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
    
     
    
    n
    
    o
    
    d
    
    e
    
    .
    
     
    
    D
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
     
    
    i
    
    s
    
     
    
    N
    
    U
    
    L
    
    L
    
    .
    """
    def AddEdge(self):
        """
        AddEdge -> void
            
            GraphNode from: 
            Input the node to begin the edge at
            
            GraphNode toPointer: 
            Input the node to end the edge at
        """
        pass
    
    
    def AddNode(self):
        """
        AddNode -> void
            
            GraphNode nodeToAdd: 
            Node to add
        """
        pass
    
    
    def BreakCycleEdge(self):
        """
        BreakCycleEdge -> void
            
            GraphNode from: 
            Input node that the edge begins at
            
            GraphNode toPointer: 
            Input node that the edge ends at
        """
        pass
    
    
    def ClearAll(self):
        """
        ClearAll -> void
            
            byte flags: 
            Input flag values to clear for all nodes in the graph
        """
        pass
    
    
    def DelNode(self):
        """
        DelNode -> void
            
            GraphNode nodeToDelete: 
            Node to delete
        """
        pass
    
    
    def FindCycles(self):
        """
        FindCycles -> bool
            
            GraphNode start: 
            Input node to begin the search for cycles at. Usually defaulted to NULL.
        """
        pass
    
    
    def GetOutgoing(self):
        """
        GetOutgoing -> GraphNodeCollection
        
        """
        pass
    
    
    def Node(self):
        """
        Node -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    def SetNodeGrowthRate(self):
        """
        SetNodeGrowthRate -> void
            
            int rate: 
            Number of nodes to allocate at once
        """
        pass
    
    
    IsEmpty = None
    
    
    NumNodes = None
    
    
    RootNode = None
    
    pass

class GraphNode(DisposableWrapper):
    """
    
    G
    
    r
    
    a
    
    p
    
    h
    
    N
    
    o
    
    d
    
    e
    
    (
    
    )
    """
    def AddRefTo(self):
        """
        AddRefTo -> void
            
            GraphNode outGoingNode: 
            Input to the outgoing node
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
            
            byte flags: 
            Input flag values to clear for this node
        """
        pass
    
    
    def CycleIn(self):
        """
        CycleIn -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def CycleOut(self):
        """
        CycleOut -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def DisconnectAll(self):
        """
        DisconnectAll -> void
        
        """
        pass
    
    
    def In(self):
        """
        In -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def IsMarkedAs(self):
        """
        IsMarkedAs -> bool
            
            int flag: 
            Input flag values to check for this node
        """
        pass
    
    
    def MarkAs(self):
        """
        MarkAs -> void
            
            byte flags: 
            Input flag values to set for this node
        """
        pass
    
    
    def MarkTree(self):
        """
        MarkTree -> void
            
            byte flags: 
            Input flag values to set for this node and all nested out nodes
            
            GraphNodeCollection appendedTo: 
            Input collection that this node and all nested out nodes should optionally be appended to
        """
        pass
    
    
    def Out(self):
        """
        Out -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def RemoveRefTo(self):
        """
        RemoveRefTo -> void
            
            GraphNode nodeToRemoveReference: 
            Input node to remove reference of
        """
        pass
    
    
    def SetEdgeGrowthRate(self):
        """
        SetEdgeGrowthRate -> void
            
            int outEdgeRate: 
            Number of outgoing edges allocated at one time
            
            int inEdgeRate: 
            Number of incoming edges allocated at one time
        """
        pass
    
    
    Data = None
    
    
    IsCycleNode = None
    
    
    NextCycleNode = None
    
    
    NumCycleIn = None
    
    
    NumCycleOut = None
    
    
    NumIn = None
    
    
    NumOut = None
    
    
    Owner = None
    
    pass

class GraphNodeCollection(DisposableWrapper, IList):
    """
    
    G
    
    r
    
    a
    
    p
    
    h
    
    N
    
    o
    
    d
    
    e
    
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
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> Integer
            
            GraphNode value: 
            Item to add.
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
            
            GraphNode value: 
            Object to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            GraphNode[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to start from
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            GraphNode value: 
            Item to seek
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Location to insert
            
            GraphNode value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            GraphNode value: 
            Item to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index to remove from
        """
        pass
    
    
    Count = None
    
    pass

  NoMetafile
  BoundingBox
  FullGraphics

  Double = 2
  Single = 1

  AllGridLines = 0x3f
  HorizontalBottom = 4
  HorizontalGridLines = 7
  HorizontalInside = 2
  HorizontalTop = 1
  InnerGridLines = 0x12
  InvalidGridLine = 0
  OuterGridLines = 0x2d
  VerticalGridLines = 0x38
  VerticalInside = 0x10
  VerticalLeft = 8
  VerticalRight = 0x20

  Color = 8
  DoubleLineSpacing = 0x20
  Invalid = 0
  LineStyle = 1
  Linetype = 4
  LineWeight = 2
  Visibility = 0x10

class GridPropertyParameter(public struct GridPropertyParameter {
  public GridProperties PropertyMask;
  public Autodesk.AutoCAD.DatabaseServices.GridLineStyle LineStyle;
  public Autodesk.AutoCAD.DatabaseServices.LineWeight LineWeight;
  public ObjectId Linetype;
  public Autodesk.AutoCAD.Colors.Color Color;
  public Autodesk.AutoCAD.DatabaseServices.Visibility Visibility;
  public double DoubleLineSpacing;
}):
    """
    
    """

    pass

class GripData(DisposableWrapper):
    """
    
    """
      MultiHotGrip = 2
      SharedGrip = 1
    
    
      WarmGrip
      HoverGrip
      HotGrip
      DragImageGrip
    
    
      Ok
      Failure
      NoRedrawGrip
      GripHotToWarm
      GetNewGripPoints
    
    
      GripStart
      GripEnd
      GripAbort
      Stretch
      Move
      Rotate
      Scale
      Mirror
      DimFocusChanged
      PopUpMenu
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetHotGripDimensionData(self):
        """
        GetHotGripDimensionData -> DynamicDimensionDataCollection
        
        """
        pass
    
    
    def GetHoverDimensionData(self):
        """
        GetHoverDimensionData -> DynamicDimensionDataCollection
        
        """
        pass
    
    
    def GetTooltip(self):
        """
        GetTooltip -> string
        
        """
        pass
    
    
    def OnGripStatusChanged(self):
        """
        OnGripStatusChanged -> void
        
        """
        pass
    
    
    def OnHotGrip(self):
        """
        OnHotGrip -> ReturnValue
        
        """
        pass
    
    
    def OnHover(self):
        """
        OnHover -> ReturnValue
        
        """
        pass
    
    
    def OnRightClick(self):
        """
        OnRightClick -> IEnumerable<IMenuItem>
        
        """
        pass
    
    
    def ViewportDraw(self):
        """
        ViewportDraw -> bool
        
        """
        pass
    
    
    def WorldDraw(self):
        """
        WorldDraw -> bool
        
        """
        pass
    
    
    AlternateBasePoint = None
    
    
    DrawAtDragImageGripPoint = None
    
    
    ForcedPickOn = None
    
    
    GizmosEnabled = None
    
    
    GripPoint = None
    
    
    HotGripInvokesRightClick = None
    
    
    IsPerViewport = None
    
    
    ModeKeywordsDisabled = None
    
    
    RubberBandLineDisabled = None
    
    
    SkipWhenShared = None
    
    
    TriggerGrip = None
    
    pass

class GripMode(DisposableWrapper):
    """
    
    G
    
    r
    
    i
    
    p
    
    M
    
    o
    
    d
    
    e
    
    (
    
    )
    """
      DragOn
      Immediate
      Command
    
    
      CursorNone
      CursorCrosshairPlus
      CursorCrosshairMinus
      CursorCrosshairCurve
      CursorCrosshairLine
      CursorCrosshairAngle
    
    
      CustomStart = 100
      Move = 1
      None = 0
    
    
    Action = None
    
    
    CLIDisplayString = None
    
    
    CLIKeywordList = None
    
    
    CLIPromptString = None
    
    
    CommandString = None
    
    
    Cursor = None
    
    
    DisplayString = None
    
    
    ModeId = None
    
    
    ToolTip = None
    
    pass

class GripModeCollection(DisposableWrapper, ICollection<Autodesk.AutoCAD.DatabaseServices.GripMode>):
    """
    
    G
    
    r
    
    i
    
    p
    
    M
    
    o
    
    d
    
    e
    
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
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> void
            
            Autodesk.AutoCAD.DatabaseServices.GripMode gripMode: 
            The mode object to add.
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
            
            Autodesk.AutoCAD.DatabaseServices.GripMode gripMode: 
            The gripMode object to test.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator<Autodesk.AutoCAD.DatabaseServices.GripMode>
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> bool
            
            Autodesk.AutoCAD.DatabaseServices.GripMode gripMode: 
            The gripMode object to remove.
        """
        pass
    
    
    Count = None
    
    
    IsReadOnly = None
    
    pass

class GripOverrule(Overrule):
    """
    
    """
    def GetGripPoints(self):
        """
        GetGripPoints(Entity, GripDataCollection, double, int, Vector3d, GetGripPointsFlags) -> void
        
        GetGripPoints(Entity, Point3dCollection, IntegerCollection, IntegerCollection) -> void
        
        """
        pass
    
    
    def GetStretchPoints(self):
        """
        GetStretchPoints -> void
        
        """
        pass
    
    
    def MoveGripPointsAt(self):
        """
        MoveGripPointsAt(Entity, GripDataCollection, Vector3d, MoveGripPointsFlags) -> void
        
        MoveGripPointsAt(Entity, IntegerCollection, Vector3d) -> void
        
        """
        pass
    
    
    def MoveStretchPointsAt(self):
        """
        MoveStretchPointsAt -> void
        
        """
        pass
    
    
    def OnGripStatusChanged(self):
        """
        OnGripStatusChanged -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

  GripsDone
  GripsToBeDeleted
  DimDataToBeDeleted

class GroundPlaneBackground(Background):
    """
    
    G
    
    r
    
    o
    
    u
    
    n
    
    d
    
    P
    
    l
    
    a
    
    n
    
    e
    
    B
    
    a
    
    c
    
    k
    
    g
    
    r
    
    o
    
    u
    
    n
    
    d
    
    (
    
    )
    """
    ColorGroundPlaneFar = None
    
    
    ColorGroundPlaneNear = None
    
    
    ColorSkyHorizon = None
    
    
    ColorSkyZenith = None
    
    
    ColorUndergroundAzimuth = None
    
    
    ColorUndergroundHorizon = None
    
    pass

class Group(DBObject):
    """
    
    G
    
    r
    
    o
    
    u
    
    p
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    G
    
    r
    
    o
    
    u
    
    p
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
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
    
     
    
    n
    
    u
    
    l
    
    l
    
     
    
    t
    
    e
    
    r
    
    m
    
    i
    
    n
    
    a
    
    t
    
    e
    
    d
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    b
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    s
    
    e
    
    l
    
    e
    
    c
    
    t
    
    a
    
    b
    
    l
    
    e
    
     
    
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
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    i
    
    s
    
     
    
    s
    
    e
    
    l
    
    e
    
    c
    
    t
    
    a
    
    b
    
    l
    
    e
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    """
    def Append(self):
        """
        Append(ObjectId) -> void
            
            ObjectId id: 
            Input objectId of the object to be appended to group
        Append(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input objectId collection containing the objectIds of the objects to be appended
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def GetAllEntityIds(self):
        """
        GetAllEntityIds -> ObjectId()
        
        """
        pass
    
    
    def GetIndex(self):
        """
        GetIndex -> Integer
            
            ObjectId id: 
            Input objectId of the object whose index is being queried
        """
        pass
    
    
    def Has(self):
        """
        Has -> bool
            
            Entity entity: 
            Input the entity being looked up
        """
        pass
    
    
    def InsertAt(self):
        """
        InsertAt(int, ObjectId) -> void
            
            int index: 
            Input insertion index
            
            ObjectId id: 
            Input objectId of the object to be inserted
        InsertAt(int, ObjectIdCollection) -> void
            
            int index: 
            Input insertion index
            
            ObjectIdCollection ids: 
            Input objectId collection containing objects to be inserted
        """
        pass
    
    
    def Prepend(self):
        """
        Prepend(ObjectId) -> void
            
            ObjectId id: 
            Input objectId of the object to be prepended to group
        Prepend(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input objectId collection containing the objectIds of the objects to be prepended
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ObjectId) -> void
            
            ObjectId id: 
            Input objectId of the object to be removed
        Remove(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input array of objectIds of objects to be removed from the group
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(int) -> void
            
            int index: 
            Input index of the object to be removed
        RemoveAt(int, ObjectIdCollection) -> void
            
            int index: 
            Input starting index of the objects to be removed
            
            ObjectIdCollection ids: 
            Input objectId array of objects to be removed after start index
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            ObjectId oldId: 
            Input objectId of the object to be removed from the group
            
            ObjectId newId: 
            Input objectId of the object to be added to the group in place of oldId
        """
        pass
    
    
    def Reverse(self):
        """
        Reverse -> void
        
        """
        pass
    
    
    def SetAnonymous(self):
        """
        SetAnonymous -> void
        
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input Color object representing the color to be set
        """
        pass
    
    
    def SetColorIndex(self):
        """
        SetColorIndex -> void
            
            int color: 
            Input AutoCAD color index to be set for entities in the group (color index must be in the range 0 to 256)
        """
        pass
    
    
    def SetHighlight(self):
        """
        SetHighlight -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input Boolean indicating whether to highlight or not
        """
        pass
    
    
    def SetLayer(self):
        """
        SetLayer(ObjectId) -> void
            
            ObjectId value: 
            Input objectId of the layer to use
        SetLayer(string) -> void
            
            string value: 
            Input null terminated string that is the name of the new layer
        """
        pass
    
    
    def SetLinetype(self):
        """
        SetLinetype(ObjectId) -> void
            
            ObjectId value: 
            Input objectId of the line type
        SetLinetype(string) -> void
            
            string value: 
            Input objectId null terminated string that is the name of the new line type
        """
        pass
    
    
    def SetLinetypeScale(self):
        """
        SetLinetypeScale -> void
            
            double value: 
            Input new value for the line type scale
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input enum value for visibility
        """
        pass
    
    
    def Transfer(self):
        """
        Transfer -> void
            
            int fromIndex: 
            Input start index to transfer from
            
            int toIndex: 
            Input start index to transfer to
            
            int numItems: 
            Input number of items to transfer
        """
        pass
    
    
    Description = None
    
    
    IsAnonymous = None
    
    
    IsNotAccessible = None
    
    
    Name = None
    
    
    NumEntities = None
    
    
    Selectable = None
    
    pass

  ArrowMark = 1
  BlockMark = 0x3a9c
  DoglegMark = 0x2711
  LeaderLineMark = 0x1389
  MTextMark = 0x3a99
  MTextUnderLineMark = 0x3a9a
  None = 0
  ToleranceMark = 0x3a9b

class Handle(public struct Handle {
}):
    """
    
    H
    
    a
    
    n
    
    d
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    l
    
    o
    
    n
    
    g
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
    l
    
    l
    
     
    
    6
    
    4
    
     
    
    b
    
    i
    
    t
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    IsOne = None
    
    
    Value = None
    
    pass

class Hatch(Entity):
    """
    
    H
    
    a
    
    t
    
    c
    
    h
    
    (
    
    )
    """
    def AppendLoop(self):
        """
        AppendLoop(HatchLoop) -> void
            
            HatchLoop hatchLoop: 
            Input type of loop
        AppendLoop(HatchLoopTypes, Curve2dCollection, IntegerCollection) -> void
            
            HatchLoopTypes loopType: 
            Input loop type.
            
            Curve2dCollection edgePtrCollection: 
            Input set of curve 2d.
            
            IntegerCollection edgeTypeCollection: 
            Input set of enumerated edge types.
        AppendLoop(HatchLoopTypes, ObjectIdCollection) -> void
            
            HatchLoopTypes loopType: 
            Input loop type
            
            ObjectIdCollection dbObjIds: 
            Input set of object IDs
        AppendLoop(HatchLoopTypes, Point2dCollection, DoubleCollection) -> void
            
            HatchLoopTypes loopType: 
            Input type of loop.
            
            Point2dCollection vertexCollection: 
            Input set of point 2d.
            
            DoubleCollection bulgeCollection: 
            Input set of double values.
        """
        pass
    
    
    def EvaluateGradientColorAt(self):
        """
        EvaluateGradientColorAt -> Autodesk.AutoCAD.Colors.Color
            
            float value: 
            Input normalized value, [0.0...1.0], at which to evaluate the gradient color
        """
        pass
    
    
    def EvaluateHatch(self):
        """
        EvaluateHatch -> void
            
            [MarshalAs(UnmanagedType.U1)] bool underEstimateNumLines: 
            If true, underestimates the count before deciding to abort. That is, if Hatch::EvaluateHatch(true) is used, the function will abort if the count is in excess of 100,000.
        """
        pass
    
    
    def GetAssociatedObjectIds(self):
        """
        GetAssociatedObjectIds -> ObjectIdCollection
        
        """
        pass
    
    
    def GetAssociatedObjectIdsAt(self):
        """
        GetAssociatedObjectIdsAt -> ObjectIdCollection
            
            int loopIndex: 
            Input index for the selected loop
        """
        pass
    
    
    def GetGradientColors(self):
        """
        GetGradientColors -> GradientColor()
        
        """
        pass
    
    
    def GetHatchLineDataAt(self):
        """
        GetHatchLineDataAt -> Line2d
            
            int index: 
            Input number at which the hatch line data will be returned
        """
        pass
    
    
    def GetHatchLinesData(self):
        """
        GetHatchLinesData -> Line2dCollection
        
        """
        pass
    
    
    def GetLoopAt(self):
        """
        GetLoopAt -> HatchLoop
            
            int loopIndex: 
            Input index of selected loop
        """
        pass
    
    
    def GetPatternDefinitionAt(self):
        """
        GetPatternDefinitionAt -> PatternDefinition
            
            int index: 
            Input pattern index
        """
        pass
    
    
    def InsertLoopAt(self):
        """
        InsertLoopAt(int, HatchLoop) -> void
            
            int loopIndex: 
            Input index for the selected loop
            
            HatchLoop hatchLoop: 
            Input loop type
        InsertLoopAt(int, HatchLoopTypes, ObjectIdCollection) -> void
            
            int loopIndex: 
            Input index for the selected loop
            
            HatchLoopTypes loopType: 
            Input loop type
            
            ObjectIdCollection dbObjIds: 
            Input set of object IDs
        """
        pass
    
    
    def LoopTypeAt(self):
        """
        LoopTypeAt -> HatchLoopTypes
            
            int loopIndex: 
            Input index of the selected loop
        """
        pass
    
    
    def RemoveAssociatedObjectIds(self):
        """
        RemoveAssociatedObjectIds -> void
        
        """
        pass
    
    
    def RemoveLoopAt(self):
        """
        RemoveLoopAt -> void
            
            int loopIndex: 
            Input index for the selected loop
        """
        pass
    
    
    def SetGradientColors(self):
        """
        SetGradientColors -> void
            
            GradientColor[] value: 
            Input array of floats representing the interpolation values defining the gradient
        """
        pass
    
    
    def SetGradient(self):
        """
        SetGradient -> void
            
            Autodesk.AutoCAD.DatabaseServices.GradientPatternType gradientType: 
            Input gradient type
            
            string gradientName: 
            Input name of the gradient to apply
        """
        pass
    
    
    def SetHatchPattern(self):
        """
        SetHatchPattern -> void
            
            Autodesk.AutoCAD.DatabaseServices.HatchPatternType patternType: 
            Input enumerated number of pattern type
            
            string patternName: 
            Input name of the pattern
        """
        pass
    
    
    Area = None
    
    
    Associative = None
    
    
    BackgroundColor = None
    
    
    Elevation = None
    
    
    GradientAngle = None
    
    
    GradientName = None
    
    
    GradientOneColorMode = None
    
    
    GradientShift = None
    
    
    GradientType = None
    
    
    HatchObjectType = None
    
    
    HatchStyle = None
    
    
    IsGradient = None
    
    
    IsHatch = None
    
    
    IsSolidFill = None
    
    
    Normal = None
    
    
    NumberOfHatchLines = None
    
    
    NumberOfLoops = None
    
    
    NumberOfPatternDefinitions = None
    
    
    Origin = None
    
    
    PatternAngle = None
    
    
    PatternDouble = None
    
    
    PatternName = None
    
    
    PatternScale = None
    
    
    PatternSpace = None
    
    
    PatternType = None
    
    
    ShadeTintValue = None
    
    pass

  CircularArc = 2
  EllipticalArc = 3
  Line = 1
  Spline = 4

class HatchLoop(public sealed class HatchLoop):
    """
    
    H
    
    a
    
    t
    
    c
    
    h
    
    L
    
    o
    
    o
    
    p
    
    
    
    
     
    
     
    
     
    
     
    
    H
    
    a
    
    t
    
    c
    
    h
    
    L
    
    o
    
    o
    
    p
    
    T
    
    y
    
    p
    
    e
    
    s
    
     
    
    l
    
    o
    
    o
    
    p
    
    T
    
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
    
     
    
    l
    
    o
    
    o
    
    p
    """
    Curves = None
    
    
    IsPolyline = None
    
    
    LoopType = None
    
    
    Polyline = None
    
    pass

  Default = 0
  Derived = 4
  Duplicate = 0x100
  External = 1
  NotClosed = 0x20
  Outermost = 0x10
  Polyline = 2
  SelfIntersecting = 0x40
  Textbox = 8
  TextIsland = 0x80

  HatchObject
  GradientObject

  UserDefined
  PreDefined
  CustomDefined

  Normal
  Outer
  Ignore

class Helix(Spline):
    """
    
    H
    
    e
    
    l
    
    i
    
    x
    
    (
    
    )
    """
    def CreateHelix(self):
        """
        CreateHelix -> void
        
        """
        pass
    
    
    def GetAxisPoint(self):
        """
        GetAxisPoint -> Point3d
        
        """
        pass
    
    
    def SetAxisPoint(self):
        """
        SetAxisPoint -> void
            
            Point3d axisPoint: 
            Input the 3D point where the axis starts
            
            [MarshalAs(UnmanagedType.U1)] bool moveStartPoint: 
            Input Boolean indicating whether to relocate the start point by the same offset that the axis point moved
        """
        pass
    
    
    AxisVector = None
    
    
    BaseRadius = None
    
    
    Constrain = None
    
    
    Height = None
    
    
    StartPoint = None
    
    
    TopRadius = None
    
    
    TotalLength = None
    
    
    TurnHeight = None
    
    
    Turns = None
    
    
    TurnSlope = None
    
    
    Twist = None
    
    pass

class HelpParameter(ConstraintGroupNode):
    """
    
    H
    
    e
    
    l
    
    p
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    (
    
    )
    """
    ConnectedConstraint = None
    
    
    ConnectedEqualparamConstraints = None
    
    
    ConnectedGeometry = None
    
    
    Value = None
    
    pass

class HighlightOverrule(Overrule):
    """
    
    """
    def Highlight(self):
        """
        Highlight -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def Unhighlight(self):
        """
        Unhighlight -> void
        
        """
        pass
    
    pass

class HighlightStateOverrule(Overrule):
    """
    
    """
    def HighlightState(self):
        """
        HighlightState -> HighlightStyle
        
        """
        pass
    
    
    def PopHighlight(self):
        """
        PopHighlight -> void
        
        """
        pass
    
    
    def PushHighlight(self):
        """
        PushHighlight -> void
        
        """
        pass
    
    pass

class HorizontalConstraint(ParallelConstraint):
    """
    
    H
    
    o
    
    r
    
    i
    
    z
    
    o
    
    n
    
    t
    
    a
    
    l
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class HostApplicationServices(RXObject):
    """
    
    """
    def FatalError(self):
        """
        FatalError -> void
            
            string message: 
            The error message.
        """
        pass
    
    
    def GetEnvironmentVariable(self):
        """
        GetEnvironmentVariable -> string
        
        """
        pass
    
    
    def GetRemoteFile(self):
        """
        GetRemoteFile -> string
            
            Uri url: 
            Input URL
            
            [MarshalAs(UnmanagedType.U1)] bool ignoreCache: 
            Input Boolean indicating whether to download the file even if it has be cached earlier in the session
        """
        pass
    
    
    def GetUrl(self):
        """
        GetUrl -> Uri
            
            string localFile: 
            Input local file
        """
        pass
    
    
    def IsUrl(self):
        """
        IsUrl -> bool
            
            string filePath: 
            Input string to be evaluated
        """
        pass
    
    
    def LoadApplication(self):
        """
        LoadApplication -> void
            
            string appName: 
            Input null-terminated string which is the application name (as set in the system registry) of the ObjectARX module to load
            
            ApplicationLoadReasons why: 
            Input LoadReasons values to use during this load
            
            [MarshalAs(UnmanagedType.U1)] bool printIt: 
            Input Boolean indicating whether or not to print load status message
            
            [MarshalAs(UnmanagedType.U1)] bool asCmd: 
            Input Boolean indicating whether to load the application as if by user command
        """
        pass
    
    
    def NotifyCorruptDrawingFoundOnOpen(self):
        """
        NotifyCorruptDrawingFoundOnOpen -> bool
            
            ObjectId id: 
            The ID of the corrupt DB object that cannot be read.
            
            Autodesk.AutoCAD.Runtime.ErrorStatus es: 
            The return code of the attempt to read in the corrupt DB object.
        """
        pass
    
    
    def PutRemoteFile(self):
        """
        PutRemoteFile -> void
            
            Uri url: 
            Input URL to which to upload file
            
            string localFile: 
            Input local file to upload
        """
        pass
    
    
    def UserBreak(self):
        """
        UserBreak -> bool
        
        """
        pass
    
    
    def FindFile(self):
        """
        FindFile -> string
            
            string fileName: 
            Given name of the file to find.
            
            Database database: 
            This will give you the path to the DWG file associated with the database, which may also be searched for the requested file. If this file search is not related to a database, database will be NULL.
            
            Autodesk.AutoCAD.DatabaseServices.FindFileHint hint: 
            Caller may pass you a hint, that you may choose to use to narrow your search.
            Default: 
            Any file
            FontFile: 
            Could be either a shape or TrueType font
            CompiledShapeFile: 
            A shape font file
            TrueTypeFontFile: 
            A TrueType font file
            EmbeddedImageFile: 
            An image file
            XRefDrawing: 
            A drawing template
            PatternFile: 
            A hatch pattern file
            ARXApplication: 
            An ObjectARX program
        """
        pass
    
    
    def GetPassword(self):
        """
        GetPassword -> string
            
            string dwgName: 
            Name of the drawing file that is requiring a password
            
            Autodesk.AutoCAD.DatabaseServices.PasswordOptions options: 
            Boolean indicating whether dwgName refers to an xref'd drawing
        """
        pass
    
    
    AllUsersRootFolder = None
    
    
    AlternateFontName = None
    
    
    ColorBookLocation = None
    
    
    CompanyName = None
    
    
    Current = None
    
    
    FontMapFileName = None
    
    
    LocalRootFolder = None
    
    
    MachineRegistryProductRootKey = None
    
    
    ModelerFlavor = None
    
    
    Product = None
    
    
    Program = None
    
    
    releaseMarketVersion = None
    
    
    RoamableRootFolder = None
    
    
    UserRegistryProductRootKey = None
    
    
    WorkingDatabase = None
    
    pass

class HyperLink(DisposableWrapper):
    """
    
    H
    
    y
    
    p
    
    e
    
    r
    
    L
    
    i
    
    n
    
    k
    
    (
    
    )
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    Description = None
    
    
    DisplayString = None
    
    
    IsOutermostContainer = None
    
    
    Name = None
    
    
    NestedLevel = None
    
    
    SubLocation = None
    
    pass

class HyperLinkCollection(DisposableWrapper, IList):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            HyperLink value: 
            Item to add.
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
            
            HyperLink value: 
            Item to check for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            HyperLink[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            HyperLink value: 
            Item to look for.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Location to insert at
            
            HyperLink value: 
            Item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            HyperLink value: 
            Object to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of object to remove.
        """
        pass
    
    
    Count = None
    
    pass

class IBLBackground(Background):
    """
    
    I
    
    B
    
    L
    
    B
    
    a
    
    c
    
    k
    
    g
    
    r
    
    o
    
    u
    
    n
    
    d
    
    (
    
    )
    """
    DisplayImage = None
    
    
    Enable = None
    
    
    IBLImageName = None
    
    
    Rotation = None
    
    
    SecondaryBackground = None
    
    pass

class ITextEditorSelectable(public interface ITextEditorSelectable):
    """
    
    """

    pass

class IdMapping(RXObject, IEnumerable):
    """
    
    I
    
    d
    
    M
    
    a
    
    p
    
    p
    
    i
    
    n
    
    g
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> void
            
            IdPair pairToAdd: 
            Input IdPair to add
        """
        pass
    
    
    def Change(self):
        """
        Change -> void
        
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ObjectId key: 
            Input key to look for
        """
        pass
    
    
    def Delete(self):
        """
        Delete -> void
            
            ObjectId key: 
            Input objectId which is the key of the ID pair to be deleted from the map
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Lookup(self):
        """
        Lookup -> IdPair
            
            ObjectId key: 
            Input key to look for
        """
        pass
    
    
    DeepCloneContext = None
    
    
    DestinationDatabase = None
    
    
    DuplicateRecordCloning = None
    
    
    OriginalDatabase = None
    
    pass

class IdMappingEventArgs(EventArgs):
    """
    
    """
    IdMapping = None
    
    pass

class IdPair(public struct IdPair {
}):
    """
    
    I
    
    d
    
    P
    
    a
    
    i
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    k
    
    e
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    k
    
    e
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    i
    
    s
    
    C
    
    l
    
    o
    
    n
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    i
    
    f
    
     
    
    i
    
    t
    
     
    
    h
    
    a
    
    s
    
     
    
    b
    
    e
    
    e
    
    n
    
     
    
    c
    
    l
    
    o
    
    n
    
    e
    
    d
    
     
    
    a
    
    l
    
    r
    
    e
    
    a
    
    d
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    i
    
    s
    
    P
    
    r
    
    i
    
    m
    
    a
    
    r
    
    y
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    i
    
    f
    
     
    
    i
    
    t
    
     
    
    i
    
    s
    
     
    
    a
    
     
    
    p
    
    r
    
    i
    
    m
    
    a
    
    r
    
    y
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    i
    
    s
    
    O
    
    w
    
    n
    
    e
    
    r
    
    T
    
    r
    
    a
    
    n
    
    s
    
    l
    
    a
    
    t
    
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
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    i
    
    f
    
     
    
    i
    
    t
    
    s
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    h
    
    a
    
    s
    
     
    
    a
    
    l
    
    r
    
    e
    
    a
    
    d
    
    y
    
     
    
    b
    
    e
    
    e
    
    n
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    l
    
    a
    
    t
    
    e
    
    d
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Culture-specific format
        """
        pass
    
    
    IsCloned = None
    
    
    IsOwnerTranslated = None
    
    
    IsPrimary = None
    
    
    Key = None
    
    
    Value = None
    
    pass

class Image(Entity):
    """
    
    """

    pass

class ImageBackground(Background):
    """
    
    I
    
    m
    
    a
    
    g
    
    e
    
    B
    
    a
    
    c
    
    k
    
    g
    
    r
    
    o
    
    u
    
    n
    
    d
    
    (
    
    )
    """
    FitToScreen = None
    
    
    ImageFileName = None
    
    
    MaintainAspectRatio = None
    
    
    Offset = None
    
    
    Scale = None
    
    
    UseTiling = None
    
    pass

  Clip = 4
  Show = 1
  ShowUnaligned = 2
  Transparent = 8

  Draft = 0
  High = 1
  Invalid = -1

  StartImplicit
  EndImplicit
  MidImplicit
  CenterImplicit
  DefineImplicit

  NoIndex
  IndexByLayer
  IndexSpatially

class InterferenceProtocolExtension(RXObject):
    """
    
    """
    def CreateInterferenceObjects(self):
        """
        CreateInterferenceObjects -> Entity()
            
            Entity ent1: 
            Input entity 1
            
            Entity ent2: 
            Input entity 2
            
            int flags: 
            Input interference flags
        """
        pass
    
    pass

  OnBothOperands
  ExtendThis
  ExtendArgument
  ExtendBoth

class ItemLocator(public struct ItemLocator {
}):
    """
    
    I
    
    t
    
    e
    
    m
    
    L
    
    o
    
    c
    
    a
    
    t
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
    t
    
    e
    
    m
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    i
    
    n
    
    p
    
    u
    
    t
    
     
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    r
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
     
    
    i
    
    t
    
    e
    
    m
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    >
    
    =
    
     
    
    0
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    r
    
    o
    
    w
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    i
    
    n
    
    p
    
    u
    
    t
    
     
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    r
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    r
    
    o
    
    w
    
    .
    
     
    
    r
    
    o
    
    w
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    >
    
    =
    
     
    
    0
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    l
    
    e
    
    v
    
    e
    
    l
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    i
    
    n
    
    p
    
    u
    
    t
    
     
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    r
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    l
    
    e
    
    v
    
    e
    
    l
    
    .
    
     
    
    l
    
    e
    
    v
    
    e
    
    l
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    >
    
    =
    
    0
    
    .
    """
    ItemIndex = None
    
    
    LevelIndex = None
    
    
    RowIndex = None
    
    pass

  StyleNone
  StyleRound
  StyleAngle
  StyleFlat

  D65White
  Fluorescent
  CoolWhite
  WhiteFluorescent
  DaylightFluorescent
  Incandescent
  Xenon
  Halogen
  Quartz
  MetalHalide
  Mercury
  PhosphorMercury
  HighPressureSodium
  LowPressureSodium
  Custom

  Kelvin
  Preset

  NoNewLayerEvaluation
  EvalNewXrefLayers
  EvalAllNewLayers

class LayerStateManager(RXObject):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    S
    
    t
    
    a
    
    t
    
    e
    
    M
    
    a
    
    n
    
    a
    
    g
    
    e
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    :
    
     
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
    o
    
    r
    
    .
    """
    def CompareLayerStateToDb(self):
        """
        CompareLayerStateToDb -> bool
            
            string name: 
            Input name of layer state to be compared to the drawing.
            
            ObjectId idVp: 
            Input object ID of the viewport whose VPLAYER settings are to be used when comparing.
        """
        pass
    
    
    def DeleteLayerState(self):
        """
        DeleteLayerState -> void
            
            string name: 
            Input layer state name to delete
        """
        pass
    
    
    def ExportLayerState(self):
        """
        ExportLayerState -> void
            
            string nameToExport: 
            Input layer state name to export
            
            string fileName: 
            Input filename to export layer state to
        """
        pass
    
    
    def GetLayerStateDescription(self):
        """
        GetLayerStateDescription -> string
            
            string name: 
            Input layer state whose description is to be retrieved
        """
        pass
    
    
    def GetLayerStateLayers(self):
        """
        GetLayerStateLayers -> ArrayList
            
            string name: 
            Input the name of the layer state to query
            
            [MarshalAs(UnmanagedType.U1)] bool bInvert: 
            Input if true, the returned array will contain the names of the layers in the current drawing that are NOT saved in the layer state.
        """
        pass
    
    
    def GetLayerStateMask(self):
        """
        GetLayerStateMask -> LayerStateMasks
            
            string name: 
            Input layer state name
        """
        pass
    
    
    def GetLayerStateNames(self):
        """
        GetLayerStateNames -> ArrayList
            
            [MarshalAs(UnmanagedType.U1)] bool bIncludeHidden: 
            Input flag to include names of hidden layer states in array.
            
            [MarshalAs(UnmanagedType.U1)] bool bIncludeXref: 
            Input flag to include XRefs
        """
        pass
    
    
    def HasLayerState(self):
        """
        HasLayerState -> bool
            
            string name: 
            Input layer state name
        """
        pass
    
    
    def ImportLayerState(self):
        """
        ImportLayerState -> void
            
            string fileName: 
            Input file to extract layer states from
        """
        pass
    
    
    def ImportLayerStateFromDb(self):
        """
        ImportLayerStateFromDb -> void
            
            string name: 
            Input the name of the layer state to be imported
            
            Database database: 
            Input a pointer to a valid, readable database from which the layer state is to be imported.
        """
        pass
    
    
    def LayerStateHasViewportData(self):
        """
        LayerStateHasViewportData -> bool
            
            string name: 
            Input layer state to be interrogated
        """
        pass
    
    
    def LayerStatesDictionaryId(self):
        """
        LayerStatesDictionaryId -> ObjectId
            
            [MarshalAs(UnmanagedType.U1)] bool createIfNotPresent: 
            Input flag controlling dictionary creation
        """
        pass
    
    
    def RenameLayerState(self):
        """
        RenameLayerState -> void
            
            string name: 
            Input existing layer state name
            
            string newName: 
            Input new layer state name
        """
        pass
    
    
    def RestoreLayerState(self):
        """
        RestoreLayerState -> void
            
            string name: 
            Input name of layer state to make current
            
            ObjectId id: 
            Input object ID of the viewport whose VPLAYER setting is to be updated with the viewport data stored
            
            int undefinedLayerStatePolicy: 
            Input value that indicates whether to handle undefined layers
            
            LayerStateMasks clientMask: 
            Input layer attribute mask
        """
        pass
    
    
    def SaveLayerState(self):
        """
        SaveLayerState -> void
            
            string name: 
            Input name of layer state to save
            
            LayerStateMasks mask: 
            Input mask to apply to layer state
            
            ObjectId id: 
            Input object ID of the viewport whose VPLAYER setting is to be captured
        """
        pass
    
    
    def SetLayerStateDescription(self):
        """
        SetLayerStateDescription -> void
            
            string name: 
            Input layer state whose description is to be updated
            
            string description: 
            Input description string up to 255 characters
        """
        pass
    
    
    def SetLayerStateMask(self):
        """
        SetLayerStateMask -> void
            
            string name: 
            Input name of layer state to mask
            
            LayerStateMasks mask: 
            Input mask to apply to layer state
        """
        pass
    
    
    LastRestoredLayerState = None
    
    pass

  Color = &H20
  CurrentViewport = &H200
  Frozen = 2
  LastRestored = &H10000
  LineType = &H40
  LineWeight = &H80
  Locked = 4
  NewViewport = &H10
  None = 0
  On = 1
  Plot = 8
  PlotStyle = &H100
  Transparency = &H400

class LayerTable(SymbolTable):
    """
    
    """
    def GenerateUsageData(self):
        """
        GenerateUsageData -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> SymbolTableEnumerator
        
        """
        pass
    
    
    def GetUnreconciledLayers(self):
        """
        GetUnreconciledLayers -> ObjectIdCollection
            
            idArray: 
            Input ID of the array to retrieve the unreconciled layers
        """
        pass
    
    
    HasUnreconciledLayers = None
    
    
    IncludingHidden = None
    
    
    SkippingReconciled = None
    
    pass

class LayerTableRecord(SymbolTableRecord):
    """
    
    L
    
    a
    
    y
    
    e
    
    r
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    )
    """
    def GetViewportOverrides(self):
        """
        GetViewportOverrides -> LayerViewportProperties
        
        """
        pass
    
    
    def HasViewportOverrides(self):
        """
        HasViewportOverrides -> bool
            
            ObjectId viewportId: 
            The object id of the viewport.
        """
        pass
    
    
    def RemoveAllOverrides(self):
        """
        RemoveAllOverrides -> void
        
        """
        pass
    
    
    Color = None
    
    
    Description = None
    
    
    EntityColor = None
    
    
    HasOverrides = None
    
    
    IsFrozen = None
    
    
    IsHidden = None
    
    
    IsLocked = None
    
    
    IsOff = None
    
    
    IsPlottable = None
    
    
    IsReconciled = None
    
    
    IsUsed = None
    
    
    LinetypeObjectId = None
    
    
    LineWeight = None
    
    
    MaterialId = None
    
    
    PlotStyleName = None
    
    
    PlotStyleNameId = None
    
    
    Transparency = None
    
    
    ViewportVisibilityDefault = None
    
    pass

class LayerViewportProperties(public sealed class LayerViewportProperties):
    """
    
    """
    def RemoveOverrides(self):
        """
        RemoveOverrides -> void
        
        """
        pass
    
    
    Color = None
    
    
    IsColorOverridden = None
    
    
    IsLinetypeOverridden = None
    
    
    IsLineWeightOverridden = None
    
    
    IsPlotStyleOverridden = None
    
    
    IsTransparencyOverridden = None
    
    
    LinetypeObjectId = None
    
    
    LineWeight = None
    
    
    PlotStyleName = None
    
    
    PlotStyleNameId = None
    
    
    Transparency = None
    
    pass

class Layout(PlotSettings):
    """
    
    L
    
    a
    
    y
    
    o
    
    u
    
    t
    
    (
    
    )
    """
    def AddToLayoutDictionary(self):
        """
        AddToLayoutDictionary -> void
            
            Database toWhichDatabase: 
            Input database to which to add the layout
            
            ObjectId blockTableRecordId: 
            Input block table record to use
        """
        pass
    
    
    def GetViewports(self):
        """
        GetViewports -> ObjectIdCollection
        
        """
        pass
    
    
    def Initialize(self):
        """
        Initialize -> ObjectId
        
        """
        pass
    
    
    AnnoAllVisible = None
    
    
    BlockTableRecordId = None
    
    
    Extents = None
    
    
    LayoutName = None
    
    
    Limits = None
    
    
    TabOrder = None
    
    
    TabSelected = None
    
    
    Thumbnail = None
    
    pass

class LayoutCopiedEventArgs(EventArgs):
    """
    
    """
    Id = None
    
    
    Name = None
    
    
    NewId = None
    
    
    NewName = None
    
    pass

class LayoutEventArgs(EventArgs):
    """
    
    """
    Id = None
    
    
    Name = None
    
    pass

class LayoutManager(RXObject):
    """
    
    """
    def CloneLayout(self):
        """
        CloneLayout -> void
            
            string copyName: 
            Input to the old Layout name
            
            string newName: 
            Input the name for new layout
            
            int newTabOrder: 
            Optional input integer specifying new tab order
        """
        pass
    
    
    def CopyLayout(self):
        """
        CopyLayout -> void
            
            string copyName: 
            Input name of Layout object to be copied
            
            string newName: 
            Input name for new copy of Layout object
        """
        pass
    
    
    def CreateLayout(self):
        """
        CreateLayout -> ObjectId
            
            string newName: 
            Input name to give new Layout object
        """
        pass
    
    
    def DeleteLayout(self):
        """
        DeleteLayout -> void
            
            string deleteName: 
            Input name of Layout object to delete
        """
        pass
    
    
    def GetLayoutId(self):
        """
        GetLayoutId -> ObjectId
            
            string name: 
            Input name of Layout object to search for
        """
        pass
    
    
    def GetNonRectangularViewportIdFromClipId(self):
        """
        GetNonRectangularViewportIdFromClipId -> ObjectId
            
            ObjectId clipId: 
            Input ObjectId of clip entity to get the nonrectangular viewport ID from
            
            name: 
            Input name of Layout object to search for.
        """
        pass
    
    
    def LayoutExists(self):
        """
        LayoutExists -> bool
            
            string name: 
            Input name of layout to find.
        """
        pass
    
    
    def RenameLayout(self):
        """
        RenameLayout -> void
            
            string oldName: 
            Input name of Layout object to rename
            
            string newName: 
            Input new name for renamed Layout object
        """
        pass
    
    
    def SetCurrentLayoutId(self):
        """
        SetCurrentLayoutId -> void
        
        """
        pass
    
    
    Current = None
    
    
    CurrentLayout = None
    
    
    LayoutCount = None
    
    pass

class LayoutRenamedEventArgs(EventArgs):
    """
    
    """
    Id = None
    
    
    Name = None
    
    
    NewName = None
    
    pass

class Leader(Curve):
    """
    
    L
    
    e
    
    a
    
    d
    
    e
    
    r
    
    (
    
    )
    """
    def AppendVertex(self):
        """
        AppendVertex -> bool
            
            Point3d pointToAdd: 
            Input point (in WCS coordinates) to add to the vertex list
        """
        pass
    
    
    def EvaluateLeader(self):
        """
        EvaluateLeader -> void
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def RemoveLastVertex(self):
        """
        RemoveLastVertex -> void
        
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input objectId of the desired DimensionStyle
        """
        pass
    
    
    def SetPlane(self):
        """
        SetPlane -> void
            
            Plane value: 
            Input desired plane within which the leader will reside
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt -> bool
            
            int index: 
            Input index number (0 based) of the vertex to change
            
            Point3d pointValue: 
            Input new point value (in WCS) to use
        """
        pass
    
    
    def VertexAt(self):
        """
        VertexAt -> Point3d
            
            int value: 
            Input index number (0 based) of the vertex desired
        """
        pass
    
    
    AnnoHeight = None
    
    
    Annotation = None
    
    
    AnnotationOffset = None
    
    
    AnnoType = None
    
    
    AnnoWidth = None
    
    
    Dimasz = None
    
    
    Dimclrd = None
    
    
    DimensionStyle = None
    
    
    DimensionStyleName = None
    
    
    Dimgap = None
    
    
    Dimldrblk = None
    
    
    Dimlwd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimtad = None
    
    
    Dimtxt = None
    
    
    FirstVertex = None
    
    
    HasArrowHead = None
    
    
    HasHookLine = None
    
    
    IsSplined = None
    
    
    LastVertex = None
    
    
    Normal = None
    
    
    NumVertices = None
    
    pass

  UnknownLeader
  LeftLeader
  RightLeader
  TopLeader
  BottomLeader

  InVisibleLeader
  StraightLeader
  SplineLeader

class Light(Entity):
    """
    
    L
    
    i
    
    g
    
    h
    
    t
    
    (
    
    )
    """
    def ResultingColor(self):
        """
        ResultingColor -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def SetHotspotAndFalloff(self):
        """
        SetHotspotAndFalloff -> void
            
            double hotspot: 
            Input the hotspot cone angle, in radians. Defines the brightest part of the spot light beam. Must be smaller than or equal to the falloff.
            
            double falloff: 
            Input the falloff cone angle, in radians. Defines the full cone of light. This is also known as the field angle. Must be larger than the hotspot.
        """
        pass
    
    
    Attenuation = None
    
    
    AttenuationType = None
    
    
    Direction = None
    
    
    EndLimitOffset = None
    
    
    FalloffAngle = None
    
    
    HasTarget = None
    
    
    HotspotAngle = None
    
    
    IlluminanceDistance = None
    
    
    Intensity = None
    
    
    IsOn = None
    
    
    IsPlottable = None
    
    
    LampColorPreset = None
    
    
    LampColorRGB = None
    
    
    LampColorTemp = None
    
    
    LampColorType = None
    
    
    LightColor = None
    
    
    LightType = None
    
    
    MapSize = None
    
    
    Name = None
    
    
    PhysicalIntensity = None
    
    
    PhysicalIntensityMethod = None
    
    
    Position = None
    
    
    Shadow = None
    
    
    ShadowType = None
    
    
    Softness = None
    
    
    StartLimitOffset = None
    
    
    TargetLocation = None
    
    
    UseLimits = None
    
    
    WebFile = None
    
    
    WebRotation = None
    
    pass

  LightingUnitsGeneric
  LightingUnitsAmerican
  LightingUnitsInternational

class Line(Curve):
    """
    
    L
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    e
    
    n
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    """
    Angle = None
    
    
    Delta = None
    
    
    EndPoint = None
    
    
    Length = None
    
    
    Normal = None
    
    
    StartPoint = None
    
    
    Thickness = None
    
    pass

class LineAngularDimension2(Dimension):
    """
    
    L
    
    i
    
    n
    
    e
    
    A
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    2
    
    (
    
    )
    
    (
    
    )
    """
    ArcPoint = None
    
    
    XLine1End = None
    
    
    XLine1Start = None
    
    
    XLine2End = None
    
    
    XLine2Start = None
    
    pass

  AtLeast = 1
  Exactly = 2

  ByBlock = -2
  ByLayer = -1
  ByLineWeightDefault = -3
  LineWeight000 = 0
  LineWeight005 = 5
  LineWeight009 = 9
  LineWeight013 = 13
  LineWeight015 = 15
  LineWeight018 = 0x12
  LineWeight020 = 20
  LineWeight025 = 0x19
  LineWeight030 = 30
  LineWeight035 = 0x23
  LineWeight040 = 40
  LineWeight050 = 50
  LineWeight053 = 0x35
  LineWeight060 = 60
  LineWeight070 = 70
  LineWeight080 = 80
  LineWeight090 = 90
  LineWeight100 = 100
  LineWeight106 = 0x6a
  LineWeight120 = 120
  LineWeight140 = 140
  LineWeight158 = 0x9e
  LineWeight200 = 200
  LineWeight211 = 0xd3

class LineWeightConverter(TypeConverter):
    """
    
    """
    def ConvertFrom(self):
        """
        ConvertFrom -> object
            
            ITypeDescriptorContext context: 
            Input context to convert within
            
            CultureInfo culture: 
            Input culture to convert within
            
            object value: 
            Input object to convert from
        """
        pass
    
    
    def CanConvertFrom(self):
        """
        CanConvertFrom -> bool
            
            ITypeDescriptorContext context: 
            Input context with which to handle source
            
            Type sourceType: 
            Input source type
        """
        pass
    
    
    def ConvertTo(self):
        """
        ConvertTo -> object
            
            ITypeDescriptorContext context: 
            Input context within which to handle value
            
            CultureInfo culture: 
            Input culture within which to handle value
            
            object value: 
            Input value to process
        """
        pass
    
    pass

class LinetypeTable(SymbolTable, IEnumerable):
    """
    
    """

    pass

class LinetypeTableRecord(SymbolTableRecord):
    """
    
    L
    
    i
    
    n
    
    e
    
    t
    
    y
    
    p
    
    e
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    )
    """
    def DashLengthAt(self):
        """
        DashLengthAt -> double
            
            int index: 
            Input index (0-based) of dash to get length of
        """
        pass
    
    
    def SetDashLengthAt(self):
        """
        SetDashLengthAt -> void
            
            int index: 
            Input index (0-based) of dash to set
            
            double value: 
            Input length value for the dash
        """
        pass
    
    
    def SetShapeIsUcsOrientedAt(self):
        """
        SetShapeIsUcsOrientedAt -> void
            
            int index: 
            Input index (0-based) of shape (or text string) to get
            
            [MarshalAs(UnmanagedType.U1)] bool isOriented: 
            Input Boolean indicating whether or not the shape is to be oriented relative to the current UCS
        """
        pass
    
    
    def SetShapeNumberAt(self):
        """
        SetShapeNumberAt -> void
            
            int index: 
            Input index at which to set the shape
            
            int shapeNumber: 
            Input shape identification number of the shape to use
        """
        pass
    
    
    def SetShapeOffsetAt(self):
        """
        SetShapeOffsetAt -> void
            
            int index: 
            Input index at which to set the shape (or text string) offset
            
            Vector2d offset: 
            Input vector whose X and Y values are the WCS X and Y offsets for the shape
        """
        pass
    
    
    def SetShapeRotationAt(self):
        """
        SetShapeRotationAt -> void
            
            int index: 
            Input index (0-based) of shape (or text string) to get
            
            double rotation: 
            Input rotation angle for the shape (or text string)
        """
        pass
    
    
    def SetShapeScaleAt(self):
        """
        SetShapeScaleAt -> void
            
            int index: 
            Input index at which to set the shape (or text string) scale
            
            double scale: 
            Input scale factor to be applied to the shape
        """
        pass
    
    
    def SetShapeStyleAt(self):
        """
        SetShapeStyleAt -> void
            
            int index: 
            Input index at which to set the shape (or text string) scale
            
            ObjectId id: 
            Input scale factor to be applied to the shape (or text string)
        """
        pass
    
    
    def SetTextAt(self):
        """
        SetTextAt -> void
            
            int index: 
            Input index at which to set the text string
            
            string value: 
            Input pointer to the text to use at index
        """
        pass
    
    
    def ShapeIsUcsOrientedAt(self):
        """
        ShapeIsUcsOrientedAt -> bool
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeNumberAt(self):
        """
        ShapeNumberAt -> Integer
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeOffsetAt(self):
        """
        ShapeOffsetAt -> Vector2d
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeRotationAt(self):
        """
        ShapeRotationAt -> double
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeScaleAt(self):
        """
        ShapeScaleAt -> double
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeStyleAt(self):
        """
        ShapeStyleAt -> ObjectId
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def TextAt(self):
        """
        TextAt -> string
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    AsciiDescription = None
    
    
    Comments = None
    
    
    IsScaledToFit = None
    
    
    NumDashes = None
    
    
    PatternLength = None
    
    pass

class LinkedData(DBObject):
    """
    
    """
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    IsEmpty = None
    
    
    Name = None
    
    pass

class LinkedTableData(LinkedData):
    """
    
    L
    
    i
    
    n
    
    k
    
    e
    
    d
    
    T
    
    a
    
    b
    
    l
    
    e
    
    D
    
    a
    
    t
    
    a
    
    (
    
    )
    """
    def AppendColumn(self):
        """
        AppendColumn -> Integer
            
            int columnsNumber: 
            Input number of columns to append
        """
        pass
    
    
    def AppendRow(self):
        """
        AppendRow -> Integer
            
            int rowsNumber: 
            Input number of rows to append
        """
        pass
    
    
    def DataType(self):
        """
        DataType -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def DeleteColumn(self):
        """
        DeleteColumn -> void
            
            int index: 
            Input starting index of the columns to delete
            
            int columnsNumberToDelete: 
            Input number of columns to delete
        """
        pass
    
    
    def DeleteContent(self):
        """
        DeleteContent -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def DeleteRow(self):
        """
        DeleteRow -> void
            
            int index: 
            Input starting index of the rows to delete
            
            int rowsNumberToDelete: 
            Input number of rows to delete
        """
        pass
    
    
    def GetBlockAttributeValue(self):
        """
        GetBlockAttributeValue -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId attributeDefinitionId: 
            Input object ID of the AttributeDefinition object
        """
        pass
    
    
    def GetBlockTableRecordId(self):
        """
        GetBlockTableRecordId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetCellState(self):
        """
        GetCellState -> CellStates
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetColumnName(self):
        """
        GetColumnName -> string
            
            int index: 
            Input column index
        """
        pass
    
    
    def GetContentTypes(self):
        """
        GetContentTypes -> CellContentTypes
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetCustomData(self):
        """
        GetCustomData -> object
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            string key: 
            Input key to retrieve the custom data
        """
        pass
    
    
    def GetDataFormat(self):
        """
        GetDataFormat -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetDataLink(self):
        """
        GetDataLink() -> ObjectIdCollection
        
        GetDataLink(CellRange) -> ObjectIdCollection
            
            CellRange range: 
            Input range to get the data links. If this is NULL it gets all the data links in the table
        GetDataLink(int, int) -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TableEnumerator
        
        GetEnumerator(TableEnumeratorOption) -> TableEnumerator
            
            TableEnumeratorOption option: 
            Input iterator option.
        """
        pass
    
    
    def GetFieldId(self):
        """
        GetFieldId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetToolTip(self):
        """
        GetToolTip -> string
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue(int, int) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        GetValue(int, int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int content: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption formatOption: 
            Input format option for formatting the cell value. See Remarks for description of each option.
        """
        pass
    
    
    def InsertColumn(self):
        """
        InsertColumn -> Integer
            
            int index: 
            Input index at which to insert the new columns
            
            int columnsNumber: 
            Input number of columns to insert
        """
        pass
    
    
    def InsertRow(self):
        """
        InsertRow -> Integer
            
            int index: 
            Input index at which to insert the new rows.
            
            int rowsNumber: 
            Input number of rows to insert
        """
        pass
    
    
    def IsContentEditable(self):
        """
        IsContentEditable -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsLinked(self):
        """
        IsLinked -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def SetBlockAttributeValue(self):
        """
        SetBlockAttributeValue -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId attributeDefinitionId: 
            Input object ID of the AttributeDefinition object
            
            string value: 
            Input attribute value to set
        """
        pass
    
    
    def SetBlockTableRecordId(self):
        """
        SetBlockTableRecordId -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId value: 
            Input attribute value to set
        """
        pass
    
    
    def SetCellState(self):
        """
        SetCellState -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            CellStates value: 
            Cell state to set. This will replace all the bits of the current state.
        """
        pass
    
    
    def SetColumnName(self):
        """
        SetColumnName -> void
            
            int index: 
            Input zero based index of the column
            
            string name: 
            Input column name to set. This can be an empty string.
        """
        pass
    
    
    def SetCustomData(self):
        """
        SetCustomData -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            string key: 
            Input key to use for the custom data
            
            object value: 
            Input custom data to set. This can be NULL. If it is NULL it deletes the custom data.
        """
        pass
    
    
    def SetDataFormat(self):
        """
        SetDataFormat -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            string format: 
            Input data format to set
        """
        pass
    
    
    def SetDataLink(self):
        """
        SetDataLink(CellRange, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            CellRange range: 
            Range of cells to link to external source.
            
            ObjectId dataLinkId: 
            Id of the data link to set
            
            [MarshalAs(UnmanagedType.U1)] bool bUpdate: 
            Input true if the data link has is to be updated after setting it, false if not
        SetDataLink(int, int, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId dataLinkId: 
            Input id of the data link to set
            
            [MarshalAs(UnmanagedType.U1)] bool bUpdate: 
            Input true if the data link is to be updated after setting it, false if not.
        """
        pass
    
    
    def SetDataType(self):
        """
        SetDataType -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.DataType dataType: 
            Input data type to set
            
            Autodesk.AutoCAD.DatabaseServices.UnitType unitType: 
            Input unit type to set
        """
        pass
    
    
    def SetFieldId(self):
        """
        SetFieldId -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId value: 
            Input field id to set
        """
        pass
    
    
    def SetSize(self):
        """
        SetSize -> void
            
            int numRows: 
            Input new row size.
            
            int numCols: 
            Input new column size.
        """
        pass
    
    
    def SetToolTip(self):
        """
        SetToolTip -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            string value: 
            Input tool tip string to set
        """
        pass
    
    
    def SetValue(self):
        """
        SetValue(int, int, object) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            object value: 
            Input value to set
        SetValue(int, int, int, object, Autodesk.AutoCAD.DatabaseServices.ParseOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int content: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            object value: 
            Input value to set.
            
            Autodesk.AutoCAD.DatabaseServices.ParseOption parseOption: 
            Input parse option. See remarks.
        """
        pass
    
    
    def UnitType(self):
        """
        UnitType -> Autodesk.AutoCAD.DatabaseServices.UnitType
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def UpdateDataLink(self):
        """
        UpdateDataLink(Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Input direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Input option flag
        UpdateDataLink(int, int, Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Input direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Input option flag
        """
        pass
    
    
    NumberOfColumns = None
    
    
    NumberOfRows = None
    
    pass

class LoftOptions(DisposableWrapper, ICloneable):
    """
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    (
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
     
    
    o
    
    p
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    c
    
    o
    
    p
    
    i
    
    e
    
    d
    
     
    
    i
    
    n
    
    t
    
    o
    
     
    
    '
    
    t
    
    h
    
    i
    
    s
    
    '
    """
    def CheckCrossSectionCurves(self):
        """
        CheckCrossSectionCurves -> LoftOptionsCheckCurvesOut
            
            Entity[] crossSectionCurves: 
            Input list of cross-section curves
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def CheckGuideCurves(self):
        """
        CheckGuideCurves -> void
            
            Entity[] guideCurves: 
            Input list of guide curves
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def CheckLoftCurves(self):
        """
        CheckLoftCurves -> LoftOptionsCheckCurvesOut
            
            Entity[] crossSectionCurves: 
            Input list of cross-section curves
            
            Entity[] guideCurves: 
            Input list of guide curves
            
            Entity pPathCurve: 
            Input pointer to path curve or null
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def CheckPathCurve(self):
        """
        CheckPathCurve -> void
            
            Entity pathCurve: 
            Input path curve
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    AlignDirection = None
    
    
    ArcLengthParam = None
    
    
    Closed = None
    
    
    DraftEnd = None
    
    
    DraftEndMag = None
    
    
    DraftStart = None
    
    
    DraftStartMag = None
    
    
    NormalOption = None
    
    
    NoTwist = None
    
    
    Ruled = None
    
    
    Simplify = None
    
    
    VirtualGuide = None
    
    pass

class LoftOptionsBuilder(public class LoftOptionsBuilder):
    """
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    B
    
    u
    
    i
    
    l
    
    d
    
    e
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    B
    
    u
    
    i
    
    l
    
    d
    
    e
    
    r
    
    (
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
    """
    def SetOptionsFromSysvars(self):
        """
        SetOptionsFromSysvars -> void
        
        """
        pass
    
    
    def ToLoftOptions(self):
        """
        ToLoftOptions -> LoftOptions
        
        """
        pass
    
    
    AlignDirection = None
    
    
    ArcLengthParam = None
    
    
    Closed = None
    
    
    DraftEnd = None
    
    
    DraftEndMag = None
    
    
    DraftStart = None
    
    
    DraftStartMag = None
    
    
    NormalOption = None
    
    
    NoTwist = None
    
    
    Ruled = None
    
    
    Simplify = None
    
    
    VirtualGuide = None
    
    pass

class LoftOptionsCheckCurvesOut(public class LoftOptionsCheckCurvesOut):
    """
    
    L
    
    o
    
    f
    
    t
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    C
    
    h
    
    e
    
    c
    
    k
    
    C
    
    u
    
    r
    
    v
    
    e
    
    s
    
    O
    
    u
    
    t
    
    (
    
    )
    """
    AllClosed = None
    
    
    AllOpen = None
    
    
    AllPlanar = None
    
    pass

  NoNormal
  FirstNormal
  LastNormal
  EndsNormal
  AllNormal
  UseDraftAngles

class LoftProfile(Profile3d):
    """
    
    L
    
    o
    
    f
    
    t
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    o
    
    f
    
    t
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    (
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    o
    
    f
    
    t
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    (
    
    L
    
    o
    
    f
    
    t
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    o
    
    f
    
    t
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    (
    
    P
    
    a
    
    t
    
    h
    
    R
    
    e
    
    f
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    L
    
    o
    
    f
    
    t
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    (
    
    )
    """
    def CopyFrom(self):
        """
        CopyFrom(LoftProfile) -> void
        
        CopyFrom(Profile3d) -> void
        
        """
        pass
    
    
    Continuity = None
    
    
    Magnitude = None
    
    pass

class LoftedSurface(Surface):
    """
    
    L
    
    o
    
    f
    
    t
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    )
    """
      LoftSurface
      BlendSurface
      NetworkSurface
    
    
    def CreateLoftedSurface(self):
        """
        CreateLoftedSurface -> void
            
            Entity[] crossSections: 
            Input array of curve entities to be used as cross sections for the lofting operation
            
            Entity[] guideCurves: 
            Input optional array of guide curves
            
            Entity pathCurve: 
            Input path curve
            
            Autodesk.AutoCAD.DatabaseServices.LoftOptions loftOptions: 
            Input loft options
        """
        pass
    
    
    def GetCrossSectionProfile(self):
        """
        GetCrossSectionProfile -> LoftProfile
            
            int idx: 
            Input index of cross section.
        """
        pass
    
    
    def GetGuideProfile(self):
        """
        GetGuideProfile -> LoftProfile
            
            int idx: 
            Input index of guide.
        """
        pass
    
    
    Closed = None
    
    
    CrossSectionProfiles = None
    
    
    CrossSections = None
    
    
    EndCrossSectionContinuity = None
    
    
    EndCrossSectionMagnitude = None
    
    
    EndGuideCurveContinuity = None
    
    
    EndGuideCurveMagnitude = None
    
    
    GuideCurves = None
    
    
    GuideProfiles = None
    
    
    LoftOptions = None
    
    
    NumberOfCrossSections = None
    
    
    NumberOfGuideCurves = None
    
    
    PathEntity = None
    
    
    PathProfile = None
    
    
    StartCrossSectionContinuity = None
    
    
    StartCrossSectionMagnitude = None
    
    
    StartGuideCurveContinuity = None
    
    
    StartGuideCurveMagnitude = None
    
    
    SurfaceType = None
    
    pass

class LongTransaction(DBObject):
    """
    
    L
    
    o
    
    n
    
    g
    
    T
    
    r
    
    a
    
    n
    
    s
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    """
    def AddToWorkSet(self):
        """
        AddToWorkSet -> void
        
        """
        pass
    
    
    def OriginObject(self):
        """
        OriginObject -> ObjectId
        
        """
        pass
    
    
    def RegenWorkSetWithDrawOrder(self):
        """
        RegenWorkSetWithDrawOrder -> void
        
        """
        pass
    
    
    def RemoveFromWorkSet(self):
        """
        RemoveFromWorkSet -> void
        
        """
        pass
    
    
    def SyncWorkSet(self):
        """
        SyncWorkSet -> void
        
        """
        pass
    
    
    def WorkSetHas(self):
        """
        WorkSetHas -> bool
        
        """
        pass
    
    
    ActiveIdMap = None
    
    
    DestinationBlock = None
    
    
    DisallowDrawOrder = None
    
    
    LongTransactionName = None
    
    
    OriginBlock = None
    
    
    Type = None
    
    pass

  SameDb
  XRefDb
  UnrelatedDb

class MInsertBlock(BlockReference):
    """
    
    M
    
    I
    
    n
    
    s
    
    e
    
    r
    
    t
    
    B
    
    l
    
    o
    
    c
    
    k
    
    (
    
    )
    
    (
    
    )
    """
    Columns = None
    
    
    ColumnSpacing = None
    
    
    Rows = None
    
    
    RowSpacing = None
    
    pass

class MLeader(Entity):
    """
    
    M
    
    L
    
    e
    
    a
    
    d
    
    e
    
    r
    
    (
    
    )
    """
    def AddFirstVertex(self):
        """
        AddFirstVertex -> void
            
            int leaderLineIndex: 
            Input index of the leader line.
            
            Point3d point: 
            Input the vertex position.
        """
        pass
    
    
    def AddLastVertex(self):
        """
        AddLastVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
            
            Point3d point: 
            Input the vertex position.
        """
        pass
    
    
    def AddLeader(self):
        """
        AddLeader -> Integer
        
        """
        pass
    
    
    def AddLeaderLine(self):
        """
        AddLeaderLine(Point3d) -> Integer
            
            Point3d point: 
            Input position of the first(head) vertex of the new leader line.
        AddLeaderLine(int) -> Integer
            
            int leaderIndex: 
            Index of the leader cluster.
        """
        pass
    
    
    def ConnectionPoint(self):
        """
        ConnectionPoint(Vector3d) -> Point3d
            
            Vector3d direction: 
            Input the specific direction.
        ConnectionPoint(Vector3d, Autodesk.AutoCAD.DatabaseServices.TextAttachmentDirection) -> Point3d
            
            Vector3d direction: 
            Input the specific direction.
            
            Autodesk.AutoCAD.DatabaseServices.TextAttachmentDirection textAttachmentDirection: 
            Specify if the leader attaches to the MText horizontally or vertically (Horizontally by default).
        """
        pass
    
    
    def GetArrowSymbolId(self):
        """
        GetArrowSymbolId -> ObjectId
            
            int leaderLineIndex: 
            Input the index of the specific leaderline.
        """
        pass
    
    
    def GetBlockAttribute(self):
        """
        GetBlockAttribute -> AttributeReference
            
            ObjectId attDefId: 
            Input attribute definition id.
        """
        pass
    
    
    def GetContentGeomExtents(self):
        """
        GetContentGeomExtents -> Extents3d
        
        """
        pass
    
    
    def getContextDataManager(self):
        """
        getContextDataManager -> IntPtr
        
        """
        pass
    
    
    def GetDogleg(self):
        """
        GetDogleg -> Vector3d
            
            int leaderIndex: 
            Input leader index.
        """
        pass
    
    
    def GetDoglegLength(self):
        """
        GetDoglegLength -> double
            
            int leaderIndex: 
            Input leader index
        """
        pass
    
    
    def GetFirstVertex(self):
        """
        GetFirstVertex -> Point3d
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def MoveMLeader(self):
        """
        MoveMLeader -> void
            
            Vector3d vec: 
            Input vector indicate direction and distance the MLeader will be moved.
            
            Autodesk.AutoCAD.DatabaseServices.MoveType type: 
            Input MoveType indicate how the MLeader will be moved.
        """
        pass
    
    
    def GetLastVertex(self):
        """
        GetLastVertex -> Point3d
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def GetLeaderIndex(self):
        """
        GetLeaderIndex -> Integer
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def GetLeaderIndexes(self):
        """
        GetLeaderIndexes -> ArrayList
        
        """
        pass
    
    
    def GetLeaderLineIndexes(self):
        """
        GetLeaderLineIndexes -> ArrayList
            
            int leaderIndex: 
            Input leader index.
        """
        pass
    
    
    def getOverridedMLeaderStyle(self):
        """
        getOverridedMLeaderStyle -> void
            
            MLeaderStyle: 
            Input a reference of MLeaderStyle, MLeader object will set its properties to this object.
        """
        pass
    
    
    def GetPlane(self):
        """
        GetPlane -> Plane
        
        """
        pass
    
    
    def GetVertex(self):
        """
        GetVertex -> Point3d
            
            int leaderLineIndex: 
            Input leader line index.
            
            int index: 
            Input index of the vertex.
        """
        pass
    
    
    def HasContent(self):
        """
        HasContent -> bool
        
        """
        pass
    
    
    def PostMLeaderToDb(self):
        """
        PostMLeaderToDb -> void
            
            Database db: 
            Input database into which the current MLeader object should be added.
        """
        pass
    
    
    def recomputeBreakPoints(self):
        """
        recomputeBreakPoints -> void
        
        """
        pass
    
    
    def RemoveFirstVertex(self):
        """
        RemoveFirstVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def RemoveLastVertex(self):
        """
        RemoveLastVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def RemoveLeader(self):
        """
        RemoveLeader -> void
            
            int index: 
            Input the index of the leader to be removed.
        """
        pass
    
    
    def RemoveLeaderLine(self):
        """
        RemoveLeaderLine -> void
            
            int leaderLineIndex: 
            Input the index of leader cluster.
        """
        pass
    
    
    def SetArrowSymbolId(self):
        """
        SetArrowSymbolId -> void
            
            int leaderLineIndex: 
            Input the index of the specific leaderline.
            
            ObjectId id: 
            Input the object id of the arrow head symbol.
        """
        pass
    
    
    def SetBlockAttribute(self):
        """
        SetBlockAttribute -> void
            
            ObjectId attDefId: 
            Input attribute definition id.
            
            AttributeReference attributeValue: 
            Input attribute value.
        """
        pass
    
    
    def SetContextDataManager(self):
        """
        SetContextDataManager -> void
            
            IntPtr contextDataManager: 
            Input the pointer of context data manager.
        """
        pass
    
    
    def SetDogleg(self):
        """
        SetDogleg -> void
            
            int leaderIndex: 
            Input leader index.
            
            Vector3d vector: 
            Input the vector represents the new length and new direction of dog-leg.
        """
        pass
    
    
    def SetDoglegLength(self):
        """
        SetDoglegLength -> void
            
            int leaderIndex: 
            Input leader index
            
            double doglegLength: 
            Input the length of dog-leg leader line
        """
        pass
    
    
    def SetFirstVertex(self):
        """
        SetFirstVertex -> void
            
            int leaderLineIndex: 
            Input the leader line index.
            
            Point3d point: 
            Input the point where the new leader head is on.
        """
        pass
    
    
    def SetLastVertex(self):
        """
        SetLastVertex -> void
            
            int leaderLineIndex: 
            Input the leader line index.
            
            Point3d point: 
            Input the point where the new leader tail is on.
        """
        pass
    
    
    def SetPlane(self):
        """
        SetPlane -> void
            
            Plane value: 
            Input desired plane within which the MLeader will reside.
        """
        pass
    
    
    def SetVertex(self):
        """
        SetVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
            
            int index: 
            Input the index of vertex.
            
            Point3d point: 
            Input the new position of this vertex.
        """
        pass
    
    
    def VerticesCount(self):
        """
        VerticesCount -> Integer
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def GetTextAttachmentType(self):
        """
        GetTextAttachmentType -> Autodesk.AutoCAD.DatabaseServices.TextAttachmentType
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction type
        """
        pass
    
    
    def SetTextAttachmentType(self):
        """
        SetTextAttachmentType -> void
            
            Autodesk.AutoCAD.DatabaseServices.TextAttachmentType textAttachmentType: 
            Input text attachment type
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction types
        """
        pass
    
    
    ArrowSize = None
    
    
    ArrowSymbolId = None
    
    
    BlockColor = None
    
    
    BlockConnectionType = None
    
    
    BlockContentId = None
    
    
    BlockPosition = None
    
    
    BlockRotation = None
    
    
    BlockScale = None
    
    
    ContentType = None
    
    
    DoglegLength = None
    
    
    EnableAnnotationScale = None
    
    
    EnableDogleg = None
    
    
    EnableFrameText = None
    
    
    EnableLanding = None
    
    
    ExtendLeaderToText = None
    
    
    LandingGap = None
    
    
    LeaderCount = None
    
    
    LeaderLineColor = None
    
    
    LeaderLineCount = None
    
    
    LeaderLineType = None
    
    
    LeaderLineTypeId = None
    
    
    LeaderLineWeight = None
    
    
    MLeaderStyle = None
    
    
    MText = None
    
    
    Normal = None
    
    
    Scale = None
    
    
    TextAlignmentType = None
    
    
    TextAngleType = None
    
    
    TextAttachmentDirection = None
    
    
    TextAttachmentType = None
    
    
    TextColor = None
    
    
    TextHeight = None
    
    
    TextLocation = None
    
    
    TextStyleId = None
    
    
    ToleranceLocation = None
    
    pass

class MLeaderStyle(DBObject):
    """
    
    M
    
    L
    
    e
    
    a
    
    d
    
    e
    
    r
    
    S
    
    t
    
    y
    
    l
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    M
    
    L
    
    e
    
    a
    
    d
    
    e
    
    r
    
    S
    
    t
    
    y
    
    l
    
    e
    
    (
    
    M
    
    L
    
    e
    
    a
    
    d
    
    e
    
    r
    
    S
    
    t
    
    y
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    L
    
    e
    
    a
    
    d
    
    e
    
    r
    
    S
    
    t
    
    y
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
    .
    """
    def OverwritePropChanged(self):
        """
        OverwritePropChanged -> bool
        
        """
        pass
    
    
    def PostMLeaderStyleToDb(self):
        """
        PostMLeaderStyleToDb -> ObjectId
        
        """
        pass
    
    
    def GetTextAttachmentType(self):
        """
        GetTextAttachmentType -> Autodesk.AutoCAD.DatabaseServices.TextAttachmentType
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction type
        """
        pass
    
    
    def SetTextAttachmentType(self):
        """
        SetTextAttachmentType -> void
            
            Autodesk.AutoCAD.DatabaseServices.TextAttachmentType textAttachmentType: 
            Input text attachment type
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction types
        """
        pass
    
    
    ArrowSize = None
    
    
    ArrowSymbolId = None
    
    
    BlockColor = None
    
    
    BlockConnectionType = None
    
    
    BlockId = None
    
    
    BlockRotation = None
    
    
    BlockScale = None
    
    
    BreakSize = None
    
    
    ContentType = None
    
    
    DefaultMText = None
    
    
    DoglegLength = None
    
    
    DrawLeaderOrderType = None
    
    
    DrawMLeaderOrderType = None
    
    
    EnableBlockRotation = None
    
    
    EnableBlockScale = None
    
    
    EnableDogleg = None
    
    
    EnableFrameText = None
    
    
    EnableLanding = None
    
    
    ExtendLeaderToText = None
    
    
    FirstSegmentAngleConstraint = None
    
    
    LandingGap = None
    
    
    LeaderLineColor = None
    
    
    LeaderLineType = None
    
    
    LeaderLineTypeId = None
    
    
    LeaderLineWeight = None
    
    
    MaxLeaderSegmentsPoints = None
    
    
    Name = None
    
    
    Scale = None
    
    
    SecondSegmentAngleConstraint = None
    
    
    TextAlignAlwaysLeft = None
    
    
    TextAlignmentType = None
    
    
    TextAngleType = None
    
    
    TextAttachmentDirection = None
    
    
    TextAttachmentType = None
    
    
    TextColor = None
    
    
    TextHeight = None
    
    
    TextStyleId = None
    
    pass

class MText(Entity):
    """
    
    M
    
    T
    
    e
    
    x
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    :
    
     
    
    (
    
    0
    
    .
    
    0
    
    ,
    
    0
    
    .
    
    0
    
    ,
    
    1
    
    .
    
    0
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    (
    
    1
    
    .
    
    0
    
    ,
    
    0
    
    .
    
    0
    
    ,
    
    0
    
    .
    
    0
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    w
    
    i
    
    d
    
    t
    
    h
    
     
    
    :
    
     
    
    0
    
    .
    
    0
    
    
    
    
     
    
     
    
     
    
     
    
    t
    
    e
    
    x
    
    t
    
    S
    
    t
    
    y
    
    l
    
    e
    
     
    
    :
    
     
    
    N
    
    U
    
    L
    
    L
    
    
    
    
     
    
     
    
     
    
     
    
    t
    
    e
    
    x
    
    t
    
    H
    
    e
    
    i
    
    g
    
    h
    
    t
    
     
    
    :
    
     
    
    0
    
    .
    
    0
    
    
    
    
     
    
     
    
     
    
     
    
    a
    
    t
    
    t
    
    a
    
    c
    
    h
    
    m
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    A
    
    c
    
    D
    
    b
    
    M
    
    T
    
    e
    
    x
    
    t
    
    :
    
    :
    
    k
    
    T
    
    o
    
    p
    
    L
    
    e
    
    f
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    f
    
    l
    
    o
    
    w
    
    D
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    A
    
    c
    
    D
    
    b
    
    M
    
    T
    
    e
    
    x
    
    t
    
    :
    
    :
    
    k
    
    B
    
    y
    
    S
    
    t
    
    y
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    c
    
    o
    
    n
    
    t
    
    e
    
    n
    
    t
    
    s
    
     
    
    :
    
     
    
    N
    
    U
    
    L
    
    L
    """
    def ConvertFieldToText(self):
        """
        ConvertFieldToText -> void
        
        """
        pass
    
    
    def CorrectSpelling(self):
        """
        CorrectSpelling -> Integer
        
        """
        pass
    
    
    def ExplodeFragments(self):
        """
        ExplodeFragments(MTextFragmentCallback) -> void
            
            MTextFragmentCallback enumerator: 
            Input fragment elaboration callback function
        ExplodeFragments(MTextFragmentCallback, object) -> void
            
            MTextFragmentCallback enumerator: 
            Input fragment elaboration callback function
            
            object userData: 
            Input user data
        ExplodeFragments(MTextFragmentCallback, object, WorldDraw) -> void
            
            MTextFragmentCallback enumerator: 
            Input fragment elaboration callback function
            
            object userData: 
            Input user data
            
            WorldDraw context: 
            Input WorldDraw object
        """
        pass
    
    
    def GetBoundingPoints(self):
        """
        GetBoundingPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetColumnHeight(self):
        """
        GetColumnHeight -> double
            
            int index: 
            The column's height to get
        """
        pass
    
    
    def SetColumnHeight(self):
        """
        SetColumnHeight -> void
            
            int index: 
            The column's height to set
            
            double height: 
            Column height
        """
        pass
    
    
    def SetContentsRtf(self):
        """
        SetContentsRtf -> Integer
            
            string value: 
            Input RTF-encoded string
        """
        pass
    
    
    def SetDynamicColumns(self):
        """
        SetDynamicColumns -> void
            
            double width: 
            Input new column width
            
            double gutter: 
            Input new column gutter
            
            [MarshalAs(UnmanagedType.U1)] bool auto_height: 
            Input new auto-height setting
        """
        pass
    
    
    def SetStaticColumns(self):
        """
        SetStaticColumns -> void
            
            double width: 
            Input new column width
            
            double gutter: 
            Input new column gutter
            
            int count: 
            Input new auto-height setting
        """
        pass
    
    
    def SetAttachmentMovingLocation(self):
        """
        SetAttachmentMovingLocation -> void
            
            Autodesk.AutoCAD.DatabaseServices.AttachmentPoint value: 
            Input desired AttachmentPoint type value
        """
        pass
    
    
    ActualHeight = None
    
    
    ActualWidth = None
    
    
    AlignChange = None
    
    
    Ascent = None
    
    
    Attachment = None
    
    
    BackgroundFill = None
    
    
    BackgroundFillColor = None
    
    
    BackgroundScaleFactor = None
    
    
    BackgroundTransparency = None
    
    
    BlockBegin = None
    
    
    BlockEnd = None
    
    
    ColorChange = None
    
    
    ColumnAutoHeight = None
    
    
    ColumnCount = None
    
    
    ColumnFlowReversed = None
    
    
    ColumnGutterWidth = None
    
    
    ColumnType = None
    
    
    ColumnWidth = None
    
    
    Contents = None
    
    
    ContentsRTF = None
    
    
    Descent = None
    
    
    Direction = None
    
    
    FlowDirection = None
    
    
    FontChange = None
    
    
    Height = None
    
    
    HeightChange = None
    
    
    LineBreak = None
    
    
    LineSpaceDistance = None
    
    
    LineSpacingFactor = None
    
    
    LineSpacingStyle = None
    
    
    Location = None
    
    
    NonBreakSpace = None
    
    
    Normal = None
    
    
    ObliqueChange = None
    
    
    OverlineOff = None
    
    
    OverlineOn = None
    
    
    ParagraphBreak = None
    
    
    Rotation = None
    
    
    ShowBorders = None
    
    
    StackStart = None
    
    
    StrikethroughOff = None
    
    
    StrikethroughOn = None
    
    
    Text = None
    
    
    TextHeight = None
    
    
    TextStyleId = None
    
    
    TextStyleName = None
    
    
    TrackChange = None
    
    
    UnderlineOff = None
    
    
    UnderlineOn = None
    
    
    UseBackgroundColor = None
    
    
    Width = None
    
    
    WidthChange = None
    
    pass

class MTextFragment(DisposableWrapper):
    """
    
    """
    def GetOverLinePoints(self):
        """
        GetOverLinePoints -> Point3d()
        
        """
        pass
    
    
    def GetStrikethroughPoints(self):
        """
        GetStrikethroughPoints -> Point3d()
        
        """
        pass
    
    
    def GetUnderLinePoints(self):
        """
        GetUnderLinePoints -> Point3d()
        
        """
        pass
    
    
    BigFont = None
    
    
    Bold = None
    
    
    CapsHeight = None
    
    
    Color = None
    
    
    Direction = None
    
    
    Extents = None
    
    
    Italic = None
    
    
    Location = None
    
    
    Normal = None
    
    
    ObliqueAngle = None
    
    
    Overlined = None
    
    
    ShxFont = None
    
    
    StackBottom = None
    
    
    StackTop = None
    
    
    Strikethrough = None
    
    
    Text = None
    
    
    TrackingFactor = None
    
    
    TrueTypeFont = None
    
    
    Underlined = None
    
    
    WidthFactor = None
    
    pass

  Terminate
  Continue

Release0 = 0
Release1 = 1
Release10 = 10
Release100 = 100
Release101 = 0x65
Release102 = 0x66
Release103 = 0x67
Release104 = 0x68
Release105 = 0x69
Release106 = 0x6a
Release107 = 0x6b
Release108 = 0x6c
Release109 = 0x6d
Release11 = 11
Release110 = 110
Release111 = 0x6f
Release112 = 0x70
Release113 = 0x71
Release114 = 0x72
Release115 = 0x73
Release116 = 0x74
Release117 = 0x75
Release118 = 0x76
Release119 = 0x77
Release12 = 12
Release120 = 120
Release121 = 0x79
Release122 = 0x7a
Release123 = 0x7b
Release124 = 0x7c
Release125 = 0x7d
Release126 = 0x7e
Release127 = 0x7f
Release128 = 0x80
Release129 = 0x81
Release13 = 13
Release130 = 130
Release131 = 0x83
Release132 = 0x84
Release133 = 0x85
Release134 = 0x86
Release135 = 0x87
Release136 = 0x88
Release137 = 0x89
Release138 = 0x8a
Release139 = 0x8b
Release14 = 14
Release140 = 140
Release141 = 0x8d
Release142 = 0x8e
Release143 = 0x8f
Release144 = 0x90
Release145 = 0x91
Release146 = 0x92
Release147 = 0x93
Release148 = 0x94
Release149 = 0x95
Release15 = 15
Release150 = 150
Release151 = 0x97
Release152 = 0x98
Release153 = 0x99
Release154 = 0x9a
Release155 = 0x9b
Release156 = 0x9c
Release157 = 0x9d
Release158 = 0x9e
Release159 = 0x9f
Release16 = 0x10
Release160 = 160
Release17 = 0x11
Release18 = 0x12
Release19 = 0x13
Release2 = 2
Release20 = 20
Release2010Max = 0xff
Release2010Newest = 0xe1
Release21 = 0x15
Release22 = 0x16
Release23 = 0x17
Release24 = 0x18
Release25 = 0x19
Release26 = 0x1a
Release27 = 0x1b
Release28 = 0x1c
Release29 = 0x1d
Release3 = 3
Release30 = 30
Release31 = 0x1f
Release32 = 0x20
Release33 = 0x21
Release34 = 0x22
Release35 = 0x23
Release36 = 0x24
Release37 = 0x25
Release38 = 0x26
Release39 = 0x27
Release4 = 4
Release40 = 40
Release41 = 0x29
Release42 = 0x2a
Release43 = 0x2b
Release44 = 0x2c
Release45 = 0x2d
Release46 = 0x2e
Release47 = 0x2f
Release48 = 0x30
Release49 = 0x31
Release5 = 5
Release50 = 50
Release51 = 0x33
Release52 = 0x34
Release53 = 0x35
Release54 = 0x36
Release55 = 0x37
Release56 = 0x38
Release57 = 0x39
Release58 = 0x3a
Release59 = 0x3b
Release6 = 6
Release60 = 60
Release61 = 0x3d
Release62 = 0x3e
Release63 = 0x3f
Release64 = 0x40
Release65 = 0x41
Release66 = 0x42
Release67 = 0x43
Release68 = 0x44
Release69 = 0x45
Release7 = 7
Release70 = 70
Release71 = 0x47
Release72 = 0x48
Release73 = 0x49
Release74 = 0x4a
Release75 = 0x4b
Release76 = 0x4c
Release77 = 0x4d
Release78 = 0x4e
Release79 = 0x4f
Release8 = 8
Release80 = 80
Release81 = 0x51
Release82 = 0x52
Release83 = 0x53
Release84 = 0x54
Release85 = 0x55
Release86 = 0x56
Release87 = 0x57
Release88 = 0x58
Release89 = 0x59
Release9 = 9
Release90 = 90
Release91 = 0x5b
Release92 = 0x5c
Release93 = 0x5d
Release94 = 0x5e
Release95 = 0x5f
Release96 = 0x60
Release97 = 0x61
Release98 = 0x62
Release99 = 0x63
ReleaseCheckExtended = 0x7d
ReleaseCurrent = 0x7d
ReleaseExtendedCurrent = 1
ReleaseExtendedNewest = 1
ReleaseMax = 0x7f
ReleaseNewest = 0x7d
ReleaseUnknown = 0x7e

class MatchProperties(RXObject):
    """
    
    """
    def CopyProperties(self):
        """
        CopyProperties -> void
            
            Entity sourceEntity: 
            Input entity from which properties will be copied
            
            Entity targetEntity: 
            Input entity to which properties will be copied
            
            int flag: 
            Input bit flags indicating which properties to copy
        """
        pass
    
    pass

class Material(DBObject):
    """
    
    M
    
    a
    
    t
    
    e
    
    r
    
    i
    
    a
    
    l
    
    (
    
    )
    """
    Ambient = None
    
    
    Anonymous = None
    
    
    Bump = None
    
    
    ChannelFlags = None
    
    
    ColorBleedScale = None
    
    
    Description = None
    
    
    Diffuse = None
    
    
    FinalGather = None
    
    
    GlobalIllumination = None
    
    
    IlluminationModel = None
    
    
    IndirectBumpScale = None
    
    
    Luminance = None
    
    
    LuminanceMode = None
    
    
    Mode = None
    
    
    Name = None
    
    
    NormalMap = None
    
    
    Opacity = None
    
    
    ReflectanceScale = None
    
    
    Reflection = None
    
    
    Reflectivity = None
    
    
    Refraction = None
    
    
    SelfIllumination = None
    
    
    Specular = None
    
    
    Translucence = None
    
    
    TransmittanceScale = None
    
    
    TwoSided = None
    
    pass

  English
  Metric

  ConvertDuplicatesToOverrrides = 4
  CopyDuplicates = 1
  IgnoreNewStyles = 8
  None = 0
  OverwriteDuplicates = 2

class MeshDataCollection(public struct MeshDataCollection {
}):
    """
    
    M
    
    e
    
    s
    
    h
    
    D
    
    a
    
    t
    
    a
    
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
    
    (
    
    )
    """
    ColorArray = None
    
    
    FaceArray = None
    
    
    MaterialIdArray = None
    
    
    VertexArray = None
    
    pass

class MeshFaceterData(public struct MeshFaceterData {
}):
    """
    
    M
    
    e
    
    s
    
    h
    
    F
    
    a
    
    c
    
    e
    
    t
    
    e
    
    r
    
    D
    
    a
    
    t
    
    a
    
    (
    
    )
    """
    FaceterDevNormal = None
    
    
    FaceterDevSurface = None
    
    
    FaceterGridRatio = None
    
    
    FaceterMaxEdgeLength = None
    
    
    FaceterMaxGrid = None
    
    
    FaceterMeshType = None
    
    
    FaceterMinUGrid = None
    
    
    FaceterMinVGrid = None
    
    pass

class MeshPointMaps(public struct MeshPointMaps {
}):
    """
    
    M
    
    e
    
    s
    
    h
    
    P
    
    o
    
    i
    
    n
    
    t
    
    M
    
    a
    
    p
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    P
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
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
    
     
    
    d
    
    e
    
    s
    
    t
    
    P
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    e
    
    s
    
    t
    
    i
    
    n
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    """
    DestPonints = None
    
    
    SourcePonints = None
    
    pass

class MidPointConstraint(GeometricalConstraint):
    """
    
    M
    
    i
    
    d
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class Mline(Entity):
    """
    
    M
    
    l
    
    i
    
    n
    
    e
    
    (
    
    )
    """
    def AppendSegment(self):
        """
        AppendSegment -> void
            
            Point3d newVertex: 
            Input new vertex point (in WCS) to be added
        """
        pass
    
    
    def Element(self):
        """
        Element -> Integer
            
            Point3d pt: 
            Input search point
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Point3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input point to find nearest point to
            
            Vector3d normal: 
            Input direction of projection
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input Boolean indicating if search should include "virtual" extension of Mline
            
            [MarshalAs(UnmanagedType.U1)] bool excludeCaps: 
            Input Boolean indicating if endcaps should not be included in nearest point search
        GetClosestPointTo(Point3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input point to find nearest point to
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input Boolean indicating if search should include "virtual" extension of Mline
            
            [MarshalAs(UnmanagedType.U1)] bool excludeCaps: 
            Input Boolean indicating if endcaps should not be included in nearest point search
        """
        pass
    
    
    def MoveVertexAt(self):
        """
        MoveVertexAt -> void
            
            int index: 
            Input index of vertex to move in the vertex array
            
            Point3d newPosition: 
            Input new vertex value
        """
        pass
    
    
    def RemoveLastSegment(self):
        """
        RemoveLastSegment -> void
            
            Point3d lastVertex: 
            Returns filled in with the value of the vertex that becomes last when current last is removed
        """
        pass
    
    
    def VertexAt(self):
        """
        VertexAt -> Point3d
            
            int index: 
            Returns the value of the vertex at the index location (0 based) in the MLine object's vertex array.
        """
        pass
    
    
    IsClosed = None
    
    
    Justification = None
    
    
    Normal = None
    
    
    NumberOfVertices = None
    
    
    Scale = None
    
    
    Style = None
    
    
    SupressEndCaps = None
    
    
    SupressStartCaps = None
    
    pass

  Top
  Zero
  Bottom

class MlineStyle(DBObject):
    """
    
    M
    
    l
    
    i
    
    n
    
    e
    
    S
    
    t
    
    y
    
    l
    
    e
    
    (
    
    )
    """
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            MlineStyle source: 
            Input MlineStyle to copy from
            
            [MarshalAs(UnmanagedType.U1)] bool checkIfReferenced: 
            Input Boolean indicating whether to check if the style is referenced
        """
        pass
    
    
    Description = None
    
    
    Elements = None
    
    
    EndAngle = None
    
    
    EndInnerArcs = None
    
    
    EndRoundCap = None
    
    
    EndSquareCap = None
    
    
    FillColor = None
    
    
    Filled = None
    
    
    Name = None
    
    
    ShowMiters = None
    
    
    StartAngle = None
    
    
    StartInnerArcs = None
    
    
    StartRoundCap = None
    
    
    StartSquareCap = None
    
    pass

class MlineStyleElement(public struct MlineStyleElement {
}):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture specific format.
        """
        pass
    
    
    Color = None
    
    
    LinetypeId = None
    
    
    Offset = None
    
    pass

class MlineStyleElementCollection(ICollection):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            MlineStyleElement element: 
            Input element to add
            
            [MarshalAs(UnmanagedType.U1)] bool checkIfReferenced: 
            Input Boolean indicating whether to check if the style is referenced
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MlineStyleElement[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> MlineStyleElementCollectionEnumerator
        
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of item to remove
        """
        pass
    
    
    Count = None
    
    pass

class MlineStyleElementCollectionEnumerator(IEnumerator):
    """
    
    M
    
    l
    
    i
    
    n
    
    e
    
    S
    
    t
    
    y
    
    l
    
    e
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
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
    
    E
    
    n
    
    u
    
    m
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    l
    
    i
    
    n
    
    e
    
    S
    
    t
    
    y
    
    l
    
    e
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
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
    
     
    
    c
    
    o
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    o
    
     
    
    g
    
    e
    
    n
    
    e
    
    r
    
    a
    
    t
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
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
    
    
    Current = None
    
    pass

  AlignmentLeft
  AlignmentCenter
  AlignmentRight

  AboveView
  BelowView

  Full
  RegionsOnly
  ObjectsOnly

  MoveAllPoints
  MoveAllExceptArrowHeaderPoints
  MoveContentAndDoglegPoints

class MultiModesGripPE(RXObject):
    """
    
    M
    
    u
    
    l
    
    t
    
    i
    
    M
    
    o
    
    d
    
    e
    
    s
    
    G
    
    r
    
    i
    
    p
    
    P
    
    E
    
    (
    
    )
    """
      Primary
      Secondary
    
    
    def CurrentMode(self):
        """
        CurrentMode -> Autodesk.AutoCAD.DatabaseServices.GripMode
            
            Entity entity: 
            The Entity whose current mode is requested.
            
            GripData gripData: 
            The grip whose mode is requested.
        """
        pass
    
    
    def CurrentModeId(self):
        """
        CurrentModeId -> UInteger
            
            Entity entity: 
            The Entity whose current mode id is requested.
            
            GripData gripData: 
            The grip whose mode id is requested.
        """
        pass
    
    
    def GetGripModes(self):
        """
        GetGripModes -> bool
            
            Entity entity: 
            The Entity whose modes are requested. The object needs to be open at least for read.
            
            GripData gripData: 
            The grip whose modes are requested.
            
            GripModeCollection modes: 
            The returned collection of available modes.
            
            ref uint curMode: 
            The returned identifier of current mode.
        """
        pass
    
    
    def GetGripType(self):
        """
        GetGripType -> GripType
            
            Entity entity: 
            The Entity whose grip type is requested.
            
            GripData gripData: 
            The grip whose grip type is requested.
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
            
            Entity entity: 
            The Entity whose current mode is reset to default.
        """
        pass
    
    
    def SetCurrentMode(self):
        """
        SetCurrentMode -> bool
            
            Entity entity: 
            The Entity whose current mode is to be set current.
            
            GripData gripData: 
            The grip whose current mode is to be set current.
            
            uint curMode: 
            The numerical identifier for the new current mode.
        """
        pass
    
    pass

  NoNewLayerNotification = 0
  NotifyOnInsert = 0x20
  NotifyOnLayerStateRestore = 8
  NotifyOnOpen = 2
  NotifyOnPlot = 1
  NotifyOnSave = 0x10
  NotifyOnXrefAttachAndReload = 4

class NormalConstraint(GeometricalConstraint):
    """
    
    N
    
    o
    
    r
    
    m
    
    a
    
    l
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class Notifier(INotifyPropertyChanged):
    """
    
    """
    def OnPropertyChanged(self):
        """
        OnPropertyChanged -> void
        
        """
        pass
    
    pass

class NurbSurface(Autodesk.AutoCAD.DatabaseServices.Surface):
    """
    
    N
    
    u
    
    r
    
    b
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    N
    
    u
    
    r
    
    b
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
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
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
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
    
    ,
    
     
    
    K
    
    n
    
    o
    
    t
    
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
    
    ,
    
     
    
    K
    
    n
    
    o
    
    t
    
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
    
    )
    
    (
    
    )
    """
    def Evaluate(self):
        """
        Evaluate(double, double) -> Point3d
        
        Evaluate(double, double, Point3d, Vector3d, Vector3d) -> void
        
        Evaluate(double, double, Point3d, Vector3d, Vector3d, Vector3d, Vector3d, Vector3d) -> void
        
        Evaluate(double, double, int, Point3d, Vector3dCollection) -> void
        
        """
        pass
    
    
    def GetControlPointAt(self):
        """
        GetControlPointAt -> Point3d
        
        """
        pass
    
    
    def GetIsolineAtU(self):
        """
        GetIsolineAtU -> Curve()
        
        """
        pass
    
    
    def GetIsolineAtV(self):
        """
        GetIsolineAtV -> Curve()
        
        """
        pass
    
    
    def GetNormal(self):
        """
        GetNormal -> Vector3d
        
        """
        pass
    
    
    def GetParameterOfPoint(self):
        """
        GetParameterOfPoint -> void
        
        """
        pass
    
    
    def GetWeight(self):
        """
        GetWeight -> double
        
        """
        pass
    
    
    def InsertControlPointsAtU(self):
        """
        InsertControlPointsAtU -> void
        
        """
        pass
    
    
    def InsertControlPointsAtV(self):
        """
        InsertControlPointsAtV -> void
        
        """
        pass
    
    
    def InsertKnotAtU(self):
        """
        InsertKnotAtU -> void
        
        """
        pass
    
    
    def InsertKnotAtV(self):
        """
        InsertKnotAtV -> void
        
        """
        pass
    
    
    def IsPlanar(self):
        """
        IsPlanar -> bool
        
        """
        pass
    
    
    def IsPointOnSurface(self):
        """
        IsPointOnSurface -> bool
        
        """
        pass
    
    
    def ModifyPosition(self):
        """
        ModifyPosition -> void
        
        """
        pass
    
    
    def ModifyPositionAndTangent(self):
        """
        ModifyPositionAndTangent -> void
        
        """
        pass
    
    
    def Rebuild(self):
        """
        Rebuild(int, int, int, int) -> void
        
        Rebuild(int, int, int, int, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def RemoveControlPointsAtU(self):
        """
        RemoveControlPointsAtU -> void
        
        """
        pass
    
    
    def RemoveControlPointsAtV(self):
        """
        RemoveControlPointsAtV -> void
        
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
        
        """
        pass
    
    
    def SetControlPointAt(self):
        """
        SetControlPointAt -> void
        
        """
        pass
    
    
    def SetControlPoints(self):
        """
        SetControlPoints -> void
        
        """
        pass
    
    
    def SetWeight(self):
        """
        SetWeight -> void
        
        """
        pass
    
    
    ControlPoints = None
    
    
    DegreeInU = None
    
    
    DegreeInV = None
    
    
    IsClosedInU = None
    
    
    IsClosedInV = None
    
    
    IsPeriodicInU = None
    
    
    IsPeriodicInV = None
    
    
    IsRational = None
    
    
    NumberOfControlPointsInU = None
    
    
    NumberOfControlPointsInV = None
    
    
    NumberOfKnotsInU = None
    
    
    NumberOfKnotsInV = None
    
    
    NumberOfSpansInU = None
    
    
    NumberOfSpansInV = None
    
    
    PeriodInU = None
    
    
    PeriodInV = None
    
    
    UKnots = None
    
    
    VKnots = None
    
    pass

class NurbsData(public struct NurbsData {
}):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to check against.
        """
        pass
    
    
    def GetControlPoints(self):
        """
        GetControlPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetKnots(self):
        """
        GetKnots -> DoubleCollection
        
        """
        pass
    
    
    def GetWeights(self):
        """
        GetWeights -> DoubleCollection
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(NurbsData) -> bool
            
            NurbsData other: 
            Object to check against.
        IsEqualTo(NurbsData, Tolerance) -> bool
            
            NurbsData other: 
            Object to check against.
            
            Tolerance tolerance: 
            Tolerance range
        """
        pass
    
    
    Closed = None
    
    
    ControlPointTolerance = None
    
    
    Degree = None
    
    
    KnotTolerance = None
    
    
    Periodic = None
    
    
    Rational = None
    
    pass

class ObjectContext(RXObject):
    """
    
    """
    CollectionName = None
    
    
    Name = None
    
    
    UniqueIdentifier = None
    
    pass

class ObjectContextCollection(RXObject, IEnumerable):
    """
    
    """
    def AddContext(self):
        """
        AddContext -> void
            
            ObjectContext ctxt: 
            The context to copy and add to the collection.
        """
        pass
    
    
    def GetContext(self):
        """
        GetContext -> ObjectContext
            
            string contextName: 
            The name of the context to copy and return.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> ObjectContextCollectionEnumerator
        
        """
        pass
    
    
    def HasContext(self):
        """
        HasContext -> bool
            
            string contextName: 
            The name of the context to find.
        """
        pass
    
    
    def RemoveContext(self):
        """
        RemoveContext -> void
            
            string contextName: 
            The name of the context to remove from the collection.
        """
        pass
    
    
    CurrentContext = None
    
    
    Name = None
    
    pass

class ObjectContextCollectionEnumerator(RXObject, IEnumerator):
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
    
    
    Current = None
    
    pass

class ObjectContextManager(RXObject):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    C
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
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
    def GetContextCollection(self):
        """
        GetContextCollection -> ObjectContextCollection
            
            string collectionName: 
            The name of the desired collection.
        """
        pass
    
    
    def RegisterContextCollection(self):
        """
        RegisterContextCollection -> void
            
            string collectionName: 
            The name of the collection to register with the manager.
            
            ObjectContextCollection collection: 
            The collection to register with the manager.
        """
        pass
    
    
    def UnregisterContextCollection(self):
        """
        UnregisterContextCollection -> void
            
            string collectionName: 
            The name of the collection to unregister with the manager.
        """
        pass
    
    pass

class ObjectErasedEventArgs(EventArgs):
    """
    
    """
    DBObject = None
    
    
    Erased = None
    
    pass

class ObjectEventArgs(EventArgs):
    """
    
    """
    DBObject = None
    
    pass

class ObjectId(IComparable<ObjectId>, IDynamicMetaObjectProvider {
}):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    n
    
    t
    
    P
    
    t
    
    r
    
     
    
    o
    
    l
    
    d
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
     
    
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
    
     
    
    f
    
    r
    
    o
    
    m
    """
    def Compare(self):
        """
        Compare -> bool
            
            ObjectId value1: 
            Input object to compare against
        """
        pass
    
    
    def ConvertToRedirectedId(self):
        """
        ConvertToRedirectedId -> ObjectId
        
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
    
    
    def GetMetaObject(self):
        """
        GetMetaObject -> DynamicMetaObject
        
        """
        pass
    
    
    Database = None
    
    
    Handle = None
    
    
    IsEffectivelyErased = None
    
    
    IsErased = None
    
    
    IsNull = None
    
    
    IsResident = None
    
    
    IsValid = None
    
    
    NonForwardedHandle = None
    
    
    Null = None
    
    
    ObjectClass = None
    
    
    OldIdPtr = None
    
    
    OriginalDatabase = None
    
    
    IsWellBehaved = None
    
    
    OldId = None
    
    pass

class ObjectIdCollection(DisposableWrapper, IList):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
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
    
    (
    
    )
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> Integer
            
            ObjectId value: 
            Item to add
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
            Item to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectId[] array: 
            Array to copy from
            
            int index: 
            Index to begin at
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ObjectId value: 
            Item to search for
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Index to insert at
            
            ObjectId value: 
            Item to add
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            ObjectId value: 
            Object to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of object to remove
        """
        pass
    
    
    Count = None
    
    pass

class ObjectIdGraph(Graph):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    G
    
    r
    
    a
    
    p
    
    h
    
    (
    
    )
    """
    def AddNode(self):
        """
        AddNode -> void
            
            ObjectIdGraphNode nodeToAdd: 
            Input ObjectIdGraphNode to add to the graph.
        """
        pass
    
    
    def DelNode(self):
        """
        DelNode -> void
            
            nodeToAdd: 
            Input ObjectIdGraphNode to remove from the graph.
        """
        pass
    
    
    def FindNode(self):
        """
        FindNode -> ObjectIdGraphNode
            
            ObjectId id: 
            Input ObjectId for node to find.
        """
        pass
    
    
    def IdNode(self):
        """
        IdNode -> ObjectIdGraphNode
            
            int index: 
            Input zero based index of the node to get.
        """
        pass
    
    pass

class ObjectIdGraphNode(GraphNode):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
    G
    
    r
    
    a
    
    p
    
    h
    
    N
    
    o
    
    d
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    o
    
    d
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    .
    """
    def Create(self):
        """
        Create -> ObjectIdGraphNode
            
            IntPtr unmanagedPointer: 
            Input pointer to the AcDbObjectIdGraphNode object that the new ObjectIdGraphNode will wrap.
            
            [MarshalAs(UnmanagedType.U1)] bool autoDelete: 
            Input boolean indicating whether the wrapped AcDbObjectIdGraphNode should be deleted when this ObjectIdGraphNode is destroyed.
        """
        pass
    
    
    Id = None
    
    pass

class ObjectOverrule(Overrule):
    """
    
    """
    def Cancel(self):
        """
        Cancel -> void
        
        """
        pass
    
    
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def DeepClone(self):
        """
        DeepClone -> DBObject
        
        """
        pass
    
    
    def Erase(self):
        """
        Erase -> void
        
        """
        pass
    
    
    def Open(self):
        """
        Open -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def WblockClone(self):
        """
        WblockClone -> DBObject
        
        """
        pass
    
    pass

class ObjectSnapContext(public sealed class ObjectSnapContext):
    """
    
    """
    GraphicsSystemSelectionMark = None
    
    
    LastPoint = None
    
    
    PickedObject = None
    
    
    PickPoint = None
    
    
    ViewTransform = None
    
    pass

class ObjectSnapInfo(public sealed class ObjectSnapInfo):
    """
    
    """
    SnapCurves = None
    
    
    SnapPoints = None
    
    pass

  ModeCenter = 3
  ModeEnd = 1
  ModeIns = 7
  ModeMid = 2
  ModeNear = 10
  ModeNode = 4
  ModePerpendicular = 8
  ModeQuad = 5
  ModeTangent = 9

class ObjectTypeAttribute(Attribute):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    y
    
    p
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    y
    
    p
    
    e
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    :
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    """
    ObjectType = None
    
    pass

class Ole2Frame(Entity):
    """
    
    O
    
    l
    
    e
    
    2
    
    F
    
    r
    
    a
    
    m
    
    e
    
    (
    
    )
    """
      Embedded = 2
      Link = 1
      Static = 3
    
    
    AutoOutputQuality = None
    
    
    IsLinked = None
    
    
    LinkName = None
    
    
    LinkPath = None
    
    
    Location = None
    
    
    LockAspect = None
    
    
    OleObject = None
    
    
    OutputQuality = None
    
    
    Position2d = None
    
    
    Position3d = None
    
    
    Rotation = None
    
    
    ScaleHeight = None
    
    
    ScaleWidth = None
    
    
    Type = None
    
    
    UserType = None
    
    
    WcsHeight = None
    
    
    WcsWidth = None
    
    pass

class OpenCloseTransaction(Transaction):
    """
    
    """
    def Abort(self):
        """
        Abort -> void
        
        """
        pass
    
    
    def AddNewlyCreatedDBObject(self):
        """
        AddNewlyCreatedDBObject -> void
            
            DBObject obj: 
            Input object to be added or removed
            
            [MarshalAs(UnmanagedType.U1)] bool add: 
            Input Boolean indicating whether to add or remove the object
        """
        pass
    
    
    def Commit(self):
        """
        Commit -> void
        
        """
        pass
    
    
    def GetObject(self):
        """
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
            
            [MarshalAs(UnmanagedType.U1)] bool forceOpenOnLockedLayer: 
            Input true if locked layers should be opened
        """
        pass
    
    
    TransactionManager = None
    
    pass

  ForRead
  ForWrite
  ForNotify

class OpenModeAttribute(Attribute):
    """
    
    O
    
    p
    
    e
    
    n
    
    M
    
    o
    
    d
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    O
    
    p
    
    e
    
    n
    
    M
    
    o
    
    d
    
    e
    
     
    
    m
    
    o
    
    d
    
    e
    
     
    
    :
    
     
    
    M
    
    o
    
    d
    
    e
    
     
    
    o
    
    f
    
     
    
    o
    
    p
    
    e
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    """
    OpenMode = None
    
    pass

  NonOrthoView
  TopView
  BottomView
  FrontView
  BackView
  LeftView
  RightView

class OsnapOverrule(Overrule):
    """
    
    """
    def GetObjectSnapPoints(self):
        """
        GetObjectSnapPoints(Entity, ObjectSnapModes, IntPtr, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection) -> void
        
        GetObjectSnapPoints(Entity, ObjectSnapModes, IntPtr, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection, Matrix3d) -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class PCAdsName(public struct PCAdsName {
  public long name1;
  public long name2;
}):
    """
    
    """

    pass

  True
  False
  NotApplicable

class ParallelConstraint(GeometricalConstraint):
    """
    
    P
    
    a
    
    r
    
    a
    
    l
    
    l
    
    e
    
    l
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  ParseOptionNone
  SetDefaultFormat
  PreserveMtextFormat

  Default
  UpperCase
  IsExternalReference

  AbsolutePath = 3
  NoPath = 1
  PathAndFile = 4
  RelativePath = 2

class PathRef(GeomRef):
    """
    
    P
    
    a
    
    t
    
    h
    
    R
    
    e
    
    f
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    a
    
    t
    
    h
    
    R
    
    e
    
    f
    
    (
    
    E
    
    d
    
    g
    
    e
    
    R
    
    e
    
    f
    
    [
    
    ]
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    a
    
    t
    
    h
    
    R
    
    e
    
    f
    
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
    
    [
    
    ]
    
    ,
    
     
    
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
    
    [
    
    ]
    
    )
    
    (
    
    )
    """
    def GetEntityArray(self):
        """
        GetEntityArray -> Entity()
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
        
        """
        pass
    
    
    def IsReferencePath(self):
        """
        IsReferencePath -> bool
        
        """
        pass
    
    
    EdgeRefs = None
    
    pass

class PatternDefinition(public struct PatternDefinition {
}):
    """
    
    P
    
    a
    
    t
    
    t
    
    e
    
    r
    
    n
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    p
    
    a
    
    t
    
    t
    
    e
    
    r
    
    n
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    t
    
    t
    
    e
    
    r
    
    n
    
     
    
    a
    
    n
    
    g
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
     
    
    b
    
    a
    
    s
    
    e
    
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
    
     
    
    b
    
    a
    
    s
    
    e
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
     
    
    o
    
    f
    
    f
    
    s
    
    e
    
    t
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    f
    
    f
    
    s
    
    e
    
    t
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
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
    
     
    
    d
    
    a
    
    s
    
    h
    
    O
    
    f
    
    f
    
    s
    
    e
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    a
    
    s
    
    h
    
     
    
    o
    
    f
    
    f
    
    s
    
    e
    
    t
    
    s
    """
    def GetDashes(self):
        """
        GetDashes -> DoubleCollection
        
        """
        pass
    
    
    Angle = None
    
    
    BaseX = None
    
    
    BaseY = None
    
    
    OffsetX = None
    
    
    OffsetY = None
    
    pass

class PdfDefinition(UnderlayDefinition):
    """
    
    P
    
    d
    
    f
    
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
    
    (
    
    )
    """

    pass

class PdfReference(UnderlayReference):
    """
    
    P
    
    d
    
    f
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    (
    
    )
    """

    pass

class PerpendicularConstraint(GeometricalConstraint):
    """
    
    P
    
    e
    
    r
    
    p
    
    e
    
    n
    
    d
    
    i
    
    c
    
    u
    
    l
    
    a
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  PeakIntensity
  Flux
  Illuminance

class PlaceHolder(DBObject):
    """
    
    P
    
    l
    
    a
    
    c
    
    e
    
    H
    
    o
    
    l
    
    d
    
    e
    
    r
    
    (
    
    )
    """

    pass

  NonPlanar
  Planar
  Linear

class PlaneSurface(Surface):
    """
    
    P
    
    l
    
    a
    
    n
    
    e
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    )
    """
    def CreateFromRegion(self):
        """
        CreateFromRegion -> void
            
            Region region: 
            Input pointer to any Region object
        """
        pass
    
    pass

  Inches
  Millimeters
  Pixels

  Degrees000
  Degrees090
  Degrees180
  Degrees270

class PlotSettings(DBObject):
    """
    
    P
    
    l
    
    o
    
    t
    
    S
    
    e
    
    t
    
    t
    
    i
    
    n
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    m
    
    o
    
    d
    
    e
    
    l
    
    T
    
    y
    
    p
    
    e
    
     
    
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
    
    h
    
    a
    
    t
    
     
    
    d
    
    e
    
    t
    
    e
    
    r
    
    m
    
    i
    
    n
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    l
    
    o
    
    t
    
     
    
    s
    
    e
    
    t
    
    u
    
    p
    
     
    
    t
    
    y
    
    p
    
    e
    """
    def AddToPlotSettingsDictionary(self):
        """
        AddToPlotSettingsDictionary -> void
            
            Database toWhichDatabase: 
            Input database to which to add plot settings object
        """
        pass
    
    
    def SetShadePlot(self):
        """
        SetShadePlot -> void
            
            PlotSettingsShadePlotType type: 
            Input type of the shade plot object
            
            ObjectId shadePlotId: 
            Input object ID of the VisualStyle or RenderSettings object to be used as the shade plot object
        """
        pass
    
    
    CanonicalMediaName = None
    
    
    CurrentStyleSheet = None
    
    
    CustomPrintScale = None
    
    
    DrawViewportsFirst = None
    
    
    ModelType = None
    
    
    PlotAsRaster = None
    
    
    PlotCentered = None
    
    
    PlotConfigurationName = None
    
    
    PlotHidden = None
    
    
    PlotOrigin = None
    
    
    PlotPaperMargins = None
    
    
    PlotPaperSize = None
    
    
    PlotPaperUnits = None
    
    
    PlotPlotStyles = None
    
    
    PlotRotation = None
    
    
    PlotSettingsName = None
    
    
    PlotType = None
    
    
    PlotViewName = None
    
    
    PlotViewportBorders = None
    
    
    PlotWindowArea = None
    
    
    PlotWireframe = None
    
    
    PrintLineweights = None
    
    
    ScaleLineweights = None
    
    
    ShadePlot = None
    
    
    ShadePlotCustomDpi = None
    
    
    ShadePlotId = None
    
    
    ShadePlotResLevel = None
    
    
    ShowPlotStyles = None
    
    
    StdScale = None
    
    
    StdScaleType = None
    
    
    UseStandardScale = None
    
    pass

  AsDisplayed
  Wireframe
  Hidden
  Rendered
  VisualStyle
  RenderPreset

class PlotSettingsValidator(DisposableWrapper):
    """
    
    """
    def GetCanonicalMediaNameList(self):
        """
        GetCanonicalMediaNameList -> StringCollection
            
            PlotSettings plotSet: 
            Input pointer to PlotSettings object
        """
        pass
    
    
    def GetLocaleMediaName(self):
        """
        GetLocaleMediaName(PlotSettings, int) -> string
            
            PlotSettings plotSet: 
            Input
            
            int index: 
            Input index into collection returned by GetCanonicalMediaNameList()
        GetLocaleMediaName(PlotSettings, string) -> string
            
            PlotSettings plotSet: 
            Input
            
            string canonicalName: 
            Input locale independent media name identifier (item type returned by GetCanonicalMediaNameList())
        """
        pass
    
    
    def GetPlotDeviceList(self):
        """
        GetPlotDeviceList -> StringCollection
        
        """
        pass
    
    
    def GetPlotStyleSheetList(self):
        """
        GetPlotStyleSheetList -> StringCollection
        
        """
        pass
    
    
    def RefreshLists(self):
        """
        RefreshLists -> void
            
            PlotSettings plotSet: 
            Input
        """
        pass
    
    
    def SetCanonicalMediaName(self):
        """
        SetCanonicalMediaName -> void
            
            PlotSettings plotSet: 
            Input
            
            string mediaName: 
            Input pointer to canonical media name
        """
        pass
    
    
    def SetClosestMediaName(self):
        """
        SetClosestMediaName -> void
            
            PlotSettings plotSet: 
            _nt_
            
            double paperWidth: 
            _nt_
            
            double paperHeight: 
            _nt_
            
            PlotPaperUnit units: 
            _nt_
            
            [MarshalAs(UnmanagedType.U1)] bool matchPrintableArea: 
            _nt_
        """
        pass
    
    
    def SetCurrentStyleSheet(self):
        """
        SetCurrentStyleSheet -> void
            
            PlotSettings plotSet: 
            Input
            
            string styleSheetName: 
            Input pointer to plot style table name
        """
        pass
    
    
    def SetCustomPrintScale(self):
        """
        SetCustomPrintScale -> void
            
            PlotSettings plotSet: 
            Input
            
            CustomScale scale: 
            Input paperspace units
        """
        pass
    
    
    def SetDefaultPlotConfig(self):
        """
        SetDefaultPlotConfig -> void
            
            PlotSettings plotSet: 
            Input
        """
        pass
    
    
    def SetPlotCentered(self):
        """
        SetPlotCentered -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            [MarshalAs(UnmanagedType.U1)] bool isCentered: 
            Input Boolean indicating whether the plot should be centered
        """
        pass
    
    
    def SetPlotConfigurationName(self):
        """
        SetPlotConfigurationName -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            string plotDeviceName: 
            Input pointer to plot device name
            
            string mediaName: 
            Input media name
        """
        pass
    
    
    def SetPlotOrigin(self):
        """
        SetPlotOrigin -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Point2d origin: 
            Input offset coordinates
        """
        pass
    
    
    def SetPlotPaperUnits(self):
        """
        SetPlotPaperUnits -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            PlotPaperUnit units: 
            Input units by which the margins, offset, and paper size are interpreted
        """
        pass
    
    
    def SetPlotViewName(self):
        """
        SetPlotViewName -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            string viewName: 
            Input named view indicating the portion of the model to plot
        """
        pass
    
    
    def SetPlotWindowArea(self):
        """
        SetPlotWindowArea -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Extents2d windowArea: 
            Input window coordinates (coordinates must be in DCS)
        """
        pass
    
    
    def SetStdScale(self):
        """
        SetStdScale -> void
            
            PlotSettings plotSet: 
            Input
            
            double standardScale: 
            Input standard scale value
        """
        pass
    
    
    def SetUseStandardScale(self):
        """
        SetUseStandardScale -> void
            
            PlotSettings plotSet: 
            Input
            
            [MarshalAs(UnmanagedType.U1)] bool useStandard: 
            Input Boolean indicating whether to use standard scale
        """
        pass
    
    
    def SetZoomToPaperOnUpdate(self):
        """
        SetZoomToPaperOnUpdate -> void
            
            PlotSettings plotSet: 
            Input
            
            [MarshalAs(UnmanagedType.U1)] bool doZoom: 
            Input Boolean indicating whether to zoom
        """
        pass
    
    
    def SetPlotRotation(self):
        """
        SetPlotRotation -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Autodesk.AutoCAD.DatabaseServices.PlotRotation rotationType: 
            Input enumeration indicating rotation
        """
        pass
    
    
    def SetPlotType(self):
        """
        SetPlotType -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Autodesk.AutoCAD.DatabaseServices.PlotType plotAreaType: 
            Input enumeration indicating the portion of the layout to plot
        """
        pass
    
    
    def SetStdScaleType(self):
        """
        SetStdScaleType -> void
            
            PlotSettings plotSet: 
            Input plot set
            
            Autodesk.AutoCAD.DatabaseServices.StdScaleType scaleType: 
            Input standard scale
            CustomScale: 
            Scale is not a standard scale
            Scale1To128inAnd1ft: 
            1/128"= 1'
            Scale1To32inchAnd1ft: 
            1/32"= 1'
            StdScale3To32InchIs1ft: 
            3/32"= 1'
            StdScale3To16InchIs1ft: 
            3/16"= 1'
            StdScale3To8InchIs1ft: 
            3/8" = 1'
            StdScale3To4InchIs1ft: 
            3/4" = 1'
            Scale3inIs1ft: 
            3"= 1'
            Scale1ftIs1ft: 
            1'= 1'
            Scale1To4: 
            1:4
            Scale1To10: 
            1:10
            Scale1To20: 
            1:20
            Scale1To30: 
            1:40
            Scale1To100: 
            1:100
            Scale4To1: 
            4:1
            Scale10To1: 
            10:1
            Scale1000To1: 
            1000:1
        """
        pass
    
    
    Current = None
    
    pass

class PlotStyleDescriptor(public struct PlotStyleDescriptor {
}):
    """
    
    P
    
    l
    
    o
    
    t
    
    S
    
    t
    
    y
    
    l
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    I
    
    d
    
     
    
    i
    
    d
    
     
    
    :
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    p
    
    l
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    P
    
    l
    
    o
    
    t
    
    S
    
    t
    
    y
    
    l
    
    e
    
    N
    
    a
    
    m
    
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
    
     
    
    N
    
    e
    
    w
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    o
    
    f
    
     
    
    p
    
    l
    
    o
    
    t
    
     
    
    s
    
    t
    
    y
    
    l
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    """
    def Equals(self):
        """
        Equals -> bool
            
            object unmanagedObjPtr: 
            Object to compare with
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Culture-specific format
        """
        pass
    
    
    Id = None
    
    
    Type = None
    
    pass

  PlotStyleNameByLayer
  PlotStyleNameByBlock
  PlotStyleNameIsDictionaryDefault
  PlotStyleNameById

class PlotStyleTableChangedEventArgs(EventArgs):
    """
    
    """
    Id = None
    
    
    NewName = None
    
    pass

  Display
  Extents
  Limits
  View
  Window
  Layout

class Point3AngularDimension(Dimension):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    A
    
    n
    
    g
    
    u
    
    l
    
    a
    
    r
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    """
    ArcPoint = None
    
    
    CenterPoint = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

class PointCloud(Entity):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    l
    
    o
    
    u
    
    d
    
    (
    
    )
    """
    def RegenPointClouds(self):
        """
        RegenPointClouds -> void
        
        """
        pass
    
    pass

class PointCloudClassificationColorRamp(DisposableWrapper):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    l
    
    o
    
    u
    
    d
    
    C
    
    l
    
    a
    
    s
    
    s
    
    i
    
    f
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    C
    
    o
    
    l
    
    o
    
    r
    
    R
    
    a
    
    m
    
    p
    
    (
    
    )
    """
    def Color(self):
        """
        Color -> EntityColor
        
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
        
        """
        pass
    
    
    def SetFrom(self):
        """
        SetFrom -> void
        
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
        
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> bool
        
        """
        pass
    
    
    Name = None
    
    
    NumColors = None
    
    pass

class PointCloudColorMap(DBObject):
    """
    
    """
    def ClassificationColorSchemeInUse(self):
        """
        ClassificationColorSchemeInUse -> string()
        
        """
        pass
    
    
    def ClassificationScheme(self):
        """
        ClassificationScheme -> bool
        
        """
        pass
    
    
    def ColorScheme(self):
        """
        ColorScheme -> bool
        
        """
        pass
    
    
    def ColorSchemeInUse(self):
        """
        ColorSchemeInUse -> string()
        
        """
        pass
    
    
    def DeleteClassificationScheme(self):
        """
        DeleteClassificationScheme -> bool
        
        """
        pass
    
    
    def DeleteColorScheme(self):
        """
        DeleteColorScheme -> bool
        
        """
        pass
    
    
    def GetColorMapId(self):
        """
        GetColorMapId -> ObjectId
        
        """
        pass
    
    
    def HasClassificationScheme(self):
        """
        HasClassificationScheme -> bool
        
        """
        pass
    
    
    def HasColorScheme(self):
        """
        HasColorScheme -> bool
        
        """
        pass
    
    
    def SetClassificationScheme(self):
        """
        SetClassificationScheme -> bool
        
        """
        pass
    
    
    def SetColorScheme(self):
        """
        SetColorScheme -> bool
        
        """
        pass
    
    
    ClassificationSchemeGUIDs = None
    
    
    ColorSchemeGUIDs = None
    
    
    DefaultClassificationColorScheme = None
    
    
    DefaultElevationColorScheme = None
    
    
    DefaultIntensityColorScheme = None
    
    pass

class PointCloudColorRamp(DisposableWrapper):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    l
    
    o
    
    u
    
    d
    
    C
    
    o
    
    l
    
    o
    
    r
    
    R
    
    a
    
    m
    
    p
    
    (
    
    )
    """
    def Color(self):
        """
        Color -> EntityColor
        
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
        
        """
        pass
    
    
    def SetFrom(self):
        """
        SetFrom -> void
        
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
        
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> bool
        
        """
        pass
    
    
    Name = None
    
    
    NumColors = None
    
    pass

class PointCloudCrop(IDisposable):
    """
    
    """
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def Create(self):
        """
        Create -> PointCloudCrop
            
            IntPtr unmanagedObjPtr: 
            Specifies the AcDbPointCloudCrop pointer. For a valid pointer, it binds the created PointCloudCrop with it; if it is System::IntPtr::Zero, it creates a non-binded PointCloudCrop.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def IsValid(self):
        """
        IsValid -> bool
        
        """
        pass
    
    
    CropPlane = None
    
    
    CropType = None
    
    
    Inside = None
    
    
    Inverted = None
    
    
    Vertices = None
    
    pass

  Invalid
  Rectangular
  Polygonal
  Circular

class PointCloudDefEx(DBObject):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    l
    
    o
    
    u
    
    d
    
    D
    
    e
    
    f
    
    E
    
    x
    
    (
    
    )
    """
    def classVersion(self):
        """
        classVersion -> Integer
        
        """
        pass
    
    
    def getAllRcsFilePaths(self):
        """
        getAllRcsFilePaths -> string()
        
        """
        pass
    
    
    def getRcsFilePath(self):
        """
        getRcsFilePath -> string
            
            string guid: 
            Specifies the GUID of the RCS
        """
        pass
    
    
    def load(self):
        """
        load -> bool
        
        """
        pass
    
    
    def unload(self):
        """
        unload -> bool
        
        """
        pass
    
    
    ActiveFileName = None
    
    
    defaultHeight = None
    
    
    defaultLength = None
    
    
    defaultWidth = None
    
    
    EntityCount = None
    
    
    extents = None
    
    
    FileType = None
    
    
    SourceFileName = None
    
    
    totalPointsCount = None
    
    
    totalRegionsCount = None
    
    
    totalScansCount = None
    
    pass

  UseMinMaxColors
  UseRGBScanColors
  HidePoints

class PointCloudEx(Entity):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    l
    
    o
    
    u
    
    d
    
    E
    
    x
    
    (
    
    )
    """
    def addCroppingBoundary(self):
        """
        addCroppingBoundary -> void
            
            PointCloudCrop cropping: 
            An AcDbPointCloudCrop object which is to be added.
        """
        pass
    
    
    def AttachPointCloud(self):
        """
        AttachPointCloud -> ObjectId
            
            string filename: 
            Point cloud source file path. This represent the original filepath use to cerate the index. This entry can be blank.
            
            Point3d location: 
            Location of point cloud entity. If entity is inserted at 0,0,0 the points will appear where they are located in the point cloud.
            
            double scale: 
            Scale factor. 1.0 is default scale, and cannot less than 0.0
            
            double rotation: 
            Rotation Angle in degrees. 0 is default rotation
            
            Database db: 
            Returns object id of created PointCloudEx
        """
        pass
    
    
    def clearCropping(self):
        """
        clearCropping -> bool
        
        """
        pass
    
    
    def findRegionItem(self):
        """
        findRegionItem -> PointCloudItem
            
            int regionId: 
            The region ID to be returned.
        """
        pass
    
    
    def findScanItem(self):
        """
        findScanItem -> PointCloudItem
        
        """
        pass
    
    
    def GetColorSchemeForStylization(self):
        """
        GetColorSchemeForStylization -> string
            
            PointCloudStylizationType type: 
            Indicates a stylization type.
        """
        pass
    
    
    def getCroppingCount(self):
        """
        getCroppingCount -> Integer
        
        """
        pass
    
    
    def getPointCloudCropping(self):
        """
        getPointCloudCropping -> PointCloudCrop
        
        """
        pass
    
    
    def getPointCloudDataList(self):
        """
        getPointCloudDataList -> List<PointCloudItem>
        
        """
        pass
    
    
    def GetScanViewInfo(self):
        """
        GetScanViewInfo -> bool
        
        """
        pass
    
    
    def HasProperty(self):
        """
        HasProperty -> PointCloudPropertyState
        
        """
        pass
    
    
    def removeLastCropping(self):
        """
        removeLastCropping -> bool
        
        """
        pass
    
    
    def setAllRegionsVisibility(self):
        """
        setAllRegionsVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            The visibility for all regions.
            
            [MarshalAs(UnmanagedType.U1)] bool includeUnassigned: 
            true or false, whether or not set the bVisible to unassigned points
        """
        pass
    
    
    def setAllScansVisibility(self):
        """
        setAllScansVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            The visibility of all scans.
        """
        pass
    
    
    def SetColorSchemeForStylization(self):
        """
        SetColorSchemeForStylization -> void
            
            string name: 
            Indicates the name of a color scheme to be set.
            
            PointCloudStylizationType type: 
            Indicates a stylization type
        """
        pass
    
    
    def setRegionVisibility(self):
        """
        setRegionVisibility -> void
            
            int regionId: 
            The region ID
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            The region's visibility
        """
        pass
    
    
    def setScanVisibility(self):
        """
        setScanVisibility -> void
            
            string scanGuid: 
            The scan GUID
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            Whether or not the scan is visible
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> bool
            
            Matrix3d xform: 
            The input transform matrix.
        """
        pass
    
    
    ActiveFileName = None
    
    
    CroppingInverted = None
    
    
    CurrentColorScheme = None
    
    
    ElevationApplyToFixedRange = None
    
    
    ElevationGradient = None
    
    
    ElevationOutOfRangeBehavior = None
    
    
    GeomExtents = None
    
    
    IntensityGradient = None
    
    
    IntensityOutOfRangeBehavior = None
    
    
    LimitBoxBound = None
    
    
    Location = None
    
    
    MinMaxElevation = None
    
    
    MinMaxIntensity = None
    
    
    NativeExtents = None
    
    
    PointCloudDefExId = None
    
    
    Rotation = None
    
    
    Scale = None
    
    
    ShowCropped = None
    
    
    Stylization = None
    
    pass

class PointCloudItem(Notifier):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    l
    
    o
    
    u
    
    d
    
    I
    
    t
    
    e
    
    m
    
    (
    
    )
    """
    def Clone(self):
        """
        Clone -> PointCloudItem
        
        """
        pass
    
    
    def CompareTo(self):
        """
        CompareTo -> bool
            
            PointCloudItem other: 
            The second point cloud item for comparison.
        """
        pass
    
    
    def CreatePointCloudDataItemCollection(self):
        """
        CreatePointCloudDataItemCollection -> List<PointCloudItem>
            
            IntPtr unmanagedObjPtr: 
            The pointer of array of AcPointCloudItem
        """
        pass
    
    
    def modopt(self):
        """
        modopt -> ValueType
        
        """
        pass
    
    
    def ToCmdString(self):
        """
        ToCmdString -> string
        
        """
        pass
    
    
    CategoryId = None
    
    
    Guid = None
    
    
    ItemId = None
    
    
    Name = None
    
    
    ProjectName = None
    
    
    Visibility = None
    
    pass

  LegacyPointCloud
  PointCloudProject
  IndividualScan
  Scan
  Region
  ScanRootGroup
  RegionRootGroup
  UnassignedPoint

  Classification = 3
  Color = 1
  Intensity = 2
  Normal = 4

  All = 1
  None = -1
  Some = 0

  ClassificationRamp = 6
  HeightRamp = 4
  IntensityRamp = 5
  NormalRamp = 3
  SingleColor = 2
  TrueColor = 1

class PointCoincidenceConstraint(GeometricalConstraint):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    o
    
    i
    
    n
    
    c
    
    i
    
    d
    
    e
    
    n
    
    c
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class PointCurveConstraint(GeometricalConstraint):
    """
    
    P
    
    o
    
    i
    
    n
    
    t
    
    C
    
    u
    
    r
    
    v
    
    e
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

  SimplePoly
  FitCurvePoly
  QuadSplinePoly
  CubicSplinePoly

  SimplePoly
  QuadSplinePoly
  CubicSplinePoly

class PolyFaceMesh(Entity, IEnumerable):
    """
    
    P
    
    o
    
    l
    
    y
    
    F
    
    a
    
    c
    
    e
    
    M
    
    e
    
    s
    
    h
    
    (
    
    )
    """
    def AppendFaceRecord(self):
        """
        AppendFaceRecord -> ObjectId
            
            FaceRecord toAppend: 
            Input FaceRecord to append to the mesh
        """
        pass
    
    
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            PolyFaceMeshVertex vertexToAppend: 
            Input vertex to append to mesh
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    NumFaces = None
    
    
    NumVertices = None
    
    pass

class PolyFaceMeshVertex(Vertex):
    """
    
    P
    
    o
    
    l
    
    y
    
    F
    
    a
    
    c
    
    e
    
    M
    
    e
    
    s
    
    h
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    l
    
    y
    
    F
    
    a
    
    c
    
    e
    
    M
    
    e
    
    s
    
    h
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    s
    
    i
    
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
    
     
    
    W
    
    C
    
    S
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    """
    Position = None
    
    pass

  BezierSurfaceMesh = 8
  CubicSurfaceMesh = 6
  QuadSurfaceMesh = 5
  SimpleMesh = 0

class PolygonMesh(Entity, IEnumerable):
    """
    
    P
    
    o
    
    l
    
    y
    
    g
    
    o
    
    n
    
    M
    
    e
    
    s
    
    h
    
    (
    
    )
    
    (
    
    )
    """
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            PolygonMeshVertex toAppend: 
            Input vertex to append to mesh
        """
        pass
    
    
    def ConvertToPolyMeshType(self):
        """
        ConvertToPolyMeshType -> void
            
            Autodesk.AutoCAD.DatabaseServices.PolyMeshType newVal: 
            Input type to which the polygon mesh should be converted
            SimpleMesh: 
            Plain mesh with no surface fitting or smoothing
            QuadSurfaceMesh: 
            Quadratic B-spline surface fit
            CubicSurfaceMesh: 
            Cubic B-spline surface fit
            BezierSurfaceMesh: 
            Bezier surface fit
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def MakeMClosed(self):
        """
        MakeMClosed -> void
        
        """
        pass
    
    
    def MakeMOpen(self):
        """
        MakeMOpen -> void
        
        """
        pass
    
    
    def MakeNClosed(self):
        """
        MakeNClosed -> void
        
        """
        pass
    
    
    def MakeNOpen(self):
        """
        MakeNOpen -> void
        
        """
        pass
    
    
    def Straighten(self):
        """
        Straighten -> void
        
        """
        pass
    
    
    def SurfaceFit(self):
        """
        SurfaceFit() -> void
        
        """
        pass
    
    
    IsMClosed = None
    
    
    IsNClosed = None
    
    
    MSize = None
    
    
    MSurfaceDensity = None
    
    
    NSize = None
    
    
    NSurfaceDensity = None
    
    
    PolyMeshType = None
    
    pass

class PolygonMeshVertex(Vertex):
    """
    
    P
    
    o
    
    l
    
    y
    
    g
    
    o
    
    n
    
    M
    
    e
    
    s
    
    h
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    l
    
    y
    
    g
    
    o
    
    n
    
    M
    
    e
    
    s
    
    h
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
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
    
     
    
    W
    
    C
    
    S
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    """
    Position = None
    
    
    VertexType = None
    
    pass

class Polyline(Curve):
    """
    
    P
    
    o
    
    l
    
    y
    
    l
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    l
    
    y
    
    l
    
    i
    
    n
    
    e
    
    (
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    v
    
    e
    
    r
    
    t
    
    i
    
    c
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    v
    
    e
    
    r
    
    t
    
    i
    
    c
    
    e
    
    s
    
     
    
    t
    
    o
    
     
    
    a
    
    l
    
    l
    
    o
    
    c
    
    a
    
    t
    
    e
    
     
    
    m
    
    e
    
    m
    
    o
    
    r
    
    y
    
     
    
    f
    
    o
    
    r
    """
    def AddVertexAt(self):
        """
        AddVertexAt -> void
            
            int index: 
            Input index (0 based) before which to insert the vertex
            
            Point2d pt: 
            Input vertex location point
            
            double bulge: 
            Input bulge value for vertex
            
            double startWidth: 
            Input start width for vertex
            
            double endWidth: 
            Input end width for vertex
        """
        pass
    
    
    def ConvertFrom(self):
        """
        ConvertFrom -> void
            
            Entity entity: 
            Input pointer to the Polyline2d to copy from
            
            [MarshalAs(UnmanagedType.U1)] bool transferId: 
            Input Boolean indicating whether or not to do a HandOverTo between the Polyline2d and the Polyline
        """
        pass
    
    
    def ConvertTo(self):
        """
        ConvertTo -> Polyline2d
            
            [MarshalAs(UnmanagedType.U1)] bool transferId: 
            Input Boolean indicating whether or not to do a handOverTo between the Polyline and the Polyline2d.
        """
        pass
    
    
    def GetArcSegment2dAt(self):
        """
        GetArcSegment2dAt -> CircularArc2d
            
            int index: 
            Input index (0 based) of the vertex for start of arc
        """
        pass
    
    
    def GetArcSegmentAt(self):
        """
        GetArcSegmentAt -> CircularArc3d
            
            int index: 
            Input index (0 based) of the vertex for start of arc
        """
        pass
    
    
    def GetBulgeAt(self):
        """
        GetBulgeAt -> double
            
            int index: 
            Input index (0 based) of the vertex for start of bulge
        """
        pass
    
    
    def GetEndWidthAt(self):
        """
        GetEndWidthAt -> double
            
            int index: 
            Input index (0 based) of the polyline
        """
        pass
    
    
    def GetLineSegment2dAt(self):
        """
        GetLineSegment2dAt -> LineSegment2d
            
            int index: 
            Input index (0 based) of the vertex for start of segment
        """
        pass
    
    
    def GetLineSegmentAt(self):
        """
        GetLineSegmentAt -> LineSegment3d
            
            int index: 
            Input index (0 based) of the vertex for start of segment
        """
        pass
    
    
    def GetPoint2dAt(self):
        """
        GetPoint2dAt -> Point2d
            
            int index: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def GetPoint3dAt(self):
        """
        GetPoint3dAt -> Point3d
            
            int value: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def GetSegmentType(self):
        """
        GetSegmentType -> SegmentType
            
            int index: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def GetStartWidthAt(self):
        """
        GetStartWidthAt -> double
            
            int index: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def MaximizeMemory(self):
        """
        MaximizeMemory -> void
        
        """
        pass
    
    
    def MinimizeMemory(self):
        """
        MinimizeMemory -> void
        
        """
        pass
    
    
    def OnSegmentAt(self):
        """
        OnSegmentAt -> bool
            
            int index: 
            Input index (0 based) of the vertex
            
            Point2d pt2d: 
            Input point (in polyline OCS coords) to check at vertex index
            
            double value: 
            Output parameter of at vertex index
        """
        pass
    
    
    def RemoveVertexAt(self):
        """
        RemoveVertexAt -> void
            
            int index: 
            Input index (0 based) of the vertex to remove
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
            
            [MarshalAs(UnmanagedType.U1)] bool reuse: 
            Input Boolean indicating whether or not to retain some vertices
            
            int vertices: 
            Input number of vertices to retain
        """
        pass
    
    
    def SetBulgeAt(self):
        """
        SetBulgeAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            double bulge: 
            Input bulge value for the vertex
        """
        pass
    
    
    def SetEndWidthAt(self):
        """
        SetEndWidthAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            double endWidth: 
            Input end width value for vertex index
        """
        pass
    
    
    def SetPointAt(self):
        """
        SetPointAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            Point2d pt: 
            Input location for the vertex
        """
        pass
    
    
    def SetStartWidthAt(self):
        """
        SetStartWidthAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            double startWidth: 
            Input start width value for vertex index
        """
        pass
    
    
    Closed = None
    
    
    ConstantWidth = None
    
    
    Elevation = None
    
    
    HasBulges = None
    
    
    HasWidth = None
    
    
    IsOnlyLines = None
    
    
    Length = None
    
    
    Normal = None
    
    
    NumberOfVertices = None
    
    
    Plinegen = None
    
    
    Thickness = None
    
    pass

class Polyline2d(Curve, IEnumerable):
    """
    
    P
    
    o
    
    l
    
    y
    
    l
    
    i
    
    n
    
    e
    
    2
    
    d
    
    (
    
    )
    
    (
    
    )
    """
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            Vertex2d vertexToAppend: 
            Input the vertex to add to the polyline
        """
        pass
    
    
    def ConvertToPolyType(self):
        """
        ConvertToPolyType -> void
            
            Autodesk.AutoCAD.DatabaseServices.Poly2dType newVal: 
            Input type to which the polyline should be converted
        """
        pass
    
    
    def CurveFit(self):
        """
        CurveFit -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def InsertVertexAt(self):
        """
        InsertVertexAt(ObjectId, Vertex2d) -> ObjectId
            
            Vertex2d newVertex: 
            Input vertex to be inserted
            
            indexVertex: 
            Input vertex in polyline after which the new vertex is to be inserted
        InsertVertexAt(Vertex2d, Vertex2d) -> void
            
            Vertex2d newVertex: 
            Input pointer to vertex to be inserted
            
            vertexId: 
            Input objectId of the vertex in the polyline after which the new vertex is to be inserted
        """
        pass
    
    
    def NonDBAppendVertex(self):
        """
        NonDBAppendVertex -> void
            
            Vertex2d vertexToAppend: 
            Input the vertex to add to the polyline
        """
        pass
    
    
    def SplineFit(self):
        """
        SplineFit() -> void
        
        """
        pass
    
    
    def Straighten(self):
        """
        Straighten -> void
        
        """
        pass
    
    
    def VertexPosition(self):
        """
        VertexPosition -> Point3d
            
            Vertex2d vertex: 
            Input vertex object to get the WCS coordinate for
        """
        pass
    
    
    Closed = None
    
    
    ConstantWidth = None
    
    
    DefaultEndWidth = None
    
    
    DefaultStartWidth = None
    
    
    Elevation = None
    
    
    Length = None
    
    
    LinetypeGenerationOn = None
    
    
    Normal = None
    
    
    PolyType = None
    
    
    Thickness = None
    
    pass

class Polyline3d(Curve, IEnumerable):
    """
    
    P
    
    o
    
    l
    
    y
    
    l
    
    i
    
    n
    
    e
    
    3
    
    d
    
    (
    
    )
    
    (
    
    )
    """
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            PolylineVertex3d vertexToAppend: 
            Input pointer to the vertex to add to the polyline
        """
        pass
    
    
    def ConvertToPolyType(self):
        """
        ConvertToPolyType -> void
            
            Autodesk.AutoCAD.DatabaseServices.Poly3dType newVal: 
            Input type to which the polyline should be converted
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def InsertVertexAt(self):
        """
        InsertVertexAt(ObjectId, PolylineVertex3d) -> ObjectId
            
            ObjectId indexVertexId: 
            Input vertex in polyline after which the new vertex is to be inserted
            
            PolylineVertex3d newVertex: 
            Input vertex to be inserted
        InsertVertexAt(PolylineVertex3d, PolylineVertex3d) -> void
            
            PolylineVertex3d indexVertex: 
            Input objectId of the vertex in the polyline after which the new vertex is to be inserted
            
            PolylineVertex3d newVertex: 
            Input vertex to be inserted
        """
        pass
    
    
    def SplineFit(self):
        """
        SplineFit() -> void
        
        """
        pass
    
    
    def Straighten(self):
        """
        Straighten -> void
        
        """
        pass
    
    
    Closed = None
    
    
    Length = None
    
    
    PolyType = None
    
    pass

class PolylineVertex3d(Vertex):
    """
    
    P
    
    o
    
    l
    
    y
    
    l
    
    i
    
    n
    
    e
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    3
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    l
    
    y
    
    l
    
    i
    
    n
    
    e
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    3
    
    d
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    a
    
    r
    
    a
    
    m
    
    0
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    W
    
    C
    
    S
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    """
    Position = None
    
    
    VertexType = None
    
    pass

class Profile3d(RXObject):
    """
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
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
    
    D
    
    a
    
    t
    
    a
    
    b
    
    a
    
    s
    
    e
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
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
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
    (
    
    P
    
    a
    
    t
    
    h
    
    R
    
    e
    
    f
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
    (
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    3
    
    d
    
    (
    
    V
    
    e
    
    r
    
    t
    
    e
    
    x
    
    R
    
    e
    
    f
    
    )
    
    (
    
    )
    """
    def ConvertProfile(self):
        """
        ConvertProfile(PathRef[]) -> Profile3d
        
        ConvertProfile([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Profile3d()
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def MergeProfiles(self):
        """
        MergeProfiles -> Profile3d()
        
        """
        pass
    
    
    Entity = None
    
    
    IsClosed = None
    
    
    IsEdge = None
    
    
    IsFace = None
    
    
    IsPlanar = None
    
    
    IsSubent = None
    
    
    IsValid = None
    
    
    ProfilePathRef = None
    
    
    ProfileVertexRef = None
    
    pass

class PropertiesOverrule(Overrule):
    """
    
    """
    def GetClassID(self):
        """
        GetClassID -> Guid
        
        """
        pass
    
    
    def List(self):
        """
        List -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class ProxyEntity(Entity):
    """
    
    """
    def GetReferences(self):
        """
        GetReferences -> DBObjectReferenceCollection
        
        """
        pass
    
    
    ApplicationDescription = None
    
    
    GraphicsMetafileType = None
    
    
    OriginalClassName = None
    
    
    OriginalDxfName = None
    
    
    ProxyFlags = None
    
    pass

class ProxyObject(DBObject):
    """
    
    """
    def GetReferences(self):
        """
        GetReferences -> DBObjectReferenceCollection
        
        """
        pass
    
    
    def ResurrectMeNow(self):
        """
        ResurrectMeNow -> void
            
            ObjectId id: 
            Input object ID of object to be resurrected
        """
        pass
    
    
    ApplicationDescription = None
    
    
    OriginalClassName = None
    
    
    OriginalDxfName = None
    
    
    ProxyFlags = None
    
    pass

class ProxyResurrectionCompletedEventArgs(EventArgs):
    """
    
    """
    ApplicationName = None
    
    
    Ids = None
    
    pass

class RadialDimension(Dimension):
    """
    
    R
    
    a
    
    d
    
    i
    
    a
    
    l
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    """
    Center = None
    
    
    ChordPoint = None
    
    
    LeaderLength = None
    
    pass

class RadialDimensionLarge(Dimension):
    """
    
    R
    
    a
    
    d
    
    i
    
    a
    
    l
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    L
    
    a
    
    r
    
    g
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    Center = None
    
    
    ChordPoint = None
    
    
    JogAngle = None
    
    
    JogPoint = None
    
    
    OverrideCenter = None
    
    pass

class RadiusDiameterConstraint(ExplicitConstraint):
    """
    
    R
    
    a
    
    d
    
    i
    
    u
    
    s
    
    D
    
    i
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    R
    
    a
    
    d
    
    i
    
    u
    
    s
    
    D
    
    i
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    R
    
    a
    
    d
    
    D
    
    i
    
    a
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    T
    
    y
    
    p
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    a
    
    d
    
    D
    
    i
    
    a
    
    C
    
    o
    
    n
    
    s
    
    t
    
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
    
     
    
    R
    
    a
    
    d
    
    D
    
    i
    
    a
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    T
    
    y
    
    p
    
    e
    
     
    
    i
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    
    .
    """
      CircleRadius
      CircleDiameter
      MinorRadius
      MajorRadius
    
    
    ConstrType = None
    
    pass

class RapidRTRenderSettings(RenderSettings):
    """
    
    R
    
    a
    
    p
    
    i
    
    d
    
    R
    
    T
    
    R
    
    e
    
    n
    
    d
    
    e
    
    r
    
    S
    
    e
    
    t
    
    t
    
    i
    
    n
    
    g
    
    s
    
    (
    
    )
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    FilterHeight = None
    
    
    FilterType = None
    
    
    FilterWidth = None
    
    
    LightingModel = None
    
    
    RenderLevel = None
    
    
    RenderTarget = None
    
    
    RenderTime = None
    
    pass

  Level
  Time
  Infinite

class RasterImage(Image):
    """
    
    R
    
    a
    
    s
    
    t
    
    e
    
    r
    
    I
    
    m
    
    a
    
    g
    
    e
    
    (
    
    )
    """
    def AssociateRasterDef(self):
        """
        AssociateRasterDef -> void
            
            RasterImageDef definition: 
            Input raster image def
        """
        pass
    
    
    def EnableReactors(self):
        """
        EnableReactors -> void
            
            [MarshalAs(UnmanagedType.U1)] bool enable: 
            Input boolean switch
        """
        pass
    
    
    def GetClipBoundary(self):
        """
        GetClipBoundary -> Point2dCollection
        
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices -> Point3dCollection
        
        """
        pass
    
    
    def ImageSize(self):
        """
        ImageSize -> Vector2d
            
            [MarshalAs(UnmanagedType.U1)] bool getCachedValue: 
            Input Boolean indicating whether the cached should be used
        """
        pass
    
    
    def SetClipBoundary(self):
        """
        SetClipBoundary(Autodesk.AutoCAD.DatabaseServices.ClipBoundaryType, Point2dCollection) -> void
            
            Autodesk.AutoCAD.DatabaseServices.ClipBoundaryType type: 
            Input clip boundary type
            
            Point2dCollection clipBoundaryVertices: 
            Input collection of clip boundary vertices
        SetClipBoundary(Vector2d) -> void
            
            Vector2d size: 
            Input vector of boundary
        """
        pass
    
    
    def SetClipBoundaryToWholeImage(self):
        """
        SetClipBoundaryToWholeImage -> void
        
        """
        pass
    
    
    Brightness = None
    
    
    ClipBoundaryType = None
    
    
    Contrast = None
    
    
    DisplayOptions = None
    
    
    Fade = None
    
    
    Height = None
    
    
    ImageDefId = None
    
    
    ImageHeight = None
    
    
    ImageTransparency = None
    
    
    ImageWidth = None
    
    
    IsClipped = None
    
    
    Name = None
    
    
    Orientation = None
    
    
    Path = None
    
    
    PixelToModelTransform = None
    
    
    Position = None
    
    
    ReactorId = None
    
    
    Rotation = None
    
    
    Scale = None
    
    
    ShowImage = None
    
    
    Width = None
    
    pass

class RasterImageDef(DBObject):
    """
    
    R
    
    a
    
    s
    
    t
    
    e
    
    r
    
    I
    
    m
    
    a
    
    g
    
    e
    
    D
    
    e
    
    f
    
    (
    
    )
    """
    def CloseImage(self):
        """
        CloseImage -> void
        
        """
        pass
    
    
    def CreateImageDictionary(self):
        """
        CreateImageDictionary -> ObjectId
            
            Database database: 
            Input AutoCAD database in which to create the dictionary
        """
        pass
    
    
    def Embed(self):
        """
        Embed -> void
        
        """
        pass
    
    
    def GetEntityCount(self):
        """
        GetEntityCount -> Integer
            
            out bool locked: 
            Input locked value
        """
        pass
    
    
    def GetImageDictionary(self):
        """
        GetImageDictionary -> ObjectId
            
            Database database: 
            Input AutoCAD database in which to find the dictionary
        """
        pass
    
    
    def ImageCopy(self):
        """
        ImageCopy -> IntPtr
            
            [MarshalAs(UnmanagedType.U1)] bool forceImageLoad: 
            Input Boolean indicating whether to load the image if it is not currently loaded
        """
        pass
    
    
    def Load(self):
        """
        Load -> void
        
        """
        pass
    
    
    def LocateActivePath(self):
        """
        LocateActivePath -> string
        
        """
        pass
    
    
    def OpenImage(self):
        """
        OpenImage -> IntPtr
        
        """
        pass
    
    
    def SetImage(self):
        """
        SetImage -> void
            
            IntPtr image: 
            Input NULL or pointer to valid Atil::Image object
            
            IntPtr fileDescription: 
            Input NULL or pointer to valid Atil::FileReadDescriptor object
            
            [MarshalAs(UnmanagedType.U1)] bool modifyDatabase: 
            Input Boolean indicating whether to do undo recording
        """
        pass
    
    
    def SuggestName(self):
        """
        SuggestName -> string
            
            DBDictionary imageDictionary: 
            Input pointer to the (previously opened for reading) image dictionary within which this name must be unique
            
            string newImagePathName: 
            Input pointer to a string containing the source image file or path name
        """
        pass
    
    
    def Unload(self):
        """
        Unload -> void
            
            [MarshalAs(UnmanagedType.U1)] bool modifyDatabase: 
            Input Boolean indicating whether or not to do undo recording
        """
        pass
    
    
    def UpdateEntities(self):
        """
        UpdateEntities -> void
        
        """
        pass
    
    
    ActiveFileName = None
    
    
    ColorDepth = None
    
    
    FileDescCopy = None
    
    
    FileType = None
    
    
    ImageModified = None
    
    
    IsEmbedded = None
    
    
    IsLoaded = None
    
    
    Organization = None
    
    
    ResolutionMMPerPixel = None
    
    
    ResolutionUnits = None
    
    
    SearchForActivePath = None
    
    
    Size = None
    
    
    SourceFileName = None
    
    
    UndoStoreSize = None
    
    pass

class RasterVariables(DBObject):
    """
    
    R
    
    a
    
    s
    
    t
    
    e
    
    r
    
    V
    
    a
    
    r
    
    i
    
    a
    
    b
    
    l
    
    e
    
    s
    
    (
    
    )
    """
    ImageFrame = None
    
    
    ImageQuality = None
    
    
    UserScale = None
    
    pass

class Ray(Curve):
    """
    
    R
    
    a
    
    y
    
    (
    
    )
    """
    BasePoint = None
    
    
    SecondPoint = None
    
    
    UnitDir = None
    
    pass

class Rectangle3d(public struct Rectangle3d {
}):
    """
    
    R
    
    e
    
    c
    
    t
    
    a
    
    n
    
    g
    
    l
    
    e
    
    3
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    u
    
    p
    
    p
    
    e
    
    r
    
    L
    
    e
    
    f
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    u
    
    p
    
    p
    
    e
    
    r
    
     
    
    l
    
    e
    
    f
    
    t
    
     
    
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
    
     
    
    u
    
    p
    
    p
    
    e
    
    r
    
    R
    
    i
    
    g
    
    h
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    u
    
    p
    
    p
    
    e
    
    r
    
     
    
    r
    
    i
    
    g
    
    h
    
    t
    
     
    
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
    
     
    
    l
    
    o
    
    w
    
    e
    
    r
    
    L
    
    e
    
    f
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    o
    
    w
    
    e
    
    r
    
     
    
    l
    
    e
    
    f
    
    t
    
     
    
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
    
     
    
    l
    
    o
    
    w
    
    e
    
    r
    
    R
    
    i
    
    g
    
    h
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    o
    
    w
    
    e
    
    r
    
     
    
    r
    
    i
    
    g
    
    h
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format.
        """
        pass
    
    
    LowerLeft = None
    
    
    LowerRight = None
    
    
    UpperLeft = None
    
    
    UpperRight = None
    
    pass

class RegAppTable(SymbolTable, IEnumerable):
    """
    
    """

    pass

class RegAppTableRecord(SymbolTableRecord):
    """
    
    R
    
    e
    
    g
    
    A
    
    p
    
    p
    
    T
    
    a
    
    b
    
    l
    
    e
    
    R
    
    e
    
    c
    
    o
    
    r
    
    d
    
    (
    
    )
    """

    pass

class Region(Entity):
    """
    
    R
    
    e
    
    g
    
    i
    
    o
    
    n
    
    (
    
    )
    """
    def AreaProperties(self):
        """
        AreaProperties -> RegionAreaProperties
            
            ref Point3d origin: 
            Input point (in WCS coords) for origin of the coordinate system to usefor evaluation.
            
            ref Vector3d xAxis: 
            Input X axis (in WCS coords) of the coordinate system to use forevaluation.
            
            ref Vector3d yAxis: 
            Input Y axis (in WCS coords) of the coordinate system to use forevaluation.
        """
        pass
    
    
    def BooleanOperation(self):
        """
        BooleanOperation -> void
            
            BooleanOperationType operation: 
            Input type of Boolean operation.
            
            Region otherRegion: 
            Input pointer to another region to perform the Boolean operation
        """
        pass
    
    
    def CreateFromCurves(self):
        """
        CreateFromCurves -> DBObjectCollection
            
            DBObjectCollection curveSegments: 
            Input collection to curve entities used to define the region's perimeter(s)
        """
        pass
    
    
    Area = None
    
    
    IsNull = None
    
    
    Normal = None
    
    
    NumChanges = None
    
    
    Perimeter = None
    
    
    UsesGraphicsCache = None
    
    pass

class RegionAreaProperties(public struct RegionAreaProperties {
}):
    """
    
    """
    Area = None
    
    
    Centroid = None
    
    
    Extents = None
    
    
    MomentsOfInertia = None
    
    
    Perimeter = None
    
    
    PrincipalMoments = None
    
    
    ProductOfInertia = None
    
    
    RadiiOfGyration = None
    
    pass

class RenderEnvironment(DBObject):
    """
    
    R
    
    e
    
    n
    
    d
    
    e
    
    r
    
    E
    
    n
    
    v
    
    i
    
    r
    
    o
    
    n
    
    m
    
    e
    
    n
    
    t
    
    (
    
    )
    """
    class DoubleRangeParameter(public struct DoubleRangeParameter {
    }):
        """
        
        D
        
        o
        
        u
        
        b
        
        l
        
        e
        
        R
        
        a
        
        n
        
        g
        
        e
        
        P
        
        a
        
        r
        
        a
        
        m
        
        e
        
        t
        
        e
        
        r
        
        
        
        
         
        
         
        
         
        
         
        
        d
        
        o
        
        u
        
        b
        
        l
        
        e
        
         
        
        n
        
         
        
        :
        
         
        
        N
        
        e
        
        a
        
        r
        
         
        
        d
        
        i
        
        s
        
        t
        
        a
        
        n
        
        c
        
        e
        
        
        
        
         
        
         
        
         
        
         
        
        d
        
        o
        
        u
        
        b
        
        l
        
        e
        
         
        
        f
        
         
        
        :
        
         
        
        F
        
        a
        
        r
        
         
        
        d
        
        i
        
        s
        
        t
        
        a
        
        n
        
        c
        
        e
        """
        Far = None
        
        
        Near = None
        
        pass
    
    
    Distances = None
    
    
    EnvironmentImageEnabled = None
    
    
    EnvironmentImageFileName = None
    
    
    FogBackgroundEnabled = None
    
    
    FogColor = None
    
    
    FogDensity = None
    
    
    FogEnabled = None
    
    pass

class RenderGlobal(DBObject):
    """
    
    R
    
    e
    
    n
    
    d
    
    e
    
    r
    
    G
    
    l
    
    o
    
    b
    
    a
    
    l
    
    (
    
    )
    """
    class DimensionsParameter(public struct DimensionsParameter {
    }):
        """
        
        D
        
        i
        
        m
        
        e
        
        n
        
        s
        
        i
        
        o
        
        n
        
        s
        
        P
        
        a
        
        r
        
        a
        
        m
        
        e
        
        t
        
        e
        
        r
        
        
        
        
         
        
         
        
         
        
         
        
        i
        
        n
        
        t
        
         
        
        w
        
         
        
        :
        
         
        
        W
        
        i
        
        d
        
        t
        
        h
        
         
        
        p
        
        a
        
        r
        
        a
        
        m
        
        e
        
        t
        
        e
        
        r
        
        
        
        
         
        
         
        
         
        
         
        
        i
        
        n
        
        t
        
         
        
        h
        
         
        
        :
        
         
        
        H
        
        e
        
        i
        
        g
        
        h
        
        t
        
         
        
        p
        
        a
        
        r
        
        a
        
        m
        
        e
        
        t
        
        e
        
        r
        """
        Height = None
        
        
        Width = None
        
        pass
    
    
    class ProcedureAndDestinationParameter(public struct ProcedureAndDestinationParameter {
    }):
        """
        
        P
        
        r
        
        o
        
        c
        
        e
        
        d
        
        u
        
        r
        
        e
        
        A
        
        n
        
        d
        
        D
        
        e
        
        s
        
        t
        
        i
        
        n
        
        a
        
        t
        
        i
        
        o
        
        n
        
        P
        
        a
        
        r
        
        a
        
        m
        
        e
        
        t
        
        e
        
        r
        
        
        
        
         
        
         
        
         
        
         
        
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
        
        D
        
        a
        
        t
        
        a
        
        b
        
        a
        
        s
        
        e
        
        S
        
        e
        
        r
        
        v
        
        i
        
        c
        
        e
        
        s
        
        .
        
        R
        
        e
        
        n
        
        d
        
        e
        
        r
        
        G
        
        l
        
        o
        
        b
        
        a
        
        l
        
        .
        
        P
        
        r
        
        o
        
        c
        
        e
        
        d
        
        u
        
        r
        
        e
        
         
        
        p
        
         
        
        :
        
         
        
        I
        
        n
        
        p
        
        u
        
        t
        
         
        
        a
        
         
        
        p
        
        r
        
        o
        
        c
        
        e
        
        d
        
        u
        
        r
        
        e
        
        
        
        
         
        
         
        
         
        
         
        
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
        
        D
        
        a
        
        t
        
        a
        
        b
        
        a
        
        s
        
        e
        
        S
        
        e
        
        r
        
        v
        
        i
        
        c
        
        e
        
        s
        
        .
        
        R
        
        e
        
        n
        
        d
        
        e
        
        r
        
        G
        
        l
        
        o
        
        b
        
        a
        
        l
        
        .
        
        D
        
        e
        
        s
        
        t
        
        i
        
        n
        
        a
        
        t
        
        i
        
        o
        
        n
        
         
        
        d
        
         
        
        :
        
         
        
        I
        
        n
        
        p
        
        u
        
        t
        
         
        
        a
        
         
        
        d
        
        e
        
        s
        
        t
        
        i
        
        n
        
        a
        
        t
        
        i
        
        o
        
        n
        """
        Destination = None
        
        
        Procedure = None
        
        pass
    
    
      Window
      Viewport
    
    
      View
      Crop
      Selected
    
    
    Dimensions = None
    
    
    HighInfoLevel = None
    
    
    PredefinedPresetsFirst = None
    
    
    ProcedureAndDestination = None
    
    
    SaveEnabled = None
    
    
    SaveFileName = None
    
    pass

class RenderSettings(DBObject):
    """
    
    R
    
    e
    
    n
    
    d
    
    e
    
    r
    
    S
    
    e
    
    t
    
    t
    
    i
    
    n
    
    g
    
    s
    
    (
    
    )
    """
    BackFacesEnabled = None
    
    
    Description = None
    
    
    DiagnosticBackgroundEnabled = None
    
    
    DisplayIndex = None
    
    
    IsPredefined = None
    
    
    MaterialsEnabled = None
    
    
    Name = None
    
    
    PreviewImageFileName = None
    
    
    ShadowsEnabled = None
    
    
    TextureSampling = None
    
    pass

class ResultBuffer(DisposableWrapper, IEnumerable, IFormattable):
    """
    
    R
    
    e
    
    s
    
    u
    
    l
    
    t
    
    B
    
    u
    
    f
    
    f
    
    e
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    R
    
    e
    
    s
    
    u
    
    l
    
    t
    
    B
    
    u
    
    f
    
    f
    
    e
    
    r
    
    (
    
    p
    
    a
    
    r
    
    a
    
    m
    
    s
    
     
    
    T
    
    y
    
    p
    
    e
    
    d
    
    V
    
    a
    
    l
    
    u
    
    e
    
    [
    
    ]
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    p
    
    a
    
    r
    
    a
    
    m
    
    s
    
     
    
    T
    
    y
    
    p
    
    e
    
    d
    
    V
    
    a
    
    l
    
    u
    
    e
    
    [
    
    ]
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    s
    """
    def Add(self):
        """
        Add(TypedValue) -> void
            
            TypedValue value: 
            Input object to add
        Add(object) -> void
            
            object value: 
            Input object to add
        """
        pass
    
    
    def AsArray(self):
        """
        AsArray -> TypedValue()
        
        """
        pass
    
    
    def Create(self):
        """
        Create -> ResultBuffer
            
            IntPtr buffer: 
            Input pointer
            
            [MarshalAs(UnmanagedType.U1)] bool autoDelete: 
            Set to true if the pointer should be deleted after creation
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to check against
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> ResultBufferEnumerator
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture definition
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format for string
            
            IFormatProvider provider: 
            Input culture definition
        """
        pass
    
    pass

class ResultBufferEnumerator(IEnumerator):
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
    
    
    Current = None
    
    pass

class RevolveOptions(DisposableWrapper, ICloneable):
    """
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    (
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
     
    
    o
    
    p
    
    t
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    c
    
    o
    
    p
    
    i
    
    e
    
    d
    
    .
    """
    def CheckRevolveCurve(self):
        """
        CheckRevolveCurve -> RevolveOptionsCheckRevolveCurveOut
            
            Point3d axisPnt: 
            Input point on axis of revolution
            
            Vector3d axisDir: 
            Input direction of axis of revolution
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean value indicating whether to display error messages
            
            unnamed: 
            Input the curve or region to be revolved
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    CloseToAxis = None
    
    
    DraftAngle = None
    
    
    TwistAngle = None
    
    pass

class RevolveOptionsBuilder(public class RevolveOptionsBuilder):
    """
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    B
    
    u
    
    i
    
    l
    
    d
    
    e
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    B
    
    u
    
    i
    
    l
    
    d
    
    e
    
    r
    
    (
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    n
    
    s
    
    t
    
    r
    
    u
    
    c
    
    t
    
    o
    
    r
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
    .
    """
    def ToRevolveOptions(self):
        """
        ToRevolveOptions -> RevolveOptions
        
        """
        pass
    
    
    CloseToAxis = None
    
    
    DraftAngle = None
    
    
    TwistAngle = None
    
    pass

class RevolveOptionsCheckRevolveCurveOut(public class RevolveOptionsCheckRevolveCurveOut):
    """
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    O
    
    p
    
    t
    
    i
    
    o
    
    n
    
    s
    
    C
    
    h
    
    e
    
    c
    
    k
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    C
    
    u
    
    r
    
    v
    
    e
    
    O
    
    u
    
    t
    
    (
    
    )
    """
    Closed = None
    
    
    EndPointsOnAxis = None
    
    
    Planar = None
    
    pass

class RevolvedSurface(Autodesk.AutoCAD.DatabaseServices.Surface):
    """
    
    R
    
    e
    
    v
    
    o
    
    l
    
    v
    
    e
    
    d
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    )
    """
    def CreateRevolvedSurface(self):
        """
        CreateRevolvedSurface -> void
            
            Entity revolveEntity: 
            Input the planar curve, region, or planar surface that is to be revolved
            
            Point3d axisPoint: 
            Input point on the axis of revolution
            
            Vector3d axisDirection: 
            Input direction on the axis of revolution
            
            double revolveAngle: 
            Input angle of rotation in radians
            
            double startAngle: 
            Input start angle of rotation, in radians. If 0, then rotation will start from current position of revolveEntity
            
            Autodesk.AutoCAD.DatabaseServices.RevolveOptions revolveOptions: 
            Input revolve options
        """
        pass
    
    
    def SetRevolve(self):
        """
        SetRevolve -> void
            
            Point3d axisPoint: 
            Input axis point
            
            Vector3d axisDirection: 
            Input axis vector
            
            double revolveAngle: 
            Input angle of revolution, in radians
            
            Autodesk.AutoCAD.DatabaseServices.RevolveOptions revolveOptions: 
            Input revolve options
        """
        pass
    
    
    AxisDirection = None
    
    
    AxisPoint = None
    
    
    RevolveAngle = None
    
    
    RevolveEntity = None
    
    
    RevolveOptions = None
    
    
    RevolveProfile = None
    
    
    StartAngle = None
    
    pass

  NotRigidSet
  ScalableRigidSet
  NonScalableRigidSet

class RotatedDimension(Dimension):
    """
    
    R
    
    o
    
    t
    
    a
    
    t
    
    e
    
    d
    
    D
    
    i
    
    m
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    """
    DimLinePoint = None
    
    
    Oblique = None
    
    
    Rotation = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

  Degrees000 = 0
  Degrees090 = 1
  Degrees180 = 2
  Degrees270 = 3
  DegreesUnknown = -1

  DataRow = 1
  HeaderRow = 4
  TitleRow = 2
  UnknownRow = 0

NoSave
Save12
Save13
Save14
Save2000
Save2004
Save2007
Save2010
Save2013

class Section(Entity):
    """
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    o
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    l
    
    i
    
    n
    
    e
    
    ;
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    a
    
    t
    
     
    
    l
    
    e
    
    a
    
    s
    
    t
    
     
    
    t
    
    w
    
    o
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    v
    
    e
    
    r
    
    t
    
    i
    
    c
    
    a
    
    l
    
    D
    
    i
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    o
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    s
    
    e
    
    g
    
    m
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
    ,
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    l
    
    i
    
    n
    
    e
    
    
    
    
    
    
    
    
    
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
     
    
    v
    
    e
    
    r
    
    t
    
    e
    
    x
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    o
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    l
    
    i
    
    n
    
    e
    
    ;
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    a
    
    t
    
     
    
    l
    
    e
    
    a
    
    s
    
    t
    
     
    
    t
    
    w
    
    o
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    v
    
    e
    
    r
    
    t
    
    i
    
    c
    
    a
    
    l
    
    D
    
    i
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    o
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    s
    
    e
    
    g
    
    m
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    p
    
    l
    
    a
    
    n
    
    e
    
    ,
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    l
    
    i
    
    n
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    v
    
    e
    
    c
    
    V
    
    i
    
    e
    
    w
    
    i
    
    n
    
    g
    
    D
    
    i
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    v
    
    i
    
    e
    
    w
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    r
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    """
    def AddVertex(self):
        """
        AddVertex -> void
            
            int nInsertAt: 
            Input index at which to add the new vertex
            
            Point3d pt: 
            Input position of the new vertex
        """
        pass
    
    
    def CreateJog(self):
        """
        CreateJog -> void
            
            Point3d ptOnSection: 
            Input point on the section line at which to create the jog
        """
        pass
    
    
    def GenerateSectionGeometry(self):
        """
        GenerateSectionGeometry -> void
            
            Entity pEnt: 
            Input sectionable entity
            
            out Array pIntFillEnts: 
            Return array containing intersection boundary geometry
            
            out Array pBackgroundEnts: 
            Return array containing intersection fill annotation geometry
            
            out Array pForegroundEnts: 
            Return array containing background geometry
            
            out Array pFurveTangencyEnts: 
            Return array containing foreground geometry
            
            out Array pCurveTangencyEnts: 
            Return array containing curve tangency geometry
        """
        pass
    
    
    def GetVertex(self):
        """
        GetVertex -> Point3d
            
            int nIndex: 
            Input zero-based index of the vertex to be retrieved; should be less than the number of vertices
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices -> void
            
            Point3dCollection pts: 
            Output reference to receive vertices
        """
        pass
    
    
    def Height(self):
        """
        Height -> double
            
            SectionHeight nHeightType: 
            Input one of the SectionHeight enum values
        """
        pass
    
    
    def HitTest(self):
        """
        HitTest -> SectionHitTestInfo
            
            Point3d ptHit: 
            Input point to perform hit test
        """
        pass
    
    
    def RemoveVertex(self):
        """
        RemoveVertex -> void
            
            int nIndex: 
            Input index of the vertex to remove
            
            nHeightType: 
            Input one of the Height enum values
            
            fHeight: 
            Input height
        """
        pass
    
    
    def SetHeight(self):
        """
        SetHeight -> void
            
            SectionHeight nHeightType: 
            Input one of the Height enum val
            
            double fHeight: 
            Input height Sets the height of the section plane above or below the section line. The height is the indicator height when the section plane type is plane or boundary, since the cuts extends infinitely in the vertical direction for these two types.
        """
        pass
    
    
    def SetVertex(self):
        """
        SetVertex -> void
            
            int nIndex: 
            Input zero-based index of the vertex to set; should be less than the number of vertices
            
            Point3d pt: 
            Input new position of the vertex
        """
        pass
    
    
    BottomPlane = None
    
    
    Boundary = None
    
    
    Elevation = None
    
    
    HasJogs = None
    
    
    IndicatorFillColor = None
    
    
    IndicatorTransparency = None
    
    
    IsLiveSectionEnabled = None
    
    
    IsSlice = None
    
    
    Name = None
    
    
    Normal = None
    
    
    NumVertices = None
    
    
    SectionPlaneOffset = None
    
    
    Settings = None
    
    
    State = None
    
    
    ThicknessDepth = None
    
    
    TopPlane = None
    
    
    VerticalDirection = None
    
    
    Vertices = None
    
    
    ViewingDirection = None
    
    pass

  DestinationFile = 0x40
  DestinationNewBlock = 0x10
  DestinationReplaceBlock = 0x20
  SourceAllObjects = 1
  SourceSelectedObjects = 2

  BackgroundGeometry = 4
  CurveTangencyLines = 0x10
  ForegroundGeometry = 8
  IntersectionBoundary = 1
  IntersectionFill = 2

  HeightAboveSectionLine = 1
  HeightBelowSectionLine = 2

class SectionHitTestInfo(public struct SectionHitTestInfo {
}):
    """
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    H
    
    i
    
    t
    
    T
    
    e
    
    s
    
    t
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
    Index = None
    
    
    PtOnSegment = None
    
    
    SubItem = None
    
    pass

class SectionManager(DBObject, IEnumerable):
    """
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def GetSection(self):
        """
        GetSection -> ObjectId
            
            string pszName: 
            Input name of the section plane to get
        """
        pass
    
    
    def GetUniqueSectionName(self):
        """
        GetUniqueSectionName -> string
            
            string pszBaseName: 
            Input System.String object.
        """
        pass
    
    
    LiveSection = None
    
    
    NumSections = None
    
    pass

class SectionSettings(DBObject):
    """
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    t
    
    t
    
    i
    
    n
    
    g
    
    s
    
    (
    
    )
    """
    def Reset(self):
        """
        Reset() -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type to be reset
        """
        pass
    
    
    def Color(self):
        """
        Color -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def DestinationBlock(self):
        """
        DestinationBlock -> ObjectId
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination block is to be returned
        """
        pass
    
    
    def DestinationFile(self):
        """
        DestinationFile -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination file is to be returned
        """
        pass
    
    
    def DivisionLines(self):
        """
        DivisionLines -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def EdgeTransparency(self):
        """
        EdgeTransparency -> Integer
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def FaceTransparency(self):
        """
        FaceTransparency -> Integer
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def GenerationOptions(self):
        """
        GenerationOptions -> SectionGeneration
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the generation options object is to be returned
        """
        pass
    
    
    def GetHatchPatternName(self):
        """
        GetHatchPatternName -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def GetHatchPatternType(self):
        """
        GetHatchPatternType -> Autodesk.AutoCAD.DatabaseServices.HatchPatternType
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def GetSourceObjects(self):
        """
        GetSourceObjects -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the source objects are to be returned
            
            ObjectIdCollection ids: 
            Output collection of the object IDs
        """
        pass
    
    
    def HatchAngle(self):
        """
        HatchAngle -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HatchScale(self):
        """
        HatchScale -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HatchSpacing(self):
        """
        HatchSpacing -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HatchVisibility(self):
        """
        HatchVisibility -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HiddenLine(self):
        """
        HiddenLine -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def Layer(self):
        """
        Layer -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def Linetype(self):
        """
        Linetype -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def LinetypeScale(self):
        """
        LinetypeScale -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input section type
        """
        pass
    
    
    def LineWeight(self):
        """
        LineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def PlotStyleName(self):
        """
        PlotStyleName -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color to set
        """
        pass
    
    
    def SetDestinationBlock(self):
        """
        SetDestinationBlock -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination block is to be set
            
            ObjectId id: 
            Input ID of the block to be replaced during section generation
        """
        pass
    
    
    def SetDestinationFile(self):
        """
        SetDestinationFile -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination file is to be set
            
            string pszFileName: 
            Input destination file name
        """
        pass
    
    
    def SetDivisionLines(self):
        """
        SetDivisionLines -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bShow: 
            Input true if division lines are to be shown, or false if they are to be hidden
        """
        pass
    
    
    def SetEdgeTransparency(self):
        """
        SetEdgeTransparency -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            int nTransparency: 
            Input edge transparency to set, in the range 0-100
        """
        pass
    
    
    def SetFaceTransparency(self):
        """
        SetFaceTransparency -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            int nTransparency: 
            Input edge transparency to set, in the range 0-100
        """
        pass
    
    
    def SetGenerationOptions(self):
        """
        SetGenerationOptions -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the generation options are to be set
            
            SectionGeneration nOptions: 
            Input options flag to set
        """
        pass
    
    
    def SetHatchPatternType(self):
        """
        SetHatchPatternType -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            Autodesk.AutoCAD.DatabaseServices.HatchPatternType nPatternType: 
            Input pattern type
        """
        pass
    
    
    def SetHatchAngle(self):
        """
        SetHatchAngle -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            double fAngle: 
            Input hatch angle
        """
        pass
    
    
    def SetHatchPatternName(self):
        """
        SetHatchPatternName -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string sNewName: 
            Input hatch pattern name
        """
        pass
    
    
    def SetHatchScale(self):
        """
        SetHatchScale -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def SetHatchSpacing(self):
        """
        SetHatchSpacing -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def SetHatchVisibility(self):
        """
        SetHatchVisibility -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bVisible: 
            Input visibility value
        """
        pass
    
    
    def SetHiddenLine(self):
        """
        SetHiddenLine -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bHiddenLine: 
            Input visibility value
        """
        pass
    
    
    def SetLayer(self):
        """
        SetLayer -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string pszLayer: 
            Input layer to set
        """
        pass
    
    
    def SetLinetype(self):
        """
        SetLinetype -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string pszLinetype: 
            Input new linetype
        """
        pass
    
    
    def SetLinetypeScale(self):
        """
        SetLinetypeScale -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            double fScale: 
            Input new linetype scale
        """
        pass
    
    
    def SetLineWeight(self):
        """
        SetLineWeight -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight nLineWeight: 
            Input line weight
        """
        pass
    
    
    def SetPlotStyleName(self):
        """
        SetPlotStyleName -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string pszPlotStyleName: 
            Input plot style name
        """
        pass
    
    
    def SetSourceObjects(self):
        """
        SetSourceObjects -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            ObjectIdCollection ids: 
            Input source object IDs
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bVisible: 
            Input visibility value
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    CurrentSectionType = None
    
    pass

  Boundary = 2
  Plane = 1
  Volume = 4

  BackLine = 8
  BackLineBottom = 0x20
  BackLineTop = 0x10
  SectionLine = 1
  SectionLineBottom = 4
  SectionLineTop = 2
  SectionSubItemNone = 0
  VerticalLineBottom = 0x80
  VerticalLineTop = 0x40

class SectionSymbol(Entity):
    """
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    S
    
    y
    
    m
    
    b
    
    o
    
    l
    
    (
    
    )
    """
    def AddSectionPoint(self):
        """
        AddSectionPoint -> void
        
        """
        pass
    
    
    def GetBulgeAt(self):
        """
        GetBulgeAt -> double
            
            int index: 
            Input: zero-based index into the section symbol point bulge collection.
        """
        pass
    
    
    def GetLabelNameAt(self):
        """
        GetLabelNameAt -> string
            
            int index: 
            Input: zero-based index into the section symbol point collection.
        """
        pass
    
    
    def GetLabelOffsetAt(self):
        """
        GetLabelOffsetAt -> Vector3d
            
            int index: 
            Input: zero-based index into the section symbol point collection.
        """
        pass
    
    
    def GetLabelOffsets(self):
        """
        GetLabelOffsets -> Vector3dCollection
        
        """
        pass
    
    
    def GetSectionPointAt(self):
        """
        GetSectionPointAt -> Point3d
            
            int index: 
            Input: zero-based index into the section symbol point collection.
        """
        pass
    
    
    def GetSectionPoints(self):
        """
        GetSectionPoints -> Point3dCollection
        
        """
        pass
    
    
    def RemoveSectionPointAt(self):
        """
        RemoveSectionPointAt -> void
        
        """
        pass
    
    
    def SetLabelNameAt(self):
        """
        SetLabelNameAt -> void
        
        """
        pass
    
    
    def SetLabelOffsetAt(self):
        """
        SetLabelOffsetAt -> void
        
        """
        pass
    
    
    def SetLabelOffsets(self):
        """
        SetLabelOffsets -> void
        
        """
        pass
    
    
    def SetSectionPointAt(self):
        """
        SetSectionPointAt -> void
        
        """
        pass
    
    
    Identifier = None
    
    
    IsHalfSection = None
    
    
    IsViewDirectionLeft = None
    
    
    Scale = None
    
    
    SectionPointsCount = None
    
    
    SymbolStyleId = None
    
    pass

  LiveSection = 1
  Section2d = 2
  Section3d = 4

  TowardsCuttingPlane
  AwayFromCuttingPlane

  EndCuttingPlane
  AboveDirectionArrowLine
  AboveDirectionArrowSymbol
  StartDirectionArrow
  EndDirectionArrow

class SectionViewStyle(DBObject):
    """
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    V
    
    i
    
    e
    
    w
    
    S
    
    t
    
    y
    
    l
    
    e
    
    (
    
    )
    """
    def DefaultViewName(self):
        """
        DefaultViewName -> string
            
            int index: 
            The index of the default name.
        """
        pass
    
    
    def GetViewLabelPattern(self):
        """
        GetViewLabelPattern -> string
            
            Field field: 
            Input: a field object to be updated with the view label pattern master field.
        """
        pass
    
    
    def PostViewStyleToDb(self):
        """
        PostViewStyleToDb -> ObjectId
            
            Database dataBasePointer: 
            Input: database to be updated
            
            string styleName: 
            Input: name to be used for this view style.
        """
        pass
    
    
    def SetDatabaseDefaults(self):
        """
        SetDatabaseDefaults -> void
            
            Database dataBasePointer: 
            Input: database to be used
        """
        pass
    
    
    def SetViewLabelPattern(self):
        """
        SetViewLabelPattern -> void
            
            string pattern: 
            Input: the pattern string for the view label.
            
            Field field: 
            Input: optional pointer to a Field object to provide the field data to be used in the view label pattern.
        """
        pass
    
    
    def ValidateIdentifierExcludeCharacters(self):
        """
        ValidateIdentifierExcludeCharacters -> bool
            
            string characters: 
            Input: the characters to validate.
        """
        pass
    
    
    def ValidateViewName(self):
        """
        ValidateViewName -> bool
            
            string name: 
            Input: section name to validate.
        """
        pass
    
    
    ArrowEndSymbolId = None
    
    
    ArrowPosition = None
    
    
    ArrowStartSymbolId = None
    
    
    ArrowSymbolColor = None
    
    
    ArrowSymbolExtensionLength = None
    
    
    ArrowSymbolSize = None
    
    
    BendLineColor = None
    
    
    BendLineLength = None
    
    
    BendLineTypeId = None
    
    
    BendLineWeight = None
    
    
    Description = None
    
    
    EndLineLength = None
    
    
    EndLineOvershoot = None
    
    
    HatchAngles = None
    
    
    HatchBackgroundColor = None
    
    
    HatchColor = None
    
    
    HatchPattern = None
    
    
    HatchScale = None
    
    
    HatchTransparency = None
    
    
    IdentifierColor = None
    
    
    IdentifierExcludeCharacters = None
    
    
    IdentifierHeight = None
    
    
    IdentifierOffset = None
    
    
    IdentifierPosition = None
    
    
    IdentifierStyleId = None
    
    
    IsContinuousLabeling = None
    
    
    IsModifiedForRecompute = None
    
    
    Name = None
    
    
    PlaneLineColor = None
    
    
    PlaneLineTypeId = None
    
    
    PlaneLineWeight = None
    
    
    ShowAllBendIndentifiers = None
    
    
    ShowAllPlaneLines = None
    
    
    ShowArrowheads = None
    
    
    ShowEndAndBendLines = None
    
    
    ShowHatching = None
    
    
    ShowViewLabel = None
    
    
    ViewLabelAlignment = None
    
    
    ViewLabelAttachment = None
    
    
    ViewLabelOffset = None
    
    
    ViewLabelPattern = None
    
    
    ViewLabelTextColor = None
    
    
    ViewLabelTextHeight = None
    
    
    ViewLabelTextStyleId = None
    
    pass

  AddTimeStamp = 0x20
  EncryptData = 1
  EncryptProperties = 2
  SignData = 0x10

  RC4 = 0x6801

class SecurityParameters(public sealed class SecurityParameters):
    """
    
    S
    
    e
    
    c
    
    u
    
    r
    
    i
    
    t
    
    y
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    s
    
    (
    
    )
    
    (
    
    )
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object.
        """
        pass
    
    
    Action = None
    
    
    Algorithm = None
    
    
    Comment = None
    
    
    Issuer = None
    
    
    Password = None
    
    
    ProviderName = None
    
    
    SerialNumber = None
    
    
    Subject = None
    
    
    TimeServer = None
    
    pass

  Line
  Arc
  Coincident
  Point
  Empty

  Crossing = 2
  Window = 1

class SequenceEnd(Entity):
    """
    
    S
    
    e
    
    q
    
    u
    
    e
    
    n
    
    c
    
    e
    
    E
    
    n
    
    d
    
    (
    
    )
    """

    pass

  Draft
  Preview
  Normal
  Presentation
  Maximum
  Custom

  AsDisplayed
  Wireframe
  Hidden
  Rendered
  VisualStyle
  RenderPreset

class Shape(Entity):
    """
    
    S
    
    h
    
    a
    
    p
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    h
    
    a
    
    p
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    s
    
    i
    
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
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    h
    
    a
    
    p
    
    e
    
    ,
    
     
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    s
    
    i
    
    z
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    h
    
    e
    
    i
    
    g
    
    h
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    h
    
    a
    
    p
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    r
    
    o
    
    t
    
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
    
     
    
    r
    
    o
    
    t
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    h
    
    a
    
    p
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    d
    
    t
    
    h
    
    F
    
    a
    
    c
    
    t
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    i
    
    d
    
    t
    
    h
    
     
    
    f
    
    a
    
    c
    
    t
    
    o
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    h
    
    a
    
    p
    
    e
    """
    Name = None
    
    
    Normal = None
    
    
    Oblique = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    ShapeIndex = None
    
    
    ShapeNumber = None
    
    
    Size = None
    
    
    StyleId = None
    
    
    Thickness = None
    
    
    WidthFactor = None
    
    pass

class Solid(Entity):
    """
    
    S
    
    o
    
    l
    
    i
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    o
    
    l
    
    i
    
    d
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    3
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    
    
    
    
    
    
    
    
    
    
    S
    
    o
    
    l
    
    i
    
    d
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    1
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    r
    
    s
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    2
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    e
    
    c
    
    o
    
    n
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    3
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    i
    
    r
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    e
    
    r
    
    4
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    o
    
    u
    
    r
    
    t
    
    h
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
    )
    
     
    
    f
    
    o
    
    r
    
     
    
    s
    
    o
    
    l
    
    i
    
    d
    """
    def GetPointAt(self):
        """
        GetPointAt -> Point3d
            
            short index: 
            Input index (1-4) of the desired point in the solid
        """
        pass
    
    
    def SetPointAt(self):
        """
        SetPointAt -> void
            
            short index: 
            Input index (1-4) of the point to set in the solid
            
            Point3d pointValue: 
            Input point value
        """
        pass
    
    
    Normal = None
    
    
    Thickness = None
    
    pass

class Solid3d(Entity):
    """
    
    S
    
    o
    
    l
    
    i
    
    d
    
    3
    
    d
    
    (
    
    )
    """
    def BooleanOperation(self):
        """
        BooleanOperation -> void
            
            BooleanOperationType operation: 
            Input type of Boolean operation
            
            Solid3d solid: 
            Input the other solid with which to carry out the Boolean operation
        """
        pass
    
    
    def ChamferEdges(self):
        """
        ChamferEdges -> void
            
            SubentityId[] subentityIds: 
            Input object ids of edges at which the chamfer will be applied
            
            SubentityId baseSubentityId: 
            Input object id of the base face where the chamfer will be applied
            
            double baseDist: 
            Input chamfer distance on the base face
            
            double otherDist: 
            Input chamfer distance on the other faces
        """
        pass
    
    
    def CheckInterference(self):
        """
        CheckInterference -> bool
            
            Solid3d otherSolid: 
            Input pointer for other solid
        """
        pass
    
    
    def CleanBody(self):
        """
        CleanBody -> void
        
        """
        pass
    
    
    def ConvertToBrepAtSubentPaths(self):
        """
        ConvertToBrepAtSubentPaths -> void
            
            FullSubentityPath[] paths: 
            Input array of references to history items
        """
        pass
    
    
    def CopyEdge(self):
        """
        CopyEdge -> Entity
            
            SubentityId subEntityId: 
            Input subentity ID of an edge in the Solid3d
        """
        pass
    
    
    def CopyFace(self):
        """
        CopyFace -> Entity
            
            SubentityId subEntityId: 
            Input subentity ID of a face in the Solid3d
        """
        pass
    
    
    def CreateBox(self):
        """
        CreateBox -> void
            
            double lengthAlongX: 
            Input value for length of the box
            
            double lengthAlongY: 
            Input value for width of the box
            
            double lengthAlongZ: 
            Input value for height of the box
        """
        pass
    
    
    def CreateFrustum(self):
        """
        CreateFrustum -> void
            
            double height: 
            Input height for the frustum
            
            double radiusAlongX: 
            Input radius for the frustum in X direction
            
            double radiusAlongY: 
            Input radius for the frustum in Y direction
            
            double topRadius: 
            Input radius for top end of the frustum
        """
        pass
    
    
    def CreateExtrudedSolid(self):
        """
        CreateExtrudedSolid(Entity, SubentityId, Vector3d, SweepOptions) -> void
        
        CreateExtrudedSolid(Entity, SubentityId, double, SweepOptions) -> void
        
        CreateExtrudedSolid(Entity, Vector3d, SweepOptions) -> void
        
        """
        pass
    
    
    def CreatePyramid(self):
        """
        CreatePyramid -> void
            
            double height: 
            Input height for pyramid
            
            int sides: 
            Input number of sides for pyramid
            
            double radius: 
            Input radius for inscribed circle of bottom polygon
            
            double topRadius: 
            Input radius for inscribed circle of top polygon
        """
        pass
    
    
    def CreateSphere(self):
        """
        CreateSphere -> void
            
            double radius: 
            Input radius for the sphere
        """
        pass
    
    
    def CreateLoftedSolid(self):
        """
        CreateLoftedSolid(Entity[], Entity[], Entity, LoftOptions) -> void
        
        CreateLoftedSolid(LoftProfile[], LoftProfile[], LoftProfile, LoftOptions) -> void
        
        """
        pass
    
    
    def CreateTorus(self):
        """
        CreateTorus -> void
            
            double majorRadius: 
            Input major radius for the torus
            
            double minorRadius: 
            Input minor radius for the torus
        """
        pass
    
    
    def CreateWedge(self):
        """
        CreateWedge -> void
            
            double lengthAlongX: 
            Input length for the wedge
            
            double lengthAlongY: 
            Input width for the wedge
            
            double lengthAlongZ: 
            Input height for the wedge
        """
        pass
    
    
    def CreateRevolvedSolid(self):
        """
        CreateRevolvedSolid(Entity, Point3d, Vector3d, double, double, RevolveOptions) -> void
        
        CreateRevolvedSolid(Entity, SubentityId, Point3d, Vector3d, double, double, RevolveOptions) -> void
        
        """
        pass
    
    
    def Extrude(self):
        """
        Extrude -> void
            
            Region region: 
            Input a region object
            
            double height: 
            Input height for extrusion
            
            double taperAngle: 
            Input taper angle in radians
        """
        pass
    
    
    def CreateSculptedSolid(self):
        """
        CreateSculptedSolid -> void
        
        """
        pass
    
    
    def ExtrudeAlongPath(self):
        """
        ExtrudeAlongPath -> void
            
            Region region: 
            Input a region object
            
            Curve path: 
            Input a curve object to extrude along
            
            double taperAngle: 
            Input extrusion taper angle in radians
        """
        pass
    
    
    def ExtrudeFaces(self):
        """
        ExtrudeFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be extruded; these faces must be planar
            
            double height: 
            Input extrusion distance to be applied to the specified faces. Use a positive value to extrude in the direction of the face normals, which point outward from the solid. Use a negative value to extrude faces into the solid.
            
            double taper: 
            Input angle of tapering to be applied to the extrusion; the tapering is relative to the axis formed from the center of each face in the direction of the face normal when a positive height is used or in the opposite direction when a negative height is used; this value should be between half pi and half pi
        """
        pass
    
    
    def CreateSweptSolid(self):
        """
        CreateSweptSolid(Entity, Entity, SweepOptions) -> void
        
        CreateSweptSolid(Entity, SubentityId, Entity, SweepOptions) -> void
        
        """
        pass
    
    
    def ExtrudeFacesAlongPath(self):
        """
        ExtrudeFacesAlongPath -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be extruded; these faces must be planar
            
            Curve path: 
            Input a curve object to extrude along
        """
        pass
    
    
    def FilletEdges(self):
        """
        FilletEdges -> void
            
            SubentityId[] subentityIds: 
            Input object ids of the edges where the fillet will be applied
            
            DoubleCollection radius: 
            Input radius at the corresponding edge
            
            DoubleCollection startSetback: 
            Input start setback at the corresponding edge
            
            DoubleCollection endSetback: 
            Input end setback at the corresponding edge
        """
        pass
    
    
    def GetSection(self):
        """
        GetSection -> Region
            
            Plane plane: 
            Input plane to use as the section cutting plane
        """
        pass
    
    
    def GetSubentityColor(self):
        """
        GetSubentityColor -> Autodesk.AutoCAD.Colors.Color
            
            SubentityId subEntityId: 
            Input subentity Id
        """
        pass
    
    
    def GetSubentityMaterial(self):
        """
        GetSubentityMaterial -> ObjectId
            
            SubentityId subEntityId: 
            Input subentity Id
        """
        pass
    
    
    def GetSubentityMaterialMapper(self):
        """
        GetSubentityMaterialMapper -> Mapper
            
            SubentityId subEntityId: 
            Input subenttity Id
        """
        pass
    
    
    def ImprintEntity(self):
        """
        ImprintEntity -> void
            
            Entity entity: 
            Input entity to be imprinted
        """
        pass
    
    
    def OffsetBody(self):
        """
        OffsetBody -> void
            
            double offsetDistance: 
            Input distance to offset each face
        """
        pass
    
    
    def OffsetFaces(self):
        """
        OffsetFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be offset
            
            double offsetDistance: 
            Input distance to offset each face
        """
        pass
    
    
    def RemoveFaces(self):
        """
        RemoveFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be removed
        """
        pass
    
    
    def Revolve(self):
        """
        Revolve -> void
            
            Region region: 
            Input region object to be revolved
            
            Point3d axisPoint: 
            Input point on the line to be projected to create the axis of revolution
            
            Vector3d axisDir: 
            Input vector representing the direction of the line to be projected to create the axis of revolution
            
            double angleOfRevolution: 
            Input angle of revolution in radians
        """
        pass
    
    
    def SeparateBody(self):
        """
        SeparateBody -> Solid3d()
        
        """
        pass
    
    
    def SetSubentityColor(self):
        """
        SetSubentityColor -> void
            
            SubentityId subEntityId: 
            Input ID of subentity face or edge to be colored
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color for the subentity
        """
        pass
    
    
    def SetSubentityMaterial(self):
        """
        SetSubentityMaterial -> void
            
            SubentityId subEntityId: 
            Input subentity Id
            
            ObjectId materialId: 
            Input object Id of the material
        """
        pass
    
    
    def ProjectOnToSolid(self):
        """
        ProjectOnToSolid -> Entity()
        
        """
        pass
    
    
    def SetSubentityMaterialMapper(self):
        """
        SetSubentityMaterialMapper -> void
            
            SubentityId subEntityId: 
            Input subentity ID
            
            Mapper mapper: 
            Input a Mapper object
        """
        pass
    
    
    def ShellBody(self):
        """
        ShellBody -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be removed from the shell
            
            double offsetDistance: 
            Input distance to offset each face
        """
        pass
    
    
    def Slice(self):
        """
        Slice(Plane) -> void
            
            Plane plane: 
            Input plane to be used for slicing the solid
        Slice(Plane, [MarshalAs(UnmanagedType.U1)] bool) -> Solid3d
            
            Plane plane: 
            Input plane to be used for slicing the solid
            
            [MarshalAs(UnmanagedType.U1)] bool negativeHalfToo: 
            Input flag to indicate whether the other side of the solid is to be generated
        Slice(Autodesk.AutoCAD.DatabaseServices.Surface) -> void
            
            Autodesk.AutoCAD.DatabaseServices.Surface surface: 
            Input the surface entity to be used to slice the solid
        Slice(Autodesk.AutoCAD.DatabaseServices.Surface, [MarshalAs(UnmanagedType.U1)] bool) -> Solid3d
            
            Autodesk.AutoCAD.DatabaseServices.Surface surface: 
            Input the surface entity to be used to slice the solid
            
            [MarshalAs(UnmanagedType.U1)] bool negativeHalfToo: 
            Input flag to indicate whether the other side of the solid is to be generated
        """
        pass
    
    
    def StlOut(self):
        """
        StlOut -> void
            
            string fileName: 
            Input file name
            
            [MarshalAs(UnmanagedType.U1)] bool asciiFormat: 
            Input Boolean indicating file format
        """
        pass
    
    
    def TaperFaces(self):
        """
        TaperFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be tapered
            
            Point3d basePoint: 
            Input origin of the draft plane
            
            Vector3d draftVector: 
            Input draft direction vector
            
            double draftAngle: 
            Input draft angle
        """
        pass
    
    
    def TransformFaces(self):
        """
        TransformFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be transformed
            
            Matrix3d matrix: 
            Input rotation and/or translation matrix to be applied to the faces
        """
        pass
    
    
    Area = None
    
    
    IsNull = None
    
    
    MassProperties = None
    
    
    NumChanges = None
    
    
    RecordHistory = None
    
    
    ShowHistory = None
    
    
    UsesGraphicsCache = None
    
    pass

class Solid3dMassProperties(public struct Solid3dMassProperties {
}):
    """
    
    S
    
    o
    
    l
    
    i
    
    d
    
    3
    
    d
    
    M
    
    a
    
    s
    
    s
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    i
    
    e
    
    s
    
    (
    
    )
    """
    Centroid = None
    
    
    Extents = None
    
    
    MomentsOfIntertia = None
    
    
    PrincipalMoments = None
    
    
    ProductsOfIntertia = None
    
    
    RadiiOfGyration = None
    
    
    Volume = None
    
    pass

class SolidBackground(Background):
    """
    
    S
    
    o
    
    l
    
    i
    
    d
    
    B
    
    a
    
    c
    
    k
    
    g
    
    r
    
    o
    
    u
    
    n
    
    d
    
    (
    
    )
    """
    Color = None
    
    pass

  SourceNotDefined
  InventorSource
  FusionSource
  ModelSpaceSource

class Spline(Curve):
    """
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    :
    
     
    
    C
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    t
    
    i
    
    c
    
    a
    
    l
    
     
    
    a
    
    r
    
    c
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    u
    
    n
    
    i
    
    t
    
    N
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    :
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    r
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    t
    
    i
    
    c
    
    a
    
    l
    
     
    
    a
    
    r
    
    c
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
    A
    
    x
    
    i
    
    s
    
     
    
    :
    
     
    
    M
    
    a
    
    j
    
    o
    
    r
    
     
    
    a
    
    x
    
    i
    
    s
    
     
    
    v
    
    e
    
    c
    
    t
    
    o
    
    r
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    t
    
    i
    
    c
    
    a
    
    l
    
     
    
    a
    
    r
    
    c
    
    ,
    
     
    
    m
    
    e
    
    a
    
    s
    
    u
    
    r
    
    e
    
    d
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
     
    
    c
    
    e
    
    n
    
    t
    
    e
    
    r
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    s
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    r
    
    a
    
    d
    
    i
    
    u
    
    s
    
    R
    
    a
    
    t
    
    i
    
    o
    
     
    
    :
    
     
    
    R
    
    a
    
    t
    
    i
    
    o
    
     
    
    o
    
    f
    
     
    
    m
    
    i
    
    n
    
    o
    
    r
    
     
    
    o
    
    r
    
     
    
    m
    
    a
    
    j
    
    o
    
    r
    
     
    
    a
    
    x
    
    i
    
    s
    
     
    
    l
    
    e
    
    n
    
    g
    
    t
    
    h
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    (
    
    i
    
    n
    
     
    
    r
    
    a
    
    d
    
    i
    
    a
    
    n
    
    s
    
    )
    
     
    
    o
    
    f
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    t
    
    i
    
    c
    
    a
    
    l
    
     
    
    a
    
    r
    
    c
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    e
    
    n
    
    d
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    :
    
     
    
    A
    
    n
    
    g
    
    l
    
    e
    
     
    
    (
    
    i
    
    n
    
     
    
    r
    
    a
    
    d
    
    i
    
    a
    
    n
    
    s
    
    )
    
     
    
    o
    
    f
    
     
    
    e
    
    n
    
    d
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    e
    
    l
    
    l
    
    i
    
    p
    
    t
    
    i
    
    c
    
    a
    
    l
    
     
    
    a
    
    r
    
    c
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    K
    
    n
    
    o
    
    t
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    n
    
    u
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    K
    
    n
    
    o
    
    t
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    n
    
    u
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    o
    
    i
    
    n
    
    t
    
     
    
    :
    
     
    
    A
    
    r
    
    r
    
    a
    
    y
    
     
    
    o
    
    f
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    t
    
    h
    
    r
    
    o
    
    u
    
    g
    
    h
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    f
    
    i
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
    T
    
    a
    
    n
    
    g
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    a
    
    n
    
    g
    
    e
    
    n
    
    t
    
     
    
    a
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    c
    
    t
    
    o
    
    r
    
    3
    
    d
    
     
    
    e
    
    n
    
    d
    
    T
    
    a
    
    n
    
    g
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    a
    
    n
    
    g
    
    e
    
    n
    
    t
    
     
    
    a
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    o
    
    r
    
    d
    
    e
    
    r
    
     
    
    :
    
     
    
    O
    
    r
    
    d
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    d
    
     
    
    (
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    a
    
    n
    
    g
    
    e
    
     
    
    2
    
     
    
    t
    
    o
    
     
    
    2
    
    6
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    f
    
    i
    
    t
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    :
    
     
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    a
    
    p
    
    p
    
    r
    
    o
    
    x
    
    i
    
    m
    
    a
    
    t
    
    e
    
     
    
    f
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
    K
    
    n
    
    o
    
    t
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    n
    
    u
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
     
    
    f
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    :
    
     
    
    A
    
    r
    
    r
    
    a
    
    y
    
     
    
    o
    
    f
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    t
    
    h
    
    r
    
    o
    
    u
    
    g
    
    h
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    f
    
    i
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    i
    
    s
    
    P
    
    e
    
    r
    
    i
    
    o
    
    d
    
    i
    
    c
    
     
    
    :
    
     
    
    I
    
    n
    
    d
    
    i
    
    c
    
    a
    
    t
    
    e
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    a
    
     
    
    p
    
    e
    
    r
    
    i
    
    o
    
    d
    
    i
    
    c
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    f
    
    i
    
    t
    
    t
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
     
    
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
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    K
    
    n
    
    o
    
    t
    
    P
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    n
    
    u
    
    m
    
     
    
    k
    
    n
    
    o
    
    t
    
    P
    
    a
    
    r
    
    a
    
    m
    
     
    
    :
    
     
    
    K
    
    n
    
    o
    
    t
    
     
    
    p
    
    a
    
    r
    
    a
    
    m
    
    e
    
    t
    
    e
    
    r
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    d
    
    e
    
    f
    
    i
    
    n
    
    i
    
    n
    
    g
    
     
    
    t
    
    h
    
    e
    
     
    
    k
    
    n
    
    o
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    s
    
     
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    d
    
    e
    
    g
    
    r
    
    e
    
    e
    
     
    
    :
    
     
    
    D
    
    e
    
    g
    
    r
    
    e
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    d
    
     
    
    (
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    a
    
    n
    
    g
    
    e
    
     
    
    1
    
     
    
    t
    
    o
    
     
    
    1
    
    1
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    f
    
    i
    
    t
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    :
    
     
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    a
    
    p
    
    p
    
    r
    
    o
    
    x
    
    i
    
    m
    
    a
    
    t
    
    e
    
     
    
    f
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    o
    
    i
    
    n
    
    t
    
     
    
    :
    
     
    
    A
    
    r
    
    r
    
    a
    
    y
    
     
    
    o
    
    f
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    t
    
    h
    
    r
    
    o
    
    u
    
    g
    
    h
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    f
    
    i
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    o
    
    r
    
    d
    
    e
    
    r
    
     
    
    :
    
     
    
    O
    
    r
    
    d
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    d
    
     
    
    (
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    a
    
    n
    
    g
    
    e
    
     
    
    2
    
     
    
    t
    
    o
    
     
    
    2
    
    6
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    f
    
    i
    
    t
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    :
    
     
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    a
    
    p
    
    p
    
    r
    
    o
    
    x
    
    i
    
    m
    
    a
    
    t
    
    e
    
     
    
    f
    
    i
    
    t
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
    
    
    
    
    
    
    
    
    
    S
    
    p
    
    l
    
    i
    
    n
    
    e
    
    (
    
    i
    
    n
    
    t
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
    ,
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
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
    
    ,
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
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
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    d
    
    e
    
    g
    
    r
    
    e
    
    e
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    d
    
    e
    
    g
    
    r
    
    e
    
    e
    
     
    
    o
    
    f
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    r
    
    a
    
    t
    
    i
    
    o
    
    n
    
    a
    
    l
    
     
    
    :
    
     
    
    T
    
    r
    
    u
    
    e
    
     
    
    i
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    r
    
    a
    
    t
    
    i
    
    o
    
    n
    
    a
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    c
    
    l
    
    o
    
    s
    
    e
    
    d
    
     
    
    :
    
     
    
    T
    
    r
    
    u
    
    e
    
     
    
    i
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    c
    
    l
    
    o
    
    s
    
    e
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    p
    
    e
    
    r
    
    i
    
    o
    
    d
    
    i
    
    c
    
     
    
    :
    
     
    
    T
    
    r
    
    u
    
    e
    
     
    
    i
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
     
    
    i
    
    s
    
     
    
    p
    
    e
    
    r
    
    i
    
    o
    
    d
    
    i
    
    c
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
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
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    P
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    (
    
    i
    
    n
    
     
    
    W
    
    C
    
    S
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
    )
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
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
    
     
    
    k
    
    n
    
    o
    
    t
    
    s
    
     
    
    :
    
     
    
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
    
     
    
    o
    
    f
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    s
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    k
    
    n
    
    o
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
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
    
     
    
    w
    
    e
    
    i
    
    g
    
    h
    
    t
    
    s
    
     
    
    :
    
     
    
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
    
     
    
    o
    
    f
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    s
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    w
    
    e
    
    i
    
    g
    
    h
    
    t
    
    s
    
     
    
    a
    
    t
    
     
    
    e
    
    a
    
    c
    
    h
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    P
    
    o
    
    i
    
    n
    
    t
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
    s
    
     
    
    t
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    o
    
    f
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    k
    
    n
    
    o
    
    t
    
    T
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    k
    
    n
    
    o
    
    t
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    t
    
    o
    
    l
    
    e
    
    r
    
    a
    
    n
    
    c
    
    e
    
     
    
    o
    
    f
    
     
    
    s
    
    p
    
    l
    
    i
    
    n
    
    e
    """
    def ElevateDegree(self):
        """
        ElevateDegree -> void
            
            int newDegree: 
            Input new spline degree value (in the range (existing degree) to 25)
        """
        pass
    
    
    def GetControlPointAt(self):
        """
        GetControlPointAt -> Point3d
            
            int index: 
            Input index (0 based) of point to get
        """
        pass
    
    
    def GetFitPointAt(self):
        """
        GetFitPointAt -> Point3d
            
            int index: 
            Input index (0 based) value
        """
        pass
    
    
    def InsertControlPointAt(self):
        """
        InsertControlPointAt -> Autodesk.AutoCAD.Runtime.ErrorStatus
        
        """
        pass
    
    
    def InsertFitPointAt(self):
        """
        InsertFitPointAt -> void
            
            int index: 
            Input index (0 based) where new fit point is to be inserted
            
            Point3d point: 
            Input new fit point (in WCS coordinates)
        """
        pass
    
    
    def InsertKnot(self):
        """
        InsertKnot -> void
            
            double value: 
            Input parameter where knot is to be added
        """
        pass
    
    
    def ModifyPositionAndTangent(self):
        """
        ModifyPositionAndTangent -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            double param: 
            Parameter
            
            Point3d point: 
            Specify the new location of the point on the spline curve
            
            Vector3d deriv: 
            Specify the tangent vector
        """
        pass
    
    
    def PurgeFitData(self):
        """
        PurgeFitData -> void
        
        """
        pass
    
    
    def Rebuild(self):
        """
        Rebuild -> Autodesk.AutoCAD.Runtime.ErrorStatus
        
        """
        pass
    
    
    def RemoveControlPointAt(self):
        """
        RemoveControlPointAt -> Autodesk.AutoCAD.Runtime.ErrorStatus
        
        """
        pass
    
    
    def RemoveFitPointAt(self):
        """
        RemoveFitPointAt -> void
            
            int index: 
            Index (0 based) of fit point to be removed
        """
        pass
    
    
    def SetControlPointAt(self):
        """
        SetControlPointAt -> void
            
            int index: 
            Input index (0 based) of control point to replace
            
            Point3d point: 
            Input new control point (in WCS coordinates)
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> void
            
            int index: 
            Input index (0 based) of fit point to replace
            
            Point3d point: 
            Input new fit point (in WCS coordinates)
        """
        pass
    
    
    def SetWeightAt(self):
        """
        SetWeightAt -> void
            
            int index: 
            Input index (0 based) of control point at which to change the weight
            
            double weight: 
            Input new weight value
        """
        pass
    
    
    def ToPolyline(self):
        """
        ToPolyline() -> Curve
        
        ToPolyline([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Curve
        
        ToPolyline(uint) -> Curve
            
            uint numOfVertices: 
            Target number of vertices. The resulting polyline will have vertices no more than this value.
        ToPolyline(uint, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Curve
        
        """
        pass
    
    
    def ToPolylineWithPrecision(self):
        """
        ToPolylineWithPrecision(int) -> Curve
            
            int precision: 
            Target precision
        ToPolylineWithPrecision(int, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Curve
        
        """
        pass
    
    
    def UpdateFitData(self):
        """
        UpdateFitData -> void
        
        """
        pass
    
    
    def WeightAt(self):
        """
        WeightAt -> double
            
            int index: 
            Input index (0 based) of control point
        """
        pass
    
    
    Degree = None
    
    
    EndFitTangent = None
    
    
    FitData = None
    
    
    FitTolerance = None
    
    
    HasFitData = None
    
    
    IsNull = None
    
    
    IsPlanar = None
    
    
    IsRational = None
    
    
    NumControlPoints = None
    
    
    NumFitPoints = None
    
    
    NurbsData = None
    
    
    StartFitTangent = None
    
    
    Type = None
    
    pass

  FitPoints
  ControlPoints

  CustomScale = 1
  Scale100To1 = 0x12
  Scale10To1 = 0x11
  Scale1ftAnd1ft = 0x22
  Scale1inAnd1ft = 30
  Scale1To1 = 2
  Scale1To10 = 7
  Scale1To100 = 13
  Scale1To128inAnd1ft = 0x13
  Scale1To16 = 8
  Scale1To16inchAnd1ft = 0x16
  Scale1To2 = 3
  Scale1To20 = 9
  Scale1To2inchAnd1ft = 0x1c
  Scale1To30 = 10
  Scale1To32inchAnd1ft = 0x15
  Scale1To4 = 4
  Scale1To40 = 11
  Scale1To4inchAnd1ft = 0x1a
  Scale1To5 = 5
  Scale1To50 = 12
  Scale1To64inchAnd1ft = 20
  Scale1To8 = 6
  Scale1To8inchAnd1ft = 0x18
  Scale2To1 = 14
  Scale3inAnd1ft = 0x20
  Scale3To16inchAnd1ft = 0x19
  Scale3To32inchAnd1ft = 0x17
  Scale3To4inchAnd1ft = 0x1d
  Scale3To8inchAnd1ft = 0x1b
  Scale4To1 = 15
  Scale6inAnd1ft = 0x21
  Scale8To1 = 0x10
  ScaleToFit = 0

  ScaleToFit
  StdScale1To128InchIs1ft
  StdScale1To64InchIs1ft
  StdScale1To32InchIs1ft
  StdScale1To16InchIs1ft
  StdScale3To32InchIs1ft
  StdScale1To8InchIs1ft
  StdScale3To16InchIs1ft
  StdScale1To4InchIs1ft
  StdScale3To8InchIs1ft
  StdScale1To2InchIs1ft
  StdScale3To4InchIs1ft
  StdScale1InchIs1ft
  StdScale3InchIs1ft
  StdScale6InchIs1ft
  StdScale1ftIs1ft
  StdScale1To1
  StdScale1To2
  StdScale1To4
  StdScale1To5
  StdScale1To8
  StdScale1To10
  StdScale1To16
  StdScale1To20
  StdScale1To30
  StdScale1To40
  StdScale1To50
  StdScale1To100
  StdScale2To1
  StdScale4To1
  StdScale8To1
  StdScale10To1
  StdScale100To1
  StdScale1000To1

class SubDMesh(Entity):
    """
    
    """
    def Cap(self):
        """
        Cap -> void
        
        """
        pass
    
    
    def Collapse(self):
        """
        Collapse -> void
        
        """
        pass
    
    
    def ComputeSurfaceArea(self):
        """
        ComputeSurfaceArea -> double
        
        """
        pass
    
    
    def ComputeVolume(self):
        """
        ComputeVolume -> double
        
        """
        pass
    
    
    def ConvertToSolid(self):
        """
        ConvertToSolid -> Solid3d
        
        """
        pass
    
    
    def ConvertToSurface(self):
        """
        ConvertToSurface([MarshalAs(UnmanagedType.U1)] bool, SubentityId) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        ConvertToSurface([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        """
        pass
    
    
    def ExtrudeConnectedFaces(self):
        """
        ExtrudeConnectedFaces(FullSubentityPath[], Point3dCollection, double) -> void
        
        ExtrudeConnectedFaces(FullSubentityPath[], double, Vector3d, double) -> void
        
        """
        pass
    
    
    def ExtrudeFaces(self):
        """
        ExtrudeFaces(FullSubentityPath[], Point3dCollection, double) -> void
        
        ExtrudeFaces(FullSubentityPath[], double, Vector3d, double) -> void
        
        """
        pass
    
    
    def GetAdjacentSubentPath(self):
        """
        GetAdjacentSubentPath -> FullSubentityPath()
        
        """
        pass
    
    
    def GetCrease(self):
        """
        GetCrease(FullSubentityPath[]) -> DoubleCollection
        
        GetCrease(SubentityId) -> double
        
        """
        pass
    
    
    def GetFacePlane(self):
        """
        GetFacePlane -> Plane
        
        """
        pass
    
    
    def GetNumberOfSubDividedFacesAt(self):
        """
        GetNumberOfSubDividedFacesAt -> Integer
        
        """
        pass
    
    
    def GetObjectMesh(self):
        """
        GetObjectMesh -> MeshDataCollection
            
            DBObject dbObj: 
            Input object to get the mesh.
            
            MeshFaceterData faceterData: 
            Input faceter setting information.
        """
        pass
    
    
    def GetSubDividedVertexAt(self):
        """
        GetSubDividedVertexAt(SubentityId) -> Point3d
        
        GetSubDividedVertexAt(int) -> Point3d
        
        """
        pass
    
    
    def GetSubentColor(self):
        """
        GetSubentColor -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def GetSubentMaterial(self):
        """
        GetSubentMaterial -> ObjectId
        
        """
        pass
    
    
    def GetSubentMaterialMapper(self):
        """
        GetSubentMaterialMapper -> Mapper
        
        """
        pass
    
    
    def GetSubentPath(self):
        """
        GetSubentPath -> FullSubentityPath()
        
        """
        pass
    
    
    def GetVertexAt(self):
        """
        GetVertexAt(SubentityId) -> Point3d
        
        GetVertexAt(int) -> Point3d
        
        """
        pass
    
    
    def MergeFaces(self):
        """
        MergeFaces -> void
        
        """
        pass
    
    
    def Setbox(self):
        """
        Setbox -> void
        
        """
        pass
    
    
    def SetCone(self):
        """
        SetCone -> void
        
        """
        pass
    
    
    def SetCrease(self):
        """
        SetCrease(FullSubentityPath[], double) -> void
        
        SetCrease(double) -> void
        
        """
        pass
    
    
    def SetCylinder(self):
        """
        SetCylinder -> void
        
        """
        pass
    
    
    def SetDragStatus(self):
        """
        SetDragStatus -> void
            
            DragStatus status: 
            Value describing the status of the drag operation; one of the values from the DragStat enumeration
        """
        pass
    
    
    def SetPyramid(self):
        """
        SetPyramid -> void
        
        """
        pass
    
    
    def SetSphere(self):
        """
        SetSphere -> void
        
        """
        pass
    
    
    def SetSubDMesh(self):
        """
        SetSubDMesh -> void
        
        """
        pass
    
    
    def SetSubentColor(self):
        """
        SetSubentColor -> void
        
        """
        pass
    
    
    def SetSubentMaterial(self):
        """
        SetSubentMaterial -> void
        
        """
        pass
    
    
    def SetSubentMaterialMapper(self):
        """
        SetSubentMaterialMapper -> void
        
        """
        pass
    
    
    def SetTorus(self):
        """
        SetTorus -> void
        
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt(SubentityId, Point3d) -> void
        
        SetVertexAt(int, Point3d) -> void
        
        """
        pass
    
    
    def SetWedge(self):
        """
        SetWedge -> void
        
        """
        pass
    
    
    def Spin(self):
        """
        Spin -> void
        
        """
        pass
    
    
    def SplitFace(self):
        """
        SplitFace -> void
        
        """
        pass
    
    
    def SubdDivideDown(self):
        """
        SubdDivideDown -> void
        
        """
        pass
    
    
    def SubdDivideUp(self):
        """
        SubdDivideUp -> void
        
        """
        pass
    
    
    def SubdRefine(self):
        """
        SubdRefine() -> void
        
        SubdRefine(FullSubentityPath[]) -> void
        
        """
        pass
    
    
    FaceArray = None
    
    
    NormalArray = None
    
    
    NumberOfFaces = None
    
    
    NumberOfSubDividedFaces = None
    
    
    NumberOfSubDividedVertices = None
    
    
    NumberOfVertices = None
    
    
    SmoothLevel = None
    
    
    SubDividedFaceArray = None
    
    
    SubDividedNormalArray = None
    
    
    SubDividedVertices = None
    
    
    VertexColorArray = None
    
    
    VertexNormalArray = None
    
    
    VertexTextureArray = None
    
    
    Vertices = None
    
    
    Watertight = None
    
    pass

class SubentRef(GeomRef):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def CreateEntity(self):
        """
        CreateEntity -> Autodesk.AutoCAD.DatabaseServices.Entity
        
        """
        pass
    
    
    Entity = None
    
    
    SubentId = None
    
    pass

class SubentityGeometry(public class SubentityGeometry):
    """
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    (
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    r
    
    v
    
    e
    
    3
    
    d
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    v
    
    e
    
     
    
    i
    
    s
    
     
    
    n
    
    o
    
    t
    
     
    
    o
    
    w
    
    n
    
    e
    
    d
    
     
    
    b
    
    y
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    G
    
    e
    
    o
    
    m
    
    e
    
    t
    
    r
    
    y
    
    (
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    3
    
    d
    
     
    
    p
    
    n
    
    t
    
     
    
    :
    
     
    
    T
    
    h
    
    e
    
     
    
    c
    
    o
    
    o
    
    r
    
    d
    
    i
    
    n
    
    a
    
    t
    
    e
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    s
    
    u
    
    b
    
    e
    
    n
    
    t
    
    i
    
    t
    
    y
    
    .
    """
    Curve = None
    
    
    Point = None
    
    
    Type = None
    
    pass

class SubentityOverrule(Overrule):
    """
    
    """
    def AddSubentPaths(self):
        """
        AddSubentPaths -> void
        
        """
        pass
    
    
    def DeleteSubentPaths(self):
        """
        DeleteSubentPaths -> void
        
        """
        pass
    
    
    def GetCompoundObjectTransform(self):
        """
        GetCompoundObjectTransform -> Matrix3d
        
        """
        pass
    
    
    def GetGripPointsAtSubentPath(self):
        """
        GetGripPointsAtSubentPath -> void
        
        """
        pass
    
    
    def GetGsMarkersAtSubentPath(self):
        """
        GetGsMarkersAtSubentPath -> IntPtr()
        
        """
        pass
    
    
    def GetSubentClassId(self):
        """
        GetSubentClassId -> Guid
        
        """
        pass
    
    
    def GetSubentPathGeomExtents(self):
        """
        GetSubentPathGeomExtents -> Extents3d
        
        """
        pass
    
    
    def GetSubentPathsAtGsMarker(self):
        """
        GetSubentPathsAtGsMarker -> FullSubentityPath()
        
        """
        pass
    
    
    def MoveGripPointsAtSubentPaths(self):
        """
        MoveGripPointsAtSubentPaths -> void
        
        """
        pass
    
    
    def OnSubentGripStatusChanged(self):
        """
        OnSubentGripStatusChanged -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def SubentPtr(self):
        """
        SubentPtr -> Entity
        
        """
        pass
    
    
    def TransformSubentPathsBy(self):
        """
        TransformSubentPathsBy -> void
        
        """
        pass
    
    pass

  Null
  Face
  Edge
  Vertex
  MlineCache
  Class

class Sun(DBObject):
    """
    
    S
    
    u
    
    n
    
    (
    
    )
    """
    Altitude = None
    
    
    Azimuth = None
    
    
    DateTime = None
    
    
    Intensity = None
    
    
    IsDaylightSavingsOn = None
    
    
    IsOn = None
    
    
    ShadowParameters = None
    
    
    SkyParameters = None
    
    
    SunColor = None
    
    
    SunDirection = None
    
    pass

class Surface(Entity):
    """
    
    """
      Isolines
      IsoParms
    
    
    def ChamferEdges(self):
        """
        ChamferEdges(SubentityId[], SubentityId, double, double) -> void
        
        ChamferEdges(SubentityId[], SubentityId, double, double, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def SliceBySurface(self):
        """
        SliceBySurface -> SurfaceSliceResults
        
        """
        pass
    
    
    def ConvertToNurbSurface(self):
        """
        ConvertToNurbSurface -> Autodesk.AutoCAD.DatabaseServices.NurbSurface()
        
        """
        pass
    
    
    def CreateBlendSurface(self):
        """
        CreateBlendSurface(LoftProfile, LoftProfile, BlendOptions) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateBlendSurface(LoftProfile, LoftProfile, BlendOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateExtendSurface(self):
        """
        CreateExtendSurface -> ObjectId
        
        """
        pass
    
    
    def CreateExtrudedSurface(self):
        """
        CreateExtrudedSurface(Profile3d, Vector3d, SweepOptions) -> ExtrudedSurface
        
        CreateExtrudedSurface(Profile3d, Vector3d, SweepOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateFilletSurface(self):
        """
        CreateFilletSurface(ObjectId, Point3d, ObjectId, Point3d, double, Autodesk.AutoCAD.DatabaseServices.FilletTrimMode, Vector3d) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateFilletSurface(ObjectId, Point3d, ObjectId, Point3d, double, Autodesk.AutoCAD.DatabaseServices.FilletTrimMode, Vector3d, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateInterferenceObjects(self):
        """
        CreateInterferenceObjects -> Entity()
        
        """
        pass
    
    
    def CreateLoftedSurface(self):
        """
        CreateLoftedSurface(LoftProfile[], LoftProfile[], LoftProfile, LoftOptions) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateLoftedSurface(LoftProfile[], LoftProfile[], LoftProfile, LoftOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateNetworkSurface(self):
        """
        CreateNetworkSurface(Profile3d[], Profile3d[]) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateNetworkSurface(Profile3d[], Profile3d[], [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateOffsetSurface(self):
        """
        CreateOffsetSurface(Entity, double) -> Entity
        
        CreateOffsetSurface(Entity, double, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreatePatchSurface(self):
        """
        CreatePatchSurface(PathRef, ObjectIdCollection, int, double) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreatePatchSurface(PathRef, ObjectIdCollection, int, double, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateRevolvedSurface(self):
        """
        CreateRevolvedSurface(Profile3d, Point3d, Vector3d, double, double, RevolveOptions) -> RevolvedSurface
        
        CreateRevolvedSurface(Profile3d, Point3d, Vector3d, double, double, RevolveOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        CreateRevolvedSurface(Profile3d, Profile3d, [MarshalAs(UnmanagedType.U1)] bool, double, double, RevolveOptions) -> RevolvedSurface
        
        CreateRevolvedSurface(Profile3d, Profile3d, [MarshalAs(UnmanagedType.U1)] bool, double, double, RevolveOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateSectionObjects(self):
        """
        CreateSectionObjects -> Entity()
        
        """
        pass
    
    
    def CreateSweptSurface(self):
        """
        CreateSweptSurface(Profile3d, Profile3d, SweepOptions) -> SweptSurface
        
        CreateSweptSurface(Profile3d, Profile3d, SweepOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def ExtendEdges(self):
        """
        ExtendEdges -> void
        
        """
        pass
    
    
    def FilletEdges(self):
        """
        FilletEdges(SubentityId[], DoubleCollection, DoubleCollection, DoubleCollection) -> void
        
        FilletEdges(SubentityId[], double, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def GetSubentityColor(self):
        """
        GetSubentityColor -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def GetSubentityMaterial(self):
        """
        GetSubentityMaterial -> ObjectId
        
        """
        pass
    
    
    def GetSubentityMaterialMapper(self):
        """
        GetSubentityMaterialMapper -> Mapper
        
        """
        pass
    
    
    def ImprintEntity(self):
        """
        ImprintEntity -> void
        
        """
        pass
    
    
    def ProjectOnToSurface(self):
        """
        ProjectOnToSurface -> Entity()
        
        """
        pass
    
    
    def RayTest(self):
        """
        RayTest -> void
        
        """
        pass
    
    
    def SetSubentityColor(self):
        """
        SetSubentityColor -> void
        
        """
        pass
    
    
    def SetSubentityMaterial(self):
        """
        SetSubentityMaterial -> void
        
        """
        pass
    
    
    def SetSubentityMaterialMapper(self):
        """
        SetSubentityMaterialMapper -> void
        
        """
        pass
    
    
    def SliceByPlane(self):
        """
        SliceByPlane -> SurfaceSliceResults
        
        """
        pass
    
    
    def TrimSurface(self):
        """
        TrimSurface -> void
        
        """
        pass
    
    
    CreationActionBodyId = None
    
    
    ModificationActionBodyIds = None
    
    
    Perimeter = None
    
    
    UIsoLineDensity = None
    
    
    UsesGraphicsCache = None
    
    
    WireframeType = None
    
    pass

class SurfaceTrimInfo(DisposableWrapper):
    """
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    T
    
    r
    
    i
    
    m
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
      InsideTool
      OutsideTool
    
    
    def SetTrimInfo(self):
        """
        SetTrimInfo(CompoundObjectId, TrimRelation, SubentityId) -> void
        
        SetTrimInfo(CompoundObjectId, Vector3d, TrimRelation) -> void
        
        """
        pass
    
    
    IsCurve = None
    
    
    ProjVector = None
    
    
    Relation = None
    
    
    ToolBodyId = None
    
    pass

  NoAlignment
  AlignSweepEntityToPath
  TranslateSweepEntityToPath
  TranslatePathToSweepEntity

class SweptSurface(Surface):
    """
    
    S
    
    w
    
    e
    
    p
    
    t
    
    S
    
    u
    
    r
    
    f
    
    a
    
    c
    
    e
    
    (
    
    )
    """
    def CreateSweptSurface(self):
        """
        CreateSweptSurface -> void
            
            Entity sweepEnt: 
            Input the curve, region, or planar surface to be swept
            
            Entity pathEnt: 
            Input the curve entity that specifies the path along which sweepEnt is to be swept
            
            Autodesk.AutoCAD.DatabaseServices.SweepOptions sweepOptions: 
            Input sweep options
        """
        pass
    
    
    Bank = None
    
    
    PathEntity = None
    
    
    PathLength = None
    
    
    PathProfile = None
    
    
    ProfileRotation = None
    
    
    ScaleAlongPath = None
    
    
    SweepEntity = None
    
    
    SweepOptions = None
    
    
    SweepProfile = None
    
    
    TwistAlongPath = None
    
    pass

class SymbolTable(DBObject, IEnumerable):
    """
    
    """
    def Add(self):
        """
        Add -> ObjectId
            
            [CallerMustClose] SymbolTableRecord value: 
            Input record to add to the table
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> SymbolTableEnumerator
        
        """
        pass
    
    
    def Has(self):
        """
        Has(ObjectId) -> bool
            
            ObjectId id: 
            Input object ID of record to search for
        Has(string) -> bool
            
            string key: 
            Input name of record to search for
        """
        pass
    
    
    IncludingErased = None
    
    pass

class SymbolTableEnumerator(DisposableWrapper, IEnumerator):
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
    
    
    Current = None
    
    pass

class SymbolTableRecord(DBObject):
    """
    
    """
    IsDependent = None
    
    
    IsResolved = None
    
    
    Name = None
    
    pass

class SymbolUtilityServices(public sealed class SymbolUtilityServices):
    """
    
    """
    def GetBlockModelSpaceId(self):
        """
        GetBlockModelSpaceId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetBlockNameFromInsertPathName(self):
        """
        GetBlockNameFromInsertPathName -> string
            
            string pathName: 
            Input path name to examine
        """
        pass
    
    
    def GetBlockPaperSpaceId(self):
        """
        GetBlockPaperSpaceId -> ObjectId
            
            Database databasePointer: 
            Input pointer to database to access
        """
        pass
    
    
    def GetInsertPathNameFromBlockName(self):
        """
        GetInsertPathNameFromBlockName -> string
            
            string blockName: 
            Input name of block from which to get the path
        """
        pass
    
    
    def GetLayerDefpointsId(self):
        """
        GetLayerDefpointsId -> ObjectId
            
            Database database: 
            Input database to access
        """
        pass
    
    
    def GetLayerZeroId(self):
        """
        GetLayerZeroId -> ObjectId
            
            Database database: 
            Input database to access
        """
        pass
    
    
    def GetLinetypeByBlockId(self):
        """
        GetLinetypeByBlockId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetLinetypeByLayerId(self):
        """
        GetLinetypeByLayerId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetLinetypeContinuousId(self):
        """
        GetLinetypeContinuousId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetMaxSymbolNameLength(self):
        """
        GetMaxSymbolNameLength -> Integer
            
            [MarshalAs(UnmanagedType.U1)] bool isNewName: 
            Input Boolean to indicate whether we want to the length for extended or legacy symbol names
            
            [MarshalAs(UnmanagedType.U1)] bool compatibilityMode: 
            Input Boolean to indicate extended or legacy symbol names
            
            false: 
            max=31
            
            true: 
            max=31
        """
        pass
    
    
    def GetPathNameFromSymbolName(self):
        """
        GetPathNameFromSymbolName -> string
            
            string symbolName: 
            Input name of block from which to get the path
            
            string extensions: 
            Input list of extensions for which to search
        """
        pass
    
    
    def GetRegAppAcadId(self):
        """
        GetRegAppAcadId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetSymbolNameFromPathName(self):
        """
        GetSymbolNameFromPathName -> string
            
            string pathName: 
            Input path name
            
            string extensions: 
            Input list of extensions to consider
        """
        pass
    
    
    def GetTextStyleStandardId(self):
        """
        GetTextStyleStandardId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def IsBlockLayoutName(self):
        """
        IsBlockLayoutName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsBlockModelSpaceName(self):
        """
        IsBlockModelSpaceName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsBlockPaperSpaceName(self):
        """
        IsBlockPaperSpaceName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsCompatibilityMode(self):
        """
        IsCompatibilityMode -> bool
            
            Database database: 
            Input database to access
        """
        pass
    
    
    def IsLayerDefpointsName(self):
        """
        IsLayerDefpointsName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLayerZeroName(self):
        """
        IsLayerZeroName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLinetypeByBlockName(self):
        """
        IsLinetypeByBlockName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLinetypeByLayerName(self):
        """
        IsLinetypeByLayerName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLinetypeContinuousName(self):
        """
        IsLinetypeContinuousName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsRegAppAcadName(self):
        """
        IsRegAppAcadName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsTextStyleStandardName(self):
        """
        IsTextStyleStandardName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsViewportActiveName(self):
        """
        IsViewportActiveName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def MakeDependentName(self):
        """
        MakeDependentName -> string
            
            string dwgName: 
            Input the drawing name
            
            string symbolName: 
            Input the symbol name
        """
        pass
    
    
    def PreValidateSymbolName(self):
        """
        PreValidateSymbolName -> string
            
            [MarshalAs(UnmanagedType.U1)] bool preserveCase: 
            Input Boolean to indicate whether to preserve the case of alphabetic letters
        """
        pass
    
    
    def RepairPreExtendedSymbolName(self):
        """
        RepairPreExtendedSymbolName -> string
            
            string oldName: 
            Input symbol name to repair
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate is vertical bars are allowed in the symbol name
        """
        pass
    
    
    def RepairSymbolName(self):
        """
        RepairSymbolName -> string
            
            string oldName: 
            Input symbol name to repair
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate if vertical bars are allowed in the symbol name
        """
        pass
    
    
    def ValidateCompatibleSymbolName(self):
        """
        ValidateCompatibleSymbolName -> ErrorStatus
            
            string name: 
            Input name to validate
            
            [MarshalAs(UnmanagedType.U1)] bool isNewName: 
            Input Boolean to indicate whether to treat the name as a new or an existing name
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate whether to allow vertical bars in the name
            
            [MarshalAs(UnmanagedType.U1)] bool compatibilityMode: 
            Input Boolean to indicate whether the validate the name as an extended or legacy symbol name
        """
        pass
    
    
    def ValidatePreExtendedSymbolName(self):
        """
        ValidatePreExtendedSymbolName -> void
            
            string name: 
            Input name to validate
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate if vertical bars are valid in the symbol name
        """
        pass
    
    
    def ValidateSymbolName(self):
        """
        ValidateSymbolName -> void
            
            string name: 
            Input name to validate
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate if vertical bars are valid in the symbol name
        """
        pass
    
    
    BlockModelSpaceName = None
    
    
    BlockPaperSpaceName = None
    
    
    LayerDefpointsName = None
    
    
    LayerZeroName = None
    
    
    LinetypeByBlockName = None
    
    
    LinetypeByLayerName = None
    
    
    LinetypeContinuousName = None
    
    
    RegAppAcadName = None
    
    
    TextStyleStandardName = None
    
    
    ViewportActiveName = None
    
    pass

class SymmetricConstraint(GeometricalConstraint):
    """
    
    S
    
    y
    
    m
    
    m
    
    e
    
    t
    
    r
    
    i
    
    c
    
    C
    
    o
    
    n
    
    s
    
    t
    
    r
    
    a
    
    i
    
    n
    
    t
    
    (
    
    )
    """

    pass

class Table(BlockReference, IEnumerable):
    """
    
    T
    
    a
    
    b
    
    l
    
    e
    
    (
    
    )
    """
    def Alignment(self):
        """
        Alignment(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which the cell alignment value will be returned
        Alignment(int, int) -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def AttachmentPoint(self):
        """
        AttachmentPoint -> Point3d
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BackgroundColor(self):
        """
        BackgroundColor(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which the Color value is returned
        BackgroundColor(int, int) -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BlockRotation(self):
        """
        BlockRotation -> double
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BlockScale(self):
        """
        BlockScale -> double
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BlockTableRecordId(self):
        """
        BlockTableRecordId -> ObjectId
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def CanDeleteColumns(self):
        """
        CanDeleteColumns -> bool
            
            int index: 
            Input System.Int32 object to check if a column can be deleted.
            
            int nCount: 
            Input number of columns to delete
        """
        pass
    
    
    def CanDeleteRows(self):
        """
        CanDeleteRows -> bool
            
            int index: 
            Input System.Int32 object to check if a row can be deleted.
            
            int nCount: 
            Input number of rows to delete
        """
        pass
    
    
    def CanInsertColumn(self):
        """
        CanInsertColumn -> bool
            
            int index: 
            Input System.Int32 object to check if new column can be inserted.
        """
        pass
    
    
    def CanInsertRow(self):
        """
        CanInsertRow -> bool
            
            int index: 
            Input System.Int32 object to check if new row can be inserted.
        """
        pass
    
    
    def CellStyleOverrides(self):
        """
        CellStyleOverrides -> TableStyleOverride()
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def CellType(self):
        """
        CellType -> TableCellType
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def ClearSubSelection(self):
        """
        ClearSubSelection -> void
        
        """
        pass
    
    
    def ClearTableStyleOverrides(self):
        """
        ClearTableStyleOverrides -> void
            
            int options: 
            Input System.Int32 object.
        """
        pass
    
    
    def ColumnWidth(self):
        """
        ColumnWidth -> double
            
            int col: 
            Input zero-based column index
        """
        pass
    
    
    def ContentColor(self):
        """
        ContentColor(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input Autodesk.AutoCAD.DatabaseServices.RowType object specifying the row type for which the Color value will be returned
        ContentColor(int, int) -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom(LinkedTableData, TableCopyOptions) -> void
            
            LinkedTableData source: 
            Input source table
            
            TableCopyOptions options: 
            Input copy option
        CopyFrom(LinkedTableData, TableCopyOptions, CellRange, CellRange) -> CellRange
            
            LinkedTableData source: 
            Input source table
            
            TableCopyOptions options: 
            Input copy option
            
            CellRange sourceRange: 
            Input source cell range
            
            CellRange targetRange: 
            Input target cell range
        CopyFrom(Table, TableCopyOptions, CellRange, CellRange) -> CellRange
            
            Table source: 
            Input table source
            
            TableCopyOptions options: 
            Input table copy options
            
            CellRange sourceRange: 
            Input source cell range
            
            CellRange targetRange: 
            Input target cell range
        """
        pass
    
    
    def CreateContent(self):
        """
        CreateContent -> Integer
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def DataType(self):
        """
        DataType(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input Autodesk.AutoCAD.DatabaseServices.RowType object specifying the data type
        DataType(int, int) -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def DeleteCellContent(self):
        """
        DeleteCellContent -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def DeleteColumns(self):
        """
        DeleteColumns -> void
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            int columns: 
            Input System.Int32 object number of columns to delete
        """
        pass
    
    
    def DeleteContent(self):
        """
        DeleteContent(CellRange) -> void
            
            range: 
            Input range of cells to delete the contents
        DeleteContent(int, int) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        DeleteContent(int, int, int) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of row.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def DeleteRows(self):
        """
        DeleteRows -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int rows: 
            Input System.Int32 object number of rows to delete
        """
        pass
    
    
    def FieldId(self):
        """
        FieldId -> ObjectId
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def Fill(self):
        """
        Fill -> void
            
            CellRange fillRange: 
            Input Autodesk.AutoCAD.DatabaseServices.CellRange object. Range to be filled. This shouldn't overlap the source range except when this range is to be cleared instead of filled in which case this range should be contained fully in source range.
            
            CellRange sourceRange: 
            Input Autodesk.AutoCAD.DatabaseServices.CellRange object. Source range to copy or use as pattern. This can be set to invalid range if the fill range is to be cleared.
            
            TableFillOptions options: 
            Input table copy options
        """
        pass
    
    
    def Format(self):
        """
        Format(Autodesk.AutoCAD.DatabaseServices.RowType) -> string
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input cell format type
        Format(int, int) -> string
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def GenerateLayout(self):
        """
        GenerateLayout -> void
        
        """
        pass
    
    
    def GetBlockAttributeValue(self):
        """
        GetBlockAttributeValue(int, int, ObjectId) -> string
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            ObjectId attributeDefinitionId: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object.
        GetBlockAttributeValue(int, int, int, ObjectId) -> string
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int column: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            ObjectId attDefId: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object.
        """
        pass
    
    
    def GetBlockTableRecordId(self):
        """
        GetBlockTableRecordId -> ObjectId
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int column: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetBreakHeight(self):
        """
        GetBreakHeight -> double
            
            int index: 
            Input table index. It should be more than or equal to 0 and less than the number of multiple tables, when the table breaks.
        """
        pass
    
    
    def GetBreakOffset(self):
        """
        GetBreakOffset -> Vector3d
            
            int index: 
            Input table index. It should be more than or equal to 0 and less than the number of multiple tables, when the table breaks.
        """
        pass
    
    
    def GetBreakSpacing(self):
        """
        GetBreakSpacing -> double
        
        """
        pass
    
    
    def GetCellExtents(self):
        """
        GetCellExtents -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            [MarshalAs(UnmanagedType.U1)] bool isOuterCell: 
            Output System.Boolean object indicating whether the specified cell is an outer cell
            
            Point3dCollection pts: 
            Output Autodesk.AutoCAD.Geometry.Point3dCollection object; point collection containing the cell extents information
        """
        pass
    
    
    def GetCellState(self):
        """
        GetCellState -> CellStates
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetCellStyle(self):
        """
        GetCellStyle -> string
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
        """
        pass
    
    
    def GetColumnName(self):
        """
        GetColumnName -> string
            
            int index: 
            Input zero based index of the column
        """
        pass
    
    
    def GetContentColor(self):
        """
        GetContentColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetContentLayout(self):
        """
        GetContentLayout -> Autodesk.AutoCAD.DatabaseServices.CellContentLayout
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetContentTypes(self):
        """
        GetContentTypes(int, int) -> CellContentTypes
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        GetContentTypes(int, int, int) -> CellContentTypes
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetCustomData(self):
        """
        GetCustomData(int, int) -> Integer
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
        GetCustomData(int, int, string) -> object
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            string key: 
            Input key to store the custom data
        """
        pass
    
    
    def GetDataFormat(self):
        """
        GetDataFormat(int, int) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        GetDataFormat(int, int, int) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetDataLink(self):
        """
        GetDataLink() -> ObjectIdCollection
        
        GetDataLink(CellRange) -> ObjectIdCollection
            
            CellRange range: 
            Input range to get the data links. If this is NULL it gets all the data links in the table.
        GetDataLink(int, int) -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetDataLinkRange(self):
        """
        GetDataLinkRange -> CellRange
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetDataType(self):
        """
        GetDataType -> DataTypeParameter
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TableEnumerator
        
        GetEnumerator(CellRange, TableEnumeratorOption) -> TableEnumerator
            
            CellRange range: 
            Input range of cells to delete the contents
            
            TableEnumeratorOption option: 
            Input enumerator option
        """
        pass
    
    
    def GetFieldId(self):
        """
        GetFieldId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetFormula(self):
        """
        GetFormula -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetIsAutoScale(self):
        """
        GetIsAutoScale -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetMargin(self):
        """
        GetMargin -> double
            
            int row: 
            Input row index. Pass the value -1 if you are only concerned with the column.
            
            int column: 
            Input row index. Pass the value -1 if you are only concerned with the row.
            
            CellMargins margin: 
            Input margin type to get
        """
        pass
    
    
    def GetMergeAllEnabled(self):
        """
        GetMergeAllEnabled -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetMergeRange(self):
        """
        GetMergeRange -> CellRange
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetNumberOfContents(self):
        """
        GetNumberOfContents -> Integer
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetOverrides(self):
        """
        GetOverrides(int, int, int) -> CellProperties
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            int contentIndex: 
            Input content index.
        GetOverrides(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType) -> CellProperties
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type
        """
        pass
    
    
    def GetRotation(self):
        """
        GetRotation -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetScale(self):
        """
        GetScale -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetTextHeight(self):
        """
        GetTextHeight -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetTextString(self):
        """
        GetTextString(int, int, int) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents
        GetTextString(int, int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption formatOption: 
            Input null-terminated text string
        """
        pass
    
    
    def GetTextStyleId(self):
        """
        GetTextStyleId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetToolTip(self):
        """
        GetToolTip -> string
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue(int, int, int) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        GetValue(int, int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption formatOption: 
            Input Autodesk.AutoCAD.DatabaseServices.FormatOption object; format option
        """
        pass
    
    
    def GridColor(self):
        """
        GridColor(int, int, CellEdgeMasks) -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input object specifying the zero-based row index for the cell
            
            int col: 
            Input object specifying the zero-based column index for the cell
            
            CellEdgeMasks edge: 
            Input object specifying the edge index for the cell
        GridColor(Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridlineType: 
            Input grid line type for which to return the Color value
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which to return the Color value
        """
        pass
    
    
    def GridLineWeight(self):
        """
        GridLineWeight(int, int, CellEdgeMasks) -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int row: 
            Input row index. This can be -1.
            
            int col: 
            Input column index. This can be -1.
            
            CellEdgeMasks edge: 
            Input integer specifying the edge index for the cell
        GridLineWeight(Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridlineType: 
            To specify cell pass a valid row and column indices; to specify row pass a valid row index and pass -1 as column index; to specify column pass a valid column index and pass -1 as row index.
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type.
        """
        pass
    
    
    def GridVisibility(self):
        """
        GridVisibility(int, int, CellEdgeMasks) -> bool
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            CellEdgeMasks edge: 
            Input specifying the edge index for the cell
        GridVisibility(Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.RowType) -> bool
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridlineType: 
            Input grid line type for which to return the grid visibility
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which to return the grid visibility
        """
        pass
    
    
    def HasFormula(self):
        """
        HasFormula -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def HitTest(self):
        """
        HitTest -> TableHitTestInfo
            
            Point3d point: 
            Input 3D point in WCS specifying the input picking point
            
            Vector3d viewVector: 
            Input 3D vector in WCS specifying the view direction for the hit test
        """
        pass
    
    
    def InsertColumns(self):
        """
        InsertColumns -> void
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            double width: 
            Input width for the inserted columns
            
            int columns: 
            Input number of columns to insert
        """
        pass
    
    
    def InsertColumnsAndInherit(self):
        """
        InsertColumnsAndInherit -> void
            
            int col: 
            Input index at which to insert the new columns
            
            int inheritFrom: 
            Input index of the column to inherit the format for the new columns. It can be -1. If it is -1 new columns don't inherit any format and they use default format.
            
            int numCols: 
            Input number of columns to insert
        """
        pass
    
    
    def InsertRows(self):
        """
        InsertRows -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            double height: 
            Input height for the inserted rows
            
            int rows: 
            Input number of rows to insert
        """
        pass
    
    
    def InsertRowsAndInherit(self):
        """
        InsertRowsAndInherit -> void
            
            int index: 
            Input index at which to insert the new rows
            
            int inheritFrom: 
            Input index of the row to inherit the format for the new rows. It can be -1. If it is -1 new rows don't inherit any format and they use default format.
            
            int numRows: 
            Input number of rows to insert
        """
        pass
    
    
    def IsAutoScale(self):
        """
        IsAutoScale -> bool
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
        """
        pass
    
    
    
