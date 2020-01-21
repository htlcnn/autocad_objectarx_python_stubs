class ActiveTaskDialog(IWin32Window):
    """
    
    """
    Handle Field = None
    
    
    def ClickButton(self):
        """
        ClickButton -> bool
            
            int buttonId: 
            Input ID of the clicked button
        """
        pass
    
    
    def ClickRadioButton(self):
        """
        ClickRadioButton -> void
            
            int buttonId: 
            Input ID of the clicked radio button
        """
        pass
    
    
    def ClickVerification(self):
        """
        ClickVerification -> void
            
            bool checkedState: 
            Input true to check the verification check box, false to uncheck it
            
            bool setKeyboardFocusToCheckBox: 
            Input true to set the keyboard focus to check box
        """
        pass
    
    
    def EnableButton(self):
        """
        EnableButton -> void
            
            int buttonId: 
            Input ID of the button to enable or disable
            
            bool enable: 
            Input true to enable the button, false to disable the button
        """
        pass
    
    
    def EnableRadioButton(self):
        """
        EnableRadioButton -> void
            
            int buttonId: 
            Input ID of the button to enable or disable
            
            bool enable: 
            Input true to enable the button, false to disable the button
        """
        pass
    
    
    def SetButtonElevationRequiredState(self):
        """
        SetButtonElevationRequiredState -> void
            
            int buttonId: 
            Input new button ID
            
            bool elevationRequired: 
            Input true to elevate the button
        """
        pass
    
    
    def SetContentText(self):
        """
        SetContentText -> bool
            
            string content: 
            Input new content text
        """
        pass
    
    
    def SetExpandedText(self):
        """
        SetExpandedText -> bool
            
            sText: 
            Input expanded text
        """
        pass
    
    
    def SetFooterText(self):
        """
        SetFooterText -> bool
            
            string footer: 
            Input new footer text
        """
        pass
    
    
    def SetMainInstruction(self):
        """
        SetMainInstruction -> bool
            
            string mainInstruction: 
            Input new main instruction string
        """
        pass
    
    
    def SetMarqueeProgressBar(self):
        """
        SetMarqueeProgressBar -> bool
            
            bool marquee: 
            Input true to set the progress bar style to the marquee progress bar, false to set the progress bar style to a regular progress bar
        """
        pass
    
    
    def SetProgressBarMarquee(self):
        """
        SetProgressBarMarquee -> void
            
            bool startMarquee: 
            Input true to start the marquee progress bar
            
            uint speed: 
            Input the speed of the marquee
        """
        pass
    
    
    def SetProgressBarPosition(self):
        """
        SetProgressBarPosition -> Integer
            
            int newPosition: 
            Input the new position of the progress bar
        """
        pass
    
    
    def SetProgressBarRange(self):
        """
        SetProgressBarRange -> bool
            
            short minRange: 
            Input the minimum range
            
            short maxRange: 
            Input the maximum range
        """
        pass
    
    
    def SetProgressBarState(self):
        """
        SetProgressBarState -> bool
            
            ProgressBarState newState: 
            Input the new state
        """
        pass
    
    
    def UpdateContentText(self):
        """
        UpdateContentText -> void
            
            string content: 
            Input new context string
            
            Exceptions: 
            Description
            
            System.InvalidOperationException: 
            The task dialog doesn't have ContentText to update. Use SetContentText instead
        """
        pass
    
    
    def UpdateExpandedText(self):
        """
        UpdateExpandedText -> void
            
            string text: 
            Input the new expanded text.
            
            Exceptions: 
            Description
            
            System.InvalidOperationException: 
            The task dialog doesn't have ExpandedText to update. Use SetExpandedText instead
        """
        pass
    
    
    def UpdateFooterIcon(self):
        """
        UpdateFooterIcon(Icon) -> void
            
            Icon icon: 
            Input a new footer icon
        UpdateFooterIcon(TaskDialogIcon) -> void
            
            TaskDialogIcon icon: 
            Input a new footer icon
        """
        pass
    
    
    def UpdateFooterText(self):
        """
        UpdateFooterText -> void
            
            string footer: 
            Input new footer text
            
            Exceptions: 
            Description
            
            System.InvalidOperationException: 
            The task dialog doesn't have FooterText to update. Use SetFooterText instead
        """
        pass
    
    
    def UpdateMainIcon(self):
        """
        UpdateMainIcon(Icon) -> void
            
            Icon icon: 
            Input new icon to set as main icon
        UpdateMainIcon(TaskDialogIcon) -> void
            
            TaskDialogIcon icon: 
            Input new icon to set as main icon
        """
        pass
    
    
    def UpdateMainInstruction(self):
        """
        UpdateMainInstruction -> void
            
            string mainInstruction: 
            Input new main instruction text
            
            Exceptions: 
            Description
            
            System.InvalidOperationException: 
            The task dialog doesn't have MainInstruction to update. Use SetMainInstruction instead
        """
        pass
    
    pass

