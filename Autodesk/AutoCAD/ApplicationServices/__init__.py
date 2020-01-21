class Application(Autodesk.AutoCAD.ApplicationServices.Core.Application):
    """
    
    """
    def AddDefaultContextMenuExtension(self):
        """
        AddDefaultContextMenuExtension -> void
            
            ContextMenuExtension menuExtension: 
            Input Autodesk.AutoCAD.Windows.ContextMenuExtension object. The context (shortcut) menu to be displayed as part of the default context menu.
        """
        pass
    
    
    def AddObjectContextMenuExtension(self):
        """
        AddObjectContextMenuExtension -> void
            
            RXClass runtimeClass: 
            Input Autodesk.AutoCAD.Runtime.RXClass object. The runtime class of the object that has the context (shortcut) menu.
            
            ContextMenuExtension menuExtension: 
            Input Autodesk.AutoCAD.Windows.ContextMenuExtension object. The context (shortcut) menu to be displayed as part of the object selection context menu.
        """
        pass
    
    
    def DoDragDrop(self):
        """
        DoDragDrop -> void
            
            Control control: 
            Input the source.
            
            object data: 
            Input the data object.
            
            System.Windows.Forms.DragDropEffects allowedEffects: 
            Input effects allowed by the source.
            
            Autodesk.AutoCAD.Windows.DropTarget target: 
            Input the target location.
        """
        pass
    
    
    def LoadMainMenu(self):
        """
        LoadMainMenu -> bool
            
            string filename: 
            The menu filename. Can be provided with or without a path, though if provided without a path, it is expected that the file is located on the current support files search path. The method call is rejected if null or the empty string; to unload the main menu, supply "." .
        """
        pass
    
    
    def InvokeContextHelp(self):
        """
        InvokeContextHelp(IntPtr, int) -> void
            
            IntPtr window: 
            Input window.
            
            int contextId: 
            Input context ID.
        InvokeContextHelp(IntPtr, int, string) -> void
            
            IntPtr window: 
            Input window.
            
            int contextId: 
            Input context ID.
            
            string helpPrefix: 
            Input help prefix.
        InvokeContextHelp(IntPtr, int, string, HelpEventArgs) -> void
            
            fileName: 
            Input name of help file.
            
            topic: 
            Input topic to open.
        """
        pass
    
    
    def LoadPartialMenu(self):
        """
        LoadPartialMenu -> bool
            
            string filename: 
            The menu filename. Can be provided with or without a path, though if provided without a path, it is expected that the file is located on the current support files search path. The method call is rejected if the string is null, empty, or "." .
        """
        pass
    
    
    def InvokeHelp(self):
        """
        InvokeHelp -> void
            
            string fileName: 
            Input name of help file.
            
            string topic: 
            Input topic to open.
        """
        pass
    
    
    def InvokeHelpForExternal(self):
        """
        InvokeHelpForExternal -> bool
        
        """
        pass
    
    
    def ReloadAllMenus(self):
        """
        ReloadAllMenus -> void
        
        """
        pass
    
    
    def SetCurrentWorkspace(self):
        """
        SetCurrentWorkspace -> bool
            
            workspaceName: 
            The name of a workspace to make current.
        """
        pass
    
    
    def ToSystemDrawingPoint(self):
        """
        ToSystemDrawingPoint -> System.Drawing.Point
        
        """
        pass
    
    
    def ToSystemDrawingSize(self):
        """
        ToSystemDrawingSize -> System.Drawing.Size
        
        """
        pass
    
    
    def ToSystemWindowsPoint(self):
        """
        ToSystemWindowsPoint -> System.Windows.Point
        
        """
        pass
    
    
    def ToSystemWindowsSize(self):
        """
        ToSystemWindowsSize -> System.Windows.Size
        
        """
        pass
    
    
    def UnloadPartialMenu(self):
        """
        UnloadPartialMenu -> bool
            
            string filename: 
            The menu filename. Can be provided with or without a path, though there is a better chance of success if provided without a path.
        """
        pass
    
    
    def RemoveDefaultContextMenuExtension(self):
        """
        RemoveDefaultContextMenuExtension -> void
            
            ContextMenuExtension menuExtension: 
            Input Autodesk.AutoCAD.Windows.ContextMenuExtension object. The context (shortcut) menu to be removed as part of the default context menu.
        """
        pass
    
    
    def RemoveObjectContextMenuExtension(self):
        """
        RemoveObjectContextMenuExtension -> void
            
            RXClass runtimeClass: 
            Input Autodesk.AutoCAD.Runtime.RXClass object. The runtime class of the object that has the context (shortcut) menu.
            
            ContextMenuExtension menuExtension: 
            Input Autodesk.AutoCAD.Windows.ContextMenuExtension object. The context (shortcut) menu to be removed as part of the object selection context (shortcut) menu.
        """
        pass
    
    
    def ShowModalDialog(self):
        """
        ShowModalDialog(Form) -> System.Windows.Forms.DialogResult
            
            Form formToShow: 
            Input the form to be shown.
        ShowModalDialog(IWin32Window, Form) -> System.Windows.Forms.DialogResult
            
            IWin32Window owner: 
            Input the owner window of this dialog.
            
            Form formToShow: 
            Input the form to be shown.
        ShowModalDialog(IWin32Window, Form, [MarshalAs(UnmanagedType.U1)] bool) -> System.Windows.Forms.DialogResult
            
            IWin32Window owner: 
            Input the owner window of this dialog.
            
            Form formToShow: 
            Input the form to be shown.
            
            [MarshalAs(UnmanagedType.U1)] bool persistSizeAndPosition: 
            Input true if the size and position should not change.
        """
        pass
    
    
    def ShowModelessDialog(self):
        """
        ShowModelessDialog(Form) -> void
            
            Form formToShow: 
            Input object to show.
        ShowModelessDialog(IWin32Window, Form) -> void
            
            IWin32Window owner: 
            Input object which owns the form.
            
            Form formToShow: 
            Input object to show.
        ShowModelessDialog(IWin32Window, Form, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            IWin32Window owner: 
            Input object which owns the form.
            
            Form formToShow: 
            Input object to show.
            
            [MarshalAs(UnmanagedType.U1)] bool persistSizeAndPosition: 
            Input true if the size and position should not change.
        """
        pass
    
    
    def ShowModalWindow(self):
        """
        ShowModalWindow(IntPtr, Uri) -> bool
            
            IntPtr owner: 
            Owner Window.
            
            Uri htmlPage: 
            URI of the page to be loaded into the modal window.
        ShowModalWindow(IntPtr, Uri, [MarshalAs(UnmanagedType.U1)] bool) -> bool
            
            IntPtr owner: 
            Owner Window.
            
            Uri htmlPage: 
            URI of the page to be loaded into the modal window.
            
            [MarshalAs(UnmanagedType.U1)] bool persistSizeAndPosition: 
            Saves the current size and position of the window if set to true.
        ShowModalWindow(Uri) -> bool
            
            Uri htmlPage: 
            URI of the page to be loaded into the modal window.
        """
        pass
    
    
    def ShowModelessWindow(self):
        """
        ShowModelessWindow(IntPtr, Uri) -> void
            
            IntPtr owner: 
            Owner Window
            
            Uri htmlPage: 
            URI of the page to be loaded into the modeless window
        ShowModelessWindow(IntPtr, Uri, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            IntPtr owner: 
            Owner Window
            
            Uri htmlPage: 
            URI of the page to be loaded into the modeless window.
            
            [MarshalAs(UnmanagedType.U1)] bool persistSizeAndPosition: 
            Saves the current size and position of the window if set to true.
        ShowModelessWindow(Uri) -> void
            
            Uri htmlPage: 
            URI of the page to be loaded into the modeless window.
        """
        pass
    
    
    AcadApplication = None
    
    
    DocumentWindowCollection = None
    
    
    InfoCenter = None
    
    
    IsSteelInstalled = None
    
    
    MenuBar = None
    
    
    MenuGroups = None
    
    
    Preferences = None
    
    
    StatusBar = None
    
    pass

