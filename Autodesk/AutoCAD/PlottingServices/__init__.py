class AppPlotStatus():
    DwfFilePlotted = -3
    NoPlotYet = -1
    PlotHadErrors = 3
    PlotHadSystemError = 4
    PlotStart = 0
    PlotSuccessful = 2
    PlottingMessage = -2
    ViewPlotLog = 1

class BeginDocumentEventArgs(EventArgs):
    """
    
    B
    
    e
    
    g
    
    i
    
    n
    
    D
    
    o
    
    c
    
    u
    
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
    
    (
    
    )
    
    (
    
    )
    """
    DocumentName = None
    
    
    FileName = None
    
    
    PlotInfo = None
    
    
    PlotToFile = None
    
    pass

class BeginPageEventArgs(EventArgs):
    """
    
    B
    
    e
    
    g
    
    i
    
    n
    
    P
    
    a
    
    g
    
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
    
    (
    
    )
    """
    LastPage = None
    
    
    PlotInfo = None
    
    
    PlotPageInfo = None
    
    pass

class BeginPlotEventArgs(EventArgs):
    """
    
    B
    
    e
    
    g
    
    i
    
    n
    
    P
    
    l
    
    o
    
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
    
    (
    
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
    
    P
    
    l
    
    o
    
    t
    
    t
    
    i
    
    n
    
    g
    
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
    
    P
    
    r
    
    o
    
    g
    
    r
    
    e
    
    s
    
    s
    
     
    
    p
    
    r
    
    o
    
    g
    
    r
    
    e
    
    s
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    l
    
    o
    
    t
    
     
    
    p
    
    r
    
    o
    
    g
    
    r
    
    e
    
    s
    
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
    
    P
    
    l
    
    o
    
    t
    
    t
    
    i
    
    n
    
    g
    
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
    
    T
    
    y
    
    p
    
    e
    
     
    
    p
    
    l
    
    o
    
    t
    
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
    
     
    
    p
    
    l
    
    o
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    """
    PlotProgress = None
    
    
    PlotType = None
    
    pass

class CustomSizeResults():
    DeviceLoadFailed = 0x2000
    Exception = 0x100
    MustCreatePC3 = 1
    PC3DirReadOnly = 4
    PC3FileReadOnly = 0x40
    PmpDirMissing = 0x10
    PmpDirReadOnly = 8
    PmpFileReadOnly = 0x800
    Possible = 0
    RotationRequired = 2
    SizeTooBig = 0x80
    UnknownErrPC3File = 0x200
    UnknownErrPmpDir = 0x20
    UnknownErrPmpFile = 0x400
    WidthAndHeightMustBePositive = 0x1000

class DeviceType():
    OneOffConfig = 2
    PC3File = 1
    SystemPrinter = 0
    Uninitialized = -1

class DsdData(RXObject):
    """
    
    D
    
    s
    
    d
    
    D
    
    a
    
    t
    
    a
    
    (
    
    )
    """
    def Copy(self):
        """
        Copy -> DsdData
        
        """
        pass
    
    
    def GetDsdEntryCollection(self):
        """
        GetDsdEntryCollection -> DsdEntryCollection
        
        """
        pass
    
    
    def ReadDsd(self):
        """
        ReadDsd -> void
            
            string fileName: 
            Input path and file name of DSD file.
        """
        pass
    
    
    def SetDsdEntryCollection(self):
        """
        SetDsdEntryCollection -> void
            
            DsdEntryCollection entries: 
            Input array of sheet entries.
        """
        pass
    
    
    def SetUnrecognizedData(self):
        """
        SetUnrecognizedData(StringCollection, StringCollection) -> void
            
            StringCollection sectionNames: 
            Input array of customized (unrecognized) section headings.
            
            StringCollection sectionData: 
            Input array of customized (unrecognized) section data.
        SetUnrecognizedData(string, string) -> void
            
            string sectionName: 
            Input customized section name.
            
            string sectionData: 
            Input customized section data.
        """
        pass
    
    
    def WriteDsd(self):
        """
        WriteDsd -> void
            
            string fileName: 
            Input path and file name of DSD file.
        """
        pass
    
    
    CategoryName = None
    
    
    DestinationName = None
    
    
    Dwf3dOptions = None
    
    
    IsHomogeneous = None
    
    
    IsSheetSet = None
    
    
    LogFilePath = None
    
    
    MajorVersion = None
    
    
    MinorVersion = None
    
    
    NoOfCopies = None
    
    
    Password = None
    
    
    PlotStampOn = None
    
    
    ProjectPath = None
    
    
    SelectionSetName = None
    
    
    SheetSetName = None
    
    
    SheetType = None
    
    
    UnrecognizedDataSectionNames = None
    
    
    UnrecognizedDataSections = None
    
    pass

