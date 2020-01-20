class AboutToBeginBackgroundPublishingEventArgs(EventArgs):
    """
    
    """
    def ReadPrivateSection(self):
        """
        ReadPrivateSection -> IDictionaryEnumerator
            
            string sectionName: 
            Input name to read
        """
        pass
    
    
    def WritePrivateSection(self):
        """
        WritePrivateSection -> void
            
            string sectionName: 
            Input section
            
            IDictionaryEnumerator data: 
            Input data to write
        """
        pass
    
    
    DsdData = None
    
    
    JobWillPublishInBackground = None
    
    pass

class AboutToBeginPublishingEventArgs(EventArgs):
    """
    
    """
    def ReadPrivateSection(self):
        """
        ReadPrivateSection -> IDictionaryEnumerator
            
            string sectionName: 
            Input name to read
        """
        pass
    
    
    def WritePrivateSection(self):
        """
        WritePrivateSection -> void
            
            string sectionName: 
            Input section
            
            IDictionaryEnumerator data: 
            Input data to write
        """
        pass
    
    
    DsdData = None
    
    
    JobWillPublishInBackground = None
    
    
    PlotLogger = None
    
    pass

class BeginAggregationEventArgs(EventArgs):
    """
    
    """
    def AddGlobalPropertyRange(self):
        """
        AddGlobalPropertyRange -> void
            
            EPlotProperty[] properties: 
            Input property to add
        """
        pass
    
    
    def AddGlobalResourceRange(self):
        """
        AddGlobalResourceRange -> void
            
            EPlotResource[] resources: 
            Input resource to add
        """
        pass
    
    
    DwfFileName = None
    
    
    DwfPassword = None
    
    
    PlotLogger = None
    
    pass

class BeginPublishingSheetEventArgs(EventArgs):
    """
    
    """
    DsdEntry = None
    
    
    PlotLogger = None
    
    
    UniqueId = None
    
    pass

class Dwf3dNavigationTreeNode(RXObject):
    """
    
    D
    
    w
    
    f
    
    3
    
    d
    
    N
    
    a
    
    v
    
    i
    
    g
    
    a
    
    t
    
    i
    
    o
    
    n
    
    T
    
    r
    
    e
    
    e
    
    N
    
    o
    
    d
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    def GetKeys(self):
        """
        GetKeys -> int()
        
        """
        pass
    
    
    def SetKeys(self):
        """
        SetKeys -> void
            
            int[] keys: 
            Input array of keys
        """
        pass
    
    
    Children = None
    
    
    DisplayName = None
    
    
    IsBlock = None
    
    
    IsGroup = None
    
    pass

class Dwf3dNavigationTreeNodeCollection(public sealed class Dwf3dNavigationTreeNodeCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Dwf3dNavigationTreeNode node: 
            Input node to be added to this collection
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            Dwf3dNavigationTreeNode node: 
            Input node to be removed from this collection.
        """
        pass
    
    
    Count = None
    
    pass

class DwfNode(public sealed class DwfNode):
    """
    
    D
    
    w
    
    f
    
    N
    
    o
    
    d
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    NodeId = None
    
    
    NodeName = None
    
    pass

class EPlotAttribute(public sealed class EPlotAttribute):
    """
    
    E
    
    P
    
    l
    
    o
    
    t
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    Name = None
    
    
    Ns = None
    
    
    NsUrl = None
    
    
    Value = None
    
    pass

class EPlotAttributeCollection(ICollection, IEnumerable):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            EPlotAttribute value: 
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
            
            Array array: 
            Input target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    
    IsSynchronized = None
    
    
    SyncRoot = None
    
    pass

class EPlotProperty(public sealed class EPlotProperty):
    """
    
    E
    
    P
    
    l
    
    o
    
    t
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    (
    
    )
    
    (
    
    )
    """
    def AddEplotAttribute(self):
        """
        AddEplotAttribute -> void
            
            EPlotAttribute att: 
            Input XML attribute object to be added to the XML attributes vector.
        """
        pass
    
    
    def AddEPlotAttribute(self):
        """
        AddEPlotAttribute -> void
            
            string ns: 
            Input namespace name.
            
            string nsUrl: 
            Input the attribute's namespace location.
            
            string attName: 
            Input attribute name.
            
            string attValue: 
            Input attribute value.
        """
        pass
    
    
    Attributes = None
    
    
    Category = None
    
    
    Name = None
    
    
    Type = None
    
    
    Units = None
    
    
    Value = None
    
    pass

class EPlotPropertyBag(public sealed class EPlotPropertyBag):
    """
    
    E
    
    P
    
    l
    
    o
    
    t
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    B
    
    a
    
    g
    
    (
    
    )
    
    (
    
    )
    """
    Id = None
    
    
    NamespaceLocation = None
    
    
    NamespaceUrl = None
    
    
    Properties = None
    
    
    References = None
    
    pass

class EPlotPropertyCollection(ICollection, IEnumerable):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            EPlotProperty value: 
            Input object to add
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
            
            Array array: 
            Input target array.
            
            int index: 
            Input zero-based index from which the copying begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    
    IsSynchronized = None
    
    
    SyncRoot = None
    
    pass

