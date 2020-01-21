class CertificationData(public sealed class CertificationData):
    """
    
    """

    pass

class ClientViewInfo(public struct ClientViewInfo {
}):
    """
    
    C
    
    l
    
    i
    
    e
    
    n
    
    t
    
    V
    
    i
    
    e
    
    w
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
    AcadWindowId = None
    
    
    ViewportId = None
    
    
    ViewportObjectId = None
    
    pass

class Configuration(DisposableWrapper):
    """
    
    C
    
    o
    
    n
    
    f
    
    i
    
    g
    
    u
    
    r
    
    a
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    """
    def Configure(self):
        """
        Configure -> bool
        
        """
        pass
    
    
    def DegradationChainPosition(self):
        """
        DegradationChainPosition -> Integer
            
            Autodesk.AutoCAD.GraphicsSystem.DegradationChannel channel: 
            Input the degradation position will be returned.
        """
        pass
    
    
    def DegradationChannelAt(self):
        """
        DegradationChannelAt -> Autodesk.AutoCAD.GraphicsSystem.DegradationChannel
            
            int order: 
            Input for which degradation channel will be returned.
        """
        pass
    
    
    def GetCanDegradeChannel(self):
        """
        GetCanDegradeChannel -> bool
            
            Autodesk.AutoCAD.GraphicsSystem.DegradationChannel channel: 
            Input object to query.
        """
        pass
    
    
    def GetCertificationData(self):
        """
        GetCertificationData -> Autodesk.AutoCAD.GraphicsSystem.CertificationData
        
        """
        pass
    
    
    def GetEffectList(self):
        """
        GetEffectList -> List<Autodesk.AutoCAD.GraphicsSystem.EffectStatus>
            
            Autodesk.AutoCAD.GraphicsSystem.EffectListType type: 
            Type of desired list.
        """
        pass
    
    
    def GetFeatureAvailableVal(self):
        """
        GetFeatureAvailableVal -> Integer
        
        """
        pass
    
    
    def GetFeatureRecommendedVal(self):
        """
        GetFeatureRecommendedVal -> Integer
        
        """
        pass
    
    
    def GetFeatureUsedVal(self):
        """
        GetFeatureUsedVal -> Integer
        
        """
        pass
    
    
    def GetHardwareAcceleratedDrivers(self):
        """
        GetHardwareAcceleratedDrivers -> DriverInfo()
        
        """
        pass
    
    
    def GetVirtualDeviceName(self):
        """
        GetVirtualDeviceName -> string
        
        """
        pass
    
    
    def IsFeatureAvailable(self):
        """
        IsFeatureAvailable -> bool
            
            UniqueString feature: 
            Input input feature.
        """
        pass
    
    
    def IsFeatureEnabled(self):
        """
        IsFeatureEnabled -> bool
            
            UniqueString feature: 
            Input input feature.
        """
        pass
    
    
    def IsFeatureRecommended(self):
        """
        IsFeatureRecommended -> bool
            
            UniqueString feature: 
            Input hardware feature to query.
        """
        pass
    
    
    def IsHardwareAccelerationAvailable(self):
        """
        IsHardwareAccelerationAvailable -> bool
        
        """
        pass
    
    
    def IsHardwareAccelerationEnabled(self):
        """
        IsHardwareAccelerationEnabled -> bool
        
        """
        pass
    
    
    def IsHardwareAccelerationRecommended(self):
        """
        IsHardwareAccelerationRecommended -> bool
        
        """
        pass
    
    
    def IsNoHardwareOverrideEnabled(self):
        """
        IsNoHardwareOverrideEnabled -> bool
        
        """
        pass
    
    
    def SetCanDegradeChannel(self):
        """
        SetCanDegradeChannel -> void
            
            Autodesk.AutoCAD.GraphicsSystem.DegradationChannel channel: 
            Input degradation channel whose status is to be changed.
            
            [MarshalAs(UnmanagedType.U1)] bool degrade: 
            Input degradation channel status.
        """
        pass
    
    
    def SetFeatureEnabled(self):
        """
        SetFeatureEnabled -> void
            
            UniqueString feature: 
            Input feature to be enabled.
            
            [MarshalAs(UnmanagedType.U1)] bool enable: 
            Input Boolean to enable or disable the feature.
        """
        pass
    
    
    def SetFeatureUsedVal(self):
        """
        SetFeatureUsedVal -> void
        
        """
        pass
    
    
    def setHardwareAcceleration(self):
        """
        setHardwareAcceleration -> void
        
        """
        pass
    
    
    def ShiftDegradationChainPosition(self):
        """
        ShiftDegradationChainPosition -> void
            
            Autodesk.AutoCAD.GraphicsSystem.DegradationChannel channel: 
            Input Autodesk.AutoCAD.GraphicsSystem.DegradationChannel object.
            
            [MarshalAs(UnmanagedType.U1)] bool shiftDown: 
            Input.
        """
        pass
    
    
    def ShowConfigDialog(self):
        """
        ShowConfigDialog -> bool
        
        """
        pass
    
    
    AdaptiveDegradation = None
    
    
    CurrentDisplayDriver = None
    
    
    CurveTessellationTolerance = None
    
    
    DefaultHardwareAcceleratedDriver = None
    
    
    DiscardBackFaces = None
    
    
    DriverName = None
    
    
    DriverRevision = None
    
    
    DriverSearchPath = None
    
    
    DriverVersion = None
    
    
    DynamicTessellation = None
    
    
    FrameRate = None
    
    
    GenerateVertexNormals = None
    
    
    Handedness = None
    
    
    HardwareAcceleratedDriver = None
    
    
    MaxLODs = None
    
    
    RedrawOnWindowExpose = None
    
    
    SurfaceTessellationTolerance = None
    
    
    Transparency = None
    
    pass

class DefaultLightingType():
    OneLight
    TwoLights

class DegradationChannel():
    ViewportDraw
    LineAntialias
    Lighting
    TransparencyQuality
    ShadowsFull
    Transparency
    DiscardBackfaces
    ShadowsGround
    EdgeStyles
    FacetEdges
    FastSilhouette
    Textures
    Materials
    LightingQuality
    Backgrounds
    IntersectEdges
    Faceted
    Wireframe
    DegradationChannels

class Device(DisposableWrapper):
    """
    
    D
    
    e
    
    v
    
    i
    
    c
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> bool
            
            View view: 
            Input view to be displayed on the device.
        """
        pass
    
    
    def Erase(self):
        """
        Erase -> bool
            
            View view: 
            Input view to be removed from the device.
        """
        pass
    
    
    def EraseAll(self):
        """
        EraseAll -> void
        
        """
        pass
    
    
    def GetSnapshot(self):
        """
        GetSnapshot -> Bitmap
            
            Rectangle rectangle: 
            Input region of snapshot.
        """
        pass
    
    
    def Invalidate(self):
        """
        Invalidate() -> void
        
        """
        pass
    
    
    def OnDisplayChange(self):
        """
        OnDisplayChange -> void
            
            int bitsPerPixel: 
            Input new number of bits per pixel.
            
            int xRes: 
            Input X resolution.
            
            int yRes: 
            Input Y resolution.
        """
        pass
    
    
    def OnRealizeBackgroundPalette(self):
        """
        OnRealizeBackgroundPalette -> void
        
        """
        pass
    
    
    def OnRealizeForegroundPalette(self):
        """
        OnRealizeForegroundPalette -> void
        
        """
        pass
    
    
    def OnSize(self):
        """
        OnSize -> void
            
            Size size: 
            Input width and height of device in pixels.
        """
        pass
    
    
    def SetLogicalPalette(self):
        """
        SetLogicalPalette -> void
            
            System.Drawing.Color[] palette: 
            Input array of logical palette colors.
        """
        pass
    
    
    def SetPhysicalPalette(self):
        """
        SetPhysicalPalette -> void
            
            System.Drawing.Color[] palette: 
            Input array that constitutes the palette.
        """
        pass
    
    
    def Update(self):
        """
        Update() -> void
        
        """
        pass
    
    
    BackgroundColor = None
    
    
    DeviceRenderType = None
    
    
    IsValid = None
    
    pass

class DriverInfo(public struct DriverInfo {
}):
    """
    
    D
    
    r
    
    i
    
    v
    
    e
    
    r
    
    I
    
    n
    
    f
    
    o
    
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
    
     
    
    h
    
    a
    
    r
    
    d
    
    w
    
    a
    
    r
    
    e
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
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
    
     
    
    s
    
    e
    
    t
    
    s
    
     
    
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
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
    s
    
    u
    
    p
    
    p
    
    o
    
    r
    
    t
    
    s
    
     
    
    h
    
    a
    
    r
    
    d
    
    w
    
    a
    
    r
    
    e
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    u
    
    l
    
    l
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
    f
    
    i
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
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
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
    f
    
    i
    
    l
    
    e
    
    
    
    
    
    
    
    
    
    
    D
    
    r
    
    i
    
    v
    
    e
    
    r
    
    I
    
    n
    
    f
    
    o
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    u
    
    l
    
    l
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
    f
    
    i
    
    l
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
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
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    r
    
    i
    
    v
    
    e
    
    r
    
     
    
    f
    
    i
    
    l
    
    e
    """
    Driver = None
    
    
    HardwareAccelerated = None
    
    
    Path = None
    
    pass

class EffectListType():
    kEL_Current
    kEL_RegistryHardware
    kEL_RegistrySoftware
    kEL_File
    kEL_HardwareBasic
    kEL_HardwareMedium
    kEL_HardwareAdvanced

class EffectStatus(public class EffectStatus):
    """
    
    """
    Available = None
    
    
    EffectName = None
    
    
    EffectUniqueString = None
    
    
    Enabled = None
    
    
    FeatureLevel = None
    
    
    Recommended = None
    
    pass

class ErrorStatus():
    Success
    OutOfRange
    InvalidInput

class GraphicsKernel(DisposableWrapper):
    """
    
    G
    
    r
    
    a
    
    p
    
    h
    
    i
    
    c
    
    s
    
    K
    
    e
    
    r
    
    n
    
    e
    
    l
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    G
    
    r
    
    a
    
    p
    
    h
    
    i
    
    c
    
    s
    
    K
    
    e
    
    r
    
    n
    
    e
    
    l
    
    (
    
    I
    
    n
    
    t
    
    P
    
    t
    
    r
    
    )
    
    (
    
    )
    """
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetImpObj(self):
        """
        GetImpObj -> AcGiGraphicsKernel*
        
        """
        pass
    
    pass

class Handedness():
    Left
    Right

class HighlightStyle():
    HighlightDashed

class InvalidationHint():
    InvalidateNone
    InvalidateIsolines
    InvalidateViewportCache
    InvalidateAll
    InvalidateAllStatic
    InvalidateFacets
    InvalidateFills
    InvalidateLinetypes
    InvalidateMaterials

class KernelDescriptor(DisposableWrapper):
    """
    
    """
    Drawing2D Field = None
    
    
    Drawing3D Field = None
    
    
    RapidRTRendering3D Field = None
    
    
    Selection3D Field = None
    
    
    def addRequirement(self):
        """
        addRequirement -> void
            
            ^capability: 
            String describing the graphics capability
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetImpObj(self):
        """
        GetImpObj -> AcGiKernelDescriptor*
        
        """
        pass
    
    
    def supports(self):
        """
        supports -> bool
            
            UniqueString capability: 
            String describing the graphics capability.
        """
        pass
    
    pass

