class ArcType():
    ArcSimple = None
    ArcSector = None
    ArcChord = None

class AttenuationType():
    None = None
    InverseLinear = None
    InverseSquare = None

class AutoTransform():
    InheritAutoTransform = 0
    Model = 4
    None = 1
    TransformObject = 2

class ChannelFlags():
    None = 0
    UseAll = 0x3f
    UseBump = 0x10
    UseDiffuse = 1
    UseOpacity = 8
    UseReflection = 4
    UseRefraction = 0x20
    UseSpecular = 2

class ClipBoundary(object):
    """
    
    ClipBoundary()
    """
    def GetAptPoints(self):
        """
        GetAptPoints -> Point2dCollection
        
        """
        pass
    
    
    def SetAptPoints(self):
        """
        SetAptPoints -> void
            
            Point2dCollection point: 
            Input point
        """
        pass
    
    
    BackClipZ = None
    
    
    ClippingBack = None
    
    
    ClippingFront = None
    
    
    DrawBoundary = None
    
    
    FrontClipZ = None
    
    
    NormalVector = None
    
    
    Point = None
    
    
    TransformInverseBlockRefXForm = None
    
    
    TransformToClipSpace = None
    
    pass

class ColorRGB(object):
    """
    
    ColorRGB()()
    
    
    ColorRGB(double, double, double)
        double red : The red component.
        double green : The green component.
        double blue : The blue component.
    
    
    """
    Blue = None
    
    
    Green = None
    
    
    Red = None
    
    pass

class ColorRGBA(object):
    """
    
    ColorRGBA()()
    
    
    ColorRGBA(double, double, double)
        double red : Input color red component
        double green : Input color green component
        double blue : Input color blue component
    
    
    ColorRGBA(double, double, double, double)
        double red : Input color red component
        double green : Input color green component
        double blue : Input color blue component
        double alpha : Input alpha-shading component
    
    
    """
    Alpha = None
    
    
    Blue = None
    
    
    Green = None
    
    
    Red = None
    
    pass

class CommonDraw(object):
    """
    
    """
    def Deviation(self):
        """
        Deviation -> double
            
            DeviationType deviationType: 
            Input desired deviation type.
            
            Point3d pointOnCurve: 
            Input point locating curve or surface to be tessellated.
        """
        pass
    
    
    Context = None
    
    
    IsDragging = None
    
    
    NumberOfIsolines = None
    
    
    RawGeometry = None
    
    
    RegenAbort = None
    
    
    RegenType = None
    
    
    SubEntityTraits = None
    
    pass

class Context(object):
    """
    
    Context()()
    
    
    """
    def DisableFastMoveDrag(self):
        """
        DisableFastMoveDrag -> void
        
        """
        pass
    
    
    ByBlockLineWeight = None
    
    
    ByBlockPlotStyleNameId = None
    
    
    Database = None
    
    
    EffectiveColor = None
    
    
    IsBoundaryClipping = None
    
    
    IsNesting = None
    
    
    IsPlotGeneration = None
    
    
    IsPostScriptOut = None
    
    
    SupportsTrueTypeText = None
    
    pass

class ContextualColors(object):
    """
    
    ContextualColors()()
    
    
    """
    def FlagsSet(self):
        """
        FlagsSet -> bool
            
            int modopt(IsLong) flag: 
            Input flag whose state is to be checked
        """
        pass
    
    
    def SetContextFlags(self):
        """
        SetContextFlags -> void
            
            int modopt(IsLong) flag: 
            Input flag to set
            
            [MarshalAs(UnmanagedType.U1)] bool set: 
            Input value to set
        """
        pass
    
    
    GridAxisLineTintXYZ = None
    
    
    GridMajorLineTintXYZ = None
    
    
    GridMinorLineTintXYZ = None
    
    
    LightDistanceColor = None
    
    
    LightShapeColor = None
    
    
    WebMeshColor = None
    
    
    WebMeshMissingColor = None
    
    pass

class DefaultLightingType():
    OneDistantLight = None
    TwoDistantLights = None

class DeviationType():
    MaxDevForCircle = None
    MaxDevForCurve = None
    MaxDevForBoundary = None
    MaxDevForIsoline = None
    MaxDevForFacet = None

class DistantLightTraits(object):
    """
    
    DistantLightTraits()
    """
    IsSunlight = None
    
    
    LampColor = None
    
    
    LightDirection = None
    
    
    PhysicalIntensity = None
    
    
    SkyParameters = None
    
    pass

class DrawFlags():
    DrawBackfaces = 1
    DrawFillTextBoundaryEnd = 0x200
    DrawFillTextBoundaryStart = 0x100
    DrawNoLineWeight = 0x20
    None = 0

class Drawable(object):
    """
    
    """
    def SetAttributes(self):
        """
        SetAttributes -> Integer
            
            DrawableTraits traits: 
            Input object to be set. Traits are filled in with the calling objects subentity traits values.
        """
        pass
    
    
    def ViewportDraw(self):
        """
        ViewportDraw -> void
            
            Autodesk.AutoCAD.GraphicsInterface.ViewportDraw vd: 
            Input ViewportDraw interface
        """
        pass
    
    
    def ViewportDrawLogicalFlags(self):
        """
        ViewportDrawLogicalFlags -> Integer
            
            Autodesk.AutoCAD.GraphicsInterface.ViewportDraw vd: 
            Input ViewportDraw interface
        """
        pass
    
    
    def WorldDraw(self):
        """
        WorldDraw -> bool
            
            Autodesk.AutoCAD.GraphicsInterface.WorldDraw wd: 
            Input WorldDraw interface
        """
        pass
    
    
    Bounds = None
    
    
    DrawableType = None
    
    
    DrawStream = None
    
    
    Id = None
    
    
    IsPersistent = None
    
    pass

class DrawableAttributes():
    BlockDependentViewportDraw = 0x1000
    HasAttributes = 0x20
    IsAnEntity = 1
    IsCompoundObject = 4
    IsDimension = 0x85
    IsExternalReference = 0x2000
    IsInvisible = 0x10
    None = 0
    NotPlottable = 0x4000
    RegenDraw = 0x100
    RegenTypeDependentGeometry = 0x40
    ShadedDisplaySingleLOD = 0x400
    StandardDisplaySingleLOD = 0x200
    UsesNesting = 2
    ViewDependentViewportDraw = 0x800
    ViewIndependentViewportDraw = 8

