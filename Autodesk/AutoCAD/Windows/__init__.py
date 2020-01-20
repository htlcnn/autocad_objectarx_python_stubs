class AutomationDataGridView(DataGridView, IRawElementProviderFragmentRoot, IRawElementProviderFragment, System.Windows.Automation.Provider.IRawElementProviderSimple, ISelectionProvider, IScrollProvider, System.Windows.Automation.Provider.ITableProvider, System.Windows.Automation.Provider.IGridProvider):
    """
    
    """
    WM_GETOBJECT Field = None
    
    
    def WndProc(self):
        """
        WndProc -> void
        
        """
        pass
    
    pass

class ColorComboBox(Control):
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

class ColorDialog(public sealed class ColorDialog):
    """
    
    """
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

class ColorItem(public sealed class ColorItem):
    """
    
    C
    
    o
    
    l
    
    o
    
    r
    
    I
    
    t
    
    e
    
    m
    
    (
    
    )
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

class ColorItemCollection(ObservableCollection<ColorItem>):
    """
    
    """

    pass

class ColorItemConverter(TypeConverter):
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

class ColorListBox(ListBox):
    """
    
    """
    def GetContainerForItemOverride(self):
        """
        GetContainerForItemOverride -> DependencyObject
        
        """
        pass
    
    pass

class ColorListBoxItem(ListBoxItem):
    """
    
    """
    def OnPreviewMouseLeftButtonDown(self):
        """
        OnPreviewMouseLeftButtonDown -> void
        
        """
        pass
    
    pass

class ContextMenuExtension(Menu, IDisposable):
    """
    
    """
    Title = None
    
    pass

  ModeMacro
  CursorCoordinates
  Snap
  Grid
  Ortho
  Polar
  ObjectTrack
  LineWeight
  PaperModel
  Paper
  Model
  ObjectSnap
  Float
  Table
  Spacer
  ViewportMaximizePrevious
  ViewportMaximize
  ViewportMaximizeNext
  DynamicInput
  DynamicUcs
  LayoutModelIcons
  ModelIcon
  LayoutIcon
  LayoutMoreIcon
  All

  Bottom = 4
  BottomLeft = 6
  BottomRight = 12
  Left = 2
  None = 0
  Right = 8
  Top = 1
  TopLeft = 3
  TopRight = 9

class DocWindowReactor(internal struct DocWindowReactor {
  private long <alignment member>;
}):
    """
    
    """

    pass

  Bottom = 0x8000
  Left = 0x1000
  None = 0
  Right = 0x4000
  Top = 0x2000

class DocumentWindow(Window):
    """
    
    D
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    (
    
    )
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

class DrawingDocumentWindow(DocumentWindow):
    """
    
    """
    Document = None
    
    pass

class DropTarget(public abstract class DropTarget):
    """
    
    D
    
    r
    
    o
    
    p
    
    T
    
    a
    
    r
    
    g
    
    e
    
    t
    
    (
    
    )
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

  None
  Information
  Critical
  Warning

class InfoCenter(public class InfoCenter):
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

class LineWeightDialog(public sealed class LineWeightDialog):
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

class LinetypeDialog(public sealed class LinetypeDialog):
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

class LocationChangingEventArgs(EventArgs):
    """
    
    """
    Location = None
    
    
    NewLocation = None
    
    pass

class Menu(public abstract class Menu):
    """
    
    M
    
    e
    
    n
    
    u
    
    (
    
    )
    """
    MenuItems = None
    
    pass

class MenuItem(Menu, IMenuItem):
    """
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
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
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
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
    
    I
    
    c
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
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
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    n
    
    a
    
    m
    
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
    
    I
    
    c
    
    o
    
    n
    
     
    
    i
    
    c
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    c
    
    o
    
    n
    """
    Checked = None
    
    
    Enabled = None
    
    
    Icon = None
    
    
    Text = None
    
    
    Visible = None
    
    pass

class MenuItemCollection(IList, IEnumerable<IMenuItem>):
    """
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
     
    
    o
    
    w
    
    n
    
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
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
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

class OpenFileDialog(public sealed class OpenFileDialog):
    """
    
    O
    
    p
    
    e
    
    n
    
    F
    
    i
    
    l
    
    e
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
     
    
    b
    
    o
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
    N
    
    a
    
    m
    
    e
    
     
    
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
    
     
    
    b
    
    o
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
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
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    b
    
    o
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
     
    
    b
    
    o
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    p
    
    e
    
    n
    
    F
    
    i
    
    l
    
    e
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
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
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    """
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

class Palette(public sealed class Palette):
    """
    
    """
    Name = None
    
    
    PaletteSet = None
    
    pass