class BeginCloseAllEventArgs(EventArgs):
    """
    
    """
    IsVetoed = None
    
    pass

class BeginQuitEventArgs(EventArgs):
    """
    
    """
    IsVetoed = None
    
    pass

class CommandEventArgs(EventArgs):
    """
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
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
    GlobalCommandName = None
    
    pass

class ConfigurationSectionNameAttribute(Attribute):
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
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    N
    
    a
    
    m
    
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
    
     
    
    a
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
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
    
    .
    """
    Name = None
    
    pass

class DatabaseExtension(public static class DatabaseExtension):
    """
    
    """
    def Audit(self):
        """
        Audit -> void
            
            this Database db: 
            Database to audit.
            
            [MarshalAs(UnmanagedType.U1)] bool bFixErrors: 
            indicates whether or not to fix any errors found. Type is Boolean.
            
            [MarshalAs(UnmanagedType.U1)] bool bCmdLnEcho: 
            indicates whether or not to echo audit information to the command line as done by the AUDIT command. Type is Boolean.
        """
        pass
    
    pass

class DocWindowManagerReactor(internal struct DocWindowManagerReactor {
  private long <alignment member>;
}):
    """
    
    """

    pass

class Document(DisposableWrapper):
    """
    
    """
    def Create(self):
        """
        Create -> Document
            
            IntPtr unmanagedPointer: 
            Input unmanaged pointer
        """
        pass
    
    
    def DowngradeDocOpen(self):
        """
        DowngradeDocOpen -> void
            
            [MarshalAs(UnmanagedType.U1)] bool bPromptForSave: 
            Input Boolean to determine if a save prompt is necessary
        """
        pass
    
    
    def GetLispSymbol(self):
        """
        GetLispSymbol -> object
        
        """
        pass
    
    
    def LockDocument(self):
        """
        LockDocument() -> DocumentLock
        
        LockDocument(DocumentLockMode, string, string, [MarshalAs(UnmanagedType.U1)] bool) -> DocumentLock
            
            DocumentLockMode lockMode: 
            Input one of the locking modes from DocumentLockMode enum.
            
            string globalCommandName: 
            Input command name.Each time a document is locked, it is considered the beginning of a "command", or action in Acad. This name is passed back by the doc manager reactor as the name of the command doing the locking. It can be NULL.
            
            string localCommandName: 
            Input name that is displayed on the command line if or when this command is undone.It can be NULL.
            
            [MarshalAs(UnmanagedType.U1)] bool promptIfFails: 
            If the document cannot be locked, due to a command already in progress in the target document, and if prompt is true, the standard prompt will be issued, and the user will be given an opportunity to complete the command in the target document and the lock will succeed.If the user chooses to cancel the lock request, or prompt is false, then the lock change will fail
        """
        pass
    
    
    def LockMode(self):
        """
        LockMode() -> DocumentLockMode
        
        LockMode([MarshalAs(UnmanagedType.U1)] bool) -> DocumentLockMode
            
            [MarshalAs(UnmanagedType.U1)] bool bIncludeMyLocks: 
            Input Boolean indicating whether to consider this application's locks or just look at other context's locks.
        """
        pass
    
    
    def SendStringToExecute(self):
        """
        SendStringToExecute -> void
            
            string command: 
            Input document to send input to.
            
            [MarshalAs(UnmanagedType.U1)] bool activate: 
            Input Boolean indicating whether to activate the target document.
            
            [MarshalAs(UnmanagedType.U1)] bool wrapUpInactiveDoc: 
            Input Boolean indicating whether to queue current active document to complete in the next OnIdle() when switching active documents.
            
            [MarshalAs(UnmanagedType.U1)] bool echoCommand: 
            Input Boolean indicating whether the sent string is echoed on the command line.
        """
        pass
    
    
    def SetLispSymbol(self):
        """
        SetLispSymbol -> void
        
        """
        pass
    
    
    def UpgradeDocOpen(self):
        """
        UpgradeDocOpen -> void
        
        """
        pass
    
    
    CommandInProgress = None
    
    
    Database = None
    
    
    Editor = None
    
    
    FormatForSave = None
    
    
    GraphicsManager = None
    
    
    IsActive = None
    
    
    IsNamedDrawing = None
    
    
    IsReadOnly = None
    
    
    Name = None
    
    
    TransactionManager = None
    
    
    UserData = None
    
    
    Window = None
    
    pass