class DrawableOverrule(object):
    """
    
    """
    def SetAttributes(self):
        """
        SetAttributes -> Integer
        
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
    
    
    def ViewportDraw(self):
        """
        ViewportDraw -> void
        
        """
        pass
    
    
    def ViewportDrawLogicalFlags(self):
        """
        ViewportDrawLogicalFlags -> Integer
        
        """
        pass
    
    
    def WorldDraw(self):
        """
        WorldDraw -> bool
        
        """
        pass
    
    pass

class DrawableTraits(object):
    """
    
    DrawableTraits()
    """
    class HighlightProperty():
        VertexRolloverHighlightSize = None
    
    
    def AddLight(self):
        """
        AddLight -> void
            
            ObjectId lightId: 
            Input the added light.
        """
        pass
    
    
    def GetHighlightProperty(self):
        """
        GetHighlightProperty -> object
            
            HighlightProperty propertyType: 
            Input DrawableTraits::HighlightProperty that identifies the highlight property type.
        """
        pass
    
    
    def SetHighlightProperty(self):
        """
        SetHighlightProperty -> void
            
            HighlightProperty propertyType: 
            Input DrawableTraits::HighlightProperty that identifies the highlight property type.
            
            object value: 
            Input Variant for value of the highight property .
        """
        pass
    
    
    def SetLayerFlags(self):
        """
        SetLayerFlags -> void
            
            LayerFlags flags: 
            Input LayerFlags
        """
        pass
    
    
    def SetupForEntity(self):
        """
        SetupForEntity -> void
            
            Entity entity: 
            Input entity
        """
        pass
    
    
    LinePattern = None
    
    
    SelectionFlags = None
    
    pass

class DrawableType():
    Geometry = None
    DistantLight = None
    PointLight = None
    SpotLight = None
    AmbientLight = None
    SolidBackground = None
    GradientBackground = None
    ImageBackground = None
    GroundPlaneBackground = None
    Viewport = None
    WebLight = None
    SkyBackground = None
    ImageBasedLightingBackground = None

class EdgeData(object):
    """
    
    """
    def GetColors(self):
        """
        GetColors -> short()
        
        """
        pass
    
    
    def GetLayers(self):
        """
        GetLayers -> ObjectId()
        
        """
        pass
    
    
    def GetLineTypes(self):
        """
        GetLineTypes -> ObjectId()
        
        """
        pass
    
    
    def GetSelectionMarkers(self):
        """
        GetSelectionMarkers -> IntPtr()
        
        """
        pass
    
    
    def GetTrueColors(self):
        """
        GetTrueColors -> EntityColor()
        
        """
        pass
    
    
    def GetVisibility(self):
        """
        GetVisibility -> byte()
        
        """
        pass
    
    
    def SetColors(self):
        """
        SetColors -> void
            
            short[] colors: 
            Input array of AutoCAD color indices.
        """
        pass
    
    
    def SetLayers(self):
        """
        SetLayers -> void
            
            ObjectId[] layers: 
            Input array of LayerTableRecord object IDs.
        """
        pass
    
    
    def SetLineTypes(self):
        """
        SetLineTypes -> void
            
            ObjectId[] lineTypes: 
            Input array of LinetypeTableRecord object IDs
        """
        pass
    
    
    def SetSelectionMarkers(self):
        """
        SetSelectionMarkers -> void
            
            IntPtr[] selectionMarkers: 
            Input array of non-zero graphic system selection markers.
        """
        pass
    
    
    def SetTrueColors(self):
        """
        SetTrueColors -> void
            
            EntityColor[] colors: 
            Input array of EntityColor objects
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            byte[] visibility: 
            Input array of visibility flags
        """
        pass
    
    pass

class ExtendedLightShape():
    Linear = None
    Rectangle = None
    Disk = None
    Cylinder = None
    Sphere = None

class ExteriorDaylightMode():
    DaylightOff = None
    DaylightOn = None
    DaylightAuto = None

class FaceData(object):
    """
    
    """
    def GetColors(self):
        """
        GetColors -> short()
        
        """
        pass
    
    
    def GetLayers(self):
        """
        GetLayers -> ObjectId()
        
        """
        pass
    
    
    def GetMappers(self):
        """
        GetMappers -> Mapper()
        
        """
        pass
    
    
    def GetMaterials(self):
        """
        GetMaterials -> ObjectId()
        
        """
        pass
    
    
    def GetNormalVectors(self):
        """
        GetNormalVectors -> Vector3d()
        
        """
        pass
    
    
    def GetSelectionMarkers(self):
        """
        GetSelectionMarkers -> IntPtr()
        
        """
        pass
    
    
    def GetTransparency(self):
        """
        GetTransparency -> Transparency()
        
        """
        pass
    
    
    def GetTrueColors(self):
        """
        GetTrueColors -> EntityColor()
        
        """
        pass
    
    
    def GetVisibility(self):
        """
        GetVisibility -> byte()
        
        """
        pass
    
    
    def SetColors(self):
        """
        SetColors -> void
            
            short[] colors: 
            Input array of AutoCAD color indices
        """
        pass
    
    
    def SetLayers(self):
        """
        SetLayers -> void
            
            ObjectId[] layers: 
            Input array of LayerTableRecord object IDs
        """
        pass
    
    
    def SetMappers(self):
        """
        SetMappers -> void
            
            Mapper[] mappers: 
            Input face mappers to be set on the this object.
        """
        pass
    
    
    def SetMaterials(self):
        """
        SetMaterials -> void
            
            ObjectId[] materials: 
            Input array of materials to be set on the this object.
        """
        pass
    
    
    def SetNormalVectors(self):
        """
        SetNormalVectors -> void
            
            Vector3d[] normal: 
            Input array of normal vectors.
        """
        pass
    
    
    def SetSelectionMarkers(self):
        """
        SetSelectionMarkers -> void
            
            IntPtr[] selectionMarker: 
            Input array of non-zero graphic system selection markers.
        """
        pass
    
    
    def SetTransparency(self):
        """
        SetTransparency -> void
            
            Transparency[] transparency: 
            Input Autodesk.AutoCAD.Colors.Transparency to set into the FaceData.
        """
        pass
    
    
    def SetTrueColors(self):
        """
        SetTrueColors -> void
            
            EntityColor[] colors: 
            Input array of EntityColor objects
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            byte[] visibility: 
            Input array of visibility flags
        """
        pass
    
    pass

class Fill(object):
    """
    
    Fill()
    """

    pass

class FillType():
    FillAlways = 1
    FillNever = 2

class FinalGatherMode():
    FinalGatherNone = None
    FinalGatherCast = None
    FinalGatherReceive = None
    FinalGatherCastAndReceive = None

class FontDescriptor(object):
    """
    
    FontDescriptor
        string typeFace : Input the font name
        [MarshalAs(UnmanagedType.U1)] bool bold : Input true for a bold text
        [MarshalAs(UnmanagedType.U1)] bool italic : Input true for an italic text
        int characters : Input indicating the character set being used
        int pitchAndFamily : Input indicating the pitch and family being used
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
            Input for culture-specific format
        """
        pass
    
    
    Bold = None
    
    
    CharacterSet = None
    
    
    Italic = None
    
    
    PitchAndFamily = None
    
    
    TypeFace = None
    
    pass

class FrontAndBackClipping(object):
    """
    
    FrontAndBackClipping
        [MarshalAs(UnmanagedType.U1)] bool clipFront : Input Boolean indicating if front clip plane is active
        [MarshalAs(UnmanagedType.U1)] bool clipBack : Input Boolean indicating if back clip plane is active
        double front : Input eye coordinate Z value of front clipping plane
        double back : Input eye coordinate Z value of front clipping plane
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object with which to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(FrontAndBackClipping) -> bool
            
            FrontAndBackClipping a: 
            Input object with which to check against
        IsEqualTo(FrontAndBackClipping, Tolerance) -> bool
            
            FrontAndBackClipping a: 
            Input object with which to check against
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    Back = None
    
    
    ClipBack = None
    
    
    ClipFront = None
    
    
    Front = None
    
    pass

class GdiDrawObject(object):
    """
    
    """
    def Draw(self):
        """
        Draw -> bool
            
            IntPtr hDC: 
            Input handle to the specified device context.
            
            Rectangle bounds: 
            Input bounding rectangle (in logical units) in which the GDI owner draw object will be displayed.
        """
        pass
    
    
    Height = None
    
    
    Width = None
    
    pass