class ApplicationMenu(INotifyPropertyChanged):
    """
    
    """
    DocumentGroupByItems = None
    
    
    IsOpen = None
    
    
    DocumentGroupByItems = None
    
    
    IsOpen = None
    
    
    IsPinned = None
    
    
    MenuContent = None
    
    pass

class ApplicationMenuItem(RibbonMenuItem):
    """
    
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
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    )
    """
    BottomListView = None
    
    
    GroupNameInternal = None
    
    
    IsPinable = None
    
    
    IsPinned = None
    
    
    IsSplit = None
    
    
    MaxDescriptionLines = None
    
    
    PinOrder = None
    
    
    SplitKeyTip = None
    
    
    TopListView = None
    
    pass

class ApplicationMenuItemCollection(ObservableCollection<ApplicationMenuItem>):
    """
    
    """

    pass

class CollectionsExtensions(public static class CollectionsExtensions):
    """
    
    """
    def ToReverse(self):
        """
        ToReverse -> Comparer<T>
        
        """
        pass
    
    
    def TryGetValueOrDefault(self):
        """
        TryGetValueOrDefault(this IDictionary<TKey, TValue>, TKey) -> TValue
        
        TryGetValueOrDefault(this IDictionary<TKey, TValue>, TKey, TValue) -> TValue
        
        """
        pass
    
    pass

class ComponentManager(public static class ComponentManager):
    """
    
    """
    ApplicationMenu = None
    
    
    AreItemsTopJustifiedInVerticalRibbon = None
    
    
    CanLargeButtonLoseTextInVerticalRibbon = None
    
    
    IsCIPEnabled = None
    
    
    IsDialogLauncherButtonWide = None
    
    
    IsRowPanelPaddingEnabled = None
    
    
    IsStandardButtonBorderVisible = None
    
    
    PropogateCreateInfoCenterExceptions = None
    
    
    QuickAccessToolBar = None
    
    
    UseOriginalImageSize = None
    
    
    FontSettings Field = None
    
    
    IsDialogLauncherButtonWide = None
    
    pass

class DisplayDeviceInfo(public sealed class DisplayDeviceInfo):
    """
    
    """
    Primary Field = None
    
    
    Dpi = None
    
    
    Dpi2D = None
    
    
    Scale = None
    
    
    Scale2D = None
    
    pass

class DocumentGroupByItems():
    All = 15
    Date = 2
    None = 0
    Ordered = 1
    Platform = 0x10
    Size = 4
    Type = 8

class DocumentItem(RibbonCommandItem):
    """
    
    """
    DocumentItemToolTipAttributes = None
    
    
    Platform = None
    
    
    PreviewImage = None
    
    pass

class DocumentItemCollection(ObservableCollection<DocumentItem>):
    """
    
    """

    pass

