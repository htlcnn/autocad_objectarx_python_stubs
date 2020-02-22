class AutomationDataGridView(object):
    """
    
    """
    WM_GETOBJECT Field = None
    
    
    def WndProc(self):
        """
        WndProc -> void
        
        """
        pass
    
    pass

class ColorComboBox(object):
    """
    
    """
    CurrentColor = None
    
    
    Highlight = None
    
    
    IndexColors = None
    
    
    MaxRecentColorCount = None
    
    
    MoreColorsCommand Field = None
    
    
    PreviewSafeColor = None
    
    
    RecentColors = None
    
    
    SelectionBoxItemTemplate = None
    
    
    SpecialColors = None
    
    
    SupportsByBlock = None
    
    
    SupportsByEntity = None
    
    
    SupportsByLayer = None
    
    
    SupportsMoreColors = None
    
    
    SupportsNone = None
    
    
    SupportsUseCurrent = None
    
    
    TrueColors = None
    
    
    def OnApplyTemplate(self):
        """
        OnApplyTemplate -> void
        
        """
        pass
    
    
    CurrentAcadColor = None
    
    
    CurrentColor = None
    
    
    Highlight = None
    
    
    IndexColors = None
    
    
    MaxRecentColorCount = None
    
    
    PreviewSafeAcadColor = None
    
    
    RecentColors = None
    
    
    SelectionBoxItemTemplate = None
    
    
    SpecialColors = None
    
    
    SupportsByBlock = None
    
    
    SupportsByEntity = None
    
    
    SupportsByLayer = None
    
    
    SupportsMoreColors = None
    
    
    SupportsNone = None
    
    
    SupportsUseCurrent = None
    
    
    TrueColors = None
    
    pass

class ColorDialog(object):
    """
    
    """
    class ColorTabs():
        ACITab = 1
        ColorBookTab = 4
        TrueColorTab = 2
    
    
    def SetDialogTabs(self):
        """
        SetDialogTabs -> void
            
            ColorTabs value: 
            Input new value
        """
        pass
    
    
    def ShowDialog(self):
        """
        ShowDialog -> DialogResult
        
        """
        pass
    
    
    Color = None
    
    
    IncludeByBlockByLayer = None
    
    pass

class ColorItem(object):
    """
    
    ColorItem()
    """
    ByBlock Field = None
    
    
    ByLayer Field = None
    
    
    IsByBlock Field = None
    
    
    IsByLayer Field = None
    
    
    IsNone Field = None
    
    
    IsUseCurrent Field = None
    
    
    None Field = None
    
    
    UseCurrent Field = None
    
    
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
    
    
    def GetIndexColorItem(self):
        """
        GetIndexColorItem -> ColorItem
        
        """
        pass
    
    
    def GetTrueColorItem(self):
        """
        GetTrueColorItem -> ColorItem
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString -> string
        
        """
        pass
    
    
    AcadColor = None
    
    
    ByLayerColor = None
    
    
    Color = None
    
    
    LocalName = None
    
    
    Name = None
    
    pass

class ColorItemCollection(object):
    """
    
    """

    pass

class ColorItemConverter(object):
    """
    
    """
    def CanConvertFrom(self):
        """
        CanConvertFrom -> bool
        
        """
        pass
    
    
    def CanConvertTo(self):
        """
        CanConvertTo -> bool
        
        """
        pass
    
    
    def ConvertFrom(self):
        """
        ConvertFrom -> object
        
        """
        pass
    
    
    def ConvertTo(self):
        """
        ConvertTo -> object
        
        """
        pass
    
    pass

class ColorListBox(object):
    """
    
    """
    def GetContainerForItemOverride(self):
        """
        GetContainerForItemOverride -> DependencyObject
        
        """
        pass
    
    pass

class ColorListBoxItem(object):
    """
    
    """
    def OnPreviewMouseLeftButtonDown(self):
        """
        OnPreviewMouseLeftButtonDown -> void
        
        """
        pass
    
    pass