class DsdEntry(RXObject):
    """
    
    D
    
    s
    
    d
    
    E
    
    n
    
    t
    
    r
    
    y
    
    (
    
    )
    """
    def Copy(self):
        """
        Copy -> DsdEntry
        
        """
        pass
    
    
    DwgName = None
    
    
    Layout = None
    
    
    Nps = None
    
    
    NpsSourceDwg = None
    
    
    OriginalSheetPath = None
    
    
    Title = None
    
    pass

class DsdEntryCollection(DisposableWrapper, ICollection):
    """
    
    D
    
    s
    
    d
    
    E
    
    n
    
    t
    
    r
    
    y
    
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
            
            DsdEntry value: 
            Input object to be added.
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
            
            DsdEntry[] array: 
            Input target array.
            
            int index: 
            Input zero-based index from where the copy begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input location to where the value will be inserted.
            
            DsdEntry value: 
            Input object to be inserted.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input. Index of entry to remove.
        """
        pass
    
    
    Count = None
    
    pass

class Dwf3dOptions(public class Dwf3dOptions):
    """
    
    """
    GroupByXrefHierarchy = None
    
    
    PublishWithMaterials = None
    
    pass

class EndDocumentEventArgs(EventArgs):
    """
    
    E
    
    n
    
    d
    
    D
    
    o
    
    c
    
    u
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    l
    
    o
    
    t
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    o
    
    f
    
     
    
    d
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    """
    Status = None
    
    pass

class EndPageEventArgs(EventArgs):
    """
    
    E
    
    n
    
    d
    
    P
    
    a
    
    g
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    h
    
    e
    
    e
    
    t
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    o
    
    f
    
     
    
    d
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    """
    Status = None
    
    pass

class EndPlotEventArgs(EventArgs):
    """
    
    E
    
    n
    
    d
    
    P
    
    l
    
    o
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    l
    
    o
    
    t
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    o
    
    f
    
     
    
    d
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    """
    Status = None
    
    pass

class HostAppServices(public sealed class HostAppServices):
    """
    
    """
    def UpdatePlotJobStatus(self):
        """
        UpdatePlotJobStatus -> void
            
            AppPlotStatus status: 
            Input Autodesk.AutoCAD.PlottingServices..AppPlotStatus object reflecting the state of the plot.
            
            string message: 
            Input for a plot message or DWF file name.
        """
        pass
    
    
    PlotLogger = None
    
    pass

class MatchingPolicy():
    MatchDisabled = 1
    MatchEnabled = 2
    MatchEnabledCustom = 3
    MatchEnabledTemporaryCustom = 4