class PaletteActivatedEventArgs(EventArgs):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    A
    
    c
    
    t
    
    i
    
    v
    
    a
    
    t
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    a
    
    c
    
    t
    
    i
    
    v
    
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
    
     
    
    p
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    t
    
    o
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    w
    
    h
    
    e
    
    n
    
     
    
    a
    
    c
    
    t
    
    i
    
    v
    
    a
    
    t
    
    e
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    d
    
    e
    
    a
    
    c
    
    t
    
    i
    
    v
    
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
    
     
    
    p
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    t
    
    o
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    w
    
    h
    
    e
    
    n
    
     
    
    d
    
    e
    
    a
    
    c
    
    t
    
    i
    
    v
    
    a
    
    t
    
    e
    
    d
    """
    Activated = None
    
    
    Deactivated = None
    
    pass

class PaletteAddContextMenuEventArgs(EventArgs):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    A
    
    d
    
    d
    
    C
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
    M
    
    e
    
    n
    
    u
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    L
    
    i
    
    s
    
    t
    
    <
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    >
    
     
    
    m
    
    e
    
    n
    
    u
    
    i
    
    t
    
    e
    
    m
    
    s
    
     
    
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
    
    s
    
     
    
    t
    
    o
    
     
    
    a
    
    d
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    L
    
    i
    
    s
    
    t
    
    <
    
    i
    
    n
    
    t
    
    >
    
     
    
    r
    
    e
    
    m
    
    o
    
    v
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    s
    
     
    
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
    
    s
    
     
    
    t
    
    o
    
     
    
    r
    
    e
    
    m
    
    o
    
    v
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    n
    
    H
    
    i
    
    t
    
    F
    
    l
    
    a
    
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
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    s
    
    e
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    v
    
    e
    
    n
    
    t
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    r
    
    i
    
    g
    
    g
    
    e
    
    r
    
    e
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    n
    
    R
    
    i
    
    g
    
    h
    
    t
    
    C
    
    l
    
    k
    
    T
    
    a
    
    b
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    t
    
    a
    
    b
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    a
    
    b
    
     
    
    f
    
    o
    
    r
    
     
    
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
    
    t
    
    e
    
    x
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    s
    
     
    
    b
    
    e
    
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
    
    e
    
    d
    """
    HitFlag = None
    
    
    MenuItems = None
    
    
    RemoveMenuItems = None
    
    
    RightClickTab = None
    
    pass

class PaletteEnterSizeMoveEventArgs(EventArgs):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    E
    
    n
    
    t
    
    e
    
    r
    
    S
    
    i
    
    z
    
    e
    
    M
    
    o
    
    v
    
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
    EnterSizeMove = None
    
    pass

class PalettePersistEventArgs(EventArgs):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    P
    
    e
    
    r
    
    s
    
    i
    
    s
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
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
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    c
    
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
    
    S
    
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
    
     
    
    c
    
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
    
     
    
    s
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    """
    ConfigurationSection = None
    
    pass

class PaletteSet(Autodesk.AutoCAD.Windows.Window, ICollection):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    S
    
    e
    
    t
    
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
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
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
    
     
    
    p
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    s
    
    e
    
    t
    
    
    
    
    
    
    
    
    
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    S
    
    e
    
    t
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    G
    
    u
    
    i
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
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
    
     
    
    p
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
     
    
    s
    
    e
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    G
    
    u
    
    i
    
    d
    
     
    
    t
    
    o
    
    o
    
    l
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    G
    
    U
    
    I
    
    D
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

class PaletteSetDockSite(public sealed class PaletteSetDockSite):
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

class PaletteSetFocusedEventArgs(EventArgs):
    """
    
    """

    pass

class PaletteSetSizeEventArgs(EventArgs):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    S
    
    e
    
    t
    
    S
    
    i
    
    z
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    c
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    i
    
    x
    
    e
    
    l
    
     
    
    w
    
    i
    
    d
    
    t
    
    h
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    c
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    i
    
    x
    
    e
    
    l
    
     
    
    h
    
    e
    
    i
    
    g
    
    h
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    d
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    e
    
    v
    
    i
    
    c
    
    e
    
    -
    
    i
    
    n
    
    d
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    t
    
     
    
    w
    
    i
    
    d
    
    t
    
    h
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    d
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    e
    
    v
    
    i
    
    c
    
    e
    
    -
    
    i
    
    n
    
    d
    
    e
    
    p
    
    e
    
    n
    
    d
    
    e
    
    n
    
    t
    
     
    
    h
    
    e
    
    i
    
    g
    
    h
    
    t
    """
    DeviceIndependentHeight = None
    
    
    DeviceIndependentWidth = None
    
    
    Height = None
    
    
    Width = None
    
    pass