class ContextMenuExtension(object):
    """
    
    """
    Title = None
    
    pass

class DefaultPane():
    ModeMacro = None
    CursorCoordinates = None
    Snap = None
    Grid = None
    Ortho = None
    Polar = None
    ObjectTrack = None
    LineWeight = None
    PaperModel = None
    Paper = None
    Model = None
    ObjectSnap = None
    Float = None
    Table = None
    Spacer = None
    ViewportMaximizePrevious = None
    ViewportMaximize = None
    ViewportMaximizeNext = None
    DynamicInput = None
    DynamicUcs = None
    LayoutModelIcons = None
    ModelIcon = None
    LayoutIcon = None
    LayoutMoreIcon = None
    All = None

class Direction():
    Bottom = 4
    BottomLeft = 6
    BottomRight = 12
    Left = 2
    None = 0
    Right = 8
    Top = 1
    TopLeft = 3
    TopRight = 9

class DocWindowReactor(object):
    """
    
    """

    pass

class DockSides():
    Bottom = 0x8000
    Left = 0x1000
    None = 0
    Right = 0x4000
    Top = 0x2000

class DocumentWindow(object):
    """
    
    DocumentWindow()
    """
    def Activate(self):
        """
        Activate -> void
        
        """
        pass
    
    
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose -> void
        
        """
        pass
    
    
    def GetWndPtr(self):
        """
        GetWndPtr -> IntPtr
        
        """
        pass
    
    
    CanUpdate = None
    
    
    Document = None
    
    
    Title = None
    
    pass

class DrawingDocumentWindow(object):
    """
    
    """
    Document = None
    
    pass

class DropTarget(object):
    """
    
    DropTarget()
    """
    def OnDragEnter(self):
        """
        OnDragEnter -> void
            
            DragEventArgs e: 
            Input dragging event
        """
        pass
    
    
    def OnDragLeave(self):
        """
        OnDragLeave -> void
        
        """
        pass
    
    
    def OnDragOver(self):
        """
        OnDragOver -> void
            
            DragEventArgs e: 
            Input dragging event
        """
        pass
    
    
    def OnDrop(self):
        """
        OnDrop -> void
            
            DragEventArgs e: 
            Input System.Windows.Forms.DragEventArgs object.
        """
        pass
    
    pass

class IconType():
    None = None
    Information = None
    Critical = None
    Warning = None

class InfoCenter(object):
    """
    
    """
    def InvokeToolbarMoveEvent(self):
        """
        InvokeToolbarMoveEvent -> void
        
        """
        pass
    
    
    def InvokeToolbarResizeEvent(self):
        """
        InvokeToolbarResizeEvent -> void
            
            int width: 
            Input width
        """
        pass
    
    
    def LaunchSubAwareModule(self):
        """
        LaunchSubAwareModule -> void
            
            short resReqid: 
            Input.
            
            string strCourseId: 
            Input.
            
            string strModuleId: 
            Input.
        """
        pass
    
    
    KeepFocus = None
    
    
    SubAwareClientInfo = None
    
    
    UPIXMLData = None
    
    
    Visible = None
    
    pass

class LineWeightDialog(object):
    """
    
    """
    def ShowDialog(self):
        """
        ShowDialog -> DialogResult
        
        """
        pass
    
    
    IncludeByBlockByLayer = None
    
    
    LineWeight = None
    
    pass

class LinetypeDialog(object):
    """
    
    """
    def ShowDialog(self):
        """
        ShowDialog -> DialogResult
        
        """
        pass
    
    
    IncludeByBlockByLayer = None
    
    
    Linetype = None
    
    pass

class LocationChangingEventArgs(object):
    """
    
    """
    Location = None
    
    
    NewLocation = None
    
    pass

class Menu(object):
    """
    
    Menu()
    """
    MenuItems = None
    
    pass

class MenuItem(object):
    """
    
    MenuItem(string)
        string value : Input new item
    
    
    MenuItem(string, System.Drawing.Icon)
        string value : Input new item name
        System.Drawing.Icon icon : Input new icon
    
    
    """
    Checked = None
    
    
    Enabled = None
    
    
    Icon = None
    
    
    Text = None
    
    
    Visible = None
    
    pass

class MenuItemCollection(object):
    """
    
    MenuItemCollection
        Menu owner : Input the parent for this object
    """
    def Add(self):
        """
        Add -> Integer
            
            MenuItem value: 
            Input the MenuItem to be added to the end of this collection; the value can be a null reference.
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
            
            MenuItem value: 
            Input the MenuItem to locate in this collection; the value can be a null reference.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MenuItem[] array: 
            Input one-dimensional array that is the destination of the elements copied from this collection; the array must have zero-based indexing.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator<IMenuItem>
        
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            MenuItem value: 
            Input the MenuItem to locate in the collection; the value can be a null reference.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index at which value should be inserted.
            
            MenuItem value: 
            Input the MenuItem to insert. The value can be a null reference.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            MenuItem value: 
            Input the MenuItem to remove from the collection; the value can be a null reference.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index of item to remove.
        """
        pass
    
    
    Count = None
    
    
    IsFixedSize = None
    
    
    IsReadOnly = None
    
    pass

class OpenFileDialog(object):
    """
    
    OpenFileDialog
        string title : Input title of dialog box
        string defaultName : Input name of box
        string extension : Input extension of box
        string dialogName : Input dialog box
        OpenFileDialogFlags flags : Input configuration flags
    """
    class OpenFileDialogFlags():
        AllowAnyExtension = 4
        AllowFoldersOnly = 0x800
        AllowMultiple = 0x1000
        DefaultIsFolder = 0x10
        DoNotTransferRemoteFiles = 0x40
        ForceDefaultFolder = 0x100
        NoFtpSites = 0x200
        NoShellExtensions = 0x400
        NoUrls = 0x80
        SearchPath = 8
    
    
    def GetFilenames(self):
        """
        GetFilenames -> string()
        
        """
        pass
    
    
    def ShowDialog(self):
        """
        ShowDialog -> DialogResult
        
        """
        pass
    
    
    Filename = None
    
    pass

class Palette(object):
    """
    
    """
    Name = None
    
    
    PaletteSet = None
    
    pass

class PaletteActivatedEventArgs(object):
    """
    
    PaletteActivatedEventArgs
        Palette activated : Input palette to display when activated
        Palette deactivated : Input palette to display when deactivated
    """
    Activated = None
    
    
    Deactivated = None
    
    pass

class PaletteAddContextMenuEventArgs(object):
    """
    
    PaletteAddContextMenuEventArgs
        List<MenuItem> menuitems : Input menu items to add
        List<int> removeMenuItems : Input menu items to remove
        int nHitFlag : Input location within the palette set of the event that triggered the context menu
        int nRightClkTab : Input palette tab of the tab for which this context menu is being displayed
    """
    HitFlag = None
    
    
    MenuItems = None
    
    
    RemoveMenuItems = None
    
    
    RightClickTab = None
    
    pass

class PaletteEnterSizeMoveEventArgs(object):
    """
    
    PaletteEnterSizeMoveEventArgs()
    """
    EnterSizeMove = None
    
    pass

class PalettePersistEventArgs(object):
    """
    
    PalettePersistEventArgs
        IConfigurationSection configurationSection : Input configuration section
    """
    ConfigurationSection = None
    
    pass

class PaletteSet(object):
    """
    
    PaletteSet(string)
        string name : Input name of palette set
    
    
    PaletteSet(string, Guid)
        string name : Input name of palette set
        Guid toolID : Input ID of tool GUID
    
    
    """
    def Activate(self):
        """
        Activate -> void
            
            int index: 
            Input index to activate
        """
        pass
    
    
    def Add(self):
        """
        Add(string, Control) -> Palette
            
            string name: 
            Input palette name
            
            Control control: 
            Input palette control
        Add(string, Uri) -> Palette
        
        """
        pass
    
    
    def AddVisual(self):
        """
        AddVisual(string, Visual) -> Palette
            
            string name: 
            Input palette name
            
            Visual control: 
            Input visual control
        AddVisual(string, Visual, [MarshalAs(UnmanagedType.U1)] bool) -> Palette
        
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Palette[] array: 
            Input target array
            
            int index: 
            Input first index to copy elements to
        """
        pass
    
    
    def EnableTransparency(self):
        """
        EnableTransparency -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input true to enable transparency
        """
        pass
    
    
    def FloatControl(self):
        """
        FloatControl(Rect) -> void
            
            Rect value: 
            Rectangle specifying the position and size of the floating PaletteSet
        FloatControl(System.Windows.Point) -> void
            
            System.Windows.Point pointOnScreen: 
            Top left positon on the screen where PaletteSet will be positioned.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def GetThemedIcon(self):
        """
        GetThemedIcon -> System.Drawing.Icon
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Input index of item to remove
        """
        pass
    
    
    def SetThemedIcon(self):
        """
        SetThemedIcon -> void
            
            System.Drawing.Icon value: 
            icon to be set
            
            ColorThemeEnum theme: 
            theme to be applied to
        """
        pass
    
    
    Anchored = None
    
    
    AutoRollUp = None
    
    
    Count = None
    
    
    DarkThemedIcon = None
    
    
    DeviceIndependentLocation = None
    
    
    DeviceIndependentMinimumSize = None
    
    
    DeviceIndependentSize = None
    
    
    Dock = None
    
    
    DockEnabled = None
    
    
    Icon = None
    
    
    KeepFocus = None
    
    
    LargeDarkThemedIcon = None
    
    
    LargeLightThemedIcon = None
    
    
    LightThemedIcon = None
    
    
    Location = None
    
    
    MinimumSize = None
    
    
    Name = None
    
    
    Opacity = None
    
    
    RolledUp = None
    
    
    Size = None
    
    
    Style = None
    
    
    TitleBarLocation = None
    
    
    Visible = None
    
    pass