class DocumentItemToolTipAttributes():
    All = 15
    CurrentlyOpenBy = 8
    DateModified = 1
    LastSavedBy = 4
    None = 0
    VersionInfo = 2

class DoubleFuzzyComparer(DoubleFuzzyComparer<double>):
    """
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    F
    
    u
    
    z
    
    z
    
    y
    
    C
    
    o
    
    m
    
    p
    
    a
    
    r
    
    e
    
    r
    
    (
    
    )
    """
    def ToDouble(self):
        """
        ToDouble -> double
        
        """
        pass
    
    pass

class DpiValue(public struct DpiValue {
  public static DpiValue Standard = > <Standard>k__BackingField;
  public static DpiValue System = > DisplayDeviceInfo.Primary.Dpi;
}):
    """
    
    """
    Standard Field = None
    
    
    System Field = None
    
    
    def FromPercent(self):
        """
        FromPercent -> DpiValue
        
        """
        pass
    
    
    def IsValid(self):
        """
        IsValid() -> bool
        
        IsValid(DpiValueComparer) -> bool
        
        """
        pass
    
    
    def ToDouble(self):
        """
        ToDouble -> double
        
        """
        pass
    
    
    def ToPercent(self):
        """
        ToPercent -> double
        
        """
        pass
    
    
    def ToPercentInt32(self):
        """
        ToPercentInt32 -> Integer
        
        """
        pass
    
    
    def ToScaleFactor(self):
        """
        ToScaleFactor() -> ScaleFactor
        
        ToScaleFactor(DpiValue) -> ScaleFactor
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString -> string
        
        """
        pass
    
    pass

class DpiValue2D(public struct DpiValue2D {
  public DpiValue X = > this.<X>k__BackingField;
  public DpiValue Y = > this.<Y>k__BackingField;
  public static DpiValue2D Standard = > <Standard>k__BackingField;
  public static DpiValue2D System = > DisplayDeviceInfo.Primary.Dpi2D;
}):
    """
    
    D
    
    p
    
    i
    
    V
    
    a
    
    l
    
    u
    
    e
    
    2
    
    D
    
    (
    
    D
    
    p
    
    i
    
    V
    
    a
    
    l
    
    u
    
    e
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    p
    
    i
    
    V
    
    a
    
    l
    
    u
    
    e
    
    2
    
    D
    
    (
    
    D
    
    p
    
    i
    
    V
    
    a
    
    l
    
    u
    
    e
    
    ,
    
     
    
    D
    
    p
    
    i
    
    V
    
    a
    
    l
    
    u
    
    e
    
    )
    
    (
    
    )
    """
    Standard Field = None
    
    
    System Field = None
    
    
    X Field = None
    
    
    Y Field = None
    
    
    def IsValid(self):
        """
        IsValid() -> bool
        
        IsValid(DpiValueComparer) -> bool
        
        """
        pass
    
    
    def ToDpiValue(self):
        """
        ToDpiValue() -> DpiValue
        
        ToDpiValue(DpiValueComparer) -> DpiValue
        
        """
        pass
    
    
    def ToScaleFactor(self):
        """
        ToScaleFactor() -> ScaleFactor2D
        
        ToScaleFactor(DpiValue2D) -> ScaleFactor2D
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString -> string
        
        """
        pass
    
    pass

class DpiValueComparer(DoubleFuzzyComparer<DpiValue>):
    """
    
    D
    
    p
    
    i
    
    V
    
    a
    
    l
    
    u
    
    e
    
    C
    
    o
    
    m
    
    p
    
    a
    
    r
    
    e
    
    r
    
    (
    
    )
    """
    Default Field = None
    
    
    def IsStandard(self):
        """
        IsStandard -> bool
        
        """
        pass
    
    
    def IsValid(self):
        """
        IsValid -> bool
        
        """
        pass
    
    
    def ToDouble(self):
        """
        ToDouble -> double
        
        """
        pass
    
    pass

