  All = 0x1f
  New = 1
  None = 0
  Open = 2
  Redo = 0x10
  Save = 4
  Undo = 8

class QuickAccessToolBarSource(ToolBarSource, IPersistentObjectSource):
    """
    
    """
    def AddStandardItem(self):
        """
        AddStandardItem -> void
            
            RibbonItem item: 
            The standard item to be added to the quick access toolbar.
            
            Exceptions: 
            Description
            
            System.ArgumentNullException: 
            The specified item is null.
            
            System.ArgumentException: 
            The item is an existing default standard command.
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            ToolBarSource toolBarSource: 
            A Autodesk.Windows.ToolBars.ToolBarSource that contains the properties to duplicate.
        """
        pass
    
    
    def FindStandardCommand(self):
        """
        FindStandardCommand -> RibbonItem
            
            QuickAccessStandardCommands commandId: 
            The standard command id.
        """
        pass
    
    
    def RemoveStandardItem(self):
        """
        RemoveStandardItem -> void
            
            RibbonItem item: 
            The standard item to be removed from the quick access toolbar.
            
            Exceptions: 
            Description
            
            System.ArgumentException: 
            Cannot find item in the standard item collection! Cannot remove a default command from the quick access toolbar!
            
            System.ArgumentNullException: 
            The specified item cannot be null.
        """
        pass
    
    
    def StandardCommandId(self):
        """
        StandardCommandId -> string
            
            QuickAccessStandardCommands commandId: 
            The standard command id.
        """
        pass
    
    
    DefaultCommands = None
    
    
    IsMenuBarVisible = None
    
    pass

class QuickAccessToolBarTraySource(ToolBarTraySource):
    """
    
    """
    Source Field = None
    
    pass

class StatusBarSource(ToolBarSource):
    """
    
    """
    CustomizeMenuPlacement Field = None
    
    
    OverflowPopupPlacement Field = None
    
    pass

class StatusBarTraySource(ToolBarTraySource):
    """
    
    """

    pass

class ToolBarSource(ICloneable, IToolBarCustomization, INotifyPropertyChanged):
    """
    
    """

    pass