class PaletteSetDockSite(object):
    """
    
    """
    def CanDock(self):
        """
        CanDock -> Rect?
        
        """
        pass
    
    
    def Dock(self):
        """
        Dock -> bool
        
        """
        pass
    
    
    def Initialize(self):
        """
        Initialize -> void
        
        """
        pass
    
    
    def Uninitialize(self):
        """
        Uninitialize -> void
        
        """
        pass
    
    pass

class PaletteSetFocusedEventArgs(object):
    """
    
    """

    pass

class PaletteSetSizeEventArgs(object):
    """
    
    PaletteSetSizeEventArgs
        int cx : Input pixel width
        int cy : Input pixel height
        double dx : Input device-independent width
        double dy : Input device-independent height
    """
    DeviceIndependentHeight = None
    
    
    DeviceIndependentWidth = None
    
    
    Height = None
    
    
    Width = None
    
    pass

class PaletteSetStateEventArgs(object):
    """
    
    PaletteSetStateEventArgs
        StateEventIndex state : Input event index state
    """
    NewState = None
    
    pass

class PaletteSetStyles():
    NameEditable = 0x10
    Notify = 0x400
    NoTitleBar = 0x8000
    PauseAutoRollupForChildModalDialog = 0x10000
    ShowAutoHideButton = 2
    ShowCloseButton = 8
    ShowPropertiesMenu = 4
    ShowTabForSingle = 0x40
    SingleColDock = 0x1000
    SingleRowDock = 0x200
    SingleRowNoVertResize = 0x800
    Snappable = 0x20
    UsePaletteNameAsTitleForSingle = 0x80