class LinePattern():
    DashDot = 3
    Dashed = 1
    DefaultLinePattern = 2
    Dotted = 2
    DoubleLongDash = 9
    DoubleMediumDash = 8
    DoubleShortDash = 7
    LongDash = 6
    LongDashDot = 14
    LongDashDotDot = 13
    LongDashShortDash = 12
    MediumDash = 5
    MediumDashDotShortDashDot = 15
    MediumDashShortDashShortDash = 11
    MediumLongDash = 10
    ShortDash = 4
    Solid = 0
    SparseDot = 0x10

class LineWeight():
    kLnWt000 = 0
    kLnWt005 = 5
    kLnWt009 = 9
    kLnWt013 = 13
    kLnWt015 = 15
    kLnWt018 = 0x12
    kLnWt020 = 20
    kLnWt025 = 0x19
    kLnWt030 = 30
    kLnWt035 = 0x23
    kLnWt040 = 40
    kLnWt050 = 50
    kLnWt053 = 0x35
    kLnWt060 = 60
    kLnWt070 = 70
    kLnWt080 = 80
    kLnWt090 = 90
    kLnWt100 = 100
    kLnWt106 = 0x6a
    kLnWt120 = 120
    kLnWt140 = 140
    kLnWt158 = 0x9e
    kLnWt200 = 200
    kLnWt211 = 0xd3
    kLnWtByBlock = -2
    kLnWtByLayer = -1
    kLnWtByLwDefault = -3