class PaletteSetStateEventArgs(EventArgs):
    """
    
    P
    
    a
    
    l
    
    e
    
    t
    
    t
    
    e
    
    S
    
    e
    
    t
    
    S
    
    t
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    a
    
    t
    
    e
    
    E
    
    v
    
    e
    
    n
    
    t
    
    I
    
    n
    
    d
    
    e
    
    x
    
     
    
    s
    
    t
    
    a
    
    t
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    e
    
    v
    
    e
    
    n
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    s
    
    t
    
    a
    
    t
    
    e
    """
    NewState = None
    
    pass

  NameEditable = &H10
  Notify = &H400
  NoTitleBar = &H8000
  PauseAutoRollupForChildModalDialog = &H10000
  ShowAutoHideButton = 2
  ShowCloseButton = 8
  ShowPropertiesMenu = 4
  ShowTabForSingle = &H40
  SingleColDock = &H1000
  SingleRowDock = &H200
  SingleRowNoVertResize = &H800
  Snappable = &H20
  UsePaletteNameAsTitleForSingle = &H80

  Left
  Right

class Pane(StatusBarItem):
    """
    
    P
    
    a
    
    n
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    MaximumWidth = None
    
    
    MinimumWidth = None
    
    
    Style = None
    
    
    Text = None
    
    pass

class PaneCollection(IList):
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

  Command = 0x10
  NoBorders = 1
  Normal = 8
  PopOut = 2
  PopUp = 0x20
  Stretch = 4

class PlotStyleDialog(public sealed class PlotStyleDialog):
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

class SaveFileDialog(public sealed class SaveFileDialog):
    """
    
    S
    
    a
    
    v
    
    e
    
    F
    
    i
    
    l
    
    e
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
     
    
    o
    
    f
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
     
    
    b
    
    o
    
    x
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    f
    
    a
    
    u
    
    l
    
    t
    
    N
    
    a
    
    m
    
    e
    
     
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
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
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    a
    
    v
    
    e
    
    F
    
    i
    
    l
    
    e
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
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
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    """
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

class SizeChangingEventArgs(LocationChangingEventArgs):
    """
    
    S
    
    i
    
    z
    
    e
    
    C
    
    h
    
    a
    
    n
    
    g
    
    i
    
    n
    
    g
    
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
    NewSize = None
    
    
    Size = None
    
    pass

  Hide = 0
  Show = 1
  ThemeChange = 4

class StatusBar(public sealed class StatusBar):
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

class StatusBarItem(DisposableWrapper):
    """
    
    S
    
    t
    
    a
    
    t
    
    u
    
    s
    
    B
    
    a
    
    r
    
    I
    
    t
    
    e
    
    m
    
    (
    
    )
    
    (
    
    )
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

class StatusBarMouseDownEventArgs(EventArgs):
    """
    
    """
    Button = None
    
    
    DoubleClick = None
    
    
    X = None
    
    
    Y = None
    
    pass

class ToggleAblePopup(Popup):
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

class TrayItem(StatusBarItem):
    """
    
    T
    
    r
    
    a
    
    y
    
    I
    
    t
    
    e
    
    m
    
    (
    
    )
    
    (
    
    )
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

class TrayItemBubbleWindow(DisposableWrapper):
    """
    
    """
    HyperLink = None
    
    
    HyperText = None
    
    
    IconType = None
    
    
    Text = None
    
    
    Text2 = None
    
    
    Title = None
    
    pass

  FailedToCreate
  NoIcons
  NoNotifications
  ClosedByUser
  TimedOut
  HyperlinkClicked
  DocumentDeactivated

class TrayItemBubbleWindowClosedEventArgs(EventArgs):
    """
    
    """
    CloseReason = None
    
    pass

class TrayItemCollection(IList):
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

class Visuals(public sealed class Visuals):
    """
    
    """
    ApplicationIcon = None
    
    
    PickBitmap = None
    
    
    PickSetBitmap = None
    
    pass

class WPFDocumentWindow(DocumentWindow):
    """
    
    W
    
    P
    
    F
    
    D
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    i
    
    s
    
    u
    
    a
    
    l
    
     
    
    w
    
    p
    
    f
    
    V
    
    i
    
    s
    
    u
    
    a
    
    l
    
     
    
    :
    
     
    
    W
    
    P
    
    F
    
     
    
    v
    
    i
    
    s
    
    u
    
    a
    
    l
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    u
    
    s
    
    e
    
    d
    
     
    
    t
    
    o
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
     
    
    W
    
    P
    
    F
    
     
    
    d
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
     
    
    a
    
    s
    
     
    
    a
    
     
    
    s
    
    u
    
    b
    
    -
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
     
    
    o
    
    f
    
     
    
    A
    
    u
    
    t
    
    o
    
    C
    
    A
    
    D
    """
    def SetDocument(self):
        """
        SetDocument -> void
            
            object document: 
            Document object assosicated with the document window
        """
        pass
    
    pass

class Window(DisposableWrapper, IWin32Window):
    """
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    (
    
    )
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

class WindowExtension(public static class WindowExtension):
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

class WindowPositionChangedEventArgs(EventArgs):
    """
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    P
    
    o
    
    s
    
    i
    
    t
    
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
    
    (
    
    )
    """
    Moved = None
    
    
    Sized = None
    
    pass