class GalleryDisplayMode():
    Window
    ComboBox
    LargeButton
    StandardButton

class MenuContent(public class MenuContent):
    """
    
    """
    Items = None
    
    pass

class PreviewToolTip(RibbonToolTipBase):
    """
    
    """
    IsProgressive = None
    
    
    Items = None
    
    pass

class ProgressBarSource(RibbonCommandItem):
    """
    
    """

    pass

class ProgressBarState():
    None
    Normal
    Error
    Paused

class PropertyValuePair(INotifyPropertyChanged):
    """
    
    """
     = None
    
    
    Value = None
    
    pass

class PropertyValuePairCollection(ObservableCollection<PropertyValuePair>):
    """
    
    """

    pass

class RibbonButton(RibbonCommandItem, IRibbonTextProperties):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source button to copy from
        """
        pass
    
    
    Orientation = None
    
    pass

class RibbonChecklistButton(RibbonListButton):
    """
    
    """

    pass

class RibbonCombo(RibbonList, IResizableWidget, IRibbonTextProperties):
    """
    
    """
    IsVirtualizing = None
    
    
    MenuItems Field = None
    
    
    Orientation Field = None
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    CommandHandler = None
    
    
    EditableText = None
    
    
    IsEditable = None
    
    
    IsVirtualizing = None
    
    pass

class RibbonCommandItem(RibbonItem):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    IsCheckable = None
    
    
    IsChecked = None
    
    pass

class RibbonCommandItemCollection(ObservableCollection<RibbonCommandItem>):
    """
    
    """

    pass

class RibbonControl(Control, INotifyPropertyChanged, ICommandTarget, IPersistentObjectSource):
    """
    
    """
    def HideContextualTab(self):
        """
        HideContextualTab -> void
            
            RibbonTab tab: 
            Contextual tab to hide.
        """
        pass
    
    
    def ShowContextualTab(self):
        """
        ShowContextualTab -> void
            
            RibbonTab tab: 
            Tab to show as a contextual tab.
            
            bool mergedTab: 
            Value indicating whether the tab should be shown as a merged contextual tab. If mergedTab is true the tab is shown as a merged contextual tab, which merges the panels of this tab to the panels of all the tabs; if false the tab is added to the list of tabs and has to be activated like any other tab.
            
            bool activate: 
            Value indicating whether the tab needs to be activated. If activate is true the contextual tab is displayed and also set as the active tab; if false the contextual tab is displayed but not set as the active tab. This argument is used only if mergedTab is false.
        """
        pass
    
    
    ActiveTab = None
    
    
    AutoHideMode = None
    
    
    ApplicationMenuButtonBackgroundBrush = None
    
    
    ApplicationMenuButtonBackgroundImage = None
    
    
    ApplicationMenuButtonDisableBackgroundBrush = None
    
    
    ApplicationMenuButtonDisableImage = None
    
    
    ApplicationMenuButtonHoverBackgroundBrush = None
    
    
    ApplicationMenuButtonHoverImage = None
    
    
    ApplicationMenuButtonPressBackgroundBrush = None
    
    
    ApplicationMenuButtonPressImage = None
    
    
    ApplicationMenuButtonText = None
    
    
    ApplicationMenuButtonToolTip = None
    
    
    IsApplicationMenuButtonDisplayedInRibbon = None
    
    
    IsModernizedUI = None
    
    
    OffsetTabs = None
    
    
    RibbonOrientation = None
    
    
    Tabs = None
    
    pass

class RibbonForm(RibbonItem):
    """
    
    """

    pass

class RibbonGallery(RibbonCombo):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    DisplayMode = None
    
    pass

class RibbonHwnd(RibbonItem):
    """
    
    """

    pass

class RibbonImageSize():
    Standard
    Large

class RibbonItem(ICloneable, IRibbonContentUid, IRibbonAutomation, IRibbonHighlightable, INotifyPropertyChanged, IWeakEventListener):
    """
    
    """
    Highlight = None
    
    
    IsInitialized Field = None
    
    
    def Clone(self):
        """
        Clone -> RibbonItem
        
        """
        pass
    
    
    def ResolveToolTip(self):
        """
        ResolveToolTip -> void
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    Description = None
    
    
    GroupName = None
    
    
    Highlight = None
    
    
    Id = None
    
    
    Image = None
    
    
    IsEnabled = None
    
    
    IsToolTipEnabled = None
    
    
    IsVisible = None
    
    
    KeyTip = None
    
    
    LargeImage = None
    
    
    MinWidth = None
    
    
    Name = None
    
    
    ShowImage = None
    
    
    ShowText = None
    
    
    Size = None
    
    
    Tag = None
    
    
    Text = None
    
    
    ToolTip = None
    
    
    Width = None
    
    pass