class DocumentActivationChangedEventArgs(EventArgs):
    """
    
    """
    NewValue = None
    
    pass

class DocumentBeginCloseEventArgs(EventArgs):
    """
    
    """
    def Veto(self):
        """
        Veto -> void
        
        """
        pass
    
    pass

class DocumentClosedEventArgs(EventArgs):
    """
    
    """
    RecentDocument = None
    
    pass

class DocumentCollection(MarshalByRefObject, ICollection):
    """
    
    """
    class ExecutionResult(INotifyCompletion):
        """
        
        """
        def GetAwaiter(self):
            """
            GetAwaiter -> DocumentCollection.ExecutionResult
            
            """
            pass
        
        
        def GetResult(self):
            """
            GetResult -> void
            
            """
            pass
        
        
        def OnCompleted(self):
            """
            OnCompleted -> void
            
            """
            pass
        
        
        IsCompleted = None
        
        pass
    
    
    def AppContextNewDocument(self):
        """
        AppContextNewDocument -> void
            
            string templateFileName: 
            Input path/filename or URL of template file to use
        """
        pass
    
    
    def AppContextOpenDocument(self):
        """
        AppContextOpenDocument -> void
            
            string fileName: 
            Input path/filenam
        """
        pass
    
    
    def AppContextRecoverDocument(self):
        """
        AppContextRecoverDocument -> void
        
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Document[] array: 
            Input the one-dimensional array that is the destination of the elements copied from DocumentCollection. The array must have zero-based indexing.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def ExecuteInApplicationContext(self):
        """
        ExecuteInApplicationContext -> void
            
            ExecuteInApplicationContextCallback callback: 
            Input Autodesk.AutoCAD.ApplicationServices.ExecuteInApplicationContextCallback object.
            
            object data: 
            Input any data that should be used for the function call.
        """
        pass
    
    
    def ExecuteInCommandContextAsync(self):
        """
        ExecuteInCommandContextAsync -> ExecutionResult
            
            Func<object, System.Threading.Tasks.Task> callback: 
            Input System.Threading.Tasks.Task object.
            
            object data: 
            Input any data that should be used for the function call.
        """
        pass
    
    
    def GetDocument(self):
        """
        GetDocument -> Document
            
            Database db: 
            Input database to obtain from.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def GetPendingDocumentForSwitch(self):
        """
        GetPendingDocumentForSwitch -> Document>
        
        """
        pass
    
    
    Count = None
    
    
    CurrentDocument = None
    
    
    DefaultFormatForSave = None
    
    
    DocumentActivationEnabled = None
    
    
    IsApplicationContext = None
    
    
    MdiActiveDocument = None
    
    pass