class EPlotResource(public sealed class EPlotResource):
    """
    
    E
    
    P
    
    l
    
    o
    
    t
    
    R
    
    e
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    (
    
    )
    
    (
    
    )
    """
    Mime = None
    
    
    Path = None
    
    
    Role = None
    
    pass

class OptionsDialogResult(public struct OptionsDialogResult {
}):
    """
    
    """
    DsdData = None
    
    
    PlotConfig = None
    
    
    Status = None
    
    pass

class PublishEntityEventArgs(EventArgs):
    """
    
    """
    def Add3DDwfProperty(self):
        """
        Add3DDwfProperty -> bool
            
            string category: 
            Input name of the category to which you want to add the property.
            
            string name: 
            Input property name.
            
            string value: 
            Input property value.
        """
        pass
    
    
    def AddNodeToMap(self):
        """
        AddNodeToMap -> bool
            
            ObjectId entityId: 
            Input object of the entity whose node ID is to be assigned.
            
            ObjectIdCollection objIds: 
            Input array of object IDs for each block that encloses this entity; an empty array if this entity is not part of a block.
            
            int nodeId: 
            Input the integer node ID to be assigned to the specified entity; should be greater than 0.
        """
        pass
    
    
    def AddPropertiesIds(self):
        """
        AddPropertiesIds -> bool
            
            EPlotPropertyBag properties: 
            Input property to add
            
            DwfNode node: 
            Input the node with which properties should be associated.
        """
        pass
    
    
    def AddPropertyBag(self):
        """
        AddPropertyBag -> bool
            
            EPlotPropertyBag properties: 
            Input property bag to add
        """
        pass
    
    
    def Cancel(self):
        """
        Cancel -> void
        
        """
        pass
    
    
    def Flush(self):
        """
        Flush -> void
        
        """
        pass
    
    
    def GetCurrentEntityNode(self):
        """
        GetCurrentEntityNode -> DwfNode
            
            ObjectIdCollection objIds: 
            Input collection holder
        """
        pass
    
    
    def getEntityBlockRefPath(self):
        """
        getEntityBlockRefPath -> ObjectIdCollection
        
        """
        pass
    
    
    def GetEntityNode(self):
        """
        GetEntityNode -> Integer
            
            ObjectId entityId: 
            Input object to look up.
            
            ObjectIdCollection objIds: 
            Input array of object IDs for each block that encloses this entity; may be an empty array if this entity is not part of a block.
        """
        pass
    
    
    def GetGraphicIDs(self):
        """
        GetGraphicIDs -> int()
        
        """
        pass
    
    
    def GetNextAvailableNode(self):
        """
        GetNextAvailableNode -> Integer
        
        """
        pass
    
    
    def SetCurrentNode(self):
        """
        SetCurrentNode -> bool
            
            int nodeId: 
            Input node ID to assign.
            
            ObjectIdCollection objIds: 
            Input array of object IDs for each block that encloses this entity; an empty array if this entity is not part of a block.
        """
        pass
    
    
    def SetNodeName(self):
        """
        SetNodeName -> bool
            
            int nodeId: 
            Input node ID on which to operate, which should exist in the map and should be greater than 0
            
            string nodeName: 
            Input node name to assign to the specified node.
        """
        pass
    
    
    EffectiveBlockLayerId = None
    
    
    Entity = None
    
    
    IsCancelled = None
    
    
    PlotLogger = None
    
    
    UniqueEntityId = None
    
    pass

class PublishEventArgs(EventArgs):
    """
    
    """
    DwfFileName = None
    
    
    DwfPassword = None
    
    
    IsMultiSheetDwf = None
    
    
    TemporaryDwfFileName = None
    
    pass

class PublishSheetEventArgs(EventArgs):
    """
    
    """
    def AddPagePropertyRange(self):
        """
        AddPagePropertyRange -> void
            
            EPlotProperty[] properties: 
            Input page properties range
        """
        pass
    
    
    def AddPageResourceRange(self):
        """
        AddPageResourceRange -> void
            
            EPlotResource[] resources: 
            Input page resource range
        """
        pass
    
    
    AreLinesHidden = None
    
    
    ArePlottingLineWeights = None
    
    
    AreScalingLineWeights = None
    
    
    CanonicalMediaName = None
    
    
    Configuration = None
    
    
    Database = None
    
    
    DisplayMaxX = None
    
    
    DisplayMaxY = None
    
    
    DisplayMinX = None
    
    
    DisplayMinY = None
    
    
    DrawingScale = None
    
    
    Dwf3dNavigationTreeNode = None
    
    
    EffectivePlotOffsetX = None
    
    
    EffectivePlotOffsetXDevice = None
    
    
    EffectivePlotOffsetY = None
    
    
    EffectivePlotOffsetYDevice = None
    
    
    IsModelLayout = None
    
    
    IsPlotJobCancelled = None
    
    
    IsScaleSpecified = None
    
    
    LayoutBoundsMaxX = None
    
    
    LayoutBoundsMaxY = None
    
    
    LayoutBoundsMinX = None
    
    
    LayoutBoundsMinY = None
    
    
    LayoutMarginMaxX = None
    
    
    LayoutMarginMaxY = None
    
    
    LayoutMarginMinX = None
    
    
    LayoutMarginMinY = None
    
    
    MaxBoundsX = None
    
    
    MaxBoundsY = None
    
    
    OriginX = None
    
    
    OriginY = None
    
    
    PaperScale = None
    
    
    PlotBoundsMaxX = None
    
    
    PlotBoundsMaxY = None
    
    
    PlotBoundsMinX = None
    
    
    PlotBoundsMinY = None
    
    
    PlotLayoutId = None
    
    
    PlotLogger = None
    
    
    PlotPaperUnit = None
    
    
    PlotRotation = None
    
    
    PlotToFileName = None
    
    
    PlotToFilePath = None
    
    
    PlotType = None
    
    
    PlotWindowMaxX = None
    
    
    PlotWindowMaxY = None
    
    
    PlotWindowMinX = None
    
    
    PlotWindowMinY = None
    
    
    PrintableBoundsX = None
    
    
    PrintableBoundsY = None
    
    
    PublishingTo3DDwf = None
    
    
    StepsPerInch = None
    
    
    UniqueLayoutId = None
    
    
    ViewPlotted = None
    
    pass