class RibbonItemCollection(RibbonObservableCollection<RibbonItem>, ICloneable):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonItemCollection
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItemCollection source: 
            Input source collection to copy from
        """
        pass
    
    pass

class RibbonItemControl(RibbonItemControlBase, IRibbonTextProperties):
    """
    
    """

    pass

class RibbonItemControlBase(ContentControl):
    """
    
    """

    pass

class RibbonItemEnumerator(IEnumerator, IDisposable):
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

class RibbonItemEventArgs(EventArgs):
    """
    
    """
    Item = None
    
    pass

class RibbonItemResizeStyles():
    ChangeSize = 1
    Collapse = 0x10
    HideText = 2
    NoResize = 0
    ResizeWidth = 4

class RibbonItemSize():
    Standard
    Large

class RibbonItemToolTipEventArgs(EventArgs):
    """
    
    """
    IsFirstTime = None
    
    
    Item = None
    
    pass

class RibbonLabel(RibbonItem, IRibbonTextProperties):
    """
    
    """
    Orientation Field = None
    
    pass

class RibbonList(RibbonItem):
    """
    
    """
    Items Field = None
    
    
    Current = None
    
    
    DropDownWidth = None
    
    
    IsGrouping = None
    
    
    ItemTemplate = None
    
    
    MaxDropDownHeight = None
    
    pass

class RibbonListButton(RibbonButton):
    """
    
    """
    HighlightDropDown = None
    
    
    Items Field = None
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source button to copy from
        """
        pass
    
    
    Current = None
    
    
    HighlightDropDown = None
    
    
    IsGrouping = None
    
    
    IsSplit = None
    
    
    IsSynchronizedWithCurrentItem = None
    
    pass

class RibbonMenuButton(RibbonListButton):
    """
    
    """

    pass

class RibbonMenuItem(RibbonCommandItem):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    pass

class RibbonPanel(ICloneable, IRibbonContentUid, IRibbonAutomation, INotifyPropertyChanged):
    """
    
    """
    def FindItem(self):
        """
        FindItem -> RibbonItem
            
            sId: 
            Id of the ribbon item to find.
        """
        pass
    
    
    FloatingOrientation = None
    
    
    HighlightPanelTitleBar = None
    
    
    HighlightWhenCollapsed = None
    
    
    Id = None
    
    
    IsEnabled = None
    
    
    IsVisible = None
    
    
    Source = None
    
    pass

class RibbonPanelBreak(RibbonItem):
    """
    
    """
    SupportedSubPanel Field = None
    
    pass

class RibbonPanelCollection(RibbonObservableCollection<RibbonPanel>):
    """
    
    """

    pass