class GenericTexture(object):
    """
    
    GenericTexture()
    """
    def Clone(self):
        """
        Clone -> GenericTexture
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
        
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
    
    
    def Set(self):
        """
        Set -> void
            
            GenericTexture value: 
            Input new value
        """
        pass
    
    
    Definition = None
    
    pass

class Geometry(object):
    """
    
    """
    def Circle(self):
        """
        Circle(Point3d, Point3d, Point3d) -> bool
            
            Point3d firstPoint: 
            Input first point on circle
            
            Point3d secondPoint: 
            Input second point on circle
            
            Point3d thirdPoint: 
            Input third point on circle
        Circle(Point3d, double, Vector3d) -> bool
            
            Point3d center: 
            Input center point for the circle.
            
            double radius: 
            Input radius for the circle.
            
            Vector3d normal: 
            Input normal vector for plane to contain the circle.
        """
        pass
    
    
    def Polypoint(self):
        """
        Polypoint -> bool
            
            Point3dCollection points: 
            Input number of vertex points
            
            Vector3dCollection normals: 
            Input normal vectors
            
            IntPtrCollection subentityMarkers: 
            Input sub-entity markers to be applied per point
        """
        pass
    
    
    def CircularArc(self):
        """
        CircularArc(Point3d, Point3d, Point3d, ArcType) -> bool
            
            Point3d start: 
            Input start point of arc
            
            Point3d point: 
            Input point on arc
            
            Point3d endingPoint: 
            Input endpoint of arc
            
            ArcType arcType: 
            Input type of arc to display
        CircularArc(Point3d, double, Vector3d, Vector3d, double, ArcType) -> bool
            
            Point3d center: 
            Input center point for arc's center of curvature.
            
            double radius: 
            Input arc's radius of curvature.
            
            Vector3d normal: 
            Input normal vector for plane to contain arc.
            
            Vector3d startVector: 
            Input vector defining the direction the arc start point is from the arc's center of curvature.
            
            double sweepAngle: 
            Input angle (in radians) that encompasses the arc.
            
            ArcType arcType: 
            Input type of arc to display.
        """
        pass
    
    
    def Draw(self):
        """
        Draw -> bool
            
            Drawable value: 
            Input Drawable to be rendered
        """
        pass
    
    
    def Edge(self):
        """
        Edge -> bool
        
        """
        pass
    
    
    def EllipticalArc(self):
        """
        EllipticalArc -> bool
            
            Point3d center: 
            Input the center point
            
            Vector3d normal: 
            Input the normal vector
            
            double majorAxisLength: 
            Input major axis length
            
            double minorAxisLength: 
            Input minor axis length
            
            double startDegreeInRads: 
            Input the start degree in radius
            
            double endDegreeInRads: 
            Input the end degree in radius
            
            double tiltDegreeInRads: 
            Input the tilt degree in radius
            
            ArcType arcType: 
            Input the arc type. See AcGiArcType for the types that can be specified.
        """
        pass
    
    
    def Mesh(self):
        """
        Mesh -> bool
            
            int rows: 
            Input number of rows in mesh
            
            int columns: 
            Input number of columns in mesh
            
            Point3dCollection points: 
            Input array of vertex points (must be rows x columns points)
            
            EdgeData edgeData: 
            Input to an existing EdgeData object
            
            FaceData faceData: 
            Input to an existing FaceData object
            
            VertexData vertexData: 
            Input to an existing VertexData object
            
            [MarshalAs(UnmanagedType.U1)] bool bAutoGenerateNormals: 
            Input Boolean to indicate whether the display system should automatically generate normals for vertices and faces if they are not passed in through vertexData and faceData.
        """
        pass
    
    
    def Image(self):
        """
        Image(ImageBGRA32, Point3d, Vector3d, Vector3d) -> bool
            
            ImageBGRA32 imageSource: 
            Input transparent image
            
            Point3d position: 
            Input start or insertion point for the image, in display coordinates
            
            Vector3d u: 
            Input the width of destination rectangle
            
            Vector3d v: 
            Input the height of destination rectangle
        Image(ImageBGRA32, Point3d, Vector3d, Vector3d, Autodesk.AutoCAD.GraphicsInterface.TransparencyMode) -> bool
            
            ImageBGRA32 imageSource: 
            Input transparent image
            
            Point3d position: 
            Input start or insertion point for the image, in display coordinates
            
            Vector3d u: 
            Input the width of destination rectangle
            
            Vector3d v: 
            Input the height of destination rectangle
            
            Autodesk.AutoCAD.GraphicsInterface.TransparencyMode transparencyMode: 
            Input the transparencyMode to the display the image with
        """
        pass
    
    
    def Polygon(self):
        """
        Polygon -> bool
            
            Point3dCollection points: 
            Input number of vertex points in polyline (minimum of two)
        """
        pass
    
    
    def OwnerDraw(self):
        """
        OwnerDraw -> bool
            
            GdiDrawObject gdiDrawObject: 
            Input GDI owner draw object.
            
            Point3d position: 
            Input start or insertion point for the GDI owner draw object.
            
            Vector3d u: 
            Input orientation and magnitude of width.
            
            Vector3d v: 
            Input orientation and magnitude of height.
        """
        pass
    
    
    def Polyline(self):
        """
        Polyline(Autodesk.AutoCAD.DatabaseServices.Polyline, int, int) -> bool
            
            Autodesk.AutoCAD.DatabaseServices.Polyline value: 
            Input existing Polyline object
            
            int fromIndex: 
            Input index to generate from
            
            int segments: 
            Input number of segments
        Polyline(Point3dCollection, Vector3d, IntPtr) -> bool
            
            Point3dCollection points: 
            Input number of vertex points in polyline (minimum of two)
            
            Vector3d normal: 
            Input normal vector
            
            IntPtr subEntityMarker: 
            Input sub-entity marker for first segment
        Polyline(Autodesk.AutoCAD.GraphicsInterface.Polyline) -> bool
            
            Autodesk.AutoCAD.GraphicsInterface.Polyline polylineObj: 
            Input a polyline object
        """
        pass
    
    
    def PopClipBoundary(self):
        """
        PopClipBoundary -> void
        
        """
        pass
    
    
    def PolyPolygon(self):
        """
        PolyPolygon -> bool
        
        """
        pass
    
    
    def PopModelTransform(self):
        """
        PopModelTransform -> bool
        
        """
        pass
    
    
    def PolyPolyline(self):
        """
        PolyPolyline -> bool
            
            PolylineCollection polylineCollection: 
            Input a PolylineCollection object
        """
        pass
    
    
    def PushClipBoundary(self):
        """
        PushClipBoundary -> bool
            
            ClipBoundary boundary: 
            Input clip boundary
        """
        pass
    
    
    def PushModelTransform(self):
        """
        PushModelTransform(Matrix3d) -> bool
            
            Matrix3d matrix: 
            Input input matrix
        PushModelTransform(Vector3d) -> bool
            
            Vector3d normal: 
            Input normal vector
        """
        pass
    
    
    def Ray(self):
        """
        Ray -> bool
            
            Point3d point1: 
            Input starting point of ray
            
            Point3d point2: 
            Input another point (different from starting point) on the ray
        """
        pass
    
    
    def Shell(self):
        """
        Shell -> bool
            
            Point3dCollection points: 
            Input array of vertex points
            
            IntegerCollection faces: 
            Input collection of integers
            
            EdgeData edgeData: 
            Input to an existing EdgeData object
            
            FaceData faceData: 
            Input to an existing FaceData object
            
            VertexData vertexData: 
            Input to an existing VertexData object
            
            [MarshalAs(UnmanagedType.U1)] bool bAutoGenerateNormals: 
            Input Boolean to indicate whether the display system should automatically generate normals for vertices and faces if they are not passed in through vertexData and faceData
        """
        pass
    
    
    def Text(self):
        """
        Text(Point3d, Vector3d, Vector3d, double, double, double, string) -> bool
            
            Point3d position: 
            Input start or insertion point for the text
            
            Vector3d normal: 
            Input normal for the plane to contain the text
            
            Vector3d direction: 
            Input direction the text will go
            
            double height: 
            Input text height
            
            double width: 
            Input text width
            
            double oblique: 
            Input text obliquing angle
            
            string message: 
            Input text string to display
        Text(Point3d, Vector3d, Vector3d, string, [MarshalAs(UnmanagedType.U1)] bool, TextStyle) -> bool
            
            Point3d position: 
            Input start or insertion point for the text
            
            Vector3d normal: 
            Input normal for the plane to contain the text
            
            Vector3d direction: 
            Input direction the text will go
            
            string message: 
            Input text string to display
            
            [MarshalAs(UnmanagedType.U1)] bool raw: 
            Input informing AutoCAD whether to interpret escape codes.
            
            TextStyle textStyle: 
            Input existing text style
        """
        pass
    
    
    def PushOrientationTransform(self):
        """
        PushOrientationTransform -> Matrix3d
            
            OrientationBehavior behavior: 
            Input orientation transform behavior to push
        """
        pass
    
    
    def WorldLine(self):
        """
        WorldLine -> bool
            
            Point3d startPoint: 
            Input start point of the worldline
            
            Point3d endPoint: 
            Input second point on the worldline
        """
        pass
    
    
    def PushPositionTransform(self):
        """
        PushPositionTransform(PositionBehavior, Point2d) -> Matrix3d
            
            PositionBehavior behavior: 
            Input transform behavior
            
            Point2d offset: 
            Input position coordinate
        PushPositionTransform(PositionBehavior, Point3d) -> Matrix3d
            
            PositionBehavior behavior: 
            Input transform behavior
            
            Point3d offset: 
            Input position coordinate
        """
        pass
    
    
    def Xline(self):
        """
        Xline -> bool
            
            Point3d point1: 
            Input point on an xline
            
            Point3d point2: 
            Input second point on an xline
        """
        pass
    
    
    def PushScaleTransform(self):
        """
        PushScaleTransform(ScaleBehavior, Point2d) -> Matrix3d
            
            ScaleBehavior behavior: 
            Input scale transformation behavior
            
            Point2d extents: 
            Input new scale values
        PushScaleTransform(ScaleBehavior, Point3d) -> Matrix3d
            
            ScaleBehavior behavior: 
            Input scale transformation behavior
            
            Point3d extents: 
            Input new scale values
        """
        pass
    
    
    def RowOfDots(self):
        """
        RowOfDots -> bool
            
            int count: 
            Input the number of dots
            
            Point3d start: 
            Input the start point for the row of dots
            
            Vector3d step: 
            Input the step among the row of dots
        """
        pass
    
    
    ModelToWorldTransform = None
    
    
    WorldToModelTransform = None
    
    pass

class GlobalIlluminationMode():
    GlobalIlluminationNone = None
    GlobalIlluminationCast = None
    GlobalIlluminationReceive = None
    GlobalIlluminationCastAndReceive = None

class Glyph(object):
    """
    
    Glyph()()
    
    
    """
    def SetLocation(self):
        """
        SetLocation -> void
            
            Point3d point: 
            Input display coordinate system (DCS) point.
        """
        pass
    
    
    Id = None
    
    
    IsPersistent = None
    
    pass

class GradientBackgroundTraits(object):
    """
    
    """
    ColorBottom = None
    
    
    ColorMiddle = None
    
    
    ColorTop = None
    
    
    Height = None
    
    
    Horizon = None
    
    
    Rotation = None
    
    pass

class GradientFill(object):
    """
    
    GradientFill()
    """
    GradientAngle = None
    
    
    GradientColors = None
    
    
    GradientShift = None
    
    
    IsAdjustAspect = None
    
    
    Type = None
    
    pass

class GradientType():
    Linear = None
    Cylinder = None
    InvCylinder = None
    Spherical = None
    Hemispherical = None
    Curved = None
    InvSpherical = None
    InvHemispherical = None
    InvCurved = None

class GroundPlaneBackgroundTraits(object):
    """
    
    """
    ColorGroundPlaneFar = None
    
    
    ColorGroundPlaneNear = None
    
    
    ColorSkyHorizon = None
    
    
    ColorSkyZenith = None
    
    
    ColorUndergroundAzimuth = None
    
    
    ColorUndergroundHorizon = None
    
    pass

class HatchPattern(object):
    """
    
    HatchPattern()
    """
    PatternLines = None
    
    pass

class HatchPatternDefinition(object):
    """
    
    HatchPatternDefinition()
    """
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    Angle = None
    
    
    BaseX = None
    
    
    BaseY = None
    
    
    DashList = None
    
    
    OffsetX = None
    
    
    OffsetY = None
    
    pass

class HighlightStyle():
    None = None
    Custom = None
    DashedAndThicken = None
    Dim = None
    ThickDim = None
    Glow = None

class IBLBackgroundTraits(object):
    """
    
    """
    DisplayImage = None
    
    
    Enable = None
    
    
    IBLImageName = None
    
    
    Rotation = None
    
    
    SecondaryBackground = None
    
    pass

class IlluminationModel():
    BlinnShader = None
    MetalShader = None

class ImageBGRA32(object):
    """
    
    ImageBGRA32()()
    
    
    ImageBGRA32(uint, uint, IntPtr)
        uint width : Input the image's width
        uint height : Input the image's height
        IntPtr imageData : Input the image's buffer data
    
    
    """
    Height = None
    
    
    Image = None
    
    
    Width = None
    
    pass

class ImageBackgroundTraits(object):
    """
    
    """
    FitToScreen = None
    
    
    ImageFilename = None
    
    
    MaintainAspectRatio = None
    
    
    UseTiling = None
    
    
    XOffset = None
    
    
    XScale = None
    
    
    YOffset = None
    
    
    YScale = None
    
    pass

class ImageFileTexture(object):
    """
    
    ImageFileTexture()
    """
    def Clone(self):
        """
        Clone -> object
        
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
    
    
    SourceFileName = None
    
    pass

