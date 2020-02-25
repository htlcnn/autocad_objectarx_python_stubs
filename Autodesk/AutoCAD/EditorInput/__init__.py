class AcMgdLivePreviewAction(object):
    """
    
    """

    pass

class AcMgdLivePreviewContextReactor(object):
    """
    
    """

    pass

class AcMgdLivePreviewReactor(object):
    """
    
    """

    pass

class AddedKeywords():
    All = 4
    CrossingCPolygon = 0x20
    Fence = 0x40
    Group = 0x400
    Last = 0x80
    LastAllPrevious = 1
    Multiple = 0x10
    PickImplied = 2
    Previous = 0x100
    WindowCrossingBoxWPolygonCPolygon = 8
    WindowWPolygon = 0x200

class ConstraintUtilities(object):
    """
    
    """
    def ShowConstraintBar(self):
        """
        ShowConstraintBar -> bool
            
            FullSubentityPath[] subentityPaths: 
            Array of full sub-entity paths of entities for which constraint bars are to be shown or hidden. If this array is empty, the show/hide action will then be applied to all constrained entities in the active document. 
            
            [MarshalAs(UnmanagedType.U1)] bool bToShow: 
             Set this to true to show constraint bars, set to false to hide constraint bars. 
        """
        pass
    
    pass

class CrossingOrWindowSelectedObject(object):
    """
    
    CrossingOrWindowSelectedObject(ObjectId, SelectionMethod, IntPtr)
        ObjectId id : Input ID of crossing object
        SelectionMethod method : Input method to select object
        IntPtr gsMarker : Input any GS markers
    
    
    CrossingOrWindowSelectedObject(ObjectId, SelectionMethod, long)
        ObjectId id : Input ID of crossing object
        SelectionMethod method : Input method to select object
        long gsMarker : Input any GS markers
    
    
    """
    def GetPickPoints(self):
        """
        GetPickPoints -> PickPointDescriptor()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture specific format
        """
        pass
    
    pass