class RibbonPanelSource(ICloneable, IRibbonContentUid, IRibbonAutomation, INotifyPropertyChanged):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonPanelSource
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonPanelSource source: 
            Source object to copy from.
        """
        pass
    
    
    def FindItem(self):
        """
        FindItem -> RibbonItem
            
            sId: 
            Id of the ribbon item to find.
        """
        pass
    
    
    Description = None
    
    
    DialogLauncher = None
    
    
    Id = None
    
    
    KeyTip = None
    
    
    Name = None
    
    
    Tag = None
    
    
    Title = None
    
    pass

class RibbonPanelSourceCollection(RibbonObservableCollection<RibbonPanelSource>, ICloneable):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonPanelSourceCollection
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonPanelSourceCollection source: 
            Source collection to copy from.
        """
        pass
    
    
    def Find(self):
        """
        Find -> RibbonPanelSource
            
            string id: 
            Id of the panel source to find.
        """
        pass
    
    pass

class RibbonPropertyChangedEventArgs(EventArgs):
    """
    
    """

    pass

class RibbonPropertyChangingEventArgs(EventArgs):
    """
    
    """

    pass

class RibbonRadioButtonGroup(RibbonListButton):
    """
    
    """

    pass

class RibbonRowBreak(RibbonItem):
    """
    
    """
    SupportedSubPanel Field = None
    
    pass

class RibbonRowPanel(RibbonItem):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Source item to copy from.
        """
        pass
    
    
    Items = None
    
    pass

class RibbonSeparator(RibbonItem):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    SeparatorStyle = None
    
    pass

class RibbonSeparatorStyle():
    Line = 0
    None = 0
    Spacer = 1

class RibbonSpinner(RibbonItem, IResizableWidget):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    Change = None
    
    
    IsEditable = None
    
    
    Maximum = None
    
    
    Minimum = None
    
    
    Value = None
    
    pass

class RibbonSplitButton(RibbonListButton):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source button to copy from
        """
        pass
    
    
    ListImageSize = None
    
    
    ListStyle = None
    
    pass

class RibbonSplitButtonListStyle():
    Icon
    List
    Descriptive

class RibbonTab(ICloneable, IRibbonContentUid, INotifyPropertyChanged, IRibbonHighlightable):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonTab
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonTab source: 
            Source tab to copy from.
        """
        pass
    
    
    def FindItem(self):
        """
        FindItem(string) -> RibbonItem
            
            sId: 
            Id of the ribbon item to find.
        FindItem(string, out RibbonPanel) -> RibbonItem
            
            out RibbonPanel parentPanel: 
            Out parameter to store the panel which contains the found item.
            
            sId: 
            Id of the ribbon item to find.
        """
        pass
    
    
    def FindPanel(self):
        """
        FindPanel -> RibbonPanel
            
            sId: 
            Id of the panel to find.
        """
        pass
    
    
    Highlight = None
    
    
    Description = None
    
    
    Id = None
    
    
    KeyTip = None
    
    
    Name = None
    
    
    IsActive = None
    
    
    Tag = None
    
    
    IsVisible = None
    
    
    Title = None
    
    pass

class RibbonTabCollection(RibbonObservableCollection<RibbonTab>):
    """
    
    """

    pass

class RibbonTextBox(RibbonItem, IResizableWidget, IRibbonTextProperties):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input source item to copy from
        """
        pass
    
    
    AcceptTextOnLostFocus = None
    
    
    CommandHandler = None
    
    
    ImageLocation = None
    
    
    InvokesCommand = None
    
    
    IsEmptyTextValid = None
    
    
    Prompt = None
    
    
    SelectTextOnFocus = None
    
    
    ShowImageAsButton = None
    
    
    Value = None
    
    pass

class RibbonTextBoxImageLocation():
    Left
    InsideLeft
    InsideRight

class RibbonToggleButton(RibbonButton):
    """
    
    """

    pass

class RibbonToolTip(RibbonToolTipBase):
    """
    
    """
    Command = None
    
    
    ExpandedContent = None
    
    
    ExpandedImage = None
    
    
    IsProgressive = None
    
    
    Mouse = None
    
    
    Shortcut = None
    
    pass