class ImageOrg():
    Bitonal = None
    Palette = None
    Gray = None
    RGBA = None
    BGRA = None
    ARGB = None
    ABGR = None
    BGR = None
    RGB = None

class ImageSource():
    FromDwg = None
    FromOleObject = None
    FromRender = None

class ImageTexture(object):
    """
    
    ImageTexture()
    """

    pass

class LightAttenuation(object):
    """
    
    LightAttenuation()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input.
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def SetLimits(self):
        """
        SetLimits -> void
            
            double startLimit: 
            Input distance from the light source where light begins to affect to model; objects closer than this are not affected by the light
            
            double endLimit: 
            Input distance from the light source beyond which the light has no effect
        """
        pass
    
    
    AttenuationType = None
    
    
    EndLimit = None
    
    
    StartLimit = None
    
    
    UseLimits = None
    
    pass

class LightTraits(object):
    """
    
    LightTraits()
    """
    On = None
    
    pass

class Linetype():
    Solid = None
    Dashed = None
    Dotted = None
    DashDot = None
    ShortDash = None
    MediumDash = None
    LongDash = None
    ShortDashX2 = None
    MediumDashX2 = None
    LongDashX2 = None
    MediumLongDash = None
    MediumDashShortDashShortDash = None
    LongDashShortDash = None
    LongDashDotDot = None
    LongDashDot = None
    MediumDashDotShortDashDot = None
    SparseDot = None
    ISODash = None
    ISODashSpace = None
    ISOLongDashDot = None
    ISOLongDashDoubleDot = None
    ISOLongDashTripleDot = None
    ISODot = None
    ISOLongDashShortDash = None
    ISOLongDashDoubleShortDash = None
    ISODashDot = None
    ISODoubleDashDot = None
    ISODashDoubleDot = None
    ISODoubleDashDoubleDot = None
    ISODashTripleDot = None
    ISODoubleDashTripleDot = None
    LineTypeNone = None
    Solid6PixelsBlank6Pixels = None

class LuminanceMode():
    SelfIllumination = None
    Luminance = None

class MapChannel():
    AllChannels = None
    MapChannels = None

class MapFilter():
    Default = None
    None = None

class Mapper(object):
    """
    
    Mapper()()
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    AutoTransform = None
    
    
    Projection = None
    
    
    Transform = None
    
    
    UTiling = None
    
    
    VTiling = None
    
    pass