class Manager(DisposableWrapper):
    """
    
    """
    def AcquireGraphicsKernel(self):
        """
        AcquireGraphicsKernel -> GraphicsKernel
            
            KernelDescriptor desc: 
            A descriptor defining the required capabilities of the kernel.
        """
        pass
    
    
    def CreateAutoCADDevice(self):
        """
        CreateAutoCADDevice -> Device
            
            IntPtr hwnd: 
            Input window handle.
            
            kernel: 
            Graphics Kernel used to create the resource
        """
        pass
    
    
    def CreateAutoCADModel(self):
        """
        CreateAutoCADModel -> Model
            
            kernel: 
            Graphics Kernel used to create resource.
        """
        pass
    
    
    def CreateAutoCADOffScreenDevice(self):
        """
        CreateAutoCADOffScreenDevice -> Device
            
            kernel: 
            Graphics Kernel used to create the resource
        """
        pass
    
    
    def CreateAutoCADView(self):
        """
        CreateAutoCADView -> View
            
            Drawable drawable: 
            Input Drawable
            
            kernel: 
            Graphics Kernel used to create the resource
        """
        pass
    
    
    def CreateAutoCADViewport(self):
        """
        CreateAutoCADViewport -> View
            
            ViewportTableRecord vp: 
            Input ViewportTableRecord
        """
        pass
    
    
    def CreateView(self):
        """
        CreateView -> View
        
        """
        pass
    
    
    def CreateViewport(self):
        """
        CreateViewport -> View
        
        """
        pass
    
    
    def DestroyView(self):
        """
        DestroyView -> void
        
        """
        pass
    
    
    def GetCurrent3dAcGsView(self):
        """
        GetCurrent3dAcGsView -> View
        
        """
        pass
    
    
    def GetCurrentAcGsView(self):
        """
        GetCurrentAcGsView -> View
        
        """
        pass
    
    
    def GetDBModel(self):
        """
        GetDBModel -> Model
            
            kernel: 
            Graphics Kernel used to query for the resource.
        """
        pass
    
    
    def GetGsModel(self):
        """
        GetGsModel -> Model
            
            TransientDrawingMode mode: 
            Input drawing mode
            
            int subDrawingMode: 
            Input the sub drawing mode of specified drawing mode
            
            int viewportNumber: 
            Input viewport identification number (this is the same type of number returned by the CVPORT system variable)
        """
        pass
    
    
    def GetGUIDevice(self):
        """
        GetGUIDevice -> Device
            
            kernel: 
            Graphics Kernel used to query for the device.
        """
        pass
    
    
    def GetOffScreenDevice(self):
        """
        GetOffScreenDevice -> Device
        
        """
        pass
    
    
    def GetOffScreenView(self):
        """
        GetOffScreenView -> View
        
        """
        pass
    
    
    def ObtainAcGsView(self):
        """
        ObtainAcGsView -> View
            
            int viewportNumber: 
            Input viewport number
            
            KernelDescriptor createIfNone: 
            Input true if the graphics system associated with the viewport ought to be created if it does not exist
        """
        pass
    
    
    def ReleaseGraphicsKernel(self):
        """
        ReleaseGraphicsKernel -> void
            
            GraphicsKernel kernel: 
            Graphics Kernel to release<
        """
        pass
    
    
    def SetViewFromViewport(self):
        """
        SetViewFromViewport -> void
            
            View view: 
            Input view to set
            
            int viewportNumber: 
            Input viewport
        """
        pass
    
    
    def SetViewportFromView(self):
        """
        SetViewportFromView(int, View) -> void
            
            int viewportNumber: 
            Input viewport number to set
            
            View view: 
            Input view to set from
        SetViewportFromView(int, View, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int viewportNumber: 
            Input viewport number to set
            
            View view: 
            Input view to set from
            
            [MarshalAs(UnmanagedType.U1)] bool regenRequired: 
            Input true if regen is required for the viewport
            
            [MarshalAs(UnmanagedType.U1)] bool rescaleRequired: 
            Input true if rescale is required for the viewport
            
            [MarshalAs(UnmanagedType.U1)] bool syncRequired: 
            Input true if synching is required for the viewport
        """
        pass
    
    
    DeviceIndependentDisplaySize = None
    
    pass