class RibbonToolTipBase(INotifyPropertyChanged):
    """
    
    """
    Content = None
    
    
    CustomContent = None
    
    
    HelpSource = None
    
    
    HelpTopic = None
    
    
    Image = None
    
    
    IsHelpEnabled = None
    
    
    Title = None
    
    pass

class TaskDialog(public class TaskDialog):
    """
    
    """
    def Show(self):
        """
        Show() -> Integer
        
        Show(IWin32Window) -> Integer
            
            IWin32Window owner: 
            The handle of the owner window that is expected to show the task dialog.
        Show(IntPtr) -> Integer
            
            IntPtr window: 
            The handle of the owner window that is expected to show the task dialog.
        Show(IntPtr, out bool, out int) -> Integer
            
            IntPtr window: 
            The handle of the owner window that is expected to show the task dialog.
            
            out bool verificationMarkChecked: 
            The flag indicates whether verification is checked.
            
            out int radioButtonResult: 
            Output the integer value of the default result of radio button The int value of the default result of the radio button.
            
            hwndOwner: 
            Input the handle of the owner window which is expected to show the task dialog
            
            verificationFlagChecked: 
            Output the status of the verification flag
        """
        pass
    
    
    AllowDialogCancellation = None
    
    
    Callback = None
    
    
    CallbackData = None
    
    
    CanBeMinimized = None
    
    
    CollapsedControlText = None
    
    
    CommonButtons = None
    
    
    ContentText = None
    
    
    CustomFooterIcon = None
    
    
    CustomMainIcon = None
    
    
    DefaultButton = None
    
    
    DefaultRadioButton = None
    
    
    EnableHyperlinks = None
    
    
    EnableVerificationHandler = None
    
    
    ExpandedByDefault = None
    
    
    ExpandedControlText = None
    
    
    ExpandedText = None
    
    
    ExpandFooterArea = None
    
    
    ExtraCheckBoxText = None
    
    
    FooterIcon = None
    
    
    FooterText = None
    
    
    MainIcon = None
    
    
    MainInstruction = None
    
    
    NoDefaultRadioButton = None
    
    
    PositionRelativeToWindow = None
    
    
    RightToLeftLayout = None
    
    
    UseCommandLinks = None
    
    
    UseCommandLinksNoIcon = None
    
    
    UseWPF = None
    
    
    VerificationText = None
    
    
    Width = None
    
    
    WidthInXP = None
    
    
    WindowIcon = None
    
    
    WindowTitle = None
    
    pass

class TaskDialogButton(public struct TaskDialogButton {
}):
    """
    
    """
    ButtonId = None
    
    
    ButtonText = None
    
    pass

class TaskDialogButtonCollection(Collection<TaskDialogButton>):
    """
    
    """

    pass

def TaskDialogCallback(self):
    """
    TaskDialogCallback -> bool
    
    """
    pass

class TaskDialogCallbackArgs(public class TaskDialogCallbackArgs):
    """
    
    """
    ButtonId = None
    
    
    Expanded = None
    
    
    ExtraCheckBoxChecked = None
    
    
    Hyperlink = None
    
    
    Notification = None
    
    
    TimerTickCount = None
    
    pass

class TaskDialogCommonButtons():
    Cancel = 8
    Close = 0x20
    No = 4
    None = 0
    Ok = 1
    Retry = 0x10
    Yes = 2

class TaskDialogIcon():
    Error = 0xfffe
    Information = 0xfffd
    None = 0
    Shield = 0xfffc
    Warning = 0xffff

class TaskDialogNotification():
    Created
    Navigated
    ButtonClicked
    HyperlinkClicked
    Timer
    Destroyed
    RadioButtonClicked
    DialogConstructed
    VerificationClicked
    Help
    ExpandoButtonClicked
    ExtraCheckBoxClicked

class TaskDialogResult():
    None
    Ok
    Cancel
    Abort
    Retry
    Ignore
    Yes
    No
    Close