class PaletteSetTitleBarLocation():
    Left = None
    Right = None

class Pane(object):
    """
    
    Pane()()
    
    
    """
    MaximumWidth = None
    
    
    MinimumWidth = None
    
    
    Style = None
    
    
    Text = None
    
    pass

class PaneCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            Pane value: 
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
            
            Pane value: 
            Input object to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Pane[] array: 
            Input one-dimensional array that is the destination
            
            int index: 
            Input zero-based index in array at which copying begins.
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
            
            Pane value: 
            Input object to retrieve index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            Pane value: 
            Input to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            Pane value: 
            Input pane to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index of item to remove
        """
        pass
    
    
    Count = None
    
    
    IsFixedSize = None
    
    
    IsReadOnly = None
    
    pass

class PaneStyles():
    Command = 0x10
    NoBorders = 1
    Normal = 8
    PopOut = 2
    PopUp = 0x20
    Stretch = 4

class PlotStyleDialog(object):
    """
    
    """
    def ShowDialog(self):
        """
        ShowDialog -> DialogResult
        
        """
        pass
    
    
    IncludeByBlockByLayer = None
    
    
    PlotStyle = None
    
    pass

class SaveFileDialog(object):
    """
    
    SaveFileDialog
        string title : Input title of dialog box
        string defaultName : Input name
        string extension : Input extension of dialog
        string dialogName : Input dialog name
        SaveFileDialogFlags flags : Input configuration flags
    """
    class SaveFileDialogFlags():
        AllowAnyExtension = 4
        DefaultIsFolder = 0x10
        DoNotTransferRemoteFiles = 0x40
        DoNotWarnIfFileExist = 0x20
        ForceDefaultFolder = 0x100
        NoFtpSites = 0x200
        NoShellExtensions = 0x400
        NoUrls = 0x80
    
    
    def ShowDialog(self):
        """
        ShowDialog -> DialogResult
        
        """
        pass
    
    
    Filename = None
    
    pass

class SizeChangingEventArgs(object):
    """
    
    SizeChangingEventArgs()
    """
    NewSize = None
    
    
    Size = None
    
    pass

class StateEventIndex():
    Hide = 0
    Show = 1
    ThemeChange = 4

class StatusBar(object):
    """
    
    """
    def CloseBubbleWindows(self):
        """
        CloseBubbleWindows -> void
        
        """
        pass
    
    
    def GetDefaultPane(self):
        """
        GetDefaultPane -> Pane
            
            DefaultPane pane: 
            Input one of the valid values from DefaultPane enumeration.
        """
        pass
    
    
    def RemoveDefaultPane(self):
        """
        RemoveDefaultPane -> void
            
            DefaultPane pane: 
            Input Autodesk.AutoCAD.Windows.DefaultPane object. Input bitwise union of one or more of the valid DefaultPane enums.
        """
        pass
    
    
    def Update(self):
        """
        Update -> void
        
        """
        pass
    
    
    Panes = None
    
    
    TrayItems = None
    
    
    Window = None
    
    pass

class StatusBarItem(object):
    """
    
    StatusBarItem()()
    
    
    """
    def DisplayContextMenu(self):
        """
        DisplayContextMenu -> void
            
            ContextMenu menu: 
            Input context menu to display
            
            Point p: 
            Input point at which to display the menu
        """
        pass
    
    
    def PointToClient(self):
        """
        PointToClient -> Point
            
            Point p: 
            Input or POINT structure that contains the screen coordinates to be converted.
        """
        pass
    
    
    def PointToScreen(self):
        """
        PointToScreen -> Point
            
            Point p: 
            Input or POINT structure that contains the client coordinates to be converted.
        """
        pass
    
    
    Enabled = None
    
    
    Icon = None
    
    
    ToolTipText = None
    
    
    Visible = None
    
    pass

class StatusBarMouseDownEventArgs(object):
    """
    
    """
    Button = None
    
    
    DoubleClick = None
    
    
    X = None
    
    
    Y = None
    
    pass

class ToggleAblePopup(object):
    """
    
    """
    KeyboardFocusableElement = None
    
    
    def OnOpened(self):
        """
        OnOpened -> void
        
        """
        pass
    
    
    def OnPreviewKeyDown(self):
        """
        OnPreviewKeyDown -> void
        
        """
        pass
    
    
    def OnPreviewMouseLeftButtonDown(self):
        """
        OnPreviewMouseLeftButtonDown -> void
        
        """
        pass
    
    
    def OnPreviewMouseRightButtonDown(self):
        """
        OnPreviewMouseRightButtonDown -> void
        
        """
        pass
    
    
    def OnPreviewMouseRightButtonUp(self):
        """
        OnPreviewMouseRightButtonUp -> void
        
        """
        pass
    
    
    KeyboardFocusableElement = None
    
    pass

class TrayItem(object):
    """
    
    TrayItem()()
    
    
    """
    def CloseBubbleWindows(self):
        """
        CloseBubbleWindows -> void
        
        """
        pass
    
    
    def ShowBubbleWindow(self):
        """
        ShowBubbleWindow -> void
            
            TrayItemBubbleWindow bubble: 
            Input bubble to show
        """
        pass
    
    pass

class TrayItemBubbleWindow(object):
    """
    
    """
    HyperLink = None
    
    
    HyperText = None
    
    
    IconType = None
    
    
    Text = None
    
    
    Text2 = None
    
    
    Title = None
    
    pass

class TrayItemBubbleWindowCloseReason():
    FailedToCreate = None
    NoIcons = None
    NoNotifications = None
    ClosedByUser = None
    TimedOut = None
    HyperlinkClicked = None
    DocumentDeactivated = None

class TrayItemBubbleWindowClosedEventArgs(object):
    """
    
    """
    CloseReason = None
    
    pass

class TrayItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            TrayItem value: 
            Input value to add
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
            
            TrayItem value: 
            Input value to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TrayItem[] array: 
            Input Autodesk.AutoCAD.Windows.TrayItem object. One-dimensional array that is the destination of the elements copied from TrayItemCollection; the array must have zero-based indexing.
            
            int index: 
            Input. The zero-based index in array at which copying begins.
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
            
            TrayItem value: 
            Input value to retrieve the index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            TrayItem value: 
            Input value to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            TrayItem value: 
            Input value to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index to remove at
        """
        pass
    
    
    Count = None
    
    
    IsFixedSize = None
    
    
    IsReadOnly = None
    
    pass