class MediaBounds(public struct MediaBounds {
}):
    """
    
    M
    
    e
    
    d
    
    i
    
    a
    
    B
    
    o
    
    u
    
    n
    
    d
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
    d
    
     
    
    p
    
    a
    
    g
    
    e
    
    S
    
    i
    
    z
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    i
    
    z
    
    e
    
     
    
    o
    
    f
    
     
    
    p
    
    a
    
    g
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
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
    
    P
    
    r
    
    i
    
    n
    
    t
    
    a
    
    b
    
    l
    
    e
    
    A
    
    r
    
    e
    
    a
    
     
    
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
    
    r
    
    i
    
    n
    
    t
    
    a
    
    b
    
    l
    
    e
    
     
    
    a
    
    r
    
    e
    
    a
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    i
    
    n
    
    t
    
    2
    
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
    
    P
    
    r
    
    i
    
    n
    
    t
    
    a
    
    b
    
    l
    
    e
    
    A
    
    r
    
    e
    
    a
    
     
    
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
    
    r
    
    i
    
    n
    
    t
    
    a
    
    b
    
    l
    
    e
    
     
    
    a
    
    r
    
    e
    
    a
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
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(MediaBounds) -> bool
            
            MediaBounds a: 
            Input object to compare against
        IsEqualTo(MediaBounds, Tolerance) -> bool
            
            MediaBounds a: 
            Input object to compare against
            
            Tolerance tolerance: 
            Input tolerance value
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
    
    
    LowerLeftPrintableArea = None
    
    
    PageSize = None
    
    
    UpperRightPrintableArea = None
    
    pass

class MergeStatus():
    CanonicalMediaName = 8
    CurrentStyleSheet = 0x80000
    DrawViewportsFirst = 0x400000
    NoChanges = 0
    PlotCentered = 0x400
    PlotConfigurationName = 1
    PlotHidden = 0x800
    PlotOrigin = 0x10
    PlotPaperMargins = 2
    PlotPaperSize = 4
    PlotPaperUnits = 0x20
    PlotPlotStyles = 0x80
    PlotRotation = 0x200
    PlotTransparency = 0x800000
    PlotType = 0x8000
    PlotViewName = 0x20000
    PlotViewportBorders = 0x40
    PlotWindowArea = 0x10000
    PrintLineWeights = 0x200000
    Scale = 0x40000
    ScaleLineWeights = 0x100000
    ShadePlot = 0x1000
    ShadePlotCustomDpi = 0x4000
    ShadePlotResLevel = 0x2000
    ShowPlotStyles = 0x100

class PlotCancelStatus():
    Continue
    CanceledByCaller
    CanceledByCancelAllButton

class PlotConfig(RXObject):
    """
    
    """
    def GetLocalMediaName(self):
        """
        GetLocalMediaName -> string
            
            string canonicalMediaName: 
            Input canonical name of the media size whose localized name is being requested.
        """
        pass
    
    
    def GetMediaBounds(self):
        """
        GetMediaBounds -> MediaBounds
            
            string canonicalMediaName: 
            Input name of the driver for the device or PC3 file.
        """
        pass
    
    
    def RefreshMediaNameList(self):
        """
        RefreshMediaNameList -> void
        
        """
        pass
    
    
    def SaveToPC3(self):
        """
        SaveToPC3 -> void
            
            string name: 
            Input PC3 file name.
        """
        pass
    
    
    CanonicalMediaNames = None
    
    
    Comment = None
    
    
    DefaultFileExtension = None
    
    
    DeviceName = None
    
    
    DriverName = None
    
    
    FullPath = None
    
    
    IsPlotToFile = None
    
    
    LocationName = None
    
    
    PlotToFileCapability = None
    
    
    PortName = None
    
    
    ServerName = None
    
    
    TagLine = None
    
    pass

class PlotConfigInfo(RXObject):
    """
    
    P
    
    l
    
    o
    
    t
    
    C
    
    o
    
    n
    
    f
    
    i
    
    g
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    DeviceName = None
    
    
    DeviceType = None
    
    
    FullPath = None
    
    pass