class DocumentCollectionEventArgs(EventArgs):
    """
    
    """
    Document = None
    
    pass

class DocumentCollectionExtension(public static class DocumentCollectionExtension):
    """
    
    """
    def Add(self):
        """
        Add -> Document
            
            string templateFileName: 
            Input System.String object.
        """
        pass
    
    
    def CloseAll(self):
        """
        CloseAll -> void
        
        """
        pass
    
    
    def Open(self):
        """
        Open(this DocumentCollection, string) -> Document
            
            string fileName: 
            Input System.String object. The name of the drawing file to open.
        Open(this DocumentCollection, string, [MarshalAs(UnmanagedType.U1)] bool) -> Document
            
            string fileName: 
            Input System.String object. The name of the drawing file to open.
            
            [MarshalAs(UnmanagedType.U1)] bool forReadOnly: 
            Input true if the item is to be read only
        Open(this DocumentCollection, string, [MarshalAs(UnmanagedType.U1)] bool, string) -> Document
            
            string fileName: 
            Input System.String object. The name of the drawing file to open.
            
            [MarshalAs(UnmanagedType.U1)] bool forReadOnly: 
            Input true if the item is to be read only
            
            string password: 
            Input a password, if the file is locked
        """
        pass
    
    pass

class DocumentDestroyedEventArgs(EventArgs):
    """
    
    """
    FileName = None
    
    pass

class DocumentExtension(public static class DocumentExtension):
    """
    
    """
    def CapturePreviewImage(self):
        """
        CapturePreviewImage -> Bitmap
            
            uint modopt(IsLong) width: 
            Input image width
            
            uint modopt(IsLong) height: 
            Input image height
        """
        pass
    
    
    def CloseAndDiscard(self):
        """
        CloseAndDiscard -> void
        
        """
        pass
    
    
    def CloseAndSave(self):
        """
        CloseAndSave -> void
            
            string fileName: 
            Input file to save to
        """
        pass
    
    
    def FromAcadDocument(self):
        """
        FromAcadDocument -> Document
            
            object acadDocument: 
            Input the object to be converted
        """
        pass
    
    
    def GetAcadDocument(self):
        """
        GetAcadDocument -> object
            
            this Document doc: 
            _nt_
        """
        pass
    
    
    def GetStatusBar(self):
        """
        GetStatusBar -> StatusBar
            
            this Document doc: 
            _nt_
        """
        pass
    
    pass

class DocumentLock(IDisposable):
    """
    
    """

    pass

class DocumentLockMode():
    AutoWrite = 1
    ExclusiveWrite = 0x40
    None = 0
    NotLocked = 2
    ProtectedAutoWrite = 20
    Read = 0x20
    Write = 4

class DocumentLockModeChangeVetoedEventArgs(EventArgs):
    """
    
    """
    Document = None
    
    
    GlobalCommandName = None
    
    pass

class DocumentLockModeChangedEventArgs(EventArgs):
    """
    
    """
    def Veto(self):
        """
        Veto -> void
        
        """
        pass
    
    
    CurrentMode = None
    
    
    Document = None
    
    
    GlobalCommandName = None
    
    
    MyCurrentMode = None
    
    
    MyPreviousMode = None
    
    pass

class DocumentLockModeWillChangeEventArgs(EventArgs):
    """
    
    """
    CurrentMode = None
    
    
    Document = None
    
    
    GlobalCommandName = None
    
    
    MyCurrentMode = None
    
    
    MyNewMode = None
    
    pass