class Model(DisposableWrapper):
    """
    
    M
    
    o
    
    d
    
    e
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    R
    
    e
    
    n
    
    d
    
    e
    
    r
    
    T
    
    y
    
    p
    
    e
    
     
    
    r
    
    e
    
    n
    
    d
    
    e
    
    r
    
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
    
     
    
    r
    
    e
    
    n
    
    d
    
    e
    
    r
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
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
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    o
    
    d
    
    e
    
    l
    """
    def AddSceneGraphRoot(self):
        """
        AddSceneGraphRoot -> bool
            
            Drawable pRoot: 
            Input object that is a scene graph root.
        """
        pass
    
    
    def EraseSceneGraphRoot(self):
        """
        EraseSceneGraphRoot -> bool
            
            Drawable pRoot: 
            Input object that was a scene graph root.
        """
        pass
    
    
    def Invalidate(self):
        """
        Invalidate -> void
            
            Autodesk.AutoCAD.GraphicsSystem.InvalidationHint hint: 
            Input hint about the invalidation required.
        """
        pass
    
    
    def OnAdded(self):
        """
        OnAdded(Drawable, Drawable) -> void
            
            Drawable added: 
            Input object that has been added to the database.
            
            Drawable parent: 
            Input optional Drawable parent.
        OnAdded(Drawable, int modopt(IsLong)) -> void
            
            Drawable added: 
            Input object that has been added to the database.
            
            int modopt(IsLong) parentId: 
            Input optional parent.
        """
        pass
    
    
    def OnErased(self):
        """
        OnErased(Drawable, Drawable) -> void
            
            Drawable erased: 
            Input object that has been removed from the database.
            
            Drawable parent: 
            Input optional Drawable parent.
        OnErased(Drawable, int modopt(IsLong)) -> void
            
            Drawable erased: 
            Input object that has been removed from the database.
            
            int modopt(IsLong) parentId: 
            Input optional parent.
        """
        pass
    
    
    def OnModified(self):
        """
        OnModified(Drawable, Drawable) -> void
            
            Drawable modified: 
            Input object that has been modified.
            
            Drawable parent: 
            Input optional Drawable parent.
        OnModified(Drawable, int modopt(IsLong)) -> void
            
            Drawable modified: 
            Input object that has been modified.
            
            int modopt(IsLong) parentId: 
            Input optional Drawable parent.
        """
        pass
    
    
    def OnPaletteModified(self):
        """
        OnPaletteModified -> void
        
        """
        pass
    
    
    def SetExtents(self):
        """
        SetExtents -> void
            
            Point3d point3dx: 
            Not implemented
            
            Point3d point3dy: 
            Not implemented
        """
        pass
    
    
    def SetSectioning(self):
        """
        SetSectioning(Point3dCollection, Vector3d) -> bool
            
            Point3dCollection pts: 
            Input array of co-planar points specifying a sectioning region.
            
            Vector3d upVector: 
            Input object that specifies the orientation of the plane containing pts.
        SetSectioning(Point3dCollection, Vector3d, double, double) -> bool
            
            Point3dCollection pts: 
            Input array of co-planar points specifying a sectioning region.
            
            Vector3d upVector: 
            Input object that specifies the orientation of the plane containing pts.
            
            double top: 
            Input that specifies the top capping height of the sectioning.
            
            double bottom: 
            Input that specifies the bottom capping height of the sectioning.
        """
        pass
    
    
    BackgroundId = None
    
    
    EnableSectioning = None
    
    
    LinetypesEnabled = None
    
    
    RenderType = None
    
    
    SectioningVisualStyle = None
    
    
    Selectable = None
    
    
    ShadowPlaneLocation = None
    
    
    Transform = None
    
    
    ViewClippingOverride = None
    
    
    VisualStyle = None
    
    
    VisualStyleId = None
    
    pass