class CrossingOrWindowSelectedSubObject(object):
    """
    
    CrossingOrWindowSelectedSubObject(FullSubentityPath, SelectionMethod, IntPtr)
        FullSubentityPath path : Input path of object
        SelectionMethod method : Input method of selection
        IntPtr gsMarker : Input any GS markers
    
    
    CrossingOrWindowSelectedSubObject(FullSubentityPath, SelectionMethod, long)
        FullSubentityPath path : Input path of object
        SelectionMethod method : Input method of selection
        long gsMarker : Input any GS markers
    
    
    """
    def GetPickPoints(self):
        """
        GetPickPoints -> PickPointDescriptor()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    pass

class CursorBadgeUtilities(object):
    """
    
    """
    def AddSupplementalCursorImage(self):
        """
        AddSupplementalCursorImage -> bool
            
            ImageBGRA32 cursorImage: 
            Input image
            
            int priority: 
            Stacking order badge should appear in. Higher numbers win.
        """
        pass
    
    
    def GetSupplementalCursorOffset(self):
        """
        GetSupplementalCursorOffset -> void
            
            y: 
            y offset
        """
        pass
    
    
    def HasSupplementalCursorImage(self):
        """
        HasSupplementalCursorImage -> bool
        
        """
        pass
    
    
    def RemoveSupplementalCursorImage(self):
        """
        RemoveSupplementalCursorImage -> bool
            
            ImageBGRA32 cursorImage: 
            Input image
        """
        pass
    
    
    def SetSupplementalCursorOffset(self):
        """
        SetSupplementalCursorOffset -> void
            
            int y: 
            Input Y offset
        """
        pass
    
    pass

class CursorType():
    Crosshair = 0
    CrosshairNoRotate = 6
    EntitySelect = 8
    EntitySelectNoPerspective = 10
    Invisible = 7
    NoSpecialCursor = -1
    NotRotated = 3
    Parallelogram = 9
    PickfirstOrGrips = 11
    RectangularCursor = 1
    RotatedCrosshair = 5
    RubberBand = 2
    TargetBox = 4

class DragCursor():
    Normal = None
    Selection = None

class DrawJig(object):
    """
    
    """

    pass

class Editor(object):
    """
    
    """
    PauseToken = None
    
    
    def DoPrompt(self):
        """
        DoPrompt -> PromptResult
            
            PromptOptions opt: 
            Input options for the prompt
        """
        pass
    
    
    def Drag(self):
        """
        Drag(Jig) -> PromptResult
            
            Jig jig: 
            Input the jig to drag
        Drag(PromptDragOptions) -> PromptPointResult
            
            PromptDragOptions options: 
            Input dragging options
        Drag(SelectionSet, string, DragCallback) -> PromptPointResult
            
            SelectionSet selection: 
            Input the selection set
            
            string message: 
            Input the prompt message
            
            DragCallback callback: 
            Input any drag callbacks
        """
        pass
    
    
    def DrawVector(self):
        """
        DrawVector -> void
            
            Point3d from: 
            Input beginning point
            
            Point3d to: 
            Input ending point
            
            int color: 
            Input color of vector
            
            [MarshalAs(UnmanagedType.U1)] bool drawHighlighted: 
            Input Boolean value indicated of the vector ought to be highlighted
        """
        pass
    
    
    def DrawVectors(self):
        """
        DrawVectors -> void
            
            ResultBuffer rb: 
            Input result buffer containing vectors
            
            Matrix3d transform: 
            Input transformation matrix
        """
        pass
    
    
    def ApplyCurDwgLayerTableChanges(self):
        """
        ApplyCurDwgLayerTableChanges -> void
        
        """
        pass
    
    
    def Command(self):
        """
        Command -> void
        
        """
        pass
    
    
    def CommandAsync(self):
        """
        CommandAsync -> CommandResult
        
        """
        pass
    
    
    def PostCommandPrompt(self):
        """
        PostCommandPrompt -> void
        
        """
        pass
    
    
    def GetAngle(self):
        """
        GetAngle(PromptAngleOptions) -> PromptDoubleResult
            
            PromptAngleOptions options: 
            Input optional parameters of the prompt.
        GetAngle(string) -> PromptDoubleResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
        """
        pass
    
    
    def GetCommandVersion(self):
        """
        GetCommandVersion -> Integer
        
        """
        pass
    
    
    def GetCorner(self):
        """
        GetCorner(PromptCornerOptions) -> PromptPointResult
            
            PromptCornerOptions options: 
            Input optional parameters of the prompt.
        GetCorner(string, Point3d) -> PromptPointResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
            
            Point3d basePoint: 
            Input the first corner of the rectangle being selected.
        """
        pass
    
    
    def StartUserInteraction(self):
        """
        StartUserInteraction -> EditorUserInteraction
            
            modalForm: 
            Input control form
        """
        pass
    
    
    def GetCurrentView(self):
        """
        GetCurrentView -> ViewTableRecord
        
        """
        pass
    
    
    def GetDistance(self):
        """
        GetDistance(PromptDistanceOptions) -> PromptDoubleResult
            
            PromptDistanceOptions options: 
            Input optional parameters of the prompt.
        GetDistance(string) -> PromptDoubleResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
        """
        pass
    
    
    def GetDouble(self):
        """
        GetDouble(PromptDoubleOptions) -> PromptDoubleResult
            
            PromptDoubleOptions options: 
            Input optional parameters of the prompt.
        GetDouble(string) -> PromptDoubleResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
        """
        pass
    
    
    def TraceBoundary(self):
        """
        TraceBoundary -> DBObjectCollection
            
            Point3d seedPoint: 
            The seed point, in UCS, for the boundary trace.
            
            [MarshalAs(UnmanagedType.U1)] bool detectIslands: 
            A boolean indicating whether or not to detect islands.
        """
        pass
    
    
    def GetEntity(self):
        """
        GetEntity(PromptEntityOptions) -> PromptEntityResult
            
            PromptEntityOptions options: 
            Input optional parameters of the prompt.
        GetEntity(string) -> PromptEntityResult
            
            string message: 
            Input prompt message
        """
        pass
    
    
    def GetFileNameForOpen(self):
        """
        GetFileNameForOpen(PromptOpenFileOptions) -> PromptFileNameResult
            
            PromptOpenFileOptions options: 
            Input file opening options
        GetFileNameForOpen(string) -> PromptFileNameResult
            
            string message: 
            Input prompt string
        """
        pass
    
    
    def GetFileNameForSave(self):
        """
        GetFileNameForSave(PromptSaveFileOptions) -> PromptFileNameResult
            
            PromptSaveFileOptions options: 
            Input file saving options
        GetFileNameForSave(string) -> PromptFileNameResult
            
            string message: 
            Input prompt message
        """
        pass
    
    
    def TurnSubentityWindowSelectionOff(self):
        """
        TurnSubentityWindowSelectionOff -> void
        
        """
        pass
    
    
    def GetInteger(self):
        """
        GetInteger(PromptIntegerOptions) -> PromptIntegerResult
            
            PromptIntegerOptions options: 
            Input optional parameters of the prompt.
        GetInteger(string) -> PromptIntegerResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
        """
        pass
    
    
    def TurnSubentityWindowSelectionOn(self):
        """
        TurnSubentityWindowSelectionOn -> void
        
        """
        pass
    
    
    def GetKeywords(self):
        """
        GetKeywords(PromptKeywordOptions) -> PromptResult
            
            PromptKeywordOptions options: 
            Input optional parameters of the prompt.
        GetKeywords(string, params string[]) -> PromptResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
            
            params string[] globalKeywords: 
            Input keywords from which the user is prompted to choose.
        """
        pass
    
    
    def GetNestedEntity(self):
        """
        GetNestedEntity(PromptNestedEntityOptions) -> PromptNestedEntityResult
            
            PromptNestedEntityOptions options: 
            Input optional parameters of the prompt.
        GetNestedEntity(string) -> PromptNestedEntityResult
            
            string message: 
            Input message to be displayed to the user during the prompt
        """
        pass
    
    
    def GetPoint(self):
        """
        GetPoint(PromptPointOptions) -> PromptPointResult
            
            PromptPointOptions options: 
            Input optional parameters of the prompt.
        GetPoint(string) -> PromptPointResult
            
            string message: 
            Input message to be displayed to the user during the prompt.
        """
        pass
    
    
    def GetSelection(self):
        """
        GetSelection() -> PromptSelectionResult
        
        GetSelection(PromptSelectionOptions) -> PromptSelectionResult
            
            PromptSelectionOptions options: 
            Input selection options
        GetSelection(PromptSelectionOptions, SelectionFilter) -> PromptSelectionResult
            
            PromptSelectionOptions options: 
            Input selection options
            
            SelectionFilter filter: 
            Input selection filter
        GetSelection(SelectionFilter) -> PromptSelectionResult
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def GetString(self):
        """
        GetString(PromptStringOptions) -> PromptResult
            
            PromptStringOptions options: 
            Input optional parameters of the prompt.
        GetString(string) -> PromptResult
            
            string message: 
            Input message to be displayed to the user during the prompt
        """
        pass
    
    
    def GetViewportNumber(self):
        """
        GetViewportNumber -> Integer
            
            Point point: 
            Input point to get viewport number from
        """
        pass
    
    
    def InitCommandVersion(self):
        """
        InitCommandVersion -> Integer
            
            int nVersion: 
            The new version variable to set
        """
        pass
    
    
    def PointToScreen(self):
        """
        PointToScreen -> Point
            
            Point3d pt: 
            Input point to grab
            
            int viewportNumber: 
            Input the point's viewport number
        """
        pass
    
    
    def Regen(self):
        """
        Regen -> void
        
        """
        pass
    
    
    def SelectAll(self):
        """
        SelectAll() -> PromptSelectionResult
        
        SelectAll(SelectionFilter) -> PromptSelectionResult
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def SelectCrossingPolygon(self):
        """
        SelectCrossingPolygon(Point3dCollection) -> PromptSelectionResult
            
            Point3dCollection polygon: 
            Input collection of points that represent vertices of the polygon.
        SelectCrossingPolygon(Point3dCollection, SelectionFilter) -> PromptSelectionResult
            
            Point3dCollection polygon: 
            Input collection of points that represent vertices of the polygon.
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def SelectCrossingWindow(self):
        """
        SelectCrossingWindow(Point3d, Point3d) -> PromptSelectionResult
            
            Point3d pt1: 
            Input first corner of selection window
            
            Point3d pt2: 
            Input opposite corner of selection window
        SelectCrossingWindow(Point3d, Point3d, SelectionFilter) -> PromptSelectionResult
            
            Point3d pt1: 
            Input first corner of selection window
            
            Point3d pt2: 
            Input opposite corner of selection window
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def SelectFence(self):
        """
        SelectFence(Point3dCollection) -> PromptSelectionResult
            
            Point3dCollection fence: 
            Input collection of points that represent vertices of the fence.
        SelectFence(Point3dCollection, SelectionFilter) -> PromptSelectionResult
            
            Point3dCollection fence: 
            Input collection of points that represent vertices of the fence.
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def SelectLast(self):
        """
        SelectLast -> PromptSelectionResult
        
        """
        pass
    
    
    def SelectPrevious(self):
        """
        SelectPrevious -> PromptSelectionResult
        
        """
        pass
    
    
    def SelectWindow(self):
        """
        SelectWindow(Point3d, Point3d) -> PromptSelectionResult
            
            Point3d pt1: 
            Input first corner of selection window.
            
            Point3d pt2: 
            Input opposite corner of selection window.
        SelectWindow(Point3d, Point3d, SelectionFilter) -> PromptSelectionResult
            
            Point3d pt1: 
            Input first corner of selection window
            
            Point3d pt2: 
            Input opposite corner of selection window
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def SelectWindowPolygon(self):
        """
        SelectWindowPolygon(Point3dCollection) -> PromptSelectionResult
            
            Point3dCollection polygon: 
            Input collection of points that represent vertices of the polygon.
        SelectWindowPolygon(Point3dCollection, SelectionFilter) -> PromptSelectionResult
            
            Point3dCollection polygon: 
            Input collection of points that represent vertices of the polygon.
            
            SelectionFilter filter: 
            Input selection filter
        """
        pass
    
    
    def SetCurrentView(self):
        """
        SetCurrentView -> void
            
            ViewTableRecord value: 
            Input new view table record value
        """
        pass
    
    
    def Snap(self):
        """
        Snap -> Point3d
            
            string snapMode: 
            Input new snap mode
            
            Point3d input: 
            Input point to place snap mode
        """
        pass
    
    
    def SwitchToModelSpace(self):
        """
        SwitchToModelSpace -> void
        
        """
        pass
    
    
    def SwitchToPaperSpace(self):
        """
        SwitchToPaperSpace -> void
        
        """
        pass
    
    
    def TurnForcedPickOff(self):
        """
        TurnForcedPickOff -> Integer
        
        """
        pass
    
    
    def TurnForcedPickOn(self):
        """
        TurnForcedPickOn -> Integer
        
        """
        pass
    
    
    def UpdateScreen(self):
        """
        UpdateScreen -> void
        
        """
        pass
    
    
    def UpdateTiledViewportsFromDatabase(self):
        """
        UpdateTiledViewportsFromDatabase -> void
        
        """
        pass
    
    
    def UpdateTiledViewportsInDatabase(self):
        """
        UpdateTiledViewportsInDatabase -> void
        
        """
        pass
    
    
    def ViewportIdFromNumber(self):
        """
        ViewportIdFromNumber -> ObjectId
            
            int viewportNumber: 
            Input viewport number
        """
        pass
    
    
    def WriteMessage(self):
        """
        WriteMessage(string) -> void
            
            string message: 
            Input messsage
        WriteMessage(string, params object[]) -> void
            
            string message: 
            Input message
            
            params object[] parameter: 
            Input array of objects to include
        """
        pass
    
    
    ActiveViewportId = None
    
    
    CurrentUserCoordinateSystem = None
    
    
    CurrentViewportObjectId = None
    
    
    Document = None
    
    
    IsDragging = None
    
    
    IsQuiescent = None
    
    
    IsQuiescentForTransparentCommand = None
    
    
    MouseHasMoved = None
    
    
    UseCommandLineInterface = None
    
    
    class CommandResult(object):
        """
        
        """
        def GetAwaiter(self):
            """
            GetAwaiter -> Editor.CommandResult
            
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
    
    pass