class DocumentPinStateChangedEventArgs(EventArgs):
    """
    
    """
    RecentDocument = None
    
    pass

class DocumentSaveFormat():
    Native = 0x40
    R12Dxf = 1
    R13Dwg = 4
    R13Dxf = 5
    R14Dwg = 8
    R14Dxf = 9
    R2000Dwg = 12
    R2000Dxf = 13
    R2000Standard = 15
    R2000Template = 14
    R2000Xml = 0x10
    R2004Dwg = 0x18
    R2004Dxf = 0x19
    R2004Standard = 0x1b
    R2004Template = 0x1a
    R2007Dwg = 0x24
    R2007Dxf = 0x25
    R2007Standard = 0x27
    R2007Template = 0x26
    R2010Dwg = 0x30
    R2010Dxf = 0x31
    R2010Standard = 0x33
    R2010Template = 50
    R2013Dwg = 60
    R2013Dxf = 0x3d
    R2013Standard = 0x3f
    R2013Template = 0x3e
    R2018Dwg = 0x40
    R2018Dxf = 0x41
    R2018Standard = 0x43
    R2018Template = 0x42
    Unknown = -1

class DocumentWindowActivatedEventArgs(EventArgs):
    """
    
    """
    DocumentWindow = None
    
    pass

class DocumentWindowCollection(ICollection, INotifyCollectionChanged, IDisposable):
    """
    
    """
    def AddDocumentWindow(self):
        """
        AddDocumentWindow(DocumentWindow) -> bool
            
            DocumentWindow documentWindow: 
            document window to be added into document window collection
        AddDocumentWindow(string, Uri) -> DocumentWindow
            
            string title: 
            Title of the document window which will be shown in the file tab
            
            Uri htmlPage: 
            URI of the web page
        """
        pass
    
    
    def ArrangeIcons(self):
        """
        ArrangeIcons -> void
        
        """
        pass
    
    
    def Cascade(self):
        """
        Cascade -> void
        
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
        
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def LookupDocumentWindow(self):
        """
        LookupDocumentWindow -> DocumentWindow
        
        """
        pass
    
    
    def MoveDocumentWindow(self):
        """
        MoveDocumentWindow -> bool
            
            DocumentWindow documentWindow: 
            Document window to be moved
            
            int newIndex: 
            New index for where to put the document window moved as the new position, the range for this parameter should be between 0 and Count-1
            
            Exceptions: 
            Description
            
            System::IndexOutOfRangeException will be thrown if newIndex is less than 0 or larger than Count-1: 
        """
        pass
    
    
    def TileHorizontally(self):
        """
        TileHorizontally -> void
        
        """
        pass
    
    
    def TileVertically(self):
        """
        TileVertically -> void
        
        """
        pass
    
    
    ActiveDocumentWindow = None
    
    
    Count = None
    
    
    IsSynchronized = None
    
    
    SyncRoot = None
    
    
    System.Collections.ICollection.IsSynchronized = None
    
    
    System.Collections.ICollection.SyncRoot = None
    
    pass

class IConfigurationSection(IDisposable):
    """
    
    """
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string name: 
            Input name to search for.
        """
        pass
    
    
    def ContainsSubsection(self):
        """
        ContainsSubsection -> bool
            
            string name: 
            Input subsection to search for.
        """
        pass
    
    
    def CreateSubsection(self):
        """
        CreateSubsection -> IConfigurationSection
            
            string name: 
            Input new subsection name.
        """
        pass
    
    
    def Delete(self):
        """
        Delete -> void
            
            string name: 
            Input name of item to delete.
        """
        pass
    
    
    def DeleteSubsection(self):
        """
        DeleteSubsection -> void
            
            string name: 
            Input the name of the subsection to delete.
        """
        pass
    
    
    def OpenSubsection(self):
        """
        OpenSubsection -> IConfigurationSection
            
            string name: 
            Input the subsection name to open.
        """
        pass
    
    
    def ReadProperty(self):
        """
        ReadProperty -> object
            
            string name: 
            Input the name to read
            
            object defaultValue: 
            Input default value to return
        """
        pass
    
    
    def WriteProperty(self):
        """
        WriteProperty -> void
            
            string name: 
            Input the name to read
            
            object value: 
            Input default value to return
        """
        pass
    
    
    IsReadOnly = None
    
    pass