class MarbleTexture(object):
    """
    
    MarbleTexture()
    """
    def Clone(self):
        """
        Clone -> MarbleTexture
        
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
    
    
    def Set(self):
        """
        Set -> void
            
            MarbleTexture value: 
            Input existing marble texture
        """
        pass
    
    
    StoneColor = None
    
    
    VeinColor = None
    
    
    VeinSpacing = None
    
    
    VeinWidth = None
    
    pass

class MaterialColor(object):
    """
    
    MaterialColor()()
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    Color = None
    
    
    Factor = None
    
    
    Method = None
    
    pass

class MaterialDiffuseComponent(object):
    """
    
    MaterialDiffuseComponent
        MaterialColor color : Input material color
        MaterialMap map : Input material map
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
            Input for culture-specific format
        """
        pass
    
    
    Color = None
    
    
    Map = None
    
    pass

class MaterialMap(object):
    """
    
    MaterialMap()()
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    BlendFactor = None
    
    
    Filter = None
    
    
    Mapper = None
    
    
    Source = None
    
    
    SourceFileName = None
    
    
    Texture = None
    
    pass

class MaterialNormalMapComponent(object):
    """
    
    MaterialNormalMapComponent
        MaterialMap map : Input material map
        Autodesk.AutoCAD.GraphicsInterface.NormalMapMethod method : Input normal map method
        double strength : Input strength
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Input object to compare against
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
            Input for culture-specific format
        """
        pass
    
    
    Map = None
    
    
    Method = None
    
    
    Strength = None
    
    pass

class MaterialOpacityComponent(object):
    """
    
    MaterialOpacityComponent
        double percentage : Input opacity percentage
        MaterialMap map : Input material map
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Input object to compare against
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
            Input for culture-specific format
        """
        pass
    
    
    Map = None
    
    
    Percentage = None
    
    pass

class MaterialRefractionComponent(object):
    """
    
    MaterialRefractionComponent
        double index : Input index of refraction
        MaterialMap map : Input material map
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Input object to compare against
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
            Input for culture-specific format
        """
        pass
    
    
    Index = None
    
    
    Map = None
    
    pass

class MaterialSpecularComponent(object):
    """
    
    MaterialSpecularComponent
        MaterialColor color : Input material color
        MaterialMap map : Input material map
        double gloss : Input gloss value
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
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
            Input for culture-specific format
        """
        pass
    
    
    Color = None
    
    
    Gloss = None
    
    
    Map = None
    
    pass

class MaterialTexture(object):
    """
    
    MaterialTexture()
    """

    pass

class MaterialTraits(object):
    """
    
    """
    Ambient = None
    
    
    Bump = None
    
    
    ChannelFlags = None
    
    
    ColorBleedScale = None
    
    
    Diffuse = None
    
    
    FinalGather = None
    
    
    GlobalIllumination = None
    
    
    IlluminationModel = None
    
    
    IndirectBumpScale = None
    
    
    Luminance = None
    
    
    LuminanceMode = None
    
    
    Mode = None
    
    
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

class Method():
    Inherit = None
    Override = None

class Mode():
    Realistic = None
    Advanced = None

class NonEntityTraits(object):
    """
    
    """
    def AddLight(self):
        """
        AddLight -> void
            
            ObjectId lightId: 
            Input the added light.
        """
        pass
    
    
    def GetHighlightProperty(self):
        """
        GetHighlightProperty -> object
        
        """
        pass
    
    
    def SetHighlightProperty(self):
        """
        SetHighlightProperty -> void
        
        """
        pass
    
    
    def SetSelectionMarker(self):
        """
        SetSelectionMarker -> void
            
            IntPtr markerId: 
            Input non-zero integer to use as graphics system marker
        """
        pass
    
    
    def SetupForEntity(self):
        """
        SetupForEntity -> void
            
            Entity entity: 
            Input entity
        """
        pass
    
    
    Color = None
    
    
    DrawFlags = None
    
    
    Fill = None
    
    
    FillType = None
    
    
    Layer = None
    
    
    LinePattern = None
    
    
    LineType = None
    
    
    LineTypeScale = None
    
    
    LineWeight = None
    
    
    Mapper = None
    
    
    Material = None
    
    
    PlotStyleDescriptor = None
    
    
    Sectionable = None
    
    
    SelectionFlags = None
    
    
    SelectionOnlyGeometry = None
    
    
    ShadowFlags = None
    
    
    Thickness = None
    
    
    TrueColor = None
    
    
    VisualStyle = None
    
    pass

class NormalMapMethod():
    TangentSpaceNormalMap = None

class OrientationBehavior():
    World = None
    Screen = None
    ZAxis = None

class OrientationType():
    Clockwise = 1
    CounterClockwise = -1
    NoOrientation = 0

class PhotographicExposureParameters(object):
    """
    
    PhotographicExposureParameters()
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    Exposure = None
    
    
    WhiteColor = None
    
    
    WhitePoint = None
    
    pass

class PixelBGRA32(object):
    """
    
    PixelBGRA32()()
    
    
    PixelBGRA32(uint)
        uint bgra : Input color of component
    
    
    PixelBGRA32(byte, byte, byte, byte)
        byte blue : Input color blue component
        byte green : Input color green component
        byte red : Input color red component
        byte alpha : Input color alpha-shading component
    
    
    """
    def init(self):
        """
        init -> void
        
        """
        pass
    
    
    Alpha = None
    
    
    Blue = None
    
    
    Green = None
    
    
    Red = None
    
    pass

class PointLightTraits(object):
    """
    
    PointLightTraits()
    """
    Attenuation = None
    
    
    HasTarget = None
    
    
    LampColor = None
    
    
    PhysicalIntensity = None
    
    
    Position = None
    
    
    TargetLocation = None
    
    pass

class Polyline(object):
    """
    
    Polyline()()
    
    
    Polyline(Point3dCollection, Vector3d, IntPtr)
        Point3dCollection pPoints : A list of points
        Vector3d normal : Input normal.
        IntPtr pBaseSubEntMarker : Subentity marker for first segment.
    
    
    """
    BaseSubEntMarker = None
    
    
    Normal = None
    
    
    Points = None
    
    pass

class PolylineCollection(object):
    """
    
    PolylineCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            Polyline value: 
            Input the polyline object.
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input the specified index.
        """
        pass
    
    
    Count = None
    
    pass

class PositionBehavior():
    World = None
    Viewport = None
    Screen = None
    ScreenLocalOrigin = None
    WorldWithScreenOffset = None

class ProceduralTexture(object):
    """
    
    ProceduralTexture()
    """

    pass

class ProceduralTextureType():
    Wood = None
    Marble = None
    Generic = None

class Projection():
    InheritProjection = None
    Planar = None
    Box = None
    Cylinder = None
    Sphere = None

class RapidRTFilterType():
    Box = None
    Triangle = None
    Gaussian = None
    Lanczos = None
    Mitchell = None

class RapidRTLightingMode():
    Simplified = None
    Basic = None
    Advanced = None

class RapidRTQuitCondition():
    ERenderLevel = None
    ERenderTime = None

class RapidRTRenderSettingsTraits(object):
    """
    
    """
    FilterHeight = None
    
    
    FilterType = None
    
    
    FilterWidth = None
    
    
    LightingMode = None
    
    
    QuitCondition = None
    
    
    RenderLevel = None
    
    
    RenderTime = None
    
    pass

class RegenType():
    ForExplode = 5
    HideOrShadeCommand = 3
    Invalid = 0
    RenderCommand = 4
    SaveWorldDrawForProxy = 6
    ShadedDisplay = 4
    StandardDisplay = 2

class RenderEnvironmentTraits(object):
    """
    
    """
    Enable = None
    
    
    EnvironmentMap = None
    
    
    FarDistance = None
    
    
    FarPercentage = None
    
    
    FogColor = None
    
    
    IsBackground = None
    
    
    NearDistance = None
    
    
    NearPercentage = None
    
    pass