class EditorExtension(object):
    """
    
    """
    def GetViewportNumber(self):
        """
        GetViewportNumber -> Integer
        
        """
        pass
    
    
    def PointToScreen(self):
        """
        PointToScreen -> Point
        
        """
        pass
    
    
    def PointToWorld(self):
        """
        PointToWorld(this Editor, Point) -> Point3d
        
        PointToWorld(this Editor, Point, int) -> Point3d
        
        """
        pass
    
    
    def StartUserInteraction(self):
        """
        StartUserInteraction -> EditorUserInteraction
        
        """
        pass
    
    pass

class EditorUserInteraction(object):
    """
    
    """
    def End(self):
        """
        End -> void
        
        """
        pass
    
    pass

class EditorVisualStyle(object):
    """
    
    """
    def setCvpVS2d(self):
        """
        setCvpVS2d -> void
        
        """
        pass
    
    
    IsVS2dType = None
    
    
    IsVS3dType = None
    
    pass

class EntityJig(object):
    """
    
    """

    pass

class FenceSelectedObject(object):
    """
    
    FenceSelectedObject(ObjectId, SelectionMethod, IntPtr, PickPointDescriptor[])
        ObjectId id : Input object to fence
        SelectionMethod method : Input selection method
        IntPtr gsMarker : Input GS markers
        PickPointDescriptor[] descriptors : Input pick point descriptors
    
    
    FenceSelectedObject(ObjectId, SelectionMethod, long, PickPointDescriptor[])
        ObjectId id : Input object to fence
        SelectionMethod method : Input selection method
        long gsMarker : Input GS markers
        PickPointDescriptor[] descriptors : Input pick point descriptors
    
    
    """
    def GetIntersectionPoints(self):
        """
        GetIntersectionPoints -> PickPointDescriptor[]
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    pass

class FenceSelectedSubObject(object):
    """
    
    FenceSelectedSubObject(FullSubentityPath, SelectionMethod, IntPtr, PickPointDescriptor[])
        FullSubentityPath path : Input subentitiy path
        SelectionMethod method : Input selection method
        IntPtr gsMarker : Input GS marker
        PickPointDescriptor[] descriptors : Input pick points
    
    
    FenceSelectedSubObject(FullSubentityPath, SelectionMethod, long, PickPointDescriptor[])
        FullSubentityPath path : Input subentitiy path
        SelectionMethod method : Input selection method
        long gsMarker : Input GS marker
        PickPointDescriptor[] descriptors : Input pick points
    
    
    """
    def GetIntersectionPoints(self):
        """
        GetIntersectionPoints -> PickPointDescriptor[]
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    pass