class InplaceTextEditor(TextEditor):
    """
    
    """
    class TextUndoType():
        UndoAnnoState = 0x3a
        UndoAttachment = 0x25
        UndoAutoDimBreak = 0x22
        UndoAutoDimension = 0x21
        UndoAutoDTextEscape = 0x1f
        UndoAutoField = 0x1c
        UndoAutoMifOrCif = 0x20
        UndoAutoSpell = 0x23
        UndoAutoStack = 0x1d
        UndoAutoSymbol = 30
        UndoBackspace = 0x11
        UndoBoldOff = 3
        UndoBoldOn = 2
        UndoChangeCase = 0x26
        UndoCharAttributes = 0x31
        UndoColor = 12
        UndoColumns = 0x39
        UndoCombineParagraphs = 40
        UndoCursorAttributes = 0x38
        UndoCustomConvert = 0x35
        UndoCut = 20
        UndoDelete = 0x12
        UndoDeleteAndMoveSelection = 0x36
        UndoDimBreakInsert = 0x34
        UndoDimensionInsert = 0x33
        UndoDimensionSymbol = 60
        UndoDimensionTemplate = 0x3d
        UndoDimensionTweak = 0x3b
        UndoFieldConvert = 0x19
        UndoFieldInsert = 0x18
        UndoFieldUpdate = 0x1a
        UndoFont = 10
        UndoHeight = 11
        UndoImportText = 0x27
        UndoItalicOff = 5
        UndoItalicOn = 4
        UndoLanguage = 0x10
        UndoObliqueAngle = 13
        UndoOverlineOff = 9
        UndoOverlineOn = 8
        UndoParagraphAttributes = 0x2e
        UndoParagraphNumbering = 0x37
        UndoPaste = 0x13
        UndoRemoveAllFormatting = 0x2b
        UndoRemoveCharFormatting = 0x29
        UndoRemoveParaFormatting = 0x2a
        UndoReplace = 0x2d
        UndoReplaceAll = 0x2c
        UndoSetDefinedHeight = 0x30
        UndoSetDefinedWidth = 0x2f
        UndoStack = 0x15
        UndoStackProperties = 0x17
        UndoStyle = 0x24
        UndoSymbolInsert = 0x1b
        UndoTrackingFactor = 15
        UndoTyping = 1
        UndoUnderlineOff = 7
        UndoUnderlineOn = 6
        UndoUnstack = 0x16
        UndoWidthScale = 14
        UndoWipeout = 50
    
    
    def AddUndoMarker(self):
        """
        AddUndoMarker -> void
        
        """
        pass
    
    
    def AttachmentMenus(self):
        """
        AttachmentMenus -> void
        
        """
        pass
    
    
    def ColumnMenus(self):
        """
        ColumnMenus -> void
        
        """
        pass
    
    
    def ColumnsDialog(self):
        """
        ColumnsDialog -> void
        
        """
        pass
    
    
    def ContextMenus(self):
        """
        ContextMenus -> void
        
        """
        pass
    
    
    def Copy(self):
        """
        Copy -> void
        
        """
        pass
    
    
    def Cut(self):
        """
        Cut -> void
        
        """
        pass
    
    
    def DrawHightlight(self):
        """
        DrawHightlight -> void
        
        """
        pass
    
    
    def FieldDialog(self):
        """
        FieldDialog -> void
        
        """
        pass
    
    
    def FindAndReplaceDialog(self):
        """
        FindAndReplaceDialog -> void
        
        """
        pass
    
    
    def FindMatchItem(self):
        """
        FindMatchItem -> void
        
        """
        pass
    
    
    def HelpDialog(self):
        """
        HelpDialog -> void
        
        """
        pass
    
    
    def HightlightColorDialog(self):
        """
        HightlightColorDialog -> void
        
        """
        pass
    
    
    def ImportTextDialog(self):
        """
        ImportTextDialog -> void
        
        """
        pass
    
    
    def InsertFile(self):
        """
        InsertFile -> void
        
        """
        pass
    
    
    def Invoke(self):
        """
        Invoke(DBText, [In, Out] ref ObjectId[]) -> void
        
        Invoke(MText, InplaceTextEditorSettings) -> void
        
        """
        pass
    
    
    def LineSpaceMenus(self):
        """
        LineSpaceMenus -> void
        
        """
        pass
    
    
    def NewFeatureWorkShop(self):
        """
        NewFeatureWorkShop -> void
        
        """
        pass
    
    
    def NumberingMenus(self):
        """
        NumberingMenus -> void
        
        """
        pass
    
    
    def OtherSymbol(self):
        """
        OtherSymbol -> void
        
        """
        pass
    
    
    def ParagraphDialog(self):
        """
        ParagraphDialog -> void
        
        """
        pass
    
    
    def Paste(self):
        """
        Paste -> void
        
        """
        pass
    
    
    def PasteWithoutFormats(self):
        """
        PasteWithoutFormats -> void
        
        """
        pass
    
    
    def Redo(self):
        """
        Redo -> void
        
        """
        pass
    
    
    def RemoveHightlight(self):
        """
        RemoveHightlight -> void
        
        """
        pass
    
    
    def ReplaceAllMatches(self):
        """
        ReplaceAllMatches -> void
        
        """
        pass
    
    
    def ReplaceCurrentMatch(self):
        """
        ReplaceCurrentMatch -> void
        
        """
        pass
    
    
    def SetStaticColumnsWithCount(self):
        """
        SetStaticColumnsWithCount -> void
        
        """
        pass
    
    
    def SpellDictionaryDialog(self):
        """
        SpellDictionaryDialog -> void
        
        """
        pass
    
    
    def SpellSettingDialog(self):
        """
        SpellSettingDialog -> void
        
        """
        pass
    
    
    def StackPropertyDialog(self):
        """
        StackPropertyDialog -> void
        
        """
        pass
    
    
    def SymbolMenus(self):
        """
        SymbolMenus -> void
        
        """
        pass
    
    
    def Undo(self):
        """
        Undo -> void
        
        """
        pass
    
    
    def WipeoutDialog(self):
        """
        WipeoutDialog -> void
        
        """
        pass
    
    
    alginment = None
    
    
    Annotative = None
    
    
    CanCopy = None
    
    
    CanCut = None
    
    
    CanExitEditor = None
    
    
    CanPaste = None
    
    
    CanRedo = None
    
    
    CanUndo = None
    
    
    Current = None
    
    
    ForcedOpaqueBackground = None
    
    
    LayerColor = None
    
    
    MultiAttribute = None
    
    
    OpaqueBackground = None
    
    
    ParagraphSupported = None
    
    
    RulerHidden = None
    
    
    RulerSupported = None
    
    
    SimpleMText = None
    
    
    SpellerEnabled = None
    
    
    TableCell = None
    
    
    Text = None
    
    
    ToolbarHidden = None
    
    
    ToolbarOptionHidden = None
    
    
    UndoRecordingDisabled = None
    
    
    Wysiwyg = None
    
    pass

