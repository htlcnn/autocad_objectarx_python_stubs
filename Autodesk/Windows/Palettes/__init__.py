class HighlightItemInfo(object):
    """
    
    HighlightItemInfo()
    """
    ItemId = None
    
    
    Mode = None
    
    pass

class IAcSeamlessHost(object):
    """
    
    """
    def GetMFCDialogHighlightItems(self):
        """
        GetMFCDialogHighlightItems -> List<HighlightItemInfo>
        
        """
        pass
    
    pass

class LocationChangingEventArgs(object):
    """
    
    """
    Location = None
    
    
    NewLocation = None
    
    pass

class Palette(object):
    """
    
    Palette()()
    
    
    Palette(string)()
    
    
    Palette(string, Guid)()
    
    
    """
    ImageProperty = None
    
    
    PaletteSetProperty = None
    
    
    TitleProperty = None
    
    
    def NotifyPropertyChanged(self):
        """
        NotifyPropertyChanged -> void
        
        """
        pass
    
    
    def NotifyPropertyChanging(self):
        """
        NotifyPropertyChanging -> void
        
        """
        pass
    
    
    Id = None
    
    
    Image = None
    
    
    MaxHeight = None
    
    
    MaxWidth = None
    
    
    MinHeight = None
    
    
    MinWidth = None
    
    
    PaletteSet = None
    
    
    Title = None
    
    pass

class PaletteActivatedEventArgs(object):
    """
    
    PaletteActivatedEventArgs()
    """
    ActivatedPalette = None
    
    
    DeactivatedPalette = None
    
    pass

class PaletteActivatingEventArgs(object):
    """
    
    PaletteActivatingEventArgs()
    """
    PaletteToActivate = None
    
    
    PaletteToDeactivate = None
    
    pass

class PaletteDockManager(object):
    """
    
    """
    def mainFrameWindow(self):
        """
        mainFrameWindow -> IntPtr
        
        """
        pass
    
    
    def paletteDockManager(self):
        """
        paletteDockManager -> PaletteDockManager
        
        """
        pass
    
    
    def SetMainFrameWindow(self):
        """
        SetMainFrameWindow -> void
        
        """
        pass
    
    pass

class PaletteService(object):
    """
    
    """
    def EnableInput(self):
        """
        EnableInput -> void
        
        """
        pass
    
    
    AcSeamlessHost = None
    
    pass

class PaletteSet(object):
    """
    
    PaletteSet()()
    
    
    PaletteSet(Guid)()
    
    
    PaletteSet(string)()
    
    
    PaletteSet(string, Guid)()
    
    
    """
    ActivePaletteIndexProperty = None
    
    
    ImageProperty = None
    
    
    PaletteCount = None
    
    
    SelectorTypeProperty = None
    
    
    TitleProperty = None
    
    
    def ActivatePalette(self):
        """
        ActivatePalette -> bool
        
        """
        pass
    
    
    def Add(self):
        """
        Add -> Integer
        
        """
        pass
    
    
    def addPaletteContent(self):
        """
        addPaletteContent -> void
        
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose -> void
        
        """
        pass
    
    
    def Hide(self):
        """
        Hide -> bool
        
        """
        pass
    
    
    def IndexOfPalette(self):
        """
        IndexOfPalette -> Integer
        
        """
        pass
    
    
    def InitFloatingPosition(self):
        """
        InitFloatingPosition -> void
        
        """
        pass
    
    
    def NotifyIsSelectedChanged(self):
        """
        NotifyIsSelectedChanged -> void
        
        """
        pass
    
    
    def NotifyPropertyChanged(self):
        """
        NotifyPropertyChanged -> void
        
        """
        pass
    
    
    def NotifyPropertyChanging(self):
        """
        NotifyPropertyChanging -> void
        
        """
        pass
    
    
    def OnSelected(self):
        """
        OnSelected -> void
        
        """
        pass
    
    
    def OnUnselected(self):
        """
        OnUnselected -> void
        
        """
        pass
    
    
    def PaletteAtIndex(self):
        """
        PaletteAtIndex -> Palette
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
        
        """
        pass
    
    
    def RemovePaletteAtIndex(self):
        """
        RemovePaletteAtIndex -> void
        
        """
        pass
    
    
    def Show(self):
        """
        Show -> bool
        
        """
        pass
    
    
    def UpdateWindowMinMaxSize(self):
        """
        UpdateWindowMinMaxSize -> void
        
        """
        pass
    
    
    ActivePaletteIndex = None
    
    
    Id = None
    
    
    Image = None
    
    
    MaxHeight = None
    
    
    MaxWidth = None
    
    
    MinHeight = None
    
    
    MinWidth = None
    
    
    SelectorType = None
    
    
    Title = None
    
    pass

class PaletteSetSelectorType():
    ImageSelector = None
    ComboBoxSelector = None

class PaletteSettings(object):
    """
    
    """
    def EnableInput(self):
        """
        EnableInput -> void
        
        """
        pass
    
    
    def NotifyPropertyChanged(self):
        """
        NotifyPropertyChanged -> void
        
        """
        pass
    
    
    CurrentTheme = None
    
    pass

