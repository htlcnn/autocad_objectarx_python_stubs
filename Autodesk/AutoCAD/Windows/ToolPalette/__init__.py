class AccessRight():
    Read = 1
    ReadOnlyFile = 4
    ReadWrite = 2

class Catalog(object):
    """
    
    Catalog()()
    
    
    """

    pass

class CatalogItem(object):
    """
    
    CatalogItem()()
    
    
    """
    def AddChild(self):
        """
        AddChild -> Integer
            
            CatalogItem newItem: 
            Input the new item to be added.
        """
        pass
    
    
    def AddTargetProduct(self):
        """
        AddTargetProduct -> Integer
            
            TargetProductInfo productInfo: 
            Input product information.
        """
        pass
    
    
    def AssignNewId(self):
        """
        AssignNewId -> void
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input bool to indicate whether to set new IDs in children
        """
        pass
    
    
    def DeleteAllChildren(self):
        """
        DeleteAllChildren -> void
        
        """
        pass
    
    
    def DeleteChild(self):
        """
        DeleteChild -> void
            
            CatalogItem item: 
            Input the child item to be deleted from this item's list of children.
        """
        pass
    
    
    def DeleteImageFile(self):
        """
        DeleteImageFile -> void
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input Boolean to indicate whether to delete image files of children.
        """
        pass
    
    
    def DeleteLinkFile(self):
        """
        DeleteLinkFile -> void
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input Boolean to indicate whether children's links should be deleted
        """
        pass
    
    
    def DeleteOverlayImageFile(self):
        """
        DeleteOverlayImageFile -> void
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input that indicates whether to delete images recursively
        """
        pass
    
    
    def DeleteTargetProduct(self):
        """
        DeleteTargetProduct -> void
            
            int index: 
            Input of the target product to delete
        """
        pass
    
    
    def DetachChild(self):
        """
        DetachChild -> void
            
            CatalogItem item: 
            Input child item to be detached from this item's list of children
        """
        pass
    
    
    def DoRefresh(self):
        """
        DoRefresh -> void
            
            RefreshFlags flag: 
            Input refresh flag
        """
        pass
    
    
    def Download(self):
        """
        Download -> void
            
            Uri url: 
            Input URL to download; should point to the same type of catalog item that is represented by this object.
            
            DownloadFlags flag: 
            Input download flag, which can be one or more of the DownloadFlags.
            
            string downloadPath: 
            Input path to which the URL will be downloaded; if NULL, the URL is downloaded to TEMP directory
        """
        pass
    
    
    def FindInChildren(self):
        """
        FindInChildren(Guid, [MarshalAs(UnmanagedType.U1)] bool) -> CatalogItem
            
            Guid id: 
            Input ID to find
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input Boolean specifying whether to search recursively (the children of the children) or only search the children of this item
        FindInChildren(string, [MarshalAs(UnmanagedType.U1)] bool) -> CatalogItem
            
            string name: 
            Input name of the item for which to search
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input Boolean specifying whether to search recursively (the children of the children) or only search the children of this item
        """
        pass
    
    
    def FromFile(self):
        """
        FromFile -> CatalogItem
            
            string file: 
            Input specifying the XML file that contains the catalog item.
            
            [MarshalAs(UnmanagedType.U1)] bool load: 
            Input Boolean to indicate whether the function should load the file into the newly created catalog item.
            
            LoadFlags flags: 
            Input ignored if load is false
        """
        pass
    
    
    def GetImage(self):
        """
        GetImage -> Autodesk.AutoCAD.Windows.ToolPalette.Image
            
            Size size: 
            Input indicating the image size
        """
        pass
    
    
    def GetChild(self):
        """
        GetChild -> CatalogItem
            
            int index: 
            Input index of the child to be retrieved.
        """
        pass
    
    
    def GetImageFilePath(self):
        """
        GetImageFilePath -> string
            
            int index: 
            Input of the image.
        """
        pass
    
    
    def GetReferencePath(self):
        """
        GetReferencePath -> string
            
            index: 
            Input index of the reference path.
        """
        pass
    
    
    def GetTargetProduct(self):
        """
        GetTargetProduct -> TargetProductInfo
            
            int index: 
            Input zero-based index of a target product list item.
        """
        pass
    
    
    def GetType(self):
        """
        GetType -> CatalogItemType
            
            string filename: 
            Input the name of an XML file that contains a catalog item
        """
        pass
    
    
    def GetXml(self):
        """
        GetXml -> string
            
            SaveFlags flag: 
            Input save option flags.
        """
        pass
    
    
    def InsertChild(self):
        """
        InsertChild -> Integer
            
            int index: 
            Input at which to insert the item .
            
            CatalogItem newItem: 
            Input object to be inserted.
        """
        pass
    
    
    def IsValidForProduct(self):
        """
        IsValidForProduct -> bool
            
            string productName: 
            Input the product name.
            
            int majorVersion: 
            Input the major version of the product.
            
            int minorVersion: 
            Input the minor version of the product.
            
            int localeId: 
            Input the locale identifier of the product.
        """
        pass
    
    
    def Load(self):
        """
        Load -> void
            
            Uri url: 
            Input specifying the file from which the item is loaded.
            
            LoadFlags flags: 
            Input one of the LoadFlags options.
        """
        pass
    
    
    def LoadLink(self):
        """
        LoadLink -> void
        
        """
        pass
    
    
    def Save(self):
        """
        Save -> void
            
            Uri url: 
            Input specifying the file to which the item is saved.
            
            SaveFlags flag: 
            Input the SaveFlags value.
        """
        pass
    
    
    def SetHelpInfo(self):
        """
        SetHelpInfo -> void
            
            string file: 
            Input specifying an HTML file, a URL, or a compiled HTML Help (CHM) file.
            
            string command: 
            Input command string.
            
            string data: 
            Input additional data required to display the help
            
            HELP_HHWND_TOPIC: file points to an HTML file, a URL, or a compiled HTML Help (CHM) file. Display the topic in HTML Help window. data should contain the topic to display.
            
            HELP_HHWND_INDEX: file points to an HTML file, a URL, or a compiled HTML Help (CHM) file. Opens the HTML Help window and attempts to find the help item in the index. data should contain the help item.
            
            HELP_BROWSER_URL: file points to a URL which should be opened in a browser.
        """
        pass
    
    
    def SetItemOrder(self):
        """
        SetItemOrder -> void
            
            CatalogItem[] itemsInOrder: 
            Input object containing the catalog items in the order in which they should be arranged in the view.
        """
        pass
    
    
    def SetReferencePath(self):
        """
        SetReferencePath -> void
            
            string value: 
            Input string to be used as the reference path for the item.
            
            int flag: 
            Input indicating type of reference path to set.
        """
        pass
    
    
    AccessRight = None
    
    
    AutoRefresh = None
    
    
    CanRefresh = None
    
    
    ChildCount = None
    
    
    CreateTime = None
    
    
    CustomData = None
    
    
    Description = None
    
    
    HasChildren = None
    
    
    HelpInfoCommand = None
    
    
    HelpInfoData = None
    
    
    HelpInfoFile = None
    
    
    ID = None
    
    
    ImageList = None
    
    
    IsLink = None
    
    
    IsLinkLoaded = None
    
    
    IsReadOnly = None
    
    
    IsRoot = None
    
    
    ItemOptions = None
    
    
    Keywords = None
    
    
    LastModifiedTime = None
    
    
    LastRefreshedTime = None
    
    
    LinkFilePath = None
    
    
    LinkUrl = None
    
    
    LocalFile = None
    
    
    Name = None
    
    
    OverlayImage = None
    
    
    OverlayImageFilePath = None
    
    
    OverlayImageInfo = None
    
    
    Parent = None
    
    
    ParentDocumentDescription = None
    
    
    ParentDocumentName = None
    
    
    ParentDocumentUrl = None
    
    
    PublisherCountry = None
    
    
    PublisherDescription = None
    
    
    PublisherEmail = None
    
    
    PublisherName = None
    
    
    PublisherUrl = None
    
    
    Refresh = None
    
    
    Root = None
    
    
    Scheme = None
    
    
    SourceID = None
    
    
    SourceUrl = None
    
    
    TargetProductCount = None
    
    
    ToolTipText = None
    
    
    Url = None
    
    pass

class CatalogItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            CatalogItem item: 
            Input item to be added.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            CatalogItem[] array: 
            Input array to copy from
            
            int index: 
            Input index to begin copying
        """
        pass
    
    
    def Find(self):
        """
        Find -> CatalogItem
            
            Guid guid: 
            Input item to find
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove(CatalogItem) -> void
            
            CatalogItem catalogItem: 
            Input object to be removed.
        Remove(Guid) -> void
            
            Guid guid: 
            Input of the item to be removed.
        """
        pass
    
    
    Count = None
    
    pass

class CatalogItemType():
    ItemCatalog = 0x10
    ItemCategory = 8
    ItemPackage = 2
    ItemPalette = 4
    ItemStockTool = 0x20
    ItemTool = 1
    ItemUnknown = 0

class CatalogSet(object):
    """
    
    """
    def LoadCatalogs(self):
        """
        LoadCatalogs() -> void
        
        LoadCatalogs(LoadFlags) -> void
            
            LoadFlags options: 
            Input object, which can be one or more of the LoadOption enum values (multiple values can be combined with bitwise OR)
        """
        pass
    
    
    def SaveCatalogs(self):
        """
        SaveCatalogs() -> void
        
        SaveCatalogs(SaveFlags) -> void
            
            SaveFlags flags: 
            Input save flags
        """
        pass
    
    
    def UnloadCatalogs(self):
        """
        UnloadCatalogs -> void
        
        """
        pass
    
    
    CatalogPath = None
    
    
    Catalogs = None
    
    
    Scheme = None
    
    pass

class CatalogTypeFlags():
    Catalog = 1
    ShapeCatalog = 4
    StockToolCatalog = 2

class Category(object):
    """
    
    Category()()
    
    
    """

    pass

class ContextMenuMode():
    ContextMenuEditorImage = 1
    ContextMenuPaletteBackground = 2
    ContextMenuPaletteSetCaption = 4
    ContextMenuPaletteSetOptionButton = 5
    ContextMenuPaletteSetTab = 3
    ContextMenuPaletteTool = 0
    ContextNone = -1

class CustomToolBase(object):
    """
    
    CustomToolBase()
    """
    def BeginEdit(self):
        """
        BeginEdit -> void
        
        """
        pass
    
    
    def CreateCommandTool(self):
        """
        CreateCommandTool -> Autodesk.AutoCAD.Windows.ToolPalette.Tool
            
            keyState: 
            Input key state
            
            pt: 
            Input point
            
            effect: 
            Input effect
        """
        pass
    
    
    def CreateFlyoutTool(self):
        """
        CreateFlyoutTool -> Autodesk.AutoCAD.Windows.ToolPalette.Tool
            
            Package palette: 
            Input palette
            
            Package shapePackage: 
            Input shape package
            
            string toolNameOverride: 
            Input tool name override
        """
        pass
    
    
    def CreatePalette(self):
        """
        CreatePalette -> Palette
            
            Catalog catalogName: 
            Input catalog name
            
            string paletteName: 
            Input palette name
        """
        pass
    
    
    def CreateShapeCatalog(self):
        """
        CreateShapeCatalog -> Package
            
            string shapeName: 
            Input shape name
        """
        pass
    
    
    def CreateStockTool(self):
        """
        CreateStockTool -> Catalog
            
            string catalogName: 
            Input catalog name
        """
        pass
    
    
    def CreateTool(self):
        """
        CreateTool() -> Autodesk.AutoCAD.Windows.ToolPalette.Tool
        
        """
        pass
    
    
    def Customize(self):
        """
        Customize -> UInteger
            
            [In] int contextFlag: 
            Input context flags
            
            [In] uint menuHandle: 
            Input menu handlers
            
            [In] uint idCommandFirst: 
            Input first command's ID
            
            [In] uint idCommandLast: 
            Input last command's ID
            
            [In] ref Guid paletteId: 
            Input palette ID
        """
        pass
    
    
    def DoModal(self):
        """
        DoModal -> void
            
            [In, Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) propertyValue: 
            Input property value
            
            [In] ObjectIdCollection activeShapes: 
            Input active shapes
        """
        pass
    
    
    def DragLeave(self):
        """
        DragLeave -> void
        
        """
        pass
    
    
    def DragEnter(self):
        """
        DragEnter -> void
            
            [In, MarshalAs(UnmanagedType.Interface)] System.Windows.Forms.IDataObject data: 
            Input data
            
            [In] uint keyState: 
            Input key state
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL point: 
            Input point
            
            [In, Out] ref uint effect: 
            Input effect
        """
        pass
    
    
    def DragOver(self):
        """
        DragOver -> void
            
            [In] uint keyState: 
            Input key state
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input point
            
            [In, Out] ref uint effect: 
            Input effect
        """
        pass
    
    
    def Drop(self):
        """
        Drop -> void
            
            [In, MarshalAs(UnmanagedType.Interface)] System.Windows.Forms.IDataObject data: 
            Input data
            
            [In] uint keyState: 
            Input key state
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input point
            
            [In, Out] ref uint effect: 
            Input effect
        """
        pass
    
    
    def DropCallback(self):
        """
        DropCallback -> bool
            
            Entity entity: 
            Input entity
        """
        pass
    
    
    def Dropped(self):
        """
        Dropped -> void
            
            [In, MarshalAs(UnmanagedType.BStr)] string url: 
            Input URL
        """
        pass
    
    
    def Edit(self):
        """
        Edit([In, MarshalAs(UnmanagedType.IUnknown)] object, [In] IntPtr, [MarshalAs(UnmanagedType.VariantBool)] out bool) -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object property: 
            Input property
            
            [In] IntPtr parentWindow: 
            Input parent window
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Output success value
        Edit([In, MarshalAs(UnmanagedType.IUnknown)] object, [In] int, [MarshalAs(UnmanagedType.VariantBool)] out bool) -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object property: 
            Input property
            
            [In] int parentWindow: 
            Input parent window
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Output success value
        Edit([In, MarshalAs(UnmanagedType.IUnknown)] object, [In] long, [MarshalAs(UnmanagedType.VariantBool)] out bool) -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object property: 
            Input property
            
            [In] long parentWindow: 
            Input parent window
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Output success value
        """
        pass
    
    
    def Editable(self):
        """
        Editable -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            out int editable: 
            Input if the object is editable
        """
        pass
    
    
    def EndEdit(self):
        """
        EndEdit -> void
            
            bEditcanceled: 
            Input if the edit should be cancelled
        """
        pass
    
    
    def EndMultipleEdit(self):
        """
        EndMultipleEdit -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object tools: 
            Input tools
            
            [In, MarshalAs(UnmanagedType.Struct)] object stockToolIds: 
            Input stock tool IDs
            
            editcanceled: 
            Input if the edit should be cancelled
        """
        pass
    
    
    def Execute(self):
        """
        Execute -> void
            
            [In] int flag: 
            Input flag
            
            [In] uint window: 
            Input window
            
            [In] uint point: 
            Input points
            
            [In] uint keyState: 
            Input key states
        """
        pass
    
    
    def GetCommandString(self):
        """
        GetCommandString -> string
            
            [In] uint idCommand: 
            Input command ID
        """
        pass
    
    
    def GetContextMenu(self):
        """
        GetContextMenu -> UInteger
            
            [In] int contextFlag: 
            Input context flags
            
            [In] uint menu: 
            Input menus
            
            [In] uint idCommandFirst: 
            Input first command ID
            
            [In] uint idCommandLast: 
            Input last command ID
        """
        pass
    
    
    def GetCustomPropertyCtrl(self):
        """
        GetCustomPropertyCtrl -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
            
            [In] uint lcid: 
            Input LC ID
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) programId: 
            Input program ID
        """
        pass
    
    
    def GetData(self):
        """
        GetData -> void
            
            [In, Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) staticProperties: 
            Input static properties
            
            [In, Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) dynamicProperties: 
            Input dynamic properties
        """
        pass
    
    
    def GetDisplayName(self):
        """
        GetDisplayName -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) propertyName: 
            Input property name
        """
        pass
    
    
    def GetDisplayString(self):
        """
        GetDisplayString -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) value: 
            Input
        """
        pass
    
    
    def GetDragDropContextInfo(self):
        """
        GetDragDropContextInfo -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object pIUnknown: 
            Input unknown
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) toolName: 
            Input tool name
            
            out uint flag: 
            Input flag
        """
        pass
    
    
    def GetDropTarget(self):
        """
        GetDropTarget -> object
        
        """
        pass
    
    
    def GetMenuHelp(self):
        """
        GetMenuHelp -> string
            
            [In] uint idCmd: 
            Input command ID
        """
        pass
    
    
    def GetPredefinedStrings(self):
        """
        GetPredefinedStrings -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            out tagCALPOLESTR value: 
            Input value
            
            out tagCADWORD cookie: 
            Input cookie
        """
        pass
    
    
    def GetPredefinedValue(self):
        """
        GetPredefinedValue -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            [In] uint cookie: 
            Input cookie
            
            [Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) value: 
            Input value
        """
        pass
    
    
    def GetPropertyIcon(self):
        """
        GetPropertyIcon -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
            
            [Out, MarshalAs(UnmanagedType.IUnknown)] ref object modopt(IsExplicitlyDereferenced) icon: 
            Input icon
        """
        pass
    
    
    def GetPropertyWeight(self):
        """
        GetPropertyWeight -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
            
            out int pPropertyWeight: 
            Input property weight
        """
        pass
    
    
    def GetPropTextColor(self):
        """
        GetPropTextColor -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
            
            [ComAliasName("stdole::OLE_COLOR")] out uint textColor: 
            Input text color
        """
        pass
    
    
    def GetStockTool(self):
        """
        GetStockTool -> object
        
        """
        pass
    
    
    def GetToolProperties(self):
        """
        GetToolProperties -> object
        
        """
        pass
    
    
    def GetUnspecifiedString(self):
        """
        GetUnspecifiedString -> string
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
        """
        pass
    
    
    def InvokeCommand(self):
        """
        InvokeCommand -> void
            
            [In] uint idCommand: 
            Input command ID
            
            [In] uint window: 
            Input window
        """
        pass
    
    
    def InvokeMenuCommand(self):
        """
        InvokeMenuCommand -> UInteger
            
            [In] uint idCmd: 
            Input command ID
            
            [In] ref Guid paletteId: 
            Input palette ID
            
            [In] uint windowHandle: 
            Input window handle
        """
        pass
    
    
    def IsFullView(self):
        """
        IsFullView -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool visible: 
            Input visibility
            
            out uint integralHeight: 
            Input height
        """
        pass
    
    
    def Load(self):
        """
        Load -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object xmlElement: 
            Input element to load
        """
        pass
    
    
    def MapPropertyToPage(self):
        """
        MapPropertyToPage -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            out Guid clsid: 
            Input CLS ID
        """
        pass
    
    
    def MultipleEdit(self):
        """
        MultipleEdit -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object tools: 
            Input tools
            
            [In, MarshalAs(UnmanagedType.Struct)] object stockToolIds: 
            Input stock tool IDs
            
            [In] int parentWindow: 
            Input parent window
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Output success of function
        """
        pass
    
    
    def New(self):
        """
        New -> void
        
        """
        pass
    
    
    def Refreshed(self):
        """
        Refreshed -> void
            
            [In, MarshalAs(UnmanagedType.BStr)] string url: 
            Input URL
        """
        pass
    
    
    def Save(self):
        """
        Save -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object xmlElement: 
            Input element to save
        """
        pass
    
    
    def SetEditorWindow(self):
        """
        SetEditorWindow([In] IntPtr, [In, MarshalAs(UnmanagedType.IUnknown)] object) -> void
            
            [In] IntPtr editorWindow: 
            Input editor window
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyInspector: 
            Input property inspector
        SetEditorWindow([In] int, [In, MarshalAs(UnmanagedType.IUnknown)] object) -> void
            
            [In] int editorWindow: 
            Input editor window
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyInspector: 
            Input property inspector
        """
        pass
    
    
    def SetFlyoutTools(self):
        """
        SetFlyoutTools -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object flyoutToolIds: 
            Input flyout tool IDs
        """
        pass
    
    
    def SetToolProperties(self):
        """
        SetToolProperties -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object toolProperties: 
            Input tool properties
        """
        pass
    
    
    def SetUnspecified(self):
        """
        SetUnspecified -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input ID
            
            [In, MarshalAs(UnmanagedType.VariantBool)] bool isUnspecified: 
            Input if it is unspecified or not
        """
        pass
    
    
    def ShowProperty(self):
        """
        ShowProperty -> void
            
            [In] int dispatchId: 
            Input diaptch ID
            
            out int show: 
            Output if it is being shown
        """
        pass
    
    
    def ValidateEditChanges(self):
        """
        ValidateEditChanges -> void
        
        """
        pass
    
    
    CurrentShapeId = None
    
    
    EditMode = None
    
    
    FlayoutPackageID = None
    
    
    ToolGuid = None
    
    
    ToolImage = None
    
    
    ToolName = None
    
    pass

class DownloadFlags():
    All = 0x1f
    Children = 0x10
    Image = 4
    Item = 1
    LinkedItem = 2
    ShowProgress = 0x40
    StockTool = 8

class DrawImageOption():
    Halo = 4
    Normal = 1
    Selected = 2
    Shadow = 8

class ExecutionContext():
    LeftButtonClicked = None
    DroppedInDrawing = None

class FlyoutEntryAttribute(object):
    """
    
    FlyoutEntryAttribute
        int modopt(IsLong) dispatchId : Input dispatch ID
    """
    DispId = None
    
    pass

def GetChildCountFor(self):
    """
    GetChildCountFor -> Integer
        
        CatalogItemType type: 
        Input item type to count.
    """
    pass

def GetNextChild(self):
    """
    GetNextChild -> CatalogItem
        
        int index: 
        Input array index at which to begin the search, or -1 to find the first item that matches the specified type
        
        CatalogItemType type: 
        Input item type to get.
    """
    pass

class IAcPiCategorizeProperties(object):
    """
    
    """
    def GetCategoryDescription(self):
        """
        GetCategoryDescription -> void
            
            [In] int categoryId: 
            Input Category ID of the category for which the description string is queried.
            
            [In] uint lcid: 
            Input Local language identifier.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) categoryDescription: 
            Input containing the category description.
        """
        pass
    
    
    def GetCategoryName(self):
        """
        GetCategoryName -> void
            
            [In] int categoryId: 
            Input Category ID of the category for which the name string is queried.
            
            [In] uint lcid: 
            Input Local language identifier.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) categoryName: 
            Input containing the category name.
        """
        pass
    
    
    def GetCategoryWeight(self):
        """
        GetCategoryWeight -> void
            
            [In] int categoryId: 
            Input Category ID of the category whose weight is being queried.
            
            out int categoryWeight: 
            Input category weight.
        """
        pass
    
    
    def GetCommandButtons(self):
        """
        GetCommandButtons -> void
            
            [In] int categoryId: 
            Input Category ID whose "What's this Help" is being queried.
            
            [Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) commandButtons: 
            Input that implement the ICommandButton interface.
        """
        pass
    
    
    def GetParentCategory(self):
        """
        GetParentCategory -> void
            
            [In] int categoryId: 
            Input Category ID of the category whose parent is being queried
            
            out int parentCategoryId: 
            Input. Category ID of the parent category of the category specified by categoryID; if zero, categoryID represents a root category.
        """
        pass
    
    
    def GetUniqueID(self):
        """
        GetUniqueID -> void
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) value: 
            Input unique ID to associate with the category
        """
        pass
    
    
    def MapPropertyToCategory(self):
        """
        MapPropertyToCategory -> void
            
            [In] int dispatchId: 
            Input dispatch id of the property.
            
            out int categoryId: 
            Input category ID that categorizes the property identified by the dispatchID parameter.
        """
        pass
    
    pass

class IAcPiPropertyDisplay(object):
    """
    
    """
    def GetCustomPropertyCtrl(self):
        """
        GetCustomPropertyCtrl -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            For static properties, the DISPID of the method/property for which an object/command wishes to supply custom ActiveX control for display/edit ; for dynamic properties, the object/command to get the programId of the custom ActiveX control.
            
            [In] uint lcid: 
            Local language identifier.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) programId: 
            Input containing the program id of supplied custom ActiveX control.
        """
        pass
    
    
    def GetPropertyIcon(self):
        """
        GetPropertyIcon -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Input. Static properties: DISPID; Dynamic properties: the object.
            
            [Out, MarshalAs(UnmanagedType.IUnknown)] ref object modopt(IsExplicitlyDereferenced) icon: 
            Input from which the IPicture interface will be queried for the left property icon display.
        """
        pass
    
    
    def GetPropertyWeight(self):
        """
        GetPropertyWeight -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Static properties: DISPID; Dynamic properties: the object.
            
            out int propertyWeight: 
            Property weight.
        """
        pass
    
    
    def GetPropTextColor(self):
        """
        GetPropTextColor -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Static properties: DISPID; Dynamic properties: the object.
            
            [ComAliasName("stdole::OLE_COLOR")] out uint textColor: 
            OLE_COLOR value used for property label text display in the Property Inspector.
        """
        pass
    
    
    def IsFullView(self):
        """
        IsFullView -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object id: 
            Static properties: DISPID; Dynamic properties: the object.
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool visible: 
            True if the property label is hidden from display and the property display/edit control is displayed in the entire property row space in the Property Inspector control's display.
            
            out uint integralHeight: 
            Integral height, in number of rows, in which the edit control is displayed by the Property Inspector
        """
        pass
    
    pass

class IAcPiPropertyUnspecified(object):
    """
    
    """
    def GetUnspecifiedString(self):
        """
        GetUnspecifiedString -> string
            
            [In, MarshalAs(UnmanagedType.Struct)] object varId: 
            Static properties: DISPID; Dynamic properties: the object.
        """
        pass
    
    
    def SetUnspecified(self):
        """
        SetUnspecified -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object varId: 
            Static properties: DISPID; Dynamic properties: the object.
            
            [In, MarshalAs(UnmanagedType.VariantBool)] bool isUnspecified: 
            Input if unspecified
        """
        pass
    
    pass

class IAcadStockTool(object):
    """
    
    """
    def CreateTool(self):
        """
        CreateTool -> object
        
        """
        pass
    
    pass

class IAcadTool(object):
    """
    
    """
    def BeginEdit(self):
        """
        BeginEdit -> void
        
        """
        pass
    
    
    def Dropped(self):
        """
        Dropped -> void
            
            [In, MarshalAs(UnmanagedType.BStr)] string url: 
            Input URL
        """
        pass
    
    
    def Edit(self):
        """
        Edit([In, MarshalAs(UnmanagedType.IUnknown)] object, [In] long, [MarshalAs(UnmanagedType.VariantBool)] out bool) -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyToEdit: 
            Input from which IAcadToolProperties can be obtained
            
            [In] long parentWindow: 
            Input handle of the application window that can be used as the parent of the editor dialog.
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Input indicating editing success or failure.
        Edit([In, MarshalAs(UnmanagedType.IUnknown)] object, [In] IntPtr, [MarshalAs(UnmanagedType.VariantBool)] out bool) -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyToEdit: 
            Input from which IAcadToolProperties can be obtained.
            
            [In] IntPtr parentWindow: 
            Input handle of the application window that can be used as the parent of the editor dialog
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Input indicating editing success or failure.
        """
        pass
    
    
    def EndEdit(self):
        """
        EndEdit -> void
            
            editcanceled: 
            Input indicating whether edits should be saved.
        """
        pass
    
    
    def EndMultipleEdit(self):
        """
        EndMultipleEdit -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object tools: 
            Input tools
            
            [In, MarshalAs(UnmanagedType.Struct)] object stockToolIds: 
            Input stock tool IDs
            
            editcanceled: 
            Input if the edit should be cancelled
        """
        pass
    
    
    def Execute(self):
        """
        Execute -> void
            
            [In] int flag: 
            Input ExecutionContext enum flag that provides context information.
            
            [In] uint window: 
            Input window handle.
            
            [In] uint point: 
            Input point where the tool was dropped.
            
            [In] uint keyState: 
            Input containing the state of the modifier keys.
        """
        pass
    
    
    def GetCommandString(self):
        """
        GetCommandString -> string
            
            [In] uint idCommand: 
            Input ID of the command for which help text is required.
        """
        pass
    
    
    def GetContextMenu(self):
        """
        GetContextMenu -> UInteger
            
            [In] int contextFlag: 
            Input ContextMenuMode enum flag specifying the context in which the context menu is invoked.
            
            [In] uint menu: 
            Input handle of the context menu
            
            [In] uint idCommandFirst: 
            Input minimum value that the tool can specify for a menu item identifier
            
            [In] uint idCommandLast: 
            Input maximum value that the handler can specify for a menu item identifier
        """
        pass
    
    
    def GetData(self):
        """
        GetData -> void
            
            [In, Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) properties: 
            Input properties
            
            [In, Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) dynamicsProperties: 
            Input dynamics properties
        """
        pass
    
    
    def GetDragDropContextInfo(self):
        """
        GetDragDropContextInfo -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object data: 
            Input being dragged.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) toolName: 
            Input text to display in the drop context menu.
            
            out uint flag: 
            Input flag value (currently not used).
        """
        pass
    
    
    def GetDropTarget(self):
        """
        GetDropTarget -> object
        
        """
        pass
    
    
    def GetStockTool(self):
        """
        GetStockTool -> object
        
        """
        pass
    
    
    def GetToolProperties(self):
        """
        GetToolProperties -> object
        
        """
        pass
    
    
    def InvokeCommand(self):
        """
        InvokeCommand -> void
            
            [In] uint idCommand: 
            Input ID of one of the context menu commands.
            
            [In] uint window: 
            Input window handle to be used in any message box displayed by the tool.
        """
        pass
    
    
    def Load(self):
        """
        Load -> void
        
        """
        pass
    
    
    def MultipleEdit(self):
        """
        MultipleEdit -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object tools: 
            Input tools
            
            [In, MarshalAs(UnmanagedType.Struct)] object stockToolIds: 
            Input stock tool IDs
            
            [In] int parentWindow: 
            Input parent window
            
            [MarshalAs(UnmanagedType.VariantBool)] out bool success: 
            Output success of function
        """
        pass
    
    
    def New(self):
        """
        New -> void
        
        """
        pass
    
    
    def Refreshed(self):
        """
        Refreshed -> void
            
            [In, MarshalAs(UnmanagedType.BStr)] string url: 
            Input URL from which the tool was refreshed.
        """
        pass
    
    
    def Save(self):
        """
        Save -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object xmlElement: 
            Input of the XML DOM node.
        """
        pass
    
    
    def SetEditorWindow(self):
        """
        SetEditorWindow([In] IntPtr, [In, MarshalAs(UnmanagedType.IUnknown)] object) -> void
            
            [In] IntPtr editorWindow: 
            Input handle of the tool properties editor window.
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyInspector: 
            Input IAcPiPropertyInspector instance in which the tool's properties are edited.
        SetEditorWindow([In] int, [In, MarshalAs(UnmanagedType.IUnknown)] object) -> void
            
            [In] int editorWindow: 
            Input handle of the tool properties editor window.
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyInspector: 
            Input IAcPiPropertyInspector instance in which the tool's properties are edited.
        SetEditorWindow([In] long, [In, MarshalAs(UnmanagedType.IUnknown)] object) -> void
            
            [In] long editorWindow: 
            Input handle of the tool properties editor window.
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object propertyInspector: 
            Input IAcPiPropertyInspector instance in which the tool's properties are edited.
        """
        pass
    
    
    def SetToolProperties(self):
        """
        SetToolProperties -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object toolProperties: 
            Input IAcadToolProperties object for the tool.
        """
        pass
    
    
    def ValidateEditChanges(self):
        """
        ValidateEditChanges -> void
        
        """
        pass
    
    
    EditMode = None
    
    pass

class IAcadToolContextMenu(object):
    """
    
    """
    def Customize(self):
        """
        Customize -> UInteger
            
            [In] int contextFlag: 
            Input ContextMenuFlag enum specifying the context in which the context menu is invoked
            
            [In] uint menuHandle: 
            Input context menu handle
            
            [In] uint idCommandFirst: 
            Input minimum value that the tool can specify for a menu item identifier.
            
            [In] uint idCommandLast: 
            Input maximum value that the handler can specify for a menu item identifier.
            
            [In] ref Guid paletteId: 
            Input if the context is ContextMenuPaletteSetTab, this contains the ID of the palette that corresponds to the tab (active or inactive); for all other contexts, this contains the ID of the active palette.
        """
        pass
    
    
    def GetMenuHelp(self):
        """
        GetMenuHelp -> string
            
            [In] uint idCmd: 
            Input ID of the command for which help text is required.
        """
        pass
    
    
    def InvokeMenuCommand(self):
        """
        InvokeMenuCommand -> UInteger
            
            [In] uint idCmd: 
            Input command identifier.
            
            [In] ref Guid paletteId: 
            Input ID of the palette.
            
            [In] uint windowHandle: 
            Input window handle.
        """
        pass
    
    pass

class IAcadToolDragSource(object):
    """
    
    """
    def BeginDrag(self):
        """
        BeginDrag -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) toolIds: 
            Input IDs of the tools being dragged
            
            [In, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) allStockToolIds: 
            Input IDs of all the stock tools to which the tools being dragged belong.
            
            [In] ref Guid currentStockToolId: 
            Input of this stock tool.
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input System.Windows.Forms.IDataObject object in which the tool can set its data.
            
            [In] uint keyState: 
            Input value indicating the state of the modifier keys.
        """
        pass
    
    
    def DragEnterDrawing(self):
        """
        DragEnterDrawing -> UInteger
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input in which the tool can set its data.
            
            [In] uint keyState: 
            Input indicating the state of the modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL point: 
            Input Autodesk.AutoCAD.Windows.ToolPalette.POINTL object expressing the current cursor coordinates in screen coordinates.
        """
        pass
    
    
    def DragOverDrawing(self):
        """
        DragOverDrawing -> UInteger
            
            [In] uint keyState: 
            Input containing the state of the modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL point: 
            Input Autodesk.AutoCAD.Windows.ToolPalette.POINTL object expressing the current cursor coordinates in screen coordinates.
        """
        pass
    
    
    def DropInDrawing(self):
        """
        DropInDrawing -> UInteger
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input in which the tool can set its data.
            
            [In] uint keyState: 
            Input containing the state of the modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input Autodesk.AutoCAD.Windows.ToolPalette.POINTL object expressing the current cursor coordinates in screen coordinates.
        """
        pass
    
    
    def DragInProgress(self):
        """
        DragInProgress -> void
            
            [In] uint dropEffect: 
            Input value returned by the most recent call to the drop target.
        """
        pass
    
    
    def DragLeaveDrawing(self):
        """
        DragLeaveDrawing -> void
        
        """
        pass
    
    
    def EndDrag(self):
        """
        EndDrag -> void
            
            [In] uint dropEffect: 
            Input value returned by the most recent call to the drop target.
        """
        pass
    
    pass

class IAcadToolDropTarget(object):
    """
    
    """
    def DragEnter(self):
        """
        DragEnter -> void
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input IDataObject object in which the tool can set its data.
            
            [In] uint keyState: 
            Input current state of the keyboard modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input POINTL object expressing the current cursor location in screen coordinates.
            
            [In, Out] ref uint effect: 
            Input current effect flag.
        """
        pass
    
    
    def DragOver(self):
        """
        DragOver -> void
            
            [In] uint keyState: 
            Input current state of the keyboard modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input Autodesk.AutoCAD.Windows.ToolPalette.POINTL expressing the current cursor location in screen coordinates.
            
            [In, Out] ref uint effect: 
            Input current effect flag.
        """
        pass
    
    
    def Drop(self):
        """
        Drop -> object
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input System.Windows.Forms.IDataObject object in which the tool can set its data.
            
            [In] uint keyState: 
            Input current state of the keyboard modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input Autodesk.AutoCAD.Windows.ToolPalette.POINTL object expressing the current cursor position in screen coordinates.
            
            [In, Out] ref uint effect: 
            Input current effect flag.
            
            [In] ref Guid currentStockToolId: 
            Input of this stock tool.
            
            [In] ref Guid parentId: 
            Input of the parent catalog item to which the new tools should be added.
        """
        pass
    
    
    def DragLeave(self):
        """
        DragLeave -> void
        
        """
        pass
    
    
    def GetDragDropContextMenuItem(self):
        """
        GetDragDropContextMenuItem -> void
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object data: 
            Input object being dragged.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) menuItemText: 
            Input containing text to display in the drop context menu.
            
            out uint flag: 
            Input flags.(currently not used)
        """
        pass
    
    pass

class IAcadToolFlyoutShape(object):
    """
    
    """
    def SetFlyoutTools(self):
        """
        SetFlyoutTools -> void
            
            [In, MarshalAs(UnmanagedType.Struct)] object flyoutToolIds: 
            Input IDs of flyout tools.
        """
        pass
    
    pass

class IAcadToolProperties(object):
    """
    
    """
    def GetAcTcTool(self):
        """
        GetAcTcTool -> UInteger
        
        """
        pass
    
    
    def GetCurrentShape(self):
        """
        GetCurrentShape -> void
            
            [Out, MarshalAs(UnmanagedType.IUnknown)] ref object modopt(IsExplicitlyDereferenced) ppTool: 
            Output shape object
        """
        pass
    
    
    def GetCustomData(self):
        """
        GetCustomData -> object
        
        """
        pass
    
    
    def GetImage(self):
        """
        GetImage -> void
            
            [In] int width: 
            Input width of the image. Only width is used, and height is ignored
            
            [In] int height: 
            Input height of the image. This parameter is ignored
            
            [Out, MarshalAs(UnmanagedType.IUnknown)] ref object modopt(IsExplicitlyDereferenced) value: 
            Input address of the output variable that receives the IAcadToolImage interface.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) resourceName: 
            Input resource identifier if the image was loaded from a resource.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) sourceFile: 
            Input file name if the image was loaded from a disk file.
        """
        pass
    
    
    def GetOverlayImage(self):
        """
        GetOverlayImage -> void
            
            [Out, MarshalAs(UnmanagedType.IUnknown)] ref object modopt(IsExplicitlyDereferenced) value: 
            Input address of the output variable that receives the IAcadToolImage interface.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) resourceName: 
            Input resource identifier if the image was loaded from a resource.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) sourceFile: 
            Input file name if the image was loaded from a disk file.
        """
        pass
    
    
    def SetImage(self):
        """
        SetImage -> void
            
            [In] int width: 
            Input image width.
            
            [In] int height: 
            Input image height.
            
            [In, MarshalAs(UnmanagedType.IUnknown)] object newVal: 
            Input address of the output variable that receives the IAcadToolImage interface.
            
            [In, MarshalAs(UnmanagedType.BStr)] string resourceName: 
            Input resource identifier if the image was loaded from a resource.
            
            [In, MarshalAs(UnmanagedType.BStr)] string sourceFile: 
            Input file name if the image was loaded from a disk file.
        """
        pass
    
    
    def SetOverlayImage(self):
        """
        SetOverlayImage -> void
        
        """
        pass
    
    
    ActiveShapeIds = None
    
    
    CurrentShapeId = None
    
    
    Description = None
    
    
    HelpCommand = None
    
    
    HelpData = None
    
    
    HelpFile = None
    
    
    ID = None
    
    
    IsFlyoutEnabled = None
    
    
    IsReadOnly = None
    
    
    Name = None
    
    
    ShapePackageId = None
    
    
    ToolTipText = None
    
    
    ToolType = None
    
    pass

class IDropTarget(object):
    """
    
    """
    def DragEnter(self):
        """
        DragEnter -> void
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input object that contains the drag data.
            
            [In] uint keyState: 
            Input indicating the state of the modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input object expressing the current cursor coordinates in screen coordinates.
            
            [In, Out] ref uint effect: 
            Input current effect flag.
        """
        pass
    
    
    def DragOver(self):
        """
        DragOver -> void
            
            [In] uint keyState: 
            Input current state of the keyboard modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input object expressing the current cursor location in screen coordinates.
            
            [In, Out] ref uint effect: 
            Input current effect flag.
        """
        pass
    
    
    def Drop(self):
        """
        Drop -> void
            
            [In, MarshalAs(UnmanagedType.Interface)] IDataObject data: 
            Input object in which the tool can set its data.
            
            [In] uint keyState: 
            Input current state of the keyboard modifier keys.
            
            [In] Autodesk.AutoCAD.Windows.ToolPalette.POINTL pt: 
            Input object expressing the current cursor position in screen coordinates.
            
            [In, Out] ref uint effect: 
            Input current effect flag.
        """
        pass
    
    
    def DragLeave(self):
        """
        DragLeave -> void
        
        """
        pass
    
    pass

class IOPMPropertyDialog(object):
    """
    
    """
    def DoModal(self):
        """
        DoModal -> void
            
            [In, Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) propertyValue: 
            Input represented as a string; can be empty but never null.
            
            [In] ObjectIdCollection activeShapes: 
            Input object whose values are represented by propertyValue; can be empty but never null.
        """
        pass
    
    pass

class IOPMPropertyExtension(object):
    """
    
    """
    def Editable(self):
        """
        Editable -> void
            
            [In] int dispatchId: 
            Input dispatch identifier of the property whose editable flag is being overridden.
            
            out int value: 
            Input value
        """
        pass
    
    
    def GetDisplayName(self):
        """
        GetDisplayName -> void
            
            [In] int dispatchId: 
            Input dispatch identifier of the property whose display name is requested.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) propertyName: 
            Input containing the display name for the property identified with DISPID.
        """
        pass
    
    
    def ShowProperty(self):
        """
        ShowProperty -> void
            
            [In] int dispatchId: 
            Input dispatch identifier of the property whose showable flag is being overridden.
            
            out int show: 
            Input containing the showable flag.
        """
        pass
    
    pass

class IPerPropertyBrowsing(object):
    """
    
    """
    def GetDisplayString(self):
        """
        GetDisplayString -> void
            
            [In] int dispatchId: 
            Input dispatch id.
            
            [Out, MarshalAs(UnmanagedType.BStr)] ref string modopt(IsExplicitlyDereferenced) value: 
            Input value
        """
        pass
    
    
    def GetPredefinedStrings(self):
        """
        GetPredefinedStrings -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            out tagCALPOLESTR value: 
            Input value
            
            out tagCADWORD cookie: 
            Input cookie
        """
        pass
    
    
    def GetPredefinedValue(self):
        """
        GetPredefinedValue -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            [In] uint cookie: 
            Input cookie
            
            [Out, MarshalAs(UnmanagedType.Struct)] ref object modopt(IsExplicitlyDereferenced) value: 
            Input value
        """
        pass
    
    
    def MapPropertyToPage(self):
        """
        MapPropertyToPage -> void
            
            [In] int dispatchId: 
            Input dispatch ID
            
            out Guid clsid: 
            Input class ID
        """
        pass
    
    pass

class Image(object):
    """
    
    Image()()
    
    
    """
    def ConvertTo(self):
        """
        ConvertTo -> void
        
        """
        pass
    
    
    def Save(string,(self):
        """
        Save(string, -> void
        
        """
        pass
    
    
    def Draw(self):
        """
        Draw -> void
            
            Graphics graphics: 
            Input the graphic to draw
            
            Rectangle rectangle: 
            Input the rectangle size
            
            DrawImageOption drawOption: 
            Input draw image options
            
            [MarshalAs(UnmanagedType.U1)] bool transparent: 
            Input true if the image ought to be transparent
        """
        pass
    
    
    def GetBitmap(self):
        """
        GetBitmap -> Bitmap
            
            System.Drawing.Color backgroundColor: 
            Input background color for the bitmap.
        """
        pass
    
    
    def Load(self):
        """
        Load(System.Runtime.InteropServices.ComTypes.IStream) -> void
            
            System.Runtime.InteropServices.ComTypes.IStream stream: 
            Input the stream that contains the image data.
        Load(IntPtr) -> void
            
            IntPtr bitmap: 
            Input handle to a Windows GDI bitmap.
        Load(string) -> void
            
            string filename: 
            Input image file to load with the path.
        """
        pass
    
    
    def Save(self):
        """
        Save(System.Runtime.InteropServices.ComTypes.IStream) -> void
            
            System.Runtime.InteropServices.ComTypes.IStream stream: 
            Input the stream into which the image must be written.
        Save(string) -> void
            
            string filename: 
            Input image file to save with path.
        Autodesk.AutoCAD.Windows.ToolPalette.Image.Save@string@Autodesk.AutoCAD.Windows.ToolPalette.ImageType -> 
            
            filename: 
            Input file name with path to save the image.
            
            saveAsType: 
            Input image format; one of ImageType enum values.
        """
        pass
    
    
    Icon = None
    
    
    IsLoaded = None
    
    
    SaveType = None
    
    
    Size = None
    
    
    Type = None
    
    pass

class ImageInfo(object):
    """
    
    ImageInfo()()
    
    
    """
    ResourceFile = None
    
    
    ResourceName = None
    
    
    Size = None
    
    pass

class ImageList(object):
    """
    
    """
    def Add(self):
        """
        Autodesk.AutoCAD.Windows.ToolPalette.ImageList.Add@Autodesk.AutoCAD.Windows.ToolPalette.Image -> 
            
            image: 
            Input object that needs to be added.
        Add(Autodesk.AutoCAD.Windows.ToolPalette.ImageInfo) -> Integer
            
            Autodesk.AutoCAD.Windows.ToolPalette.ImageInfo info: 
            Input object containing the information that needs to be added to the list.
        Add(Autodesk.AutoCAD.Windows.ToolPalette.Image, [MarshalAs(UnmanagedType.U1)] bool) -> Integer
        
        """
        pass
    
    
    def Delete(self):
        """
        Delete -> void
            
            int index: 
            Input zero-based index of the image; the index should be in the range of zero to one less than the number of images
        """
        pass
    
    
    def DeleteAllImages(self):
        """
        DeleteAllImages -> void
        
        """
        pass
    
    
    def GetImage(self):
        """
        GetImage -> Autodesk.AutoCAD.Windows.ToolPalette.Image
            
            int index: 
            Input zero-based index of the image; the index should be in the range of zero to one less than the number of images.
        """
        pass
    
    
    def GetImageIndex(self):
        """
        GetImageIndex -> Integer
            
            Size size: 
            Input size of the image; only width is used and height is ignored
            
            [MarshalAs(UnmanagedType.U1)] bool exactMatch: 
            Input exact match Boolean
        """
        pass
    
    
    def GetImageInfo(self):
        """
        GetImageInfo -> Autodesk.AutoCAD.Windows.ToolPalette.ImageInfo
            
            int index: 
            Input zero-based index of the image; the index should be in the range of zero to one less than the number of images
        """
        pass
    
    
    def LoadImageW(self):
        """
        LoadImageW -> void
        
        """
        pass
    
    
    def UpdateImage(self):
        """
        UpdateImage -> Integer
            
            Autodesk.AutoCAD.Windows.ToolPalette.Image image: 
            Input object that needs to replace the image of the same size.
        """
        pass
    
    
    def SetImage(self):
        """
        SetImage -> void
            
            int index: 
            Input zero-based index of the image; the index should be in the range of zero to one less than the number of images.
            
            Autodesk.AutoCAD.Windows.ToolPalette.Image image: 
            Input object that needs to be set at the specified index.
        """
        pass
    
    
    def SetImageInfo(self):
        """
        SetImageInfo -> void
            
            int index: 
            Input zero-based index of the image; the index should be in the range of zero to one less than the number of images.
            
            Autodesk.AutoCAD.Windows.ToolPalette.ImageInfo info: 
            Input new info
        """
        pass
    
    
    Count = None
    
    
    ImageOptions = None
    
    pass

class ImageOptionFlags():
    RenderBitmapOpaque = None
    UserOverride = None

class ImageType():
    Bitmap = 1
    EnhancedMetaFile = 4
    Gif = 7
    Icon = 3
    Jpeg = 5
    MetaFile = 2
    Png = 6
    Tiff = 8
    Uninitialized = -1

class ItemOptionFlags():
    MenuRemoveImage = 0x10
    MenuSetImage = 8
    MenuUpdateImage = 4
    None = 0
    SupportsAutoImage = 1
    SupportsUserImage = 2

class LoadFlags():
    LoadImages = 2
    LoadLinks = 1

class POINTL(object):
    """
    
    """

    pass

class Package(object):
    """
    
    Package()()
    
    
    """

    pass

class Palette(object):
    """
    
    Palette()
    """

    pass

class PerPropertyBrowsingEntryAttribute(object):
    """
    
    PerPropertyBrowsingEntryAttribute
        int modopt(IsLong) dispatchId : Input dispatch ID
        string programId : Input program ID
        string leftIconResource : Input left icon resource
        int leftIconType : Input left icon type
        string ellipsisBmpResource : Input ellipsis BMP resource
        int ellipsisBmpType : Input ellipsis BMP type
        int modopt(IsLong) textColor : Input color of text
        [MarshalAs(UnmanagedType.U1)] bool fullView : Input if in full view or not
        int modopt(IsLong) integralHeight : Input integral height
        int modopt(IsLong) weight : Input weight
    """
    EllipsisBmpResource = None
    
    
    EllipsisBmpType = None
    
    
    IsFullView = None
    
    
    LefIconResource = None
    
    
    LeftIconType = None
    
    
    ProgId = None
    
    pass

class RefreshFlags():
    RefreshAll = 0x1f
    RefreshChildren = 0x10
    RefreshImage = 4
    RefreshItem = 1
    RefreshLinkedItem = 2
    RefreshShowProgress = 0x40
    RefreshStockTool = 8

class ReturnStatus():
    ContextMenuShow = None
    ContextMenuHide = None
    ExecutionCanceled = None
    ExecutionCancelRejected = None
    ContextMenuUpdatePalette = None

class SaveFlags():
    SaveAnsi = 0x20
    SaveAs = 8
    SaveImages = 4
    SaveLinksAsEmbedded = 2
    SaveLinksAsLinks = 1
    SaveOverlayImages = 0x10

class Scheme(object):
    """
    
    Scheme
        string name : Input name of the scheme.
    """
    def Find(self):
        """
        Find -> CatalogItem
            
            Guid guid: 
            Input of the catalog item to find.
            
            CatalogTypeFlags flags: 
            Input type of catalog to search, which can be one or more of the CatalogType enum values (multiple values can be combined with bitwise OR)
        """
        pass
    
    
    def GetCatalogSet(self):
        """
        GetCatalogSet -> CatalogSet
            
            CatalogTypeFlags flags: 
            Input type of catalog set to get, which can be one of the following CatalogType enum values: Catalog or StockToolCatalog
        """
        pass
    
    
    def LoadCatalogs(self):
        """
        LoadCatalogs() -> void
        
        LoadCatalogs(CatalogTypeFlags, LoadFlags) -> void
            
            CatalogTypeFlags flags: 
            Input catalog type to load, which can be one or more of the CatalogType enum values (multiple values can be combined with bitwise OR).
            
            LoadFlags loadFlags: 
            Input load option, which can be one or more of the LoadOption enum values (multiple values can be combined with bitwise OR)
        """
        pass
    
    
    def SaveCatalogs(self):
        """
        SaveCatalogs() -> void
        
        SaveCatalogs(CatalogTypeFlags, SaveFlags) -> void
            
            CatalogTypeFlags flags: 
            Input catalog type to load, which can be one or more of the CatalogType enum values (multiple values can be combined with bitwise OR).
            
            SaveFlags saveFlags: 
            Input save option, which can be one or more of the SaveFlags enum values (multiple values can be combined with bitwise OR)
        """
        pass
    
    
    def UnloadCatalogs(self):
        """
        UnloadCatalogs() -> void
        
        UnloadCatalogs(CatalogTypeFlags) -> void
            
            CatalogTypeFlags flags: 
            Input catalog type to load, which can be one or more of the CatalogType enum values (multiple values can be combined with bitwise OR).
        """
        pass
    
    
    Name = None
    
    pass

class SchemeCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Scheme
            
            string name: 
            Input name of the scheme collection.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Scheme[] array: 
            Input array to copy to
            
            int index: 
            Input index to begin copying from
        """
        pass
    
    
    def Find(self):
        """
        Find -> Scheme
            
            string name: 
            Input name of the scheme collection to find.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove(Scheme) -> void
            
            Scheme scheme: 
            Input the scheme to be removed.
        Remove(string) -> void
            
            string name: 
            Input name of the scheme collection to be removed.
        """
        pass
    
    
    Count = None
    
    pass

class StockTool(object):
    """
    
    StockTool()
    """
    def CreateAcadStockTool(self):
        """
        CreateAcadStockTool -> object
        
        """
        pass
    
    
    def CreateAcadTool(self):
        """
        CreateAcadTool -> object
        
        """
        pass
    
    
    def CreateTool(self):
        """
        CreateTool() -> Tool
        
        CreateTool([MarshalAs(UnmanagedType.U1)] bool) -> Tool
            
            [MarshalAs(UnmanagedType.U1)] bool setDefaults: 
            If TRUE, sets the default properties of the tool by copying the stock tool's properties; if FALSE, does not set the tool properties.
        """
        pass
    
    
    ComClassID = None
    
    
    ModuleFileName = None
    
    
    ModuleInstallArguments = None
    
    
    ModuleInstallUrl = None
    
    pass

class TargetProductInfo(object):
    """
    
    TargetProductInfo()()
    
    
    TargetProductInfo(string, string, Version, Version)
        string productName : Input product name
        string localeId : Input localized ID
        Version minimumVersion : Input minimum version number
        Version maximumVersion : Input maximum version number
    
    
    """
    LocaleId = None
    
    
    MaximumVersion = None
    
    
    MinimumVersion = None
    
    
    ProductName = None
    
    pass

class Tool(object):
    """
    
    Tool()()
    
    
    """
    def CreateAcadTool(self):
        """
        CreateAcadTool -> object
            
            [MarshalAs(UnmanagedType.U1)] bool loadData: 
            Input, if true, loads the tool's custom data.
        """
        pass
    
    
    def EnableFlyout(self):
        """
        EnableFlyout -> void
            
            [MarshalAs(UnmanagedType.U1)] bool useFlyout: 
            Input indicating whether to use a flyout
        """
        pass
    
    
    def Execute(self):
        """
        Execute -> void
            
            int flag: 
            Input execution context flag.
            
            IWin32Window window: 
            Input window handle in which the tool was dropped, if the tool was executed by dragging and dropping into the drawing window
            
            Point point: 
            Input point at which the tool was dropped, if the tool was executed by dragging and dropping into the drawing window; the point is in the client coordinates of the window specified in window.
            
            int keyState: 
            Input state of the modifier keys if the tool was executed by dragging and dropping into the drawing window
        """
        pass
    
    
    def GetActiveShapes(self):
        """
        GetActiveShapes -> Tool()
        
        """
        pass
    
    
    CurrentShape = None
    
    
    CurrentShapeGuid = None
    
    
    IsFlyoutEnabled = None
    
    
    ShapePackage = None
    
    
    StockTool = None
    
    
    StockToolFileUrl = None
    
    
    StockToolId = None
    
    
    ToolData = None
    
    
    ToolType = None
    
    pass

class ToolAttribute(object):
    """
    
    ToolAttribute
        string toolName : Input tool name
        string toolImage : Input tool image location
    """
    ToolImage = None
    
    
    ToolName = None
    
    pass

class ToolEditFlags():
    EditCustom = 1
    EditDefault = 0
    EditMultiple = 4
    EditNone = 2

class ToolPaletteManager(object):
    """
    
    ToolPaletteManager()
    """
    def GetShapePackage(self):
        """
        GetShapePackage -> CatalogItem
            
            string value: 
            Input name of package.
        """
        pass
    
    
    def LoadCatalogs(self):
        """
        LoadCatalogs() -> void
        
        LoadCatalogs(CatalogTypeFlags, LoadFlags) -> void
            
            CatalogTypeFlags flags: 
            Input catalog type to load.
            
            LoadFlags options: 
            Input load option.
        """
        pass
    
    
    def SaveCatalogs(self):
        """
        SaveCatalogs() -> void
        
        SaveCatalogs(CatalogTypeFlags, SaveFlags) -> void
            
            CatalogTypeFlags flags: 
            Input catalog type to save.
            
            SaveFlags options: 
            Input save option.
        """
        pass
    
    
    def UnloadCatalogs(self):
        """
        UnloadCatalogs() -> void
        
        UnloadCatalogs(CatalogTypeFlags) -> void
            
            CatalogTypeFlags flags: 
            Input Unload options.
        """
        pass
    
    
    CatalogPath = None
    
    
    Catalogs = None
    
    
    Manager = None
    
    
    Schemes = None
    
    
    ShapeCatalog = None
    
    
    ShapeCatalogFile = None
    
    
    StockToolCatalogPath = None
    
    
    StockToolCatalogs = None
    
    pass

class ToolType():
    Flyout = 2
    Normal = 1
    Separator = 4
    Text = 1