class InplaceTextEditorSettings(DisposableWrapper):
    """
    
    I
    
    n
    
    p
    
    l
    
    a
    
    c
    
    e
    
    T
    
    e
    
    x
    
    t
    
    E
    
    d
    
    i
    
    t
    
    o
    
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
    class EditFlags():
        CursorAtEnd = 4
        ForceOpaqueBackground = 1
        SelectAll = 2
    
    
    class EntityType():
        Default
        TableCell
        MultiAttribute
    
    
    DefinedHeight = None
    
    
    Flags = None
    
    
    SimpleMText = None
    
    
    TabSupported = None
    
    
    Type = None
    
    pass

class LayoutSwitchedEventArgs(EventArgs):
    """
    
    """
    NewLayout = None
    
    pass

class LayoutSwitchingEventArgs(EventArgs):
    """
    
    """
    NewLayout = None
    
    
    OldLayout = None
    
    pass

class LispWillStartEventArgs(EventArgs):
    """
    
    """
    FirstLine = None
    
    pass

class LongTransactionManager(RXObject):
    """
    
    """
    def AbortLongTransaction(self):
        """
        AbortLongTransaction -> void
        
        """
        pass
    
    
    def AddClassFilter(self):
        """
        AddClassFilter -> void
        
        """
        pass
    
    
    def CheckIn(self):
        """
        CheckIn -> void
        
        """
        pass
    
    
    def CheckOut(self):
        """
        CheckOut -> ObjectId
        
        """
        pass
    
    
    def CurrentLongTransactionFor(self):
        """
        CurrentLongTransactionFor -> ObjectId
        
        """
        pass
    
    
    def IsFiltered(self):
        """
        IsFiltered -> bool
        
        """
        pass
    
    pass

class RecentDocumentCollection(ReadOnlyObservableCollection<RecentDocument>, IDisposable):
    """
    
    """
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
        
        """
        pass
    
    
    Instance = None
    
    
    UsePinnedItems = None
    
    pass

class SystemVariableChangedEventArgs(EventArgs):
    """
    
    """
    Changed = None
    
    
    Name = None
    
    pass

class SystemVariableChangingEventArgs(EventArgs):
    """
    
    """
    Name = None
    
    pass

class TabbedDialogEventArgs(EventArgs):
    """
    
    """
    def AddTab(self):
        """
        AddTab -> void
            
            string name: 
            Input the name of the newly created tab.
            
            TabbedDialogExtension extension: 
            Input a TabeddedDialogExtension that is responsible for the client area of the new tab.
        """
        pass
    
    pass