class Visuals(object):
    """
    
    """
    ApplicationIcon = None
    
    
    PickBitmap = None
    
    
    PickSetBitmap = None
    
    pass

class WPFDocumentWindow(object):
    """
    
    WPFDocumentWindow
        Visual wpfVisual : WPF visual to be used to create WPF document window as a sub-window of AutoCAD
    """
    def SetDocument(self):
        """
        SetDocument -> void
            
            object document: 
            Document object assosicated with the document window
        """
        pass
    
    pass

class Window(object):
    """
    
    Window()
    """
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def Focus(self):
        """
        Focus -> bool
        
        """
        pass
    
    
    def FromHandle(self):
        """
        FromHandle -> Autodesk.AutoCAD.Windows.Window
        
        """
        pass
    
    
    def GetWndPtr(self):
        """
        GetWndPtr -> IntPtr
        
        """
        pass
    
    
    DeviceIndependentLocation = None
    
    
    DeviceIndependentSize = None
    
    
    Handle = None
    
    
    Text = None
    
    
    UnmanagedWindow = None
    
    
    Visible = None
    
    
    WindowState = None
    
    pass

class WindowExtension(object):
    """
    
    """
    def GetIcon(self):
        """
        GetIcon -> Icon
        
        """
        pass
    
    
    def GetLocation(self):
        """
        GetLocation -> Point
        
        """
        pass
    
    
    def GetSize(self):
        """
        GetSize -> Size
        
        """
        pass
    
    
    def SetIcon(self):
        """
        SetIcon -> void
        
        """
        pass
    
    
    def SetLocation(self):
        """
        SetLocation -> void
        
        """
        pass
    
    
    def SetSize(self):
        """
        SetSize -> void
        
        """
        pass
    
    pass

class WindowPositionChangedEventArgs(object):
    """
    
    WindowPositionChangedEventArgs()
    """
    Moved = None
    
    
    Sized = None
    
    pass