class InputPointContext(object):
    """
    
    """
    def GetAlignmentPaths(self):
        """
        GetAlignmentPaths -> Curve3d()
        
        """
        pass
    
    
    def GetCustomObjectSnapModes(self):
        """
        GetCustomObjectSnapModes -> CustomObjectSnapMode()
        
        """
        pass
    
    
    def GetCustomObjectSnapOverrides(self):
        """
        GetCustomObjectSnapOverrides -> CustomObjectSnapMode()
        
        """
        pass
    
    
    def GetKeyPointEntities(self):
        """
        GetKeyPointEntities -> FullSubentityPath()
        
        """
        pass
    
    
    def GetPickedEntities(self):
        """
        GetPickedEntities -> FullSubentityPath()
        
        """
        pass
    
    
    CartesianSnappedPoint = None
    
    
    ComputedPoint = None
    
    
    Document = None
    
    
    DrawContext = None
    
    
    GrippedPoint = None
    
    
    History = None
    
    
    LastPoint = None
    
    
    ObjectSnapMask = None
    
    
    ObjectSnapOverrides = None
    
    
    ObjectSnappedPoint = None
    
    
    PointComputed = None
    
    
    RawPoint = None
    
    
    ToolTipText = None
    
    pass

class Jig(object):
    """
    
    """

    pass

class JigPromptAngleOptions(object):
    """
    
    JigPromptAngleOptions()()
    
    
    JigPromptAngleOptions(string)
        string message : Input prompt message
    
    
    JigPromptAngleOptions(string, string)
        string messageAndKeywords : Input prompt message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    DefaultValue = None
    
    pass

class JigPromptDistanceOptions(object):
    """
    
    JigPromptDistanceOptions()()
    
    
    JigPromptDistanceOptions(string)
        string message : Input prompt message
    
    
    JigPromptDistanceOptions(string, string)
        string messageAndKeywords : Input prompt message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    DefaultValue = None
    
    pass

class JigPromptGeometryOptions(object):
    """
    
    JigPromptGeometryOptions()()
    
    
    JigPromptGeometryOptions(string)
        string message : Input prompt message
    
    
    JigPromptGeometryOptions(string, string)
        string messageAndKeywords : Input prompt message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    BasePoint = None
    
    
    UseBasePoint = None
    
    pass

class JigPromptOptions(object):
    """
    
    """
    Cursor = None
    
    
    UserInputControls = None
    
    pass

class JigPromptPointOptions(object):
    """
    
    JigPromptPointOptions()()
    
    
    JigPromptPointOptions(string)
        string message : Input prompt string
    
    
    JigPromptPointOptions(string, string)
        string messageAndKeywords : Input prompt message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    DefaultValue = None
    
    pass

class JigPromptStringOptions(object):
    """
    
    JigPromptStringOptions()()
    
    
    JigPromptStringOptions(string)
        string message : Input prompt message
    
    
    JigPromptStringOptions(string, string)()
    
    
    """
    DefaultValue = None
    
    pass

class JigPrompts(object):
    """
    
    """
    def AcquireAngle(self):
        """
        AcquireAngle() -> PromptDoubleResult
        
        AcquireAngle(JigPromptAngleOptions) -> PromptDoubleResult
            
            JigPromptAngleOptions options: 
            Input prompt angle options
        AcquireAngle(string) -> PromptDoubleResult
            
            string message: 
            Input prompt message
        AcquireAngle(string, string) -> PromptDoubleResult
        
        """
        pass
    
    
    def AcquireDistance(self):
        """
        AcquireDistance() -> PromptDoubleResult
        
        AcquireDistance(JigPromptDistanceOptions) -> PromptDoubleResult
            
            JigPromptDistanceOptions options: 
            Input prompt distance options
        AcquireDistance(string) -> PromptDoubleResult
            
            string message: 
            Input prompt message
        AcquireDistance(string, string) -> PromptDoubleResult
        
        """
        pass
    
    
    def AcquirePoint(self):
        """
        AcquirePoint() -> PromptPointResult
        
        AcquirePoint(JigPromptPointOptions) -> PromptPointResult
            
            JigPromptPointOptions options: 
            Input prompt point options
        AcquirePoint(string) -> PromptPointResult
            
            string message: 
            Input prompt message
        AcquirePoint(string, string) -> PromptPointResult
        
        """
        pass
    
    
    def AcquireString(self):
        """
        AcquireString() -> PromptResult
        
        AcquireString(JigPromptStringOptions) -> PromptResult
            
            JigPromptStringOptions options: 
            Input prompt string options
        AcquireString(string) -> PromptResult
            
            string message: 
            Input prompt message
        AcquireString(string, string) -> PromptResult
        
        """
        pass
    
    pass

class Keyword(object):
    """
    
    """
    DisplayName = None
    
    
    Enabled = None
    
    
    GlobalName = None
    
    
    IsReadOnly = None
    
    
    LocalName = None
    
    
    Visible = None
    
    pass

class KeywordCollection(object):
    """
    
    KeywordCollection()
    """
    def Add(self):
        """
        Add(string) -> void
            
            string globalName: 
            Input the global name of the keyword; this is never displayed, but can be used by programs to access keywords when the local translation is not known.
        Add(string, string) -> void
            
            string globalName: 
            Input the global name of the keyword; this is never displayed, but can be used by programs to access keywords when the local translation is not known.
            
            string localName: 
            Input the local name of the keyword; the user enters the local name to specify the keyword.
        Add(string, string, string) -> void
            
            string globalName: 
            Input global name of the keyword; this is never displayed, but can be used by programs to access keywords when the local translation is not known.
            
            string localName: 
            Input local name of the keyword; the user enters the local name to specify the keyword.
            
            string displayName: 
            Input display name of the keyword; this is shown on the command line and is usually the same as local name.
        Add(string, string, string, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            string globalName: 
            Input global name of the keyword; this is never displayed, but can be used by programs to access keywords when the local translation is not known.
            
            string localName: 
            Input local name of the keyword; the user enters the local name to specify the keyword.
            
            string displayName: 
            Input display name of the keyword; this is shown on the command line and is usually the same as local name.
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            Input indicates whether the keyword should be shows to the user.
            
            [MarshalAs(UnmanagedType.U1)] bool enabled: 
            Input indicates whether the keyword is currently enabled; a disabled keyword is disabled is not accepted as user input.
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
            
            Keyword[] array: 
            Input the one-dimensional Array that is the destination of the elements copied from KeywordCollection. The array must have zero-based indexing.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetDisplayString(self):
        """
        GetDisplayString -> string
            
            [MarshalAs(UnmanagedType.U1)] bool showNoDefault: 
            Input true if the default values ought not be shown
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    
    Default = None
    
    
    IsReadOnly = None
    
    pass

