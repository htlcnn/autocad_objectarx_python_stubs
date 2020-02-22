class AppPlotStatus():
    DwfFilePlotted = -3
    NoPlotYet = -1
    PlotHadErrors = 3
    PlotHadSystemError = 4
    PlotStart = 0
    PlotSuccessful = 2
    PlottingMessage = -2
    ViewPlotLog = 1

class BeginDocumentEventArgs(object):
    """
    
    BeginDocumentEventArgs()()
    
    
    """
    DocumentName = None
    
    
    FileName = None
    
    
    PlotInfo = None
    
    
    PlotToFile = None
    
    pass

class BeginPageEventArgs(object):
    """
    
    BeginPageEventArgs()()
    
    
    """
    LastPage = None
    
    
    PlotInfo = None
    
    
    PlotPageInfo = None
    
    pass

class BeginPlotEventArgs(object):
    """
    
    BeginPlotEventArgs()
        Autodesk.AutoCAD.PlottingServices.PlotProgress progress : Input plot progress
        Autodesk.AutoCAD.PlottingServices.PlotType plotType : Input plot type
    
    
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

class DsdData(object):
    """
    
    DsdData()
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

class DsdEntry(object):
    """
    
    DsdEntry()
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

class DsdEntryCollection(object):
    """
    
    DsdEntryCollection()
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

class Dwf3dOptions(object):
    """
    
    """
    GroupByXrefHierarchy = None
    
    
    PublishWithMaterials = None
    
    pass

class EndDocumentEventArgs(object):
    """
    
    EndDocumentEventArgs
        PlotCancelStatus status : Input status of document
    """
    Status = None
    
    pass

class EndPageEventArgs(object):
    """
    
    EndPageEventArgs
        SheetCancelStatus status : Input status of document
    """
    Status = None
    
    pass

class EndPlotEventArgs(object):
    """
    
    EndPlotEventArgs
        PlotCancelStatus status : Input status of document
    """
    Status = None
    
    pass

class HostAppServices(object):
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

class MediaBounds(object):
    """
    
    MediaBounds
        Point2d pageSize : Input size of page
        Point2d lowerLeftPrintableArea : Input lower left printable area
        Point2d upperRightPrintableArea : Input upper right printable area
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
    Continue = None
    CanceledByCaller = None
    CanceledByCancelAllButton = None

class PlotConfig(object):
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

class PlotConfigInfo(object):
    """
    
    PlotConfigInfo()
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

class PlotConfigInfoCollection(object):
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

class PlotConfigManager(object):
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

class PlotEngine(object):
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

class PlotFactory(object):
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

class PlotInfo(object):
    """
    
    PlotInfo()
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

class PlotInfoValidator(object):
    """
    
    PlotInfoValidator()
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

class PlotLogger(object):
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
    DialogTitle = None
    SheetName = None
    SheetNameToolTip = None
    Status = None
    SheetProgressCaption = None
    SheetSetProgressCaption = None
    MessageCanceling = None
    MessageCancelingCurrent = None
    CancelSheetButtonMessage = None
    CancelJobButtonMessage = None
    MessageCount = None

class PlotPageInfo(object):
    """
    
    PlotPageInfo()
    """

    pass

class PlotProgress(object):
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

class PlotProgressDialog(object):
    """
    
    PlotProgressDialog
        [MarshalAs(UnmanagedType.U1)] bool isPreview : Input true if the dialog is a preview
        int sheetCount : Input the sheet count
        [MarshalAs(UnmanagedType.U1)] bool showCancelSheetButton : Input true to show the cancel sheet button
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

class PlotReactorManager(object):
    """
    
    """

    pass

class PlotToFileCapability():
    NoPlotToFile = None
    PlotToFileAllowed = None
    MustPlotToFile = None

class PreviewEndPlotInfo(object):
    """
    
    PreviewEndPlotInfo()
    """
    Status = None
    
    pass

class PreviewEndPlotStatus():
    Normal = None
    Plot = None
    Cancel = None
    Next = None
    Previous = None

class PreviewEngineFlags():
    NextSheet = 2
    Plot = 1
    PreviousSheet = 4

class ProcessPlotState():
    NotPlotting = None
    ForegroundPlotting = None
    BackgroundPlotting = None

class RefreshCode():
    All = None
    RefreshDevicesList = None
    RefreshStyleList = None
    RefreshSystemDevicesList = None
    RefreshPC3DevicesList = None

class SheetCancelStatus():
    Continue = None
    CanceledByCancelButton = None
    CanceledByCancelAllButton = None
    CanceledByCaller = None

class SheetType():
    SingleDwf = None
    MultiDwf = None
    OriginalDevice = None
    SingleDwfx = None
    MultiDwfx = None
    SinglePdf = None
    MultiPdf = None

class StdConfiguration():
    NoneDevice = None
    DefaultWindowsSysPrinter = None
    Dwf6ePlot = None
    DwfEplotOptForPlotting = None
    DwfEplotOptForViewing = None
    PublishToWebDwf = None
    PublishToWebJpg = None
    PublishToWebPng = None
    DWFxePlot = None
    PublishToWebDWFx = None