class PlotConfigInfoCollection(DisposableWrapper, ICollection, IEnumerable):
    """
    
    """
    def CopyTo(self):
        """
        CopyTo -> void
            
            PlotConfigInfo[] array: 
            Input target array.
            
            int index: 
            Input zero-based index from which the array is copied.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class PlotConfigManager(public sealed class PlotConfigManager):
    """
    
    """
    def SetCurrentConfig(self):
        """
        SetCurrentConfig -> PlotConfig
            
            string deviceName: 
            Input name of the device for which plotter configuration is requested.
        """
        pass
    
    
    ColorDependentPlotStyles = None
    
    
    CurrentConfig = None
    
    
    Devices = None
    
    
    NamedPlotStyles = None
    
    pass

class PlotEngine(None (initial) -> plot -> document -> page -> graphics):
    """
    
    """
    def BeginDocument(self):
        """
        BeginDocument -> void
            
            PlotInfo plotInfo: 
            Input template for the document.
            
            string documentName: 
            Input document name.
            
            object parameters: 
            Input Reserved for future use.
            
            int modopt(IsLong) copies: 
            Input number of copies desired; 1 if plotting to a file.
            
            [MarshalAs(UnmanagedType.U1)] bool plotToFile: 
            Input indicating whether to plot to a file or a device.
            
            string fileName: 
            Input full path and file name, if plotting to a file.
        """
        pass
    
    
    def BeginGenerateGraphics(self):
        """
        BeginGenerateGraphics -> void
            
            object parameters: 
            Reserved for future use.
        """
        pass
    
    
    def BeginPage(self):
        """
        BeginPage -> void
            
            PlotPageInfo pageInfo: 
            Input page information, modified in this call to reflect the pre-scan of the page.
            
            PlotInfo plotInfo: 
            Input reference to the validated PlotInfo for this page.
            
            [MarshalAs(UnmanagedType.U1)] bool lastPage: 
            Input indicating whether this is the last page in the document.
            
            object parameters: 
            Reserved for future use.
        """
        pass
    
    
    def BeginPlot(self):
        """
        BeginPlot -> void
            
            PlotProgress plotProgress: 
            Input plot progress
            
            object parameters: 
            Reserved for future use.
        """
        pass
    
    
    def Destroy(self):
        """
        Destroy -> void
        
        """
        pass
    
    
    def EndDocument(self):
        """
        EndDocument -> void
            
            object parameters: 
            Reserved for future use.
        """
        pass
    
    
    def EndGenerateGraphics(self):
        """
        EndGenerateGraphics -> void
            
            object parameters: 
            Reserved for future use.
        """
        pass
    
    
    def EndPage(self):
        """
        EndPage -> void
            
            object parameters: 
            Reserved for future use.
        """
        pass
    
    
    def EndPlot(self):
        """
        EndPlot -> void
            
            object parameters: 
            Input caller-allocated PREVIEWENDPLOT structure.
        """
        pass
    
    
    IsBackgroundPackaging = None
    
    pass

class PlotFactory(public sealed class PlotFactory):
    """
    
    """
    def CreatePreviewEngine(self):
        """
        CreatePreviewEngine -> PlotEngine
            
            int modopt(IsLong) previewFlags: 
            Input flags that define the behavior of the preview state when AutoCAD previews the layout.
        """
        pass
    
    
    def CreatePublishEngine(self):
        """
        CreatePublishEngine -> PlotEngine
        
        """
        pass
    
    
    ProcessPlotState = None
    
    pass

class PlotInfo(RXObject):
    """
    
    P
    
    l
    
    o
    
    t
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
    def IsCompatibleDocument(self):
        """
        IsCompatibleDocument -> bool
            
            PlotInfo info: 
            Input object to be compared to this object for document compatibility.
        """
        pass
    
    
    DeviceOverride = None
    
    
    IsValidated = None
    
    
    Layout = None
    
    
    OverrideSettings = None
    
    
    ValidatedConfig = None
    
    
    ValidatedSettings = None
    
    pass

class PlotInfoValidator(RXObject):
    """
    
    P
    
    l
    
    o
    
    t
    
    I
    
    n
    
    f
    
    o
    
    V
    
    a
    
    l
    
    i
    
    d
    
    a
    
    t
    
    o
    
    r
    
    (
    
    )
    """
    def Validate(self):
        """
        Validate -> void
            
            PlotInfo info: 
            Input object to validate.
        """
        pass
    
    
    DimensionalWeight = None
    
    
    MediaBoundsWeight = None
    
    
    MediaGroupWeight = None
    
    
    MediaMatchingPolicy = None
    
    
    MediaMatchingThreshold = None
    
    
    PrintableBoundsWeight = None
    
    
    SheetDimensionalWeight = None
    
    
    SheetMediaGroupWeight = None
    
    pass

class PlotLogger(DisposableWrapper):
    """
    
    """
    def EndJob(self):
        """
        EndJob -> void
        
        """
        pass
    
    
    def EndSheet(self):
        """
        EndSheet -> void
        
        """
        pass
    
    
    def LogAbortRetryIgnoreError(self):
        """
        LogAbortRetryIgnoreError -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def LogError(self):
        """
        LogError -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def LogInformation(self):
        """
        LogInformation -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def LogMessage(self):
        """
        LogMessage -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def LogSevereError(self):
        """
        LogSevereError -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def LogTerminalError(self):
        """
        LogTerminalError -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def LogWarning(self):
        """
        LogWarning -> void
            
            string message: 
            Input formatted error string to be recorded in the log.
        """
        pass
    
    
    def StartJob(self):
        """
        StartJob -> void
        
        """
        pass
    
    
    def StartSheet(self):
        """
        StartSheet -> void
        
        """
        pass
    
    
    ErrorHasHappenedInJob = None
    
    
    ErrorHasHappenedInSheet = None
    
    
    WarningHasHappenedInJob = None
    
    
    WarningHasHappenedInSheet = None
    
    pass

