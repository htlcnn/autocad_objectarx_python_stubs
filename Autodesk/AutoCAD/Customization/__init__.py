class AbstractRibbonSubPanel(object):
    """
    
    AbstractRibbonSubPanel
        parent : Sets the Parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
        
        """
        pass
    
    
    ContainerCollection = None
    
    
    Items = None
    
    
    ResizePriority = None
    
    
    TopJustify = None
    
    pass

class AcceleratorCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            MenuAccelerator menuAccelerator: 
            Input object item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            MenuAccelerator value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MenuAccelerator[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            MenuAccelerator value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input a zero-based index.
            
            MenuAccelerator value: 
            Input an item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(MenuAccelerator) -> void
            
            MenuAccelerator element: 
            Input the item to remove.
        """
        pass
    
    pass

class AliasCollection(object):
    """
    
    """
    def Add(self):
        """
        Add(string) -> void
            
            string alias: 
            Input the item to add.
        Add(string, string) -> void
            
            string alias: 
            Input the name of the CUI file to load as a partial.
            
            string insertBefore: 
            Input the name of the CUI file to be inserted before. If null, the CUI file is appended to the end of the list.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string alias: 
            Input the name of the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            string[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string alias: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero based index.
            
            string alias: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(string) -> void
            
            string alias: 
            Input the name of the alias to remove.
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            string newAlias: 
            Input the new alias.
            
            string oldAlias: 
            Input the alias to be replaced.
        """
        pass
    
    pass

class ApplicationAndDrawingStatusBarsToggle():
    AllOff = 0
    AllOn = 2
    ApplicationOnly = 1
    DrawingStatusBarOnly = 3

class BUTTONPREFIX():
    BUTTONS = None
    AUX = None

class ButtonGroup(object):
    """
    
    ButtonGroup(MenuGroup, StringCollection, BUTTONPREFIX)
        MenuGroup parent : Input the parent MenuGroup.
        StringCollection aliasList : Input a collection of strings to use as aliases.
        BUTTONPREFIX prefix : Identifies this group as either BUTTONS (digitizer buttons) or AUX (mouse buttons).
    
    
    ButtonGroup(ButtonGroup, MenuGroup, int, BUTTONPREFIX)
        ButtonGroup source : Input the group to duplicate.
        MenuGroup parent : Input the parent MenuGroup.
        int index : Input the index at which to insert this group into the parent's collection.
        BUTTONPREFIX prefix : Identifies this group as either BUTTONS (digitizer buttons) or AUX (mouse buttons).
    
    
    """
    ButtonItems = None
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Parent = None
    
    pass

class ButtonGroupCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ButtonGroup buttonGroup: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ButtonGroup value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ButtonGroup[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetCustomGroups(self):
        """
        GetCustomGroups -> ArrayList
        
        """
        pass
    
    
    def GetGroupByAlias(self):
        """
        GetGroupByAlias -> ButtonGroup
            
            string searchAlias: 
            Input the alias being searched for.
        """
        pass
    
    
    def GetGroupByNumber(self):
        """
        GetGroupByNumber -> ButtonGroup
            
            int groupNumber: 
            Input the number of the button group to find.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ButtonGroup value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input a zero-based index.
            
            ButtonGroup value: 
            Input the item to insert.
        """
        pass
    
    
    def NextAlias(self):
        """
        NextAlias -> string
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ButtonGroup) -> void
            
            ButtonGroup element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ButtonItem(object):
    """
    
    ButtonItem(ButtonGroup)
        ButtonGroup parent : Input the parent ButtonGroup that will contain this item.
    
    
    ButtonItem(ButtonGroup, ButtonItem, int)
        ButtonGroup parent : Input the parent.
        ButtonItem buttonItem : Input where the data is copied from.
        int index : Input the index at which to insert new item in parent array. Pass in -1 to append the item to end of array.
    
    
    ButtonItem(ButtonGroup, MenuMacro)
        ButtonGroup parent : Input the parent ButtonGroup that will contain this item.
        MenuMacro menuMacro : Input the macro to be executed.
    
    
    ButtonItem(ButtonGroup, MenuMacro, int)
        ButtonGroup parent : Input the parent ButtonGroup that will contain this item.
        MenuMacro menuMacro : Input the menu macro which will be executed.
        int index : Input the index at which to insert new PopMenuItem in the parent's collection.
    
    
    """
    BlankLine = None
    
    
    Parent = None
    
    pass

class ButtonItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ButtonItem buttonItem: 
            Input the item to add
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ButtonItem value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ButtonItem[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ButtonItem value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ButtonItem value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ButtonItem) -> void
            
            ButtonItem element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ContextualTabDisplayType():
    Full = 0
    FullWithoutFocus = 2
    Merged = 1

class ControlType():
    _3DNavPointTriplet1 = 0x138c
    _3DNavPointTriplet2 = 0x138d
    _3DNavStepSizeSliderControl = 0x138a
    _3DNavStepsPerSecSliderControl = 0x138b
    _3DNavViewComboCtrl = 0x1388
    _3DNavZoomSliderControl = 0x1389
    ArrayEditNameControl = 6
    CustomControl = 20
    DimStyleControl = 11
    FindTextControl = 0x13
    LayerControl = 1
    LayerFilterComboControl = 0x13a2
    LayerLockTransparencySliderControl = 0x13a1
    LayerStateComboControl = 0x13a0
    LightColorCorrectCtrl = 0x1393
    LightSliderControl1 = 0x138e
    LightSliderControl2 = 0x138f
    LightSliderControl3 = 0x1390
    LightSliderControl4 = 0x1391
    LightSliderControl5 = 0x1392
    LineTypeControl = 2
    LineWeightControl = 4
    MldStyleControl = 0x12
    NamedViewControl = 0x10
    OPTColorControl = 3
    PlotStyleControl = 9
    RedoSkinnyButtonControl = 13
    RefblknameControl = 5
    RenderImageQualityControl = 0x1396
    RenderOutputFileControl = 0x1397
    RenderOutputSizeControl = 0x1398
    RenderProgressControl = 0x1395
    RenderStyleControl = 0x1394
    TblStyleControl = 15
    TextHeightComboControl = 0x13a3
    TxtStyleControl = 14
    UCSControl = 10
    UndoSkinnyButtonControl = 12
    ViewControl = 8
    ViewportScaleControl = 7
    VSEdgeColorControl = 0x139a
    VSEdgeOverhangSliderControl = 0x139b
    VSIntersectionEdgeColorControl = 0x139f
    VSJitterEdgeSliderControl = 0x139c
    VSObscuredEdgeColorControl = 0x139e
    VSSilhouetteEdgeWidthSliderControl = 0x139d
    VSStylesComboControl = 0x1399
    WorkspacesControl = 0x11

class CuiFileCollectionBase(object):
    """
    
    """
    def Add(self):
        """
        Add(string) -> Integer
            
            string fileName: 
            Input the filename to add, with or without path.
        Add(string, object) -> void
            
            string fileName: 
            Input the filename to add, with or without path..
            
            object insertBefore: 
            Input the object to insert ahead of. If null, the file is appended to the end of the list.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string fileName: 
            Input the item to find
        """
        pass
    
    
    def GetFileNameByIndex(self):
        """
        GetFileNameByIndex -> string
            
            int index: 
            The index of the file.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string fileName: 
            Input the item to find
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index entry
            
            string fileName: 
            Input the filename to insert, with or without path..
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            string fileName: 
            filename to remove, with or without path.
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            string newFile: 
            Input the new filename.
            
            string oldFile: 
            Input the old filename to replace.
        """
        pass
    
    pass

class CustomizationCollection(object):
    """
    
    CustomizationCollection
        CustomizationElement owner : Input owner for this collection
    """
    def Contains(self):
        """
        Contains -> bool
            
            CustomizationElement customElement: 
            Input the element to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string elementId: 
            Input the unique ID of the element to search for
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            CustomizationElement existElement: 
            Input the existing element
            
            CustomizationElement newElement: 
            Input the new element
        """
        pass
    
    pass

class CustomizationElement(object):
    """
    
    CustomizationElement(ElementBase)
        ElementBase parent : Input the parent to associate with.
    
    
    CustomizationElement(ElementBase, Version)
        ElementBase parent : Input the parent to associate with
        Version revision : Input revision number
    
    
    """
    ElementID = None
    
    
    PreserveTargetElementID = None
    
    pass

class CustomizationReference(object):
    """
    
    CustomizationReference(ElementBase)
        ElementBase parent : Input parent
    
    
    CustomizationReference(ElementBase, string)
        ElementBase parent : Input parent
        string macroID : Input macro ID
    
    
    CustomizationReference(ElementBase, string, Version)
        ElementBase parent : Input parent
        string macroID : Input macro ID
        Version revision : Input revision number
    
    
    """
    MacroID = None
    
    
    MenuMacroReference = None
    
    pass

class CustomizationSection(object):
    """
    
    CustomizationSection()()
    
    
    CustomizationSection(string)
        string fileName : Input the name of the CUI file.
    
    
    CustomizationSection(string, bool)
        string fileName : Input the name of the CUI file.
        bool readOnly : Input whether or not to open the file as read-only.
    
    
    CustomizationSection(string, bool, bool)
        string fileName : Input the name of the CUI file.
        bool readOnly : Input whether or not to open the file as read-only.
        bool showMessageBox : Input whether error and warning messages are to be displayed in a dialog: If set to true, displays in a dialog; otherwise, prints to the command line.
    
    
    CustomizationSection(string, string)
        string fileName : Input the full path for the file being created.
        string menuGroupName : Input the name of the MenuGroup. This will display in the tree view in the CUI dialog and the CUILoad dialog.
    
    
    CustomizationSection(string, string, bool, bool, string[])()
    
    
    CustomizationSection(string, string[])()
    
    
    """
    EXTENSION_BAK = None
    
    
    EXTENSION_OPC = None
    
    
    EXTENSION_BACKUP = None
    
    
    EXTENSION_COMPILED = None
    
    
    EXTENSION_RESOURCE = None
    
    
    EXTENSION_SOURCE = None
    
    
    EXTENSION_TEMPLATE = None
    
    
    EXTENSION_XML = None
    
    
    def AddPartialMenu(self):
        """
        AddPartialMenu -> bool
            
            filename: 
            The menu filename. Can be provided with or without a path, though if provided without a path, it is expected that the file is located on the current support files search path.
        """
        pass
    
    
    def RemovePartialMenu(self):
        """
        RemovePartialMenu -> bool
            
            string menuGroupName: 
            Optional; may be null. The menu group name used in the partial menu. When the partial menu is not found or not loaded, the menu group name can be used to ensure the workspaces are "cleaned up" properly.
            
            filename: 
            The filename of the partial menu. Can be supplied with or without a path to the file, but the filename extension, .CUIX, must either be supplied, or will be assumed. (All legacy menu formats, such as .MNU and .CUI, are converted to .CUIX before they are loaded into AutoCAD. Therefore, only .CUIX menu files can be removed.)
        """
        pass
    
    
    def CloneMenuMacro(self):
        """
        CloneMenuMacro -> MenuMacro
            
            MenuMacro sourceMenuMacro: 
            Input the macro to duplicate.
            
            bool useSimilarMacro: 
            Input whether to re-use existing macros with the same Command string.
        """
        pass
    
    
    def FindMenuMacro(self):
        """
        FindMenuMacro -> MenuMacro
            
            string macroId: 
            Input the ID of the macro to search for.
        """
        pass
    
    
    def FireModifiedEvent(self):
        """
        FireModifiedEvent -> void
        
        """
        pass
    
    
    def LookupElement(self):
        """
        LookupElement -> CustomizationElement
            
            string id: 
            Input the ID for the element within this file.
        """
        pass
    
    
    def Save(self):
        """
        Save() -> bool
        
        Save(bool) -> bool
            
            bool createBackup: 
            Input the full path for file to be created.
        """
        pass
    
    
    CUIFileBaseName = None
    
    
    CUIParseError = None
    
    
    CUIFileName = None
    
    
    CuiFileVersion = None
    
    
    CurrMajorVer = None
    
    
    CurrMinorVer = None
    
    
    MenuGroupDisplayName = None
    
    
    HostServices = None
    
    
    IsModified = None
    
    
    MenuGroup = None
    
    
    MenuGroupName = None
    
    
    PartialCuiFiles = None
    
    
    ReadOnly = None
    
    
    Workspaces = None
    
    pass

class DefaultDisplay():
    AddToWorkspace = 1
    DoNotAddToWorkspace = 0

class DigitizerButtonGroupCollection(object):
    """
    
    """

    pass

class DockableWindowOrient():
    bottom = 3
    floating = 1
    ignore = 6
    left = 4
    right = 5
    top = 2

class DockedFloatingIgnoreToggle():
    docked = 0
    floating = 1
    ignore = 2

class DoubleClickAction(object):
    """
    
    DoubleClickAction()()
    
    
    DoubleClickAction(MenuGroup)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
    
    
    DoubleClickAction(MenuGroup, DoubleClickAction)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        DoubleClickAction sourceDoubleClickAction : Input the source DoubleClickAction to copy the data from.
    
    
    DoubleClickAction(MenuGroup, DoubleClickAction, int)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        DoubleClickAction sourceDoubleClickAction : Input the source DoubleClickAction to copy the data from.
        int index : Input the zero-based index where the DoubleClickAction will be inserted.
    
    
    DoubleClickAction(MenuGroup, int)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        int index : Input the zero-based index where the DoubleClickAction will be inserted.
    
    
    DoubleClickAction(MenuGroup, string)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        string name : Input the name of the double click action.
    
    
    DoubleClickAction(MenuGroup, string, int)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        string name : Input the name of the double click action.
        int index : Input the zero-based index where the DoubleClickAction will be inserted.
    
    
    DoubleClickAction(MenuGroup, string, string, string)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        string name : Input the name of the double click action.
        string description : Input the description of the double click action.
        string dxfname : Input the dxfname of the object associated with the double click action.
    
    
    DoubleClickAction(MenuGroup, string, string, string, int)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        string name : Input the name of the double click action.
        string description : Input the description of the double click action.
        string dxfname : Input the dxfname of the object associated with the double click action.
        int index : Input the zero-based index where the DoubleClickAction will be inserted.
    
    
    DoubleClickAction(MenuGroup, string, string, string, MenuMacro)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        string name : Input the name of the double click action.
        string description : Input the description of the double click action.
        string dxfname : Input the dxfname of the object associated with the double click action.
        MenuMacro menuMacro : Input the MenuMacro command associated with the double click action.
    
    
    DoubleClickAction(MenuGroup, string, string, string, MenuMacro, int)
        MenuGroup parent : Input the MenuGroup that this double click action belongs to.
        string name : Input the name of the double click action.
        string description : Input the description of the double click action.
        string dxfname : Input the dxfname of the object associated with the double click action.
        MenuMacro menuMacro : Input the MenuMacro command associated with the double click action.
        int index : Input the zero-based index where the DoubleClickAction will be inserted.
    
    
    """
    Description = None
    
    
    DoubleClickCmd = None
    
    
    DxfName = None
    
    
    Name = None
    
    
    Parent = None
    
    pass

class DoubleClickCmd(object):
    """
    
    DoubleClickCmd()()
    
    
    DoubleClickCmd(DoubleClickAction)
        DoubleClickAction parent : Input the DoubleClickAction that this command belongs to.
    
    
    DoubleClickCmd(DoubleClickAction, DoubleClickCmd)
        DoubleClickAction parent : Input the DoubleClickAction that this command belongs to.
        DoubleClickCmd sourceDoubleClickCmd : Input the DoubleClickCmd to copy the data from.
    
    
    DoubleClickCmd(DoubleClickAction, MenuMacro)
        DoubleClickAction parent : Input the DoubleClickAction that this command belongs to.
        MenuMacro menuMacro : Input the MenuMacro command.
    
    
    """

    pass

class DoubleClickCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            DoubleClickAction doubleclickAction: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            DoubleClickAction value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DoubleClickAction[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            DoubleClickAction value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            DoubleClickAction value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(DoubleClickAction) -> void
            
            DoubleClickAction element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class DoubleClickDxfNameChangedEventArgs(object):
    """
    
    DoubleClickDxfNameChangedEventArgs
        DoubleClickAction doubleClickAction : Input Autodesk.AutoCAD.Customization.DoubleClickAction object.
        string oldName : Input System.String object.
    """
    DoubleClickActionChanged = None
    
    
    OldDoubleClickDxfName = None
    
    pass

class ElementBase(object):
    """
    
    ElementBase
        ElementBase parent : Input parent of this object.
    """
    def SetIsModified(self):
        """
        SetIsModified -> void
        
        """
        pass
    
    
    Parent = None
    
    pass

class FileOpenException(object):
    """
    
    """

    pass

class FileSaveException(object):
    """
    
    """

    pass

class GalleryDisplayMode():
    ComboBox = 1
    LargeButton = 2
    StandardButton = 3
    Window = 0

class ICustomizationContainer(object):
    """
    
    """
    ContainerCollection = None
    
    pass

class IHostServices(object):
    """
    
    """
    def DisplayMessage(self):
        """
        DisplayMessage -> void
            
            string message: 
            Input the message to display.
            
            string title: 
            Input the title for the dialog box.
        """
        pass
    
    
    def EnterpriseCUIFile(self):
        """
        EnterpriseCUIFile -> CustomizationSection
        
        """
        pass
    
    
    def FindFile(self):
        """
        FindFile -> string
            
            string fileName: 
            Input the file name
        """
        pass
    
    
    def GetDieselEvalString(self):
        """
        GetDieselEvalString -> string
            
            string dieselExpression: 
            Input the expression
        """
        pass
    
    
    def GetLoadedMenuGroupNames(self):
        """
        GetLoadedMenuGroupNames -> ArrayList
        
        """
        pass
    
    
    def InsertMenuOnMenuBar(self):
        """
        InsertMenuOnMenuBar -> void
            
            string menuGroupName: 
            Input the menu group to add to
            
            string alias: 
            Input a new alias
        """
        pass
    
    
    def IsOEM(self):
        """
        IsOEM -> bool
        
        """
        pass
    
    
    def RegistryProductRootKey(self):
        """
        RegistryProductRootKey -> string
        
        """
        pass
    
    
    def WriteMessage(self):
        """
        WriteMessage -> void
            
            string message: 
            Input the message to display.
        """
        pass
    
    pass

class IImageContainer(object):
    """
    
    """

    pass

class IReference(object):
    """
    
    """
    MacroID = None
    
    
    MenuMacroReference = None
    
    pass

class IShortcutKeyCombo(object):
    """
    
    """
    def ShortcutKey(self):
        """
        ShortcutKey -> string
        
        """
        pass
    
    
    def ShortcutName(self):
        """
        ShortcutName -> string
        
        """
        pass
    
    pass

class ImageMenu(object):
    """
    
    ImageMenu(ImageMenu, MenuGroup)
        ImageMenu imageIn : Input the ImageMenu from which to copy data.
        MenuGroup parent : Input the MenuGroup to set as the parent.
    
    
    ImageMenu(ImageMenu, MenuGroup, int)
        ImageMenu imageIn : Input the ImageMenu from which to copy data.
        MenuGroup parent : Input the MenuGroup to set as the parent.
        int index : Input the index where the ImageMenu should be inserted in the MenuGroup array of ImageMenus.
    
    
    ImageMenu(MenuGroup)
        MenuGroup parent : Input the parent.
    
    
    ImageMenu(MenuGroup, string)
        MenuGroup parent : Input the parent.
        string dialogTitle : Input the string to set as the dialog's title.
    
    
    ImageMenu(MenuGroup, string, string, StringCollection)
        MenuGroup parent : Input the parent.
        string dialogTitle : Input the string to set as the dialog's title.
        string description : Input the string to set as the description.
        StringCollection aliases : Input a collection of strings to use as aliases.
    
    
    ImageMenu(MenuGroup, string, StringCollection)
        MenuGroup parent : Input the MenuGroup to set as the parent.
        string dialogTitle : Input the string to set as the dialog's title.
        StringCollection aliases : Input a collection of strings to use as aliases.
    
    
    """
    def AddBlankLine(self):
        """
        AddBlankLine -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    DialogTitle = None
    
    
    ImageMenuItems = None
    
    
    Parent = None
    
    pass

class ImageMenuCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ImageMenu imageMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ImageMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ImageMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ImageMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ImageMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ImageMenu) -> void
            
            ImageMenu element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ImageMenuItem(object):
    """
    
    ImageMenuItem(ImageMenu)
        ImageMenu parent : Input the ImageMenu that will hold this item.
    
    
    ImageMenuItem(ImageMenu, ImageMenuItem, int)
        ImageMenu parent : Input the ImageMenu that will hold this item.
        ImageMenuItem imageMenuItem : Input the ImageMenuItem to copy data from.
        int index : Input the index at which to insert new item in parent array. You may pass in -1 to append the item to end of array.
    
    
    ImageMenuItem(ImageMenu, MenuMacro)
        ImageMenu parent : Input the ImageMenu that will hold this item.
        MenuMacro menuMacro : Input the MenuMacro to execute
    
    
    ImageMenuItem(ImageMenu, MenuMacro, int)
        ImageMenu parent : Input the ImageMenu that will hold this item.
        MenuMacro menuMacro : Input the MenuMacro to execute
        int index : Input the index at which to insert new item in parent array. You may pass in -1 to append the item to end of array.
    
    
    ImageMenuItem(ImageMenu, MenuMacro, string, string)
        ImageMenu parent : Input the ImageMenu that will hold this item.
        MenuMacro menuMacro : Input the MenuMacro to execute
        string slideName : Input the name of image file or image within a slide library to show.
        string slideLibrary : Input the name of the slide library.
    
    
    ImageMenuItem(ImageMenu, MenuMacro, string, string, int)
        ImageMenu parent : Input the ImageMenu that will hold this item.
        MenuMacro menuMacro : Input the MenuMacro to execute
        string slideName : Input the name of image file or image within a slide library to show.
        string slideLibrary : Input the name of the slide library.
        int index : Input the index at which to insert new item in parent array. You may pass in -1 to append the item to end of array.
    
    
    ImageMenuItem(ImageMenu, MenuMacro, string, string, string, int)
        ImageMenu parent : Input the ImageMenu that will hold this item
        MenuMacro menuMacro : Input the MenuMacro to execute
        string name : Input the item name
        string slideName : Input the name of image file or image within a slide library to show.
        string slideLibrary : Input the name of the slide library.
        int index : Input the index at which to insert new item in parent array. You may pass in -1 to append the item to end of array.
    
    
    """
    BlankLine = None
    
    
    Name = None
    
    
    Parent = None
    
    
    SlideLibrary = None
    
    
    SlideName = None
    
    pass

class ImageMenuItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ImageMenuItem imageMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ImageMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ImageMenuItem[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ImageMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ImageMenuItem value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ImageMenuItem) -> void
            
            ImageMenuItem element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ImageUpdatedEventArgs(object):
    """
    
    ImageUpdatedEventArgs
        string oldImage : Input old image
        string newImage : Input new image
    """
    NewImageName = None
    
    
    OldImageName = None
    
    pass

class LspFileCollection(object):
    """
    
    """
    def InsertRange(self):
        """
        InsertRange -> void
            
            int startIndex: 
            Input the index to start inserting.
            
            ArrayList newItems: 
            Input an array of new items
        """
        pass
    
    pass

class MacroCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            Macro macro: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Macro value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Array array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Macro value: 
            Input the item to find.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Index of item to remove
        """
        pass
    
    pass

class MacroGroup(object):
    """
    
    MacroGroup
        string name : Input the name of the MacroGroup .
        MenuGroup parent : Input the parent.
    """
    def AddMacro(self):
        """
        AddMacro -> void
            
            MenuMacro menuMac: 
            Input the MenuMacro to add.
        """
        pass
    
    
    def CreateMenuMacro(self):
        """
        CreateMenuMacro(string, string, string) -> MenuMacro
            
            string name: 
            Input the name of the macro.
            
            string command: 
            Input the command macro string.
            
            string tag: 
            Input the UID attribute.
        CreateMenuMacro(string, string, string, string, MacroType, string, string, string) -> MenuMacro
            
            string name: 
            Input the name of the macro
            
            string command: 
            Input the command macro string
            
            string tag: 
            Input the UID attribute
            
            string help: 
            Input the macro description
            
            MacroType macroType: 
            Input the category in which to put the macro.
            
            string smallImage: 
            Input a small Image Resource ID or file name.
            
            string largeImage: 
            Input a large Image Resource ID or file name.
            
            string labelId: 
            Input an ID to assign to the name string. Pass in null to have one generated.
        """
        pass
    
    
    def IsClassA(self):
        """
        IsClassA -> bool
        
        """
        pass
    
    
    Name = None
    
    
    Parent = None
    
    
    MenuMacros = None
    
    pass

class MacroGroupCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            MacroGroup macroGroup: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(MacroGroup) -> bool
            
            MacroGroup value: 
            Input the item to find.
        Contains(string) -> bool
            
            string name: 
            Input the name to search for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MacroGroup[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            MacroGroup value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            MacroGroup value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class MacroNameChangedEventArgs(object):
    """
    
    MacroNameChangedEventArgs
        Macro macro : Input the macro that changed.
        string oldName : Input the old name.
    """
    MacroChanged = None
    
    
    OldMacroName = None
    
    pass

class MacroType():
    Any = 0
    Dimension = 8
    Draw = 7
    Edit = 2
    File = 1
    Format = 5
    Help = 11
    Insert = 4
    Legacy = 13
    Modify = 9
    Overrides = 12
    Tools = 6
    View = 3
    Window = 10

class MacroUIDChangedEventArgs(object):
    """
    
    MacroUIDChangedEventArgs
        string oldUID : Input the old ID
        string newUID : Input the new ID
    """
    NewMacroUID = None
    
    
    OldMacroUID = None
    
    pass

class MenuAccelerator(object):
    """
    
    MenuAccelerator(MenuAccelerator, MenuGroup)
        MenuAccelerator sourceAccelerator : Input the accelerator to duplicate.
        MenuGroup parent : Input the MenuGroup to which the new accelerator will be appended.
    
    
    MenuAccelerator(MenuAccelerator, MenuGroup, int)
        MenuAccelerator sourceAccelerator : Input the accelerator to duplicate.
        MenuGroup parent : Input the MenuGroup to which the new accelerator will be appended.
        int index : Input the index to insert object in parent collection.
    
    
    MenuAccelerator(MenuMacro, MenuGroup)
        MenuMacro menuMacro : Input the macro to assign to this accelerator key.
        MenuGroup parent : Input the MenuGroup to which the new accelerator will be appended.
    
    
    MenuAccelerator(MenuMacro, MenuGroup, int)
        MenuMacro menuMacro : Input the macro to assign to this accelerator key.
        MenuGroup parent : Input the MenuGroup to which the new accelerator will be appended.
        int index : Input the index to insert object in parent collection.
    
    
    MenuAccelerator(MenuMacro, string, MenuGroup)
        MenuMacro menuMacro : Input the macro to assign to this accelerator key.
        string acceleratorKeyCombination : Input the AcceleratorShortcutKey property.
        MenuGroup parent : Input the MenuGroup to which the new accelerator will be appended.
    
    
    MenuAccelerator(MenuMacro, string, MenuGroup, int)
        MenuMacro menuMacro : Input the macro to assign to this accelerator key.
        string acceleratorKeyCombination : Input the AcceleratorShortcutKey property.
        MenuGroup parent : Input the MenuGroup to which the new accelerator will be appended.
        int index : Input the index to insert object in parent collection.
    
    
    """
    def ShortcutKey(self):
        """
        ShortcutKey -> string
        
        """
        pass
    
    
    def ShortcutName(self):
        """
        ShortcutName -> string
        
        """
        pass
    
    
    Name = None
    
    
    Parent = None
    
    pass

class MenuGroup(object):
    """
    
    """
    def IsModified(self):
        """
        IsModified -> bool
            
            ItemsCollection ic: 
            A single enum value indicating which menu collection to test.
        """
        pass
    
    
    def FindMacroGroup(self):
        """
        FindMacroGroup -> MacroGroup
            
            string groupName: 
            Input the name of MacroGroup to find.
        """
        pass
    
    
    def SetModifiedItems(self):
        """
        SetModifiedItems -> void
            
            ItemsCollection ic: 
            A single enum value indicating which menu collection contains modifications.
        """
        pass
    
    
    Accelerators = None
    
    
    AnyModified = None
    
    
    RibbonRoot = None
    
    
    DigitizerButtons = None
    
    
    DoubleClickActions = None
    
    
    ImageMenus = None
    
    
    LspFiles = None
    
    
    MacroGroups = None
    
    
    MouseButtons = None
    
    
    Name = None
    
    
    QuickAccessToolbars = None
    
    
    PopMenus = None
    
    
    QuickPropertiesObjectTypes = None
    
    
    ScreenMenus = None
    
    
    TabletMenus = None
    
    
    TemporaryOverrides = None
    
    
    Toolbars = None
    
    
    ToolPanels = None
    
    
    class ItemsCollection():
        Accelerators = None
        DashboardPanelSets = None
        DashboardToolPanels = None
        DigitizerButtons = None
        DoubleClickActions = None
        ImageMenus = None
        MacroGroups = None
        MouseButtons = None
        QuickPropertiesObjectTypes = None
        RolloverTooltipObjectTypes = None
        PopMenus = None
        RibbonRoot = None
        ScreenMenus = None
        TabletMenus = None
        TemporaryOverrides = None
        Toolbars = None
        QuickAccessToobars = None
        LspFile = None
    
    pass

class MenuGroupItemsCollection(object):
    """
    
    """
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string elementId: 
            Input the unique ID of the element to find.
        """
        pass
    
    
    Owner = None
    
    pass

class MenuGroupNameChangedEventArgs(object):
    """
    
    MenuGroupNameChangedEventArgs
        string oldName : Input the old name.
    """
    OldName = None
    
    pass

class MenuMacro(object):
    """
    
    MenuMacro(MacroGroup, string, string, string)
        MacroGroup parent : Input the parent MacroGroup.
        string name : Input the name which will be displayed in the command list.
        string command : Input the command macro string.
        string tag : Input the unique ID for the macro.
    
    
    MenuMacro(MacroGroup, string, string, string, MacroType)
        MacroGroup parent : Input the parent MacroGroup.
        string name : Input the name which will be displayed in the command list.
        string command : Input the command macro string.
        string tag : Input the unique ID for the macro.
        MacroType macroType : Input the macro type to one of the MacroType enums.
    
    
    MenuMacro(MenuMacro, MacroGroup, bool)
        MenuMacro menuMacIn : Input the MenuMacro to duplicate.
        MacroGroup parent : Input which sets the parent.
        bool DeepClone : If true, all macros within the MenuMacro will be duplicated. Otherwise, only the current macro is duplicated.
    
    
    """
    def isCitizenA(self):
        """
        isCitizenA -> bool
        
        """
        pass
    
    
    def isModified(self):
        """
        isModified -> bool
        
        """
        pass
    
    
    def isUserSource(self):
        """
        isUserSource -> bool
        
        """
        pass
    
    
    def ResetToDefault(self):
        """
        ResetToDefault -> void
        
        """
        pass
    
    
    def SetRevision(self):
        """
        SetRevision -> void
        
        """
        pass
    
    
    ElementID = None
    
    
    Macros = None
    
    
    macro = None
    
    
    Parent = None
    
    pass

class MenuMacroCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            MenuMacro menuMacro: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            MenuMacro value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MenuMacro[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf(MenuMacro) -> Integer
            
            MenuMacro item: 
            Input the item to find.
        IndexOf(string) -> Integer
            
            string macroID: 
            Input the ID of item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            MenuMacro value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(MenuMacro) -> void
            
            MenuMacro element: 
            Input the item to remove.
        """
        pass
    
    pass

class ModelLayoutIgnoreToggle():
    ignore = 2
    Layout = 1
    Model = 0

class ObjectProperty(object):
    """
    
    ObjectProperty
        ObjectProperty source : Input object to copy
        ObjectType parent : Input parent of new object
        int index : Input index for collection
    """
    state = None
    
    pass

class ObjectPropertyCategory(object):
    """
    
    """
    def setSubItemState(self):
        """
        setSubItemState -> void
            
            int newVal: 
            Input new value
        """
        pass
    
    
    PropertyList = None
    
    
    state = None
    
    pass

class ObjectType(object):
    """
    
    """
    ClassName = None
    
    
    ContainerCollection = None
    
    
    DisplayName = None
    
    
    Parent = None
    
    
    PropCollection = None
    
    
    SubtypeList = None
    
    pass

class ObjectTypeCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ObjectType ObjectType: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(ObjectType) -> bool
            
            ObjectType value: 
            Input the item to find.
        Contains(string) -> bool
            
            string className: 
            Input the class name item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectType[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindWithName(self):
        """
        FindWithName -> ObjectType
            
            string className: 
            Input item's class name
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ObjectType value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ObjectType value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(ObjectType) -> void
            
            ObjectType element: 
            Input the item to remove.
        """
        pass
    
    
    def SortByDisplayName(self):
        """
        SortByDisplayName -> void
        
        """
        pass
    
    pass

class OnOffIgnoreToggle():
    ignore = 3
    off = 2
    on = 1

class Orientation():
    Horizontal = 0
    Vertical = 1

class OverrideItem(object):
    """
    
    OverrideItem
        string macroID : Input the ID of the MenuMacro referenced by this item.
        OverrideKeyState keyState : Input the "Up" or "Down" key state
        TemporaryOverride parent : Input the parent.
    """
    KeyState = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    Parent = None
    
    pass

class OverrideKeyState():
    Down = None
    Up = None

class Panel(object):
    """
    
    Panel(PanelSet)
        PanelSet parent : Input the parent
    
    
    Panel(string, PanelSet)
        string name : Input the panel's name.
        PanelSet parent : Input the parent.
    
    
    Panel(PanelSet, Panel, int)
        PanelSet parent : Input the parent.
        Panel source : Input the copy source.
        int index : Input the index position.
    
    
    """
    Aliases = None
    
    
    Description = None
    
    
    LargeImage = None
    
    
    LowerPanel = None
    
    
    LowerToolPanel = None
    
    
    Name = None
    
    
    Parent = None
    
    
    SmallImage = None
    
    
    UpperPanel = None
    
    
    UpperToolPanel = None
    
    pass

class PanelCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Panel panel: 
            Input the new panel
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Panel value: 
            Input the panel to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Panel[] array: 
            Input the array to copy to
            
            int index: 
            Input the zero-based array index
        """
        pass
    
    
    def FindPanelWithAlias(self):
        """
        FindPanelWithAlias -> Panel
            
            string panelAlias: 
            Input the alias to search for.
        """
        pass
    
    
    def FindPanelWithName(self):
        """
        FindPanelWithName -> Panel
            
            string panelName: 
            Input the name to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Panel value: 
            Input the item to search for.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the array position.
            
            Panel value: 
            Input the object to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string panelName: 
            Input the name to search for.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the Panel index in the collection.
        Remove(Panel) -> void
            
            Panel element: 
            Input the object to remove.
        """
        pass
    
    
    AllAliases = None
    
    pass

class PanelPosition():
    Upper = None
    Lower = None

class PanelSet(object):
    """
    
    """
    ContainerCollection = None
    
    
    Panels = None
    
    pass

class PartialCuiFileCollection(object):
    """
    
    """

    pass

class PopMenu(object):
    """
    
    PopMenu(string, StringCollection, string, MenuGroup)
        string name : Input the name of this PopMenu.
        StringCollection aliasList : Input the list of aliases for the PopMenu. If you intend for this menu to be a sub-menu of another PopMenu, aliasList should be null.
        string tag : Input the UID of this PopMenu.
        MenuGroup menuGroup : Input the parent.
    
    
    PopMenu(PopMenu, MenuGroup, int)
        PopMenu popIn : Input the source PopMenu.
        MenuGroup menuGroup : Input the parent.
        int index : Input the index at which to insert new PopMenu in the parent's collection. Since PopMenus are referenced by their ElementID or Aliases, the index value can normally be -1, to simply append this menu to the PopMenuCollection.
    
    
    """
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    DisplayName = None
    
    
    HasDiesel = None
    
    
    IsShortcut = None
    
    
    Name = None
    
    
    Parent = None
    
    
    PopAlias = None
    
    
    PopMenuItems = None
    
    
    ShortcutAlias = None
    
    
    TopLevelMenu = None
    
    pass

class PopMenuCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            PopMenu popMenu: 
            Input the item to add.
        """
        pass
    
    
    def AddPopMenu(self):
        """
        AddPopMenu -> bool
            
            PopMenu popMenu: 
            Input the PopMenu to add.
            
            PopMenu insertBefore: 
            Input the PopMenu before which to insert.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            PopMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            PopMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based collection index at which copying begins.
        """
        pass
    
    
    def FindPopWithAlias(self):
        """
        FindPopWithAlias -> PopMenu
            
            string pmAlias: 
            Input the alias you seek.
        """
        pass
    
    
    def FindPopWithName(self):
        """
        FindPopWithName -> PopMenu
            
            string pmName: 
            Input the name which is sought.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            PopMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            PopMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string pmName: 
            Input the name you seek.
        """
        pass
    
    
    def NextAlias(self):
        """
        NextAlias -> string
            
            bool isContext: 
            Input whether to get the next pulldown menu alias or context menu alias.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(PopMenu) -> void
            
            PopMenu popMenu: 
            Input the item to remove.
        """
        pass
    
    
    AllAliases = None
    
    pass

class PopMenuItem(object):
    """
    
    PopMenuItem(PopMenu)
        PopMenu parent : Input the parent.
    
    
    PopMenuItem(PopMenu, int)
        PopMenu parent : Input the parent.
        int index : Input the index at which to insert a new PopMenuItem in the parent's collection.
    
    
    PopMenuItem(PopMenuItem, PopMenu, int)
        PopMenuItem source : Input the PopMenuItem to duplicate.
        PopMenu parent : Input the parent.
        int index : Input the index at which to insert a new PopMenuItem in the parent's collection.
    
    
    PopMenuItem(MenuMacro, string, PopMenu, int)
        MenuMacro menuMacro : Input the macro to execute
        string name : Input the name of the PopMenuItem, if different from the name of the MenuMacro; otherwise, can be null
        PopMenu parent : Input the parent
        int index : Input the index at which to insert a new PopMenuItem in the parent's collection
    
    
    PopMenuItem(MenuMacro, string, PopMenuItemBase, PopMenu, int)
        MenuMacro menuMacro : Input the macro to execute.
        string name : Input the name of the PopMenuItem if different from the name of the MenuMacro; otherwise, can be null.
        PopMenuItemBase insertBefore : Input the item before which to insert.
        PopMenu parent : Input the parent.
        int index : Input the index at which to insert a new PopMenuItem in the parent's collection.
    
    
    """
    DisplayName = None
    
    
    HasDiesel = None
    
    
    IsSeparator = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    Name = None
    
    pass

class PopMenuItemBase(object):
    """
    
    """
    Parent = None
    
    pass

class PopMenuItemCollection(object):
    """
    
    PopMenuItemCollection
        CustomizationElement owner : Input Autodesk.AutoCAD.Customization.CustomizationElement object.
    """
    def Add(self):
        """
        Add -> void
            
            PopMenuItemBase popMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            PopMenuItemBase element: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            PopMenuItemBase[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in the array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            PopMenuItemBase element: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            PopMenuItemBase element: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(PopMenuItemBase) -> void
            
            PopMenuItemBase element: 
            Input the item to remove.
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            PopMenuItemBase existElement: 
            Input the old PopMenuItemBase element.
            
            PopMenuItemBase newElement: 
            Input the new PopMenuItemBase element.
        """
        pass
    
    pass

class PopMenuRef(object):
    """
    
    PopMenuRef
        PopMenu popMenu : Input the PopMenu to use as a sub-menu.
        PopMenu parent : Input the parent popmenu.
        int index : Input the index at which to insert the new PopMenuRef in the parent's collection. -1 will append the pop menu to the end of the collection.
    """
    MenuReference = None
    
    
    Parent = None
    
    pass

class PropertyCollection(object):
    """
    
    PropertyCollection(ObjectPropertyBase)
        parent : Input parent
    
    
    PropertyCollection(ObjectType)
        type : Input type
    
    
    """
    def Add(self):
        """
        Add -> void
            
            ObjectPropertyBase objPropBase: 
            Input new object
        """
        pass
    
    
    def Contains(self):
        """
        Contains(ObjectPropertyBase) -> bool
            
            ObjectPropertyBase value: 
            Input value to check for
        Contains(string) -> bool
            
            string name: 
            Input item name
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectPropertyBase[] array: 
            Input target array
            
            int index: 
            Input the zero-based index in array at which copying begins
        """
        pass
    
    
    def FindWithName(self):
        """
        FindWithName -> ObjectPropertyBase
            
            string name: 
            Input name
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ObjectPropertyBase value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ObjectPropertyBase value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ObjectPropertyBase) -> void
            
            ObjectPropertyBase element: 
            Input item to remove
        """
        pass
    
    
    Initialized = None
    
    
    ObjectTypeInfo = None
    
    pass

class QuickAccessToolbar(object):
    """
    
    QuickAccessToolbar()()
    
    
    QuickAccessToolbar(MenuGroup)
        MenuGroup parent : Sets the parent.
    
    
    QuickAccessToolbar(string, MenuGroup)
        string UID : Element Id to use for the toolbar. If the ID is not unique to the file, a unique ID will be generated.
        MenuGroup parent : Parent MenuGroup that contains this toolbar.
    
    
    """
    class QuickAccessToolbarNameChangedEventArgs(object):
        """
        
        QuickAccessToolbarNameChangedEventArgs
            QuickAccessToolbar toolbar : The modified toolbar
            string oldName : The old name
        """
        OldToolbarName = None
        
        
        ToolbarChanged = None
        
        pass
    
    
    Aliases = None
    
    
    Description = None
    
    
    Name = None
    
    
    Parent = None
    
    
    RibbonItems = None
    
    pass

class QuickAccessToolbarCollection(object):
    """
    
    QuickAccessToolbarCollection
        MenuGroup owner : Owner of the collection.
    """
    def Add(self):
        """
        Add -> void
            
            QuickAccessToolbar qatToolbar: 
            Item to add.
        """
        pass
    
    
    def AddQATToolbar(self):
        """
        AddQATToolbar -> bool
            
            QuickAccessToolbar qatToolbar: 
            Toolbar to add.
            
            object obj: 
            Toolbar in the collection in front of which qatToolbar is to be inserted.If NULL, or obj is not found in the collection, then qatToolbar is appended to the end.
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> QuickAccessToolbar
            
            QuickAccessToolbar source: 
            Source QuickAccessToolbar.
            
            QuickAccessToolbar insertBefore: 
            QuickAccessToolbar to insert this one before.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            QuickAccessToolbar value: 
            Item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            QuickAccessToolbar[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindToolbarWithAlias(self):
        """
        FindToolbarWithAlias -> QuickAccessToolbar
            
            string toolbarAlias: 
            Alias to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            QuickAccessToolbar value: 
            Item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Zero-based index.
            
            QuickAccessToolbar value: 
            Item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string toolbarName: 
            Name to search for.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(QuickAccessToolbar) -> void
            
            QuickAccessToolbar qatToolbar: 
            Item to remove.
        Remove(int) -> void
            
            int index: 
            Index of item to remove.
        """
        pass
    
    pass

class QuickAccessToolbarOrientation():
    Above = 0
    Below = 1

class RibbonAutoHideMode():
    HidePanelBar = None
    HidePanel = None
    TruncatePanelBar = None

class RibbonButton(object):
    """
    
    RibbonButton
        CustomizationElement parent : Sets the Parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy.
        """
        pass
    
    
    ButtonStyle = None
    
    
    KeyTip = None
    
    pass

class RibbonButtonStyle():
    LargeWithHorizontalText = 1
    LargeWithoutText = 4
    LargeWithText = 0
    SmallWithoutText = 3
    SmallWithText = 2

class RibbonCommandButton(object):
    """
    
    RibbonCommandButton
        CustomizationElement parent : Sets the Parent
    """
    ImageUpdated = None
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    
    GroupName = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    TooltipTitle = None
    
    
    ButtonStyle = None
    
    
    KeyTip = None
    
    pass

class RibbonControl(object):
    """
    
    RibbonControl
        CustomizationElement parent : Sets the Parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    
    MaxWidth = None
    
    
    MinWidth = None
    
    
    LargeImage = None
    
    
    SmallImage = None
    
    
    KeyTip = None
    
    pass

class RibbonDataBoundDropDown(object):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    
    ButtonStyle = None
    
    
    ListStyle = None
    
    
    SmallImage = None
    
    
    LargeImage = None
    
    
    KeyTip = None
    
    pass

class RibbonDialogBoxLauncher(object):
    """
    
    RibbonDialogBoxLauncher
        RibbonPanelSource ribbonPanelSource : Input the RibbonPanelSource to which this item belongs.
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            item: 
            The RibbonItem from which to copy the data.
        """
        pass
    
    
    KeyTip = None
    
    pass

class RibbonFoldPanel(object):
    """
    
    RibbonFoldPanel
        parent : Sets the Parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def IsAllowedChildType(self):
        """
        IsAllowedChildType -> bool
        
        """
        pass
    
    
    def IsValidChildType(self):
        """
        IsValidChildType -> bool
        
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
        
        """
        pass
    
    
    DefaultSize = None
    
    
    MaximumSize = None
    
    
    MinimumSize = None
    
    
    ResizeStyle = None
    
    pass

class RibbonFoldPanelItemSize():
    Large = 3
    Medium = 2
    Small = 1

class RibbonFoldPanelResizeStyle():
    DoNotResize = 1
    None = 0

class RibbonGalleryControl(object):
    """
    
    RibbonGalleryControl
        CustomizationElement parent : Sets the Parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    pass

class RibbonImageSize():
    Large = 3
    None = 0
    Standard = 1

class RibbonItem(object):
    """
    
    RibbonItem
        CustomizationElement parent : Sets the Parent
    """
    def Clone(self):
        """
        Clone -> RibbonItem
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem item: 
            The RibbonItem from which to copy the data.
        """
        pass
    
    
    def IsAllowedChildType(self):
        """
        IsAllowedChildType -> bool
        
        """
        pass
    
    
    Id = None
    
    
    Text = None
    
    pass

class RibbonItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            RibbonItem item: 
            The RibbonItem being added to the collection.
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> RibbonItem
            
            RibbonItem source: 
            The RibbonItem to clone and insert.
            
            RibbonItem insertBefore: 
            Then RibbonItem in the collection before which the source is to be inserted.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Zero-based index.
            
            RibbonItem value: 
            RibbonItem to insert.
        """
        pass
    
    pass

class RibbonItemSize():
    Large = 3
    Medium = 2
    Standard = 1

class RibbonLockModes():
    LockAll = 7
    LockDockedPanels = 1
    LockFloatingPanels = 2
    LockTabs = 4
    None = 0

class RibbonPanelBreak(object):
    """
    
    RibbonPanelBreak
        RibbonPanelSource parent : Sets the Parent
    """

    pass

class RibbonPanelResizeStyle():
    CollapseLast = 2
    Default = 0
    NoCollapse = 1

class RibbonPanelSource(object):
    """
    
    RibbonPanelSource
        parent : Sets the Parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem from which the data is copied.
        """
        pass
    
    
    def FindItem(self):
        """
        FindItem -> RibbonItem
            
            string id: 
            Id of the ribbon item to find.
        """
        pass
    
    
    def GetMenuMacros(self):
        """
        GetMenuMacros() -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Items = None
    
    
    KeyTip = None
    
    
    Name = None
    
    
    DialogBoxLauncher = None
    
    pass

class RibbonPanelSourceCollection(object):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonPanelSource
            
            RibbonPanelSource sourcePanel: 
            The RibbonPanelSource to clone and insert.
            
            RibbonPanelSource insertBefore: 
            The RibbonPanelSource in the collection before which sourcePanel is to be inserted.
        """
        pass
    
    
    def FindRibbonPanelWithText(self):
        """
        FindRibbonPanelWithText -> RibbonPanelSource
            
            string ribbonPanelName: 
            Input name of ribbon panel.
        """
        pass
    
    
    def IsTextFree(self):
        """
        IsTextFree -> bool
            
            string ribbonPanelName: 
            The name of the panel being searched for.
        """
        pass
    
    pass

class RibbonPanelSourceReference(object):
    """
    
    RibbonPanelSourceReference
        RibbonTabSource tabSource : Input the RibbonTabSource to which this item belongs.
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input RibbonItem from which to copy the data.
        """
        pass
    
    
    PanelId = None
    
    pass

class RibbonPanelSourceReferenceCollection(object):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonPanelSourceReference
            
            RibbonPanelSourceReference source: 
            Input the source RibbonPanelSourceReference.
            
            RibbonPanelSourceReference insertBefore: 
            Input RibbonPanelSourceReference before which the source is being inserted.
        """
        pass
    
    pass

class RibbonRoot(object):
    """
    
    """
    def FindPanel(self):
        """
        FindPanel -> RibbonPanelSource
            
            string id: 
            Input the string id of the RibbonPanelSource to find.
        """
        pass
    
    
    def FindPanelSource(self):
        """
        FindPanelSource -> RibbonPanelSource
            
            Collection<CustomizationSection> cuiFiles: 
            _nt_
            
            string sMenuGroupName: 
            _nt_
            
            string sId: 
            _nt_
        """
        pass
    
    
    def FindPanelWithAlias(self):
        """
        FindPanelWithAlias -> RibbonPanelSource
            
            string ribbonPanelAlias: 
            Input the ribbon panel alias being searched for.
        """
        pass
    
    
    def FindTab(self):
        """
        FindTab -> RibbonTabSource
            
            string id: 
            Input the string identifying the RibbonTabSource to find.
        """
        pass
    
    
    def FindTabWithAlias(self):
        """
        FindTabWithAlias -> RibbonTabSource
            
            string ribbonTabAlias: 
            Input the ribbon tab alias to search for.
        """
        pass
    
    
    def RemovePanel(self):
        """
        RemovePanel -> void
            
            RibbonPanelSource panelSource: 
            Input the RibbonPanelSource to remove.
        """
        pass
    
    
    RibbonPanelSources = None
    
    
    RibbonTabSelectors = None
    
    
    RibbonTabSources = None
    
    pass

class RibbonRowPanel(object):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to copy the data.
        """
        pass
    
    
    def IsValidChildType(self):
        """
        IsValidChildType -> bool
        
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
        
        """
        pass
    
    
    ResizeStyle = None
    
    pass

class RibbonRowPanelResizeStyle():
    DoNotResize = 4
    NeverHideText = 1
    NeverShrink = 3
    NeverWrap = 2
    None = 0

class RibbonSeparator(object):
    """
    
    RibbonSeparator
        CustomizationElement parent : Input the parent item.
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to copy the data.
        """
        pass
    
    
    SeparatorStyle = None
    
    pass

class RibbonSeparatorStyle():
    Line = 1
    Spacer = 2

class RibbonSplitButton(object):
    """
    
    RibbonSplitButton
        CustomizationElement parent : Input the parent item.
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input RibbonItem being copied from.
        """
        pass
    
    
    Command = None
    
    
    Grouping = None
    
    
    ListStyle = None
    
    
    TooltipTitle = None
    
    
    ButtonStyle = None
    
    
    Behavior = None
    
    
    Items = None
    
    
    ContainerCollection = None
    
    
    SmallImage = None
    
    
    LargeImage = None
    
    
    KeyTip = None
    
    pass

class RibbonSplitButtonBehavior():
    DropDownFollow = 1
    DropDownNoFollow = 2
    SplitFollow = 3
    SplitFollowStaticText = 5
    SplitNoFollow = 4

class RibbonSplitButtonListStyle():
    Descriptive = 3
    Icon = 1
    IconText = 2

class RibbonTabSelector(object):
    """
    
    """
    def Append(self):
        """
        Append -> bool
            
            string sId: 
            Input the identifier of the tab to be added.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string sId: 
            Input the identifier of the tab to find.
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which the to copy the data.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> bool
            
            string sId: 
            Id of the tab to be inserted.
            
            string sInsertBefore: 
            The new tab will be placed before this tab.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> bool
            
            string sId: 
            Input the string Id of the tab to be removed.
        """
        pass
    
    
    Rule = None
    
    
    Tabs = None
    
    pass

class RibbonTabSelectorCollection(object):
    """
    
    RibbonTabSelectorCollection
        RibbonRoot owner : Input the RibbonRoot to which this collection belongs.
    """
    def Clone(self):
        """
        Clone -> RibbonTabSelector
            
            RibbonTabSelector source: 
            Source RibbonTabSelector
            
            RibbonTabSelector insertBefore: 
            RibbonTabSelector to insert this one before.
        """
        pass
    
    pass

class RibbonTabSource(object):
    """
    
    RibbonTabSource
        RibbonRoot ribbonRoot : Input the RibbonRoot to which this item belongs.
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to copy the data.
        """
        pass
    
    
    def Find(self):
        """
        Find -> RibbonPanelSourceReference
            
            string id: 
            Input the string that identifies the RibbonPanelSourceReference to find.
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    DefaultDisplay = None
    
    
    DisplayType = None
    
    
    Items = None
    
    
    Name = None
    
    
    WorkspaceBehavior = None
    
    
    KeyTip = None
    
    pass

class RibbonTabSourceCollection(object):
    """
    
    RibbonTabSourceCollection
        RibbonRoot owner : Input the RibbonRoot to which this collection belongs.
    """
    def Clone(self):
        """
        Clone -> RibbonTabSource
            
            RibbonTabSource source: 
            Input the source RibbonTabSource to clone and insert.
            
            RibbonTabSource insertBefore: 
            Input the RibbonTabSource before which the source is to be inserted in the collection.
        """
        pass
    
    pass

class RibbonToggleButton(object):
    """
    
    RibbonToggleButton
        CustomizationElement parent : Input the parent that will contain this item.
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to the copy the data.
        """
        pass
    
    
    ButtonStyle = None
    
    
    KeyTip = None
    
    pass

class ScreenMenu(object):
    """
    
    ScreenMenu(MenuGroup)
        MenuGroup parent : Input the parent MenuGroup.
    
    
    ScreenMenu(MenuGroup, string)
        MenuGroup parent : Input the parent MenuGroup.
        string name : Input the name of the screen menu.
    
    
    ScreenMenu(ScreenMenu, MenuGroup)
        ScreenMenu sourceMenu : Input the source menu to copy data from.
        MenuGroup parent : Input the parent MenuGroup.
    
    
    ScreenMenu(ScreenMenu, MenuGroup, int)
        ScreenMenu sourceMenu : Input the source menu to copy data from.
        MenuGroup parent : Input the parent MenuGroup.
        int index : Input the location within the parent's collection at which to insert the menu.
    
    
    ScreenMenu(MenuGroup, string, string, StringCollection, int, bool)
        MenuGroup parent : Input the parent MenuGroup.
        string name : Input the name of the screen menu.
        string description : Input a description for the screen menu.
        StringCollection aliasList : Input a collection of strings to use as aliases.
        int start : Input the line number on which to start inserting menu items.
        bool createBlankMenuItems : If true, creates a screen menu with 22 blank lines.
    
    
    ScreenMenu(MenuGroup, string, StringCollection, int, bool)
        MenuGroup parent : Input the parent MenuGroup.
        string name : Input the name of the screen menu.
        StringCollection aliases : Input a collection of strings to use as aliases.
        int start : Input the line number on which to start inserting menu items.
        bool createBlankMenuItems : If true, creates a screen menu with 22 blank lines.
    
    
    """
    def AddBlankLine(self):
        """
        AddBlankLine -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    Name = None
    
    
    NumLines = None
    
    
    Parent = None
    
    
    ScreenMenuItems = None
    
    
    StartLine = None
    
    pass

class ScreenMenuCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ScreenMenu screenMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ScreenMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ScreenMenu[] array: 
            Input the target array
            
            int index: 
            Input the zero-based index in array at which copying begins
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ScreenMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ScreenMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ScreenMenu) -> void
            
            ScreenMenu element: 
            Input item to remove
        """
        pass
    
    pass

class ScreenMenuItem(object):
    """
    
    ScreenMenuItem(ScreenMenu)
        ScreenMenu parent : Input the parent screen menu that will contain this menu item.
    
    
    ScreenMenuItem(ScreenMenu, MenuMacro)
        ScreenMenu parent : Input the parent screen menu that will contain this menu item.
        MenuMacro menuMacro : Input the MenuMacro that this item references.
    
    
    ScreenMenuItem(ScreenMenu, MenuMacro, int)
        ScreenMenu parent : Input the parent screen menu that will contain this menu item.
        MenuMacro menuMacro : Input the MenuMacro that this item references.
        int index : Locates the menu item at a specific index within the parent's ScreenMenuItemCollection.
    
    
    ScreenMenuItem(ScreenMenu, ScreenMenuItem, int)
        ScreenMenu parent : Input Autodesk.AutoCAD.Customization.ScreenMenu object, which sets the parent screen menu that will contain this menu item.
        ScreenMenuItem screenMenuItem : Input Autodesk.AutoCAD.Customization.ScreenMenuItem object, ScreenMenuItem from which to copy data.
        int index : Input System.Int32 object. Locates the menu item at a specific index within the parent's ScreenMenuItemCollection.
    
    
    """
    BlankLine = None
    
    
    Name = None
    
    
    Parent = None
    
    pass

class ScreenMenuItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ScreenMenuItem screenMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ScreenMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ScreenMenuItem[] array: 
            Input the target array
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ScreenMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ScreenMenuItem value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(ScreenMenuItem) -> void
            
            ScreenMenuItem element: 
            Input the item to remove.
        """
        pass
    
    
    def RemoveRange(self):
        """
        RemoveRange -> void
            
            int startIndex: 
            Input the index at which to begin removal. The item at this index is included in the items removed.
            
            int endIndex: 
            Input the index at which to stop removing items. The item at this index is included in the items removed.
        """
        pass
    
    pass

class ShortcutKeyChangeAction():
    NameChanged = None
    KeyChanged = None

class ShortcutKeyChangedEventArgs(object):
    """
    
    ShortcutKeyChangedEventArgs
        IShortcutKeyCombo shortcutKey : Input the new shortcut key.
        ShortcutKeyChangeAction action : Input the new action.
    """
    ShortcutKeyAction = None
    
    
    ShortcutKeyChanged = None
    
    pass

class TabletMenu(object):
    """
    
    TabletMenu(MenuGroup)
        MenuGroup parent : Input the menu group to which the TabletMenu will be added.
    
    
    TabletMenu(MenuGroup, StringCollection)
        MenuGroup parent : Input the menu group to which the TabletMenu will be added.
        StringCollection aliases : Input a collection of aliases for this TabletMenu.
    
    
    TabletMenu(MenuGroup, StringCollection, int, int)
        MenuGroup parent : Input the menu group to which the TabletMenu will be added.
        StringCollection aliases : Input a collection of aliases for this TabletMenu.
        int rows : Input the number of rows in this table menu
        int columns : Input the number of columns in this tablet menu
    
    
    TabletMenu(TabletMenu, MenuGroup)
        TabletMenu sourceMenu : Input the source menu that is used to populate data.
        MenuGroup parent : Input the menu group to which the TabletMenu will be added.
    
    
    TabletMenu(TabletMenu, MenuGroup, int)
        TabletMenu sourceMenu : Input the source menu that is used to populate data.
        MenuGroup parent : Input the menu group to which the TabletMenu will be added.
        int index : Input the index at which to insert the TabletMenu in the tablet menu collection.
    
    
    """
    def AddBlankLine(self):
        """
        AddBlankLine -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    Columns = None
    
    
    ContainerCollection = None
    
    
    Parent = None
    
    
    Rows = None
    
    
    TabletArea = None
    
    
    TabletMenuItems = None
    
    pass

class TabletMenuCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            TabletMenu tabletMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            TabletMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TabletMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            TabletMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            TabletMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove.
        Remove(TabletMenu) -> void
            
            TabletMenu element: 
            Input the item to remove.
        """
        pass
    
    pass

class TabletMenuItem(object):
    """
    
    TabletMenuItem(TabletMenu)
        TabletMenu parent : Input the containment TabletMenu.
    
    
    TabletMenuItem(TabletMenu, MenuMacro)
        TabletMenu parent : Input the containment TabletMenu.
        MenuMacro menuMacro : Input the menu macro that this item will execute.
    
    
    TabletMenuItem(TabletMenu, MenuMacro, int)
        TabletMenu parent : Input the containment TabletMenu.
        MenuMacro menuMacro : Input the menu macro that this item will execute.
        int index : Input the array position at which to insert the item.
    
    
    TabletMenuItem(TabletMenu, TabletMenuItem, int)
        TabletMenu parent : Input the containment TabletMenu.
        TabletMenuItem tabletMenuItem : Input the TabletMenuItem to copy data from.
        int index : Input the array position at which to insert the item.
    
    
    """
    BlankLine = None
    
    
    Parent = None
    
    pass

class TabletMenuItemCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            TabletMenuItem tabletMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            TabletMenuItem item: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TabletMenuItem[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            TabletMenuItem item: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            TabletMenuItem item: 
            Input the item to insert.
        """
        pass
    
    
    def InsertRange(self):
        """
        InsertRange -> void
            
            int startIndex: 
            Input the index at which to begin inserting.
            
            ArrayList newItems: 
            Input the array of items to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(TabletMenuItem) -> void
            
            TabletMenuItem element: 
            Input the item to remove.
        """
        pass
    
    
    def RemoveRange(self):
        """
        RemoveRange -> void
            
            int startIndex: 
            Input the index at which to begin removal. The item at this index is included in the items removed.
            
            int endIndex: 
            Input the index at which to stop removing items. The item at this index is included in the items removed.
        """
        pass
    
    pass

class TemporaryOverride(object):
    """
    
    TemporaryOverride(MenuGroup)
        MenuGroup parent : Input the parent.
    
    
    TemporaryOverride(MenuGroup, MenuMacro)
        MenuGroup parent : Input the parent.
        MenuMacro menuMacro : Input the macro to execute.
    
    
    TemporaryOverride(MenuGroup, MenuMacro, MenuMacro)
        MenuGroup parent : Input the parent.
        MenuMacro menuMacroKeyDown : Input the macro to execute on key down.
        MenuMacro menuMacroKeyUp : Input the macro to execute on key up.
    
    
    TemporaryOverride(MenuGroup, TemporaryOverride, int)
        MenuGroup parent : Input the parent.
        TemporaryOverride source : Input the source override object to duplicate.
        int index : Input the index at which to insert the TemporaryOverrride in the parent.
    
    
    """
    def ShortcutKey(self):
        """
        ShortcutKey -> string
        
        """
        pass
    
    
    def ShortcutName(self):
        """
        ShortcutName -> string
        
        """
        pass
    
    
    Description = None
    
    
    DownOverride = None
    
    
    Name = None
    
    
    OverrideShortcutKey = None
    
    
    Parent = None
    
    
    UpOverride = None
    
    pass

class TemporaryOverrideCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            TemporaryOverride temporaryOverride: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            TemporaryOverride value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TemporaryOverride[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            TemporaryOverride value: 
            Input the item to find.
        """
        pass
    
    
    def FindTemporaryOverrideWithName(self):
        """
        FindTemporaryOverrideWithName -> TemporaryOverride
            
            name: 
            The name of the override.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            TemporaryOverride value: 
            Input the item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string name: 
            Input the name for which to search.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(TemporaryOverride) -> void
            
            TemporaryOverride element: 
            Input the item to remove.
        """
        pass
    
    pass

class ToolPanel(object):
    """
    
    ToolPanel(MenuGroup)
        MenuGroup parent : Input the parent.
    
    
    ToolPanel(MenuGroup, bool)
        MenuGroup parent : Input the parent.
        bool bForFlyout : Input true if the tool panel should have flyouts.
    
    
    ToolPanel(string, MenuGroup)
        string name : Input a name for the tool panel.
        MenuGroup parent : Input the parent.
    
    
    ToolPanel(string, string, string, MenuGroup)
        string name : Input a name for the tool panel.
        string description : Input a description for the tool panel.
        string UID : Input a unique ID.
        MenuGroup parent : Input the parent.
    
    
    ToolPanel(ToolPanel, MenuGroup, int)
        ToolPanel toolpanelIn : Input the object to copy.
        MenuGroup parent : Input the parent.
        int index : Input its array index.
    
    
    """
    def indexOfRowBreak(self):
        """
        indexOfRowBreak -> Integer
            
            int row: 
            Input row index
        """
        pass
    
    
    def indexOfRowStart(self):
        """
        indexOfRowStart -> Integer
            
            int row: 
            Input row index
        """
        pass
    
    
    Parent = None
    
    
    Rows = None
    
    pass

class ToolPanelCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ToolPanel toolpanel: 
            Input the object to add.
        """
        pass
    
    
    def AddToolPanel(self):
        """
        AddToolPanel -> bool
            
            ToolPanel toolpanel: 
            Input the tool panel to append to.
            
            object obj: 
            Input the object to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ToolPanel value: 
            Input the object to check.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ToolPanel[] array: 
            Input the object to be copied.
            
            int index: 
            Input the object acting as the array index.
        """
        pass
    
    
    def FindToolPanelWithAlias(self):
        """
        FindToolPanelWithAlias -> ToolPanel
            
            string toolpanelAlias: 
            Input the alias to search by.
        """
        pass
    
    
    def FindToolPanelWithName(self):
        """
        FindToolPanelWithName -> ToolPanel
            
            string toolpanelName: 
            Input the name of the tool panel.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ToolPanel value: 
            Input a tool panel to seek.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input a zero-based array index.
            
            ToolPanel value: 
            Input an object to add.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string toolpanelName: 
            Input the object name to seek.
        """
        pass
    
    
    def NextName(self):
        """
        NextName -> string
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ToolPanel) -> void
            
            ToolPanel toolpanel: 
            Input the item to remove
        """
        pass
    
    
    AllAliases = None
    
    pass

class ToolPanelNameChangedEventArgs(object):
    """
    
    ToolPanelNameChangedEventArgs
        ToolPanel toolpanel : Input the object to create.
        string oldName : Input the old name.
    """
    OldToolPanelName = None
    
    
    ToolPanelChanged = None
    
    pass

class ToolPanelRef(object):
    """
    
    ToolPanelRef
        ToolPanel tp : Input the tool panel object, which this reference will point to.
        Panel parent : Input the panel object, which contains this reference.
        PanelPosition ps : Input the panel position, whether upper or lower.
    """
    PanelReference = None
    
    
    Parent = None
    
    pass

class ToolTip(object):
    """
    
    ToolTip(Macro)
        Macro parent : Input parent
    
    
    ToolTip(Macro, ToolTip)
        Macro parent : Input parent
        ToolTip that : Input object to copy
    
    
    """
    BasicContent = None
    
    
    CommandName = None
    
    
    EnableHelp = None
    
    
    ExtendedHelpFile = None
    
    
    HasBasicContent = None
    
    
    HasCommandName = None
    
    
    HasEnableHelp = None
    
    
    HasHelpSource = None
    
    
    HasHelpTopic = None
    
    
    HelpSource = None
    
    
    HelpTopic = None
    
    
    Parent = None
    
    pass

class ToolTipContent(object):
    """
    
    """
    SourceKey = None
    
    
    UriSource = None
    
    pass

class Toolbar(object):
    """
    
    Toolbar(MenuGroup)
        MenuGroup parent : Input the parent.
    
    
    Toolbar(string, MenuGroup)
        string name : Input the name of the toolbar.
        MenuGroup parent : Input the parent.
    
    
    Toolbar(Toolbar, MenuGroup, int)
        Toolbar toolbarIn : Input the source to be copied.
        MenuGroup parent : Input the parent.
        int index : Input the index at which to insert new PopMenuItem in parent's collection.
    
    
    """
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    Name = None
    
    
    Parent = None
    
    
    Rows = None
    
    
    ToolbarItems = None
    
    
    ToolbarOrient = None
    
    
    ToolbarVisible = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class ToolbarButton(object):
    """
    
    ToolbarButton(string, string, Toolbar, int)
        string macroId : Input the UID of the MenuMacro to associate with the button.
        string name : Input the name to use as the toolbar button's tool tip, if different from the name of the MenuMacro.
        Toolbar parent : Input the parent.
        int index : Input the index at which to insert new PopMenuItem in parent's collection.
    
    
    ToolbarButton(Toolbar)
        Toolbar parent : Input the parent.
    
    
    ToolbarButton(Toolbar, int)
        Toolbar parent : Input the parent.
        int index : Input the index at which to inserts the button into the parent toolbar.
    
    
    ToolbarButton(ToolbarButton, Toolbar, int)
        ToolbarButton source : Input the toolbar from which to duplicate data.
        Toolbar parent : Input the parent.
        int index : Input the index at which to inserts the button into the parent toolbar.
    
    
    """
    DrawSeparator = None
    
    
    IsRowBreak = None
    
    
    IsSeparator = None
    
    
    Loader = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    Name = None
    
    pass

class ToolbarCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Toolbar toolbar: 
            Input the item to add.
        """
        pass
    
    
    def AddToolbar(self):
        """
        AddToolbar -> bool
            
            Toolbar toolbar: 
            Input the toolbar to add.
            
            object obj: 
            Input the toolbar to insert at beginning of the collection. If obj is null or is not found in the collection, the toolbar is appended to the end.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Toolbar value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Toolbar[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindToolbarWithAlias(self):
        """
        FindToolbarWithAlias -> Toolbar
            
            string toolbarAlias: 
            Input the alias for which to search.
        """
        pass
    
    
    def FindToolbarWithName(self):
        """
        FindToolbarWithName -> Toolbar
            
            string toolbarName: 
            Input the name for which to search.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Toolbar value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            Toolbar value: 
            Input the item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string toolbarName: 
            Input the name for which to search.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(Toolbar) -> void
            
            Toolbar toolbar: 
            Input the item to remove
        """
        pass
    
    
    AllAliases = None
    
    pass

class ToolbarControl(object):
    """
    
    ToolbarControl
        ToolbarControl source : Input the control to duplicate.
        Toolbar parent : Input the parent
        int index : Input the index at which to insert the control into the parent toolbar.
    """
    ControlType = None
    
    
    Loader = None
    
    pass

class ToolbarFlyout(object):
    """
    
    ToolbarFlyout(string, string, string, string, string, bool, Toolbar, int)
        string name : Input the name of the flyout if different from the toolbar. The name will display as a tool tip.
        string uid : Input the unique ID for the toolbar. If the given ID is already in use, a new one will be generated.
        string refToolbar : Input the toolbar to reference as a flyout.
        string smlImage : Input the image to use for the toolbar when it is set to use small images.
        string lgImage : Input the image to use for the toolbar when it is set to use large images.
        bool bToolbarOwnIcon : If set to true, the toolbar uses its own images.
        Toolbar parent : Input the parent.
        int index : Input the index in the collection at which to insert flyout.
    
    
    ToolbarFlyout(string, string, string, string, Toolbar, int)
        string name : Input the name of the flyout if different from the toolbar. The name will display as a tool tip.
        string description : Input the description of the flyout. This will display on the status bar.
        string menuGroup : Input the name of the menu group of the target toolbar.
        string searchAlias : Input the alias of the target toolbar.
        Toolbar parent : Input the parent.
        int index : Input the index in the collection at which to insert flyout.
    
    
    ToolbarFlyout(Toolbar, int)
        Toolbar parent : Input the parent.
        int index : Input the index in the collection at which to insert flyout.
    
    
    ToolbarFlyout(ToolbarFlyout, Toolbar, int)
        ToolbarFlyout flyIn : Input the ToolbarFlyout to clone.
        Toolbar parent : Input the parent.
        int index : Input the index in the collection at which to insert flyout.
    
    
    """
    Description = None
    
    
    FlyoutName = None
    
    
    IsCircular = None
    
    
    LargeImage = None
    
    
    Loader = None
    
    
    MenuGroup = None
    
    
    SmallImage = None
    
    
    ToolbarReference = None
    
    
    UnqualifiedAlias = None
    
    
    UseOwnIcon = None
    
    pass

class ToolbarItemBase(object):
    """
    
    """
    Parent = None
    
    pass

class ToolbarItemCollection(object):
    """
    
    ToolbarItemCollection
        CustomizationElement owner : Input owner of this collection
    """
    def Add(self):
        """
        Add -> void
            
            ToolbarItemBase toolbarItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ToolbarItemBase value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ToolbarItemBase[] array: 
            Input the target array
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ToolbarItemBase value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ToolbarItemBase value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ToolbarItemBase) -> void
            
            ToolbarItemBase element: 
            Input the item to remove
        """
        pass
    
    pass

class ToolbarNameChangedEventArgs(object):
    """
    
    ToolbarNameChangedEventArgs
        Toolbar toolbar : Input the modified toolbar.
        string oldName : Input the old name.
    """
    OldToolbarName = None
    
    
    ToolbarChanged = None
    
    pass

class ToolbarOrient():
    bottom = 3
    floating = 1
    left = 4
    right = 5
    top = 2

class ToolbarVisible():
    hide = 0
    show = 1

class UpdateType():
    New = None
    Modified = None

class Util(object):
    """
    
    """
    def IsEmpty(self):
        """
        IsEmpty -> bool
            
            string s: 
            Input the object which is to be tested.
        """
        pass
    
    
    def IsEqualNoCase(self):
        """
        IsEqualNoCase -> bool
            
            string s1: 
            Input System.String object, the first string to compare.
            
            string s2: 
            Input System.String object, the second string to compare.
        """
        pass
    
    pass

class Version():
    CurrentVersion = 15
    TwoThousandEight = 2
    TwoThousandEighteen = 12
    TwoThousandEleven = 5
    TwoThousandFifteen = 9
    TwoThousandFourteen = 8
    TwoThousandNine = 3
    TwoThousandNineteen = 13
    TwoThousandSeven = 1
    TwoThousandSeventeen = 11
    TwoThousandSix = 0
    TwoThousandSixteen = 10
    TwoThousandTen = 4
    TwoThousandThirteen = 7
    TwoThousandTwelve = 6
    TwoThousandTwenty = 14
    Unknown = 0x10

class VersionableElement(object):
    """
    
    """
    def addInternalUseProperties(self):
        """
        addInternalUseProperties -> void
        
        """
        pass
    
    
    def FireModifiedEvent(self):
        """
        FireModifiedEvent -> void
        
        """
        pass
    
    
    def SetRevision(self):
        """
        SetRevision -> void
        
        """
        pass
    
    
    def UserModified(self):
        """
        UserModified -> bool
        
        """
        pass
    
    
    ModifiedRevision = None
    
    pass

class WSRibbonPanelSourceReference(object):
    """
    
    WSRibbonPanelSourceReference
        WSRibbonTabSourceReference parent : Input the parent
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            WSRibbonPanelSourceReference item: 
            Input the WSRibbonPanelSourceReference from which to copy the data.
        """
        pass
    
    
    def Create(self):
        """
        Create -> WSRibbonPanelSourceReference
            
            RibbonPanelSourceReference panelSourceref: 
            Input the RibbonPanelSourceReference from which the item is to be created.
        """
        pass
    
    
    def FindPanelSource(self):
        """
        FindPanelSource -> RibbonPanelSource
            
            Collection<CustomizationSection> cuiFiles: 
            CUI files to be searched.
        """
        pass
    
    
    FloatingGroup = None
    
    
    FloatingOrder = None
    
    
    FloatingOrientation = None
    
    
    Orientation = None
    
    
    PanelId = None
    
    
    Show = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class WSRibbonRoot(object):
    """
    
    """
    def Clone(self):
        """
        Clone -> WSRibbonRoot
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            WSRibbonRoot item: 
            Input the WSRibbonRoot from which to copy the data.
        """
        pass
    
    
    def FindTabReference(self):
        """
        FindTabReference -> WSRibbonTabSourceReference
            
            string sMenuGroupName: 
            Input the name of the menu group.
            
            string id: 
            Input the string Id of the WSRibbonTabSourceReference to find.
        """
        pass
    
    
    AutoHideMode = None
    
    
    LockMode = None
    
    
    ShowPanelTitleInHorizontalOrientation = None
    
    
    ShowPanelTitleInVerticalOrientation = None
    
    
    WorkspaceTabs = None
    
    pass

class WSRibbonTabSourceReference(object):
    """
    
    WSRibbonTabSourceReference
        WSRibbonRoot parent : Input the parent WSRibbonRoot.
    """
    TabId = None
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            WSRibbonTabSourceReference item: 
            Input the WSRibbonTabSourceReference from which to copy the data.
        """
        pass
    
    
    def Create(self):
        """
        Create -> WSRibbonTabSourceReference
            
            RibbonTabSource tabSource: 
            input the RibbonTabSource from which to create the WSRibbonTabSourceReference object.
        """
        pass
    
    
    def Find(self):
        """
        Find -> WSRibbonPanelSourceReference
            
            string panelId: 
            Input the string Id of the WSRibbonPanelSourceReference to find.
        """
        pass
    
    
    def FindTabSource(self):
        """
        FindTabSource -> RibbonTabSource
            
            Collection<CustomizationSection> cuiFiles: 
            CUI files to be searched.
        """
        pass
    
    
    IsActive = None
    
    
    MenuGroup = None
    
    
    Panels = None
    
    
    Show = None
    
    pass

class WSToolbarChangedEventArgs(object):
    """
    
    WSToolbarChangedEventArgs
        WorkspaceToolbar wstoolbar : Input the workspace toolbar object.
    """
    WorkspaceToolbarChanged = None
    
    pass

class Workspace(object):
    """
    
    Workspace
        CustomizationSection parent : Input the parent to set.
        Workspace source : Input the object to copy from.
    """
    DefaultWorkspace = None
    
    
    Description = None
    
    
    WorkspaceRibbonRoot = None
    
    
    DockableWindows = None
    
    
    LayoutModelTabs = None
    
    
    Name = None
    
    
    Parent = None
    
    
    ScreenMenus = None
    
    
    Script = None
    
    
    ScrollBars = None
    
    
    StatusBar = None
    
    
    StartOn = None
    
    
    WorkspacePopMenus = None
    
    
    WorkspaceToolbars = None
    
    pass

class WorkspaceCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Workspace workspace: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Workspace value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Workspace[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Workspace value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            Workspace value: 
            Input the item to insert.
        """
        pass
    
    
    def SetDefaultWorkspaceByName(self):
        """
        SetDefaultWorkspaceByName -> bool
            
            workspaceName: 
            The name of a workspace to set as the default in the menu.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove.
        Remove(Workspace) -> void
            
            Workspace Workspace: 
            Input the item to remove.
        """
        pass
    
    
    def SetDefaultWorkspace(self):
        """
        SetDefaultWorkspace -> bool
            
            string elementId: 
            Input the ID of the workspace.
        """
        pass
    
    
    Owner = None
    
    pass

class WorkspaceDockableWindow(object):
    """
    
    WorkspaceDockableWindow(Workspace, string)
        Workspace parent : Input the parent workspace of this dockable window.
        string className : Input the GUID of the class that is stored in the registry to identify this dockable window.
    
    
    WorkspaceDockableWindow(Workspace, string, string, string)
        Workspace parent : Input the parent workspace of this dockable window.
        string className : Input the GUID of the class that is stored in the registry to identify this dockable window.
        string name : Input the name of this dockable window.
        string command : Input the command associated with this dockable window in order to display it.
    
    
    WorkspaceDockableWindow(Workspace, WorkspaceDockableWindow)
        Workspace parent : Input the parent workspace of this dockable window.
        WorkspaceDockableWindow from : Input the dockable window whose properties are to be applied to this window.
    
    
    """
    AllowDock = None
    
    
    AutoHide = None
    
    
    ClassName = None
    
    
    DefaultGroup = None
    
    
    Display = None
    
    
    DockColumn = None
    
    
    DockFloat = None
    
    
    DockHeight = None
    
    
    DockRow = None
    
    
    DockWidth = None
    
    
    Height = None
    
    
    Name = None
    
    
    Orientation = None
    
    
    Parent = None
    
    
    TransparencyAmount = None
    
    
    UseTransparency = None
    
    
    Width = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class WorkspaceDockableWindowCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WorkspaceDockableWindow workspaceDockableWindow: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WorkspaceDockableWindow value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WorkspaceDockableWindow[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def FindDockableWindow(self):
        """
        FindDockableWindow -> WorkspaceDockableWindow
            
            string windowName: 
            Input the name to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WorkspaceDockableWindow value: 
            Input the item to find.
        """
        pass
    
    
    def IndexOfClassName(self):
        """
        IndexOfClassName -> Integer
            
            string className: 
            Input a GUID that is read from the registry and uniquely identifies a dockable window.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            WorkspaceDockableWindow value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(WorkspaceDockableWindow) -> void
            
            WorkspaceDockableWindow workspaceDockableWindow: 
            Input the item to remove.
        """
        pass
    
    pass

class WorkspacePopMenu(object):
    """
    
    WorkspacePopMenu(Workspace, PopMenu)
        Workspace parent : Input the parent workspace.
        PopMenu popMenu : Input the pop menu of this object.
    
    
    WorkspacePopMenu(Workspace, WorkspacePopMenu)
        Workspace parent : Input the parent workspace.
        WorkspacePopMenu from : Input the pop menu that this object represents.
    
    
    """
    Display = None
    
    
    MenuGroup = None
    
    
    PopMenuID = None
    
    
    Parent = None
    
    pass

class WorkspacePopMenuCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WorkspacePopMenu workspacePopMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WorkspacePopMenu element: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WorkspacePopMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindWorkspacePopMenu(self):
        """
        FindWorkspacePopMenu -> WorkspacePopMenu
            
            string popMenuElementId: 
            Input the pop menu to be found.
            
            string MenuGroup: 
            Input the menu group of given pop menu.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WorkspacePopMenu element: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            WorkspacePopMenu element: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(WorkspacePopMenu) -> void
            
            WorkspacePopMenu workspacePopMenu: 
            Input the item to remove.
        """
        pass
    
    pass

class WorkspaceQuickAccessToolbar(object):
    """
    
    WorkspaceQuickAccessToolbar(Workspace, QuickAccessToolbar)
        Workspace parent : Parent Workspace.
        QuickAccessToolbar qatToolbar : Toolbar.
    
    
    WorkspaceQuickAccessToolbar(Workspace, WorkspaceQuickAccessToolbar)
        Workspace parent : Sets the parent.
        WorkspaceQuickAccessToolbar fromWQAT : Source to copy from.
    
    
    """
    MenuGroup = None
    
    
    Parent = None
    
    
    ToolbarId = None
    
    pass

class WorkspaceRibbonPanelCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WSRibbonPanelSourceReference wsPanel: 
            Input the WSRibbonPanelSourceReference to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WSRibbonPanelSourceReference value: 
            Input the WSRibbonPanelSourceReference to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WSRibbonPanelSourceReference[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index of the target array where the copy begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WSRibbonPanelSourceReference value: 
            Input the WSRibbonPanelSourceReference to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index where the insert is to take place.
            
            WSRibbonPanelSourceReference value: 
            Input the WSRibbonPanelSourceReference to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(WSRibbonPanelSourceReference) -> void
            
            WSRibbonPanelSourceReference panel: 
            Input the WSRibbonPanelSourceReference to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of the WSRibbonPanelSourceReference to remove.
        """
        pass
    
    pass

class WorkspaceRibbonTabCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WSRibbonTabSourceReference wsTab: 
            Item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WSRibbonTabSourceReference value: 
            Item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WSRibbonTabSourceReference[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WSRibbonTabSourceReference value: 
            Item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Zero based index.
            
            WSRibbonTabSourceReference value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove(WSRibbonTabSourceReference) -> void
            
            WSRibbonTabSourceReference wsTab: 
            Item to remove.
        Remove(int) -> void
            
            int index: 
            Index of item to remove.
        """
        pass
    
    pass

class WorkspaceToolbar(object):
    """
    
    WorkspaceToolbar(Workspace, Toolbar)
        Workspace parent : Input the parent workspace.
        Toolbar toolbar : Input the containment object.
    
    
    WorkspaceToolbar(Workspace, WorkspaceToolbar)
        Workspace parent : Input the parent workspace.
        WorkspaceToolbar from : Input the source from which to copy.
    
    
    """
    Display = None
    
    
    DockColumn = None
    
    
    DockRow = None
    
    
    MenuGroup = None
    
    
    Parent = None
    
    
    Rows = None
    
    
    ToolbarId = None
    
    
    ToolbarOrient = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class WorkspaceToolbarCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WorkspaceToolbar workspaceToolbar: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WorkspaceToolbar value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WorkspaceToolbar[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def FindWorkspaceToolbar(self):
        """
        FindWorkspaceToolbar -> WorkspaceToolbar
            
            string toolbarElementId: 
            Input the element ID of toolbar to be found.
            
            string menuGroup: 
            Input the menu group of toolbar to be found.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WorkspaceToolbar value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            WorkspaceToolbar value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(WorkspaceToolbar) -> void
            
            WorkspaceToolbar workspaceToolbar: 
            Input the item to remove.
        """
        pass
    
    pass

class YesNoIgnoreToggle():
    ignore = 2
    no = 0
    yes = 1