class PaletteTheme(object):
    """
    
    """
    def CreateInstanceCore(self):
        """
        CreateInstanceCore -> Freezable
        
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            PaletteTheme theme: 
            Specify the PaletteTheme that is used to compared.
        """
        pass
    
    
    ActiveTabBrush = None
    
    
    ActiveTextBrush = None
    
    
    ActivityIndicatorBrush = None
    
    
    ApplicationFrameActiveGradientBottomColor = None
    
    
    ApplicationFrameActiveGradientTopColor = None
    
    
    ApplicationFrameCaptionActiveGradientBottomColor = None
    
    
    ApplicationFrameCaptionActiveGradientTopColor = None
    
    
    ApplicationFrameCaptionInactiveBorderColor = None
    
    
    ApplicationFrameCaptionInactiveGradientBottomColor = None
    
    
    ApplicationFrameCaptionInactiveGradientTopColor = None
    
    
    ApplicationFrameCaptionInnerBorderColor = None
    
    
    ApplicationFrameCaptionOuterBorderColor = None
    
    
    ApplicationFrameControlButtonsClickBorderColor = None
    
    
    ApplicationFrameControlButtonsClickGradientFillBottomColor = None
    
    
    ApplicationFrameControlButtonsClickGradientFillTopColor = None
    
    
    ApplicationFrameControlButtonsClickSymbolColor = None
    
    
    ApplicationFrameControlButtonsRolloverBorderColor = None
    
    
    ApplicationFrameControlButtonsRolloverGradientFillBottomColor = None
    
    
    ApplicationFrameControlButtonsRolloverGradientFillTopColor = None
    
    
    ApplicationFrameControlButtonsRolloverSymbolColor = None
    
    
    ApplicationFrameControlButtonsSymbolColor = None
    
    
    ApplicationFrameDocumentNameFileNameTextColor = None
    
    
    ApplicationFrameDocumentNameInactiveFileNameTextColor = None
    
    
    ApplicationFrameInactiveBorderColor = None
    
    
    ApplicationFrameInactiveGradientColor = None
    
    
    ApplicationFrameInnerBorderColor = None
    
    
    ApplicationFrameMenuBarClickBorderColor = None
    
    
    ApplicationFrameMenuBarClickFillColor = None
    
    
    ApplicationFrameMenuBarMenuHighlightTextColor = None
    
    
    ApplicationFrameMenuBarMenuTextColor = None
    
    
    ApplicationFrameMenuBarRolloverBorderColor = None
    
    
    ApplicationFrameMenuBarRolloverFillColor = None
    
    
    ApplicationFrameNonClientInnerBorderColor = None
    
    
    ApplicationFrameNonClientOuterBorderColor = None
    
    
    ApplicationFrameOuterBorderColor = None
    
    
    BoldFont = None
    
    
    CategoryBackgroundBrush = None
    
    
    CategoryBackgroundColor = None
    
    
    CategoryBorderBrush = None
    
    
    CategoryBorderColor = None
    
    
    CategoryButtonClickBackgroundBrush = None
    
    
    CategoryButtonClickBackgroundColor = None
    
    
    CategoryButtonHoverBackgroundBrush = None
    
    
    CategoryButtonHoverBackgroundColor = None
    
    
    CategoryExpanderBrush = None
    
    
    CategoryExpanderColor = None
    
    
    CategoryExpanderFillBrush = None
    
    
    CategoryExpanderFillColor = None
    
    
    CategoryExpanderShadowBrush = None
    
    
    CategoryExpanderShadowColor = None
    
    
    CheckBoxBackgroundBrush = None
    
    
    CheckBoxBackgroundColor = None
    
    
    CheckBoxBorderBrush = None
    
    
    CheckBoxBorderColor = None
    
    
    CheckBoxCheckBrush = None
    
    
    CheckBoxCheckColor = None
    
    
    CheckBoxHoverBackgroundBrush = None
    
    
    CheckBoxHoverBackgroundColor = None
    
    
    CheckBoxHoverBorderBrush = None
    
    
    CheckBoxHoverBorderColor = None
    
    
    CheckBoxPressedBackgroundBrush = None
    
    
    CheckBoxPressedBackgroundColor = None
    
    
    CheckBoxPressedBorderBrush = None
    
    
    CheckBoxPressedBorderColor = None
    
    
    ColorControlArrowColor = None
    
    
    ColorControlButtonBackgroundColor1 = None
    
    
    ColorControlButtonBackgroundColor2 = None
    
    
    ColorControlButtonBorderColor = None
    
    
    ColorControlCheckedButtonBorderColor = None
    
    
    ColorControlCheckedButtonPanelBackgroundColor1 = None
    
    
    ColorControlCheckedButtonPanelBackgroundColor2 = None
    
    
    ColorControlDisabledArrowColor = None
    
    
    ColorControlDisabledForegroundColor = None
    
    
    ColorControlForegroundColor = None
    
    
    ColorControlListBoxItemBackgroundColor1 = None
    
    
    ColorControlListBoxItemBackgroundColor2 = None
    
    
    ColorControlListBoxItemBorderColor = None
    
    
    ColorControlMouseOverButtonBorderColor = None
    
    
    ColorControlMouseOverButtonPanelBackgroundColor1 = None
    
    
    ColorControlMouseOverButtonPanelBackgroundColor2 = None
    
    
    ColorControlNormalButtonBorderColor = None
    
    
    ColorControlNormalButtonPanelBackgroundColor1 = None
    
    
    ColorControlNormalButtonPanelBackgroundColor2 = None
    
    
    ColorControlPopupBackgroundColor = None
    
    
    ColorControlPopupBorderColor = None
    
    
    ColorControlPopupSeparatorColor = None
    
    
    ColorControlPopupTextColor = None
    
    
    ColorControlPressedButtonBorderColor = None
    
    
    ColorControlPressedButtonPanelBackgroundColor1 = None
    
    
    ColorControlPressedButtonPanelBackgroundColor2 = None
    
    
    ColorControlPressedListBoxItemBackgroundColor1 = None
    
    
    ColorControlPressedListBoxItemBackgroundColor2 = None
    
    
    ColorControlPressedListBoxItemBorderColor = None
    
    
    ColorControlSelectListBoxItemBackgroundColor1 = None
    
    
    ColorControlSelectListBoxItemBackgroundColor2 = None
    
    
    ColorControlSelectListBoxItemBorderColor = None
    
    
    ComboBoxActiveBackgroundBottomColor = None
    
    
    ComboBoxActiveBackgroundBrush = None
    
    
    ComboBoxActiveBackgroundTopColor = None
    
    
    ComboBoxArrowBrush = None
    
    
    ComboBoxArrowColor = None
    
    
    ComboBoxArrowShadowBrush = None
    
    
    ComboBoxArrowShadowColor = None
    
    
    ComboBoxBackgroundBottomColor = None
    
    
    ComboBoxBackgroundBrush = None
    
    
    ComboBoxBackgroundTopColor = None
    
    
    ComboBoxBorderBrush = None
    
    
    ComboBoxBorderColor = None
    
    
    ComboBoxDisabledTextBrush = None
    
    
    ComboBoxDisabledTextColor = None
    
    
    ComboBoxHoverBackgroundBottomColor = None
    
    
    ComboBoxHoverBackgroundBrush = None
    
    
    ComboBoxHoverBackgroundTopColor = None
    
    
    ComboBoxHoverBorderBrush = None
    
    
    ComboBoxHoverBorderColor = None
    
    
    ComboBoxHoverSelectHighlightBrush = None
    
    
    ComboBoxHoverSelectHighlightColor = None
    
    
    ComboBoxHoverTextBrush = None
    
    
    ComboBoxHoverTextColor = None
    
    
    ComboBoxSelectBackgroundBottomColor = None
    
    
    ComboBoxSelectBackgroundBrush = None
    
    
    ComboBoxSelectBackgroundTopColor = None
    
    
    ComboBoxSelectTextBrush = None
    
    
    ComboBoxSelectTextColor = None
    
    
    ComboBoxSeparatorBrush = None
    
    
    ComboBoxSeparatorColor = None
    
    
    ComboBoxTextBrush = None
    
    
    ComboBoxTextColor = None
    
    
    CommandLineBackgroundBorderColor = None
    
    
    CommandLineBackgroundColor1 = None
    
    
    CommandLineBackgroundColor2 = None
    
    
    CommandLineButtonBackgroundPressedColor = None
    
    
    CommandLineButtonBackgroundRolloverColor = None
    
    
    CommandLineButtonBorderPressedColor = None
    
    
    CommandLineButtonBorderRolloverColor = None
    
    
    CommandLineButtonPathFillColor = None
    
    
    CommandLineCommandOptionsTextHighlightedColor = None
    
    
    CommandLineCommandOptionsTextHighlightedColorBrush = None
    
    
    CommandLineDefaultTextForegroundColor = None
    
    
    CommandLineHintBackgroundColor = None
    
    
    CommandLineHintBorderColor = None
    
    
    CommandLineHintHeaderBackgroundColor = None
    
    
    CommandLineHintHeaderTextColor = None
    
    
    CommandLineHintScrollBarThumbColor = None
    
    
    CommandLineHintSelectBackgroundColor = None
    
    
    CommandLineHintSelectBorderColor = None
    
    
    CommandLineHintSelectTextColor = None
    
    
    CommandLineHintTextColor = None
    
    
    CommandLineHistoryBackgroundColor = None
    
    
    CommandLineHistoryBackgroundColorBrush = None
    
    
    CommandLineHistoryBorderColor = None
    
    
    CommandLineImageButtonBackgroundRolloverColor1 = None
    
    
    CommandLineImageButtonBackgroundRolloverColor2 = None
    
    
    CommandLineImageButtonBackgroundRolloverColor3 = None
    
    
    CommandLineImageButtonBackgroundRolloverColor4 = None
    
    
    CommandLineImageButtonBorderRolloverColor = None
    
    
    CommandLineInputAreaBorderColor = None
    
    
    CommandLineSuggestionListExpandedBackgroundBrush = None
    
    
    CommandLineSuggestionListExpandedBackgroundColor = None
    
    
    CommandLineTitlePathColor = None
    
    
    ContainerBackgroundBrush = None
    
    
    ContainerBorderBrush = None
    
    
    ContainerHighlightBrush = None
    
    
    ControlActiveOuterBorderBrush = None
    
    
    ControlActiveOuterBorderColor = None
    
    
    ControlActiveTextColor = None
    
    
    ControlBorderBrush = None
    
    
    ControlBorderColor = None
    
    
    ControlCaretBrush = None
    
    
    ControlCaretColor = None
    
    
    ControlDisabledTextBrush = None
    
    
    ControlDisabledTextColor = None
    
    
    ControlErrorOuterBorderBrush = None
    
    
    ControlErrorOuterBorderColor = None
    
    
    ControlHighlightColor = None
    
    
    ControlInactiveTextBrush = None
    
    
    ControlInactiveTextColor = None
    
    
    ControlTextBrush = None
    
    
    ControlTextColor = None
    
    
    FileTabsActiveBackgroundBottomColor = None
    
    
    FileTabsActiveBackgroundBrush = None
    
    
    FileTabsActiveBackgroundTopColor = None
    
    
    FileTabsActiveInverseBackgroundBrush = None
    
    
    FileTabsBorderColor = None
    
    
    FileTabsButtonHoverBorderColor = None
    
    
    FileTabsButtonHoverColor = None
    
    
    FileTabsCloseButtonForegroundClickColor = None
    
    
    FileTabsCloseButtonForegroundColor = None
    
    
    FileTabsCloseButtonForegroundHoverColor = None
    
    
    FileTabsHighlightBottomColor = None
    
    
    FileTabsHighlightBrush = None
    
    
    FileTabsHighlightTopColor = None
    
    
    FileTabsHorizListBoxActiveBorderColor = None
    
    
    FileTabsHorizListBoxBackgroundBrush = None
    
    
    FileTabsHorizListBoxBackgroundColor = None
    
    
    FileTabsHorizListBoxHoverColor = None
    
    
    FileTabsInactiveBackgroundBottomColor = None
    
    
    FileTabsInactiveBackgroundBrush = None
    
    
    FileTabsInactiveBackgroundTopColor = None
    
    
    FileTabsInactiveInverseBackgroundBrush = None
    
    
    FileTabsInnerHighlightBrush = None
    
    
    FileTabsInnerHighlightColor = None
    
    
    FileTabsInverseHighlightBrush = None
    
    
    FileTabsNewButtonForegroundClickColor = None
    
    
    FileTabsNewButtonForegroundColor = None
    
    
    FileTabsNewButtonForegroundHoverColor = None
    
    
    FileTabsRowBackgroundBrush = None
    
    
    FileTabsRowBackgroundColor = None
    
    
    GroupGripColor = None
    
    
    GroupGripShadowColor = None
    
    
    InactiveSearchBrush = None
    
    
    InactiveTextBrush = None
    
    
    IPETextFocusBackgroundBottomColor = None
    
    
    IPETextFocusBackgroundBrush = None
    
    
    IPETextFocusBackgroundTopColor = None
    
    
    IsDark = None
    
    
    ListBoxBorderBrush = None
    
    
    ListBoxBorderColor = None
    
    
    ListBoxClickBackgroundBottomColor = None
    
    
    ListBoxClickBackgroundBrush = None
    
    
    ListBoxClickBackgroundTopColor = None
    
    
    ListBoxClickBorderBrush = None
    
    
    ListBoxClickBorderColor = None
    
    
    ListBoxColumnHeaderArrowBrush = None
    
    
    ListBoxColumnHeaderArrowColor = None
    
    
    ListBoxColumnHeaderBackgroundBottomColor = None
    
    
    ListBoxColumnHeaderBackgroundBrush = None
    
    
    ListBoxColumnHeaderBackgroundTopColor = None
    
    
    ListBoxColumnHeaderBorderBrush = None
    
    
    ListBoxColumnHeaderBorderColor = None
    
    
    ListBoxColumnHeaderSortCellBackgroundBottomColor = None
    
    
    ListBoxColumnHeaderSortCellBackgroundBrush = None
    
    
    ListBoxColumnHeaderSortCellBackgroundTopColor = None
    
    
    ListBoxColumnHeaderTextBrush = None
    
    
    ListBoxColumnHeaderTextColor = None
    
    
    ListBoxDisabledTextBrush = None
    
    
    ListBoxDisabledTextColor = None
    
    
    ListBoxGridBrush = None
    
    
    ListBoxGridColor = None
    
    
    ListBoxGroupHeaderTextBrush = None
    
    
    ListBoxGroupHeaderTextColor = None
    
    
    ListBoxHoverBackgroundBottomColor = None
    
    
    ListBoxHoverBackgroundBrush = None
    
    
    ListBoxHoverBackgroundTopColor = None
    
    
    ListBoxHoverBorderBrush = None
    
    
    ListBoxHoverBorderColor = None
    
    
    ListBoxInactiveTextBrush = None
    
    
    ListBoxInactiveTextColor = None
    
    
    ListBoxInnerShadowBrush = None
    
    
    ListBoxInnerShadowColor = None
    
    
    ListBoxSelectBackgroundBottomColor = None
    
    
    ListBoxSelectBackgroundBrush = None
    
    
    ListBoxSelectBackgroundTopColor = None
    
    
    ListBoxSelectBorderBrush = None
    
    
    ListBoxSelectBorderColor = None
    
    
    ListBoxSelectDisabledTextBrush = None
    
    
    ListBoxSelectDisabledTextColor = None
    
    
    ListBoxSelectHoverBackgroundBottomColor = None
    
    
    ListBoxSelectHoverBackgroundBrush = None
    
    
    ListBoxSelectHoverBackgroundTopColor = None
    
    
    ListBoxSelectHoverBorderBrush = None
    
    
    ListBoxSelectHoverBorderColor = None
    
    
    ListBoxSelectInactiveBackgroundBottomColor = None
    
    
    ListBoxSelectInactiveBackgroundBrush = None
    
    
    ListBoxSelectInactiveBackgroundTopColor = None
    
    
    ListBoxSelectInactiveTextBrush = None
    
    
    ListBoxSelectInactiveTextColor = None
    
    
    ListBoxSelectTextBrush = None
    
    
    ListBoxSelectTextColor = None
    
    
    ListBoxTextBrush = None
    
    
    ListBoxTextColor = None
    
    
    MenuBackgroundBrush = None
    
    
    MenuBackgroundColor = None
    
    
    MenuCheckMarkBrush = None
    
    
    MenuCheckMarkColor = None
    
    
    MenuInnerBorderBrush = None
    
    
    MenuInnerBorderColor = None
    
    
    MenuItemHoverBackgroundBottomColor = None
    
    
    MenuItemHoverBackgroundBrush = None
    
    
    MenuItemHoverBackgroundTopColor = None
    
    
    MenuItemHoverBorderBrush = None
    
    
    MenuItemHoverBorderColor = None
    
    
    MenuOuterBorderBrush = None
    
    
    MenuOuterBorderColor = None
    
    
    MenuSeparatorBrush = None
    
    
    MenuSeparatorColor = None
    
    
    MenuTextBrush = None
    
    
    MenuTextColor = None
    
    
    NormalFont = None
    
    
    OverallColor = None
    
    
    OverallTextColor = None
    
    
    PaletteActivityIndicatorOutlineColor = None
    
    
    PaletteAnchorBarActiveTitleBackgroundColor = None
    
    
    PaletteAnchorBarBackgroundColor = None
    
    
    PaletteAnchorBarCaptionTextColor = None
    
    
    PaletteAnchorBarEmbossLeftTopColor = None
    
    
    PaletteAnchorBarEmbossRightBottomColor = None
    
    
    PaletteAnchorBarGradientColor1 = None
    
    
    PaletteAnchorBarGradientColor2 = None
    
    
    PaletteAnchorBarInnerHighlightColor = None
    
    
    PaletteAnchorBarOuterBorderColor = None
    
    
    PaletteColumnHeaderBackgroundColor = None
    
    
    PaletteContainerBackgroundColor = None
    
    
    PaletteContainerBorderColor = None
    
    
    PaletteContainerCloseColor = None
    
    
    PaletteContainerHighlightColor = None
    
    
    PaletteHyperlinkTextColor = None
    
    
    PaletteSearchActiveBottomColor = None
    
    
    PaletteSearchActiveTopColor = None
    
    
    PaletteSearchInactiveBottomColor = None
    
    
    PaletteSearchInactiveTopColor = None
    
    
    PaletteTabActiveBottomColor = None
    
    
    PaletteTabActiveTopColor = None
    
    
    PaletteTabBackgroundColor = None
    
    
    PaletteTabBorderColor = None
    
    
    PaletteTabHighlightColor = None
    
    
    PaletteTabInactiveColor = None
    
    
    PaletteTabScrollColor = None
    
    
    PaletteTextActiveColor = None
    
    
    PaletteTextInactiveColor = None
    
    
    PaletteTextSearchAutocompleteColor = None
    
    
    PaletteTextSearchPlaceholderColor = None
    
    
    PaletteTextSearchUserstringColor = None
    
    
    PaletteTreeOrListBackgroundBrush = None
    
    
    PaletteTreeOrListBackgroundColor = None
    
    
    PropertyInspectorCategoryBackgroundColor = None
    
    
    PropertyInspectorItemBorderColor = None
    
    
    PropertyInspectorSubCategoryBackgroundColor = None
    
    
    PropertyInspectorTextLabelColor = None
    
    
    PushButtonActiveBackgroundBottomColor = None
    
    
    PushButtonActiveBackgroundBrush = None
    
    
    PushButtonActiveBackgroundTopColor = None
    
    
    PushButtonActiveShadowColor = None
    
    
    PushButtonActiveTextBrush = None
    
    
    PushButtonActiveTextColor = None
    
    
    PushButtonBackgroundBottomColor = None
    
    
    PushButtonBackgroundBrush = None
    
    
    PushButtonBackgroundTopColor = None
    
    
    PushButtonBorderBrush = None
    
    
    PushButtonBorderColor = None
    
    
    PushButtonHoverBackgroundBottomColor = None
    
    
    PushButtonHoverBackgroundBrush = None
    
    
    PushButtonHoverBackgroundTopColor = None
    
    
    PushButtonHoverBorderBrush = None
    
    
    PushButtonHoverBorderColor = None
    
    
    QATButtonBackgroundActiveColor1 = None
    
    
    QATButtonBackgroundActiveColor2 = None
    
    
    QATButtonBackgroundActiveRolloverColor1 = None
    
    
    QATButtonBackgroundActiveRolloverColor2 = None
    
    
    QATButtonBackgroundPressedColor1 = None
    
    
    QATButtonBackgroundPressedColor2 = None
    
    
    QATButtonBackgroundRolloverColor1 = None
    
    
    QATButtonBackgroundRolloverColor2 = None
    
    
    QATButtonBorderActiveColor = None
    
    
    QATButtonBorderActiveRolloverColor = None
    
    
    QATButtonBorderPressedColor = None
    
    
    QATButtonBorderRollOverColor = None
    
    
    QATCheckBoxBackgroundColor1 = None
    
    
    QATCheckBoxBackgroundColor2 = None
    
    
    QATCheckBoxBorderColor = None
    
    
    QATCheckBoxPressedBackgroundColor = None
    
    
    QATCheckBoxPressedBorderColor = None
    
    
    QATCheckBoxRollOverBackgroundColor = None
    
    
    QATCheckBoxRollOverBorderColor = None
    
    
    QATComboBoxBackgroundColor1 = None
    
    
    QATComboBoxBackgroundColor2 = None
    
    
    QATComboBoxBorderColor = None
    
    
    QATComboBoxButtonPressedBackgroundColor = None
    
    
    QATComboBoxButtonPressedBorderColor = None
    
    
    QATComboBoxButtonRollOverBackgroundColor = None
    
    
    QATComboBoxButtonRollOverBorderColor = None
    
    
    QATComboBoxDropDownBackgroundColor = None
    
    
    QATComboBoxDropDownBorderColor = None
    
    
    QATComboBoxRollOverBackgroundColor = None
    
    
    QATComboBoxRollOverBorderColor = None
    
    
    QATComboBoxSelectBackgroundColor = None
    
    
    QATComboBoxSelectBorderColor = None
    
    
    QATDisabledTextBoxBackgroundColor = None
    
    
    QATDisabledTextForegroundColor = None
    
    
    QATDropDownListBoxBackgroundColor = None
    
    
    QATDropDownListBoxBorderColor = None
    
    
    QATListBoxRollOverBackgroundColor = None
    
    
    QATListBoxRollOverBorderColor = None
    
    
    QATListBoxSelectBackgroundColor = None
    
    
    QATListBoxSelectBorderColor = None
    
    
    QATListBoxSeparatorColor = None
    
    
    QATListButtonBackgroundRolloverColor1 = None
    
    
    QATListButtonBackgroundRolloverColor2 = None
    
    
    QATListHeaderBackgroundColor = None
    
    
    QATMenuItemListBoxBackgroundColor = None
    
    
    QATMenuItemListBoxBorderColor = None
    
    
    QATMenuItemListBoxRollOverBackgroundColor = None
    
    
    QATMenuItemListBoxRollOverBorderColor = None
    
    
    QATPromptTextForegroundColor = None
    
    
    QATSeparatorColor = None
    
    
    QATSpinnerBackgroundColor = None
    
    
    QATTextBoxBackgroundColor = None
    
    
    QATTextBoxBorderColor = None
    
    
    QATTextBoxForegroundColor = None
    
    
    QATTextBoxRollOverBorderColor = None
    
    
    QATToggleButtonPressedBackgroundColor = None
    
    
    QATToggleButtonPressedBorderColor = None
    
    
    QATToggleButtonRollOverBackgroundColor = None
    
    
    QATToggleButtonRollOverBorderColor = None
    
    
    QATToolBarListBoxBackgroundColor = None
    
    
    QATToolBarTextBlockColor1 = None
    
    
    QATToolBarTextBlockColor2 = None
    
    
    RibbonArrowColor = None
    
    
    RibbonBlueInnerBorderColor = None
    
    
    RibbonBlueOuterBorderColor = None
    
    
    RibbonBluePanelBackgroundColor1 = None
    
    
    RibbonBluePanelBackgroundColor2 = None
    
    
    RibbonBluePanelBackgroundColor3 = None
    
    
    RibbonBluePanelBackgroundVerticalLeftColor1 = None
    
    
    RibbonBluePanelBackgroundVerticalLeftColor2 = None
    
    
    RibbonBluePanelBackgroundVerticalRightColor1 = None
    
    
    RibbonBluePanelBackgroundVerticalRightColor2 = None
    
    
    RibbonBluePanelBorderColor = None
    
    
    RibbonBluePanelTitleBarBackgroundColor1 = None
    
    
    RibbonBluePanelTitleBarBackgroundColor2 = None
    
    
    RibbonBluePanelTitleBarBackgroundColor3 = None
    
    
    RibbonBlueTabItemBackgroundDefaultColor1 = None
    
    
    RibbonBlueTabItemBackgroundDefaultColor2 = None
    
    
    RibbonBlueTabItemBackgroundSelectedColor1 = None
    
    
    RibbonBlueTabItemBackgroundSelectedColor2 = None
    
    
    RibbonButtonBackgroundActiveColor1 = None
    
    
    RibbonButtonBackgroundActiveColor2 = None
    
    
    RibbonButtonBackgroundActiveRolloverColor1 = None
    
    
    RibbonButtonBackgroundActiveRolloverColor2 = None
    
    
    RibbonButtonBackgroundPressedColor1 = None
    
    
    RibbonButtonBackgroundPressedColor2 = None
    
    
    RibbonButtonBackgroundRolloverColor1 = None
    
    
    RibbonButtonBackgroundRolloverColor2 = None
    
    
    RibbonButtonBorderActiveColor = None
    
    
    RibbonButtonBorderActiveRolloverColor = None
    
    
    RibbonButtonBorderColor = None
    
    
    RibbonButtonBorderInvisibleColor = None
    
    
    RibbonButtonBorderPressedColor = None
    
    
    RibbonButtonBorderRollOverColor = None
    
    
    RibbonCheckBoxBackgroundColor1 = None
    
    
    RibbonCheckBoxBackgroundColor2 = None
    
    
    RibbonCheckBoxBorderColor = None
    
    
    RibbonCheckBoxPressedBackgroundColor = None
    
    
    RibbonCheckBoxPressedBorderColor = None
    
    
    RibbonCheckBoxRollOverBackgroundColor = None
    
    
    RibbonCheckBoxRollOverBorderColor = None
    
    
    RibbonComboBoxBackgroundColor1 = None
    
    
    RibbonComboBoxBackgroundColor2 = None
    
    
    RibbonComboBoxBorderColor = None
    
    
    RibbonComboBoxButtonPressedBackgroundColor = None
    
    
    RibbonComboBoxButtonPressedBorderColor = None
    
    
    RibbonComboBoxButtonRollOverBackgroundColor = None
    
    
    RibbonComboBoxButtonRollOverBorderColor = None
    
    
    RibbonComboBoxDropDownBackgroundColor = None
    
    
    RibbonComboBoxDropDownBorderColor = None
    
    
    RibbonComboBoxRollOverBackgroundColor = None
    
    
    RibbonComboBoxRollOverBorderColor = None
    
    
    RibbonComboBoxSelectBackgroundColor = None
    
    
    RibbonComboBoxSelectBorderColor = None
    
    
    RibbonCyanInnerBorderColor = None
    
    
    RibbonCyanOuterBorderColor = None
    
    
    RibbonCyanPanelBackgroundColor1 = None
    
    
    RibbonCyanPanelBackgroundColor2 = None
    
    
    RibbonCyanPanelBackgroundColor3 = None
    
    
    RibbonCyanPanelBackgroundVerticalLeftColor1 = None
    
    
    RibbonCyanPanelBackgroundVerticalLeftColor2 = None
    
    
    RibbonCyanPanelBackgroundVerticalRightColor1 = None
    
    
    RibbonCyanPanelBackgroundVerticalRightColor2 = None
    
    
    RibbonCyanPanelBorderColor = None
    
    
    RibbonCyanPanelTitleBarBackgroundColor1 = None
    
    
    RibbonCyanPanelTitleBarBackgroundColor2 = None
    
    
    RibbonCyanPanelTitleBarBackgroundColor3 = None
    
    
    RibbonCyanTabItemBackgroundDefaultColor1 = None
    
    
    RibbonCyanTabItemBackgroundDefaultColor2 = None
    
    
    RibbonCyanTabItemBackgroundSelectedColor1 = None
    
    
    RibbonCyanTabItemBackgroundSelectedColor2 = None
    
    
    RibbonDisabledTextBoxBackgroundColor = None
    
    
    RibbonDisabledTextForegroundColor = None
    
    
    RibbonDropDownListBoxBackgroundColor = None
    
    
    RibbonDropDownListBoxBorderColor = None
    
    
    RibbonFloatingFrameBackgroundColor = None
    
    
    RibbonGalleryBackgroundFillColor = None
    
    
    RibbonGreenInnerBorderColor = None
    
    
    RibbonGreenOuterBorderColor = None
    
    
    RibbonGreenPanelBackgroundColor1 = None
    
    
    RibbonGreenPanelBackgroundColor2 = None
    
    
    RibbonGreenPanelBackgroundColor3 = None
    
    
    RibbonGreenPanelBackgroundVerticalLeftColor1 = None
    
    
    RibbonGreenPanelBackgroundVerticalLeftColor2 = None
    
    
    RibbonGreenPanelBackgroundVerticalRightColor1 = None
    
    
    RibbonGreenPanelBackgroundVerticalRightColor2 = None
    
    
    RibbonGreenPanelBorderColor = None
    
    
    RibbonGreenPanelTitleBarBackgroundColor1 = None
    
    
    RibbonGreenPanelTitleBarBackgroundColor2 = None
    
    
    RibbonGreenPanelTitleBarBackgroundColor3 = None
    
    
    RibbonGreenTabItemBackgroundDefaultColor1 = None
    
    
    RibbonGreenTabItemBackgroundDefaultColor2 = None
    
    
    RibbonGreenTabItemBackgroundSelectedColor1 = None
    
    
    RibbonGreenTabItemBackgroundSelectedColor2 = None
    
    
    RibbonItemStyleButtonBackgroundIdleColor1 = None
    
    
    RibbonItemStyleButtonBackgroundIdleColor2 = None
    
    
    RibbonItemStyleButtonBorderColor = None
    
    
    RibbonListBoxRollOverBackgroundColor = None
    
    
    RibbonListBoxRollOverBorderColor = None
    
    
    RibbonListBoxSelectBackgroundColor = None
    
    
    RibbonListBoxSelectBorderColor = None
    
    
    RibbonListBoxSeparatorColor = None
    
    
    RibbonListButtonBackgroundRolloverColor1 = None
    
    
    RibbonListButtonBackgroundRolloverColor2 = None
    
    
    RibbonListHeaderBackgroundColor = None
    
    
    RibbonMenuItemListBoxBackgroundColor = None
    
    
    RibbonMenuItemListBoxBorderColor = None
    
    
    RibbonMenuItemListBoxRollOverBackgroundColor = None
    
    
    RibbonMenuItemListBoxRollOverBorderColor = None
    
    
    RibbonOverflowTabPanelBackgroundColor = None
    
    
    RibbonOverflowTabPanelBorderColor = None
    
    
    RibbonOverflowTabPanelForegroundColor = None
    
    
    RibbonPanelBackgroundColor1 = None
    
    
    RibbonPanelBackgroundColor2 = None
    
    
    RibbonPanelBarBackgroundColor1 = None
    
    
    RibbonPanelBarBackgroundColor2 = None
    
    
    RibbonPanelBorderColor = None
    
    
    RibbonPanelContentBackgroundColor1 = None
    
    
    RibbonPanelContentBackgroundColor2 = None
    
    
    RibbonPanelDialogBoxLauncherColor = None
    
    
    RibbonPanelSlideoutAreaDefaultColor1 = None
    
    
    RibbonPanelSlideoutAreaDefaultColor2 = None
    
    
    RibbonPanelSlideoutSeparatorColor = None
    
    
    RibbonPanelTitleForegroundColor = None
    
    
    RibbonPurpleInnerBorderColor = None
    
    
    RibbonPurpleOuterBorderColor = None
    
    
    RibbonPurplePanelBackgroundColor1 = None
    
    
    RibbonPurplePanelBackgroundColor2 = None
    
    
    RibbonPurplePanelBackgroundColor3 = None
    
    
    RibbonPurplePanelBackgroundVerticalLeftColor1 = None
    
    
    RibbonPurplePanelBackgroundVerticalLeftColor2 = None
    
    
    RibbonPurplePanelBackgroundVerticalRightColor1 = None
    
    
    RibbonPurplePanelBackgroundVerticalRightColor2 = None
    
    
    RibbonPurplePanelBorderColor = None
    
    
    RibbonPurplePanelTitleBarBackgroundColor1 = None
    
    
    RibbonPurplePanelTitleBarBackgroundColor2 = None
    
    
    RibbonPurplePanelTitleBarBackgroundColor3 = None
    
    
    RibbonPurpleTabItemBackgroundDefaultColor1 = None
    
    
    RibbonPurpleTabItemBackgroundDefaultColor2 = None
    
    
    RibbonPurpleTabItemBackgroundSelectedColor1 = None
    
    
    RibbonPurpleTabItemBackgroundSelectedColor2 = None
    
    
    RibbonRenderBackgroundColor = None
    
    
    RibbonRenderBorderColor = None
    
    
    RibbonRenderProgressBarBackgroundColor = None
    
    
    RibbonRenderProgressBarBorderColor = None
    
    
    RibbonRenderProgressBarForegroundColor = None
    
    
    RibbonResizeControlBackgroundColor = None
    
    
    RibbonResizeControlBorderColor = None
    
    
    RibbonScrollBarThumbFillColor = None
    
    
    RibbonScrollBarThumbRolloverBorderColor = None
    
    
    RibbonScrollBarThumbRolloverGradientColor1 = None
    
    
    RibbonScrollBarThumbRolloverGradientColor2 = None
    
    
    RibbonScrollBarThumbRolloverGradientColor3 = None
    
    
    RibbonScrollBarThumbRolloverGradientColor4 = None
    
    
    RibbonScrollbarTrackBackgroundColor = None
    
    
    RibbonScrollbarTrackBorderColor = None
    
    
    RibbonSeparatorColor = None
    
    
    RibbonSlideoutButtonBorderColor = None
    
    
    RibbonSlideoutPanelBorderColor = None
    
    
    RibbonSliderBorderColor = None
    
    
    RibbonSliderTextBoxBackgroundColor = None
    
    
    RibbonSliderTextBoxBorderColor = None
    
    
    RibbonSliderTextForegroundColor = None
    
    
    RibbonSliderThumbColor = None
    
    
    RibbonSliderThumbInactiveColor1 = None
    
    
    RibbonSliderThumbInactiveColor2 = None
    
    
    RibbonSliderTickColor = None
    
    
    RibbonSliderTrackDecreaseBackgroundColor = None
    
    
    RibbonSpinnerBackgroundColor = None
    
    
    RibbonSpinnerButtonArrowColor = None
    
    
    RibbonTabBackgroundColor = None
    
    
    RibbonTabItemForegroundColor = None
    
    
    RibbonTabItemRolloverColor1 = None
    
    
    RibbonTabItemRolloverColor2 = None
    
    
    RibbonTabItemRolloverForegroundColor = None
    
    
    RibbonTabItemSelectedColor1 = None
    
    
    RibbonTabItemSelectedColor2 = None
    
    
    RibbonTabItemSelectedForegroundColor = None
    
    
    RibbonTabListBoxBorderColor = None
    
    
    RibbonTabOverflowArrowHighlightColor = None
    
    
    RibbonTabOverflowArrowIdleColor = None
    
    
    RibbonTabsListItemContainerBorderColor = None
    
    
    RibbonTabsListItemContainerBorderRollOverColor = None
    
    
    RibbonTextBoxBackgroundColor = None
    
    
    RibbonTextBoxBorderColor = None
    
    
    RibbonTextBoxForegroundColor = None
    
    
    RibbonTextBoxRollOverBorderColor = None
    
    
    RibbonTextForegroundColor = None
    
    
    RibbonToggleButtonPressedBackgroundColor = None
    
    
    RibbonToggleButtonPressedBorderColor = None
    
    
    RibbonToggleButtonRollOverBackgroundColor = None
    
    
    RibbonToggleButtonRollOverBorderColor = None
    
    
    RibbonYellowInnerBorderColor = None
    
    
    RibbonYellowOuterBorderColor = None
    
    
    RibbonYellowPanelBackgroundColor1 = None
    
    
    RibbonYellowPanelBackgroundColor2 = None
    
    
    RibbonYellowPanelBackgroundColor3 = None
    
    
    RibbonYellowPanelBackgroundVerticalLeftColor1 = None
    
    
    RibbonYellowPanelBackgroundVerticalLeftColor2 = None
    
    
    RibbonYellowPanelBackgroundVerticalRightColor1 = None
    
    
    RibbonYellowPanelBackgroundVerticalRightColor2 = None
    
    
    RibbonYellowPanelBorderColor = None
    
    
    RibbonYellowPanelTitleBarBackgroundColor1 = None
    
    
    RibbonYellowPanelTitleBarBackgroundColor2 = None
    
    
    RibbonYellowPanelTitleBarBackgroundColor3 = None
    
    
    RibbonYellowTabItemBackgroundDefaultColor1 = None
    
    
    RibbonYellowTabItemBackgroundDefaultColor2 = None
    
    
    RibbonYellowTabItemBackgroundSelectedColor1 = None
    
    
    RibbonYellowTabItemBackgroundSelectedColor2 = None
    
    
    ScrollBarThumbBrush = None
    
    
    SearchTextPlaceholderBrush = None
    
    
    SpinControlArrowBrush = None
    
    
    SpinControlArrowColor = None
    
    
    SpinControlBackgroundBottomColor = None
    
    
    SpinControlBackgroundBrush = None
    
    
    SpinControlBackgroundTopColor = None
    
    
    SpinControlBorderBrush = None
    
    
    SpinControlBorderColor = None
    
    
    SpinControlClickBackgroundBottomColor = None
    
    
    SpinControlClickBackgroundBrush = None
    
    
    SpinControlClickBackgroundTopColor = None
    
    
    SpinControlHighlightColor = None
    
    
    SpinControlHoverBackgroundBottomColor = None
    
    
    SpinControlHoverBackgroundBrush = None
    
    
    SpinControlHoverBackgroundTopColor = None
    
    
    SquareButtonBackgroundBrush = None
    
    
    SquareButtonBackgroundColor = None
    
    
    SquareButtonBorderBrush = None
    
    
    SquareButtonBorderColor = None
    
    
    SquareButtonClickBackgroundBottomColor = None
    
    
    SquareButtonClickBackgroundBrush = None
    
    
    SquareButtonClickBackgroundTopColor = None
    
    
    SquareButtonClickBorderBrush = None
    
    
    SquareButtonClickBorderColor = None
    
    
    SquareButtonClickHighlightBrush = None
    
    
    SquareButtonClickHighlightColor = None
    
    
    SquareButtonDisabledBackgroundBrush = None
    
    
    SquareButtonDisabledBackgroundColor = None
    
    
    SquareButtonDisabledBorderBrush = None
    
    
    SquareButtonDisabledBorderColor = None
    
    
    SquareButtonHoverBackgroundBottomColor = None
    
    
    SquareButtonHoverBackgroundBrush = None
    
    
    SquareButtonHoverBackgroundTopColor = None
    
    
    SquareButtonHoverBorderBrush = None
    
    
    SquareButtonHoverBorderColor = None
    
    
    SquareButtonHoverHighlightBrush = None
    
    
    SquareButtonHoverHighlightColor = None
    
    
    SquareButtonToggledBackgroundBrush = None
    
    
    SquareButtonToggledBackgroundColor = None
    
    
    SquareButtonToggledBorderBrush = None
    
    
    SquareButtonToggledBorderColor = None
    
    
    SquareButtonToggledDisabledBackgroundBrush = None
    
    
    SquareButtonToggledDisabledBackgroundColor = None
    
    
    SquareButtonToggledDisabledBorderBrush = None
    
    
    SquareButtonToggledDisabledBorderColor = None
    
    
    SquareButtonToggledHoverBackgroundBrush = None
    
    
    SquareButtonToggledHoverBackgroundColor = None
    
    
    SquareButtonToggledHoverBorderBrush = None
    
    
    SquareButtonToggledHoverBorderColor = None
    
    
    StatusBarBackgroundBrush = None
    
    
    StatusBarBackgroundColor = None
    
    
    StatusBarInnerBorderBrush = None
    
    
    StatusBarInnerBorderColor = None
    
    
    StatusBarOuterBorderBrush = None
    
    
    StatusBarOuterBorderColor = None
    
    
    StatusBarSeparatorBrush = None
    
    
    StatusBarSeparatorColor = None
    
    
    StatusBarTextBrush = None
    
    
    StatusBarTextColor = None
    
    
    StatusBarTooltipBackgroundBrush = None
    
    
    StatusBarTooltipBackgroundColor = None
    
    
    StatusBarTooltipStateTextBrush = None
    
    
    StatusBarTooltipStateTextColor = None
    
    
    TabBackgroundBrush = None
    
    
    TabBorderBrush = None
    
    
    TabHighlightBrush = None
    
    
    TextInputActiveBackgroundBottomColor = None
    
    
    TextInputActiveBackgroundBrush = None
    
    
    TextInputActiveBackgroundTopColor = None
    
    
    TextInputActiveBorderBrush = None
    
    
    TextInputActiveBorderColor = None
    
    
    TextInputActiveHighlightBrush = None
    
    
    TextInputActiveHighlightColor = None
    
    
    TextInputActiveTextColor = None
    
    
    TextInputBackgroundBrush = None
    
    
    TextInputBackgroundColor = None
    
    
    TextInputBorderBrush = None
    
    
    TextInputBorderColor = None
    
    
    TextInputDisabledTextBrush = None
    
    
    TextInputDisabledTextColor = None
    
    
    TextInputInactiveTextBrush = None
    
    
    TextInputInactiveTextColor = None
    
    
    TextInputInnerShadowColor = None
    
    
    TextInputTextBrush = None
    
    
    TextInputTextColor = None
    
    
    ToolbarBackgroundColor = None
    
    
    ToolbarBorderColor = None
    
    
    ToolbarCloseButtonColor = None
    
    
    ToolbarGripBackgroundColor = None
    
    
    ToolbarGripDarkDotColor = None
    
    
    ToolbarGripLightDotColor = None
    
    
    ToolbarRolloverBorderColor = None
    
    
    TreeControlBorderBrush = None
    
    
    TreeControlBorderColor = None
    
    
    TreeControlDisabledTextBrush = None
    
    
    TreeControlDisabledTextColor = None
    
    
    TreeControlInactiveTextBrush = None
    
    
    TreeControlInactiveTextColor = None
    
    
    TreeControlLineBrush = None
    
    
    TreeControlLineColor = None
    
    
    TreeControlSelectActiveBackgroundBrush = None
    
    
    TreeControlSelectActiveBackgroundColor = None
    
    
    TreeControlSelectBackgroundBrush = None
    
    
    TreeControlSelectBackgroundColor = None
    
    
    TreeControlSelectDisabledTextBrush = None
    
    
    TreeControlSelectDisabledTextColor = None
    
    
    TreeControlSelectInactiveBackgroundBrush = None
    
    
    TreeControlSelectInactiveBackgroundColor = None
    
    
    TreeControlSelectInactiveTextBrush = None
    
    
    TreeControlSelectInactiveTextColor = None
    
    
    TreeControlSelectTextBrush = None
    
    
    TreeControlSelectTextColor = None
    
    
    TreeControlTextBrush = None
    
    
    TreeControlTextColor = None
    
    pass

class PaletteThemeDefaults(object):
    """
    
    """
    DarkOverallColor = None
    
    
    DarkTextColor = None
    
    
    LightOverallColor = None
    
    
    LightTextColor = None
    
    pass

class SizeChangingEventArgs(object):
    """
    
    SizeChangingEventArgs()
    """
    NewSize = None
    
    
    Size = None
    
    pass

class Win32Palette(object):
    """
    
    """
    SourceHWND = None
    
    pass

class Win32PaletteSet(object):
    """
    
    Win32PaletteSet()
    """
    HWND = None
    
    pass

class WindowPositionChangedEventArgs(object):
    """
    
    WindowPositionChangedEventArgs()
    """
    Moved = None
    
    
    Sized = None
    
    pass