class PlotMessageIndex():
    DialogTitle
    SheetName
    SheetNameToolTip
    Status
    SheetProgressCaption
    SheetSetProgressCaption
    MessageCanceling
    MessageCancelingCurrent
    CancelSheetButtonMessage
    CancelJobButtonMessage
    MessageCount

class PlotPageInfo(RXObject):
    """
    
    P
    
    l
    
    o
    
    t
    
    P
    
    a
    
    g
    
    e
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """

    pass

class PlotProgress(DisposableWrapper):
    """
    
    """
    def Heartbeat(self):
        """
        Heartbeat -> void
        
        """
        pass
    
    
    IsPlotCancelled = None
    
    
    IsSheetCancelled = None
    
    
    IsVisible = None
    
    
    LowerPlotProgressRange = None
    
    
    LowerSheetProgressRange = None
    
    
    PlotCancelStatus = None
    
    
    PlotProgressPos = None
    
    
    SheetCancelStatus = None
    
    
    SheetProgressPos = None
    
    
    StatusMsgString = None
    
    
    UpperPlotProgressRange = None
    
    
    UpperSheetProgressRange = None
    
    pass

class PlotProgressDialog(PlotProgress):
    """
    
    P
    
    l
    
    o
    
    t
    
    P
    
    r
    
    o
    
    g
    
    r
    
    e
    
    s
    
    s
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    e
    
    v
    
    i
    
    e
    
    w
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    r
    
    u
    
    e
    
     
    
    i
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
     
    
    i
    
    s
    
     
    
    a
    
     
    
    p
    
    r
    
    e
    
    v
    
    i
    
    e
    
    w
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    s
    
    h
    
    e
    
    e
    
    t
    
    C
    
    o
    
    u
    
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
    
    h
    
    e
    
    e
    
    t
    
     
    
    c
    
    o
    
    u
    
    n
    
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
    
     
    
    s
    
    h
    
    o
    
    w
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    S
    
    h
    
    e
    
    e
    
    t
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    r
    
    u
    
    e
    
     
    
    t
    
    o
    
     
    
    s
    
    h
    
    o
    
    w
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    a
    
    n
    
    c
    
    e
    
    l
    
     
    
    s
    
    h
    
    e
    
    e
    
    t
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    """
    def Destroy(self):
        """
        Destroy -> void
        
        """
        pass
    
    
    def OnBeginPlot(self):
        """
        OnBeginPlot -> void
        
        """
        pass
    
    
    def OnBeginSheet(self):
        """
        OnBeginSheet -> void
        
        """
        pass
    
    
    def OnEndPlot(self):
        """
        OnEndPlot -> void
        
        """
        pass
    
    
    def OnEndSheet(self):
        """
        OnEndSheet -> void
        
        """
        pass
    
    
    IsSingleSheetPlot = None
    
    pass

class PlotReactorManager(public sealed class PlotReactorManager):
    """
    
    """

    pass

class PlotToFileCapability():
    NoPlotToFile
    PlotToFileAllowed
    MustPlotToFile

class PreviewEndPlotInfo(DisposableWrapper):
    """
    
    P
    
    r
    
    e
    
    v
    
    i
    
    e
    
    w
    
    E
    
    n
    
    d
    
    P
    
    l
    
    o
    
    t
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
    Status = None
    
    pass

class PreviewEndPlotStatus():
    Normal
    Plot
    Cancel
    Next
    Previous

class PreviewEngineFlags():
    NextSheet = 2
    Plot = 1
    PreviousSheet = 4

class ProcessPlotState():
    NotPlotting
    ForegroundPlotting
    BackgroundPlotting

class RefreshCode():
    All
    RefreshDevicesList
    RefreshStyleList
    RefreshSystemDevicesList
    RefreshPC3DevicesList

class SheetCancelStatus():
    Continue
    CanceledByCancelButton
    CanceledByCancelAllButton
    CanceledByCaller

class SheetType():
    SingleDwf
    MultiDwf
    OriginalDevice
    SingleDwfx
    MultiDwfx
    SinglePdf
    MultiPdf

class StdConfiguration():
    NoneDevice
    DefaultWindowsSysPrinter
    Dwf6ePlot
    DwfEplotOptForPlotting
    DwfEplotOptForViewing
    PublishToWebDwf
    PublishToWebJpg
    PublishToWebPng
    DWFxePlot
    PublishToWebDWFx