class TabbedDialogExtension(public sealed class TabbedDialogExtension):
    """
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    o
    
    w
    
    n
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    O
    
    K
    
     
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
    n
    
     
    
    "
    
    O
    
    k
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    o
    
    w
    
    n
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    O
    
    K
    
     
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
    n
    
     
    
    "
    
    O
    
    k
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    C
    
    a
    
    n
    
    c
    
    e
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
     
    
    "
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    o
    
    w
    
    n
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    O
    
    K
    
     
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
    n
    
     
    
    "
    
    O
    
    k
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    C
    
    a
    
    n
    
    c
    
    e
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
     
    
    "
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    H
    
    e
    
    l
    
    p
    
     
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
     
    
    "
    
    H
    
    e
    
    l
    
    p
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    (
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    s
    
    .
    
    F
    
    o
    
    r
    
    m
    
    s
    
    .
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    o
    
    w
    
    n
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    e
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    O
    
    K
    
     
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
    n
    
     
    
    "
    
    O
    
    k
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    C
    
    a
    
    n
    
    c
    
    e
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
     
    
    "
    
    C
    
    a
    
    n
    
    c
    
    e
    
    l
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    H
    
    e
    
    l
    
    p
    
     
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
     
    
    "
    
    H
    
    e
    
    l
    
    p
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    n
    
    A
    
    p
    
    p
    
    l
    
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
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    r
    
    v
    
    i
    
    c
    
    e
    
    s
    
    .
    
    T
    
    a
    
    b
    
    b
    
    e
    
    d
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    h
    
    a
    
    n
    
    d
    
    l
    
    e
    
     
    
    w
    
    h
    
    a
    
    t
    
     
    
    h
    
    a
    
    p
    
    p
    
    e
    
    n
    
    s
    
     
    
    o
    
    n
    
     
    
    a
    
    n
    
     
    
    "
    
    A
    
    p
    
    p
    
    l
    
    y
    
    "
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
    .
    """
    def SetDirty(self):
        """
        SetDirty -> void
            
            System.Windows.Forms.Control control: 
            Input System.Windows.Forms.Control object to set the bit for.
            
            [MarshalAs(UnmanagedType.U1)] bool dirty: 
            Input System.Boolean object value for the bit.
        """
        pass
    
    
    Control = None
    
    
    OnApply = None
    
    
    OnCancel = None
    
    
    OnHelp = None
    
    
    OnOk = None
    
    pass

class UnknownCommandEventArgs(EventArgs):
    """
    
    """
    GlobalCommandName = None
    
    pass

class UserConfigurationManager(MarshalByRefObject):
    """
    
    """
    def OpenCurrentProfile(self):
        """
        OpenCurrentProfile -> IConfigurationSection
        
        """
        pass
    
    
    def OpenDialogSection(self):
        """
        OpenDialogSection -> IConfigurationSection
            
            object dialog: 
            Input System.Object object. Input dialog name whose registry entry is to be retrieved.
        """
        pass
    
    
    def OpenGlobalSection(self):
        """
        OpenGlobalSection -> IConfigurationSection
        
        """
        pass
    
    pass

class WhoHasInfo(public struct WhoHasInfo {
}):
    """
    
    """
    ComputerName = None
    
    
    IsFileLocked = None
    
    
    OpenTime = None
    
    
    UserName = None
    
    pass

class XrefFileLock(DisposableWrapper):
    """
    
    """
    def ConsistencyCheck(self):
        """
        ConsistencyCheck() -> void
        
        ConsistencyCheck(ObjectId) -> ObjectIdCollection
            
            ObjectId selectedBlockId: 
            Selected BTR object ID to operate on
        """
        pass
    
    
    def ConsistencyCheckLocal(self):
        """
        ConsistencyCheckLocal -> ObjectIdCollection
            
            ObjectId selectedBlockId: 
            Selected BTR object ID to operate on
        """
        pass
    
    
    def GetXloadCtlType(self):
        """
        GetXloadCtlType -> Integer
            
            ObjectId selectedBlockId: 
            Selected BTR object ID to operate on
        """
        pass
    
    
    def LockFile(self):
        """
        LockFile -> XrefFileLock
            
            ObjectId selectedBlockId: 
            Block Table Record object ID to operate on
        """
        pass
    
    
    def ReleaseFile(self):
        """
        ReleaseFile -> void
        
        """
        pass
    
    
    def ReloadFile(self):
        """
        ReloadFile() -> void
        
        ReloadFile(int) -> void
            
            int xldCtlType: 
            XLOADCTL mode to reload with
        """
        pass
    
    
    OutOfSyncBlockIds = None
    
    
    XloadCtlType = None
    
    pass