class LivePreview(object):
    """
    
    LivePreview()()
    
    
    LivePreview(Document)()
    
    
    LivePreview(Document, [MarshalAs(UnmanagedType.U1)] bool)()
    
    
    """
    def AbortAll(self):
        """
        AbortAll -> void
        
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def EndPreview(self):
        """
        EndPreview() -> void
        
        EndPreview([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        EndPreview(int) -> void
        
        EndPreview(int, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def EndRecording(self):
        """
        EndRecording -> void
        
        """
        pass
    
    
    def IsPreviewRecording(self):
        """
        IsPreviewRecording() -> bool
        
        IsPreviewRecording(Document) -> bool
        
        """
        pass
    
    
    def IsPreviewStarted(self):
        """
        IsPreviewStarted() -> bool
        
        IsPreviewStarted(Document) -> bool
        
        """
        pass
    
    
    def QueueAction(self):
        """
        QueueAction(LivePreviewActionBase) -> void
        
        QueueAction(LivePreviewActionBase, int) -> void
        
        """
        pass
    
    
    def StartRecording(self):
        """
        StartRecording -> void
        
        """
        pass
    
    pass

class LivePreviewAction(object):
    """
    
    LivePreviewAction()
    """
    def Execute(self):
        """
        Execute -> void
        
        """
        pass
    
    pass

class LivePreviewActionBase(object):
    """
    
    LivePreviewActionBase()
    """
    def Execute(self):
        """
        Execute -> void
        
        """
        pass
    
    
    def OnAborted(self):
        """
        OnAborted -> void
        
        """
        pass
    
    pass

class LivePreviewCommand(object):
    """
    
    LivePreviewCommand()
    """
    def Execute(self):
        """
        Execute -> void
        
        """
        pass
    
    pass

class LivePreviewContextParameter(object):
    """
    
    """
    LivePreview = None
    
    
    Type = None
    
    
    Value = None
    
    pass

class LivePreviewContextProxy(object):
    """
    
    LivePreviewContextProxy()
    """
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def Finalize(self):
        """
        Finalize -> void
        
        """
        pass
    
    pass

class LivePreviewContextType():
    EndPreview = None
    UpdatePreview = None

class LivePreviewDelegate(object):
    """
    
    LivePreviewDelegate(LivePreviewCallback)()
    
    
    LivePreviewDelegate(LivePreviewCallback, LivePreviewCallback)()
    
    
    """
    def Execute(self):
        """
        Execute -> void
        
        """
        pass
    
    
    def OnAborted(self):
        """
        OnAborted -> void
        
        """
        pass
    
    pass

class LivePreviewEventArgs(object):
    """
    
    LivePreviewEventArgs()()
    
    
    LivePreviewEventArgs(Autodesk.AutoCAD.ApplicationServices.Document, params object[])()
    
    
    LivePreviewEventArgs(params object[])()
    
    
    """
    def LockDocument(self):
        """
        LockDocument -> IDisposable
        
        """
        pass
    
    
    CommandParameter = None
    
    
    Document = None
    
    
    Parameters = None
    
    pass

class LivePreviewPropertySetting(object):
    """
    
    LivePreviewPropertySetting()
    """
    def Execute(self):
        """
        Execute -> void
        
        """
        pass
    
    pass

class ObjectSnapMasks():
    AllowTangent = 0x20000
    ApparentIntersection = 0x800
    Center = 4
    DisablePerpendicular = 0x40000
    End = 1
    Immediate = 0x10000
    Insertion = 0x40
    Intersection = 0x20
    Middle = 2
    Near = 0x200
    Node = 8
    NoneOverride = 0x200000
    Perpendicular = 0x80
    Quadrant = 0x10
    Quick = 0x400
    RelativeCartesian = 0x80000
    RelativePolar = 0x100000
    Tangent = 0x100

class PickPointDescriptor(object):
    """
    
    PickPointDescriptor
        PickPointKind kind : Input the type of pick point
        Point3d pointOnLine : Input the point on the line to pick
        Vector3d direction : Input the direction of the pick
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(PickPointDescriptor) -> bool
            
            PickPointDescriptor a: 
            Input object to compare
        IsEqualTo(PickPointDescriptor, Tolerance) -> bool
            
            PickPointDescriptor a: 
            Input object to compare
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    Direction = None
    
    
    Kind = None
    
    
    PointOnLine = None
    
    pass

class PickPointKind():
    InfiniteLine = None
    Ray = None
    LineSegment = None

class PickPointSelectedObject(object):
    """
    
    PickPointSelectedObject(ObjectId, SelectionMethod, IntPtr, PickPointDescriptor)
        ObjectId id : Input object ID
        SelectionMethod method : Input method of selection
        IntPtr gsMarker : Input GS markers
        PickPointDescriptor descriptor : Input pick point descriptor
    
    
    PickPointSelectedObject(ObjectId, SelectionMethod, long, PickPointDescriptor)
        ObjectId id : Input object ID
        SelectionMethod method : Input method of selection
        long gsMarker : Input GS markers
        PickPointDescriptor descriptor : Input pick point descriptor
    
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    PickPoint = None
    
    pass

class PickPointSelectedSubObject(object):
    """
    
    PickPointSelectedSubObject(FullSubentityPath, SelectionMethod, IntPtr, PickPointDescriptor)
        FullSubentityPath path : Input subentity path
        SelectionMethod method : Input method of selection
        IntPtr gsMarker : Input GS markers
        PickPointDescriptor descriptor : Input pick point descriptor
    
    
    PickPointSelectedSubObject(FullSubentityPath, SelectionMethod, long, PickPointDescriptor)
        FullSubentityPath path : Input subentity path
        SelectionMethod method : Input method of selection
        long gsMarker : Input GS markers
        PickPointDescriptor descriptor : Input pick point descriptor
    
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    PickPoint = None
    
    pass

class PointFilterEventArgs(object):
    """
    
    """
    CallNext = None
    
    
    Context = None
    
    
    Result = None
    
    pass

class PointFilterResult(object):
    """
    
    """
    DisplayObjectSnapGlyph = None
    
    
    NewPoint = None
    
    
    Retry = None
    
    
    ToolTipText = None
    
    pass

class PointHistoryBits():
    Aligned = 0x400
    AppFiltered = 0x800
    CartSnapped = 0x10
    CoordinatePending = 0x70000
    CyclingPoint = 0x40
    DidNotPick = 0
    ForcedPick = 0x1000
    FromKeyboard = 0x80000
    Gripped = 8
    LastPoint = 4
    NotDigitizer = 2
    NotInteractive = 0x100000
    ObjectSnapped = 0x80
    Ortho = 0x20
    PickAborted = 0x8000
    PickMask = 0xe000
    PolarAngle = 0x100
    Tablet = 1
    UsedObjectSnapBox = 0x4000
    UsedPickBox = 0x2000
    XPending = 0x10000
    YPending = 0x20000
    ZPending = 0x40000

class PointMonitorEventArgs(object):
    """
    
    """
    def AppendToolTipText(self):
        """
        AppendToolTipText -> void
            
            string value: 
            Input item to be appended.
        """
        pass
    
    
    Context = None
    
    pass

class PromptAngleOptions(object):
    """
    
    PromptAngleOptions(string)
        string message : Input prompt message
    
    
    PromptAngleOptions(string, string)()
    
    
    """
    AllowArbitraryInput = None
    
    
    AllowNone = None
    
    
    AllowZero = None
    
    
    BasePoint = None
    
    
    DefaultValue = None
    
    
    UseAngleBase = None
    
    
    UseBasePoint = None
    
    
    UseDashedLine = None
    
    
    UseDefaultValue = None
    
    pass

class PromptAngleOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptCornerOptions(object):
    """
    
    PromptCornerOptions(string, Point3d)
        string message : Input prompt message
        Point3d basePoint : Input base point
    
    
    PromptCornerOptions(string, string, Point3d)()
    
    
    """
    AllowArbitraryInput = None
    
    
    AllowNone = None
    
    
    BasePoint = None
    
    
    LimitsChecked = None
    
    
    UseDashedLine = None
    
    pass

class PromptDistanceOptions(object):
    """
    
    PromptDistanceOptions(string)
        string message : Input prompt message
    
    
    PromptDistanceOptions(string, string)()
    
    
    """
    BasePoint = None
    
    
    DefaultValue = None
    
    
    Only2d = None
    
    
    UseBasePoint = None
    
    
    UseDashedLine = None
    
    pass

class PromptDistanceOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptDoubleOptions(object):
    """
    
    PromptDoubleOptions(string)
        string message : Input prompt message
    
    
    PromptDoubleOptions(string, string)
        string messageAndKeywords : Input prompt message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    DefaultValue = None
    
    pass

class PromptDoubleOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptDoubleResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    Value = None
    
    pass

class PromptDoubleResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class PromptDragOptions(object):
    """
    
    PromptDragOptions(SelectionSet, string, DragCallback)
        SelectionSet selection : Input selection set
        string message : Input prompt message
        DragCallback callback : Input drag callback
    
    
    PromptDragOptions(SelectionSet, string, string, DragCallback)
        SelectionSet selection : Input selection set
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
        DragCallback callback : Input drag callback
    
    
    """
    AllowArbitraryInput = None
    
    
    AllowNone = None
    
    
    Callback = None
    
    
    Cursor = None
    
    
    Selection = None
    
    pass

class PromptEditorOptions(object):
    """
    
    """

    pass

class PromptEntityOptions(object):
    """
    
    PromptEntityOptions(string)
        string message : Input prompt message
    
    
    PromptEntityOptions(string, string)
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    def AddAllowedClass(self):
        """
        AddAllowedClass -> void
            
            Type type: 
            Input type of class
            
            [MarshalAs(UnmanagedType.U1)] bool exactMatch: 
            Input boolean for exact type
        """
        pass
    
    
    def RemoveAllowedClass(self):
        """
        RemoveAllowedClass -> void
            
            Type type: 
            Input type of class
        """
        pass
    
    
    def SetRejectMessage(self):
        """
        SetRejectMessage -> void
            
            string message: 
            Input prompt message
        """
        pass
    
    
    AllowNone = None
    
    
    AllowObjectOnLockedLayer = None
    
    pass

class PromptEntityOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptEntityResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    ObjectId = None
    
    
    PickedPoint = None
    
    pass

class PromptEntityResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class PromptFileNameResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    ReadOnly = None
    
    pass

class PromptFileOptions(object):
    """
    
    """
    AllowUrls = None
    
    
    DialogCaption = None
    
    
    DialogName = None
    
    
    Filter = None
    
    
    FilterIndex = None
    
    
    InitialDirectory = None
    
    
    InitialFileName = None
    
    
    Message = None
    
    
    PreferCommandLine = None
    
    pass

class PromptForEntityEndingEventArgs(object):
    """
    
    """
    def RemoveSelectedObject(self):
        """
        RemoveSelectedObject -> void
        
        """
        pass
    
    
    def ReplaceSelectedObject(self):
        """
        ReplaceSelectedObject -> void
            
            SelectedObject newValue: 
            Input new value
        """
        pass
    
    
    Result = None
    
    pass

class PromptForSelectionEndingEventArgs(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            SelectedObject value: 
            Input object to be added.
        """
        pass
    
    
    def AddSubEntity(self):
        """
        AddSubEntity -> void
            
            SelectedSubObject value: 
            Input object to be added.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Input index of item to removes
        """
        pass
    
    
    def RemoveSubEntity(self):
        """
        RemoveSubEntity -> void
            
            int entityIndex: 
            Input entity index of item to remove
            
            int subEntityIndex: 
            Input subEntity index of item to removes
        """
        pass
    
    
    Flags = None
    
    
    Selection = None
    
    pass

class PromptIntegerOptions(object):
    """
    
    PromptIntegerOptions(string)
        string message : Input prompt message
    
    
    PromptIntegerOptions(string, string)
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
    
    
    PromptIntegerOptions(string, string, int, int)
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
        int lowerLimit : Input lower limit
        int upperLimit : Input upper limit
    
    
    """
    DefaultValue = None
    
    
    LowerLimit = None
    
    
    UpperLimit = None
    
    pass

class PromptIntegerOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptIntegerResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    Value = None
    
    pass

class PromptIntegerResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class PromptKeywordOptions(object):
    """
    
    PromptKeywordOptions(string)
        string message : Input prompt message
    
    
    PromptKeywordOptions(string, string)
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    AllowArbitraryInput = None
    
    
    AllowNone = None
    
    pass

class PromptKeywordOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptNestedEntityOptions(object):
    """
    
    PromptNestedEntityOptions(string)
        string message : Input prompt message
    
    
    PromptNestedEntityOptions(string, string)
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    AllowNone = None
    
    
    NonInteractivePickPoint = None
    
    
    UseNonInteractivePickPoint = None
    
    pass

class PromptNestedEntityOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptNestedEntityResult(object):
    """
    
    """
    def GetContainers(self):
        """
        GetContainers -> ObjectId()
        
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
    
    
    Transform = None
    
    pass

class PromptNestedEntityResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class PromptNumericalOptions(object):
    """
    
    """
    AllowArbitraryInput = None
    
    
    AllowNegative = None
    
    
    AllowNone = None
    
    
    AllowZero = None
    
    
    UseDefaultValue = None
    
    pass

class PromptOpenFileOptions(object):
    """
    
    PromptOpenFileOptions
        string message : Input prompt message
    """
    SearchPath = None
    
    
    TransferRemoteFiles = None
    
    pass

class PromptOptions(object):
    """
    
    """
    def SetMessageAndKeywords(self):
        """
        SetMessageAndKeywords -> void
            
            string messageAndKeywords: 
            Input message and keywords
            
            string globalKeywords: 
            Input global keywords
        """
        pass
    
    
    AppendKeywordsToMessage = None
    
    
    IsReadOnly = None
    
    
    Keywords = None
    
    
    Message = None
    
    pass

class PromptPointOptions(object):
    """
    
    PromptPointOptions(string)
        string message : Input prompt message
    
    
    PromptPointOptions(string, string)
        string messageAndKeywords : Input message and keywords
        string globalKeywords : Input global keywords
    
    
    """
    UseBasePoint = None
    
    pass

class PromptPointOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptPointResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    Value = None
    
    pass

class PromptPointResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class PromptResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    Status = None
    
    
    StringResult = None
    
    pass

class PromptSaveFileOptions(object):
    """
    
    PromptSaveFileOptions
        string message : Input prompt message
    """
    DeriveInitialFilenameFromDrawingName = None
    
    
    DisplaySaveOptionsMenuItem = None
    
    
    ForceOverwriteWarningForScriptsAndLisp = None
    
    pass

class PromptSelectionOptions(object):
    """
    
    PromptSelectionOptions()
    """
    def AddKeywordsToMinimalList(self):
        """
        AddKeywordsToMinimalList -> void
            
            AddedKeywords kwds: 
            bitwise combination of AddedKeywords enum values
        """
        pass
    
    
    def RemoveKeywordsFromFullList(self):
        """
        RemoveKeywordsFromFullList -> void
            
            SubtractedKeywords kwds: 
            bitwise combination of SubtractedKeywords enum values
        """
        pass
    
    
    def SetKeywords(self):
        """
        SetKeywords -> void
            
            string keywords: 
            Input keywords
            
            string globalKeywords: 
            Input global keywords
        """
        pass
    
    
    AllowDuplicates = None
    
    
    AllowSubSelections = None
    
    
    ForceSubSelections = None
    
    
    Keywords = None
    
    
    MessageForAdding = None
    
    
    MessageForRemoval = None
    
    
    PrepareOptionalDetails = None
    
    
    RejectObjectsFromNonCurrentSpace = None
    
    
    RejectObjectsOnLockedLayers = None
    
    
    RejectPaperspaceViewport = None
    
    
    SelectEverythingInAperture = None
    
    
    SingleOnly = None
    
    
    SinglePickInSpace = None
    
    pass

class PromptSelectionOptionsEventArgs(object):
    """
    
    """
    def GetPoints(self):
        """
        GetPoints -> Point3d()
        
        """
        pass
    
    
    Filter = None
    
    
    Options = None
    
    pass

class PromptSelectionResult(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    Status = None
    
    
    Value = None
    
    pass

class PromptSelectionResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class PromptStatus():
    Cancel = -5002
    Error = -5001
    Keyword = -5005
    Modeless = 0x13a3
    None = 0x1388
    OK = 0x13ec
    Other = 0x13a4

class PromptStringOptions(object):
    """
    
    PromptStringOptions
        string message : Input.
    """
    AllowSpaces = None
    
    
    DefaultValue = None
    
    
    UseDefaultValue = None
    
    pass

class PromptStringOptionsEventArgs(object):
    """
    
    """
    Options = None
    
    pass

class PromptStringResultEventArgs(object):
    """
    
    """
    Result = None
    
    pass

class RolloverEventArgs(object):
    """
    
    """
    Highlighted = None
    
    
    Picked = None
    
    pass

class SamplerStatus():
    OK = None
    NoChange = None
    Cancel = None

class SelectedObject(object):
    """
    
    SelectedObject(Autodesk.AutoCAD.DatabaseServices.ObjectId, SelectedSubObject[])
        Autodesk.AutoCAD.DatabaseServices.ObjectId id : Input selected object's ID
        SelectedSubObject[] subSelections : Input any subselections
    
    
    SelectedObject(Autodesk.AutoCAD.DatabaseServices.ObjectId, Autodesk.AutoCAD.EditorInput.SelectionMethod, IntPtr)
        Autodesk.AutoCAD.EditorInput.SelectionMethod method : Input selection method
        IntPtr gsMarker : Input GS marker
        path : Input object path
    
    
    SelectedObject(Autodesk.AutoCAD.DatabaseServices.ObjectId, Autodesk.AutoCAD.EditorInput.SelectionMethod, long)
        Autodesk.AutoCAD.DatabaseServices.ObjectId id : Input object path
        Autodesk.AutoCAD.EditorInput.SelectionMethod method : Input selection method
        long gsMarker : Input GS marker
    
    
    """
    def GetSubentities(self):
        """
        GetSubentities -> SelectedSubObject()
        
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
    
    
    GraphicsSystemMarker = None
    
    
    GraphicsSystemMarkerPtr = None
    
    
    ObjectId = None
    
    
    OptionalDetails = None
    
    
    SelectionMethod = None
    
    pass

class SelectedSubObject(object):
    """
    
    SelectedSubObject(Autodesk.AutoCAD.DatabaseServices.FullSubentityPath, Autodesk.AutoCAD.EditorInput.SelectionMethod, IntPtr)
        Autodesk.AutoCAD.DatabaseServices.FullSubentityPath path : Input object path
        Autodesk.AutoCAD.EditorInput.SelectionMethod method : Input selection method
        IntPtr gsMarker : Input GS marker
    
    
    SelectedSubObject(Autodesk.AutoCAD.DatabaseServices.FullSubentityPath, Autodesk.AutoCAD.EditorInput.SelectionMethod, long)
        Autodesk.AutoCAD.DatabaseServices.FullSubentityPath path : Input object path
        Autodesk.AutoCAD.EditorInput.SelectionMethod method : Input selection method
        long gsMarker : Input GS marker
    
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    FullSubentityPath = None
    
    
    GraphicsSystemMarker = None
    
    
    GraphicsSystemMarkerPtr = None
    
    
    OptionalDetails = None
    
    
    SelectionMethod = None
    
    pass

class SelectionAddedEventArgs(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            SelectedObject value: 
            Input value to add
        """
        pass
    
    
    def AddSubEntity(self):
        """
        AddSubEntity -> void
            
            SelectedSubObject value: 
            Input subentity to add
        """
        pass
    
    
    def Highlight(self):
        """
        Highlight -> void
            
            int subSelectionIndex: 
            Input subselection index
            
            FullSubentityPath path: 
            Input path to highlight
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Input index of object to remove
        """
        pass
    
    
    def RemoveSubEntity(self):
        """
        RemoveSubEntity -> void
            
            int entityIndex: 
            Input entity index
            
            int subEntityIndex: 
            Input subentity index
        """
        pass
    
    
    AddedObjects = None
    
    
    Flags = None
    
    
    Selection = None
    
    pass

class SelectionDetails(object):
    """
    
    """
    def GetContainers(self):
        """
        GetContainers -> ObjectId()
        
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
    
    
    Transform = None
    
    pass

class SelectionFilter(object):
    """
    
    SelectionFilter
        TypedValue[] value : Input Autodesk.AutoCAD.DatabaseServices.TypedValue[] object.
    """
    def GetFilter(self):
        """
        GetFilter -> TypedValue()
        
        """
        pass
    
    pass

class SelectionFlags():
    Duplicates = 2
    FailedPickAuto = 0x200
    NestedEntities = 4
    Normal = 0
    PickfirstSet = 0x20
    PickPoints = 1
    PreviousSet = 0x40
    SinglePick = 0x10
    SubEntities = 8
    SubSelection = 0x80
    Undo = 0x100

class SelectionMethod():
    Crossing = 3
    Fence = 4
    NonGraphical = 0
    PickPoint = 1
    SubEntity = 5
    Unavailable = -1
    Window = 2

class SelectionMode():
    All = 6
    Box = 3
    Crossing = 2
    CrossingPolygon = 8
    Entity = 5
    Every = 11
    Extents = 12
    FencePolyline = 7
    Group = 13
    Last = 4
    Multiple = 15
    Pick = 10
    Previous = 14
    Window = 1
    WindowPolygon = 9

class SelectionRemovedEventArgs(object):
    """
    
    """
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Input index of object to remove
        """
        pass
    
    
    def RemoveSubentity(self):
        """
        RemoveSubentity -> void
            
            int index: 
            Input index of object to remove
            
            int subentityIndex: 
            Input subentity index
        """
        pass
    
    
    Flags = None
    
    
    RemovedObjects = None
    
    
    Selection = None
    
    pass

class SelectionSet(object):
    """
    
    SelectionSet()
    """
    def CopyTo(self):
        """
        CopyTo -> void
            
            SelectedObject[] array: 
            Input the one-dimensional array that is the destination of the elements copied from SelectionSet. The array must have zero-based indexing
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FromObjectIds(self):
        """
        FromObjectIds -> SelectionSet
            
            ObjectId[] ids: 
            Input array of IDs to copy
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def GetObjectIds(self):
        """
        GetObjectIds -> ObjectId()
        
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
    
    
    Count = None
    
    
    IsSynchronized = None
    
    
    SyncRoot = None
    
    pass

class SelectionTextInputEventArgs(object):
    """
    
    """
    def AddObjects(self):
        """
        AddObjects -> void
            
            ObjectId[] ids: 
            Input an array of object IDs to be added to the selection set.
        """
        pass
    
    
    def SetErrorMessage(self):
        """
        SetErrorMessage -> void
            
            string errorMessage: 
            Input the error message text.
        """
        pass
    
    
    Input = None
    
    pass

class SubtractedKeywords():
    AddRemove = 0x800
    All = 4
    BoxAuto = 8
    CrossingCPolygon = 0x20
    Fence = 0x40
    Group = 0x400
    Last = 0x80
    LastAllGroupPrevious = 1
    Multiple = 0x10
    PickImplied = 2
    Previous = 0x100
    WindowWPolygon = 0x200

class UserInputControls():
    Accept3dCoordinates = 0x80
    AcceptMouseUpAsPoint = 0x100
    AcceptOtherInputString = 0x800
    AnyBlankTerminatesInput = 0x200
    DoNotEchoCancelForCtrlC = 4
    DoNotUpdateLastPoint = 8
    GovernedByOrthoMode = 1
    GovernedByUCSDetect = 0x1000
    InitialBlankTerminatesInput = 0x400
    NoDwgLimitsChecking = 0x10
    NoNegativeResponseAccepted = 0x40
    NoZDirectionOrtho = 0x2000
    NoZeroResponseAccepted = 0x20
    NullResponseAccepted = 2
    UseBasePointElevation = 0x8000