class RenderSettingsTraits(object):
    """
    
    """
    BackFacesEnabled = None
    
    
    DiagnosticBackgroundEnabled = None
    
    
    MaterialEnabled = None
    
    
    ModelScaleFactor = None
    
    
    ShadowsEnabled = None
    
    
    TextureSampling = None
    
    pass

class ScaleBehavior():
    World = None
    Viewport = None
    Screen = None
    ViewportLocalOrigin = None
    ScreenLocalOrigin = None

class SelectionFlags():
    None = None
    SelectionIgnore = None

class ShadowFlags():
    ShadowsCastAndReceive = None
    ShadowsDoesNotCast = None
    ShadowsDoesNotReceive = None
    ShadowsIgnore = None

class ShadowParameters(object):
    """
    
    ShadowParameters()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input.
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    ExtendedLightLength = None
    
    
    ExtendedLightRadius = None
    
    
    ExtendedLightShape = None
    
    
    ExtendedLightWidth = None
    
    
    ShadowMapSize = None
    
    
    ShadowMapSoftness = None
    
    
    ShadowSamples = None
    
    
    ShadowsOn = None
    
    
    ShadowType = None
    
    
    ShapeVisibility = None
    
    pass

class ShadowType():
    RayTraced = None
    Maps = None
    Sampled = None

class SkyBackgroundTraits(object):
    """
    
    """
    SkyParameters = None
    
    pass

class SkyParameters(object):
    """
    
    SkyParameters()
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
    
    
    AerialPerspective = None
    
    
    DiskIntensity = None
    
    
    DiskScale = None
    
    
    GlowIntensity = None
    
    
    GroundColor = None
    
    
    Haze = None
    
    
    HorizonBlur = None
    
    
    HorizonHeight = None
    
    
    Illumination = None
    
    
    IntensityFactor = None
    
    
    NightColor = None
    
    
    RedBlueShift = None
    
    
    Saturation = None
    
    
    SolarDiskSamples = None
    
    
    SunDirection = None
    
    
    VisibilityDistance = None
    
    pass

class SolidBackgroundTraits(object):
    """
    
    """
    ColorSolid = None
    
    pass

class Source():
    Scene = None
    File = None
    Procedural = None

class SpotLightTraits(object):
    """
    
    SpotLightTraits()
    """
    def SetHotspotAndFalloff(self):
        """
        SetHotspotAndFalloff -> bool
            
            double hotspot: 
            Input hotspot cone angle, in radians. Defines the brightest part of the spot light beam. Must be smaller than or equal to the falloff angle.
            
            double falloff: 
            Input falloff angle, in radians. Defines the full cone of light. This is also known as the field angle. Must be larger than or equal to the hotspot.
        """
        pass
    
    
    Attenuation = None
    
    
    Falloff = None
    
    
    Hotspot = None
    
    
    LampColor = None
    
    
    PhysicalIntensity = None
    
    
    Position = None
    
    
    TargetLocation = None
    
    pass

class StandardLightTraits(object):
    """
    
    StandardLightTraits()
    """
    Intensity = None
    
    
    LightColor = None
    
    
    Shadow = None
    
    pass

class SubEntityTraits(object):
    """
    
    SubEntityTraits()
    """
    def SetSelectionMarker(self):
        """
        SetSelectionMarker -> void
            
            IntPtr markerId: 
            Input non-zero integer to use as graphics system marker
        """
        pass
    
    
    Color = None
    
    
    DrawFlags = None
    
    
    Fill = None
    
    
    FillType = None
    
    
    Layer = None
    
    
    LineType = None
    
    
    LineTypeScale = None
    
    
    LineWeight = None
    
    
    Mapper = None
    
    
    Material = None
    
    
    PlotStyleDescriptor = None
    
    
    Sectionable = None
    
    
    SelectionOnlyGeometry = None
    
    
    ShadowFlags = None
    
    
    Thickness = None
    
    
    Transparency = None
    
    
    TrueColor = None
    
    
    VisualStyle = None
    
    pass

class TextStyle(object):
    """
    
    TextStyle()()
    
    
    TextStyle(string, string, double, double, double, double, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(Unman()
    
    
    """
    def ExtentsBox(self):
        """
        ExtentsBox -> Extents2d
            
            string value1: 
            Input text string for which the extents are to be determined
            
            [MarshalAs(UnmanagedType.U1)] bool includeSpaces: 
            Input indicating if leading and trailing spaces are to be included
            
            [MarshalAs(UnmanagedType.U1)] bool raw: 
            Input indicating if the AutoCAD escape sequences are to be interpreted
            
            WorldDraw context: 
            Input if NULL, the AutoCAD default regen pipeline is used to calculate extents
        """
        pass
    
    
    def FromTextStyleTableRecord(self):
        """
        FromTextStyleTableRecord(ObjectId) -> void
            
            e: 
            The ObjectId of the TextStyleTableRecord to copy from
        FromTextStyleTableRecord(string) -> void
            
            e: 
            The name of the TextStyleTableRecord to copy from
        """
        pass
    
    
    def SetTrackKerning(self):
        """
        SetTrackKerning -> void
            
            double trackPercent: 
            Input. For internal use.
        """
        pass
    
    
    def ToTextStyleTableRecord(self):
        """
        ToTextStyleTableRecord() -> ObjectId
        
        ToTextStyleTableRecord(ObjectId) -> void
            
            e: 
            The ObjectId of the TextStyleTableRecord to copy to
        ToTextStyleTableRecord(string) -> ObjectId
            
            e: 
            The name of the TextStyleTableRecord to copy to
        """
        pass
    
    
    Backward = None
    
    
    BigFontFileName = None
    
    
    FileName = None
    
    
    Font = None
    
    
    LoadStyleRec = None
    
    
    ObliquingAngle = None
    
    
    Overlined = None
    
    
    PreLoaded = None
    
    
    Strikethrough = None
    
    
    StyleName = None
    
    
    TextSize = None
    
    
    TrackingPercent = None
    
    
    Underlined = None
    
    
    UpsideDown = None
    
    
    Vertical = None
    
    
    XScale = None
    
    pass

class Tiling():
    InheritTiling = None
    Tile = None
    Crop = None
    Clamp = None
    Mirror = None