class Node(DisposableWrapper):
    """
    
    """
    Drawable = None
    
    pass

class Projection():
    Parallel
    Perspective

class Quality():
    LowQuality
    MediumQuality
    HighQuality

class RenderType():
    Main
    Sprite
    Direct
    Highlight
    HighlightSelection
    DirectTopmost
    Contrast
    Count

class RendererType():
    Default
    Software
    SoftwareNewViewsOnly
    FullRender
    SelectionRender

class StereoParameters(public struct StereoParameters {
}):
    """
    
    S
    
    t
    
    e
    
    r
    
    e
    
    o
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    m
    
    a
    
    g
    
    n
    
    i
    
    t
    
    u
    
    d
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    a
    
    g
    
    n
    
    i
    
    t
    
    u
    
    d
    
    e
    
     
    
    o
    
    f
    
     
    
    v
    
    i
    
    e
    
    w
    
     
    
    s
    
    e
    
    p
    
    a
    
    r
    
    a
    
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
    
    r
    
    a
    
    l
    
    l
    
    a
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    a
    
    l
    
    l
    
    a
    
    x
    """
    Magnitude = None
    
    
    Parallax = None
    
    pass

class View(DisposableWrapper):
    """
    
    V
    
    i
    
    e
    
    w
    
    (
    
    )
    
    (
    
    )
    """
    def Add(self):
        """
        Add -> bool
            
            Drawable drawable: 
            Input root of scene graph.
            
            Model model: 
            Input object to which all notifications for the above scene graph are directed.
        """
        pass
    
    
    def BeginInteractivity(self):
        """
        BeginInteractivity -> void
            
            double frameRateInHZ: 
            Input desired frame rate per second.
        """
        pass
    
    
    def ClearFrozenLayers(self):
        """
        ClearFrozenLayers -> void
        
        """
        pass
    
    
    def Clone(self):
        """
        Clone() -> View
        
        """
        pass
    
    
    def Dolly(self):
        """
        Dolly(Vector3d) -> void
            
            Vector3d vector: 
            Input camera space dolly vector.
        Dolly(double, double, double) -> void
            
            double y: 
            Input Camera space y dolly amount.
            
            double z: 
            Input Camera space z dolly amount.
        """
        pass
    
    
    def EnableDefaultLighting(self):
        """
        EnableDefaultLighting([MarshalAs(UnmanagedType.U1)] bool) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool bEnable: 
            Input flag to enable or disable default lighting.
        EnableDefaultLighting([MarshalAs(UnmanagedType.U1)] bool, Autodesk.AutoCAD.GraphicsSystem.DefaultLightingType) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool bEnable: 
            Input flag to enable or disable default lighting.
            
            Autodesk.AutoCAD.GraphicsSystem.DefaultLightingType type: 
            Input type of default lighting to use.
        """
        pass
    
    
    def EndInteractivity(self):
        """
        EndInteractivity -> void
        
        """
        pass
    
    
    def Erase(self):
        """
        Erase -> bool
            
            Drawable drawable: 
            Input object to be removed from the view.
        """
        pass
    
    
    def EraseAll(self):
        """
        EraseAll -> void
        
        """
        pass
    
    
    def ExtentsInView(self):
        """
        ExtentsInView -> bool
            
            Point3d minPoint: 
            Input WCS point of the corner of the bounding box extents.
            
            Point3d maxPoint: 
            Input WCS point of the corner of the bounding box extents.
        """
        pass
    
    
    def Flush(self):
        """
        Flush -> void
        
        """
        pass
    
    
    def FreezeLayer(self):
        """
        FreezeLayer(IntPtr) -> void
            
            IntPtr layerId: 
            Input Layer to be treated as frozen.
        FreezeLayer(long) -> void
            
            long layerId: 
            Input Layer to be treated as frozen.
        """
        pass
    
    
    def GetModel(self):
        """
        GetModel -> Model
            
            Drawable drw: 
            The drawable object.
        """
        pass
    
    
    def GetModelList(self):
        """
        GetModelList -> Model()
        
        """
        pass
    
    
    def GetNumPixelsInUnitSquare(self):
        """
        GetNumPixelsInUnitSquare(Point3d) -> Point2d
            
            Point3d givenWorldpt: 
            Input WCS point for the center point of the display coordinate unit square.
        GetNumPixelsInUnitSquare(Point3d, [MarshalAs(UnmanagedType.U1)] bool) -> Point2d
            
            Point3d givenWorldpt: 
            Input WCS point for the center point of the display coordinate unit square.
            
            [MarshalAs(UnmanagedType.U1)] bool includePerspective: 
            Input indicating perspective mode.
        """
        pass
    
    
    def GetSnapshot(self):
        """
        GetSnapshot -> Bitmap
            
            Rectangle rectangle: 
            Input region used by snapshot.
        """
        pass
    
    
    def Hide(self):
        """
        Hide -> void
        
        """
        pass
    
    
    def Invalidate(self):
        """
        Invalidate() -> void
        
        """
        pass
    
    
    def InvalidateCachedViewportGeometry(self):
        """
        InvalidateCachedViewportGeometry -> void
        
        """
        pass
    
    
    def Orbit(self):
        """
        Orbit -> void
            
            double y: 
            Input up vector.
        """
        pass
    
    
    def Pan(self):
        """
        Pan -> void
            
            double y: 
            Input up vector
        """
        pass
    
    
    def PointInView(self):
        """
        PointInView -> bool
            
            Point3d point: 
            Input WCS point to test.
        """
        pass
    
    
    def RemoveViewportClipRegion(self):
        """
        RemoveViewportClipRegion -> void
        
        """
        pass
    
    
    def RenderToImage(self):
        """
        RenderToImage() -> Bitmap
        
        RenderToImage(Drawable, Rectangle) -> Bitmap
            
            Drawable settings: 
            Input for the graphics settings
            
            Rectangle rectScreen: 
            Input for the rectangle in device coordinates
        RenderToImage(Drawable, Rectangle, [MarshalAs(UnmanagedType.U1)] bool) -> Bitmap
            
            Drawable settings: 
            Input for the graphics settings
            
            Rectangle rectScreen: 
            Input for the rectangle in device coordinates
            
            [MarshalAs(UnmanagedType.U1)] bool flipImage: 
            Input that specifies whether the rendered image should be flipped
        """
        pass
    
    
    def Roll(self):
        """
        Roll -> void
            
            double angle: 
            Input angular rotation about the eye vector in radians.
        """
        pass
    
    
    def SetView(self):
        """
        SetView(Point3d, Point3d, Vector3d, double, double) -> void
            
            Point3d position: 
            Input camera position.
            
            Point3d target: 
            Input camera target.
            
            Vector3d upVector: 
            Input camera up vector.
            
            double fieldWidth: 
            Input width of the projection plane.
            
            double fieldHeight: 
            Input height of the projection plane.
        SetView(Point3d, Point3d, Vector3d, double, double, Autodesk.AutoCAD.GraphicsSystem.Projection) -> void
            
            Point3d position: 
            Input camera position.
            
            Point3d target: 
            Input camera target.
            
            Vector3d upVector: 
            Input camera up vector.
            
            double fieldWidth: 
            Input width of the projection plane
            
            double fieldHeight: 
            Input height of the projection plane
            
            Autodesk.AutoCAD.GraphicsSystem.Projection projection: 
            Input parallel or perspective projection.
        """
        pass
    
    
    def SetViewportClipRegion(self):
        """
        SetViewportClipRegion -> void
            
            int contours: 
            Input number of polygonal contours and the size of the counts array.
            
            int[] counts: 
            Input array where each entry corresponds to the number of device coordinate points used to specify that contour in the points array. For example, counts[i] contains the number of points that represent the (ith + 1) polygonal contour.
            
            Point[] points: 
            Input array of points that specify polygonal contours.
        """
        pass
    
    
    def Show(self):
        """
        Show -> void
        
        """
        pass
    
    
    def ThawLayer(self):
        """
        ThawLayer(IntPtr) -> void
            
            IntPtr layerId: 
            Input Layer to be treated as thawed.
        ThawLayer(long) -> void
            
            long layerId: 
            Input Layer to be treated as thawed.
        """
        pass
    
    
    def Update(self):
        """
        Update -> void
        
        """
        pass
    
    
    def Zoom(self):
        """
        Zoom -> void
            
            double factor: 
            Input zoom factor.
        """
        pass
    
    
    def ZoomExtents(self):
        """
        ZoomExtents -> void
            
            Point3d minPoint: 
            Input WCS point representing the corner of the bounding box extents.
            
            Point3d maxPoint: 
            Input WCS point representing the corner of the bounding box extents.
        """
        pass
    
    
    def ZoomWindow(self):
        """
        ZoomWindow -> void
            
            Point2d lowerLeft: 
            Input screen coordinate of the lower-left point of the new zoom window.
            
            Point2d upperRight: 
            Input screen coordinate of the upper-right point of the new zoom window.
        """
        pass
    
    
    AcadWindowId = None
    
    
    BackClip = None
    
    
    BackgroundId = None
    
    
    Device = None
    
    
    EnableBackClip = None
    
    
    EnableFrontClip = None
    
    
    EnableStereo = None
    
    
    ExceededBounds = None
    
    
    FieldHeight = None
    
    
    FieldWidth = None
    
    
    FrontClip = None
    
    
    IsInteractive = None
    
    
    IsPerspective = None
    
    
    IsValid = None
    
    
    IsVisible = None
    
    
    ObjectToDeviceMatrix = None
    
    
    Position = None
    
    
    ProjectionMatrix = None
    
    
    ScreenMatrix = None
    
    
    StereoParameters = None
    
    
    Target = None
    
    
    UpVector = None
    
    
    ViewingMatrix = None
    
    
    ViewportBorderProperties = None
    
    
    ViewportBorderVisibility = None
    
    
    ViewportExtents = None
    
    
    ViewportId = None
    
    
    ViewportObjectId = None
    
    
    VisualStyle = None
    
    
    VisualStyleId = None
    
    
    WorldToDeviceMatrix = None
    
    pass

class ViewEventArgs(EventArgs):
    """
    
    V
    
    i
    
    e
    
    w
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    (
    
    )
    """
    View = None
    
    pass

class ViewUpdateEventArgs(EventArgs):
    """
    
    V
    
    i
    
    e
    
    w
    
    U
    
    p
    
    d
    
    a
    
    t
    
    e
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    (
    
    )
    """
    View = None
    
    
    viewUpdateFlags = None
    
    pass

class ViewUpdateFlags():
    CameraChanged = 1

class ViewportBorderProperties(public struct ViewportBorderProperties {
}):
    """
    
    V
    
    i
    
    e
    
    w
    
    p
    
    o
    
    r
    
    t
    
    B
    
    o
    
    r
    
    d
    
    e
    
    r
    
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
    
     
    
    d
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    w
    
    e
    
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
    
     
    
    d
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
     
    
    w
    
    e
    
    i
    
    g
    
    h
    
    t
    """
    Color = None
    
    
    Weight = None
    
    pass