class PublishUIEventArgs(EventArgs):
    """
    
    """
    def ReadPrivateSection(self):
        """
        ReadPrivateSection -> IDictionaryEnumerator
            
            string sectionName: 
            Input section name to read from
        """
        pass
    
    
    def WritePrivateSection(self):
        """
        WritePrivateSection -> void
            
            string sectionName: 
            Input section name to write to
            
            IDictionaryEnumerator data: 
            Input data to write
        """
        pass
    
    
    DsdData = None
    
    
    IUnknown = None
    
    
    JobWillPublishInBackground = None
    
    pass

class Publisher(MarshalByRefObject):
    """
    
    """
    def FireAboutToBeginBackgroundPublishing(self):
        """
        FireAboutToBeginBackgroundPublishing -> void
            
            AboutToBeginBackgroundPublishingEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireAboutToBeginPublishing(self):
        """
        FireAboutToBeginPublishing -> void
            
            AboutToBeginPublishingEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireAboutToEndPublishing(self):
        """
        FireAboutToEndPublishing -> void
            
            PublishEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireAboutToMoveFile(self):
        """
        FireAboutToMoveFile -> void
            
            PublishEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireBeginAggregation(self):
        """
        FireBeginAggregation -> void
            
            BeginAggregationEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireBeginEntity(self):
        """
        FireBeginEntity -> void
            
            PublishEntityEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireBeginPublishingSheet(self):
        """
        FireBeginPublishingSheet -> void
            
            BeginPublishingSheetEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireBeginSheet(self):
        """
        FireBeginSheet -> void
            
            PublishSheetEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireCancelledOrFailedPublishing(self):
        """
        FireCancelledOrFailedPublishing -> void
            
            PublishEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireEndEntity(self):
        """
        FireEndEntity -> void
            
            PublishEntityEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireEndPublish(self):
        """
        FireEndPublish -> void
            
            PublishEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireEndSheet(self):
        """
        FireEndSheet -> void
            
            PublishSheetEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def FireInitPublishOptionsDialog(self):
        """
        FireInitPublishOptionsDialog -> void
            
            PublishUIEventArgs e: 
            Input event argument to launch
        """
        pass
    
    
    def PublishDsd(self):
        """
        PublishDsd -> Integer
            
            string dsdFile: 
            Input file to publish
            
            PlotProgressDialog plotProgressDialog: 
            Input plot progress dialog
        """
        pass
    
    
    def PublishExecute(self):
        """
        PublishExecute -> void
            
            DsdData dsdData: 
            Input data to execute
            
            PlotConfig plotConfig: 
            Input plot progress dialog
        """
        pass
    
    
    def PublishSelectedLayouts(self):
        """
        PublishSelectedLayouts -> void
            
            [MarshalAs(UnmanagedType.U1)] bool bOverride: 
            Input true if there are overrides.
        """
        pass
    
    
    def ShowDwfOptionsDialog(self):
        """
        ShowDwfOptionsDialog -> OptionsDialogResult
            
            DsdData dsdData: 
            Input data to execute
            
            PlotConfig plotConfig: 
            Input plot progress dialog
            
            string optionsDialogTitle: 
            Input title of options
        """
        pass
    
    
    def ShowPublishDialog(self):
        """
        ShowPublishDialog -> void
            
            DsdData dsdData: 
            Input data to execute
            
            PlotConfig plotConfig: 
            Input plot progress dialog
            
            StringCollection namePageSetups: 
            Input name of page setups
            
            StringCollection namePageSetupPaths: 
            Input name of page setup paths
            
            string optionsDialogTitle: 
            Input title of options
            
            string optionsButtonText: 
            Input title of buttons
        """
        pass
    
    
    CurrentPublishedSheetSetPath = None
    
    pass