class ToneOperatorParameters(object):
    """
    
    ToneOperatorParameters()
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
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
    
    
    Brightness = None
    
    
    ChromaticAdaptation = None
    
    
    ColorDifferentiation = None
    
    
    Contrast = None
    
    
    ExteriorDaylight = None
    
    
    IsActive = None
    
    
    MidTones = None
    
    
    ProcessBackground = None
    
    
    WhiteColor = None
    
    pass

class TransientDrawingMode():
    Main = None
    Sprite = None
    DirectShortTerm = None
    Highlight = None
    DirectTopmost = None
    Contrast = None
    Count = None

class TransientManager(object):
    """
    
    """
    def AddChildTransient(self):
        """
        AddChildTransient -> bool
            
            Drawable added: 
            Input the adding child transient
            
            Drawable parent: 
            Input the parent transient
        """
        pass
    
    
    def AddTransient(self):
        """
        AddTransient -> bool
            
            Drawable added: 
            Input the transient to be added
            
            TransientDrawingMode mode: 
            Input the drawing mode where transient will be added
            
            int subDrawingMode: 
            Input the sub drawing mode of specified drawing mode
            
            IntegerCollection viewportNumbers: 
            Input viewport numbers for viewports to add this transient
        """
        pass
    
    
    def EraseChildTransient(self):
        """
        EraseChildTransient -> bool
            
            Drawable erased: 
            Input the erasing child transient
            
            Drawable parent: 
            Input the parent transient
        """
        pass
    
    
    def EraseTransient(self):
        """
        EraseTransient -> bool
            
            Drawable erased: 
            Input the transient to be removed
            
            IntegerCollection viewportNumbers: 
            Input viewport numbers for viewports to erase this transient
        """
        pass
    
    
    def EraseTransients(self):
        """
        EraseTransients -> bool
            
            TransientDrawingMode mode: 
            Input the drawing mode where transient stores
            
            int subDrawingMode: 
            Input the sub drawing mode of specified drawing mode of transient being erased
            
            IntegerCollection viewportNumbers: 
            Input viewport numbers for viewports to erase this transient
        """
        pass
    
    
    def GetFreeSubDrawingMode(self):
        """
        GetFreeSubDrawingMode -> Integer
            
            TransientDrawingMode mode: 
            Input transient drawing mode
            
            IntegerCollection viewportNumbers: 
            Input the sub drawing mode. If the value is equal to 0, the transient manager will try to get a free draw order and set this value; if the value is bigger than 0, the transient manager will check whether this value is free or not
            
            [In, Out] ref int subDrawingMode: 
            Input viewport numbers for viewports
        """
        pass
    
    
    def UpdateChildTransient(self):
        """
        UpdateChildTransient -> void
            
            Drawable updated: 
            Input the updating child transient
            
            Drawable parent: 
            Input the parent transient
        """
        pass
    
    
    def UpdateTransient(self):
        """
        UpdateTransient -> void
            
            Drawable updated: 
            Input the transient being updated via transient manager
            
            IntegerCollection viewportNumbers: 
            Input viewport numbers for viewports to update this transient
        """
        pass
    
    
    CurrentTransientManager = None
    
    pass

class TransparencyMode():
    TransparencyOff = None
    Transparency1Bit = None
    Transparency8Bit = None

class VSDisplayShadowType():
    None = None
    GroundPlane = None
    Full = None
    FullAndGround = None

class VSDisplayStyles():
    BackgroundsFlag = 1
    LightingFlag = 2
    MaterialsFlag = 4
    None = 0
    TexturesFlag = 8

class VSEdgeJitterAmount():
    JitterHigh = 3
    JitterLow = 1
    JitterMedium = 2

class VSEdgeLinePattern():
    Dashed = 2
    Dotted = 3
    DoubleLongDash = 9
    DoubleMediumDash = 8
    DoubleShortDash = 7
    LongDash = 6
    MediumDash = 5
    MediumLongDash = 10
    ShortDash = 4
    Solid = 1
    SparseDot = 11

class VSEdgeModel():
    NoEdges = None
    Isolines = None
    FacetEdges = None

class VSEdgeModifiers():
    AlwaysOnTopFlag = 0x40
    EdgeColorFlag = 8
    EdgeHaloGapFlag = 0x10
    EdgeJitterFlag = 2
    EdgeOpacityFlag = 0x80
    EdgeOverhangFlag = 1
    EdgeWidthFlag = 4
    None = 0

class VSEdgeStyles():
    IntersectionFlag = 8
    None = 0
    ObscuredFlag = 4
    SilhouetteFlag = 2
    VisibleFlag = 1

class VSFaceColorMode():
    None = None
    ObjectColor = None
    BackgroundColor = None
    Mono = None
    Tint = None
    Desaturate = None

class VSFaceLightingModel():
    Invisible = None
    Constant = None
    Phong = None
    Gooch = None

class VSFaceLightingQuality():
    NoLighting = None
    PerFaceLighting = None
    PerVertexLighting = None
    PerPixelLighting = None

class VSFaceModifiers():
    None = None
    FaceOpacityFlag = None
    SpecularFlag = None

class VariantType():
    Undefined = None
    Boolean = None
    Int = None
    Double = None
    Color = None
    String = None
    Table = None

class VertexData(object):
    """
    
    """
    def get_MappingCoords(self):
        """
        get_MappingCoords -> Point3d()
            
            MapChannel mapChannel: 
            Input material map channel to which the mapping coordinates will be returned.
        """
        pass
    
    
    def GetNormalVectors(self):
        """
        GetNormalVectors -> Vector3d()
        
        """
        pass
    
    
    def GetTrueColors(self):
        """
        GetTrueColors -> EntityColor()
        
        """
        pass
    
    
    def set_MappingCoords(self):
        """
        set_MappingCoords -> void
            
            MapChannel mapChannel: 
            Input material map channel to which the mapping coordinates will be returned.
            
            Point3d[] coords: 
            Input 3d co-ordinate point.
        """
        pass
    
    
    def SetNormalVectors(self):
        """
        SetNormalVectors -> void
            
            Vector3d[] normal: 
            Input array of normal vectors
        """
        pass
    
    
    def SetTrueColors(self):
        """
        SetTrueColors -> void
            
            EntityColor[] colors: 
            Input array of colors
        """
        pass
    
    
    OrientationFlag = None
    
    pass

class Viewport(object):
    """
    
    Viewport()()
    
    
    """
    def DoInversePerspective(self):
        """
        DoInversePerspective -> Point3d
            
            Point3d value: 
            Input point to be transformed
        """
        pass
    
    
    def DoPerspective(self):
        """
        DoPerspective -> Point3d
            
            Point3d value: 
            Input point to be transformed
        """
        pass
    
    
    def GetNumPixelsInUnitSquare(self):
        """
        GetNumPixelsInUnitSquare -> Point2d
            
            Point3d givenWorldPoint: 
            Input WCS point for the center point of the display coordinate unit square
        """
        pass
    
    
    def LayerVisible(self):
        """
        LayerVisible -> bool
            
            ObjectId idLayer: 
            Input layer to be investigated
        """
        pass
    
    
    AcadWindowId = None
    
    
    CameraLocation = None
    
    
    CameraTarget = None
    
    
    CameraUpVector = None
    
    
    DeviceContextViewportCorners = None
    
    
    EyeToModelTransform = None
    
    
    EyeToWorldTransform = None
    
    
    FrontAndBackClipping = None
    
    
    IsPerspective = None
    
    
    LinetypeGenerationCriteria = None
    
    
    LinetypeScaleMultiplier = None
    
    
    ModelToEyeTransform = None
    
    
    ViewDirection = None
    
    
    ViewportId = None
    
    
    WorldToEyeTransform = None
    
    pass

class ViewportDraw(object):
    """
    
    ViewportDraw()()
    
    
    """
    def IsValidId(self):
        """
        IsValidId -> bool
            
            IntPtr id: 
            Input viewport ID value
        """
        pass
    
    
    Geometry = None
    
    
    SequenceNumber = None
    
    
    Viewport = None
    
    
    ViewportObjectId = None
    
    pass

class ViewportGeometry(object):
    """
    
    ViewportGeometry()()
    
    
    """
    def DeviceContextPolygon(self):
        """
        DeviceContextPolygon -> bool
            
            Point3dCollection points: 
            Input list of points in the polygon, in display coordinates
        """
        pass
    
    
    def DeviceContextPolyline(self):
        """
        DeviceContextPolyline -> bool
            
            Point3dCollection points: 
            Input list of points in the polyline, in display coordinates
        """
        pass
    
    
    def DeviceContextRasterImage(self):
        """
        DeviceContextRasterImage -> bool
            
            Point3d origin: 
            Input image origin
            
            Vector3d u: 
            Input image "width" orientation
            
            Vector3d v: 
            Input image "height" orientation
            
            Matrix2d pixel: 
            Input image's pixel coordinate to display coordinate transformation matrix (2D)
            
            ObjectId entityId: 
            Input objectId of the image entity
            
            ImageOrg imageOrg: 
            Input ImageOrg Enumerated Type image organization enum value
            
            int imageWidth: 
            Input source image width in pixels
            
            int imageHeight: 
            Input source image height in pixels
            
            short imageColorDepth: 
            Input number of colors used in the image (2 to the color depth power)
            
            [MarshalAs(UnmanagedType.U1)] bool transparency: 
            Input Boolean indicating whether or not the image contains transparent regions
            
            Autodesk.AutoCAD.GraphicsInterface.ImageSource source: 
            Input value indicating image source
            
            Vector3d unRotated: 
            Input non-rotated image origin
            
            ImageOrg originalImage: 
            Input original image organization
            
            Matrix2d unRotatedPixel: 
            Input unrotated pixel-to-DC transformation matrix (2D)
            
            int unRotatedImageWidth: 
            Input unrotated source image width (in pixels)
            
            int unRotatedImageHeight: 
            Input unrotated source image height (in pixels)
        """
        pass
    
    
    def PolygonEye(self):
        """
        PolygonEye -> bool
            
            Point3dCollection points: 
            Input list of points in the polygon, in eye coordinates
        """
        pass
    
    
    def PolylineEye(self):
        """
        PolylineEye -> bool
            
            Point3dCollection points: 
            Input list of points in the polyline, in eye coordinates
        """
        pass
    
    pass

class ViewportTraits(object):
    """
    
    ViewportTraits()
    """
    AmbientLightColor = None
    
    
    Background = None
    
    
    Brightness = None
    
    
    Contrast = None
    
    
    DefaultLightingOn = None
    
    
    DefaultLightingType = None
    
    
    RenderEnvironment = None
    
    
    RenderSettings = None
    
    
    ToneOperatorParameters = None
    
    pass

class VisualStyle(object):
    """
    
    VisualStyle()
        Autodesk.AutoCAD.GraphicsInterface.VisualStyleType type : Input the type of visual style to configure
    
    
    """
    def GetPropertyType(self):
        """
        GetPropertyType -> Autodesk.AutoCAD.GraphicsInterface.VariantType
            
            VisualStyleProperty prop: 
            Input enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty.
        """
        pass
    
    
    def GetTrait(self):
        """
        GetTrait -> object
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to get from the visual style.
        """
        pass
    
    
    def GetTraitFlag(self):
        """
        GetTraitFlag -> bool
            
            uint modopt(IsLong) flagVal: 
            Input bit flag enum unsigned long property to get from the visual style.
            
            flagProp: 
            Input bitfield enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty for the property flag being queried.
        """
        pass
    
    
    def Operation(self):
        """
        Operation -> VisualStyleOperation
            
            VisualStyleProperty prop: 
            The property whose operation is to be queried.
        """
        pass
    
    
    def SetTrait(self):
        """
        SetTrait(VisualStyleProperty, Autodesk.AutoCAD.Colors.Color, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceMonoColorEdgeIntersectionColorEdgeObscuredColorEdgeColorEdgeSilhouetteColor
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
            
            pColor: 
            Input AcCmColor property value to set.
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
        SetTrait(VisualStyleProperty, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty for which the operation is being set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use for the property.
        """
        pass
    
    
    def SetTraitFlag(self):
        """
        SetTraitFlag -> void
            
            uint modopt(IsLong) flagVal: 
            Input bit flag enum unsigned long property to set into the visual style.
            
            [MarshalAs(UnmanagedType.U1)] bool bEnable: 
            Input bool set to true to enable the flag, false to disable.
            
            flagProp: 
            Input bitfield enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set into the visual style.
        """
        pass
    
    
    Type = None
    
    pass

class VisualStyleOperation():
    Disable = 2
    Enable = 3
    Inherit = 0
    InvalidOperation = -1
    Set = 1

class VisualStyleProperty():
    BloomEffect = 0x23
    BloomIntensity = 50
    BloomRadius = 0x2b
    BloomThreshold = 0x2a
    BlurAmount = 0x25
    BlurEffect = 0x21
    Color = 0x33
    DepthOfField = 0x37
    DisplayBrightness = 0x1a
    DisplayShadowType = 0x1b
    DisplayStyle = 0x19
    EdgeColor = 15
    EdgeCreaseAngle = 13
    EdgeHaloGap = 0x16
    EdgeHidePrecision = 0x18
    EdgeIntersectionColor = 9
    EdgeIntersectionLinePattern = 12
    EdgeIsolines = 0x17
    EdgeJitterAmount = 0x13
    EdgeModel = 7
    EdgeModifier = 14
    EdgeObscuredColor = 10
    EdgeObscuredLinePattern = 11
    EdgeOpacity = 0x10
    EdgeOverhang = 0x12
    EdgeSilhouetteColor = 20
    EdgeSilhouetteWidth = 0x15
    EdgeStyle = 8
    EdgeTexturePath = 0x36
    EdgeWidth = 0x11
    EdgeWiggleAmount = 0x35
    FaceAdjustment = 0x2d
    FaceColorMode = 2
    FaceLightingModel = 0
    FaceLightingQuality = 1
    FaceModifier = 3
    FaceMonoColor = 6
    FaceOpacity = 4
    FaceSpecular = 5
    FocusDistance = 0x38
    FocusWidth = 0x39
    InvalidProperty = -1
    LightingEnabled = 30
    MonoEffect = 0x20
    PastelEffect = 0x24
    PencilAngle = 0x26
    PencilColor = 0x29
    PencilEffect = 0x22
    PencilPattern = 40
    PencilScale = 0x27
    PostBrightness = 0x2f
    PostContrast = 0x2e
    PosterizeEffect = 0x1f
    PostPower = 0x30
    PropertyCount = 0x3a
    TintColor = 0x2c
    TintEffect = 0x31
    Transparency = 0x34
    UseDrawOrder = 0x1c
    ViewportTransparency = 0x1d

class VisualStyleTraits(object):
    """
    
    """
    AcGiVisualStyle = None
    
    pass

class VisualStyleType():
    Basic = 7
    Brighten = 12
    ColorChange = 0x10
    Conceptual = 9
    Custom = 10
    Dim = 11
    DisplayOnly = 0x13
    EdgeColorOff = 0x16
    EdgeOnly = 0x12
    EmptyStyle = 0x1f
    FaceOnly = 0x11
    FacePattern = 15
    Flat = 0
    FlatWithEdges = 1
    Gouraud = 2
    GouraudWithEdges = 3
    Hidden = 6
    JitterOff = 20
    LinePattern = 14
    OverhangOff = 0x15
    Realistic = 8
    Shaded = 0x1b
    ShadedWithEdges = 0x1a
    ShadesOfGray = 0x17
    Sketchy = 0x18
    Thicken = 13
    Wireframe2D = 4
    Wireframe3D = 5
    XRay = 0x19

class WebFileType():
    TypeA = 3
    TypeB = 2
    TypeC = 1

class WebLightTraits(object):
    """
    
    WebLightTraits()
    """
    WebFile = None
    
    
    WebFileType = None
    
    
    WebFlux = None
    
    
    WebHorzAng90to270 = None
    
    
    WebRotation = None
    
    
    WebSymmetry = None
    
    pass

class WebSymmetry():
    NoSymmetry = None
    SingleSymmetry = None
    DoubleSymmetry = None
    AxialSymmetry = None

class WoodTexture(object):
    """
    
    WoodTexture()
    """
    def Clone(self):
        """
        Clone -> WoodTexture
        
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
    
    
    def Set(self):
        """
        Set -> void
            
            WoodTexture value: 
            Input new texture value
        """
        pass
    
    
    AxialNoise = None
    
    
    Color1 = None
    
    
    Color2 = None
    
    
    GrainThickness = None
    
    
    RadialNoise = None
    
    pass

class WorldGeometry(object):
    """
    
    WorldGeometry()()
    
    
    """
    def SetExtents(self):
        """
        SetExtents -> void
            
            Extents3d extents: 
            Input an array of two points.
        """
        pass
    
    
    def StartAttributesSegment(self):
        """
        StartAttributesSegment -> void
        
        """
        pass
    
    pass