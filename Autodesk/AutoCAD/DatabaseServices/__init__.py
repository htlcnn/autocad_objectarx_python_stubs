class AbstractViewTable(object):
    """
    
    """

    pass

class AbstractViewTableRecord(object):
    """
    
    """
    def SetSun(self):
        """
        SetSun -> ObjectId
            
            [CallerMustClose] DBObject sun: 
            Input the sun object.
        """
        pass
    
    
    def SetUcs(self):
        """
        SetUcs(Autodesk.AutoCAD.DatabaseServices.OrthographicView) -> void
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input the object for the UCS view
        SetUcs(ObjectId) -> void
            
            ObjectId id: 
            Input the object which references a UcsTableRecord.
        SetUcs(Point3d, Vector3d, Vector3d) -> void
            
            Point3d origin: 
            Input the object to act as an origin
            
            Vector3d y: 
            Input the object to act as a Y-coordinate
        """
        pass
    
    
    def SetUcsToWorld(self):
        """
        SetUcsToWorld -> void
        
        """
        pass
    
    
    def SetViewDirection(self):
        """
        SetViewDirection -> void
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input the orthographic view
        """
        pass
    
    
    AmbientLightColor = None
    
    
    BackClipDistance = None
    
    
    BackClipEnabled = None
    
    
    Background = None
    
    
    Brightness = None
    
    
    CenterPoint = None
    
    
    Contrast = None
    
    
    DefaultLightingOn = None
    
    
    DefaultLightingType = None
    
    
    Elevation = None
    
    
    FrontClipAtEye = None
    
    
    FrontClipDistance = None
    
    
    FrontClipEnabled = None
    
    
    Height = None
    
    
    LensLength = None
    
    
    PerspectiveEnabled = None
    
    
    SunId = None
    
    
    Target = None
    
    
    ToneOperatorParameters = None
    
    
    Ucs = None
    
    
    UcsName = None
    
    
    UcsOrthographic = None
    
    
    ViewDirection = None
    
    
    ViewOrthographic = None
    
    
    ViewTwist = None
    
    
    VisualStyleId = None
    
    
    Width = None
    
    pass

class ActionsToEvaluateCallback(object):
    """
    
    ActionsToEvaluateCallback()
    """
    def NeedsToEvaluate(self):
        """
        NeedsToEvaluate -> void
            
            ObjectId objectId: 
            ObjectId of an AssocAction, AssocDependency or an arbitrary DBObject that needs to be evaluated.
            
            AssocStatus newStatus: 
            The new evaluation request status of the action or dependency. If it is not an evaluation request, the needsToEvaluate() implementation should not change the status of the action or dependency.
            
            [MarshalAs(UnmanagedType.U1)] bool ownedActionsAlso: 
            If the action that needs to evaluate is an AssocNetwork, this argument controls whether all the actions owned by the network also need to be evaluated. The caller usually passes true.
        """
        pass
    
    pass

class AlignedDimension(object):
    """
    
    AlignedDimension()()
    
    
    """
    DimLinePoint = None
    
    
    Oblique = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

class AngleConstraint():
    Degrees015 = 1
    Degrees030 = 2
    Degrees045 = 3
    Degrees060 = 4
    Degrees090 = 6
    DegreesAny = 0
    DegreesHorz = 12

class AngularConstraint(object):
    """
    
    AngularConstraint()()
    
    
    AngularConstraint(AngularSectorType)
        AngularSectorType type : Input SectorType indicating the angle sector which is used to measure the angle.
    
    
    """
    class AngularSectorType():
        ParallelAntiClockwise = None
        AntiParallelClockwise = None
        ParallelClockwise = None
        AntiParallelAntiClockwise = None
    
    
    def AngleMultiplier(self):
        """
        AngleMultiplier -> double
        
        """
        pass
    
    
    def SetAngleMultiplier(self):
        """
        SetAngleMultiplier -> void
            
            double multiplier: 
            The angle multiplication factor.
        """
        pass
    
    
    SectorType = None
    
    pass

class AnnotationScale(object):
    """
    
    AnnotationScale()
    """
    CollectionName = None
    
    
    DrawingUnits = None
    
    
    IsTemporaryScale = None
    
    
    Name = None
    
    
    PaperUnits = None
    
    
    Scale = None
    
    
    UniqueIdentifier = None
    
    pass

class AnnotationType():
    MText = None
    FeatureControlFrame = None
    BlockRef = None
    NoAnnotation = None

class AnnotativeStates():
    NotApplicable = None

class ApplicationLoadReasons():
    LoadDisabled = 0x10
    OnAutoCADStartup = 2
    OnCommandInvocation = 4
    OnLoadRequest = 8
    OnProxyDetection = 1
    TransparentlyLoadable = 0x20

class Arc(object):
    """
    
    Arc()()
    
    
    Arc(Point3d, Vector3d, double, double, double)
        Point3d center : Input the center point of the arc.
        Vector3d normal : Input the normal vector of the plane containing the arc.
        double radius : Input the radius of the arc.
        double startAngle : Input the starting angle of the arc.
        double endAngle : Input the ending angle of the arc.
    
    
    Arc(Point3d, double, double, double)
        Point3d center : Input the center point of the arc.
        double radius : Input the radius of the arc.
        double startAngle : Input the starting angle of the arc.
        double endAngle : Input the ending angle of the arc.
    
    
    """
    Center = None
    
    
    EndAngle = None
    
    
    Length = None
    
    
    Normal = None
    
    
    Radius = None
    
    
    StartAngle = None
    
    
    Thickness = None
    
    
    TotalAngle = None
    
    pass

class ArcDimension(object):
    """
    
    ArcDimension
        Point3d centerPoint : Input the center of the arc being dimensioned
        Point3d xLine1Point : Input the first extension line end point
        Point3d xLine2Point : Input the second extension line end point
        Point3d arcPoint : Input the point on arc being dimensioned
        string dimensionText : Input the dimension text to use instead of calculated value
        ObjectId dimensionStyle : Input the dimension style object ID.
    """
    ArcEndParam = None
    
    
    ArcPoint = None
    
    
    ArcStartParam = None
    
    
    ArcSymbolType = None
    
    
    CenterPoint = None
    
    
    HasLeader = None
    
    
    IsPartial = None
    
    
    Leader1Point = None
    
    
    Leader2Point = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

class Assoc2dConstraintCallback(object):
    """
    
    Assoc2dConstraintCallback()
    """
    def CanBeRelaxed(self):
        """
        CanBeRelaxed -> bool
            
            ExplicitConstraint constraint: 
            The dimension constraint that is to be erased.
        """
        pass
    
    
    def ConstraintDeactivated(self):
        """
        ConstraintDeactivated -> void
            
            ExplicitConstraint constraint: 
            The constraint that is to be activated or deactivated.
            
            [MarshalAs(UnmanagedType.U1)] bool deactivated: 
            Whether to deactivate or reactivate the constraint
        """
        pass
    
    pass

class Assoc2dConstraintGroup(object):
    """
    
    Assoc2dConstraintGroup
        Plane plane : Input Plane of the newly created constraint group object. Default value is Plane::kXYPlane.
    """
    class SolutionStatusType():
        WellDefined = None
        UnderConstrained = None
        OverConstrained = None
        Inconsistent = None
        NotEvaluated = None
        NotAvailable = None
        RejectedByClient = None
    
    
    def Add3PointAngularConstraint(self):
        """
        Add3PointAngularConstraint -> ThreePointAngleConstraint
            
            ConstrainedPoint consPoint1: 
            Input reference of the first (angle) point which must be a kind of ConstraintPoint
            
            ConstrainedPoint consPoint2: 
            Input reference of the second point which must be a kind of ConstraintPoint
            
            ConstrainedPoint consPoint3: 
            Input reference of the third point which must be a kind of ConstraintPoint
            
            AngularConstraint.AngularSectorType sectorType: 
            Input AngularConstraint::SectorType indicating the angle sector to measure.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
            
            ObjectId dimDependencyId: 
            Input object id of the dimension dependency object.
        """
        pass
    
    
    def AddAngularConstraint(self):
        """
        AddAngularConstraint -> AngularConstraint
            
            ConstrainedLine consLine1: 
            Input reference to ConstrainedLine object
            
            ConstrainedLine consLine2: 
            Input reference to ConstrainedLine object
            
            AngularConstraint.AngularSectorType sectorType: 
            Input AngularConstraint.SectorType indicating the angle sector to measure.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
            
            ObjectId dimDependencyId: 
            Input object id of the dimension dependency object.
        """
        pass
    
    
    def AddConstrainedGeometry(self):
        """
        AddConstrainedGeometry -> ConstrainedGeometry
            
            FullSubentityPath subentPath: 
            Input FullSubentPath of the constrained entity, down to the subentity level. Only SubentityType.Edge and SubentityType.Vertex are valid subent types. The vertex subent must NOT be edge vertex.
        """
        pass
    
    
    def AddDistanceConstraint(self):
        """
        AddDistanceConstraint -> DistanceConstraint
            
            ConstrainedGeometry consGeom1: 
            Input reference to the first ConstrainedGeometry object.
            
            ConstrainedGeometry consGeom2: 
            Input reference to the second ConstrainedGeometry object.
            
            DistanceConstraint.DistanceDirectionType directionType: 
            Input DistanceConstraint::DirectionType indicating the direction type of the distance constraint to be created.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
            
            Vector3d fixedDirection: 
            Input reference to Vector3d indicating the fixed direction of the distance constraint to be created. It will be used only when the directionType is kFixedDirection. Relative to the World Coordinate System.
            
            ConstrainedLine directionLine: 
            Input reference to ConstrainedLine object indicating the relative direction of the distance constraint to be created. It will be used only when the directionType is kPerpendicularToLine or kParallelToLine.
        """
        pass
    
    
    def AddGeometricalConstraint(self):
        """
        AddGeometricalConstraint(GeometricalConstraint.ConstraintType, ConstrainedGeometry[]) -> GeometricalConstraint
            
            GeometricalConstraint.ConstraintType type: 
            Input GeometricalConstraint::GeometricalConstraintType indicating the type of constraint to be created.
            
            ConstrainedGeometry[] consGeoms: 
            Input array of the ConstrainedGeometry.
        AddGeometricalConstraint(GeometricalConstraint.ConstraintType, FullSubentityPath[]) -> GeometricalConstraint
            
            GeometricalConstraint.ConstraintType type: 
            Input GeometricalConstraint::GeometricalConstraintType indicating the type of constraint to be created.
            
            FullSubentityPath[] paths: 
            Input array of the FullSubentPath which can be mapped to ConstrainedGeometry.
        """
        pass
    
    
    def AddGlobalCallback(self):
        """
        AddGlobalCallback -> void
            
            Assoc2dConstraintCallback callback: 
            The callback to be registered.
        """
        pass
    
    
    def AddRadiusDiameterConstraint(self):
        """
        AddRadiusDiameterConstraint -> RadiusDiameterConstraint
            
            ConstrainedGeometry consGeom: 
            Input reference to ConstrainedGeometry object which must be a kind of ConstrainedCircle or ConstrainedEllipse.
            
            RadiusDiameterConstraint.RadDiaConstrType type: 
            Input RadiusDiameterConstraint::RadiusDiameterConstrType indicating the type of constraint to be created.
            
            ObjectId valueDependencyId: 
            Input object id of the value dependency object.
        """
        pass
    
    
    def AutoConstrain(self):
        """
        AutoConstrain -> void
            
            FullSubentityPath[] paths: 
            List of subentites which are to be constrained automatically.
            
            Tolerance tol: 
            Tol to define distance tolerance as well as angle tolerance. Tolerance.EqualPoint() defines distance tolerance and Tolerance.EqualVector() defines angle tolerance. Angle tolerance is in radians of angle.
            
            AutoConstrainEvaluationCallback callback: 
            Reference to autoconstraint evaluation callback. This callback will implement constraint priority and priority override.
        """
        pass
    
    
    def ConstraintStatus(self):
        """
        ConstraintStatus -> SolutionStatusType
            
            GeometricalConstraint constraint: 
            Input reference to GeometricalConstraint indicating the constraint object to be checked.
        """
        pass
    
    
    def DeleteConstrainedGeometry(self):
        """
        DeleteConstrainedGeometry -> void
            
            ObjectId geomDependencyId: 
            Input ObjectId of the AssocGeomDependency object.
        """
        pass
    
    
    def DeleteConstraint(self):
        """
        DeleteConstraint -> void
            
            GeometricalConstraint geomConst: 
            Input GeometricalConstraint indicating the constraint to be deleted.
        """
        pass
    
    
    def GeometryMirrored(self):
        """
        GeometryMirrored -> void
            
            AssocGeomDependency geomDependency: 
            Reference to AssocGeomDependency for which implicit point needs to be updated for mirror action.
        """
        pass
    
    
    def GeometryStatus(self):
        """
        GeometryStatus -> SolutionStatusType
            
            ConstrainedGeometry consGeom: 
            Input reference to ConstrainedGeometry indicating the constrained geometry object to be checked.
        """
        pass
    
    
    def GetAllConnectedGeomDependencies(self):
        """
        GetAllConnectedGeomDependencies -> ObjectIdCollection
            
            ObjectIdCollection srcGeomDependencyIds: 
            Input ObjectIdArray indicating the source AssocGeomDependency objects.
        """
        pass
    
    
    def GetConstrainedGeometry(self):
        """
        GetConstrainedGeometry(AssocGeomDependency) -> ConstrainedGeometry
            
            AssocGeomDependency geomDependency: 
            Input reference to AssocGeomDependency of the constrained entity. The AssocGeomDependency object maybe transient, in other words, not added into the database yet.
        GetConstrainedGeometry(AssocGeomDependency, Autodesk.AutoCAD.DatabaseServices.ImplicitPointType, int, [MarshalAs(UnmanagedType.U1)] bool) -> ConstrainedGeometry
            
            AssocGeomDependency geomDependency: 
            Input reference to AssocGeomDependency of the constrained entity. The AssocGeomDependency object maybe transient, in other words, not added into the database yet.
            
            Autodesk.AutoCAD.DatabaseServices.ImplicitPointType ptType: 
            Input reference to ConstrainedImplicitPoint::ImplicitPointType indicating the implicit point type of a constrained curve. Only present when caller want to retrieve the ConstrainedImplicitPoint of a ConstrainedCurve. Default value is NULL.
            
            int defPtIndex: 
            Input integer index of define points of a parametric curve. Currently only control points of a spline are supported. It is only valid when the implicit point type is kDefineImplicit. Default value is -1(invalid index value).
            
            createArcLineMid: 
            Input Boolean indicating if create implicit midpoint of arc or line segment if it is not there. Default value is false.
        GetConstrainedGeometry(FullSubentityPath, [MarshalAs(UnmanagedType.U1)] bool) -> ConstrainedGeometry
            
            [MarshalAs(UnmanagedType.U1)] bool createArcLineMid: 
            Input Boolean indicating if create implicit midpoint of arc or line segment if it is not there. Default value is false.
            
            fullSubentPath: 
            Input FullSubentPath of the constrained entity, down to the subentity level. Only vertex or edge subentity type can be passed in.
        """
        pass
    
    
    def GetGroupNode(self):
        """
        GetGroupNode -> ConstraintGroupNode
            
            uint nodeId: 
            Input ConstraintGroupNodeId indicating the node id.
        """
        pass
    
    
    def GlobalCallback(self):
        """
        GlobalCallback -> Assoc2dConstraintCallback
        
        """
        pass
    
    
    def RegenDimensionSystem(self):
        """
        RegenDimensionSystem -> void
        
        """
        pass
    
    
    def RemoveGlobalCallback(self):
        """
        RemoveGlobalCallback -> void
            
            Assoc2dConstraintCallback callback: 
            The callback to be unregistered.
        """
        pass
    
    
    def SolutionStatus(self):
        """
        SolutionStatus -> SolutionStatusType
            
            [MarshalAs(UnmanagedType.U1)] bool alsoCheckForConstraints: 
            Input boolean indicating if need to check constraints. Default value is true.
        """
        pass
    
    
    def TransformActionBy(self):
        """
        TransformActionBy -> void
            
            Matrix3d transform: 
            The given transformation matrix.
        """
        pass
    
    
    ConstrainedGeometries = None
    
    
    Constraints = None
    
    
    GetDOF = None
    
    
    WorkPlane = None
    
    pass

class AssocAction(object):
    """
    
    AssocAction()
    """
    def AddDependency(self):
        """
        AddDependency -> void
            
            ObjectId dependencyId: 
            ObjectId of the AssocDependency being added to this action.
            
            [MarshalAs(UnmanagedType.U1)] bool setThisActionAsOwningAction: 
            If true, sets this action to be the database owner of the dependency. In this case the dependency must not be already owned by any other action.
        """
        pass
    
    
    def AddMoreObjectsToDeepClone(self):
        """
        AddMoreObjectsToDeepClone -> void
            
            IdMapping idMap: 
            The IdMapping of the current deep cloning session.
            
            ObjectIdCollection additionalObjectsToClone: 
            Additional objects that the action also wants to deep clone. It is legal to add objects that have already been cloned; they will be ignored and not cloned again.
        """
        pass
    
    
    def AreDependenciesEqual(self):
        """
        AreDependenciesEqual -> bool
            
            AssocDependency dependency1: 
            The dependency owned by this action. It needs to be open at least for read.
            
            AssocDependency dependency2: 
            Another dependency. It needs to be open at least for read.
        """
        pass
    
    
    def AreDependenciesOnTheSameThing(self):
        """
        AreDependenciesOnTheSameThing -> bool
            
            AssocDependency dependency1: 
            The dependency owned by this action. It needs to be open at least for read.
            
            AssocDependency dependency2: 
            Another dependency. It needs to be open at least for read.
        """
        pass
    
    
    def DependentObjectCloned(self):
        """
        DependentObjectCloned -> void
            
            AssocDependency dependency: 
            The AssocDependency on the DBObject that has been cloned.
            
            DBObject dbObj: 
            The original object.
            
            DBObject newObj: 
            The newly created clone.
        """
        pass
    
    
    def DragStatus(self):
        """
        DragStatus -> void
            
            Autodesk.AutoCAD.DatabaseServices.DragStatus status: 
            See the DragStatus enum.
        """
        pass
    
    
    def Evaluate(self):
        """
        Evaluate -> void
            
            AssocEvaluationCallback evaluationCallback: 
            While the action is being evaluated, it calls methods of the callback object to inform the client code about the evaluation. The callback reference must not be NULL. See the definition of AssocEvaluationCallback for more details.
        """
        pass
    
    
    def EvaluateDependencies(self):
        """
        EvaluateDependencies -> void
        
        """
        pass
    
    
    def EvaluateDependency(self):
        """
        EvaluateDependency -> void
            
            AssocDependency dependency: 
            The dependency that is to be evaluated. It needs to be open at least for read.
        """
        pass
    
    
    def EvaluationPriority(self):
        """
        EvaluationPriority -> AssocEvaluationPriority
        
        """
        pass
    
    
    def GetActionBody(self):
        """
        GetActionBody -> ObjectId
        
        """
        pass
    
    
    def GetActionsDependentOnObject(self):
        """
        GetActionsDependentOnObject(DBObject, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectIdCollection
            
            DBObject dbObj: 
            The DBObject whose actions are requested. The object needs to be open at least for read.
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Actions that depend-on the object wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Actions that modify the object wanted.
        GetActionsDependentOnObject(DBObject, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, ObjectIdCollection) -> void
        
        """
        pass
    
    
    def GetDependencies(self):
        """
        GetDependencies -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Read-type dependencies wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Write-type dependencies wanted.
        """
        pass
    
    
    def GetDependentActionsToEvaluate(self):
        """
        GetDependentActionsToEvaluate -> void
            
            ActionsToEvaluateCallback actionsToEvaluateCallback: 
            The method uses this callback to report other AssocActions, AssocDependencies and arbitrary DBObjects that should also be scheduled to evaluate when this action is evaluated.
        """
        pass
    
    
    def GetDependentObjects(self):
        """
        GetDependentObjects -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Dependent-on objects wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Modified objects wanted.
        """
        pass
    
    
    def HasDependencyCachedValue(self):
        """
        HasDependencyCachedValue -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether it has cached value. It needs to be open at least for read.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            AssocAction otherAction: 
            The other action needs to be open for read.
        """
        pass
    
    
    def IsExternalDependency(self):
        """
        IsExternalDependency -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether it is external. Needs to be open at least for read.
        """
        pass
    
    
    def IsOwnedDependency(self):
        """
        IsOwnedDependency -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether it is owned by this action. Needs to be open at least for read.
        """
        pass
    
    
    def IsRelevantDependencyChange(self):
        """
        IsRelevantDependencyChange -> bool
            
            AssocDependency dependency: 
            The dependency that is checked whether the change in the object it depends on is relevant or not. It needs to be open at least for read.
        """
        pass
    
    
    def ObjectThatOwnsNetworkInstance(self):
        """
        ObjectThatOwnsNetworkInstance -> ObjectId
        
        """
        pass
    
    
    def OwnedDependencyStatusChanged(self):
        """
        OwnedDependencyStatusChanged -> void
            
            AssocDependency ownedDependency: 
            The dependency whose status has just been changed.
            
            AssocStatus previousStatus: 
            Previous status of the dependency.
        """
        pass
    
    
    def PostProcessAfterDeepClone(self):
        """
        PostProcessAfterDeepClone -> void
            
            IdMapping idMap: 
            The IdMapping of the current deep cloning session.
        """
        pass
    
    
    def PostProcessAfterDeepCloneCancel(self):
        """
        PostProcessAfterDeepCloneCancel -> void
            
            IdMapping idMap: 
            The IdMapping of the current deep cloning session.
        """
        pass
    
    
    def RemoveActionsControllingObject(self):
        """
        RemoveActionsControllingObject(ObjectId) -> void
        
        RemoveActionsControllingObject(ObjectId, int) -> void
        
        RemoveActionsControllingObject(ObjectId, int, ObjectId) -> void
        
        """
        pass
    
    
    def RemoveAllDependencies(self):
        """
        RemoveAllDependencies -> void
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseThem: 
            Erase the AssocDependencies after removing them.
        """
        pass
    
    
    def RemoveDependency(self):
        """
        RemoveDependency -> void
            
            ObjectId dependencyId: 
            ObjectId of the AssocDependency being removed from this action.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erases the dependency after removing it.
        """
        pass
    
    
    def SetOwningNetwork(self):
        """
        SetOwningNetwork -> void
            
            ObjectId networkId: 
            The AssocNetwork logically owning this action.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoSetAsDatabaseOwner: 
            Make the network the database owner of this action.
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
            
            AssocStatus newStatus: 
            The new AssocStatus of the action.
            
            [MarshalAs(UnmanagedType.U1)] bool notifyOwningNetwork: 
            If true, and the passed-in status indicates that the action needs to be evaluated, the status of the AssocNetwork owning this dependency is set to the same status (unless the network evaluation status is already more severe than the new one).
            
            [MarshalAs(UnmanagedType.U1)] bool setInOwnedActions: 
            If true, and this action owns some other actions (such as AssocNetwork owns actions), the status is also set in all owned actions (both directly owned and recursively owned).
        """
        pass
    
    
    def TransformActionBy(self):
        """
        TransformActionBy -> void
            
            Matrix3d transform: 
            The provided transformation matrix.
        """
        pass
    
    
    ActionBody = None
    
    
    CurrentEvaluationCallback = None
    
    
    IsActionBodyAProxy = None
    
    
    IsActionEvaluationInProgress = None
    
    
    OwningNetwork = None
    
    
    Status = None
    
    pass

class AssocActionBody(object):
    """
    
    """
    class ValueParam(object):
        """
        
        ValueParam()
        """
        EvaluatorId = None
        
        
        Expression = None
        
        
        Value = None
        
        pass
    
    
    def AddDependency(self):
        """
        AddDependency -> void
        
        """
        pass
    
    
    def AddMoreObjectsToDeepCloneOverride(self):
        """
        AddMoreObjectsToDeepCloneOverride -> void
        
        """
        pass
    
    
    def AddParam(self):
        """
        AddParam -> void
        
        """
        pass
    
    
    def AreDependenciesEqualOverride(self):
        """
        AreDependenciesEqualOverride -> bool
        
        """
        pass
    
    
    def AreDependenciesOnTheSameThingOverride(self):
        """
        AreDependenciesOnTheSameThingOverride -> bool
        
        """
        pass
    
    
    def CreateActionAndActionBodyAndPostToDatabase(self):
        """
        CreateActionAndActionBodyAndPostToDatabase -> void
        
        """
        pass
    
    
    def currentEvaluationCallback(self):
        """
        currentEvaluationCallback -> AssocEvaluationCallback
        
        """
        pass
    
    
    def DependentObjectClonedOverride(self):
        """
        DependentObjectClonedOverride -> void
        
        """
        pass
    
    
    def DragStatusOverride(self):
        """
        DragStatusOverride -> void
        
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def EvaluateDependencies(self):
        """
        EvaluateDependencies -> void
        
        """
        pass
    
    
    def EvaluateDependencyOverride(self):
        """
        EvaluateDependencyOverride -> bool
        
        """
        pass
    
    
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def EvaluationPriorityOverride(self):
        """
        EvaluationPriorityOverride -> void
        
        """
        pass
    
    
    def GetActionBodiesOnObject(self):
        """
        GetActionBodiesOnObject -> void
        
        """
        pass
    
    
    def GetDependencies(self):
        """
        GetDependencies -> ObjectIdCollection
        
        """
        pass
    
    
    def GetDependenciesOverride(self):
        """
        GetDependenciesOverride -> ObjectIdCollection
        
        """
        pass
    
    
    def GetDependentActionsToEvaluateOverride(self):
        """
        GetDependentActionsToEvaluateOverride -> void
        
        """
        pass
    
    
    def GetDependentObjectsOverride(self):
        """
        GetDependentObjectsOverride -> ObjectIdCollection
        
        """
        pass
    
    
    def GetParentAction(self):
        """
        GetParentAction -> ObjectId
        
        """
        pass
    
    
    def GetValueParam(self):
        """
        GetValueParam(string) -> ValueParam
        
        GetValueParam(string, int) -> ValueParam
        
        """
        pass
    
    
    def GetValueParamArray(self):
        """
        GetValueParamArray -> ValueParam()
        
        """
        pass
    
    
    def GetValueParamUnitType(self):
        """
        GetValueParamUnitType -> Autodesk.AutoCAD.DatabaseServices.UnitType
        
        """
        pass
    
    
    def HasAnyErasedOrBrokenDependencies(self):
        """
        HasAnyErasedOrBrokenDependencies -> bool
        
        """
        pass
    
    
    def HasDependencyCachedValueOverride(self):
        """
        HasDependencyCachedValueOverride -> bool
        
        """
        pass
    
    
    def IsActionEvaluationInProgress(self):
        """
        IsActionEvaluationInProgress -> bool
        
        """
        pass
    
    
    def IsEqualToOverride(self):
        """
        IsEqualToOverride -> bool
        
        """
        pass
    
    
    def IsExternalDependencyOverride(self):
        """
        IsExternalDependencyOverride -> bool
        
        """
        pass
    
    
    def IsOwnedDependencyOverride(self):
        """
        IsOwnedDependencyOverride -> bool
        
        """
        pass
    
    
    def IsRelevantDependencyChangeOverride(self):
        """
        IsRelevantDependencyChangeOverride -> bool
        
        """
        pass
    
    
    def OwnedDependencyStatusChangedOverride(self):
        """
        OwnedDependencyStatusChangedOverride -> void
        
        """
        pass
    
    
    def OwnedValueParamNames(self):
        """
        OwnedValueParamNames -> string()
        
        """
        pass
    
    
    def ParamAtIndex(self):
        """
        ParamAtIndex -> ObjectId
        
        """
        pass
    
    
    def ParamAtName(self):
        """
        ParamAtName(string) -> ObjectId
        
        ParamAtName(string, int) -> ObjectId
        
        """
        pass
    
    
    def ParamsAtName(self):
        """
        ParamsAtName -> ObjectIdCollection
        
        """
        pass
    
    
    def PostProcessAfterDeepCloneCancelOverride(self):
        """
        PostProcessAfterDeepCloneCancelOverride -> void
        
        """
        pass
    
    
    def PostProcessAfterDeepCloneOverride(self):
        """
        PostProcessAfterDeepCloneOverride -> void
        
        """
        pass
    
    
    def RemoveAllDependencies(self):
        """
        RemoveAllDependencies -> void
        
        """
        pass
    
    
    def RemoveAllDependenciesOverride(self):
        """
        RemoveAllDependenciesOverride -> void
        
        """
        pass
    
    
    def RemoveAllParams(self):
        """
        RemoveAllParams -> void
        
        """
        pass
    
    
    def RemoveDependency(self):
        """
        RemoveDependency -> void
        
        """
        pass
    
    
    def RemoveParam(self):
        """
        RemoveParam -> void
        
        """
        pass
    
    
    def RemoveValueParam(self):
        """
        RemoveValueParam -> void
        
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
        
        """
        pass
    
    
    def SetValueParam(self):
        """
        SetValueParam(string, ValueParam, [MarshalAs(UnmanagedType.U1)] bool) -> string
        
        SetValueParam(string, ValueParam, [MarshalAs(UnmanagedType.U1)] bool, int) -> string
        
        """
        pass
    
    
    def SetValueParamArray(self):
        """
        SetValueParamArray -> string()
        
        """
        pass
    
    
    def SetValueParamUnitType(self):
        """
        SetValueParamUnitType -> void
        
        """
        pass
    
    
    def TransformActionByOverride(self):
        """
        TransformActionByOverride -> void
        
        """
        pass
    
    
    def ValueParamInputVariables(self):
        """
        ValueParamInputVariables -> ObjectIdCollection
        
        """
        pass
    
    
    OwnedParams = None
    
    
    OwningNetwork = None
    
    
    ParamCount = None
    
    
    ParentAction = None
    
    
    Status = None
    
    pass

class AssocActionParam(object):
    """
    
    AssocActionParam()
    """
    def DetachDependencies(self):
        """
        DetachDependencies -> void
        
        """
        pass
    
    
    def GetDependencies(self):
        """
        GetDependencies -> ObjectIdCollection
        
        """
        pass
    
    
    def MakeParamConstant(self):
        """
        MakeParamConstant -> void
        
        """
        pass
    
    
    def MakeParamEmpty(self):
        """
        MakeParamEmpty -> void
        
        """
        pass
    
    
    def TransformConstantGeometry(self):
        """
        TransformConstantGeometry -> void
        
        """
        pass
    
    
    Name = None
    
    
    ParentAction = None
    
    pass

class AssocArray(object):
    """
    
    """
    def AddSourceEntity(self):
        """
        AddSourceEntity -> void
        
        """
        pass
    
    
    def CreateArray(self):
        """
        CreateArray -> AssocArray
        
        """
        pass
    
    
    def DeleteItem(self):
        """
        DeleteItem -> void
        
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> ObjectIdCollection
        
        """
        pass
    
    
    def GetAssociativeArray(self):
        """
        GetAssociativeArray -> AssocArray
        
        """
        pass
    
    
    def getItemLocators(self):
        """
        getItemLocators -> ItemLocator()
        
        """
        pass
    
    
    def GetItemTransform(self):
        """
        GetItemTransform -> Matrix3d
        
        """
        pass
    
    
    def GetParameters(self):
        """
        GetParameters -> AssocArrayParameters
        
        """
        pass
    
    
    def IsAssociativeArray(self):
        """
        IsAssociativeArray -> bool
        
        """
        pass
    
    
    def RemoveSourceEntity(self):
        """
        RemoveSourceEntity -> void
        
        """
        pass
    
    
    def ReplaceItems(self):
        """
        ReplaceItems -> void
        
        """
        pass
    
    
    def ResetItems(self):
        """
        ResetItems -> void
        
        """
        pass
    
    
    def TransformItemBy(self):
        """
        TransformItemBy -> void
        
        """
        pass
    
    
    EntityId = None
    
    
    SourceEntities = None
    
    pass

class AssocArrayCommonParameters(object):
    """
    
    """
    def GetLevelCount(self):
        """
        GetLevelCount -> Integer
        
        """
        pass
    
    
    def GetLevelSpacing(self):
        """
        GetLevelSpacing -> double
        
        """
        pass
    
    
    def GetRowCount(self):
        """
        GetRowCount -> Integer
        
        """
        pass
    
    
    def GetRowElevation(self):
        """
        GetRowElevation -> double
        
        """
        pass
    
    
    def GetRowSpacing(self):
        """
        GetRowSpacing -> double
        
        """
        pass
    
    
    def SetLevelCount(self):
        """
        SetLevelCount -> void
        
        """
        pass
    
    
    def SetLevelSpacing(self):
        """
        SetLevelSpacing -> void
        
        """
        pass
    
    
    def SetRowCount(self):
        """
        SetRowCount -> void
        
        """
        pass
    
    
    def SetRowElevation(self):
        """
        SetRowElevation -> void
        
        """
        pass
    
    
    def SetRowSpacing(self):
        """
        SetRowSpacing -> void
        
        """
        pass
    
    
    BaseNormal = None
    
    
    BasePlane = None
    
    
    BasePoint = None
    
    
    LevelCount = None
    
    
    LevelSpacing = None
    
    
    RowCount = None
    
    
    RowElevation = None
    
    
    RowSpacing = None
    
    pass

class AssocArrayParameters(object):
    """
    
    """
    def Commit(self):
        """
        Commit -> void
        
        """
        pass
    
    
    Owner = None
    
    pass

class AssocArrayPathParameters(object):
    """
    
    AssocArrayPathParameters()()
    
    
    AssocArrayPathParameters(double, double, double, int, int, int, double)()
    
    
    """
    class MethodType():
        Divide = None
        Measure = None
    
    
    def GetEndOffset(self):
        """
        GetEndOffset -> double
        
        """
        pass
    
    
    def GetItemCount(self):
        """
        GetItemCount -> Integer
        
        """
        pass
    
    
    def GetItemSpacing(self):
        """
        GetItemSpacing -> double
        
        """
        pass
    
    
    def GetStartOffset(self):
        """
        GetStartOffset -> double
        
        """
        pass
    
    
    def SetEndOffset(self):
        """
        SetEndOffset -> void
        
        """
        pass
    
    
    def SetItemCount(self):
        """
        SetItemCount -> void
        
        """
        pass
    
    
    def SetItemSpacing(self):
        """
        SetItemSpacing -> void
        
        """
        pass
    
    
    def SetStartOffset(self):
        """
        SetStartOffset -> void
        
        """
        pass
    
    
    AlignItems = None
    
    
    EndOffset = None
    
    
    ItemCount = None
    
    
    ItemSpacing = None
    
    
    Method = None
    
    
    Path = None
    
    
    PathDirection = None
    
    
    StartOffset = None
    
    pass

class AssocArrayPolarParameters(object):
    """
    
    AssocArrayPolarParameters()()
    
    
    AssocArrayPolarParameters(double, double, double, int, int, int, double)()
    
    
    """
    class ArcDirection():
        Clockwise = None
        CounterClockwise = None
    
    
    def GetAngleBetweenItems(self):
        """
        GetAngleBetweenItems -> double
        
        """
        pass
    
    
    def GetFillAngle(self):
        """
        GetFillAngle -> double
        
        """
        pass
    
    
    def GetItemCount(self):
        """
        GetItemCount -> Integer
        
        """
        pass
    
    
    def GetRadius(self):
        """
        GetRadius -> double
        
        """
        pass
    
    
    def GetStartAngle(self):
        """
        GetStartAngle -> double
        
        """
        pass
    
    
    def SetAngleBetweenItems(self):
        """
        SetAngleBetweenItems -> void
        
        """
        pass
    
    
    def SetFillAngle(self):
        """
        SetFillAngle -> void
        
        """
        pass
    
    
    def SetItemCount(self):
        """
        SetItemCount -> void
        
        """
        pass
    
    
    def SetRadius(self):
        """
        SetRadius -> void
        
        """
        pass
    
    
    def SetStartAngle(self):
        """
        SetStartAngle -> void
        
        """
        pass
    
    
    AngleBetweenItems = None
    
    
    Direction = None
    
    
    FillAngle = None
    
    
    ItemCount = None
    
    
    Radius = None
    
    
    RotateItems = None
    
    
    StartAngle = None
    
    pass

class AssocArrayRectangularParameters(object):
    """
    
    AssocArrayRectangularParameters()()
    
    
    AssocArrayRectangularParameters(double, double, double, int, int, int, double, double)()
    
    
    """
    def GetAxesAngle(self):
        """
        GetAxesAngle -> double
        
        """
        pass
    
    
    def GetColumnCount(self):
        """
        GetColumnCount -> Integer
        
        """
        pass
    
    
    def GetColumnSpacing(self):
        """
        GetColumnSpacing -> double
        
        """
        pass
    
    
    def SetAxesAngle(self):
        """
        SetAxesAngle -> void
        
        """
        pass
    
    
    def SetColumnCount(self):
        """
        SetColumnCount -> void
        
        """
        pass
    
    
    def SetColumnSpacing(self):
        """
        SetColumnSpacing -> void
        
        """
        pass
    
    
    AxesAngle = None
    
    
    ColumnCount = None
    
    
    ColumnSpacing = None
    
    
    XAxisDirection = None
    
    
    YAxisDirection = None
    
    pass

class AssocAsmBodyActionParam(object):
    """
    
    AssocAsmBodyActionParam()
    """
    def SetBody(self):
        """
        SetBody(Entity, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        SetBody(ObjectId, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AssocBlendSurfaceActionBody(object):
    """
    
    AssocBlendSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetContinuityGripPoints(self):
        """
        GetContinuityGripPoints -> void
        
        """
        pass
    
    
    def GetEndEdgeBulge(self):
        """
        GetEndEdgeBulge -> double
        
        """
        pass
    
    
    def GetEndEdgeContinuity(self):
        """
        GetEndEdgeContinuity -> short
        
        """
        pass
    
    
    def GetProfiles(self):
        """
        GetProfiles -> void
        
        """
        pass
    
    
    def GetStartEdgeBulge(self):
        """
        GetStartEdgeBulge -> double
        
        """
        pass
    
    
    def GetStartEdgeContinuity(self):
        """
        GetStartEdgeContinuity -> short
        
        """
        pass
    
    
    def SetEndEdgeBulge(self):
        """
        SetEndEdgeBulge -> void
        
        """
        pass
    
    
    def SetEndEdgeContinuity(self):
        """
        SetEndEdgeContinuity -> void
        
        """
        pass
    
    
    def SetStartEdgeBulge(self):
        """
        SetStartEdgeBulge -> void
        
        """
        pass
    
    
    def SetStartEdgeContinuity(self):
        """
        SetStartEdgeContinuity -> void
        
        """
        pass
    
    
    BlendOption = None
    
    
    EndEdgeBulge = None
    
    
    EndEdgeContinuity = None
    
    
    StartEdgeBulge = None
    
    
    StartEdgeContinuity = None
    
    pass

class AssocCompoundActionParam(object):
    """
    
    AssocCompoundActionParam()
    """
    def AddParam(self):
        """
        AddParam -> Integer
        
        """
        pass
    
    
    def ParamAtIndex(self):
        """
        ParamAtIndex -> ObjectId
        
        """
        pass
    
    
    def ParamAtName(self):
        """
        ParamAtName(string) -> ObjectId
        
        ParamAtName(string, int) -> ObjectId
        
        """
        pass
    
    
    def ParamsAtName(self):
        """
        ParamsAtName -> ObjectIdCollection
        
        """
        pass
    
    
    def RemoveAllParams(self):
        """
        RemoveAllParams -> void
        
        """
        pass
    
    
    def RemoveParam(self):
        """
        RemoveParam -> void
        
        """
        pass
    
    
    OwnedParams = None
    
    
    ParamCount = None
    
    pass

class AssocConstraintType():
    NoneAssocConstraintType = None
    DistanceAssocConstraintType = None
    HorizontalDistanceAssocConstraintType = None
    VerticalDistanceAssocConstraintType = None
    Angle0AssocConstraintType = None
    Angle1AssocConstraintType = None
    Angle2AssocConstraintType = None
    Angle3AssocConstraintType = None
    RadiusAssocConstraintType = None
    DiameterAssocConstraintType = None

class AssocDependency(object):
    """
    
    AssocDependency()
    """
    def AttachToObject(self):
        """
        AttachToObject -> void
            
            CompoundObjectId compoundId: 
            The CompoundObjectId to attach the dependency to. If regular ObjectId is passed in, it is automatically converted to CompoundObjectId.
        """
        pass
    
    
    def DetachFromObject(self):
        """
        DetachFromObject -> void
        
        """
        pass
    
    
    def Evaluate(self):
        """
        Evaluate -> void
        
        """
        pass
    
    
    def GetDependenciesOnObject(self):
        """
        GetDependenciesOnObject -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool readDependenciesWanted: 
            Read-type dependencies wanted.
            
            [MarshalAs(UnmanagedType.U1)] bool writeDependenciesWanted: 
            Write-type dependencies wanted.
            
            object: 
            The DBObject whose dependencies are requested. The object needs to be open at least for read.
        """
        pass
    
    
    def GetFirstDependencyOnObject(self):
        """
        GetFirstDependencyOnObject -> ObjectId
            
            object: 
            The DBObject whose first dependency is requested. The object needs to be open at least for read.
        """
        pass
    
    
    def IsDependentOnTheSameThingAs(self):
        """
        IsDependentOnTheSameThingAs -> bool
            
            AssocDependency otherDependency: 
            The other dependency needs to be open for read.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            AssocDependency otherDependency: 
            The other dependency needs to be open for read.
        """
        pass
    
    
    def NotifyDependenciesOnObject(self):
        """
        NotifyDependenciesOnObject -> void
            
            AssocStatus newStatus: 
            The new status to be set to the dependencies.
            
            object: 
            The DBObject whose dependencies are to be notified. The object needs to be open at least for read.
        """
        pass
    
    
    def SetDependentOnObject(self):
        """
        SetDependentOnObject -> void
            
            CompoundObjectId compoundId: 
            The CompoundObjectId the dependency should depend-on (may be null).
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
            
            AssocStatus newStatus: 
            The new AssocStatus of the dependency.
            
            notifyOwningAction: 
            If true, and the passed-in status indicates that the dependency needs to be evaluated, the status of the AssocAction owning this dependency is set to the same status (unless the action evaluation status is already more severe than the new one). The action then notifies its owning network.
        """
        pass
    
    
    def UpdateDependentOnObject(self):
        """
        UpdateDependentOnObject -> void
        
        """
        pass
    
    
    CurrentEvaluationCallback = None
    
    
    DependencyBody = None
    
    
    DependentOnCompoundObject = None
    
    
    DependentOnObject = None
    
    
    DependentOnObjectStatus = None
    
    
    HasCachedValue = None
    
    
    IsActionEvaluationInProgress = None
    
    
    IsAttachedToObject = None
    
    
    IsDelegatingToOwningAction = None
    
    
    IsDependentOnCompoundObject = None
    
    
    IsDependentOnObjectReadOnly = None
    
    
    IsObjectStateDependent = None
    
    
    IsReadDependency = None
    
    
    IsRelevantChange = None
    
    
    IsWriteDependency = None
    
    
    NextDependencyOnObject = None
    
    
    Order = None
    
    
    OwningAction = None
    
    
    PrevDependencyOnObject = None
    
    
    Status = None
    
    pass

class AssocDependencyBody(object):
    """
    
    """
    def ClonedOverride(self):
        """
        ClonedOverride -> void
        
        """
        pass
    
    
    def currentEvaluationCallback(self):
        """
        currentEvaluationCallback -> AssocEvaluationCallback
        
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def ErasedOverride(self):
        """
        ErasedOverride -> void
        
        """
        pass
    
    
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def IsDependentOnTheSameThingAsOverride(self):
        """
        IsDependentOnTheSameThingAsOverride -> bool
        
        """
        pass
    
    
    def IsEqualToOverride(self):
        """
        IsEqualToOverride -> bool
        
        """
        pass
    
    
    def ModifiedOverride(self):
        """
        ModifiedOverride -> void
        
        """
        pass
    
    
    def SetStatus(self):
        """
        SetStatus -> void
        
        """
        pass
    
    
    def UpdateDependentOnObjectOverride(self):
        """
        UpdateDependentOnObjectOverride -> void
        
        """
        pass
    
    
    DependentOnObject = None
    
    
    HasCachedValueOverride = None
    
    
    IsActionEvaluationInProgress = None
    
    
    IsAttachedToObject = None
    
    
    IsRelevantChangeOverride = None
    
    
    OwningAction = None
    
    
    ParentDependency = None
    
    
    Status = None
    
    pass

class AssocDependencyPE(object):
    """
    
    AssocDependencyPE()
    """
    def AllowsDependencies(self):
        """
        AllowsDependencies -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool isWriteDependency: 
            The dependency will also modify the object.
            
            object: 
            The queried object, must be open for read.
        """
        pass
    
    pass

class AssocDimDependencyBody(object):
    """
    
    AssocDimDependencyBody()
    """
    def CreateAndPostToDatabase(self):
        """
        CreateAndPostToDatabase -> void
            
            ObjectId dimId: 
            ObjectId of the Dimension.
            
            ref ObjectId dimDepId: 
            ObjectId of the created AssocDependency.
            
            ref ObjectId dimDepBodyId: 
            ObjectId of the created AssocDimDependencyBody.
        """
        pass
    
    
    def UpdateDependentOnObjectOverride(self):
        """
        UpdateDependentOnObjectOverride -> void
        
        """
        pass
    
    
    EntityMeasurementOverride = None
    
    
    EntityTextOverride = None
    
    
    IsEntityAttachmentChangedOverride = None
    
    pass

class AssocDimDependencyBodyBase(object):
    """
    
    """
    class NotificationIgnorerDotNet(object):
        """
        
        """
        def IsIgnoringNotifications(self):
            """
            IsIgnoringNotifications -> bool
            
            """
            pass
        
        pass
    
    
    def ComposeEntityText(self):
        """
        ComposeEntityText -> string
            
            int requiredNameFormat: 
            The constraint name format display, deafault value if -1. If requiredNameFormat == -1, CONSTRAINTNAMEFORMAT sysvar is used for choosing the text format.
        """
        pass
    
    
    def Constraint(self):
        """
        Constraint -> ExplicitConstraint
        
        """
        pass
    
    
    def DeactivateConstraint(self):
        """
        DeactivateConstraint -> void
        
        """
        pass
    
    
    def DragStatus(self):
        """
        DragStatus -> void
            
            Autodesk.AutoCAD.DatabaseServices.DragStatus status: 
            The current DragStatus.
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def EntityAttachmentPointMoved(self):
        """
        EntityAttachmentPointMoved -> void
            
            SubentityGeometry[] newAttachedGeometries: 
            The new attached geometries to be updated.
            
            double measurement: 
            New measurement, default value is 0.0.
        """
        pass
    
    
    def ErasedOverride(self):
        """
        ErasedOverride -> void
            
            [MarshalAs(UnmanagedType.U1)] bool isErasing: 
            Boolean isErasing.
            
            pDbObj: 
            The controlled entity.
        """
        pass
    
    
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def FormatToCurrentPrecision(self):
        """
        FormatToCurrentPrecision -> string
            
            string expression: 
            The expression to be formatted.
            
            [MarshalAs(UnmanagedType.U1)] bool isAngular: 
            Indicates it is an angular constraint.
        """
        pass
    
    
    def GetEntityNameAndExpression(self):
        """
        GetEntityNameAndExpression -> void
            
            ref string name: 
            Name from the managed entity display text.
            
            ref string expression: 
            Expression from the managed entity display text.
        """
        pass
    
    
    def GetEraseDimensionIfDependencyIsErased(self):
        """
        GetEraseDimensionIfDependencyIsErased -> bool
        
        """
        pass
    
    
    def GetFromEntity(self):
        """
        GetFromEntity -> ObjectId
            
            ObjectId entityId: 
            The entity id of the dependent-on Entity, such as of an Dimension.
        """
        pass
    
    
    def GetNameAndExpressionFromEntityText(self):
        """
        GetNameAndExpressionFromEntityText -> void
            
            string entityText: 
            The string to extract name and expression from.
            
            [MarshalAs(UnmanagedType.U1)] bool useMeasurementIfNoText: 
            Indicates whether to use measurement value if no text is given.
            
            double measurement: 
            The provided entity measurement.
            
            [MarshalAs(UnmanagedType.U1)] bool isAngular: 
            Indicates that the constraint is angular.
            
            ref string name: 
            Name component extracted from entityText.
            
            ref string expression: 
            Expression component extracted from entityText.
        """
        pass
    
    
    def GetSubentityGeoms(self):
        """
        GetSubentityGeoms -> SubentityGeometry()
            
            Vector3d distanceDirection: 
            Direction of the distance constraint.
        """
        pass
    
    
    def GetVariableNameAndExpression(self):
        """
        GetVariableNameAndExpression -> void
            
            ref string name: 
            Variable name.
            
            ref string expression: 
            Variable expression.
            
            string value: 
            Variable value.
        """
        pass
    
    
    def ModifiedOverride(self):
        """
        ModifiedOverride -> void
            
            DBObject dbObj: 
            The controlled entity.
        """
        pass
    
    
    def ReactivateConstraint(self):
        """
        ReactivateConstraint -> void
        
        """
        pass
    
    
    def SetEntityNameAndExpression(self):
        """
        SetEntityNameAndExpression -> void
            
            string name: 
            New name the managed entity should display.
            
            string expression: 
            New expression the managed entity should display.
            
            string value: 
            New value the managed entity should display.
        """
        pass
    
    
    def SetEraseDimensionIfDependencyIsErased(self):
        """
        SetEraseDimensionIfDependencyIsErased -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool yesNo: 
            Indicates to suppress the erase behavior or not.
        """
        pass
    
    
    def SetNameAndExpression(self):
        """
        SetNameAndExpression -> void
            
            string name: 
            New name to be set.
            
            string expression: 
            New expression to be set.
        """
        pass
    
    
    def SetVariableNameAndExpression(self):
        """
        SetVariableNameAndExpression -> void
            
            string name: 
            New name of the AssocVariable.
            
            string expression: 
            New expression of the AssocVariable.
        """
        pass
    
    
    def SetVariableValueToMeasuredValue(self):
        """
        SetVariableValueToMeasuredValue -> void
        
        """
        pass
    
    
    def SubErase(self):
        """
        SubErase -> void
            
            [MarshalAs(UnmanagedType.U1)] bool erasing: 
            Boolean erasing.
        """
        pass
    
    
    def UpdateDependentOnObjectOverride(self):
        """
        UpdateDependentOnObjectOverride -> void
        
        """
        pass
    
    
    def ValidateEntityText(self):
        """
        ValidateEntityText -> string
            
            string entityTextToValidate: 
            The entity text to check.
        """
        pass
    
    
    ConstrainedGeoms = None
    
    
    EntityMeasurementOverride = None
    
    
    EntityTextOverride = None
    
    
    GetCurrentlyUsedEntityNameFormat = None
    
    
    GetMeasuredValue = None
    
    
    IsConstraintActive = None
    
    
    IsEntityAttachmentChangedOverride = None
    
    
    IsReferenceOnly = None
    
    
    IsRelevantChangeOverride = None
    
    
    SubentityConstrainedGeoms = None
    
    
    Variable = None
    
    pass

class AssocDraggingState():
    NotDraggingAssocDraggingState = None
    FirstSampleAssocDraggingState = None
    IntermediateSampleAssocDraggingState = None
    LastSampleAssocDraggingState = None

class AssocEdgeActionParam(object):
    """
    
    AssocEdgeActionParam()
    """
    def GetEdgeRef(self):
        """
        GetEdgeRef -> EdgeRef()
        
        """
        pass
    
    
    def SetEdgeRef(self):
        """
        SetEdgeRef(EdgeRef) -> void
        
        SetEdgeRef(EdgeRef, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AssocEdgeChamferActionBody(object):
    """
    
    AssocEdgeChamferActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetBaseDistance(self):
        """
        GetBaseDistance -> double
        
        """
        pass
    
    
    def GetOtherDistance(self):
        """
        GetOtherDistance -> double
        
        """
        pass
    
    
    def SetBaseDistance(self):
        """
        SetBaseDistance -> void
        
        """
        pass
    
    
    def SetOtherDistance(self):
        """
        SetOtherDistance -> void
        
        """
        pass
    
    
    BaseDistance = None
    
    
    OtherDistance = None
    
    pass

class AssocEdgeFilletActionBody(object):
    """
    
    AssocEdgeFilletActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetRadius(self):
        """
        GetRadius -> double
        
        """
        pass
    
    
    def SetRadius(self):
        """
        SetRadius -> void
        
        """
        pass
    
    
    Radius = None
    
    pass

class AssocEvaluationCallback(object):
    """
    
    AssocEvaluationCallback()
    """
    def BeginActionEvaluation(self):
        """
        BeginActionEvaluation -> void
            
            AssocAction action: 
            The action that is being evaluated.
        """
        pass
    
    
    def BeginActionEvaluationUsingObject(self):
        """
        BeginActionEvaluationUsingObject -> void
            
            ObjectId objectId: 
            The DBObject that is going to be used or modified by the action.
            
            [MarshalAs(UnmanagedType.U1)] bool objectIsGoingToBeUsed: 
            The object contents is going to be used.
            
            [MarshalAs(UnmanagedType.U1)] bool objectIsGoingToBeModified: 
            The object contents is going to be modified.
            
            DBObject substituteObject: 
            An DBObject optionally provided by the custom evaluation callback code. The custom evaluation callback code should not assign NULL to this output argument if it does not want to provide a substitute object. It should only assign a non-NULL pointer if it intends to provide a substitute object.
            
            action: 
            The action that is being evaluated.
        """
        pass
    
    
    def CancelActionEvaluation(self):
        """
        CancelActionEvaluation -> bool
        
        """
        pass
    
    
    def DraggingState(self):
        """
        DraggingState -> AssocDraggingState
        
        """
        pass
    
    
    def EndActionEvaluation(self):
        """
        EndActionEvaluation -> void
            
            AssocAction action: 
            The action that is being evaluated.
        """
        pass
    
    
    def EndActionEvaluationUsingObject(self):
        """
        EndActionEvaluationUsingObject -> void
            
            AssocAction action: 
            The action that is being evaluated.
            
            ObjectId objectId: 
            The same DBObjectId that has been previously passed to the matching BeginActionEvaluationUsingObject() callback.
            
            object: 
            The object that has been used or modified by the action. It may be NULL if the original object couldn't be opened or if the substitute object was not of the expected type.
        """
        pass
    
    
    def EvaluationMode(self):
        """
        EvaluationMode -> AssocEvaluationMode
        
        """
        pass
    
    
    def GetTransformationType(self):
        """
        GetTransformationType -> AssocTransformationType
        
        """
        pass
    
    
    def SetActionEvaluationErrorStatus(self):
        """
        SetActionEvaluationErrorStatus(AssocAction, Autodesk.AutoCAD.Runtime.ErrorStatus) -> void
            
            AssocAction action: 
            The action that is being evaluated.
            
            Autodesk.AutoCAD.Runtime.ErrorStatus errorStatus: 
            Action evaluation error status.
        SetActionEvaluationErrorStatus(AssocAction, Autodesk.AutoCAD.Runtime.ErrorStatus, ObjectId, DBObject, IntPtr) -> void
            
            AssocAction action: 
            The action that is being evaluated.
            
            Autodesk.AutoCAD.Runtime.ErrorStatus errorStatus: 
            Action evaluation error status.
            
            ObjectId objectId: 
            The failed object id (such as of an AssocDependency).
            
            IntPtr errorInfo: 
            Additional info about the error.
            
            object: 
            The failed object pointer (such as of an AssocDependency).
        """
        pass
    
    pass

class AssocEvaluationMode():
    ModifyObjectsAssocEvaluationMode = None
    ModifyActionAssocEvaluationMode = None

class AssocEvaluationPriority():
    CanBeEvaluatedAssocEvaluationPriority = 0x3e8
    CannotBeEvaluatedAssocEvaluationPriority = -1000
    CannotDermineAssocEvaluationPriority = 0

class AssocExtendSurfaceActionBody(object):
    """
    
    AssocExtendSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetDistance(self):
        """
        GetDistance -> double
        
        """
        pass
    
    
    def SetDistance(self):
        """
        SetDistance -> void
        
        """
        pass
    
    
    Distance = None
    
    pass

class AssocExtrudedSurfaceActionBody(object):
    """
    
    AssocExtrudedSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetHeight(self):
        """
        GetHeight -> double
        
        """
        pass
    
    
    def GetTaperAngle(self):
        """
        GetTaperAngle -> double
        
        """
        pass
    
    
    def SetHeight(self):
        """
        SetHeight -> void
        
        """
        pass
    
    
    def SetTaperAngle(self):
        """
        SetTaperAngle -> void
        
        """
        pass
    
    
    Height = None
    
    
    TaperAngle = None
    
    pass

class AssocFaceActionParam(object):
    """
    
    AssocFaceActionParam()
    """
    def GetFaceRef(self):
        """
        GetFaceRef -> FaceRef()
        
        """
        pass
    
    
    def SetFaceRef(self):
        """
        SetFaceRef(FaceRef) -> void
        
        SetFaceRef(FaceRef, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AssocFilletSurfaceActionBody(object):
    """
    
    AssocFilletSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetFilletHandleData(self):
        """
        GetFilletHandleData -> void
        
        """
        pass
    
    
    def GetHintPoints(self):
        """
        GetHintPoints -> Point3d()
        
        """
        pass
    
    
    def GetRadius(self):
        """
        GetRadius -> double
        
        """
        pass
    
    
    def SetHintPoints(self):
        """
        SetHintPoints -> void
        
        """
        pass
    
    
    def SetRadius(self):
        """
        SetRadius -> void
        
        """
        pass
    
    
    Radius = None
    
    
    TrimMode = None
    
    pass

class AssocGeomDependency(object):
    """
    
    AssocGeomDependency()
    """
    def DependentOnObjectMirrored(self):
        """
        DependentOnObjectMirrored -> void
        
        """
        pass
    
    
    def RedirectToAnotherSubentity(self):
        """
        RedirectToAnotherSubentity -> void
            
            ObjectId oldObjectId: 
            The DBObject whose AssocGeomDependencies are to be redirected. It will be opened for write.
            
            SubentityId oldSubentId: 
            The SubentityId of the AssocGeomDependencies that is to be redirected.
            
            ObjectId newObjectId: 
            The object to redirect the dependencies to. It will be opened for write.
            
            SubentityId newSubentId: 
            The new SubentityId in the new object.
        """
        pass
    
    
    EdgeSubentityGeometry = None
    
    
    FaceSubentityGeometry = None
    
    
    IsCachingSubentityGeometry = None
    
    
    PersistentSubentId = None
    
    
    Subentity = None
    
    
    SubentityType = None
    
    
    TransientSubentCount = None
    
    
    TransientSubentIds = None
    
    
    VertexSubentityGeometry = None
    
    pass

class AssocGlobalUtility(object):
    """
    
    """
    def EvaluationRequestSeverityLevel(self):
        """
        EvaluationRequestSeverityLevel -> Integer
            
            AssocStatus status: 
            The AssocStatus.
        """
        pass
    
    
    def IsDraggingProvidingSubstituteObjects(self):
        """
        IsDraggingProvidingSubstituteObjects -> bool
            
            AssocEvaluationCallback evaluationCallback: 
            The current AssocEvaluationCallback. NULL pointer is allowed.
        """
        pass
    
    
    def IsEvaluationRequest(self):
        """
        IsEvaluationRequest -> bool
            
            AssocStatus status: 
            The AssocStatus.
        """
        pass
    
    
    def IsToBeSkipped(self):
        """
        IsToBeSkipped -> bool
            
            AssocStatus status: 
            The AssocStatus.
        """
        pass
    
    pass

class AssocLoftedSurfaceActionBody(object):
    """
    
    AssocLoftedSurfaceActionBody()
    """
    class ProfileType():
        EndCrossSection = 2
        EndGuide = 8
        StartCrossSection = 1
        StartGuide = 4
    
    
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge(ProfileType) -> double
        
        GetBulge(ProfileType, out string, out string) -> double
        
        """
        pass
    
    
    def GetContinuity(self):
        """
        GetContinuity(ProfileType) -> Integer
        
        GetContinuity(ProfileType, out string, out string) -> Integer
        
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge(ProfileType, double) -> void
        
        SetBulge(ProfileType, double, string, string) -> void
        
        """
        pass
    
    
    def SetContinuity(self):
        """
        SetContinuity(ProfileType, int) -> void
        
        SetContinuity(ProfileType, int, string, string) -> void
        
        """
        pass
    
    pass

class AssocManager(object):
    """
    
    AssocManager()
    """
    def AddGlobalEvaluationCallback(self):
        """
        AddGlobalEvaluationCallback -> void
            
            int order: 
            Specifies the ordering of the user-provided callbacks in the global AssocEvaluationMultiCallback. The lower-order callbacks are called before the higher-order callbacks. The drag callback is inserted with order 0, i.e. callbacks with negative order will be called before it and callbacks with positive order will be called after it.
            
            pCallback: 
            The user-provided evaluation callback. The callback does not become owned by the global AssocEvaluationMultiCallback, it is just referenced by it.
        """
        pass
    
    
    def AuditAssociativeData(self):
        """
        AuditAssociativeData -> void
            
            Database database: 
            Database whose associative data is to be audited.
            
            [MarshalAs(UnmanagedType.U1)] bool traverseWholeDatabase: 
            If true, all objects in the database are visited and checked, and therefore loaded into memory.
        """
        pass
    
    
    def EvaluateTopLevelNetwork(self):
        """
        EvaluateTopLevelNetwork -> bool
            
            AssocEvaluationCallback callback: 
            Optional AssocEvaluationCallback that is added to the global callback before the evaluation and removed after the evaluation is completed.
            
            int callbackOrder: 
            Order of the optional AssocEvaluationCallback.
            
            patabase: 
            Database whose top-level network is to be evaluated.
        """
        pass
    
    
    def GetGlobalEvaluationCallbacks(self):
        """
        GetGlobalEvaluationCallbacks -> void
            
            ref ArrayList callbacks: 
            The returned evaluation callbacks.
            
            ref ArrayList orders: 
            The returned evaluation callback orders.
        """
        pass
    
    
    def GlobalEvaluationMultiCallback(self):
        """
        GlobalEvaluationMultiCallback -> AssocEvaluationCallback
        
        """
        pass
    
    
    def HasAssocNetwork(self):
        """
        HasAssocNetwork -> bool
        
        """
        pass
    
    
    def Initialize(self):
        """
        Initialize -> void
        
        """
        pass
    
    
    def RemoveGlobalEvaluationCallback(self):
        """
        RemoveGlobalEvaluationCallback -> void
            
            pCallback: 
            The user-provided evaluation callback to be removed.
        """
        pass
    
    pass

class AssocNetwork(object):
    """
    
    AssocNetwork()
    """
    def AddAction(self):
        """
        AddAction -> void
            
            ObjectId actionId: 
            AssocAction being added to the network.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoSetAsDatabaseOwner: 
            Make this network the database owner of the action.
        """
        pass
    
    
    def AddActions(self):
        """
        AddActions -> void
            
            ObjectIdCollection actionIds: 
            AssocActions being added to the network.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoSetAsDatabaseOwner: 
            Make this network the database owner of the actions.
        """
        pass
    
    
    def GetInstanceFromDatabase(self):
        """
        GetInstanceFromDatabase -> ObjectId
            
            Database database: 
            Database owning the network.
            
            [MarshalAs(UnmanagedType.U1)] bool createIfDoesNotExist: 
            If it does not exist yet, create a new subdictionary under the named object dictionary of the database. Create an AssocNetwork and make it owned by this newly created subdictionary.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
        """
        pass
    
    
    def GetInstanceFromObject(self):
        """
        GetInstanceFromObject -> ObjectId
            
            ObjectId owningObjectId: 
            The Object owning the sub-dictionary that owns the AssocNetwork.
            
            [MarshalAs(UnmanagedType.U1)] bool createIfDoesNotExist: 
            If it does not exist yet, create a new subdictionary of the extension dictionary of the object. Create an AssocNetwork and make it owned by this newly created subdictionary.
            
            [MarshalAs(UnmanagedType.U1)] bool addToTopLevelNetwork: 
            If the network is newly created, it also adds it to the the top-level network of the database that owns the owningObjectId. It has no effect if the network already exists or if createIfDoesNotExist is false.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
        """
        pass
    
    
    def OwnedActionStatusChanged(self):
        """
        OwnedActionStatusChanged -> void
            
            AssocAction ownedAction: 
            The action whose status has just been changed.
            
            AssocStatus previousStatus: 
            Previous status of the action.
        """
        pass
    
    
    def RemoveAction(self):
        """
        RemoveAction -> void
            
            ObjectId actionId: 
            AssocAction being removed from the network.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erase the action after removing it.
        """
        pass
    
    
    def RemoveAllActions(self):
        """
        RemoveAllActions -> void
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseThem: 
            Erase the actions after removing them.
        """
        pass
    
    
    def RemoveInstanceFromDatabase(self):
        """
        RemoveInstanceFromDatabase -> void
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erase the network after removing it.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
            
            owningObjectId: 
            The database whose named object dictionary owns the sub-dictionary that owns the AssocNetwork.
        """
        pass
    
    
    def RemoveInstanceFromObject(self):
        """
        RemoveInstanceFromObject -> void
            
            ObjectId owningObjectId: 
            The DBObject whose extension dictionary owns the sub-dictionary that owns the AssocNetwork.
            
            [MarshalAs(UnmanagedType.U1)] bool alsoEraseIt: 
            Erase the network after removing it.
            
            string dictionaryKey: 
            The name of the sub-dictionary under which the network belongs. If no key name is given, the default "ACAD_ASSOCNETWORK" key is used.
        """
        pass
    
    
    GetActions = None
    
    pass

class AssocNetworkSurfaceActionBody(object):
    """
    
    AssocNetworkSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge(AssocLoftedSurfaceActionBody.ProfileType) -> double
        
        GetBulge(AssocLoftedSurfaceActionBody.ProfileType, out string, out string) -> double
        
        """
        pass
    
    
    def GetContinuity(self):
        """
        GetContinuity(AssocLoftedSurfaceActionBody.ProfileType) -> Integer
        
        GetContinuity(AssocLoftedSurfaceActionBody.ProfileType, out string, out string) -> Integer
        
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge(AssocLoftedSurfaceActionBody.ProfileType, double) -> void
        
        SetBulge(AssocLoftedSurfaceActionBody.ProfileType, double, string, string) -> void
        
        """
        pass
    
    
    def SetContinuity(self):
        """
        SetContinuity(AssocLoftedSurfaceActionBody.ProfileType, int) -> void
        
        SetContinuity(AssocLoftedSurfaceActionBody.ProfileType, int, string, string) -> void
        
        """
        pass
    
    pass

class AssocObjectTransaction(object):
    """
    
    AssocObjectTransaction(AssocAction)
        AssocAction actionBeingEvaluated : The action that is just being evaluated.
    
    
    AssocObjectTransaction(AssocActionBody)
        AssocActionBody actionBodyBeingEvaluated : The action that is just being evaluated.
    
    
    AssocObjectTransaction(AssocDependency)
        AssocDependency dependencyBeingEvaluated : The action that is just being evaluated.
    
    
    AssocObjectTransaction(AssocDependencyBody)
        AssocDependencyBody dependencyBodyBeingEvaluated : The action that is just being evaluated.
    
    
    """
    def IsSubstituteObject(self):
        """
        IsSubstituteObject -> bool
            
            DBObject dbObject: 
            Object for which it finds out whether there is a substitute object.
        """
        pass
    
    
    def GetDBObject(self):
        """
        GetDBObject -> DBObject
            
            ObjectId objectId: 
            ObjectId of the object that should be opened.
            
            OpenMode openMode: 
            ForRead, ForWrite, ForNotify.
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Opens the object even if it is erased.
            
            [MarshalAs(UnmanagedType.U1)] bool openOnLockedLayer: 
            Opens the object even on the locked layer.
        """
        pass
    
    pass

class AssocOffsetSurfaceActionBody(object):
    """
    
    AssocOffsetSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetDistance(self):
        """
        GetDistance -> double
        
        """
        pass
    
    
    def SetDistance(self):
        """
        SetDistance -> void
        
        """
        pass
    
    
    Distance = None
    
    pass

class AssocParamBasedActionBody(object):
    """
    
    """

    pass

class AssocPatchSurfaceActionBody(object):
    """
    
    AssocPatchSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance(ObjectId, EdgeRef[], EdgeRef[], VertexRef[], [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        CreateInstance(ObjectId, EdgeRef[], EdgeRef[], VertexRef[], int, double, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def GetBulge(self):
        """
        GetBulge -> double
        
        """
        pass
    
    
    def GetContinuity(self):
        """
        GetContinuity -> Integer
        
        """
        pass
    
    
    def SetBulge(self):
        """
        SetBulge -> void
        
        """
        pass
    
    
    def SetConstraintCurves(self):
        """
        SetConstraintCurves -> void
        
        """
        pass
    
    
    def SetConstraintPoints(self):
        """
        SetConstraintPoints -> void
        
        """
        pass
    
    
    def SetContinuity(self):
        """
        SetContinuity -> void
        
        """
        pass
    
    
    Bulge = None
    
    
    Continuity = None
    
    
    ContinuityGripPoint = None
    
    pass

class AssocPathActionParam(object):
    """
    
    AssocPathActionParam()
    """
    def GetEdgeRefArray(self):
        """
        GetEdgeRefArray -> EdgeRef()()
        
        """
        pass
    
    
    def SetEdgeRefArray(self):
        """
        SetEdgeRefArray -> void
        
        """
        pass
    
    
    def UpdateEdgeRef(self):
        """
        UpdateEdgeRef -> void
        
        """
        pass
    
    pass

class AssocPathBasedSurfaceActionBody(object):
    """
    
    AssocPathBasedSurfaceActionBody()
    """
    def GetInputPaths(self):
        """
        GetInputPaths -> void
        
        """
        pass
    
    
    def GetInputPoints(self):
        """
        GetInputPoints -> VertexRef()
        
        """
        pass
    
    
    def MakeInputPathsDrawOnTopOfResultingSurface(self):
        """
        MakeInputPathsDrawOnTopOfResultingSurface -> void
        
        """
        pass
    
    
    def RemoveAllPathParams(self):
        """
        RemoveAllPathParams -> void
        
        """
        pass
    
    
    def SetInputPaths(self):
        """
        SetInputPaths(EdgeRef[]) -> void
        
        SetInputPaths(PathRef[]) -> void
        
        """
        pass
    
    
    def SetInputPoints(self):
        """
        SetInputPoints -> void
        
        """
        pass
    
    
    def UpdateInputPath(self):
        """
        UpdateInputPath -> void
        
        """
        pass
    
    
    InputPathParams = None
    
    pass

class AssocPersSubentityId(object):
    """
    
    AssocPersSubentityId()
    """
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            See the AuditInfo documentation.
        """
        pass
    
    
    def CreateObjectAndDwgInFields(self):
        """
        CreateObjectAndDwgInFields -> void
            
            Database database: 
            AcDbDatabase that is going to own the AcDbAssocPersSubentId.
            
            DwgFiler filer: 
            The filer to read the data from. The first data is the class identification.
            
            ref AssocPersSubentityId createdPersSubentId: 
            This is an in/out argument used to return the created and filled-in object of an AssocPersSubentityId-derived class. If the createdPersSubentId is passed in as not NULL, the code tries to reuse the existing object, if it is of the expected derived class. If it is passed in as NULL or is not of the expected derived type, it creates a new object (deleting the existing one, if any).
        """
        pass
    
    
    def CreateObjectAndDxfInFields(self):
        """
        CreateObjectAndDxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the data from. The first data is the class identification.
            
            ref AssocPersSubentityId createdPersSubentId: 
            This is an in/out argument used to return the created and filled-in object of an AssocPersSubentityId-derived class. If the createdPersSubentId is passed in as not NULL, the code tries to reuse the existing object, if it is of the expected derived class. If it is passed in as NULL or is not of the expected derived type, it creates a new object (deleting the existing one, if any).
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> void
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> void
            
            DwgFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> void
            
            DxfFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def GetTransientSubentIds(self):
        """
        GetTransientSubentIds -> SubentityId()
            
            Entity entity: 
            The entity needs to be open for read.
            
            subents: 
            The returned SubentityIds.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            AssocPersSubentityId other: 
            The other AssocPersSubentityId.
            
            ntity: 
            The entity owning the subentities of this and the other AssocPersSubentityId.
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> void
            
            Entity mirroredEntity: 
            The entity that has been mirrored. It needs to be open for read.
        """
        pass
    
    
    def SubentType(self):
        """
        SubentType -> SubentityType
            
            Entity entity: 
            The entity needs to be open for read.
        """
        pass
    
    
    def TransientSubentCount(self):
        """
        TransientSubentCount -> Integer
            
            Entity entity: 
            The entity needs to be open for read.
        """
        pass
    
    
    IsNull = None
    
    pass

class AssocPersSubentityIdPE(object):
    """
    
    AssocPersSubentityIdPE()
    """
    def CreateNewPersSubent(self):
        """
        CreateNewPersSubent -> AssocPersSubentityId
            
            Entity entity: 
            The entity must be open for write, but usually no changes to the entity will be made.
            
            CompoundObjectId compId: 
            Contains full context path to entity. Can be empty for simple reference.
            
            SubentityId subentId: 
            Transient SubentityId.
        """
        pass
    
    
    def GetAllSubentities(self):
        """
        GetAllSubentities -> SubentityId()
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityType subentType: 
            The required type of the subentities.
        """
        pass
    
    
    def GetEdgeSubentityGeometry(self):
        """
        GetEdgeSubentityGeometry -> Curve3d
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId edgeSubentId: 
            Edge SubentityId whose curve is to be obtained.
        """
        pass
    
    
    def GetEdgeVertexSubentities(self):
        """
        GetEdgeVertexSubentities -> void
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId edgeSubentId: 
            Edge SubentityId whose vertex SubentityIds are to be obtained.
            
            ref SubentityId startVertexSubentId: 
            Returned SubentityId of the start vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId endVertexSubentId: 
            Returned SubentityId of the end vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId[] otherVertexSubentIds: 
            Returned other SubentityIds associated with the edge, such as the circle or arc center, spline control and fit points, etc.
        """
        pass
    
    
    def GetFaceSubentityGeometry(self):
        """
        GetFaceSubentityGeometry -> Autodesk.AutoCAD.Geometry.Surface
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId faceSubentId: 
            Face SubentityId whose surface is to be changed.
        """
        pass
    
    
    def GetRigidSetState(self):
        """
        GetRigidSetState -> Integer
            
            Entity entity: 
            The entity must be open for read.
        """
        pass
    
    
    def GetRigidSetTransform(self):
        """
        GetRigidSetTransform -> Matrix3d
            
            Entity entity: 
            The entity must be open for read.
        """
        pass
    
    
    def GetSplineEdgeVertexSubentities(self):
        """
        GetSplineEdgeVertexSubentities -> void
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId edgeSubentId: 
            Edge SubentId whose vertex SubentityIds are to be obtained.
            
            ref SubentityId startVertexSubentId: 
            Returned SubentityId of the start vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId endVertexSubentId: 
            Returned SubentityId of the end vertex of the edge (or NullSubentityId if there is not any).
            
            ref SubentityId[] controlPointSubentIds: 
            Returned SubentityIds identifying the spline control points. The order is the same as the order of the spline control points.
            
            ref SubentityId[] fitPointSubentIds: 
            Returned SubentityIds identifying the spline fit points (if any). The order is the same as the order of the spline fit points.
        """
        pass
    
    
    def GetSubentGeometryXform(self):
        """
        GetSubentGeometryXform -> Matrix3d
            
            Entity entity: 
            The entity must be open for read.
            
            ObjectId[] fullSubentPath: 
            Full path of the sub-entity whose collective transformation matrix is to be determined.
        """
        pass
    
    
    def GetTransientSubentityIds(self):
        """
        GetTransientSubentityIds -> SubentityId()
            
            Entity entity: 
            The entity needs to be open for read.
            
            AssocPersSubentityId perSubentId: 
            The persistent subentity id on the entity.
        """
        pass
    
    
    def GetVertexSubentityGeometry(self):
        """
        GetVertexSubentityGeometry -> Point3d
            
            Entity entity: 
            The entity must be open for read.
            
            SubentityId vertexSubentId: 
            Vertex SubentityId whose position is to be obtained.
        """
        pass
    
    
    def MirrorPersSubent(self):
        """
        MirrorPersSubent -> void
            
            Entity mirroredEntity: 
            The entity that has been mirrored. It needs to be open for read.
            
            AssocPersSubentityId persSubentIdToMirror: 
            The AssocPersSubentityId to be changed to reflect the fact that the entity has been mirrored.
        """
        pass
    
    
    def SetEdgeSubentityGeometry(self):
        """
        SetEdgeSubentityGeometry -> void
            
            Entity entity: 
            The entity must be open for write.
            
            SubentityId edgeSubentId: 
            Edge SubentityId whose curve is to be changed.
            
            Curve3d newEdgeCurve: 
            New curve of the edge subentity (copied, not reused).
        """
        pass
    
    
    def SetFaceSubentityGeometry(self):
        """
        SetFaceSubentityGeometry -> void
            
            Entity entity: 
            The entity must be open for write.
            
            SubentityId faceSubentId: 
            Face SubentityId whose surface is to be changed.
            
            Autodesk.AutoCAD.Geometry.Surface newFaceSurface: 
            New surface of the face subentity (copied, not reused).
        """
        pass
    
    
    def SetRigidSetTransform(self):
        """
        SetRigidSetTransform -> void
            
            Entity entity: 
            The entity must be open for write.
            
            Matrix3d trans: 
            New transformation matrix of the rigid set entity.
        """
        pass
    
    
    def SetVertexSubentityGeometry(self):
        """
        SetVertexSubentityGeometry -> void
            
            Entity entity: 
            The entity must be open for write.
            
            SubentityId vertexSubentId: 
            Vertex SubentityId whose position is to be changed.
            
            Point3d newVertexPosition: 
            New coordinates of the vertex subentity.
        """
        pass
    
    pass

class AssocPlaneSurfaceActionBody(object):
    """
    
    AssocPlaneSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    pass

class AssocRevolvedSurfaceActionBody(object):
    """
    
    AssocRevolvedSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetRevolveAngle(self):
        """
        GetRevolveAngle -> double
        
        """
        pass
    
    
    def SetRevolveAngle(self):
        """
        SetRevolveAngle -> void
        
        """
        pass
    
    
    RevolveAngle = None
    
    pass

class AssocSimplePersSubentId(object):
    """
    
    AssocSimplePersSubentId()
    """
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            See the AuditInfo documentation.
        """
        pass
    
    
    def DwgInFields(self):
        """
        DwgInFields -> void
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> void
            
            DwgFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> void
            
            DxfFiler filer: 
            The filer to write the object data to.
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            Entity entity: 
            The entity owning the subentities of this and the other AssocPersSubentityId.
            
            AssocPersSubentityId other: 
            The other AssocSimplePersSubentityId.
        """
        pass
    
    
    def SubentId(self):
        """
        SubentId -> SubentityId
        
        """
        pass
    
    
    def SubentType(self):
        """
        SubentType -> SubentityType
        
        """
        pass
    
    
    def TransientSubentCount(self):
        """
        TransientSubentCount -> Integer
            
            Entity entity: 
            Not used.
        """
        pass
    
    
    IsNull = None
    
    pass

class AssocSingleEdgePersSubentId(object):
    """
    
    AssocSingleEdgePersSubentId()
    """
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            Entity entity: 
            The entity owning the subentities of this and the other AssocSingleEdgePersSubentId.
            
            AssocPersSubentityId other: 
            The other AssocSingleEdgePersSubentId.
        """
        pass
    
    
    def SubentType(self):
        """
        SubentType -> SubentityType
            
            Entity entity: 
            Not used.
        """
        pass
    
    
    def TransientSubentCount(self):
        """
        TransientSubentCount -> Integer
            
            Entity entity: 
            Not used.
        """
        pass
    
    
    IsNull = None
    
    pass

class AssocStatus():
    IsUpToDateAssocStatus = None
    ChangedDirectlyAssocStatus = None
    ChangedTransitivelyAssocStatus = None
    ChangedNoDifferenceAssocStatus = None
    FailedToEvaluateAssocStatus = None
    ErasedAssocStatus = None
    SuppressedAssocStatus = None

class AssocSurfaceActionBody(object):
    """
    
    AssocSurfaceActionBody()
    """
    def EvaluateOverride(self):
        """
        EvaluateOverride -> void
        
        """
        pass
    
    
    def FindActionsThatAffectedTopologicalSubentity(self):
        """
        FindActionsThatAffectedTopologicalSubentity -> ObjectIdCollection
        
        """
        pass
    
    
    def ResultingSurfaceDep(self):
        """
        ResultingSurfaceDep([MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        ResultingSurfaceDep([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def SetResultingSurface(self):
        """
        SetResultingSurface -> void
        
        """
        pass
    
    
    IsSemiAssociative = None
    
    
    ResultingSurface = None
    
    pass

class AssocSweptSurfaceActionBody(object):
    """
    
    AssocSweptSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectId
        
        """
        pass
    
    
    def GetAlignAngle(self):
        """
        GetAlignAngle -> double
        
        """
        pass
    
    
    def GetScaleFactor(self):
        """
        GetScaleFactor -> double
        
        """
        pass
    
    
    def GetTwistAngle(self):
        """
        GetTwistAngle -> double
        
        """
        pass
    
    
    def SetAlignAngle(self):
        """
        SetAlignAngle -> void
        
        """
        pass
    
    
    def SetScaleFactor(self):
        """
        SetScaleFactor -> void
        
        """
        pass
    
    
    def SetTwistAngle(self):
        """
        SetTwistAngle -> void
        
        """
        pass
    
    
    AlignAngle = None
    
    
    ScaleFactor = None
    
    
    TwistAngle = None
    
    pass

class AssocTransformationType():
    NotSpecified = None
    Stretch = None
    Rotate = None
    Move = None

class AssocTrimSurfaceActionBody(object):
    """
    
    AssocTrimSurfaceActionBody()
    """
    def CreateInstance(self):
        """
        CreateInstance -> ObjectIdCollection
        
        """
        pass
    
    
    def MakeTrimPermanent(self):
        """
        MakeTrimPermanent -> void
        
        """
        pass
    
    
    def SetTrimInfo(self):
        """
        SetTrimInfo -> void
        
        """
        pass
    
    
    def Untrim(self):
        """
        Untrim -> void
        
        """
        pass
    
    
    TrimmedArea = None
    
    pass

class AssocValueDependency(object):
    """
    
    AssocValueDependency()
    """
    DependentOnObjectValue = None
    
    
    ValueName = None
    
    pass

class AssocValueProviderPE(object):
    """
    
    AssocValueProviderPE()
    """
    def CanGetValue(self):
        """
        CanGetValue -> bool
            
            string valueName: 
            The name of the queried value.
            
            object: 
            The object must be open for read.
        """
        pass
    
    
    def CanSetValue(self):
        """
        CanSetValue -> bool
            
            string valueName: 
            The name of the queried value.
            
            object: 
            The object must be open for read.
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue -> ResultBuffer
            
            string valueName: 
            The name of the queried value.
            
            object: 
            The object must be open for read.
        """
        pass
    
    
    def SetValue(self):
        """
        SetValue -> void
            
            string valueName: 
            The name of the value to be set.
            
            ResultBuffer newValue: 
            The new value.
            
            object: 
            The object must be open for write.
        """
        pass
    
    pass

class AssocVariable(object):
    """
    
    AssocVariable()
    """
    def AddGlobalCallback(self):
        """
        AddGlobalCallback -> void
            
            pCallback: 
            The callback to be registered.
        """
        pass
    
    
    def EvaluateExpression(self):
        """
        EvaluateExpression(ObjectIdCollection, ResultBuffer[], ResultBuffer) -> string
            
            ref ObjectIdCollection objectIds: 
            Array of ids of value-providing objects. It is an in/out argument. It is being appended during the evaluation with ids of the value-providing objects whose values have been obtained (currently these objects are only AssocVariables).
            
            ref ResultBuffer[] objectValues: 
            Array of values of value-providing objects. It is an in/out argument. It is being appended during the evaluation with values of the value-providing objects whose values have been obtained (currently these objects are only AssocVariables).
            
            ref ResultBuffer evaluatedExpressionValue: 
            Returned evaluated value of the expression.
        EvaluateExpression(ResultBuffer) -> string
            
            ref ResultBuffer evaluatedExpressionValue: 
            Returned evaluated value of the expression.
        """
        pass
    
    
    def FindObjectByName(self):
        """
        FindObjectByName -> ObjectId
            
            string objectName: 
            The name of the searched-for object.
            
            RXClass pObjectClass: 
            The class of the searched-for object (isKindOf() test is used).
        """
        pass
    
    
    def globalCallback(self):
        """
        globalCallback -> AssocVariableCallback
        
        """
        pass
    
    
    def RemoveGlobalCallback(self):
        """
        RemoveGlobalCallback -> void
            
            pCallback: 
            The callback to be unregistered.
        """
        pass
    
    
    def SetName(self):
        """
        SetName -> void
            
            string newName: 
            New name of the variable.
            
            [MarshalAs(UnmanagedType.U1)] bool updateReferencingExpressions: 
            If true, it finds all expressions referencing this variable and changes them (changes their strings) to reflect the new name of the variable.
        """
        pass
    
    
    def ValidateNameAndExpression(self):
        """
        ValidateNameAndExpression -> void
            
            string nameToValidate: 
            The variable name to validate. May be null.
            
            string expressionToValidate: 
            The variable expression to validate. May be null.
            
            ref string errorMessage: 
            Error string if the name or expression is not valid, empty otherwise.
        """
        pass
    
    
    Description = None
    
    
    EvaluatorId = None
    
    
    Expression = None
    
    
    Name = None
    
    
    Value = None
    
    pass

class AssocVariableCallback(object):
    """
    
    AssocVariableCallback()
    """
    def CanBeErased(self):
        """
        CanBeErased -> bool
            
            AssocVariable variable: 
            The AcDbAssocVariable that is to be erased.
        """
        pass
    
    
    def ValidateNameAndExpression(self):
        """
        ValidateNameAndExpression -> string
            
            AssocVariable variable: 
            The variable whose name and/or expression are being validated.
            
            string nameToValidate: 
            The variable name to validate. May be null.
            
            string expressionToValidate: 
            The variable expression to validate. May be null.
        """
        pass
    
    pass

class AssocVertexActionParam(object):
    """
    
    AssocVertexActionParam()
    """
    def GetVertexRef(self):
        """
        GetVertexRef -> VertexRef
        
        """
        pass
    
    
    def SetVertexRef(self):
        """
        SetVertexRef -> void
        
        """
        pass
    
    
    DependentOnCompoundObject = None
    
    pass

class AttachmentPoint():
    BaseAlign = 13
    BaseCenter = 11
    BaseFit = 0x11
    BaseLeft = 10
    BaseMid = 0x15
    BaseRight = 12
    BottomAlign = 14
    BottomCenter = 8
    BottomFit = 0x12
    BottomLeft = 7
    BottomMid = 0x16
    BottomRight = 9
    MiddleAlign = 15
    MiddleCenter = 5
    MiddleFit = 0x13
    MiddleLeft = 4
    MiddleMid = 0x17
    MiddleRight = 6
    TopAlign = 0x10
    TopCenter = 2
    TopFit = 20
    TopLeft = 1
    TopMid = 0x18
    TopRight = 3

class AttributeCollection(object):
    """
    
    """
    def AppendAttribute(self):
        """
        AppendAttribute -> ObjectId
            
            [CallerMustClose] AttributeReference attributeToAddToBlockReference: 
            Input the attribute to add.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectId[] array: 
            Input the array to copy to.
            
            int index: 
            Input the index position to start adding at.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class AttributeDefinition(object):
    """
    
    AttributeDefinition()()
    
    
    """
    def UpdateMTextAttributeDefinition(self):
        """
        UpdateMTextAttributeDefinition -> void
        
        """
        pass
    
    
    Constant = None
    
    
    FieldLength = None
    
    
    Invisible = None
    
    
    IsMTextAttributeDefinition = None
    
    
    LockPositionInBlock = None
    
    
    MTextAttributeDefinition = None
    
    
    Preset = None
    
    
    Prompt = None
    
    
    Tag = None
    
    
    Verifiable = None
    
    pass

class AttributeReference(object):
    """
    
    AttributeReference()()
    
    
    """
    def SetAttributeFromBlock(self):
        """
        SetAttributeFromBlock(AttributeDefinition, Matrix3d) -> void
            
            AttributeDefinition definition: 
            Input the the attribute definition entity to be used as a data template
            
            Matrix3d blockTransform: 
            Input a block transformation matrix.
        SetAttributeFromBlock(Matrix3d) -> void
            
            Matrix3d blockTransform: 
            Input a block transformation matrix.
        """
        pass
    
    
    def UpdateMTextAttribute(self):
        """
        UpdateMTextAttribute -> void
        
        """
        pass
    
    
    FieldLength = None
    
    
    Invisible = None
    
    
    IsConstant = None
    
    
    IsMTextAttribute = None
    
    
    IsPreset = None
    
    
    IsVerifiable = None
    
    
    LockPositionInBlock = None
    
    
    MTextAttribute = None
    
    
    Tag = None
    
    pass

class AuditInfo(object):
    """
    
    """
    def ErrorsFixed(self):
        """
        ErrorsFixed -> void
            
            int count: 
            Input the number of errors fixed
        """
        pass
    
    
    def ErrorsFound(self):
        """
        ErrorsFound -> void
            
            int count: 
            Input the number of errors found
        """
        pass
    
    
    def IncNumEntities(self):
        """
        IncNumEntities -> void
        
        """
        pass
    
    
    def PrintError(self):
        """
        PrintError(DBObject, string, string, string) -> void
            
            DBObject value: 
            Input the name string will be extracted.
            
            string value2: 
            Input a string describing the value of the bad data
            
            string validation: 
            Input a string describing the reason the data is bad
            
            string defaultValue: 
            Input a string describing the default value it is set to
        PrintError(string, string, string, string) -> void
            
            string name: 
            Input a string describing the type of erroneous data found
            
            string value: 
            Input a string describing the value of the bad data
            
            string validation: 
            Input a string describing the reason the data is bad
            
            string defaultValue: 
            Input a string describing the default value it is set to
        """
        pass
    
    
    def PrintNumEntities(self):
        """
        PrintNumEntities -> void
            
            string msg: 
            Input the string to be printed
        """
        pass
    
    
    def RequestRegen(self):
        """
        RequestRegen -> void
        
        """
        pass
    
    
    def ResetNumEntities(self):
        """
        ResetNumEntities -> void
        
        """
        pass
    
    
    AuditPass = None
    
    
    FixErrors = None
    
    
    NumEntities = None
    
    
    NumErrors = None
    
    
    NumFixes = None
    
    pass

class AuditPass():
    Pass1 = 1
    Pass2 = 2

class AutoConstrainEvaluationCallback(object):
    """
    
    AutoConstrainEvaluationCallback
        AcAutoConstrainEvaluationCallback* impObj : Unmanaged C++ object pointer
    """
    def GetAutoConstrainPriority(self):
        """
        GetAutoConstrainPriority -> GeometricalConstraint.ConstraintType()
            
            constraintList: 
            List of constraint types to be considered for autoConstrain in decending order of priority. Constraint type not present in the list will not be considered for autoconstraint.
        """
        pass
    
    
    def GetConstraintPriorityOverride(self):
        """
        GetConstraintPriorityOverride -> Integer
            
            GeometricalConstraint.ConstraintType type: 
            Geometric constraint type that is possible between given set of constrained geometry.
            
            ConstrainedGeometry[] geometries: 
            List of constrained geometry, which are potential candidate for provided constraint type. User may
        """
        pass
    
    
    def GetTotalConstraints(self):
        """
        GetTotalConstraints -> Integer
            
            ref GeometricalConstraint[] constraints: 
            reference to array of constraints, to return list of constraints found by autoconstraint evaluation. This parameter can be null if caller doesn't want list of constraints.
        """
        pass
    
    
    IsEvaluationCancelled = None
    
    pass

class Background(object):
    """
    
    """
    def GetBackgroundDictionaryId(self):
        """
        GetBackgroundDictionaryId -> ObjectId
            
            Database database: 
            Input the database from which to retrieve the background dictionary
            
            [MarshalAs(UnmanagedType.U1)] bool createIfNotPresent: 
            Input whether the function should create the background dictionary if it does not currently exists in the specified database
        """
        pass
    
    pass

class BeginInsertEventArgs(object):
    """
    
    """
    From = None
    
    pass

class BeginWblockBlockEventArgs(object):
    """
    
    """
    BlockId = None
    
    
    From = None
    
    pass

class BeginWblockEntireDatabaseEventArgs(object):
    """
    
    """
    From = None
    
    pass

class BeginWblockObjectsEventArgs(object):
    """
    
    """
    From = None
    
    
    IdMapping = None
    
    pass

class BeginWblockSelectedObjectsEventArgs(object):
    """
    
    """
    From = None
    
    
    InsertionPoint = None
    
    pass

class BlendOptions(object):
    """
    
    BlendOptions()
    """
    class DriveModeType():
        DriveModeFirst = None
        DriveModeSecond = None
        DriveModeBoth = None
    
    
    CoplanarDirection = None
    
    
    CoplanarPoint = None
    
    
    DriveMode = None
    
    
    Quality = None
    
    
    Simplify = None
    
    
    Solid = None
    
    pass

class BlendOptionsBuilder(object):
    """
    
    """
    def ToBlendOptions(self):
        """
        ToBlendOptions -> BlendOptions
        
        """
        pass
    
    
    CoplanarDirection = None
    
    
    CoplanarPoint = None
    
    
    DriveMode = None
    
    
    Quality = None
    
    
    Simplify = None
    
    
    Solid = None
    
    pass

class BlockBegin(object):
    """
    
    BlockBegin()
    """

    pass

class BlockConnectionType():
    ConnectExtents = None
    ConnectBase = None

class BlockEnd(object):
    """
    
    BlockEnd()
    """

    pass

class BlockInsertionPointsEventArgs(object):
    """
    
    BlockInsertionPointsEventArgs
        Autodesk.AutoCAD.DatabaseServices.BlockTableRecord blockTableRecord : Input block table record to insert at
        Point3dCollection points : Input the points to insert
        Vector3dCollection alignmentVectors : Input the vectors to align against
    """
    AlignmentVectors = None
    
    
    BlockTableRecord = None
    
    
    InsertionPoints = None
    
    pass

class BlockReference(object):
    """
    
    BlockReference
        Point3d position : Input Autodesk.AutoCAD.Geometry.Point3d object, the position point
        ObjectId blockTableRecord : Input Autodesk.AutoCAD.DatabaseServices.ObjectId object, the object ID of BlockTableRecord to reference
    """
    def ConvertToStaticBlock(self):
        """
        ConvertToStaticBlock() -> void
        
        ConvertToStaticBlock(string) -> void
            
            string newBlockName: 
            Input the name of the new block definition
        """
        pass
    
    
    def ExplodeToOwnerSpace(self):
        """
        ExplodeToOwnerSpace -> void
        
        """
        pass
    
    
    def GeometryExtentsBestFit(self):
        """
        GeometryExtentsBestFit() -> Extents3d
        
        GeometryExtentsBestFit(Matrix3d) -> Extents3d
            
            Matrix3d parentTransform: 
            Input Autodesk.AutoCAD.Geometry.Matrix3d transformation to be applied to the block reference’s geometry
        """
        pass
    
    
    def ResetBlock(self):
        """
        ResetBlock -> void
        
        """
        pass
    
    
    AnonymousBlockTableRecord = None
    
    
    AttributeCollection = None
    
    
    BlockTableRecord = None
    
    
    BlockTransform = None
    
    
    BlockUnit = None
    
    
    DynamicBlockReferencePropertyCollection = None
    
    
    DynamicBlockTableRecord = None
    
    
    IsDynamicBlock = None
    
    
    Name = None
    
    
    Normal = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    ScaleFactors = None
    
    
    TreatAsBlockRefForExplode = None
    
    
    UnitFactor = None
    
    pass

class BlockScaling():
    Any = None
    Uniform = None

class BlockTable(object):
    """
    
    """

    pass

class BlockTableRecord(object):
    """
    
    BlockTableRecord()
    """
    def AppendEntity(self):
        """
        AppendEntity -> ObjectId
            
            [CallerMustClose] Entity entity: 
            Input the object to append (must not be NULL)
        """
        pass
    
    
    def AssumeOwnershipOf(self):
        """
        AssumeOwnershipOf -> void
            
            ObjectIdCollection entitiesToMove: 
            Input a collection of entities to change ownership of
        """
        pass
    
    
    def GetAnonymousBlockIds(self):
        """
        GetAnonymousBlockIds -> ObjectIdCollection
        
        """
        pass
    
    
    def GetBlockReferenceIds(self):
        """
        GetBlockReferenceIds -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool directOnly: 
            Input an indication that only those BlockReferences that directly refer to this BlockTableRecord should be included in the IDs. If this value is true and the block is nested, the parent block's references will not be included.
            
            [MarshalAs(UnmanagedType.U1)] bool forceValidity: 
            Input an indication that older drawings which have been demand loaded should be loaded completely, in order to find their BlockReferenceIds. This is because older drawings did not store this information. This parameter is only applicable if directOnly is false.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> BlockTableRecordEnumerator
        
        """
        pass
    
    
    def GetErasedBlockReferenceIds(self):
        """
        GetErasedBlockReferenceIds -> ObjectIdCollection
        
        """
        pass
    
    
    def GetXrefDatabase(self):
        """
        GetXrefDatabase -> Database
            
            [MarshalAs(UnmanagedType.U1)] bool incrementUnresolved: 
            Input an indication whether or not to return the database of an unresolved xref
        """
        pass
    
    
    def UpdateAnonymousBlocks(self):
        """
        UpdateAnonymousBlocks -> void
        
        """
        pass
    
    
    BlockBeginId = None
    
    
    BlockEndId = None
    
    
    BlockScaling = None
    
    
    Comments = None
    
    
    DrawOrderTableId = None
    
    
    Explodable = None
    
    
    HasAttributeDefinitions = None
    
    
    HasPreviewIcon = None
    
    
    Hyperlinks = None
    
    
    IncludingErased = None
    
    
    IsAnonymous = None
    
    
    IsDynamicBlock = None
    
    
    IsFromExternalReference = None
    
    
    IsFromOverlayReference = None
    
    
    IsLayout = None
    
    
    IsUnloaded = None
    
    
    LayoutId = None
    
    
    Origin = None
    
    
    PathName = None
    
    
    PreviewIcon = None
    
    
    Units = None
    
    
    XrefStatus = None
    
    pass

class BlockTableRecordEnumerator(object):
    """
    
    """
    def MoveNext(self):
        """
        MoveNext -> bool
        
        """
        pass
    
    pass

class Body(object):
    """
    
    Body()
    """
    def AcisIn(self):
        """
        AcisIn -> DBObjectCollection
            
            string fileName: 
            Input the file name of ASCII ACIS SAT file to be read in.
        """
        pass
    
    
    def AcisOut(self):
        """
        AcisOut -> void
            
            string fileName: 
            Input the file name to write data to.
            
            DBObjectCollection entitiesOutToFile: 
            Input a collection containing all the Entity objects that are to be written out to the file
        """
        pass
    
    
    IsNull = None
    
    
    NumChanges = None
    
    
    UsesGraphicsCache = None
    
    pass

class BooleanOperationType():
    BoolUnite = None
    BoolIntersect = None
    BoolSubtract = None

class BulgeVertex(object):
    """
    
    BulgeVertex
        Point2d point : Input the 2D coordinates of the new vertex.
        double bulge : Input the new bulge value.
    """
    Bulge = None
    
    
    Vertex = None
    
    pass

class BulgeVertexCollection(object):
    """
    
    BulgeVertexCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            BulgeVertex value: 
            Input the object to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            BulgeVertex value: 
            Input the object to check for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            BulgeVertex[] array: 
            Input the object to copy from.
            
            int index: 
            Input the index to begin copying.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            BulgeVertex value: 
            Input the object to check.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the index to insert at.
            
            BulgeVertex value: 
            Input the object to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            BulgeVertex value: 
            Input the object to remove.
        """
        pass
    
    pass

class CallerMustCloseAttribute(object):
    """
    
    """

    pass

class Cell(object):
    """
    
    """
    Column = None
    
    
    Row = None
    
    pass

class CellAlignment():
    BottomCenter = 8
    BottomLeft = 7
    BottomRight = 9
    MiddleCenter = 5
    MiddleLeft = 4
    MiddleRight = 6
    TopCenter = 2
    TopLeft = 1
    TopRight = 3

class CellClass():
    Label = None
    Data = None

class CellContentLayout():
    Flow = 1
    StackedHorizontal = 2
    StackedVertical = 4

class CellContentTypes():
    Block = 4
    Field = 2
    Unknown = 0
    Value = 1

class CellEdgeMasks():
    BottomMask = 4
    LeftMask = 8
    RightMask = 2
    TopMask = 1

class CellMargins():
    Bottom = 4
    Left = 2
    Right = 8
    Top = 1

class CellOption():
    InheritCellFormat = None

class CellProperties():
    Alignment = 0x10
    AutoScale = 0x100
    BackgroundColor = 0x200
    ContentColor = 0x20
    ContentLayout = 0x4000
    DataFormat = 2
    DataType = 1
    FlowDirBtoT = 0x10000
    Invalid = 0
    MarginBottom = 0x2000
    MarginHorzSpacing = 0x20000
    MarginLeft = 0x400
    MarginRight = 0x1000
    MarginTop = 0x800
    MarginVertSpacing = 0x40000
    MergeAll = 0x8000
    Rotation = 4
    Scale = 8
    TextHeight = 0x80
    TextStyle = 0x40

class CellRange(object):
    """
    
    CellRange()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object pRange: 
            Input range to check against.
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    BottomRight = None
    
    
    BottomRow = None
    
    
    LeftColumn = None
    
    
    RightColumn = None
    
    
    TopLeft = None
    
    
    TopRow = None
    
    pass

class CellStates():
    ContentLocked = 1
    ContentModifiedAfterUpdate = 8
    ContentReadOnly = 2
    FormatLocked = 0x10
    FormatModifiedAfterUpdate = 0x40
    FormatReadOnly = 0x20
    Linked = 4
    None = 0

class CellType():
    Unknown = None
    Integer = None
    Double = None
    CharPtr = None
    Point = None
    ObjectId = None
    HardOwnerId = None
    SoftOwnerId = None
    HardPtrId = None
    SoftPtrId = None
    Bool = None
    Vector = None

class CenterPointConstraint(object):
    """
    
    """

    pass

class Circle(object):
    """
    
    Circle()()
    
    
    Circle(Point3d, Vector3d, double)
        Point3d center : Input center location
        Vector3d normal : Input normal vector
        double radius : Input radius length
    
    
    """
    Center = None
    
    
    Circumference = None
    
    
    Diameter = None
    
    
    Normal = None
    
    
    Radius = None
    
    
    Thickness = None
    
    pass

class ClipBoundaryType():
    Invalid = None
    Rectangle = None
    Poly = None

class ColinearConstraint(object):
    """
    
    ColinearConstraint()
    """

    pass

class CollisionType():
    Solid = None

class ColumnType():
    NoColumns = None
    StaticColumns = None
    DynamicColumns = None

class CompositeConstraint(object):
    """
    
    """
    OwnedConstraints = None
    
    pass

class CompoundObjectId(object):
    """
    
    CompoundObjectId()()
    
    
    CompoundObjectId(CompoundObjectId)()
    
    
    CompoundObjectId(ObjectId)
        ObjectId id : ObjectId of the DBObject that this CompoundObjectId is going to reference.
    
    
    CompoundObjectId(ObjectId, Database)
        ObjectId id : ObjectId of the DBObject that this CompoundObjectId is going to reference.
        Database hostDatabase : The host database. If null, the database is taken from the ObjectId (even if it is in XREF database).
    
    
    CompoundObjectId(ObjectId, ObjectIdCollection, Database)
        ObjectId id : ObjectId of the DBObject that this CompoundObjectId is going to reference.
        ObjectIdCollection path : The path of BlockRefrences that lead to the referenced object. The first BlockReference in the path resides in the host database, the second BlockReference is from the BlockTableRecord that the first BlockReference references, the third BlockReference is from the BlockTableRecord that the second BlockReference references, etc.
        pHostDatabase : The host database. If null, the database is taken from the first BlockReference id in the path (even if it is in XREF database).
    
    
    """
    class StatusType():
        CouldNotResolveNonTerminal = 2
        CouldNotResolveTerminal = 3
        CouldNotResolveTooEarly = 4
        IncompatibleIdType = 0x3e8
        Valid = 0
        WasLoadedNowUnloaded = 1
    
    
    def DwgInFields(self):
        """
        DwgInFields -> void
            
            DwgFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DwgOutFields(self):
        """
        DwgOutFields -> void
            
            DwgFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def DxfInFields(self):
        """
        DxfInFields -> void
            
            DxfFiler filer: 
            The filer to read the object data from.
        """
        pass
    
    
    def DxfOutFields(self):
        """
        DxfOutFields -> void
            
            DxfFiler filer: 
            The filer to read the object data to.
        """
        pass
    
    
    def IsValid(self):
        """
        IsValid -> bool
            
            int validityCheckingLevel: 
            Input the level of testing.
        """
        pass
    
    
    def NullId(self):
        """
        NullId -> CompoundObjectId
        
        """
        pass
    
    
    def Remap(self):
        """
        Remap -> bool
            
            IdMapping idMap: 
            See the description of the IdMapping class.
        """
        pass
    
    
    def Set(self):
        """
        Set(CompoundObjectId, Database) -> void
        
        Set(ObjectId, Database) -> void
            
            ObjectId id: 
            ObjectId of the Object that this CompoundObjectId is going to reference.
            
            Database hostDatabase: 
            The host database. If null, the database is taken from the ObjectId (even if it is in XREF database).
        Set(ObjectId, ObjectIdCollection, Database) -> void
            
            ObjectId id: 
            ObjectId of the DBObject that this CompoundObjectId is going to reference.
            
            ObjectIdCollection path: 
            The path of BlockRefrences that lead to the referenced object. The first BlockRefrence in the path resides in the host database, the second BlockReference is from the BlockTableRecord that the first BlockReference references, the third BlockReference is from the BlockTableRecord that the second BlockReference references, etc.
            
            Database hostDatabase: 
            The host database. If null, the database is taken from the first BlockReference id in the path (even if it is in XREF database).
        """
        pass
    
    
    def SetEmpty(self):
        """
        SetEmpty -> void
        
        """
        pass
    
    
    def SetFullPath(self):
        """
        SetFullPath -> void
            
            ObjectIdCollection fullPath: 
            The path of AcDbBlockRefrences and the leaf level object itself as the last element of the array.
            
            pHostDatabase: 
            The host database. If null, the database is taken from the first AcDbBlockReference id in the fullPath.
        """
        pass
    
    
    FullPath = None
    
    
    IsEmpty = None
    
    
    IsExternal = None
    
    
    IsSimpleObjectId = None
    
    
    LeafId = None
    
    
    Path = None
    
    
    Status = None
    
    
    TopId = None
    
    
    Transform = None
    
    pass

class ConcentricConstraint(object):
    """
    
    ConcentricConstraint()
    """

    pass

class ConstrainType():
    TurnHeight = None
    Turns = None
    Height = None

class Constrained2PointsConstructionLine(object):
    """
    
    Constrained2PointsConstructionLine()()
    
    
    Constrained2PointsConstructionLine(Point3d, Point3d)
        Point3d point1 : Input first 3D point. Relative to the work plane of the owning Assoc2dConstraintGroup object.
        Point3d point2 : Input second 3D point. Relative to the work plane of the owning Assoc2dConstraintGroup object.
    
    
    """

    pass

class ConstrainedArc(object):
    """
    
    ConstrainedArc()()
    
    
    ConstrainedArc(ObjectId)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained arc is holding on.
    
    
    """
    EndPoint = None
    
    
    MidPoint = None
    
    
    StartPoint = None
    
    pass

class ConstrainedBoundedEllipse(object):
    """
    
    ConstrainedBoundedEllipse()()
    
    
    ConstrainedBoundedEllipse(ObjectId)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained bounded ellipse is holding on.
    
    
    """
    EndPoint = None
    
    
    StartPoint = None
    
    pass

class ConstrainedBoundedLine(object):
    """
    
    ConstrainedBoundedLine()()
    
    
    ConstrainedBoundedLine(ObjectId, [MarshalAs(UnmanagedType.U1)] bool)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained line is holding on.
        [MarshalAs(UnmanagedType.U1)] bool ray : Input Boolean indicating whether this bounded line is a ray.
    
    
    """
    EndPoint = None
    
    
    IsRay = None
    
    
    MidPoint = None
    
    
    StartPoint = None
    
    pass

class ConstrainedCircle(object):
    """
    
    ConstrainedCircle()()
    
    
    ConstrainedCircle(ObjectId)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained circle is holding on.
    
    
    """
    CenterPoint = None
    
    
    Radius = None
    
    pass

class ConstrainedConstructionLine(object):
    """
    
    ConstrainedConstructionLine()
    """

    pass

class ConstrainedCurve(object):
    """
    
    """
    ConstrainedImplicitPoints = None
    
    
    IsBounded = None
    
    pass

class ConstrainedDatumLine(object):
    """
    
    ConstrainedDatumLine()()
    
    
    ConstrainedDatumLine(Point3d, Vector3d)
        Point3d pointOnLine : Input any 3D point. Relative to the work plane of the owning Assoc2dConstraintGroup object.
        Vector3d direction : Input any 3D vector(must not be zero length). Relative to the work plane of the owning Assoc2dConstraintGroup object.
    
    
    """

    pass

class ConstrainedEllipse(object):
    """
    
    ConstrainedEllipse()()
    
    
    ConstrainedEllipse(ObjectId)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained ellipse is holding on.
    
    
    """
    CenterPoint = None
    
    
    Direction = None
    
    
    MajorRadius = None
    
    
    MinorRadius = None
    
    pass

class ConstrainedGeometry(object):
    """
    
    """
    def CommonConstraints(self):
        """
        CommonConstraints -> GeometricalConstraint()
            
            ConstrainedGeometry otherConsGeom: 
            The reference to the other ConstrainedGeometry object.
        """
        pass
    
    
    ConnectedConstraints = None
    
    
    ConnectedGeometries = None
    
    
    FullSubentityPaths = None
    
    
    GeomDependencyId = None
    
    
    IsReadOnly = None
    
    
    OwningRigidSet = None
    
    pass

class ConstrainedImplicitPoint(object):
    """
    
    ConstrainedImplicitPoint()()
    
    
    ConstrainedImplicitPoint(uint, Autodesk.AutoCAD.DatabaseServices.ImplicitPointType, int)
        uint constrCurvId : Input ConstraintGroupNodeId indicating the constrained curve to which this implicit point belongs.
        Autodesk.AutoCAD.DatabaseServices.ImplicitPointType ptype : Input ImplicitPointType indicating the type of this implicit point.
        int index : Input int indicating the define point index of this implicit point. It is only valid when the point type is kDefineImplicit. Default value is -1 (invalid index).
    
    
    """
    ConstrainedCurveId = None
    
    
    Point = None
    
    
    PointIndex = None
    
    
    PointType = None
    
    pass

class ConstrainedLine(object):
    """
    
    ConstrainedLine()()
    
    
    ConstrainedLine(ObjectId)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained line is holding on.
    
    
    """
    Direction = None
    
    
    PointOnLine = None
    
    pass

class ConstrainedPoint(object):
    """
    
    ConstrainedPoint()()
    
    
    ConstrainedPoint(ObjectId)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained line is holding on.
    
    
    """
    Point = None
    
    pass

class ConstrainedRigidSet(object):
    """
    
    ConstrainedRigidSet()()
    
    
    ConstrainedRigidSet([MarshalAs(UnmanagedType.U1)] bool, Matrix3d)
        [MarshalAs(UnmanagedType.U1)] bool bScalable : Input boolean indicating whether this rigid set can be uniformly scaled or not.
        Matrix3d trans : Input Matrix3d indicating the initial transform of this rigid set Relative to the work plane of the owning Assoc2dConstraintGroup object.
    
    
    """
    def GetConstrainedGeomAt(self):
        """
        GetConstrainedGeomAt -> ConstrainedGeometry
            
            int index: 
            Input the index.
        """
        pass
    
    
    NumOfConstrainedGeoms = None
    
    
    Transform = None
    
    pass

class ConstrainedSpline(object):
    """
    
    ConstrainedSpline()()
    
    
    ConstrainedSpline(ObjectId, NurbCurve3d)
        ObjectId geomDependencyId : Input ObjectId indicating the AssocGeomDependency object to which this constrained spline is holding on.
        NurbCurve3d spline : Input NurbCurve3d indicating the AcGe representation of this constrained spline Relative to the work plane of the owning Assoc2dConstraintGroup object.
    
    
    """
    def DefinePointAt(self):
        """
        DefinePointAt -> Point3d
            
            int index: 
            Input the index.
        """
        pass
    
    
    NumOfDefinePoints = None
    
    
    NurbSpline = None
    
    pass

class ConstraintGroupNode(object):
    """
    
    """
    NodeId = None
    
    
    OwningConstraintGroupId = None
    
    pass

class ContentType():
    NoneContent = None
    BlockContent = None
    MTextContent = None
    ToleranceContent = None

class Curve(object):
    """
    
    """
    def CreateFromGeCurve(self):
        """
        CreateFromGeCurve(Curve3d) -> Curve
        
        CreateFromGeCurve(Curve3d, Tolerance) -> Curve
        
        CreateFromGeCurve(Curve3d, Vector3d) -> Curve
        
        CreateFromGeCurve(Curve3d, Vector3d, Tolerance) -> Curve
        
        """
        pass
    
    
    def Extend(self):
        """
        Extend([MarshalAs(UnmanagedType.U1)] bool, Point3d) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool extendStart: 
            Input whether to extend the curve's start or end .
            
            Point3d toPoint: 
            Input the new start or end point of the curve.
        Extend(double) -> void
            
            double newParameter: 
            Input the new start or end parameter on the curve
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Point3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input the point (in WCS coordinates) for which to find nearest point on curve
            
            Vector3d direction: 
            Input the normal vector (in WCS coordinates) for plane to project onto
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input whether or not to extend curve in search for nearest point.
        GetClosestPointTo(Point3d, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input the point (in WCS coordinates) for which to find nearest point on curve
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input whether or not to extend curve in search for nearest point.
        """
        pass
    
    
    def GetDistanceAtParameter(self):
        """
        GetDistanceAtParameter -> double
            
            double value: 
            Input the object representing the parameter.
        """
        pass
    
    
    def GetDistAtPoint(self):
        """
        GetDistAtPoint -> double
            
            Point3d point: 
            Input the object representing the point.
        """
        pass
    
    
    def GetFirstDerivative(self):
        """
        GetFirstDerivative(Point3d) -> Vector3d
            
            Point3d point: 
            Input the derivative value
        GetFirstDerivative(double) -> Vector3d
            
            double value: 
            Input the derivative value
        """
        pass
    
    
    def GetGeCurve(self):
        """
        GetGeCurve() -> Curve3d
        
        GetGeCurve(Tolerance) -> Curve3d
        
        """
        pass
    
    
    def GetOffsetCurves(self):
        """
        GetOffsetCurves -> DBObjectCollection
            
            double offsetDist: 
            Input the distance to offset the curve
        """
        pass
    
    
    def GetOffsetCurvesGivenPlaneNormal(self):
        """
        GetOffsetCurvesGivenPlaneNormal -> DBObjectCollection
            
            Vector3d normal: 
            Input the normal vector for plane in which to offset
            
            double offsetDist: 
            Input distance to offset the curve
        """
        pass
    
    
    def GetOrthoProjectedCurve(self):
        """
        GetOrthoProjectedCurve -> Curve
            
            Plane planeToProjectOn: 
            Input plane onto which the curve is to be projected
        """
        pass
    
    
    def GetParameterAtDistance(self):
        """
        GetParameterAtDistance -> double
            
            double dist: 
            Input distance along the curve from the beginning of the curve to the location for the desired parameter.
        """
        pass
    
    
    def GetParameterAtPoint(self):
        """
        GetParameterAtPoint -> double
            
            Point3d point: 
            Input point (in WCS coordinates) on the curve at which the parameter is desired Returns the parameter of the curve at point
        """
        pass
    
    
    def GetPointAtDist(self):
        """
        GetPointAtDist -> Point3d
            
            double value: 
            Input distance along the curve from the beginning of the curve to the location of the desired point
        """
        pass
    
    
    def GetPointAtParameter(self):
        """
        GetPointAtParameter -> Point3d
            
            double value: 
            Input parameter on the curve at which the point is desired
        """
        pass
    
    
    def GetProjectedCurve(self):
        """
        GetProjectedCurve -> Curve
            
            Plane planeToProjectOn: 
            Input plane onto which the curve is to be projected
            
            Vector3d projectionDirection: 
            Input direction (in WCS coordinates) of the projection
        """
        pass
    
    
    def GetSecondDerivative(self):
        """
        GetSecondDerivative(Point3d) -> Vector3d
            
            Point3d point: 
            Input the derivative value
        GetSecondDerivative(double) -> Vector3d
            
            double value: 
            Input the derivative value
        """
        pass
    
    
    def GetSplitCurves(self):
        """
        GetSplitCurves(DoubleCollection) -> DBObjectCollection
            
            DoubleCollection value: 
            Input collection of points (in WCS coordinates) on the curve
        GetSplitCurves(Point3dCollection) -> DBObjectCollection
            
            Point3dCollection points: 
            Input collection of parameters on the curve
        """
        pass
    
    
    def ReverseCurve(self):
        """
        ReverseCurve -> void
        
        """
        pass
    
    
    def SetFromGeCurve(self):
        """
        SetFromGeCurve(Curve3d) -> void
        
        SetFromGeCurve(Curve3d, Tolerance) -> void
        
        SetFromGeCurve(Curve3d, Vector3d) -> void
        
        SetFromGeCurve(Curve3d, Vector3d, Tolerance) -> void
        
        """
        pass
    
    
    Area = None
    
    
    Closed = None
    
    
    EndParam = None
    
    
    EndPoint = None
    
    
    IsPeriodic = None
    
    
    Spline = None
    
    
    StartParam = None
    
    
    StartPoint = None
    
    pass

class CustomObjectSnapMode(object):
    """
    
    CustomObjectSnapMode(string, string, string, Autodesk.AutoCAD.GraphicsInterface.Glyph)
        string localModeString : Input local mode string
        string globalModeString : Input global mode string
        string toolTipText : Input tool tip text
        Autodesk.AutoCAD.GraphicsInterface.Glyph glyph : Input glyph to use
    
    
    CustomObjectSnapMode(string, string, string, Autodesk.AutoCAD.GraphicsInterface.Glyph, System.Drawing.Bitmap, string)
        string localModeString : Input local mode string
        string globalModeString : Input global mode string
        string toolTipText : Input tool tip text
        Autodesk.AutoCAD.GraphicsInterface.Glyph glyph : Input glyph to use
        System.Drawing.Bitmap bitmap : Input menu item icon
        string displayString : Input menu item display string
    
    
    """
    def Activate(self):
        """
        Activate -> void
            
            string mode: 
            Input custom OSNAP mode string
        """
        pass
    
    
    def ApplyToEntityType(self):
        """
        ApplyToEntityType -> void
            
            RXClass entity: 
            Input entity to apply to
            
            AddObjectSnapInfo callback: 
            Input callback to apply
        """
        pass
    
    
    def Deactivate(self):
        """
        Deactivate -> void
            
            string mode: 
            Input mode string
        """
        pass
    
    
    def IsActive(self):
        """
        IsActive -> bool
            
            string mode: 
            Input custom OSNAP mode string
        """
        pass
    
    
    def RemoveFromEntityType(self):
        """
        RemoveFromEntityType -> void
            
            RXClass entity: 
            Input entity to remove
        """
        pass
    
    
    Bitmap = None
    
    
    DisplayString = None
    
    
    GlobalModeString = None
    
    
    Glyph = None
    
    
    GlyphSize = None
    
    
    LocalModeString = None
    
    
    ToolTipText = None
    
    pass

class CustomScale(object):
    """
    
    CustomScale
        double numerator : Input numerator value
        double denominator : Input denominator value
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
        IsEqualTo(CustomScale) -> bool
            
            CustomScale a: 
            Input scale to compare
        IsEqualTo(CustomScale, Tolerance) -> bool
            
            CustomScale a: 
            Input custom scale to compare
            
            Tolerance tolerance: 
            Input tolerance range
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object definition.
        """
        pass
    
    
    Denominator = None
    
    
    Numerator = None
    
    pass

class DBDictionary(object):
    """
    
    DBDictionary()
    """
    def Contains(self):
        """
        Contains(ObjectId) -> bool
            
            ObjectId objId: 
            Object to search for
        Contains(string) -> bool
            
            string entryName: 
            Name to search by
        """
        pass
    
    
    def Copy(self):
        """
        Copy -> DBDictionary
        
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DBDictionaryEntry[] array: 
            Array to receive data from
            
            int index: 
            Index to begin at
        """
        pass
    
    
    def GetAt(self):
        """
        GetAt -> ObjectId
            
            string entryName: 
            String representing the entry's search key name to look for
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> DbDictionaryEnumerator
        
        """
        pass
    
    
    def NameAt(self):
        """
        NameAt -> string
            
            ObjectId objId: 
            Object ID to search for
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ObjectId) -> void
            
            ObjectId objId: 
            Object ID of the object to remove
        Remove(string) -> ObjectId
            
            string key: 
            String representing the entry's key (or name)
        """
        pass
    
    
    def SetAt(self):
        """
        SetAt -> ObjectId
            
            string searchKey: 
            String representing the object's search key name
            
            [CallerMustClose] DBObject newValue: 
            The new object to add to the dictionary
        """
        pass
    
    
    def SetName(self):
        """
        SetName -> void
            
            string oldName: 
            String representing the entry's old key string name
            
            string newName: 
            String representing the entry's new key string name
        """
        pass
    
    
    Count = None
    
    
    IncludingErased = None
    
    
    MergeStyle = None
    
    
    TreatElementsAsHard = None
    
    pass

class DBDictionaryEntry(object):
    """
    
    DBDictionaryEntry
        string key : Original key
        ObjectId value : Original object ID value
    """
    m_key = None
    
    
    m_value = None
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object.
        """
        pass
    
    
    Key = None
    
    
    Value = None
    
    pass

class DBObject(object):
    """
    
    """
    def AddContext(self):
        """
        AddContext -> void
            
            ObjectContext context: 
            The context to add.
        """
        pass
    
    
    def ApplyPaperOrientationTransform(self):
        """
        ApplyPaperOrientationTransform -> void
            
            Autodesk.AutoCAD.DatabaseServices.Viewport viewport: 
            The viewport in which the object is to be displayed.
        """
        pass
    
    
    def ApplyPartialUndo(self):
        """
        ApplyPartialUndo -> void
            
            DwgFiler undoFiler: 
            The undo filer containing the partial undo information to be re-instated
            
            RXClass classObj: 
            The RXClass object for the class that is expected to be handling this Undo information
        """
        pass
    
    
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            An AuditInfo object
        """
        pass
    
    
    def Cancel(self):
        """
        Cancel -> void
        
        """
        pass
    
    
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def CloseAndPage(self):
        """
        CloseAndPage -> void
            
            [MarshalAs(UnmanagedType.U1)] bool onlyWhenClean: 
            Boolean indicating to turn off or on undo recording
        """
        pass
    
    
    def CreateExtensionDictionary(self):
        """
        CreateExtensionDictionary -> void
        
        """
        pass
    
    
    def DecomposeForSave(self):
        """
        DecomposeForSave -> DecomposeForSaveReplacementRecord
            
            DwgVersion version: 
            DWG version being saved to
        """
        pass
    
    
    def DeepClone(self):
        """
        DeepClone -> DBObject
            
            DBObject ownerPointer: 
            Object to which the clones should be appended
            
            IdMapping idMap: 
            Current object ID map
            
            [MarshalAs(UnmanagedType.U1)] bool isPrimary: 
            Boolean indicating whether this object is primary or owned
        """
        pass
    
    
    def DisableUndoRecording(self):
        """
        DisableUndoRecording -> void
            
            [MarshalAs(UnmanagedType.U1)] bool disable: 
            Boolean indicating to turn off or on Undo recording
        """
        pass
    
    
    def DowngradeOpen(self):
        """
        DowngradeOpen -> void
        
        """
        pass
    
    
    def DowngradeToNotify(self):
        """
        DowngradeToNotify -> void
            
            [MarshalAs(UnmanagedType.U1)] bool wasWritable: 
            Input indicating if object was open for write when upgradeFromNotify was called
        """
        pass
    
    
    def GetBinaryDataForKey(self):
        """
        GetBinaryDataForKey -> byte()
            
            string key: 
            Input extension dictionary key under which the data is stored
        """
        pass
    
    
    def DwgIn(self):
        """
        DwgIn -> void
            
            DwgFiler filer: 
            DWG filer to be used for this filing operation
        """
        pass
    
    
    def DwgOut(self):
        """
        DwgOut -> void
            
            DwgFiler filer: 
            DWG filer to be used for this filing operation
        """
        pass
    
    
    def DxfIn(self):
        """
        DxfIn -> void
            
            DxfFiler filer: 
            DXF filer to be used for this filing operation
        """
        pass
    
    
    def DxfOut(self):
        """
        DxfOut -> void
            
            DxfFiler filer: 
            Filer to be used for this filing operation
        """
        pass
    
    
    def HandOverTo(self):
        """
        HandOverTo -> void
            
            [CallerMustClose] DBObject newPointer: 
            Object to be used to replace the current object
            
            [MarshalAs(UnmanagedType.U1)] bool keepXData: 
            Boolean indicating if xdata is to be transferred during the process
            
            [MarshalAs(UnmanagedType.U1)] bool keepExtensionDictionary: 
            Boolean indicating whether the extension dictionary is passed on from the old object to the new one. If set to kTrue, the extension dictionary will be passed on, otherwise it will be left behind.
        """
        pass
    
    
    def Erase(self):
        """
        Erase() -> void
        
        Erase([MarshalAs(UnmanagedType.U1)] bool) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool erasing: 
            Boolean indicating if object is to be erased or unerased
        """
        pass
    
    
    def GetField(self):
        """
        GetField() -> Autodesk.AutoCAD.DatabaseServices.ObjectId
        
        GetField(string) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            string propertyName: 
            Input a property name for the field you want to retrieve
        """
        pass
    
    
    def GetObjectSaveVersion(self):
        """
        GetObjectSaveVersion(DwgFiler) -> FullDwgVersion
            
            DwgFiler filer: 
            Filer to be used for this filing operation
        GetObjectSaveVersion(DxfFiler) -> FullDwgVersion
            
            DxfFiler filer: 
            DXF filer to be used for this filing operation
        """
        pass
    
    
    def GetPersistentReactorIds(self):
        """
        GetPersistentReactorIds -> ObjectIdCollection
        
        """
        pass
    
    
    def SetBinaryDataForKey(self):
        """
        SetBinaryDataForKey -> void
            
            string key: 
            Input extension dictionary key to be used
            
            byte[] chunk: 
            Input a flat array of bytes that are the binary data to save
        """
        pass
    
    
    def GetReactors(self):
        """
        GetReactors -> List<RXObject>
        
        """
        pass
    
    
    def GetTransientReactors(self):
        """
        GetTransientReactors -> List<RXObject>
        
        """
        pass
    
    
    def GetXDataForApplication(self):
        """
        GetXDataForApplication -> ResultBuffer
            
            string applicationName: 
            Name of the registered application to use when retrieving the xdata
        """
        pass
    
    
    def HasContext(self):
        """
        HasContext -> bool
            
            ObjectContext context: 
            The context to check for.
        """
        pass
    
    
    def HasPersistentReactor(self):
        """
        HasPersistentReactor -> bool
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId objId: 
            Object ID of a persistent reactor object
        """
        pass
    
    
    def IsCustomObject(self):
        """
        IsCustomObject -> bool
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId id: 
            Custom ID to check.
        """
        pass
    
    
    def ReleaseExtensionDictionary(self):
        """
        ReleaseExtensionDictionary -> void
        
        """
        pass
    
    
    def RemoveContext(self):
        """
        RemoveContext -> void
            
            ObjectContext context: 
            The context to remove from the collection.
        """
        pass
    
    
    def RemoveField(self):
        """
        RemoveField() -> Autodesk.AutoCAD.DatabaseServices.ObjectId
        
        RemoveField(Autodesk.AutoCAD.DatabaseServices.ObjectId) -> void
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId id: 
            Field ID to remove from the object
        RemoveField(string) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            string propertyName: 
            Property name whose field is to be removed
        """
        pass
    
    
    def ResetScaleDependentProperties(self):
        """
        ResetScaleDependentProperties -> void
        
        """
        pass
    
    
    def SetField(self):
        """
        SetField([CallerMustClose] Field) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            [CallerMustClose] Field field: 
            Field to set
        SetField(string, [CallerMustClose] Field) -> Autodesk.AutoCAD.DatabaseServices.ObjectId
            
            string propertyName: 
            Property name for which to set the field
            
            [CallerMustClose] Field field: 
            Field to set
        """
        pass
    
    
    def SetFromStyle(self):
        """
        SetFromStyle -> bool
        
        """
        pass
    
    
    def SetObjectIdsInFlux(self):
        """
        SetObjectIdsInFlux -> void
        
        """
        pass
    
    
    def SetPaperOrientation(self):
        """
        SetPaperOrientation -> void
            
            [MarshalAs(UnmanagedType.U1)] bool bPaperOrientation: 
            The new value for the paper orientation property.
        """
        pass
    
    
    def SupportsCollection(self):
        """
        SupportsCollection -> bool
            
            string collectionName: 
            The name of the collection (context type) to test for support.
        """
        pass
    
    
    def SwapIdWith(self):
        """
        SwapIdWith -> void
            
            Autodesk.AutoCAD.DatabaseServices.ObjectId otherId: of object to swap with
            
            [MarshalAs(UnmanagedType.U1)] bool swapExtendedData: 
            Boolean indicating whether to swap extended entity data
            
            [MarshalAs(UnmanagedType.U1)] bool swapExtensionDictionary: 
            Boolean indicating whether to swap extension dictionaries
        """
        pass
    
    
    def SwapReferences(self):
        """
        SwapReferences -> void
            
            IdMapping idMap: 
            Input refedit ID map
        """
        pass
    
    
    def UpgradeFromNotify(self):
        """
        UpgradeFromNotify -> bool
        
        """
        pass
    
    
    def UpgradeOpen(self):
        """
        UpgradeOpen -> void
        
        """
        pass
    
    
    def WblockClone(self):
        """
        WblockClone -> DBObject
            
            RXObject ownerPointer: 
            Input object to which the clones should be appended. If the owner has not been cloned, then the Database must be passed in.
            
            IdMapping idMap: 
            Input current object ID map
            
            [MarshalAs(UnmanagedType.U1)] bool isPrimary: 
            Input Boolean indicating whether this object is primary or owned
        """
        pass
    
    
    def XDataTransformBy(self):
        """
        XDataTransformBy -> void
            
            Matrix3d transform: 
            Transformation matrix to be applied to the XData
        """
        pass
    
    
    Annotative = None
    
    
    ClassID = None
    
    
    Database = None
    
    
    Drawable = None
    
    
    ExtensionDictionary = None
    
    
    Handle = None
    
    
    HasFields = None
    
    
    HasSaveVersionOverride = None
    
    
    Id = None
    
    
    IsAProxy = None
    
    
    IsCancelling = None
    
    
    IsErased = None
    
    
    IsEraseStatusToggled = None
    
    
    IsModified = None
    
    
    IsModifiedGraphics = None
    
    
    IsModifiedXData = None
    
    
    IsNewObject = None
    
    
    IsNotifyEnabled = None
    
    
    IsNotifying = None
    
    
    IsObjectIdsInFlux = None
    
    
    IsPersistent = None
    
    
    IsReadEnabled = None
    
    
    IsReallyClosing = None
    
    
    IsTransactionResident = None
    
    
    IsUndoing = None
    
    
    IsWriteEnabled = None
    
    
    MergeStyle = None
    
    
    ObjectBirthVersion = None
    
    
    ObjectId = None
    
    
    OwnerId = None
    
    
    PaperOrientation = None
    
    
    UndoFiler = None
    
    
    XData = None
    
    pass

class DBObjectCollection(object):
    """
    
    DBObjectCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            DBObject value: 
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
            
            DBObject value: 
            Object to look for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DBObject[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to start copying at
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
            
            DBObject value: 
            Item to retrieve the index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Index to insert at
            
            DBObject value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            DBObject value: 
            Item to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of item to remove
        """
        pass
    
    
    Count = None
    
    pass

class DBObjectReference(object):
    """
    
    DBObjectReference
        Autodesk.AutoCAD.DatabaseServices.ObjectId id : Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        int kind : Input System.Int32 object
    """
    Kind = None
    
    
    ObjectId = None
    
    pass

class DBObjectReferenceCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            DBObjectReference value: 
            Input object to add
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            DBObjectReference value: 
            Object to look for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DBObjectReference[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to start copying at
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            DBObjectReference value: 
            Item to retrieve the index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Index to insert at
            
            DBObjectReference value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            DBObjectReference value: 
            Item to remove
        """
        pass
    
    pass

class DBPoint(object):
    """
    
    DBPoint()()
    
    
    DBPoint(Point3d)
        Point3d position : Input position (in WCS coordinates) for the point
    
    
    """
    EcsRotation = None
    
    
    Normal = None
    
    
    Position = None
    
    
    Thickness = None
    
    pass

class DBText(object):
    """
    
    DBText()
    """
    def AdjustAlignment(self):
        """
        AdjustAlignment -> void
            
            Database alternateDatabaseToUse: 
            Database to be used if the text entity is not in a database (this argument is ignored if the text entity is in a database)
        """
        pass
    
    
    def ConvertFieldToText(self):
        """
        ConvertFieldToText -> void
        
        """
        pass
    
    
    def CorrectSpelling(self):
        """
        CorrectSpelling -> Integer
        
        """
        pass
    
    
    AlignmentPoint = None
    
    
    Height = None
    
    
    HorizontalMode = None
    
    
    IsDefaultAlignment = None
    
    
    IsMirroredInX = None
    
    
    IsMirroredInY = None
    
    
    Justify = None
    
    
    Normal = None
    
    
    Oblique = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    TextString = None
    
    
    TextStyleName = None
    
    
    Thickness = None
    
    
    VerticalMode = None
    
    
    WidthFactor = None
    
    pass

class DBVisualStyle(object):
    """
    
    DBVisualStyle()
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            VisualStyle pSrc: 
            Input visual style source
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            VisualStyle pDest: 
            Input visual style destination.
        """
        pass
    
    
    def GetTrait(self):
        """
        GetTrait -> object
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty being queried.
        """
        pass
    
    
    def GetTraitFlag(self):
        """
        GetTraitFlag -> bool
            
            uint modopt(IsLong) flagVal: 
            Input bit flag enum unsigned long property being queried.
            
            flagProp: 
            Input bitfield enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty being queried.
        """
        pass
    
    
    def SetTrait(self):
        """
        SetTrait(VisualStyleProperty, Autodesk.AutoCAD.Colors.Color, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty being set. Valid Property values for this method are:FaceMonoColorEdgeIntersectionColorEdgeObscuredColorEdgeColorEdgeSilhouetteColor
            
            pColor: 
            Input AcCmColor property value.
            
            op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, [MarshalAs(UnmanagedType.U1)] bool, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:EdgeHidePrecision
            
            [MarshalAs(UnmanagedType.U1)] bool bVal: 
            Input boolean property value to set.
            
            op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, double, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceOpacityFaceSpecularEdgeCreaseAngleEdgeOpacityDisplayBrightness
            
            double dVal: 
            Input double property value to set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, double, double, double, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceMonoColorEdgeIntersectionColorEdgeObscuredColorEdgeColorEdgeSilhouetteColor
            
            double red: 
            Input red color value to set. Valid value is from 0.0 to 1.0.
            
            double green: 
            Input green color value to set. Valid value is from 0.0 to 1.0.
            
            double blue: 
            Input blue color value to set. Valid value is from 0.0 to 1.0.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, int, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set. Valid Property values for this method are:FaceLightingModelFaceLightingQualityFaceColorModeFaceModifierEdgeModelEdgeStyleEdgeObscuredLinePatternEdgeIntersectionLinePatternEdgeModifierEdgeWidthEdgeOverhangEdgeJitterAmountEdgeSilhouetteWidthEdgeHaloGapEdgeIsolinesDisplayStyleDisplayShadowType
            
            int nVal: 
            Input integer property value to set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        SetTrait(VisualStyleProperty, object, VisualStyleOperation) -> void
            
            VisualStyleProperty prop: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set.
            
            object val: 
            Input Autodesk.AutoCAD.GraphicsInterface.Variant property value to set.
            
            VisualStyleOperation op: 
            Input Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation to use when setting the property.
        """
        pass
    
    
    def SetTraitFlag(self):
        """
        SetTraitFlag -> void
            
            uint modopt(IsLong) flagVal: 
            Input bit flag enum unsigned long property to set.
            
            [MarshalAs(UnmanagedType.U1)] bool bEnable: 
            True to enable the flag; False to disable.
            
            flagProp: 
            Input bitfield enum Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty to set.
        """
        pass
    
    
    Description = None
    
    
    InternalUseOnly = None
    
    
    Type = None
    
    pass

class DataAdapterProvider(object):
    """
    
    DataAdapterProvider()
    """
    def GetDataAdapter(self):
        """
        GetDataAdapter -> DataAdapter
            
            string adapterId: 
            Input ID to check for
        """
        pass
    
    pass

class DataCell(object):
    """
    
    DataCell()
    """
    def Init(self):
        """
        Init -> void
        
        """
        pass
    
    
    def SetBool(self):
        """
        SetBool -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input System.Boolean object.
        """
        pass
    
    
    def SetDouble(self):
        """
        SetDouble -> void
            
            double value: 
            Input System.Double object.
        """
        pass
    
    
    def SetHardOwnershipId(self):
        """
        SetHardOwnershipId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object.
        """
        pass
    
    
    def SetHardPointerId(self):
        """
        SetHardPointerId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetInteger(self):
        """
        SetInteger -> void
            
            int value: 
            Input System.Int32 object.
        """
        pass
    
    
    def SetObjectId(self):
        """
        SetObjectId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetPoint(self):
        """
        SetPoint -> void
            
            Point3d value: 
            Input Autodesk.AutoCAD.Geometry.Point3d object
        """
        pass
    
    
    def SetSoftOwnershipId(self):
        """
        SetSoftOwnershipId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetSoftPointerId(self):
        """
        SetSoftPointerId -> void
            
            ObjectId value: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object
        """
        pass
    
    
    def SetString(self):
        """
        SetString -> void
            
            string value: 
            Input System.String object
        """
        pass
    
    
    def SetVector(self):
        """
        SetVector -> void
            
            Vector3d value: 
            Input Autodesk.AutoCAD.Geometry.Vector3d object.
        """
        pass
    
    
    CellType = None
    
    
    Value = None
    
    pass

class DataCellCollection(object):
    """
    
    DataCellCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            DataCell value: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell object
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
            
            DataCell value: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell object.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DataCell[] array: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell[] object
            
            int index: 
            Input
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
            
            DataCell value: 
            Input Autodesk.AutoCAD.DatabaseServices.DataCell object
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            DataCell value: 
            Input the data to be inserted
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            DataCell value: 
            Input value to be removed.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index to remove from
        """
        pass
    
    
    Count = None
    
    pass

class DataColumn(object):
    """
    
    DataColumn()()
    
    
    DataColumn(DataColumn)
        DataColumn column : Set the column to a specific type
    
    
    """
    def AppendCell(self):
        """
        AppendCell -> void
            
            DataCell cell: 
            New cell to add
        """
        pass
    
    
    def Assign(self):
        """
        Assign -> void
            
            DataColumn col: 
            New column to add
        """
        pass
    
    
    def GetCellAt(self):
        """
        GetCellAt -> DataCell
            
            int index: 
            Index of cell to retrieve
        """
        pass
    
    
    def GetIndexAtCell(self):
        """
        GetIndexAtCell -> Integer
            
            DataCell cell: 
            Input cell to be matched
        """
        pass
    
    
    def InsertCellAt(self):
        """
        InsertCellAt -> void
            
            int index: 
            Position at which to insert the cell
            
            DataCell cell: 
            Cell to insert
        """
        pass
    
    
    def RemoveCellAt(self):
        """
        RemoveCellAt -> void
            
            int index: 
            Index of cell to remove from the column
        """
        pass
    
    
    def SetCellAt(self):
        """
        SetCellAt -> void
            
            int index: 
            Index of the cell to be updated
            
            DataCell cell: 
            Cell to set
        """
        pass
    
    
    ColumnName = None
    
    
    ColumnType = None
    
    
    GrowLength = None
    
    
    NumCells = None
    
    
    PhysicalLength = None
    
    pass

class DataLink(object):
    """
    
    DataLink()
    """
    def GetUpdateStatus(self):
        """
        GetUpdateStatus -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            out Autodesk.AutoCAD.DatabaseServices.UpdateDirection pDir: 
            Stores the direction of the last update.
            
            out DateTime pTime: 
            Stores the time of the last update.
            
            [Out] string errMessage: 
            Stores the error message of the last update.
        """
        pass
    
    
    def GetTargets(self):
        """
        GetTargets -> ObjectIdCollection
        
        """
        pass
    
    
    def GetSourceFiles(self):
        """
        GetSourceFiles -> ArrayList
            
            Autodesk.AutoCAD.DatabaseServices.DataLinkGetSourceContext nContext: 
            Context in which this method is called
        """
        pass
    
    
    def RepathSourceFiles(self):
        """
        RepathSourceFiles -> void
            
            string sBasePath: 
            The base path
            
            Autodesk.AutoCAD.DatabaseServices.PathOption nOption: 
            The path option
        """
        pass
    
    
    def Update(self):
        """
        Update -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Update options
        """
        pass
    
    
    ConnectionString = None
    
    
    DataAdapterId = None
    
    
    DataLinkOption = None
    
    
    Description = None
    
    
    IsValid = None
    
    
    Name = None
    
    
    ToolTip = None
    
    
    UpdateOption = None
    
    pass

class DataLinkGetSourceContext():
    Etransmit = 1
    FileWatcher = 3
    OrignalPath = 0x100
    Other = 4
    Unknown = 0
    XrefManager = 2

class DataLinkManager(object):
    """
    
    """
    def AddDataLink(self):
        """
        AddDataLink -> ObjectId
            
            DataLink dataLink: 
            Data link object to add to the manager.
        """
        pass
    
    
    def GetDataLink(self):
        """
        GetDataLink() -> ObjectIdCollection
        
        GetDataLink(string) -> ObjectId
            
            string name: 
            Name of the data link to get.
        """
        pass
    
    
    def RemoveDataLink(self):
        """
        RemoveDataLink(ObjectId) -> void
            
            ObjectId idDataLink: 
            Reference to the data link to remove.
        RemoveDataLink(string) -> ObjectId
            
            string name: 
            Key to retrieve the data link.
        """
        pass
    
    
    def Update(self):
        """
        Update(Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection direction: 
            Update direction.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Update options.
        Update(ObjectIdCollection, Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            ObjectIdCollection dataIds: 
            Data link ids to update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection direction: 
            Update direction.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Update options.
        """
        pass
    
    
    DataLinkCount = None
    
    pass

class DataLinkOption():
    Anonymous = None
    PersistCache = None

class DataTable(object):
    """
    
    DataTable()
    """
    def AppendColumn(self):
        """
        AppendColumn -> void
            
            Autodesk.AutoCAD.DatabaseServices.CellType type: 
            Type of the column being added
            
            string columnName: 
            Name of the column
        """
        pass
    
    
    def AppendRow(self):
        """
        AppendRow -> void
            
            DataCellCollection row: 
            Row being added
            
            [MarshalAs(UnmanagedType.U1)] bool validate: 
            Validation flag
        """
        pass
    
    
    def Assign(self):
        """
        Assign -> void
            
            DataTable other: 
            New table to assign.
        """
        pass
    
    
    def GetCellAt(self):
        """
        GetCellAt -> DataCell
            
            int row: 
            Row index of cell to access
            
            int col: 
            Column index of cell to access
        """
        pass
    
    
    def GetColumnAt(self):
        """
        GetColumnAt -> DataColumn
            
            int index: 
            Index of column
        """
        pass
    
    
    def GetColumnIndexAtName(self):
        """
        GetColumnIndexAtName -> Integer
            
            string name: 
            Name of column
        """
        pass
    
    
    def GetColumnNameAt(self):
        """
        GetColumnNameAt -> string
            
            int index: 
            Column index
        """
        pass
    
    
    def GetColumnTypeAt(self):
        """
        GetColumnTypeAt -> Autodesk.AutoCAD.DatabaseServices.CellType
            
            int index: 
            Column index
        """
        pass
    
    
    def GetRowAt(self):
        """
        GetRowAt -> DataCellCollection
            
            int index: 
            Row index
        """
        pass
    
    
    def InsertColumnAt(self):
        """
        InsertColumnAt -> void
            
            int index: 
            Column index at which to insert the new column
            
            Autodesk.AutoCAD.DatabaseServices.CellType type: 
            Type of new column
            
            string columnName: 
            Name of new column
        """
        pass
    
    
    def InsertRowAt(self):
        """
        InsertRowAt -> void
            
            int index: 
            Row index of position at which to insert the row
            
            DataCellCollection row: 
            Row of data to insert
            
            [MarshalAs(UnmanagedType.U1)] bool validate: 
            Validation flag
        """
        pass
    
    
    def RemoveColumnAt(self):
        """
        RemoveColumnAt -> void
            
            int index: 
            Index of column to remove
        """
        pass
    
    
    def RemoveRowAt(self):
        """
        RemoveRowAt -> void
            
            int index: 
            Index of row to remove
        """
        pass
    
    
    def SetCellAt(self):
        """
        SetCellAt -> void
            
            int row: 
            Row index of the cell to be replaced
            
            int col: 
            Column index of the cell to be replaced
            
            DataCell cell: 
            New cell
        """
        pass
    
    
    def SetRowAt(self):
        """
        SetRowAt -> void
            
            int index: 
            Row index of the row to be replaced
            
            DataCellCollection row: 
            New row of data
            
            [MarshalAs(UnmanagedType.U1)] bool validate: 
            Validation flag
        """
        pass
    
    
    NumColsGrowSize = None
    
    
    NumColsPhysicalSize = None
    
    
    NumColumns = None
    
    
    NumRows = None
    
    
    NumRowsGrowSize = None
    
    
    NumRowsPhysicalSize = None
    
    
    TableName = None
    
    pass

class DataType():
    Buffer = 0x80
    Date = 8
    Double = 2
    General = 0x200
    Long = 1
    ObjectId = 0x40
    Point = 0x10
    Point3d = 0x20
    Resbuf = 0x100
    String = 4
    Unknown = 0

class Database(object):
    """
    
    Database()()
    
    
    Database([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool)
        [MarshalAs(UnmanagedType.U1)] bool buildDefaultDrawing : System.Boolean specifying whether or not to build an empty object
        [MarshalAs(UnmanagedType.U1)] bool noDocument : System.Boolean specifying whether or not to associate this database to the current document
    
    
    """
    def AbortDeepClone(self):
        """
        AbortDeepClone -> void
            
            IdMapping idMap: 
            Input used in the deepClone operation being aborted
        """
        pass
    
    
    def AddDBObject(self):
        """
        AddDBObject -> ObjectId
            
            [CallerMustClose] DBObject appendIt: 
            Input object to be added to the database
        """
        pass
    
    
    def ApplyPartialOpenFilters(self):
        """
        ApplyPartialOpenFilters -> void
            
            SpatialFilter spatialFilter: 
            Specifies the model space volume to be used for spatial filtering
            
            Autodesk.AutoCAD.DatabaseServices.Filters.LayerFilter layerFilter: 
            Specifies the layers to be used for filtering
        """
        pass
    
    
    def AttachXref(self):
        """
        AttachXref -> ObjectId
            
            string fileName: 
            Input xref file path name
            
            string blockName: 
            Input xref block name symbol to use
        """
        pass
    
    
    def AuditXData(self):
        """
        AuditXData -> void
            
            AuditInfo info: 
            Not implemented
        """
        pass
    
    
    def BindXrefs(self):
        """
        BindXrefs -> void
            
            ObjectIdCollection xrefIds: 
            Input collection of ObjectIds for the xref BlockTableRecords to bind.
            
            [MarshalAs(UnmanagedType.U1)] bool insertBind: 
            Input System.Boolean to indicate whether or not to convert xref symbols to insert-like bind names.
        """
        pass
    
    
    def ClassDxfName(self):
        """
        ClassDxfName -> string
            
            RXClass getMyDxfName: 
            Input Autodesk.AutoCAD.Runtime.RXClass object to get the name of.
        """
        pass
    
    
    def CloseInput(self):
        """
        CloseInput -> void
            
            [MarshalAs(UnmanagedType.U1)] bool closeFile: 
            Input System.Boolean indicating whether to close the drawing file
        """
        pass
    
    
    def CountEmptyObjects(self):
        """
        CountEmptyObjects -> Integer
            
            int flags: 
            The setting of the count mode. It is stored as a bitcode using the combination of the following enum values:ZeroLengthCurve - Count zero length curves (AcDbCurve derived objects such as LINE, POLYLINE, SPLINE, etc.)EmptyText - Count empty TEXT/MTEXT objects (which contain only spaces, tabs, enters and/or new lines)AllEmptyObj - Count all empty objects
        """
        pass
    
    
    def CountHardReferences(self):
        """
        CountHardReferences -> void
            
            ObjectIdCollection ids: 
            Input collection of objectId entities of objects to find the count of hard references to those objects
            
            int[] count: 
            Input array of the same size as ids that will be filled in with the counts for each corresponding element in ids
        """
        pass
    
    
    def DeepCloneObjects(self):
        """
        DeepCloneObjects -> void
            
            ObjectIdCollection identifiers: 
            Input collection of objects to be deep cloned
            
            ObjectId id: 
            Input Object ID of object to be the owner of the clones
            
            IdMapping mapping: 
            Returns collection of objects to be used for translating object ID relationships
            
            [MarshalAs(UnmanagedType.U1)] bool deferTranslation: 
            Input Boolean indicating whether or not ID translation should be done
        """
        pass
    
    
    def DetachXref(self):
        """
        DetachXref -> void
            
            ObjectId xrefId: 
            Input object ID of the xref block to detach
        """
        pass
    
    
    def DisablePartialOpen(self):
        """
        DisablePartialOpen -> void
        
        """
        pass
    
    
    def DisableUndoRecording(self):
        """
        DisableUndoRecording -> void
            
            [MarshalAs(UnmanagedType.U1)] bool disable: 
            Input Boolean indicating turn Undo on or off
        """
        pass
    
    
    def DxfIn(self):
        """
        DxfIn -> void
            
            string fileName: 
            Input full path of the DXF file to be read into database
            
            string logFilename: 
            Log file to record all warning/error messages from reading the DXF file
        """
        pass
    
    
    def DxfOut(self):
        """
        DxfOut(string, int, DwgVersion) -> void
            
            string fileName: 
            Input name or URL of the new DXF file to create (the .dxf extension is not added automatically)
            
            int precision: 
            Number of bits of accuracy, from 0 to 16
            
            DwgVersion version: 
            Sets the DWG version major and minor number
        DxfOut(string, int, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            string fileName: 
            Input name or URL of the new DXF file to create (the .dxf extension is not added automatically)
            
            int precision: 
            Number of bits of accuracy, from 0 to 16
            
            [MarshalAs(UnmanagedType.U1)] bool saveThumbnailImage: 
            Input Boolean indicating whether to save thumbnail
        """
        pass
    
    
    def EraseEmptyObjects(self):
        """
        EraseEmptyObjects -> Integer
            
            int flags: 
            The setting of the erase mode. It is stored as a bitcode using the combination of the following enum values:ZeroLengthCurve - Erase zero length curves (AcDbCurve derived objects such as LINE, POLYLINE, SPLINE, etc.)EmptyText - Erase empty TEXT/MTEXT objects (which contain only spaces, tabs, enters and/or new lines)AllEmptyObj - Erase all empty objects
        """
        pass
    
    
    def EvaluateFields(self):
        """
        EvaluateFields() -> FieldEvaluationResult
        
        EvaluateFields(FieldEvaluationContext) -> FieldEvaluationResult
            
            FieldEvaluationContext context: 
            Input bitwise value that determines the contexts in which fields should be evaluated. Refer to the DatabaseServices.FieldEvaluationContext enum for available context values.
        EvaluateFields(FieldEvaluationContext, string) -> FieldEvaluationResult
            
            FieldEvaluationContext context: 
            Input bitwise value that determines the contexts in which fields should be evaluated. Refer to the DatabaseServices.FieldEvaluationContext enum for available context values.
            
            string prop: 
            Input property name whose field is to be evaluated; if empty, all fields are evaluated
        """
        pass
    
    
    def ForceWblockDatabaseCopy(self):
        """
        ForceWblockDatabaseCopy -> void
        
        """
        pass
    
    
    def FromAcadDatabase(self):
        """
        FromAcadDatabase -> Database
        
        """
        pass
    
    
    def GetAllDatabases(self):
        """
        GetAllDatabases -> List<Database>
        
        """
        pass
    
    
    def GetDimensionStyleChildData(self):
        """
        GetDimensionStyleChildData -> DimStyleTableRecord
            
            RXClass classDescriptor: 
            Input object to check.
        """
        pass
    
    
    def GetDimensionStyleChildId(self):
        """
        GetDimensionStyleChildId -> ObjectId
            
            RXClass classDescriptor: 
            Input dimension class descriptor
            
            ObjectId parentStyle: 
            Input parent dimension style ID
        """
        pass
    
    
    def GetDimensionStyleParentId(self):
        """
        GetDimensionStyleParentId -> ObjectId
            
            ObjectId childStyle: 
            Input child dimension style ID
        """
        pass
    
    
    def GetDimRecentStyleList(self):
        """
        GetDimRecentStyleList -> ObjectIdCollection
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def GetHostDwgXrefGraph(self):
        """
        GetHostDwgXrefGraph -> XrefGraph
            
            [MarshalAs(UnmanagedType.U1)] bool includeGhosts: 
            If set to true, includes ghost nodes.
        """
        pass
    
    
    def GetNearestLineWeight(self):
        """
        GetNearestLineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int weight: 
            Input lineweight in hundredths of a millimeter
        """
        pass
    
    
    def GetObjectId(self):
        """
        GetObjectId -> ObjectId
            
            [MarshalAs(UnmanagedType.U1)] bool createIfNotFound: 
            Input Boolean indicating to create a objectId stub if input handle is not found
            
            Handle objHandle: 
            Input Handle object containing the handle being passed in
            
            int identifier: 
            Reserved for future use
        """
        pass
    
    
    def GetMetaObject(self):
        """
        GetMetaObject -> DynamicMetaObject
        
        """
        pass
    
    
    def GetSupportedDxfOutVersions(self):
        """
        GetSupportedDxfOutVersions -> DwgVersion()
        
        """
        pass
    
    
    def GetSupportedSaveVersions(self):
        """
        GetSupportedSaveVersions -> DwgVersion()
        
        """
        pass
    
    
    def GetViewports(self):
        """
        GetViewports -> ObjectIdCollection
            
            [MarshalAs(UnmanagedType.U1)] bool bGetPaperspaceVports: 
            Input flag indicating whether to return paperspace viewports associated with layouts
        """
        pass
    
    
    def GetVisualStyleList(self):
        """
        GetVisualStyleList -> StringCollection
        
        """
        pass
    
    
    def Insert(self):
        """
        Insert(Matrix3d, Database, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            Matrix3d transform: 
            Input transformation matrix applied to all objects being inserted
            
            Database dataBase: 
            Input database to insert from
            
            [MarshalAs(UnmanagedType.U1)] bool preserveSourceDatabase: 
            Input to determine whether the source database pDb will be left intact
        Insert(string, Database, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
            
            string blockName: 
            Input name to be used by the new block table record created by this function
            
            Database dataBase: 
            Input database from which to insert entities
            
            [MarshalAs(UnmanagedType.U1)] bool preserveSourceDatabase: 
            Input bool to determine whether the source database is left intact
        Insert(string, string, Database, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
            
            string sourceBlockName: 
            Input name of the blockTableRecord
            
            string destinationBlockName: 
            Input name to be used by the new block table record created by this function
            
            Database dataBase: 
            Input database from which to insert entities
            
            [MarshalAs(UnmanagedType.U1)] bool preserveSourceDatabase: 
            Input bool to determine whether the source database is left intact
        """
        pass
    
    
    def IsObjectNonPersistent(self):
        """
        IsObjectNonPersistent -> bool
            
            ObjectId id: 
            Input ID of the object to be interrogated
        """
        pass
    
    
    def IsValidLineWeight(self):
        """
        IsValidLineWeight -> bool
            
            int weight: 
            Input lineweight in hundredths of a millimeter
        """
        pass
    
    
    def LoadLineTypeFile(self):
        """
        LoadLineTypeFile -> void
            
            string lineTypeName: 
            Input linetype name string (wild cards may be used)
            
            string filename: 
            Input path/filename or URL of linetype file to load from (path is optional)
        """
        pass
    
    
    def LoadMlineStyleFile(self):
        """
        LoadMlineStyleFile -> void
            
            string mlineStyleName: 
            Input MlineStyle name string (no wild cards)
            
            string fileName: 
            Input path/filename or URL of file to load from (path is optional)
        """
        pass
    
    
    def MarkObjectNonPersistent(self):
        """
        MarkObjectNonPersistent -> void
            
            ObjectId id: 
            Input ID of the object to be modified
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input true to make the object non-persistent, or false to make it persistent
        """
        pass
    
    
    def OverlayXref(self):
        """
        OverlayXref -> ObjectId
            
            string fileName: 
            Input xref file path name
            
            string blockName: 
            Input xref block name symbol to use
        """
        pass
    
    
    def Purge(self):
        """
        Purge(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input collection of object ID entities of objects
        Purge(ObjectIdGraph) -> void
            
            ObjectIdGraph idGraph: 
            Input graph of objects in the database. The graph will be returned containing only those objects that may safely be removed from the database.
        """
        pass
    
    
    def ReadDwgFile(self):
        """
        ReadDwgFile(IntPtr, [MarshalAs(UnmanagedType.U1)] bool, string) -> void
            
            IntPtr drawingFile: 
            Input pointer to DWG file to read
            
            [MarshalAs(UnmanagedType.U1)] bool allowCPConversion: 
            Input Boolean indicating whether to allow codepage conversion
            
            string password: 
            Input string containing a DWG password
        ReadDwgFile(string, FileOpenMode, [MarshalAs(UnmanagedType.U1)] bool, string) -> void
            
            string fileName: 
            Input name or URL of file to read
            
            FileOpenMode mode: 
            Input open mode
            
            [MarshalAs(UnmanagedType.U1)] bool allowCPConversion: 
            Input Boolean indicating whether to allow codepage conversion
            
            string password: 
            Input string containing a DWG password
        ReadDwgFile(string, FileShare, [MarshalAs(UnmanagedType.U1)] bool, string) -> void
            
            string fileName: 
            Input name or URL of file to read
            
            FileShare fileSharing: 
            Input share mode
            
            [MarshalAs(UnmanagedType.U1)] bool allowCPConversion: 
            Input Boolean indicating whether to allow codepage conversion
            
            string password: 
            Input string containing a DWG password
            _SH_DENYWR: 
            Opens an existing file as read-onlyDenies write-access to the file by other sessions
            _SH_DENYRW: 
            Opens a file for reading and writingDenies read-write access to the file by other sessions
            _SH_DENYNO: 
            Opens an existing file as read-onlyPermits read-write access to the file by other sessions
        """
        pass
    
    
    def ReclaimMemoryFromErasedObjects(self):
        """
        ReclaimMemoryFromErasedObjects -> void
            
            ObjectIdCollection ids: 
            A collection of object ids whose memory is to be reclaimed by deleting their objects. All object ids in the collection must correspond to erased objects, which must be entirely closed.
        """
        pass
    
    
    def ReloadXrefs(self):
        """
        ReloadXrefs -> void
            
            ObjectIdCollection xrefIds: 
            Input collection of ObjectIds for the xref BlockTableRecords to unload
        """
        pass
    
    
    def ResolveXrefs(self):
        """
        ResolveXrefs -> void
            
            [MarshalAs(UnmanagedType.U1)] bool useThreadEngine: 
            Input Boolean indicating whether to use the thread engine for xref resolution
            
            [MarshalAs(UnmanagedType.U1)] bool doNewOnly: 
            Input Boolean indicating whether to process only newly added xrefs
        """
        pass
    
    
    def RestoreForwardingXrefSymbols(self):
        """
        RestoreForwardingXrefSymbols -> void
        
        """
        pass
    
    
    def RestoreOriginalXrefSymbols(self):
        """
        RestoreOriginalXrefSymbols -> void
        
        """
        pass
    
    
    def ResetTimes(self):
        """
        ResetTimes -> void
        
        """
        pass
    
    
    def Save(self):
        """
        Save -> void
        
        """
        pass
    
    
    def SaveAs(self):
        """
        SaveAs(string, Autodesk.AutoCAD.DatabaseServices.SecurityParameters) -> void
            
            string fileName: 
            Input file name or URL to write database out to
            
            Autodesk.AutoCAD.DatabaseServices.SecurityParameters security: 
            Input a SecurityParameters structure
        SaveAs(string, DwgVersion) -> void
            
            string fileName: 
            Input file name or URL to write database out to
            
            DwgVersion version: 
            Input dwg version to which to save the file
        SaveAs(string, [MarshalAs(UnmanagedType.U1)] bool, DwgVersion, Autodesk.AutoCAD.DatabaseServices.SecurityParameters) -> void
            
            string fileName: 
            Input file name or URL to write database out to
            
            [MarshalAs(UnmanagedType.U1)] bool bBakAndRename: 
            Input bool indicating whether or not to create a .bak file and change document name in AutoCAD
            
            DwgVersion version: 
            Input dwg version to which to save the file
            
            Autodesk.AutoCAD.DatabaseServices.SecurityParameters security: 
            Input a SecurityParameters structure
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input pointer to DimStyleTableRecord from which to copy dimension variable information
        """
        pass
    
    
    def SetTimeZoneAsUtcOffset(self):
        """
        SetTimeZoneAsUtcOffset -> Autodesk.AutoCAD.DatabaseServices.TimeZone
            
            double offset: 
            Input the offset, in hours
            
            Exceptions: 
            Description
            
            validInput: 
            Thrown if a valid time zone is not found
        """
        pass
    
    
    def SetWorldPaperspaceUcsBaseOrigin(self):
        """
        SetWorldPaperspaceUcsBaseOrigin -> void
            
            Point3d origin: 
            Input new origin point in WCS coordinates
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input view for which base point is desired
        """
        pass
    
    
    def SetWorldUcsBaseOrigin(self):
        """
        SetWorldUcsBaseOrigin -> void
            
            Point3d origin: 
            Input new origin point in WCS coordinates
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input view for which base point is desired
        """
        pass
    
    
    def TimeZoneDescription(self):
        """
        TimeZoneDescription -> string
            
            Autodesk.AutoCAD.DatabaseServices.TimeZone tz: 
            Input a value from the TimeZone enum
        """
        pass
    
    
    def TimeZoneOffset(self):
        """
        TimeZoneOffset -> double
            
            Autodesk.AutoCAD.DatabaseServices.TimeZone tz: 
            Input one of the time zones contained in the TimeZone enum
            
            Exceptions: 
            Description
            
            validInput: 
            Thrown if an invalid TimeZone is passed in
        """
        pass
    
    
    def UnloadXrefs(self):
        """
        UnloadXrefs -> void
            
            ObjectIdCollection xrefIds: 
            Input collection of ObjectIds for the xref BlockTableRecords to unload
        """
        pass
    
    
    def UpdateExt(self):
        """
        UpdateExt -> void
            
            [MarshalAs(UnmanagedType.U1)] bool doBestFit: 
            Determines whether to generate the tightest bounding box
        """
        pass
    
    
    def Wblock(self):
        """
        Wblock() -> void
        
        """
        pass
    
    
    def XBindXrefs(self):
        """
        XBindXrefs -> void
            
            ObjectIdCollection xrefSymbolIds: 
            Input collection of ObjectIds of SymbolTableRecord objects to be bound.
            
            [MarshalAs(UnmanagedType.U1)] bool insertBind: 
            Input bool to indicate whether or not to convert xref symbols to insert-like bind names.
        """
        pass
    
    
    def WblockCloneObjects(self):
        """
        WblockCloneObjects -> void
            
            ObjectIdCollection identifiers: 
            Input collection of objects to be deep cloned
            
            ObjectId id: 
            Input object ID of object to be the owner of the clones
            
            IdMapping mapping: 
            Collection of IdPair objects to be used for translating object ID relationships
            
            Autodesk.AutoCAD.DatabaseServices.DuplicateRecordCloning cloning: 
            Input action for duplicate records
            
            [MarshalAs(UnmanagedType.U1)] bool deferTranslation: 
            Input Boolean indicating whether or not ID translation should be done
        """
        pass
    
    
    def WorldPaperspaceUcsBaseOrigin(self):
        """
        WorldPaperspaceUcsBaseOrigin -> Point3d
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input desired view
        """
        pass
    
    
    def WorldUcsBaseOrigin(self):
        """
        WorldUcsBaseOrigin -> Point3d
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView orthoView: 
            Input view for which base point is desired
        """
        pass
    
    
    AcadDatabase = None
    
    
    AllowExtendedNames = None
    
    
    Angbase = None
    
    
    Angdir = None
    
    
    AnnoAllVisible = None
    
    
    AnnotativeDwg = None
    
    
    ApproxNumObjects = None
    
    
    Attmode = None
    
    
    Aunits = None
    
    
    Auprec = None
    
    
    BlockTableId = None
    
    
    ByBlockLinetype = None
    
    
    ByLayerLinetype = None
    
    
    CameraDisplay = None
    
    
    CameraHeight = None
    
    
    Cannoscale = None
    
    
    Cecolor = None
    
    
    Celtscale = None
    
    
    Celtype = None
    
    
    Celweight = None
    
    
    Cetransparency = None
    
    
    Chamfera = None
    
    
    Chamferb = None
    
    
    Chamferc = None
    
    
    Chamferd = None
    
    
    Clayer = None
    
    
    Cmaterial = None
    
    
    Cmljust = None
    
    
    Cmlscale = None
    
    
    CmlstyleID = None
    
    
    ColorDictionaryId = None
    
    
    ContinuousLinetype = None
    
    
    Cshadow = None
    
    
    CurrentSpaceId = None
    
    
    CurrentViewportTableRecordId = None
    
    
    DataLinkDictionaryId = None
    
    
    DataLinkManager = None
    
    
    DetailViewStyle = None
    
    
    DetailViewStyleDictionaryId = None
    
    
    DgnFrame = None
    
    
    Dimadec = None
    
    
    Dimalt = None
    
    
    Dimaltd = None
    
    
    Dimaltf = None
    
    
    Dimaltrnd = None
    
    
    Dimalttd = None
    
    
    Dimalttz = None
    
    
    Dimaltu = None
    
    
    Dimaltz = None
    
    
    Dimapost = None
    
    
    Dimarcsym = None
    
    
    Dimaso = None
    
    
    DimAssoc = None
    
    
    Dimasz = None
    
    
    Dimatfit = None
    
    
    Dimaunit = None
    
    
    Dimazin = None
    
    
    Dimblk = None
    
    
    Dimblk1 = None
    
    
    Dimblk2 = None
    
    
    Dimcen = None
    
    
    Dimclrd = None
    
    
    Dimclre = None
    
    
    Dimclrt = None
    
    
    Dimdec = None
    
    
    Dimdle = None
    
    
    Dimdli = None
    
    
    Dimdsep = None
    
    
    Dimexe = None
    
    
    Dimexo = None
    
    
    Dimfrac = None
    
    
    Dimfxlen = None
    
    
    DimfxlenOn = None
    
    
    Dimgap = None
    
    
    Dimjogang = None
    
    
    Dimjust = None
    
    
    Dimldrblk = None
    
    
    Dimlfac = None
    
    
    Dimlim = None
    
    
    Dimltex1 = None
    
    
    Dimltex2 = None
    
    
    Dimltype = None
    
    
    Dimlunit = None
    
    
    Dimlwd = None
    
    
    Dimlwe = None
    
    
    Dimpost = None
    
    
    Dimrnd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimsd1 = None
    
    
    Dimsd2 = None
    
    
    Dimse1 = None
    
    
    Dimse2 = None
    
    
    Dimsho = None
    
    
    Dimsoxd = None
    
    
    Dimstyle = None
    
    
    DimStyleTableId = None
    
    
    Dimtad = None
    
    
    Dimtdec = None
    
    
    Dimtfac = None
    
    
    Dimtfill = None
    
    
    Dimtfillclr = None
    
    
    Dimtih = None
    
    
    Dimtix = None
    
    
    Dimtm = None
    
    
    Dimtmove = None
    
    
    Dimtofl = None
    
    
    Dimtoh = None
    
    
    Dimtol = None
    
    
    Dimtolj = None
    
    
    Dimtp = None
    
    
    Dimtsz = None
    
    
    Dimtvp = None
    
    
    Dimtxsty = None
    
    
    Dimtxt = None
    
    
    Dimtzin = None
    
    
    Dimupt = None
    
    
    Dimzin = None
    
    
    DispSilh = None
    
    
    dragvs = None
    
    
    DrawOrderCtl = None
    
    
    DwfFrame = None
    
    
    DwgFileWasSavedByAutodeskSoftware = None
    
    
    DxEval = None
    
    
    Elevation = None
    
    
    EndCaps = None
    
    
    Extmax = None
    
    
    Extmin = None
    
    
    Facetres = None
    
    
    Filename = None
    
    
    Filletrad = None
    
    
    Fillmode = None
    
    
    FingerprintGuid = None
    
    
    GeoDataObject = None
    
    
    GroupDictionaryId = None
    
    
    HaloGap = None
    
    
    Handseed = None
    
    
    HideText = None
    
    
    HomeView = None
    
    
    HpInherit = None
    
    
    HpOrigin = None
    
    
    HyperlinkBase = None
    
    
    Indexctl = None
    
    
    Insbase = None
    
    
    Insunits = None
    
    
    Interferecolor = None
    
    
    Interfereobjvs = None
    
    
    Interferevpvs = None
    
    
    IntersectColor = None
    
    
    IntersectDisplay = None
    
    
    IsBeingDestroyed = None
    
    
    IsEmr = None
    
    
    Isolines = None
    
    
    IsPartiallyOpened = None
    
    
    JoinStyle = None
    
    
    LastSavedAsMaintenanceVersion = None
    
    
    LastSavedAsVersion = None
    
    
    Latitude = None
    
    
    LayerEval = None
    
    
    LayerFilters = None
    
    
    LayerNotify = None
    
    
    LayerStateManager = None
    
    
    LayerTableId = None
    
    
    LayerZero = None
    
    
    LayoutDictionaryId = None
    
    
    LensLength = None
    
    
    LightGlyphDisplay = None
    
    
    LightingUnits = None
    
    
    LightsInBlocks = None
    
    
    Limcheck = None
    
    
    Limmax = None
    
    
    Limmin = None
    
    
    LinetypeTableId = None
    
    
    LineWeightDisplay = None
    
    
    LoftAng1 = None
    
    
    LoftAng2 = None
    
    
    LoftMag1 = None
    
    
    LoftMag2 = None
    
    
    LoftNormals = None
    
    
    LoftParam = None
    
    
    Longitude = None
    
    
    Ltscale = None
    
    
    Lunits = None
    
    
    Luprec = None
    
    
    MaintenanceReleaseVersion = None
    
    
    MaterialDictionaryId = None
    
    
    Maxactvp = None
    
    
    Measurement = None
    
    
    Menu = None
    
    
    Mirrtext = None
    
    
    MLeaderscale = None
    
    
    MLeaderstyle = None
    
    
    MLeaderStyleDictionaryId = None
    
    
    MLStyleDictionaryId = None
    
    
    MsLtScale = None
    
    
    MsOleScale = None
    
    
    NamedObjectsDictionaryId = None
    
    
    NeedsRecovery = None
    
    
    NorthDirection = None
    
    
    NumberOfSaves = None
    
    
    ObjectContextManager = None
    
    
    ObscuredColor = None
    
    
    ObscuredLineType = None
    
    
    OleStartUp = None
    
    
    OriginalFileMaintenanceVersion = None
    
    
    OriginalFileName = None
    
    
    OriginalFileSavedByMaintenanceVersion = None
    
    
    OriginalFileSavedByVersion = None
    
    
    OriginalFileVersion = None
    
    
    Orthomode = None
    
    
    PaperSpaceVportId = None
    
    
    PdfFrame = None
    
    
    Pdmode = None
    
    
    Pdsize = None
    
    
    Pelevation = None
    
    
    Pextmax = None
    
    
    Pextmin = None
    
    
    Pinsbase = None
    
    
    Plimcheck = None
    
    
    Plimmax = None
    
    
    Plimmin = None
    
    
    PlineEllipse = None
    
    
    Plinegen = None
    
    
    Plinewid = None
    
    
    PlotSettingsDictionaryId = None
    
    
    PlotStyleMode = None
    
    
    PlotStyleNameDictionaryId = None
    
    
    PlotStyleNameId = None
    
    
    ProjectName = None
    
    
    Psltscale = None
    
    
    PsolHeight = None
    
    
    PsolWidth = None
    
    
    Pucs = None
    
    
    PucsBase = None
    
    
    Pucsname = None
    
    
    Pucsorg = None
    
    
    PucsOrthographic = None
    
    
    Pucsxdir = None
    
    
    Pucsydir = None
    
    
    Qtextmode = None
    
    
    RegAppTableId = None
    
    
    Regenmode = None
    
    
    RetainOriginalThumbnailBitmap = None
    
    
    Saveproxygraphics = None
    
    
    SectionManagerId = None
    
    
    SectionViewStyle = None
    
    
    SectionViewStyleDictionaryId = None
    
    
    SecurityParameters = None
    
    
    Shadedge = None
    
    
    Shadedif = None
    
    
    ShadowPlaneLocation = None
    
    
    ShowHist = None
    
    
    Sketchinc = None
    
    
    Skpoly = None
    
    
    SolidHist = None
    
    
    SortEnts = None
    
    
    Splframe = None
    
    
    Splinesegs = None
    
    
    Splinetype = None
    
    
    StepSize = None
    
    
    StepsPerSec = None
    
    
    StyleSheet = None
    
    
    SummaryInfo = None
    
    
    Surftab1 = None
    
    
    Surftab2 = None
    
    
    Surftype = None
    
    
    Surfu = None
    
    
    Surfv = None
    
    
    Tablestyle = None
    
    
    TableStyleDictionaryId = None
    
    
    Tdcreate = None
    
    
    Tdindwg = None
    
    
    Tducreate = None
    
    
    Tdupdate = None
    
    
    Tdusrtimer = None
    
    
    Tduupdate = None
    
    
    Textsize = None
    
    
    Textstyle = None
    
    
    TextStyleTableId = None
    
    
    Thickness = None
    
    
    ThumbnailBitmap = None
    
    
    TileMode = None
    
    
    TileModeLightSynch = None
    
    
    TimeZone = None
    
    
    Tracewid = None
    
    
    TransactionManager = None
    
    
    Treedepth = None
    
    
    TStackAlign = None
    
    
    TstackSize = None
    
    
    Ucs = None
    
    
    UcsBase = None
    
    
    Ucsname = None
    
    
    Ucsorg = None
    
    
    UcsOrthographic = None
    
    
    UcsTableId = None
    
    
    Ucsxdir = None
    
    
    Ucsydir = None
    
    
    UndoRecording = None
    
    
    Unitmode = None
    
    
    UpdateThumbnail = None
    
    
    Useri1 = None
    
    
    Useri2 = None
    
    
    Useri3 = None
    
    
    Useri4 = None
    
    
    Useri5 = None
    
    
    Userr1 = None
    
    
    Userr2 = None
    
    
    Userr3 = None
    
    
    Userr4 = None
    
    
    Userr5 = None
    
    
    Usrtimer = None
    
    
    VersionGuid = None
    
    
    ViewportScaleDefault = None
    
    
    ViewportTableId = None
    
    
    ViewTableId = None
    
    
    Visretain = None
    
    
    VisualStyleDictionaryId = None
    
    
    Worldview = None
    
    
    XclipFrame = None
    
    
    XrefBlockId = None
    
    
    XrefEditEnabled = None
    
    pass

class DatabaseIOEventArgs(object):
    """
    
    """
    FileName = None
    
    pass

class DatabaseSummaryInfo(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input System.Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object
        """
        pass
    
    
    Author = None
    
    
    Comments = None
    
    
    CustomProperties = None
    
    
    HyperlinkBase = None
    
    
    Keywords = None
    
    
    LastSavedBy = None
    
    
    RevisionNumber = None
    
    
    Subject = None
    
    
    Title = None
    
    pass

class DatabaseSummaryInfoBuilder(object):
    """
    
    DatabaseSummaryInfoBuilder()()
    
    
    DatabaseSummaryInfoBuilder(DatabaseSummaryInfo)
        DatabaseSummaryInfo value : Input Autodesk.AutoCAD.DatabaseServices.DatabaseSummaryInfo object.
    
    
    """
    def ToDatabaseSummaryInfo(self):
        """
        ToDatabaseSummaryInfo -> DatabaseSummaryInfo
        
        """
        pass
    
    
    Author = None
    
    
    Comments = None
    
    
    CustomProperties = None
    
    
    CustomPropertyTable = None
    
    
    HyperlinkBase = None
    
    
    Keywords = None
    
    
    LastSavedBy = None
    
    
    RevisionNumber = None
    
    
    Subject = None
    
    
    Title = None
    
    pass

class DbDictionaryEnumerator(object):
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
    
    
    Entry = None
    
    
    Key = None
    
    
    Value = None
    
    pass

class DbHomeView(object):
    """
    
    DbHomeView()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def ToggleDefaultSettings(self):
        """
        ToggleDefaultSettings -> void
        
        """
        pass
    
    
    Center = None
    
    
    Eye = None
    
    
    Height = None
    
    
    Perspective = None
    
    
    Up = None
    
    
    Width = None
    
    pass

class DecomposeForSaveReplacementRecord(object):
    """
    
    DecomposeForSaveReplacementRecord
        DBObject replacement : Input Autodesk.AutoCAD.DatabaseServices.DBObject object
        [MarshalAs(UnmanagedType.U1)] bool exchangeXData : Input System.Boolean object
    """
    ExchangeXData = None
    
    
    ReplacementId = None
    
    
    ReplacementObject = None
    
    pass

class DeepCloneType():
    Block = 2
    Copy = 0
    Explode = 1
    Insert = 6
    InsertCopy = 10
    Objects = 8
    SymbolTableMerge = 4
    Wblock = 7
    WblockObjects = 11
    XrefBind = 3
    XrefInsert = 9

class DefaultLightingType():
    OneDistantLight = None
    TwoDistantLights = None

class DetailSymbol(object):
    """
    
    DetailSymbol()
    """
    def IsOverriddenProperty(self):
        """
        IsOverriddenProperty -> bool
            
            flag: 
            Input: the NAMESPACE_ACDB::DetailViewModelEdge value to test if it is overridden
        """
        pass
    
    
    BoundarySize = None
    
    
    BoundaryType = None
    
    
    DetailViewScale = None
    
    
    Direction = None
    
    
    DisplayIdentifier = None
    
    
    Identifier = None
    
    
    IdentifierPosition = None
    
    
    ModelEdgeDirection = None
    
    
    ModelEdgeOrigin = None
    
    
    ModelEdgeType = None
    
    
    Origin = None
    
    
    OwningViewScale = None
    
    
    Scale = None
    
    
    SymbolStyleId = None
    
    pass

class DetailSymbolBoundaryType():
    CircularBoundary = None
    RectangularBoundary = None
    CustomBoundary = None

class DetailSymbolOverriddenProperty():
    IdentifierPosition = 2
    ModelEdge = 1

class DetailViewIdentifierPlacement():
    OutsideBoundary = None
    OutsideBoundaryWithLeader = None
    OnBoundary = None
    OnBoundaryWithLeader = None

class DetailViewModelEdge():
    Smooth = None
    SmoothWithBorder = None
    SmoothWithConnectionLine = None
    Jagged = None

class DetailViewStyle(object):
    """
    
    DetailViewStyle()
    """
    def DefaultViewName(self):
        """
        DefaultViewName -> string
            
            int index: 
            The index of the default name.
        """
        pass
    
    
    def GetViewLabelPattern(self):
        """
        GetViewLabelPattern -> string
            
            Field field: 
            Input: a field object to be updated with the view label pattern master field.
        """
        pass
    
    
    def PostViewStyleToDb(self):
        """
        PostViewStyleToDb -> ObjectId
            
            Database dataBasePointer: 
            Input: database to be updated.
            
            string styleName: 
            Input: name to be used for this view style.
        """
        pass
    
    
    def SetDatabaseDefaults(self):
        """
        SetDatabaseDefaults -> void
            
            Database dataBasePointer: 
            Input: database to be used
        """
        pass
    
    
    def SetViewLabelPattern(self):
        """
        SetViewLabelPattern -> void
            
            string pattern: 
            Input: the pattern string for the view label.
            
            Field field: 
            Input: optional pointer to a Field
        """
        pass
    
    
    def ValidateViewName(self):
        """
        ValidateViewName -> bool
            
            string name: 
            Input: section name to validate.
        """
        pass
    
    
    ArrowSymbolColor = None
    
    
    ArrowSymbolId = None
    
    
    ArrowSymbolSize = None
    
    
    BorderLineColor = None
    
    
    BorderLineTypeId = None
    
    
    BorderLineWeight = None
    
    
    BoundaryLineColor = None
    
    
    BoundaryLineTypeId = None
    
    
    BoundaryLineWeight = None
    
    
    ConnectionLineColor = None
    
    
    ConnectionLineTypeId = None
    
    
    ConnectionLineWeight = None
    
    
    Description = None
    
    
    IdentifierColor = None
    
    
    IdentifierHeight = None
    
    
    IdentifierOffset = None
    
    
    IdentifierPlacement = None
    
    
    IdentifierStyleId = None
    
    
    IsModifiedForRecompute = None
    
    
    ModelEdge = None
    
    
    Name = None
    
    
    ShowArrowheads = None
    
    
    ShowViewLabel = None
    
    
    ViewLabelAlignment = None
    
    
    ViewLabelAttachment = None
    
    
    ViewLabelOffset = None
    
    
    ViewLabelPattern = None
    
    
    ViewLabelTextColor = None
    
    
    ViewLabelTextHeight = None
    
    
    ViewLabelTextStyleId = None
    
    pass

class DgnDefinition(object):
    """
    
    DgnDefinition()
    """
    SetShowRasterRef = None
    
    
    ShowRasterRef = None
    
    
    UseMasterUnits = None
    
    
    XrefDepth = None
    
    pass

class DgnReference(object):
    """
    
    DgnReference()
    """

    pass

class DgnUnderlayItem(object):
    """
    
    """
    SetShowRasterRef = None
    
    
    ShowRasterRef = None
    
    
    UseMasterUnits = None
    
    pass

class DiametricDimension(object):
    """
    
    DiametricDimension()()
    
    
    """
    ChordPoint = None
    
    
    FarChordPoint = None
    
    
    LeaderLength = None
    
    pass

class DictionaryWithDefaultDictionary(object):
    """
    
    DictionaryWithDefaultDictionary()
    """
    DefaultId = None
    
    
    ObjectBirthVersion = None
    
    pass

class DimArrowFlag():
    FirstArrow = None
    SecondArrow = None

class DimStyleTable(object):
    """
    
    """

    pass

class DimStyleTableRecord(object):
    """
    
    DimStyleTableRecord()
    """
    def GetArrowId(self):
        """
        GetArrowId -> ObjectId
            
            DimArrowFlag whichArrow: 
            Input a dimension arrowhead
        """
        pass
    
    
    Dimadec = None
    
    
    Dimalt = None
    
    
    Dimaltd = None
    
    
    Dimaltf = None
    
    
    Dimaltrnd = None
    
    
    Dimalttd = None
    
    
    Dimalttz = None
    
    
    Dimaltu = None
    
    
    Dimaltz = None
    
    
    Dimapost = None
    
    
    Dimarcsym = None
    
    
    Dimasz = None
    
    
    Dimatfit = None
    
    
    Dimaunit = None
    
    
    Dimazin = None
    
    
    Dimblk = None
    
    
    Dimblk1 = None
    
    
    Dimblk2 = None
    
    
    Dimcen = None
    
    
    Dimclrd = None
    
    
    Dimclre = None
    
    
    Dimclrt = None
    
    
    Dimdec = None
    
    
    Dimdle = None
    
    
    Dimdli = None
    
    
    Dimdsep = None
    
    
    Dimexe = None
    
    
    Dimexo = None
    
    
    Dimfrac = None
    
    
    Dimfxlen = None
    
    
    DimfxlenOn = None
    
    
    Dimgap = None
    
    
    Dimjogang = None
    
    
    Dimjust = None
    
    
    Dimldrblk = None
    
    
    Dimlfac = None
    
    
    Dimlim = None
    
    
    Dimltex1 = None
    
    
    Dimltex2 = None
    
    
    Dimltype = None
    
    
    Dimlunit = None
    
    
    Dimlwd = None
    
    
    Dimlwe = None
    
    
    Dimpost = None
    
    
    Dimrnd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimsd1 = None
    
    
    Dimsd2 = None
    
    
    Dimse1 = None
    
    
    Dimse2 = None
    
    
    Dimsoxd = None
    
    
    Dimtad = None
    
    
    Dimtdec = None
    
    
    Dimtfac = None
    
    
    Dimtfill = None
    
    
    Dimtfillclr = None
    
    
    Dimtih = None
    
    
    Dimtix = None
    
    
    Dimtm = None
    
    
    Dimtmove = None
    
    
    Dimtofl = None
    
    
    Dimtoh = None
    
    
    Dimtol = None
    
    
    Dimtolj = None
    
    
    Dimtp = None
    
    
    Dimtsz = None
    
    
    Dimtvp = None
    
    
    Dimtxsty = None
    
    
    Dimtxt = None
    
    
    Dimtzin = None
    
    
    Dimupt = None
    
    
    Dimzin = None
    
    
    IsModifiedForRecompute = None
    
    pass

class Dimension(object):
    """
    
    """
    def FieldFromMText(self):
        """
        FieldFromMText -> void
            
            MText dimMText: 
            The MText object from which the text field is copied
        """
        pass
    
    
    def FieldToMText(self):
        """
        FieldToMText -> void
            
            MText dimMText: MText object to which the new field will be attached
        """
        pass
    
    
    def FormatMeasurement(self):
        """
        FormatMeasurement -> string
            
            double measurement: 
            Input measurement value.
            
            string dimensionText: 
            Input alternate value.
        """
        pass
    
    
    def GenerateLayout(self):
        """
        GenerateLayout -> void
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def RecomputeDimensionBlock(self):
        """
        RecomputeDimensionBlock -> void
            
            [MarshalAs(UnmanagedType.U1)] bool forceUpdate: 
            Boolean indicating whether or not to force an update on screen
        """
        pass
    
    
    def RemoveTextField(self):
        """
        RemoveTextField -> void
        
        """
        pass
    
    
    def ResetTextDefinedSize(self):
        """
        ResetTextDefinedSize -> void
        
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input object ID of DimStyleTableRecord from which to copy dimension variable information
        """
        pass
    
    
    AlternatePrefix = None
    
    
    AlternateSuffix = None
    
    
    AltSuppressLeadingZeros = None
    
    
    AltSuppressTrailingZeros = None
    
    
    AltSuppressZeroFeet = None
    
    
    AltSuppressZeroInches = None
    
    
    AltToleranceSuppressLeadingZeros = None
    
    
    AltToleranceSuppressTrailingZeros = None
    
    
    AltToleranceSuppressZeroFeet = None
    
    
    AltToleranceSuppressZeroInches = None
    
    
    CenterMarkSize = None
    
    
    CenterMarkType = None
    
    
    Dimadec = None
    
    
    Dimalt = None
    
    
    Dimaltd = None
    
    
    Dimaltf = None
    
    
    Dimaltrnd = None
    
    
    Dimalttd = None
    
    
    Dimalttz = None
    
    
    Dimaltu = None
    
    
    Dimaltz = None
    
    
    Dimapost = None
    
    
    Dimarcsym = None
    
    
    Dimasz = None
    
    
    Dimatfit = None
    
    
    Dimaunit = None
    
    
    Dimazin = None
    
    
    Dimblk = None
    
    
    Dimblk1 = None
    
    
    Dimblk2 = None
    
    
    DimBlockId = None
    
    
    DimBlockPosition = None
    
    
    Dimcen = None
    
    
    Dimclrd = None
    
    
    Dimclre = None
    
    
    Dimclrt = None
    
    
    Dimdec = None
    
    
    Dimdle = None
    
    
    Dimdli = None
    
    
    Dimdsep = None
    
    
    DimensionStyle = None
    
    
    DimensionStyleName = None
    
    
    DimensionText = None
    
    
    Dimexe = None
    
    
    Dimexo = None
    
    
    Dimfrac = None
    
    
    Dimfxlen = None
    
    
    DimfxlenOn = None
    
    
    Dimgap = None
    
    
    Dimjogang = None
    
    
    Dimjust = None
    
    
    Dimldrblk = None
    
    
    Dimlfac = None
    
    
    Dimlim = None
    
    
    Dimltex1 = None
    
    
    Dimltex2 = None
    
    
    Dimltype = None
    
    
    Dimlunit = None
    
    
    Dimlwd = None
    
    
    Dimlwe = None
    
    
    Dimpost = None
    
    
    Dimrnd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimsd1 = None
    
    
    Dimsd2 = None
    
    
    Dimse1 = None
    
    
    Dimse2 = None
    
    
    Dimsoxd = None
    
    
    Dimtad = None
    
    
    Dimtdec = None
    
    
    Dimtfac = None
    
    
    Dimtfill = None
    
    
    Dimtfillclr = None
    
    
    Dimtih = None
    
    
    Dimtix = None
    
    
    Dimtm = None
    
    
    Dimtmove = None
    
    
    Dimtofl = None
    
    
    Dimtoh = None
    
    
    Dimtol = None
    
    
    Dimtolj = None
    
    
    Dimtp = None
    
    
    Dimtsz = None
    
    
    Dimtvp = None
    
    
    Dimtxt = None
    
    
    Dimtzin = None
    
    
    Dimupt = None
    
    
    Dimzin = None
    
    
    DynamicDimension = None
    
    
    Elevation = None
    
    
    HorizontalRotation = None
    
    
    Measurement = None
    
    
    Normal = None
    
    
    Prefix = None
    
    
    Suffix = None
    
    
    SuppressAngularLeadingZeros = None
    
    
    SuppressAngularTrailingZeros = None
    
    
    SuppressLeadingZeros = None
    
    
    SuppressTrailingZeros = None
    
    
    SuppressZeroFeet = None
    
    
    SuppressZeroInches = None
    
    
    TextAttachment = None
    
    
    TextDefinedSize = None
    
    
    TextLineSpacingFactor = None
    
    
    TextLineSpacingStyle = None
    
    
    TextPosition = None
    
    
    TextRotation = None
    
    
    ToleranceSuppressLeadingZeros = None
    
    
    ToleranceSuppressTrailingZeros = None
    
    
    ToleranceSuppressZeroFeet = None
    
    
    ToleranceSuppressZeroInches = None
    
    
    UsingDefaultTextPosition = None
    
    pass

class DimensionCenterMarkType():
    Mark = None
    Line = None

class DimensionStyleOverrule(object):
    """
    
    """
    def DimensionStyle(self):
        """
        DimensionStyle -> ObjectId
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            DimStyleTableRecord style: 
            Existing DimStyleTableRecord to which the dimension variable data will be copied.
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetDimensionStyle(self):
        """
        SetDimensionStyle -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            ObjectId id: 
            Input the object ID of the desired DimStyleTableRecord to be used by the dimension.
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData(Dimension, DimStyleTableRecord) -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            DimStyleTableRecord style: 
            DimStyleTableRecord from which to copy the dimension variable information.
        SetDimstyleData(Dimension, ObjectId) -> void
            
            Dimension dimension: 
            Dimension that this overrule is applied against.
            
            ObjectId dimstyleId: 
            Object ID of DimStyleTableRecord from which to copy dimension variable information.
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Name of dictionary entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Array of ids defining the lookup table
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Name of the registered application.
        """
        pass
    
    pass

class DistanceConstraint(object):
    """
    
    DistanceConstraint()()
    
    
    DistanceConstraint(Vector3d)
        Vector3d direction : Input AcGeVector3d indicating the fixed direction which is used to measure the distance. The vector length must not be zero.
    
    
    DistanceConstraint(uint, DistanceDirectionType)
        uint consLineId : Input AcConstraintGroupNodeId indicating the constrained line whose direction is used to measure the distance.
        DistanceDirectionType type : Input DirectionType indicating the direction type which must be either PerpendicularToLine or ParallelToLine.
    
    
    """
    class DistanceDirectionType():
        NotDirected = None
        FixedDirection = None
        PerpendicularToLine = None
        ParallelToLine = None
    
    
    ConstrainedLineId = None
    
    
    Direction = None
    
    
    DirectionType = None
    
    pass

class DragStatus():
    DragStart = None
    DragEnd = None
    DragAbort = None

class DrawLeaderOrderType():
    DrawLeaderHeadFirst = None
    DrawLeaderTailFirst = None

class DrawMLeaderOrderType():
    DrawContentFirst = None
    DrawLeaderFirst = None

class DrawOrderTable(object):
    """
    
    """
    def FirstEntityIsDrawnBeforeSecond(self):
        """
        FirstEntityIsDrawnBeforeSecond -> bool
            
            ObjectId first: 
            Input first object ID
            
            ObjectId second: 
            Input second object ID
        """
        pass
    
    
    def GetFullDrawOrder(self):
        """
        GetFullDrawOrder -> ObjectIdCollection
            
            byte honorSortEntitiesMask: 
            Input indicating whether to test the host database's $SORTENTS variable
        """
        pass
    
    
    def GetRelativeDrawOrder(self):
        """
        GetRelativeDrawOrder -> ObjectIdCollection
            
            byte honorSortEntitiesMask: 
            Input indicating whether to test the host database's $SORTENTS variable
        """
        pass
    
    
    def GetSortHandle(self):
        """
        GetSortHandle -> Handle
            
            ObjectId id: 
            Input object ID
        """
        pass
    
    
    def MoveAbove(self):
        """
        MoveAbove -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
            
            ObjectId target: 
            Target entity
        """
        pass
    
    
    def MoveBelow(self):
        """
        MoveBelow -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
            
            ObjectId target: 
            Target entity
        """
        pass
    
    
    def MoveToBottom(self):
        """
        MoveToBottom -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
        """
        pass
    
    
    def MoveToTop(self):
        """
        MoveToTop -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
        """
        pass
    
    
    def SetRelativeDrawOrder(self):
        """
        SetRelativeDrawOrder -> void
            
            ObjectIdCollection collection: 
            Collection of object IDs
        """
        pass
    
    
    def SwapOrder(self):
        """
        SwapOrder -> void
            
            ObjectId id1: 
            Object ID of first entity
            
            ObjectId id2: 
            Object ID of second entity
        """
        pass
    
    
    BlockId = None
    
    pass

class DuplicateRecordCloning():
    NotApplicable = None
    Ignore = None
    Replace = None
    RefMangleName = None
    MangleName = None
    UnmangleName = None

class DwfDefinition(object):
    """
    
    DwfDefinition()
    """
    isDWFx = None
    
    pass

class DwfReference(object):
    """
    
    DwfReference()
    """

    pass

class DwgFiler(object):
    """
    
    DwgFiler()
    """
    def ReadAddress(self):
        """
        ReadAddress -> IntPtr
        
        """
        pass
    
    
    def ReadBinaryChunk(self):
        """
        ReadBinaryChunk -> byte()
        
        """
        pass
    
    
    def ReadBoolean(self):
        """
        ReadBoolean -> bool
        
        """
        pass
    
    
    def ReadByte(self):
        """
        ReadByte -> byte
        
        """
        pass
    
    
    def ReadBytes(self):
        """
        ReadBytes -> void
            
            byte[] value: 
            A pre-allocated memory area to read bytes into
        """
        pass
    
    
    def ReadDouble(self):
        """
        ReadDouble -> double
        
        """
        pass
    
    
    def ReadHandle(self):
        """
        ReadHandle -> Handle
        
        """
        pass
    
    
    def ReadHardOwnershipId(self):
        """
        ReadHardOwnershipId -> ObjectId
        
        """
        pass
    
    
    def ReadHardPointerId(self):
        """
        ReadHardPointerId -> ObjectId
        
        """
        pass
    
    
    def ReadInt16(self):
        """
        ReadInt16 -> short
        
        """
        pass
    
    
    def ReadInt32(self):
        """
        ReadInt32 -> Integer
        
        """
        pass
    
    
    def ReadInt64(self):
        """
        ReadInt64 -> long
        
        """
        pass
    
    
    def ReadPoint2d(self):
        """
        ReadPoint2d -> Point2d
        
        """
        pass
    
    
    def ReadPoint3d(self):
        """
        ReadPoint3d -> Point3d
        
        """
        pass
    
    
    def ReadScale3d(self):
        """
        ReadScale3d -> Scale3d
        
        """
        pass
    
    
    def ReadSoftOwnershipId(self):
        """
        ReadSoftOwnershipId -> ObjectId
        
        """
        pass
    
    
    def ReadSoftPointerId(self):
        """
        ReadSoftPointerId -> ObjectId
        
        """
        pass
    
    
    def ReadString(self):
        """
        ReadString -> string
        
        """
        pass
    
    
    def ReadUInt16(self):
        """
        ReadUInt16 -> ushort
        
        """
        pass
    
    
    def ReadUInt32(self):
        """
        ReadUInt32 -> UInteger
        
        """
        pass
    
    
    def ReadUInt64(self):
        """
        ReadUInt64 -> ulong
        
        """
        pass
    
    
    def ReadVector2d(self):
        """
        ReadVector2d -> Vector2d
        
        """
        pass
    
    
    def ReadVector3d(self):
        """
        ReadVector3d -> Vector3d
        
        """
        pass
    
    
    def ResetFilerStatus(self):
        """
        ResetFilerStatus -> void
        
        """
        pass
    
    
    def Seek(self):
        """
        Seek -> void
        
        """
        pass
    
    
    def WriteAddress(self):
        """
        WriteAddress -> void
            
            IntPtr value: 
            Location to write to
        """
        pass
    
    
    def WriteBinaryChunk(self):
        """
        WriteBinaryChunk -> void
            
            byte[] chunk: 
            Location to write to
        """
        pass
    
    
    def WriteBoolean(self):
        """
        WriteBoolean -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Location to write to
        """
        pass
    
    
    def WriteByte(self):
        """
        WriteByte -> void
            
            byte value: 
            Location to write to
        """
        pass
    
    
    def WriteBytes(self):
        """
        WriteBytes -> void
            
            byte[] value: 
            Location to write to
        """
        pass
    
    
    def WriteDouble(self):
        """
        WriteDouble -> void
            
            double value: 
            Location to write to
        """
        pass
    
    
    def WriteHandle(self):
        """
        WriteHandle -> void
            
            Handle handle: 
            Location to write to
        """
        pass
    
    
    def WriteHardOwnershipId(self):
        """
        WriteHardOwnershipId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteHardPointerId(self):
        """
        WriteHardPointerId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteInt16(self):
        """
        WriteInt16 -> void
            
            short value: 
            Location to write to
        """
        pass
    
    
    def WriteInt32(self):
        """
        WriteInt32 -> void
            
            int value: 
            Location to write to
        """
        pass
    
    
    def WriteInt64(self):
        """
        WriteInt64 -> void
        
        """
        pass
    
    
    def WritePoint2d(self):
        """
        WritePoint2d -> void
            
            Point2d value: 
            Location to write to
        """
        pass
    
    
    def WritePoint3d(self):
        """
        WritePoint3d -> void
            
            Point3d value: 
            Location to write to
        """
        pass
    
    
    def WriteScale3d(self):
        """
        WriteScale3d -> void
            
            Scale3d value: 
            Location to write to
        """
        pass
    
    
    def WriteSoftOwnershipId(self):
        """
        WriteSoftOwnershipId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteSoftPointerId(self):
        """
        WriteSoftPointerId -> void
            
            ObjectId value: 
            Location to write to
        """
        pass
    
    
    def WriteString(self):
        """
        WriteString -> void
            
            string value: 
            Location to write to
        """
        pass
    
    
    def WriteUInt16(self):
        """
        WriteUInt16 -> void
            
            ushort value: 
            Location to write to
        """
        pass
    
    
    def WriteUInt32(self):
        """
        WriteUInt32 -> void
            
            uint value: 
            Location to write to
        """
        pass
    
    
    def WriteUInt64(self):
        """
        WriteUInt64 -> void
        
        """
        pass
    
    
    def WriteVector2d(self):
        """
        WriteVector2d -> void
            
            Vector2d value: 
            Location to write to
        """
        pass
    
    
    def WriteVector3d(self):
        """
        WriteVector3d -> void
            
            Vector3d value: 
            Location to write to
        """
        pass
    
    
    DwgVersion = None
    
    
    ExtendedMinorVersion = None
    
    
    FilerStatus = None
    
    
    FilerType = None
    
    
    Position = None
    
    pass

class DwgVersion():
    AC1001 = 8
    AC1002 = 9
    AC1003 = 10
    AC1004 = 11
    AC1005 = 12
    AC1006 = 13
    AC1007 = 14
    AC1008 = 15
    AC1009 = 0x10
    AC1010 = 0x11
    AC1011 = 0x12
    AC1012 = 0x13
    AC1013 = 20
    AC1014 = 0x15
    AC1015 = 0x17
    AC1021 = 0x1b
    AC1024 = 0x1d
    AC1027 = 0x1f
    AC1032 = 0x21
    AC1500 = 0x16
    AC1800 = 0x19
    AC1800a = 0x18
    AC1To2 = 1
    AC1To40 = 2
    AC1To50 = 3
    AC2100a = 0x1a
    AC2400a = 0x1c
    AC2700a = 30
    AC2To10 = 5
    AC2To20 = 4
    AC2To21 = 6
    AC2To22 = 7
    AC3200a = 0x20
    Current = 0x21
    Max = 0xff
    MC0To0 = 0
    Newest = 0x21
    Unknown = 0xfe

class DxfCode():
    Alpha = 440
    Angle = 50
    ArbitraryHandle = 320
    AttributePrompt = 3
    AttributeTag = 2
    BinaryChunk = 310
    BlockName = 2
    Bool = 290
    CircleSides = 0x48
    CLShapeName = 4
    CLShapeText = 9
    Color = 0x3e
    ColorName = 430
    ColorRgb = 420
    Comment = 0x3e7
    ControlString = 0x66
    DashLength = 0x31
    Description = 3
    DimBlk1 = 6
    DimBlk2 = 7
    DimensionAlternativePrefixSuffix = 4
    DimensionBlock = 5
    DimPostString = 3
    DimStyleName = 3
    DimVarHandle = 0x69
    Elevation = 0x26
    EmbeddedObjectStart = 0x65
    End = -1
    ExtendedDataAsciiString = 0x3e8
    ExtendedDataBinaryChunk = 0x3ec
    ExtendedDataControlString = 0x3ea
    ExtendedDataDist = 0x411
    ExtendedDataHandle = 0x3ed
    ExtendedDataInteger16 = 0x42e
    ExtendedDataInteger32 = 0x42f
    ExtendedDataLayerName = 0x3eb
    ExtendedDataReal = 0x410
    ExtendedDataRegAppName = 0x3e9
    ExtendedDataScale = 0x412
    ExtendedDataWorldXCoordinate = 0x3f3
    ExtendedDataWorldXDir = 0x3f5
    ExtendedDataWorldXDisp = 0x3f4
    ExtendedDataWorldYCoordinate = 0x3fd
    ExtendedDataWorldYDir = 0x3ff
    ExtendedDataWorldYDisp = 0x3fe
    ExtendedDataWorldZCoordinate = 0x407
    ExtendedDataWorldZDir = 0x409
    ExtendedDataWorldZDisp = 0x408
    ExtendedDataXCoordinate = 0x3f2
    ExtendedDataYCoordinate = 0x3fc
    ExtendedDataZCoordinate = 0x406
    ExtendedInt16 = 400
    FirstEntityId = -2
    GradientAngle = 460
    GradientColCount = 0x1c5
    GradientColVal = 0x1cf
    GradientName = 470
    GradientObjType = 450
    GradientPatType = 0x1c3
    GradientShift = 0x1cd
    GradientTintType = 0x1c4
    GradientTintVal = 0x1ce
    Handle = 5
    HardOwnershipId = 360
    HardPointerId = 340
    HasSubentities = 0x42
    HeaderId = -2
    Int16 = 70
    Int32 = 90
    Int64 = 160
    Int8 = 280
    Invalid = -9999
    LayerLinetype = 0x3d
    LayerName = 8
    LayoutName = 410
    LinetypeAlign = 0x48
    LinetypeElement = 0x31
    LinetypeName = 6
    LinetypePdc = 0x49
    LinetypeProse = 3
    LinetypeScale = 0x30
    LineWeight = 370
    MlineOffset = 0x31
    MlineStyleName = 2
    NormalX = 210
    NormalY = 220
    NormalZ = 230
    Operator = -4
    PixelScale = 0x2f
    PlotStyleNameId = 390
    PlotStyleNameType = 380
    PReactors = -5
    Real = 40
    RegAppFlags = 0x47
    RenderMode = 0x119
    ShapeName = 2
    ShapeScale = 0x2e
    ShapeXOffset = 0x2c
    ShapeYOffset = 0x2d
    SoftOwnershipId = 350
    SoftPointerId = 330
    Start = 0
    Subclass = 100
    SymbolTableName = 2
    SymbolTableRecordComments = 4
    SymbolTableRecordName = 2
    Text = 1
    TextBigFontFile = 4
    TextFontFile = 3
    TextStyleName = 7
    Thickness = 0x27
    TxtSize = 40
    TxtStyleFlags = 0x47
    TxtStylePSize = 0x2a
    TxtStyleXScale = 0x29
    UcsOrg = 110
    UcsOrientationX = 0x6f
    UcsOrientationY = 0x70
    ViewBackClip = 0x2c
    ViewBrightness = 0x8d
    ViewContrast = 0x8e
    ViewFrontClip = 0x2b
    ViewHeight = 0x2d
    ViewLensLength = 0x2a
    ViewMode = 0x47
    ViewportActive = 0x44
    ViewportAspect = 0x29
    ViewportGrid = 0x4c
    ViewportHeight = 40
    ViewportIcon = 0x4a
    ViewportNumber = 0x45
    ViewportSnap = 0x4b
    ViewportSnapAngle = 50
    ViewportSnapPair = 0x4e
    ViewportSnapStyle = 0x4d
    ViewportTwist = 0x33
    ViewportVisibility = 0x43
    ViewportZoom = 0x49
    ViewWidth = 0x29
    Visibility = 60
    XCoordinate = 10
    XDataStart = -3
    XDictionary = -6
    XInt16 = 170
    XReal = 140
    XRefPath = 1
    XTextString = 300
    XXInt16 = 270
    YCoordinate = 20
    ZCoordinate = 30

class DxfFiler(object):
    """
    
    """
    def AtSubclassData(self):
        """
        AtSubclassData -> bool
            
            string value: 
            subClassName that should be compared
        """
        pass
    
    
    def FilerStatus(self):
        """
        FilerStatus -> void
        
        """
        pass
    
    
    def HaltAtClassBoundaries(self):
        """
        HaltAtClassBoundaries -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input Boolean indicating whether or not to halt at certain key markers in the file
        """
        pass
    
    
    def PushBackItem(self):
        """
        PushBackItem -> void
        
        """
        pass
    
    
    def ReadResultBuffer(self):
        """
        ReadResultBuffer -> ResultBuffer
        
        """
        pass
    
    
    def ResetFilerStatus(self):
        """
        ResetFilerStatus -> void
        
        """
        pass
    
    
    def RewindFiler(self):
        """
        RewindFiler -> Integer
        
        """
        pass
    
    
    def SetError(self):
        """
        SetError(string, params string[]) -> void
            
            string format: 
            Input error message string
            
            params string[] values: 
            Input arguments to replace any formatting codes in the error message text
        SetError(Autodesk.AutoCAD.Runtime.ErrorStatus, string, params string[]) -> void
            
            Autodesk.AutoCAD.Runtime.ErrorStatus value: 
            Input ErrorStatus error code
            
            string format: 
            Input error message string
            
            params string[] values: 
            Input arguments to replace any formatting codes in the error message text
        """
        pass
    
    
    def WriteBool(self):
        """
        WriteBool -> void
            
            DxfCode opCode: 
            Input DXF group code to be written out
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input boolean value to be written out
        """
        pass
    
    
    def WriteBoolean(self):
        """
        WriteBoolean -> void
            
            DxfCode opCode: 
            DXF group code to be written out Boolean to be written out
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input boolean value to be written out
        """
        pass
    
    
    def WriteByte(self):
        """
        WriteByte -> void
            
            DxfCode opCode: 
            Input DXF group code to be written out
            
            byte value: 
            Input byte value to be written out
        """
        pass
    
    
    def WriteBytes(self):
        """
        WriteBytes -> void
            
            DxfCode opCode: 
            Input DXF group code to be written out
            
            byte[] chunk: 
            Input byte array to be written out
        """
        pass
    
    
    def WriteDouble(self):
        """
        WriteDouble -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            double value: 
            Double to be written out
            
            int precision: 
            _nt_
        """
        pass
    
    
    def WriteEmbeddedObjectStart(self):
        """
        WriteEmbeddedObjectStart -> void
        
        """
        pass
    
    
    def WriteHandle(self):
        """
        WriteHandle -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Handle value: 
            Input Handle value to be written out
        """
        pass
    
    
    def WriteInt16(self):
        """
        WriteInt16 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            short value: 
            Input System.Int16 value to be written out
        """
        pass
    
    
    def WriteInt32(self):
        """
        WriteInt32 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            int value: 
            Input System.Int32 value to be written out
        """
        pass
    
    
    def WriteInt64(self):
        """
        WriteInt64 -> void
        
        """
        pass
    
    
    def WriteObjectId(self):
        """
        WriteObjectId -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            ObjectId value: 
            Input object ID value to be written out
        """
        pass
    
    
    def WritePoint2d(self):
        """
        WritePoint2d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Point2d value: 
            2D point to be written out
            
            int precision: 
            Decimal places to use when writing out the coordinate double values
        """
        pass
    
    
    def WritePoint3d(self):
        """
        WritePoint3d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Point3d value: 
            3D point to be written out
            
            int precision: 
            Decimal places to use when writing out the coordinate double values
        """
        pass
    
    
    def WriteResultBuffer(self):
        """
        WriteResultBuffer -> void
            
            ResultBuffer buffer: 
            Resbuf structure to be written out
        """
        pass
    
    
    def WriteScale3d(self):
        """
        WriteScale3d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Scale3d value: Scale3d object to be written out
            
            int precision: 
            Decimal places to use when writing out the Scale3d object
        """
        pass
    
    
    def WriteString(self):
        """
        WriteString -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            string value: 
            Input System.String value to be written out
        """
        pass
    
    
    def WriteUInt16(self):
        """
        WriteUInt16 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            ushort value: 
            Input System.UInt16 value to be written out
        """
        pass
    
    
    def WriteUInt32(self):
        """
        WriteUInt32 -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            uint value: 
            Input System.UInt32 value to be written out
        """
        pass
    
    
    def WriteUInt64(self):
        """
        WriteUInt64 -> void
        
        """
        pass
    
    
    def WriteVector2d(self):
        """
        WriteVector2d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Vector2d value: 
            2D vector to be written out
            
            int precision: 
            Decimal places to use when writing out the 2D vector
        """
        pass
    
    
    def WriteVector3d(self):
        """
        WriteVector3d -> void
            
            DxfCode opCode: 
            DXF group code to be written out
            
            Vector3d value: 
            3D vector to be written out
            
            int precision: 
            Decimal places to use when writing out the 3D vector
        """
        pass
    
    
    def WriteXDataStart(self):
        """
        WriteXDataStart -> void
        
        """
        pass
    
    
    AtEmbeddedObjectStart = None
    
    
    AtEndOfFile = None
    
    
    AtEndOfObject = None
    
    
    AtExtendedData = None
    
    
    Database = None
    
    
    DwgVersion = None
    
    
    Elevation = None
    
    
    ErrorMessage = None
    
    
    ExtendedMinorVersion = None
    
    
    FilerType = None
    
    
    IncludesDefaultValues = None
    
    
    IsModifyingExistingObject = None
    
    
    Precision = None
    
    
    Thickness = None
    
    pass

class DynamicBlockReferenceProperty(object):
    """
    
    """
    def GetAllowedValues(self):
        """
        GetAllowedValues -> object()
        
        """
        pass
    
    
    BlockId = None
    
    
    Description = None
    
    
    PropertyName = None
    
    
    PropertyTypeCode = None
    
    
    ReadOnly = None
    
    
    Show = None
    
    
    UnitsType = None
    
    
    Value = None
    
    
    VisibleInCurrentVisibilityState = None
    
    pass

class DynamicBlockReferencePropertyCollection(object):
    """
    
    """
    def CopyTo(self):
        """
        CopyTo -> void
            
            DynamicBlockReferenceProperty[] array: 
            Input array to copy from
            
            int index: 
            Input zero-based index to start at
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class DynamicBlockReferencePropertyCollectionEnumerator(object):
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

class DynamicBlockReferencePropertyUnitsType():
    NoUnits = None
    Angular = None
    Distance = None
    Area = None

class DynamicDimensionChangedEventArgs(object):
    """
    
    DynamicDimensionChangedEventArgs
        int index : Input the index of the dimension
        double value : Input the floating point value of the dimension
    """
    Index = None
    
    
    Value = None
    
    pass

class DynamicDimensionData(object):
    """
    
    DynamicDimensionData()()
    
    
    """
    ApplicationData = None
    
    
    Dimension = None
    
    
    Editable = None
    
    
    Focal = None
    
    
    HideIfValueIsZero = None
    
    
    Visible = None
    
    pass

class DynamicDimensionDataCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            DynamicDimensionData data: 
            A DynamicDimensionData object to add.
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
            
            DynamicDimensionData[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to begin at
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int i: 
            The position of the item to be removed.
        """
        pass
    
    
    Count = None
    
    pass

class EdgeRef(object):
    """
    
    EdgeRef()()
    
    
    EdgeRef(CompoundObjectId)()
    
    
    EdgeRef(CompoundObjectId, SubentityId)()
    
    
    EdgeRef(CompoundObjectId, SubentityId, SubentityId)()
    
    
    EdgeRef(CompoundObjectId, SubentityId, SubentityId, Curve3d)()
    
    
    EdgeRef(Curve3d)()
    
    
    EdgeRef(Entity)()
    
    
    EdgeRef(FullSubentityPath)()
    
    
    EdgeRef(IntPtr, [MarshalAs(UnmanagedType.U1)] bool)()
    
    
    """
    Curve = None
    
    
    FaceSubentity = None
    
    pass

class Ellipse(object):
    """
    
    Ellipse()()
    
    
    Ellipse(Point3d, Vector3d, Vector3d, double, double, double)
        Point3d center : Input center of the ellipse
        Vector3d unitNormal : Input vector specifying normal, which determines the plane of the ellipse
        Vector3d majorAxis : Input vector which represents 1/2 the major axis of the ellipse
        double radiusRatio : Input ratio of the major radius to the minor radius
        double startAngle : Input start angle of the ellipse in radians
        double endAngle : Input end angle of the ellipse in radians
    
    
    """
    def GetAngleAtParameter(self):
        """
        GetAngleAtParameter -> double
            
            double value: 
            Input parameter to evaluate
        """
        pass
    
    
    def GetParameterAtAngle(self):
        """
        GetParameterAtAngle -> double
            
            double angle: 
            Input angle (in radians) at which the parameter is desired
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            Point3d center: 
            Input center point (in WCS coordinates) for the ellipse
            
            Vector3d unitNormal: 
            Input normal vector (in WCS coordinates) which defines the plane in which the ellipse lies
            
            Vector3d majorAxis: 
            Input major axis (in WCS coordinates) for the ellipse
            
            double radiusRatio: 
            Input desired ratio of the major radius to the minor radius
            
            double startAngle: 
            Input start angle (in radians) for the ellipse
            
            double endAngle: 
            Input end angle (in radians) for the ellipse
        """
        pass
    
    
    Center = None
    
    
    EndAngle = None
    
    
    EndParam = None
    
    
    IsNull = None
    
    
    MajorAxis = None
    
    
    MajorRadius = None
    
    
    MinorAxis = None
    
    
    MinorRadius = None
    
    
    Normal = None
    
    
    RadiusRatio = None
    
    
    StartAngle = None
    
    
    StartParam = None
    
    pass

class EndCap():
    Round = None
    Angle = None
    Square = None

class Entity(object):
    """
    
    """
    def AddSubentityPaths(self):
        """
        AddSubentityPaths -> void
            
            FullSubentityPath[] subPaths: 
            Input an array of FullSubentityPath identifiers to add to the entity.
        """
        pass
    
    
    def BoundingBoxIntersectWith(self):
        """
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Plane projectionPlane: 
            Input projection plane for the apparent intersection of the two entities
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        BoundingBoxIntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity will intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input requested intersection type
            
            Plane projectionPlane: 
            Input projection plane for the apparent intersection of the two entities
            
            Point3dCollection points: 
            Output with the points (in WCS coordinates) of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. May be 0 if not applicable
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. May be 0 if not applicable
            Intersect.OnBothOperands: 
            Do not extend either this entity's bounding box edges nor the entityPointer entity. This results in only calculating intersections where the bounding box lines actually intersect with the entityPointer entity.
            Intersect.ExtendThis: 
            Extend this entity's bounding box edges (if necessary) when calculating intersections, but do not extend the entityPointer entity.
            Intersect.ExtendArg : 
            Extend the entityPointer entity (if necessary) when calculating intersections, but do not extend this entity's bounding box edges.
            Intersect.ExtendBoth: 
            Extend both the entityPointer entity and this entity's bounding box edges (if necessary) when calculating intersections
        """
        pass
    
    
    def DeleteSubentityPaths(self):
        """
        DeleteSubentityPaths -> void
            
            FullSubentityPath[] subPaths: 
            Input an array of FullSubentityPath identifiers to delete from the entity
        """
        pass
    
    
    def Draw(self):
        """
        Draw -> void
        
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> void
            
            DBObjectCollection entitySet: 
            Input collection of pointers to new entities; this array may already contain pointers from other entities' explode() methods
        """
        pass
    
    
    def GetGripPoints(self):
        """
        GetGripPoints(GripDataCollection, double, int, Vector3d, GetGripPointsFlags) -> bool
        
        GetGripPoints(Point3dCollection, IntegerCollection, IntegerCollection) -> void
            
            Point3dCollection gripPoints: 
            Input pre-existing array to append the grip points to; output with the entity's grip points appended
            
            IntegerCollection snapModes: 
            not currently used
            
            IntegerCollection geometryIds: 
            not currently used
        """
        pass
    
    
    def GetGraphicsMarkersAtSubentityPathIntPtr(self):
        """
        GetGraphicsMarkersAtSubentityPathIntPtr -> IntPtrCollection
            
            FullSubentityPath subPath: 
            Input FullSubentityPath object that contains an SubentId property with the information necessary to determine the subentity (or subentities) for which the GS Marker(s) is requested.
        """
        pass
    
    
    def GetGripPointsAtSubentityPath(self):
        """
        GetGripPointsAtSubentityPath -> bool
        
        """
        pass
    
    
    def GetObjectSnapPoints(self):
        """
        GetObjectSnapPoints(ObjectSnapModes, int, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection) -> void
            
            ObjectSnapModes snapMode: 
            Input osnap mode being requested
            
            int gsSelectionMark: 
            Input GS marker of the subentity involved in the object snap operation
            
            Point3d pickPoint: 
            Input point (in WCS coordinates) picked during the object snap operation
            
            Point3d lastPoint: 
            Input point (in WCS coordinates) selected just before pickPoint
            
            Matrix3d viewTransform: 
            Input transformation matrix to transform from WCS to DCS
            
            Point3dCollection snapPoints: 
            Input pre-existing array to append osnap points to (may already contain points); output with object snap points appended
            
            IntegerCollection geometryIds: 
            Not in use
            ObjectSnapModes.ModeEnd: 
            Find the endpoint on the entity that is nearest to the pickPoint.
            ObjectSnapModes.ModeMid: 
            Find the midpoint (of any line, arc, etc., subentity) that is nearest to the pickPoint
            ObjectSnapModes.ModeCenter : 
            Find the center point (of any circle or arc subentity) that is nearest to the pickPoint
            ObjectSnapModes.ModeNode: 
            Find the node point (for example, dimension node points) that is nearest to the pickPoint
            ObjectSnapModes.ModeQuad : 
            Find the quad point (traditionally the four quadrant points on a circle) that's nearest to pickPoint
            ObjectSnapModes.ModeIns : 
            Find the intersection point of the entity and a line perpendicular to the entity that passes through lastPoint
            ObjectSnapModes.ModePerpindicular: 
            Find the intersection point of the entity and a line perpendicular to the entity that passes through lastPoint
            ObjectSnapModes.ModeTangent : 
            Find a point on the entity where a line that passes through lastPoint will be tangent to the entity
            ObjectSnapModes.ModeNear : 
            Find the point on the entity that's nearest to pickPoint. You decide what 'nearest' means
        GetObjectSnapPoints(ObjectSnapModes, int, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection, Matrix3d) -> void
            
            ObjectSnapModes snapMode: 
            Input osnap mode being requested
            
            int gsSelectionMark: 
            Input GS marker of the subentity involved in the object snap operation
            
            Point3d pickPoint: 
            Input point (in WCS coordinates) picked during the object snap operation
            
            Point3d lastPoint: 
            Input point (in WCS coordinates) selected just before pickPoint
            
            Matrix3d viewTransform: 
            Input transformation matrix to transform from WCS to DCS
            
            Point3dCollection snapPoints: 
            Input pre-existing array to append osnap points to (may already contain points); output with object snap points appended
            
            IntegerCollection geometryIds: 
            Not in use
            
            Matrix3d insertionMat: 
            Input block transformation
        """
        pass
    
    
    def GetPlane(self):
        """
        GetPlane -> Plane
        
        """
        pass
    
    
    def GetStretchPoints(self):
        """
        GetStretchPoints -> void
            
            Point3dCollection stretchPoints: 
            Input pre-existing array to append the stretch points to; output with the entity's stretch points appended
        """
        pass
    
    
    def GetSubentity(self):
        """
        GetSubentity -> Entity
            
            FullSubentityPath id: 
            Input the path to the subentity
        """
        pass
    
    
    def GetSubentityGeometricExtents(self):
        """
        GetSubentityGeometricExtents -> Extents3d
            
            FullSubentityPath subPath: 
            Input the path to the subentity
        """
        pass
    
    
    def GetSubentityPathsAtGraphicsMarker(self):
        """
        GetSubentityPathsAtGraphicsMarker(SubentityType, IntPtr, Point3d, Matrix3d, ObjectId[]) -> FullSubentityPath()
        
        GetSubentityPathsAtGraphicsMarker(SubentityType, long, Point3d, Matrix3d, int, ObjectId[]) -> FullSubentityPath()
        
        """
        pass
    
    
    def GetTransformedCopy(self):
        """
        GetTransformedCopy -> Entity
            
            Matrix3d transform: 
            Input matrix by which to transform the copy of the entity
        """
        pass
    
    
    def Highlight(self):
        """
        Highlight() -> void
        
        Highlight(FullSubentityPath, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            FullSubentityPath subId: 
            Input FullSubentityPath that identifies the subentity to highlight
            
            [MarshalAs(UnmanagedType.U1)] bool highlightAll: 
            Input Boolean indicating whether to highlight in all viewports
        """
        pass
    
    
    def HighlightState(self):
        """
        HighlightState -> HighlightStyle
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, IntPtr, IntPtr) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            IntPtr thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            IntPtr otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        IntersectWith(Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, long, long) -> void
            
            Entity entityPointer: 
            Input entity with which "this" entity is to intersect
            
            Autodesk.AutoCAD.DatabaseServices.Intersect intersectType: 
            Input type of intersection requested
            
            Plane projectionPlane: 
            Input plane for the projection to occur
            
            Point3dCollection points: 
            Output with the points of intersection appended
            
            long thisGraphicSystemMarker: 
            Input GS marker of subentity of "this" entity that's involved in the intersection operation. Use the 0 default if not applicable.
            
            long otherGraphicSystemMarker: 
            Input GS marker of subentity of the entity pointed to by entityPointer that's involved in the intersection operation. Use the 0 default if not applicable.
        """
        pass
    
    
    def JoinEntity(self):
        """
        JoinEntity -> void
            
            Entity secondaryEntity: 
            The secondary entity, which provides the data to be joined to the this entity.
            
            Exceptions: 
            Description
            
            Autodesk.AutoCAD.Runtime.Exception for ErrorStatus {InvalidInput} or {NotApplicable}: 
            _nt_
        """
        pass
    
    
    def JoinEntities(self):
        """
        JoinEntities -> IntegerCollection
            
            Entity[] otherEntities: 
            The other entities to be joined to the primary entity. Note, some implementations might require all of these entities to be of the same type as the primary entity.
            
            Exceptions: 
            Description
            
            Autodesk.AutoCAD.Runtime.Exception for ErrorStatus {InvalidInput} or {NotApplicable}: 
            _nt_
        """
        pass
    
    
    def List(self):
        """
        List -> void
        
        """
        pass
    
    
    def MoveGripPointsAt(self):
        """
        MoveGripPointsAt(GripDataCollection, Vector3d, MoveGripPointsFlags) -> void
        
        MoveGripPointsAt(IntegerCollection, Vector3d) -> void
            
            IntegerCollection indices: 
            Input array containing index values (which correspond to grip points reported by the GetGripPoints() method) that indicate which grip points are currently "hot"
            
            Vector3d offset: 
            Input vector (in WCS coordinates) indicating the direction and magnitude that the grip points have been translated
        """
        pass
    
    
    def MoveStretchPointsAt(self):
        """
        MoveStretchPointsAt -> void
            
            IntegerCollection indices: 
            Input array containing index values (which correspond to stretch points reported by the GetStretchPoints() method) that indicate which stretch points are being translated
            
            Vector3d offset: 
            Input vector (in WCS coordinates) indicating the direction and magnitude that the stretch points have been translated
        """
        pass
    
    
    def PopHighlight(self):
        """
        PopHighlight -> void
            
            FullSubentityPath subId: 
            Input AcDbFullSubentPath that identifies the subentity to unhighlight
        """
        pass
    
    
    def PushHighlight(self):
        """
        PushHighlight -> void
            
            FullSubentityPath subId: 
            Input AcDbFullSubentPath that identifies the subentity to highlight
            
            HighlightStyle highlightStyle: 
            Input AcGiHighlightStyle for this subid
        """
        pass
    
    
    def RecordGraphicsModified(self):
        """
        RecordGraphicsModified -> void
            
            [MarshalAs(UnmanagedType.U1)] bool setModified: 
            Input Boolean value to indicate if the entity's graphics should be updated on screen when the object is closed
        """
        pass
    
    
    def SaveAs(self):
        """
        SaveAs -> void
            
            WorldDraw mode: 
            Input pointer to fully initialized WorldDraw object (or an object of a class derived from WorldDraw)
            
            Autodesk.AutoCAD.DatabaseServices.SaveType st: 
            Input SaveType indicates why the saveAs is being called.
        """
        pass
    
    
    def SetDatabaseDefaults(self):
        """
        SetDatabaseDefaults() -> void
        
        SetDatabaseDefaults(Database) -> void
            
            Database sourceDatabase: 
            Input database whose defaults will be used to set the values of the entity
        """
        pass
    
    
    def SetDragStatus(self):
        """
        SetDragStatus -> void
            
            DragStatus status: 
            Value describing the status of the drag operation; one of the values from the DragStat enumeration
        """
        pass
    
    
    def SetGripStatus(self):
        """
        SetGripStatus -> void
            
            GripStatus status: 
            Value describing the status of the grip operation; one of the values from the GripStatus enumeration
        """
        pass
    
    
    def SetLayerId(self):
        """
        SetLayerId -> void
            
            ObjectId newValue: 
            Input name of the LayerTableRecord to be referenced by the entity
            
            [MarshalAs(UnmanagedType.U1)] bool allowHidden: 
            Input Boolean indicating whether to allow newValue to specify a hidden layer
        """
        pass
    
    
    def SetPropertiesFrom(self):
        """
        SetPropertiesFrom -> void
            
            Entity entityPointer: 
            Input entity from which to copy the properties
        """
        pass
    
    
    def SetSubentityGripStatus(self):
        """
        SetSubentityGripStatus -> void
            
            GripStatus status: 
            Input the status of the grip operation
            
            FullSubentityPath subentity: 
            Input the subentity on the object whose grip status changed
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
            
            Matrix3d transform: 
            Input transformation matrix to be applied to the entity
        """
        pass
    
    
    def TransformSubentityPathsBy(self):
        """
        TransformSubentityPathsBy -> void
            
            FullSubentityPath[] subPaths: 
            Input an array of one or more FullSubentityPath objects identifying the subentities to transform
            
            Matrix3d transform: 
            Input the WCS transformation to apply to each of the supplied subentities.
        """
        pass
    
    
    def Unhighlight(self):
        """
        Unhighlight() -> void
        
        Unhighlight(FullSubentityPath, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            FullSubentityPath subId: 
            Input FullSubentityPath that identifies which subentity to unhighlight
            
            [MarshalAs(UnmanagedType.U1)] bool highlightAll: 
            Input Boolean indicating whether to unhighlight in all viewports
        """
        pass
    
    
    BlockId = None
    
    
    BlockName = None
    
    
    CastShadows = None
    
    
    CloneMeForDragging = None
    
    
    CollisionType = None
    
    
    Color = None
    
    
    ColorIndex = None
    
    
    CompoundObjectTransform = None
    
    
    Ecs = None
    
    
    EdgeStyleId = None
    
    
    EntityColor = None
    
    
    FaceStyleId = None
    
    
    ForceAnnoAllVisible = None
    
    
    GeometricExtents = None
    
    
    Hyperlinks = None
    
    
    IsPlanar = None
    
    
    Layer = None
    
    
    LayerId = None
    
    
    Linetype = None
    
    
    LinetypeId = None
    
    
    LinetypeScale = None
    
    
    LineWeight = None
    
    
    Material = None
    
    
    MaterialId = None
    
    
    MaterialMapper = None
    
    
    PlotStyleName = None
    
    
    PlotStyleNameId = None
    
    
    ReceiveShadows = None
    
    
    Transparency = None
    
    
    Visible = None
    
    
    VisualStyleId = None
    
    pass

class EntityAlignmentEventArgs(object):
    """
    
    EntityAlignmentEventArgs
        Autodesk.AutoCAD.DatabaseServices.Entity Entity : Input Autodesk.AutoCAD.DatabaseServices.Entity object.
        Point3d PickPoint : Input Autodesk.AutoCAD.Geometry.Point3d object.
        Vector3d Normal : Input Autodesk.AutoCAD.Geometry.Vector3d object.
        Point3d ClosestPoint : Input Autodesk.AutoCAD.Geometry.Point3d object.
        Vector3d Direction : Input Autodesk.AutoCAD.Geometry.Vector3d object.
        FullSubentityPath[] Path : Input Autodesk.AutoCAD.DatabaseServices.FullSubentityPath[] object.
    """
    def GetPickedEntities(self):
        """
        GetPickedEntities -> FullSubentityPath[]
        
        """
        pass
    
    
    ClosestPoint = None
    
    
    Direction = None
    
    
    Entity = None
    
    
    Normal = None
    
    
    PickPoint = None
    
    pass

class EqualCurvatureConstraint(object):
    """
    
    EqualCurvatureConstraint()
    """

    pass

class EqualDistanceConstraint(object):
    """
    
    EqualDistanceConstraint()
    """

    pass

class EqualHelpParameterConstraint(object):
    """
    
    EqualHelpParameterConstraint()
    """
    def GetEqualHelpParameters(self):
        """
        GetEqualHelpParameters -> void
            
            pHelpParameter1: 
            The returned pointer to the first AcHelpParameter object.
            
            pHelpParameter2: 
            The returned pointer to the second AcHelpParameter object.
        """
        pass
    
    pass

class EqualLengthConstraint(object):
    """
    
    EqualLengthConstraint()
    """

    pass

class EqualRadiusConstraint(object):
    """
    
    EqualRadiusConstraint()
    """

    pass

class ExplicitConstraint(object):
    """
    
    """
    DimDependencyId = None
    
    
    MeasuredValue = None
    
    
    ValueDependencyId = None
    
    pass

class Extents2d(object):
    """
    
    Extents2d(Point2d, Point2d)
        Point2d minimum : Input minimum extent
        Point2d maximum : Input maximum extent
    
    
    Extents2d(double, double, double, double)
        double minX : Minimum X extent
        double minY : Minimum Y extent
        double maxX : Maximum X extent
        double maxY : Maximum Y extent
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Extents2d) -> bool
            
            Extents2d a: 
            Object to compare
        IsEqualTo(Extents2d, Tolerance) -> bool
            
            Extents2d a: 
            Input object to compare
            
            Tolerance tolerance: 
            Input tolerance to be used
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format to display
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    MaxPoint = None
    
    
    MinPoint = None
    
    pass

class Extents3d(object):
    """
    
    Extents3d()()
    
    
    Extents3d(Point3d, Point3d)
        Point3d min : Input minimum extent
        Point3d max : Input maximum extent
    
    
    """
    def AddBlockExtents(self):
        """
        AddBlockExtents -> void
            
            BlockTableRecord pointerToBlockTableRecord: 
            Pointer to a block table record
        """
        pass
    
    
    def AddExtents(self):
        """
        AddExtents -> void
            
            Extents3d source: 
            Input another Extents3d object
        """
        pass
    
    
    def AddPoint(self):
        """
        AddPoint -> void
            
            Point3d pt: 
            Input 3D point
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare
        """
        pass
    
    
    def ExpandBy(self):
        """
        ExpandBy -> void
            
            Vector3d vector: 
            Input 3D vector
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Extents3d) -> bool
            
            Extents3d a: 
            Input object to compare
        IsEqualTo(Extents3d, Tolerance) -> bool
            
            Extents3d a: 
            Input object to compare
            
            Tolerance tolerance: 
            Input tolerance to check against
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            Point3d min: 
            Input minimum extent
            
            Point3d max: 
            Input maximum extent
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format to display
            
            IFormatProvider provider: 
            Input culture-specific format
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
            
            Matrix3d mat: 
            Input 3D transformation matrix
        """
        pass
    
    
    MaxPoint = None
    
    
    MinPoint = None
    
    pass

class ExtrudedSurface(object):
    """
    
    ExtrudedSurface()
    """
    def CreateExtrudedSurface(self):
        """
        CreateExtrudedSurface -> void
            
            Entity sweepEnt: 
            Input the curve, region, or planar surface to be swept
            
            Vector3d directionVec: 
            Input the vector that indicates the direction and distance of the sweep operation
            
            Autodesk.AutoCAD.DatabaseServices.SweepOptions sweepOptions: 
            Input sweep options
        """
        pass
    
    
    def SetExtrude(self):
        """
        SetExtrude -> void
            
            Vector3d sweepVec: 
            Input extrusion vector
            
            Autodesk.AutoCAD.DatabaseServices.SweepOptions sweepOptions: 
            Input sweep options
        """
        pass
    
    
    Height = None
    
    
    SweepEntity = None
    
    
    SweepOptions = None
    
    
    SweepProfile = None
    
    
    SweepVec = None
    
    
    TaperAngle = None
    
    pass

class Face(object):
    """
    
    Face()()
    
    
    Face(Point3d, Point3d, Point3d, Point3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool)
        Point3d pointer1 : Input first corner point (in WCS coordinates)
        Point3d pointer2 : Input second corner point (in WCS coordinates)
        Point3d pointer3 : Input third corner point (in WCS coordinates)
        Point3d pointer4 : Input fourth corner point (in WCS coordinates)
        [MarshalAs(UnmanagedType.U1)] bool value1 : Input Boolean indicating whether or not first edge will be visible
        [MarshalAs(UnmanagedType.U1)] bool value2 : Input Boolean indicating whether or not second edge will be visible
        [MarshalAs(UnmanagedType.U1)] bool value3 : Input Boolean indicating whether or not third edge will be visible
        [MarshalAs(UnmanagedType.U1)] bool value4 : Input Boolean indicating whether or not fourth edge will be visible
    
    
    Face(Point3d, Point3d, Point3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool)
        Point3d pointer1 : Input first corner point (in WCS coordinates)
        Point3d pointer2 : Input second corner point (in WCS coordinates)
        Point3d pointer3 : Input third corner point (in WCS coordinates)
        [MarshalAs(UnmanagedType.U1)] bool value1 : Input Boolean indicating whether or not first edge will be visible
        [MarshalAs(UnmanagedType.U1)] bool value2 : Input Boolean indicating whether or not second edge will be visible
        [MarshalAs(UnmanagedType.U1)] bool value3 : Input Boolean indicating whether or not third edge will be visible
        [MarshalAs(UnmanagedType.U1)] bool value4 : Input Boolean indicating whether or not fourth edge will be visible
    
    
    """
    def GetVertexAt(self):
        """
        GetVertexAt -> Point3d
            
            short value: 
            Input vertex index number (must be 1 through 4)
        """
        pass
    
    
    def IsEdgeVisibleAt(self):
        """
        IsEdgeVisibleAt -> bool
            
            short vertexIndex: 
            Input vertex index number (must be 1 through 4)
        """
        pass
    
    
    def MakeEdgeInvisibleAt(self):
        """
        MakeEdgeInvisibleAt -> void
            
            short vertexIndex: 
            Input vertex index number of starting vertex for edge
        """
        pass
    
    
    def MakeEdgeVisibleAt(self):
        """
        MakeEdgeVisibleAt -> void
            
            short vertexIndex: 
            Input vertex index number of starting vertex for edge
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt -> void
            
            short vertexIndex: 
            Input vertex index number (must be 1 through 4)
            
            Point3d vertexPosition: 
            Input vertex position (in WCS coordinates)
        """
        pass
    
    pass

class FaceRecord(object):
    """
    
    FaceRecord()()
    
    
    FaceRecord(short, short, short, short)
        short vertex0 : Input index number of first vertex for the face
        short vertex1 : Input index number of second vertex for the face
        short vertex2 : Input index number of third vertex for the face
        short vertex3 : Input index number of fourth vertex for the face
    
    
    """
    def GetVertexAt(self):
        """
        GetVertexAt -> short
            
            short faceIndex: 
            Input face corner index number (must be 0 through 3)
        """
        pass
    
    
    def IsEdgeVisibleAt(self):
        """
        IsEdgeVisibleAt -> bool
            
            short faceIndex: 
            Input face corner index number (must be 0 through 3)
        """
        pass
    
    
    def MakeEdgeInvisibleAt(self):
        """
        MakeEdgeInvisibleAt -> void
            
            short faceIndex: 
            Input index number of starting corner for edge (must be 0 - 3)
        """
        pass
    
    
    def MakeEdgeVisibleAt(self):
        """
        MakeEdgeVisibleAt -> void
            
            short faceIndex: 
            Input index number of starting corner for edge (must be 0 - 3)
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt -> void
            
            short faceIndex: 
            Input face corner index number (must be 0 - 3)
            
            short vertexIndex: 
            Input index of vertex in PolyFaceMesh's vertex list that is to be used for this face corner
        """
        pass
    
    pass

class FaceRef(object):
    """
    
    FaceRef()()
    
    
    FaceRef(CompoundObjectId)()
    
    
    FaceRef(CompoundObjectId, SubentityId)()
    
    
    """

    pass

class FeatureControlFrame(object):
    """
    
    FeatureControlFrame()()
    
    
    FeatureControlFrame(string, Point3d, Vector3d, Vector3d)
        string codes : Input text string containing the codes to specify the feature control symbols and the tolerance for this object. If this value is Null, this is just like calling the default constructor.
        Point3d insertionPoint : Input Insertion point (WCS) of this Fcf object
        Vector3d normalVector : Input Normal vector (WCS) of the plane containing this Fcf object
        : Input X-direction vector (WCS) of this Fcf
    
    
    """
    def GetBoundingPoints(self):
        """
        GetBoundingPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetBoundingPolyline(self):
        """
        GetBoundingPolyline -> Point3dCollection
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input objectId of the desired DimensionStyle to be used by the Fcf
        """
        pass
    
    
    def SetOrientation(self):
        """
        SetOrientation -> void
            
            Vector3d norm: 
            Input vector (in WCS) to be used to define the new plane that will contain the Fcf
            
            Vector3d dir: 
            Input X-Direction vector (WCS) for the Fcf
        """
        pass
    
    
    Dimclrd = None
    
    
    Dimclrt = None
    
    
    DimensionStyle = None
    
    
    DimensionStyleName = None
    
    
    Dimgap = None
    
    
    Dimscale = None
    
    
    Dimtxsty = None
    
    
    Dimtxt = None
    
    
    Direction = None
    
    
    Location = None
    
    
    Normal = None
    
    
    Text = None
    
    
    TextStyleId = None
    
    
    TextStyleName = None
    
    pass

class Field(object):
    """
    
    Field()()
    
    
    Field(string)
        string fieldCode : Input field code
    
    
    Field(string, [MarshalAs(UnmanagedType.U1)] bool)
        string fieldCode : Input field code
        [MarshalAs(UnmanagedType.U1)] bool textField : Input flag indicating whether this is a text field
    
    
    """
    def ConvertToTextField(self):
        """
        ConvertToTextField -> void
        
        """
        pass
    
    
    def Evaluate(self):
        """
        Evaluate() -> void
        
        Evaluate(int, Database) -> void
            
            int evaluationOptions: 
            Input context in which the field is evaluated; the context flag can be one of the predefined FieldEvaluationContext enum flags or a user-defined context flag
            
            Database database: 
            Input database to be used for the evaluation, which can be null
        """
        pass
    
    
    def FindField(self):
        """
        FindField -> bool
        
        """
        pass
    
    
    def GetChildren(self):
        """
        GetChildren -> Field()
        
        """
        pass
    
    
    def GetChildrenIds(self):
        """
        GetChildrenIds -> ObjectId()
        
        """
        pass
    
    
    def GetData(self):
        """
        GetData -> object
            
            string key: 
            Input key to get the data; the key cannot be null or an empty string
        """
        pass
    
    
    def GetFieldCode(self):
        """
        GetFieldCode() -> string
        
        GetFieldCode(FieldCodeFlags) -> string
            
            FieldCodeFlags flags: 
            Input flag, which can be one or more of the FieldCodeFlags values
        """
        pass
    
    
    def GetFieldCodeWithChildren(self):
        """
        GetFieldCodeWithChildren() -> FieldCodeWithChildren
        
        GetFieldCodeWithChildren(FieldCodeFlags) -> FieldCodeWithChildren
            
            FieldCodeFlags flags: 
            Input flag, which can be one or more of the FieldCodeFlags values
        """
        pass
    
    
    def GetStringValue(self):
        """
        GetStringValue -> string
        
        """
        pass
    
    
    def SetData(self):
        """
        SetData(string, object) -> void
            
            string key: 
            Input key to use to set and get the data; the key cannot be null or an empty string
            
            object data: 
            Input the object that contains the data
        SetData(string, object, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            string key: 
            Input key to use to set and get the data; the key cannot be null or an empty string
            
            object data: 
            Input the object that contains the data
            
            [MarshalAs(UnmanagedType.U1)] bool recursive: 
            Input true if the data is to be set in all child fields, false if it is to be set only in this field
        """
        pass
    
    
    def SetFieldCode(self):
        """
        SetFieldCode -> void
            
            string fieldCode: 
            Input field code to set
        """
        pass
    
    
    def SetFieldCodeWithChildren(self):
        """
        SetFieldCodeWithChildren(FieldCodeFlags, FieldCodeWithChildren) -> void
            
            FieldCodeFlags flag: 
            Input flag, which can be one or more of the FieldCodeFlags values
            
            FieldCodeWithChildren fieldCode: 
            Input field code to set
        SetFieldCodeWithChildren(FieldCodeWithChildren) -> void
            
            FieldCodeWithChildren fieldCode: 
            Input field code to set
        """
        pass
    
    
    DataType = None
    
    
    EvaluationOption = None
    
    
    EvaluationStatus = None
    
    
    EvaluatorId = None
    
    
    FilingOption = None
    
    
    Format = None
    
    
    HyperLink = None
    
    
    IsTextField = None
    
    
    State = None
    
    
    Value = None
    
    pass

class FieldCodeFlags():
    AddMarkers = 0x10
    EscapeBackslash = 0x20
    EvaluatedChildren = 4
    EvaluatedText = 2
    FieldCode = 1
    ObjectReference = 8
    PreserveFields = 0x80
    StripOptions = 0x40
    TextField = 0x100

class FieldCodeWithChildren(object):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            int i: 
            Index at which the new entry will be added to the array of children.
            
            Field field: 
            New child field to add to the array of children at index i.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    Children = None
    
    
    FieldCode = None
    
    pass

class FieldEvaluationContext():
    Demand = 0x20
    Etransmit = 8
    Open = 1
    Plot = 4
    Preview = 0x40
    Regen = 0x10
    Save = 2

class FieldEvaluationOptions():
    Automatic = 0x3f
    Disable = 0
    OnDemand = 0x20
    OnEtransmit = 8
    OnOpen = 1
    OnPlot = 4
    OnRegen = 0x10
    OnSave = 2

class FieldEvaluationResult(object):
    """
    
    """
    Evaluated = None
    
    
    Found = None
    
    pass

class FieldEvaluationStatus():
    EvaluatorNotFound = 4
    InvalidCode = 0x10
    InvalidContext = 0x20
    NotYetEvaluated = 1
    OtherError = 0x40
    Success = 2
    SyntaxError = 8

class FieldEvaluationStatusResult(object):
    """
    
    FieldEvaluationStatusResult
        FieldEvaluationStatus s : _nt_
        int e : _nt_
        string m : _nt_
    """
    ErrorCode = None
    
    
    ErrorMessage = None
    
    
    Status = None
    
    pass

class FieldFilingOptions():
    SkipFilingResult = 1

class FieldState():
    Compiled = 2
    Evaluated = 8
    HasCache = 0x10
    HasFormattedString = 0x20
    Initialized = 1
    Modified = 4

class FileOpenMode():
    OpenForReadAndAllShare = 3
    OpenForReadAndReadShare = 1
    OpenForReadAndWriteNoShare = 2
    OpenTryForReadShare = 4

class FilerType():
    FileFiler = None
    CopyFiler = None
    UndoFiler = None
    BagFiler = None
    IdTranslateFiler = None
    PageFiler = None
    DeepCloneFiler = None
    IdFiler = None
    PurgeFiler = None
    WblockCloneFiler = None

class FilletTrimMode():
    TrimNone = None
    TrimStart = None
    TrimSecond = None
    TrimBoth = None

class FindFileHint():
    Default = None
    FontFile = None
    CompiledShapeFile = None
    TrueTypeFontFile = None
    EmbeddedImageFile = None
    XRefDrawing = None
    PatternFile = None
    ArxApplication = None
    FontMapFile = None
    UnderlayFile = None

class FitData(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare with
        """
        pass
    
    
    def GetFitPoints(self):
        """
        GetFitPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(FitData) -> bool
            
            FitData other: 
            Object to compare with
        IsEqualTo(FitData, Tolerance) -> bool
            
            FitData other: 
            Object to compare with
            
            Tolerance tolerance: 
            Tolerance range
        """
        pass
    
    
    Degree = None
    
    
    EndTangent = None
    
    
    FitTolerance = None
    
    
    StartTangent = None
    
    
    TangentsExist = None
    
    pass

class FixedConstraint(object):
    """
    
    FixedConstraint()
    """

    pass

class FlowDirection():
    NotSet = None
    LeftToRight = None
    RightToLeft = None
    TopToBottom = None
    BottomToTop = None
    ByStyle = None

class Font(object):
    """
    
    Font()
    """
    IsTrueType = None
    
    
    Name = None
    
    pass

class FormattedTableData(object):
    """
    
    FormattedTableData()
    """
    def GetAlignment(self):
        """
        GetAlignment -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetBackgroundColor(self):
        """
        GetBackgroundColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
        """
        pass
    
    
    def GetContentColor(self):
        """
        GetContentColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetGridColor(self):
        """
        GetGridColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetGridLinetype(self):
        """
        GetGridLinetype -> ObjectId
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetGridLineWeight(self):
        """
        GetGridLineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetGridVisibility(self):
        """
        GetGridVisibility -> Autodesk.AutoCAD.DatabaseServices.Visibility
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetMargin(self):
        """
        GetMargin -> double
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            CellMargins margin: 
            Input margin type to get
        """
        pass
    
    
    def GetMergeRange(self):
        """
        GetMergeRange -> CellRange
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetRotation(self):
        """
        GetRotation -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetOverride(self):
        """
        GetOverride(int, int, int) -> CellProperties
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            int content: 
            Input content index. This can be -1. See remarks.
        GetOverride(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType) -> GridProperties
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line type
        """
        pass
    
    
    def GetScale(self):
        """
        GetScale -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetTextHeight(self):
        """
        GetTextHeight -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetTextStyle(self):
        """
        GetTextStyle -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsFormatEditable(self):
        """
        IsFormatEditable -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsMerged(self):
        """
        IsMerged -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def Merge(self):
        """
        Merge -> void
            
            CellRange range: 
            Input cell range to merge
        """
        pass
    
    
    def RemoveAllOverrides(self):
        """
        RemoveAllOverrides -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
        """
        pass
    
    
    def SetAlignment(self):
        """
        SetAlignment -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.CellAlignment value: 
            Input alignment
        """
        pass
    
    
    def SetBackgroundColor(self):
        """
        SetBackgroundColor -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.Colors.Color value: 
            Input color to set
        """
        pass
    
    
    def SetContentColor(self):
        """
        SetContentColor -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.Colors.Color value: 
            Input color
        """
        pass
    
    
    def SetGridColor(self):
        """
        SetGridColor -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.Colors.Color value: 
            Input grid color to set
        """
        pass
    
    
    def SetGridLinetype(self):
        """
        SetGridLinetype -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            ObjectId value: 
            Input grid line type to set
        """
        pass
    
    
    def SetGridLineWeight(self):
        """
        SetGridLineWeight -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight value: 
            Input grid line weight to set
        """
        pass
    
    
    def SetGridVisibility(self):
        """
        SetGridVisibility -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLinetype: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.Visibility value: 
            Input grid visibility to set
        """
        pass
    
    
    def SetMargin(self):
        """
        SetMargin -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            CellMargins margin: 
            Input margin type to set. Multiple margin types can be combined using OR.
            
            double value: 
            Input margin value to set
        """
        pass
    
    
    def SetOverride(self):
        """
        SetOverride(int, int, int, CellProperties) -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            int content: 
            Input content index. This can be -1. See remarks.
            
            CellProperties cellProperty: 
            Input override to set
        SetOverride(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, GridProperties) -> void
            
            int row: 
            Input row index. This can be -1. See remarks
            
            int column: 
            Input column index. This can be -1. See
        """
        pass
    
    
    def SetRotation(self):
        """
        SetRotation -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            double value: 
            Input angle in radians
        """
        pass
    
    
    def SetScale(self):
        """
        SetScale -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            double value: 
            Input scale
        """
        pass
    
    
    def SetTextHeight(self):
        """
        SetTextHeight -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            double value: 
            Input text height
        """
        pass
    
    
    def SetTextStyle(self):
        """
        SetTextStyle -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId value: 
            Input text style
        """
        pass
    
    
    def Unmerge(self):
        """
        Unmerge -> void
            
            CellRange range: 
            Input cell range to unmerge
        """
        pass
    
    pass

class FrameSetting():
    ImageFrameAbove = 1
    ImageFrameBelow = 2
    ImageFrameInvalid = -1
    ImageFrameOff = 0
    ImageFrameOnNoPlot = 3

class FullDwgVersion(object):
    """
    
    FullDwgVersion
        DwgVersion majorVersion : Input major version
        Autodesk.AutoCAD.DatabaseServices.MaintenanceReleaseVersion minorVersion : Input minor version
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString -> string
        
        """
        pass
    
    
    MajorVersion = None
    
    
    MinorVersion = None
    
    pass

class FullSubentityPath(object):
    """
    
    FullSubentityPath
        ObjectId[] ids : Input object ID array
        SubentityId index : Input subent ID object
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare to
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetObjectIds(self):
        """
        GetObjectIds -> ObjectId()
        
        """
        pass
    
    
    IsNull = None
    
    
    Null = None
    
    
    SubentId = None
    
    pass

class G2SmoothConstraint(object):
    """
    
    G2SmoothConstraint()
    """

    pass

class GeoCSProjectionCode():
    Alber = 4
    Azede = 0x3b
    Azmea = 11
    Azmed = 7
    Bipolar = 0x1f
    Bonne = 0x18
    Cassini = 0x16
    Eckert4 = 0x19
    Eckert6 = 0x1a
    Edcnc = 12
    Edcyl = 20
    EdcylE = 0x43
    GaussK = 0x2e
    Gnomonic = 0x13
    Goode = 0x1c
    Hom1uv = 0x501
    Hom1xy = 0x502
    Hom2uv = 0x503
    Hom2xy = 0x504
    Krovak = 0x2f
    Krvk95 = 0x33
    LL = 1
    Lm1sp = 0x24
    Lm2sp = 0x25
    Lmblg = 0x26
    Lmbrtaf = 0x41
    Lmtan = 8
    Miller = 13
    Mndotl = 0x29
    Mndott = 0x2a
    Modpc = 10
    Mollweid = 0x1b
    Mrcat = 6
    MrcatK = 0x31
    Mstero = 15
    Neacyl = 0x1d
    Nerth = 0x37
    Nrthsrt = 0x40
    Nzealand = 0x10
    OblqM = 5
    Obqcyl = 0x38
    Ortho = 0x12
    Ostn02 = 60
    Ostn97 = 0x3a
    Ostro = 0x22
    PlateCarree = 0x44
    Plycn = 9
    Pstro = 0x21
    Pstrosl = 0x35
    PvMercator = 0x45
    Robinson = 0x17
    Rskew = 0x505
    Rskewc = 0x506
    Rskewo = 0x507
    Sinus = 0x11
    Sotrm = 0x2b
    Sstro = 0x23
    Swiss = 0x20
    Sys34 = 0x39
    Sys34_01 = 0x42
    Sys34_99 = 0x3d
    Teacyl = 30
    Tm = 3
    Trmeraf = 0x36
    Trmrkrg = 0x3e
    Trmrs = 0x2d
    Unknown = 0
    Utm = 0x2c
    Vdgrntn = 0x15
    Wccsl = 0x27
    Wccst = 40
    Winkl = 0x3f

class GeoCSType():
    Unknown = None
    Arbitrary = None
    Geographic = None
    Projected = None

class GeoCSUnit():
    BenoitChain = 0x1a
    BenoitLink = 30
    Brealey = 0x26
    CaGrid = 0x17
    CapeRood = 0x25
    Centimeter = 7
    Centisec = 0x3f2
    ClarkeChain = 0x18
    ClarkeFoot = 5
    ClarkeLink = 0x1c
    Decameter = 0x30
    Decimeter = 0x12
    Decisec = 0x3f1
    Degree = 0x3e9
    Dekameter = 20
    Foot = 2
    Furlong = 0x23
    GermanMeter = 0x16
    GoldCoastFoot = 40
    Grad = 0x3ea
    Grade = 0x3eb
    GunterChain = 0x19
    GunterLink = 0x1d
    Hectometer = 0x15
    IFoot = 4
    IInch = 6
    IMile = 13
    Inch = 3
    IndianFoot = 0x2b
    IndianFt37 = 0x2c
    IndianFt62 = 0x2d
    IndianFt75 = 0x2e
    IndianYard = 0x2a
    IndianYd37 = 0x2f
    InternationalChain = 0x31
    InternationalLink = 50
    IYard = 12
    Kilometer = 8
    Knot = 14
    Lat66 = 0x10
    Lat83 = 0x11
    MapInfo = 0x3ec
    Meter = 1
    MicroInch = 0x29
    Mil = 0x3ed
    Mile = 11
    Millimeter = 0x13
    Millisec = 0x3f3
    Minute = 0x3ee
    NautM = 15
    Perch = 0x21
    Pole = 0x22
    Radian = 0x3ef
    Rod = 0x20
    Rood = 0x24
    SearsChain = 0x1b
    SearsFoot = 0x27
    SearsLink = 0x1f
    SearsYard = 10
    Second = 0x3f0
    Unknown = 0
    Yard = 9

class GeoCoordinateCategory(object):
    """
    
    """
    def CreateAll(self):
        """
        CreateAll -> GeoCoordinateCategory()
        
        """
        pass
    
    
    def GetCoordinateAt(self):
        """
        GetCoordinateAt -> GeoCoordinateSystem
        
        """
        pass
    
    
    def NumOfCoordinate(self):
        """
        NumOfCoordinate -> Integer
        
        """
        pass
    
    
    ID = None
    
    pass

class GeoCoordinateSystem(object):
    """
    
    """
    def Create(self):
        """
        Create -> GeoCoordinateSystem
            
            string coordSysIdOrFullDef: 
            A coordinate system name. For example: "WORLD-MERCATOR"
        """
        pass
    
    
    def CreateAll(self):
        """
        CreateAll() -> GeoCoordinateSystem()
        
        CreateAll(GeoCoordinateCategory) -> GeoCoordinateSystem()
        
        CreateAll(ValueType modopt(Point3d) modopt(IsBoxed)) -> GeoCoordinateSystem()
            
            ValueType modopt(Point3d) modopt(IsBoxed) geoPt: 
            Input geodetic point in (longitude, latitude, altitude) format.
        """
        pass
    
    
    def GetProjectionParamList(self):
        """
        GetProjectionParamList -> GeoProjectionParam()
        
        """
        pass
    
    
    CartesianExtents = None
    
    
    Datum = None
    
    
    Description = None
    
    
    Ellipsoid = None
    
    
    EPSGcode = None
    
    
    GeodeticExtents = None
    
    
    GeoUnit = None
    
    
    ID = None
    
    
    Offset = None
    
    
    ProjectionCode = None
    
    
    Type = None
    
    
    Unit = None
    
    
    UnitScale = None
    
    
    WktRepresentation = None
    
    
    XmlRepresentation = None
    
    pass

class GeoCoordinateTransformer(object):
    """
    
    """
    def Create(self):
        """
        Create -> GeoCoordinateTransformer
        
        """
        pass
    
    
    def TransformPoint(self):
        """
        TransformPoint(Point3d) -> Point3d
        
        TransformPoint(string, string, Point3d) -> Point3d
        
        """
        pass
    
    
    def TransformPoints(self):
        """
        TransformPoints(Point3dCollection) -> Point3dCollection
        
        TransformPoints(string, string, Point3dCollection) -> Point3dCollection
        
        """
        pass
    
    
    SourceCSid = None
    
    
    TargetCSid = None
    
    pass

class GeoLocationData(object):
    """
    
    GeoLocationData()
    """
    def AddMeshPointMap(self):
        """
        AddMeshPointMap -> void
            
            int index: 
            Input the index to insert at
            
            Point2d sourcePt: 
            Input the source point
            
            Point2d destPt: 
            Input the destination point
        """
        pass
    
    
    def EraseFromDb(self):
        """
        EraseFromDb -> void
        
        """
        pass
    
    
    def GetMeshPointMap(self):
        """
        GetMeshPointMap -> MeshPointMap
            
            int index: 
            Input the index to insert at
        """
        pass
    
    
    def GetMeshPointMaps(self):
        """
        GetMeshPointMaps -> MeshPointMaps
        
        """
        pass
    
    
    def PostToDb(self):
        """
        PostToDb -> ObjectId
        
        """
        pass
    
    
    def ResetMeshPointMaps(self):
        """
        ResetMeshPointMaps -> void
        
        """
        pass
    
    
    def SetMeshPointMaps(self):
        """
        SetMeshPointMaps -> void
            
            Point2dCollection sourcePts: 
            Input source points collection
            
            Point2dCollection destPts: 
            Input destination points collection
        """
        pass
    
    
    def TransformFromLonLatAlt(self):
        """
        TransformFromLonLatAlt -> Point3d
        
        """
        pass
    
    
    def TransformToLonLatAlt(self):
        """
        TransformToLonLatAlt(Point3d) -> Point3d
            
            Point3d dwgPt: 
            Input dwg point (x, y, z)
        TransformToLonLatAlt(double, double, double) -> GeoDataLonLatAltInfo
            
            double y: 
            Input y coordinate of dwg point
            
            double z: 
            Input z coordinate of dwg point
        """
        pass
    
    
    def UpdateTransformationMatrix(self):
        """
        UpdateTransformationMatrix -> void
        
        """
        pass
    
    
    BlockTableRecordId = None
    
    
    CoordinateProjectionRadius = None
    
    
    DoSeaLevelCorrection = None
    
    
    GeoRSSTag = None
    
    
    NorthDirection = None
    
    
    NorthDirectionVector = None
    
    
    NumMeshPoints = None
    
    
    ScaleEstimationMethod = None
    
    
    ScaleFactor = None
    
    
    SeaLevelElevation = None
    
    
    UpDirection = None
    
    pass

class GeoPositionMarker(object):
    """
    
    GeoPositionMarker()()
    
    
    GeoPositionMarker(Point3d, double, double)()
    
    
    """
    EnableFrameText = None
    
    
    GeoPosition = None
    
    
    LandingGap = None
    
    
    MText = None
    
    
    MTextVisible = None
    
    
    Normal = None
    
    
    Notes = None
    
    
    Position = None
    
    
    Radius = None
    
    
    Text = None
    
    
    TextAlignmentType = None
    
    
    TextStyle = None
    
    pass

class GeomRef(object):
    """
    
    """
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    IsEmpty = None
    
    
    IsValid = None
    
    pass

class GeomapImage(object):
    """
    
    GeomapImage()
    """
    def GetImageVertices(self):
        """
        GetImageVertices -> Point3dCollection
        
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices -> Point3dCollection
        
        """
        pass
    
    
    def ImageSize(self):
        """
        ImageSize -> Vector2d
        
        """
        pass
    
    
    def UpdateMapImage(self):
        """
        UpdateMapImage -> bool
            
            [MarshalAs(UnmanagedType.U1)] bool Reset: 
            Input Boolean to indicate whether to recapture the image in optimal resolution to the screen. If true, the L
        """
        pass
    
    
    BottomLeftPoint = None
    
    
    Brightness = None
    
    
    Contrast = None
    
    
    Fade = None
    
    
    Height = None
    
    
    ImageBottomLeftPoint = None
    
    
    ImageHeight = None
    
    
    ImageWidth = None
    
    
    IsOutOfDate = None
    
    
    LOD = None
    
    
    MapType = None
    
    
    Resolution = None
    
    
    Width = None
    
    pass

class GeometricalConstraint(object):
    """
    
    """
    class ConstraintType():
        Horizontal = None
        Vertical = None
        Parallel = None
        Perpendicular = None
        Normal = None
        Collinear = None
        Coincident = None
        Concentric = None
        Tangent = None
        EqualRadius = None
        EqualLength = None
        Symmetric = None
        Smooth = None
        Fix = None
    
    
    def Deactivate(self):
        """
        Deactivate -> void
        
        """
        pass
    
    
    def GetConnectedHelpParameterFor(self):
        """
        GetConnectedHelpParameterFor -> HelpParameter
            
            ConstrainedGeometry consGeom: 
            The reference to ConstrainedGeometry object.
        """
        pass
    
    
    def Reactivate(self):
        """
        Reactivate -> void
        
        """
        pass
    
    
    ConnectedGeometries = None
    
    
    ConnectedHelpParameters = None
    
    
    IsActive = None
    
    
    IsEnabled = None
    
    
    IsImplied = None
    
    
    IsInternal = None
    
    
    OwningCompositeConstraint = None
    
    pass

class GeometryOverrule(object):
    """
    
    """
    def GetGeomExtents(self):
        """
        GetGeomExtents -> Extents3d
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(Entity, Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Plane, Point3dCollection, IntPtr, IntPtr) -> void
        
        IntersectWith(Entity, Entity, Autodesk.AutoCAD.DatabaseServices.Intersect, Point3dCollection, IntPtr, IntPtr) -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class GradientBackground(object):
    """
    
    GradientBackground()
    """
    ColorBottom = None
    
    
    ColorMiddle = None
    
    
    ColorTop = None
    
    
    Height = None
    
    
    Horizon = None
    
    
    Rotation = None
    
    pass

class GradientColor(object):
    """
    
    GradientColor
        Color color : Input color making up the parameters
        float value : Input float representing the interpolation values defining the gradient
    """
    def get_Color(self):
        """
        get_Color -> Color
        
        """
        pass
    
    
    def get_Value(self):
        """
        get_Value -> float
        
        """
        pass
    
    pass

class GradientPatternType():
    PreDefinedGradient = None
    UserDefinedGradient = None

class Graph(object):
    """
    
    Graph
        GraphNode root : Input root node. Default is NULL.
    """
    def AddEdge(self):
        """
        AddEdge -> void
            
            GraphNode from: 
            Input the node to begin the edge at
            
            GraphNode toPointer: 
            Input the node to end the edge at
        """
        pass
    
    
    def AddNode(self):
        """
        AddNode -> void
            
            GraphNode nodeToAdd: 
            Node to add
        """
        pass
    
    
    def BreakCycleEdge(self):
        """
        BreakCycleEdge -> void
            
            GraphNode from: 
            Input node that the edge begins at
            
            GraphNode toPointer: 
            Input node that the edge ends at
        """
        pass
    
    
    def ClearAll(self):
        """
        ClearAll -> void
            
            byte flags: 
            Input flag values to clear for all nodes in the graph
        """
        pass
    
    
    def DelNode(self):
        """
        DelNode -> void
            
            GraphNode nodeToDelete: 
            Node to delete
        """
        pass
    
    
    def FindCycles(self):
        """
        FindCycles -> bool
            
            GraphNode start: 
            Input node to begin the search for cycles at. Usually defaulted to NULL.
        """
        pass
    
    
    def GetOutgoing(self):
        """
        GetOutgoing -> GraphNodeCollection
        
        """
        pass
    
    
    def Node(self):
        """
        Node -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    def SetNodeGrowthRate(self):
        """
        SetNodeGrowthRate -> void
            
            int rate: 
            Number of nodes to allocate at once
        """
        pass
    
    
    IsEmpty = None
    
    
    NumNodes = None
    
    
    RootNode = None
    
    pass

class GraphNode(object):
    """
    
    GraphNode()
    """
    def AddRefTo(self):
        """
        AddRefTo -> void
            
            GraphNode outGoingNode: 
            Input to the outgoing node
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
            
            byte flags: 
            Input flag values to clear for this node
        """
        pass
    
    
    def CycleIn(self):
        """
        CycleIn -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def CycleOut(self):
        """
        CycleOut -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def DisconnectAll(self):
        """
        DisconnectAll -> void
        
        """
        pass
    
    
    def In(self):
        """
        In -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def IsMarkedAs(self):
        """
        IsMarkedAs -> bool
            
            int flag: 
            Input flag values to check for this node
        """
        pass
    
    
    def MarkAs(self):
        """
        MarkAs -> void
            
            byte flags: 
            Input flag values to set for this node
        """
        pass
    
    
    def MarkTree(self):
        """
        MarkTree -> void
            
            byte flags: 
            Input flag values to set for this node and all nested out nodes
            
            GraphNodeCollection appendedTo: 
            Input collection that this node and all nested out nodes should optionally be appended to
        """
        pass
    
    
    def Out(self):
        """
        Out -> GraphNode
            
            int index: 
            Input desired node index
        """
        pass
    
    
    def RemoveRefTo(self):
        """
        RemoveRefTo -> void
            
            GraphNode nodeToRemoveReference: 
            Input node to remove reference of
        """
        pass
    
    
    def SetEdgeGrowthRate(self):
        """
        SetEdgeGrowthRate -> void
            
            int outEdgeRate: 
            Number of outgoing edges allocated at one time
            
            int inEdgeRate: 
            Number of incoming edges allocated at one time
        """
        pass
    
    
    Data = None
    
    
    IsCycleNode = None
    
    
    NextCycleNode = None
    
    
    NumCycleIn = None
    
    
    NumCycleOut = None
    
    
    NumIn = None
    
    
    NumOut = None
    
    
    Owner = None
    
    pass

class GraphNodeCollection(object):
    """
    
    GraphNodeCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            GraphNode value: 
            Item to add.
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
            
            GraphNode value: 
            Object to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            GraphNode[] array: 
            Array to copy from
            
            int index: 
            Zero-based index to start from
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
            
            GraphNode value: 
            Item to seek
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Location to insert
            
            GraphNode value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            GraphNode value: 
            Item to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index to remove from
        """
        pass
    
    
    Count = None
    
    pass

class GraphicsMetafileType():
    NoMetafile = None
    BoundingBox = None
    FullGraphics = None

class GridLineStyle():
    Double = 2
    Single = 1

class GridLineType():
    AllGridLines = 0x3f
    HorizontalBottom = 4
    HorizontalGridLines = 7
    HorizontalInside = 2
    HorizontalTop = 1
    InnerGridLines = 0x12
    InvalidGridLine = 0
    OuterGridLines = 0x2d
    VerticalGridLines = 0x38
    VerticalInside = 0x10
    VerticalLeft = 8
    VerticalRight = 0x20

class GridProperties():
    Color = 8
    DoubleLineSpacing = 0x20
    Invalid = 0
    LineStyle = 1
    Linetype = 4
    LineWeight = 2
    Visibility = 0x10

class GridPropertyParameter(object):
    """
    
    """

    pass

class GripData(object):
    """
    
    """
    class Context():
        MultiHotGrip = 2
        SharedGrip = 1
    
    
    class DrawType():
        WarmGrip = None
        HoverGrip = None
        HotGrip = None
        DragImageGrip = None
    
    
    class ReturnValue():
        Ok = None
        Failure = None
        NoRedrawGrip = None
        GripHotToWarm = None
        GetNewGripPoints = None
    
    
    class Status():
        GripStart = None
        GripEnd = None
        GripAbort = None
        Stretch = None
        Move = None
        Rotate = None
        Scale = None
        Mirror = None
        DimFocusChanged = None
        PopUpMenu = None
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetHotGripDimensionData(self):
        """
        GetHotGripDimensionData -> DynamicDimensionDataCollection
        
        """
        pass
    
    
    def GetHoverDimensionData(self):
        """
        GetHoverDimensionData -> DynamicDimensionDataCollection
        
        """
        pass
    
    
    def GetTooltip(self):
        """
        GetTooltip -> string
        
        """
        pass
    
    
    def OnGripStatusChanged(self):
        """
        OnGripStatusChanged -> void
        
        """
        pass
    
    
    def OnHotGrip(self):
        """
        OnHotGrip -> ReturnValue
        
        """
        pass
    
    
    def OnHover(self):
        """
        OnHover -> ReturnValue
        
        """
        pass
    
    
    def OnRightClick(self):
        """
        OnRightClick -> IEnumerable<IMenuItem>
        
        """
        pass
    
    
    def ViewportDraw(self):
        """
        ViewportDraw -> bool
        
        """
        pass
    
    
    def WorldDraw(self):
        """
        WorldDraw -> bool
        
        """
        pass
    
    
    AlternateBasePoint = None
    
    
    DrawAtDragImageGripPoint = None
    
    
    ForcedPickOn = None
    
    
    GizmosEnabled = None
    
    
    GripPoint = None
    
    
    HotGripInvokesRightClick = None
    
    
    IsPerViewport = None
    
    
    ModeKeywordsDisabled = None
    
    
    RubberBandLineDisabled = None
    
    
    SkipWhenShared = None
    
    
    TriggerGrip = None
    
    pass

class GripMode(object):
    """
    
    GripMode()
    """
    class ActionType():
        DragOn = None
        Immediate = None
        Command = None
    
    
    class CursorType():
        CursorNone = None
        CursorCrosshairPlus = None
        CursorCrosshairMinus = None
        CursorCrosshairCurve = None
        CursorCrosshairLine = None
        CursorCrosshairAngle = None
    
    
    class ModeIdentifier():
        CustomStart = 100
        Move = 1
        None = 0
    
    
    Action = None
    
    
    CLIDisplayString = None
    
    
    CLIKeywordList = None
    
    
    CLIPromptString = None
    
    
    CommandString = None
    
    
    Cursor = None
    
    
    DisplayString = None
    
    
    ModeId = None
    
    
    ToolTip = None
    
    pass

class GripModeCollection(object):
    """
    
    GripModeCollection()
    """
    def Add(self):
        """
        Add -> void
            
            Autodesk.AutoCAD.DatabaseServices.GripMode gripMode: 
            The mode object to add.
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
            
            Autodesk.AutoCAD.DatabaseServices.GripMode gripMode: 
            The gripMode object to test.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator<Autodesk.AutoCAD.DatabaseServices.GripMode>
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> bool
            
            Autodesk.AutoCAD.DatabaseServices.GripMode gripMode: 
            The gripMode object to remove.
        """
        pass
    
    
    Count = None
    
    
    IsReadOnly = None
    
    pass

class GripOverrule(object):
    """
    
    """
    def GetGripPoints(self):
        """
        GetGripPoints(Entity, GripDataCollection, double, int, Vector3d, GetGripPointsFlags) -> void
        
        GetGripPoints(Entity, Point3dCollection, IntegerCollection, IntegerCollection) -> void
        
        """
        pass
    
    
    def GetStretchPoints(self):
        """
        GetStretchPoints -> void
        
        """
        pass
    
    
    def MoveGripPointsAt(self):
        """
        MoveGripPointsAt(Entity, GripDataCollection, Vector3d, MoveGripPointsFlags) -> void
        
        MoveGripPointsAt(Entity, IntegerCollection, Vector3d) -> void
        
        """
        pass
    
    
    def MoveStretchPointsAt(self):
        """
        MoveStretchPointsAt -> void
        
        """
        pass
    
    
    def OnGripStatusChanged(self):
        """
        OnGripStatusChanged -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class GripStatus():
    GripsDone = None
    GripsToBeDeleted = None
    DimDataToBeDeleted = None

class GroundPlaneBackground(object):
    """
    
    GroundPlaneBackground()
    """
    ColorGroundPlaneFar = None
    
    
    ColorGroundPlaneNear = None
    
    
    ColorSkyHorizon = None
    
    
    ColorSkyZenith = None
    
    
    ColorUndergroundAzimuth = None
    
    
    ColorUndergroundHorizon = None
    
    pass

class Group(object):
    """
    
    Group()()
    
    
    Group(string, [MarshalAs(UnmanagedType.U1)] bool)
        string description : Input null terminated string describing the group
        [MarshalAs(UnmanagedType.U1)] bool selectable : Input Boolean value indicating whether the group is selectable or not
    
    
    """
    def Append(self):
        """
        Append(ObjectId) -> void
            
            ObjectId id: 
            Input objectId of the object to be appended to group
        Append(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input objectId collection containing the objectIds of the objects to be appended
        """
        pass
    
    
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def GetAllEntityIds(self):
        """
        GetAllEntityIds -> ObjectId()
        
        """
        pass
    
    
    def GetIndex(self):
        """
        GetIndex -> Integer
            
            ObjectId id: 
            Input objectId of the object whose index is being queried
        """
        pass
    
    
    def Has(self):
        """
        Has -> bool
            
            Entity entity: 
            Input the entity being looked up
        """
        pass
    
    
    def InsertAt(self):
        """
        InsertAt(int, ObjectId) -> void
            
            int index: 
            Input insertion index
            
            ObjectId id: 
            Input objectId of the object to be inserted
        InsertAt(int, ObjectIdCollection) -> void
            
            int index: 
            Input insertion index
            
            ObjectIdCollection ids: 
            Input objectId collection containing objects to be inserted
        """
        pass
    
    
    def Prepend(self):
        """
        Prepend(ObjectId) -> void
            
            ObjectId id: 
            Input objectId of the object to be prepended to group
        Prepend(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input objectId collection containing the objectIds of the objects to be prepended
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ObjectId) -> void
            
            ObjectId id: 
            Input objectId of the object to be removed
        Remove(ObjectIdCollection) -> void
            
            ObjectIdCollection ids: 
            Input array of objectIds of objects to be removed from the group
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt(int) -> void
            
            int index: 
            Input index of the object to be removed
        RemoveAt(int, ObjectIdCollection) -> void
            
            int index: 
            Input starting index of the objects to be removed
            
            ObjectIdCollection ids: 
            Input objectId array of objects to be removed after start index
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            ObjectId oldId: 
            Input objectId of the object to be removed from the group
            
            ObjectId newId: 
            Input objectId of the object to be added to the group in place of oldId
        """
        pass
    
    
    def Reverse(self):
        """
        Reverse -> void
        
        """
        pass
    
    
    def SetAnonymous(self):
        """
        SetAnonymous -> void
        
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input Color object representing the color to be set
        """
        pass
    
    
    def SetColorIndex(self):
        """
        SetColorIndex -> void
            
            int color: 
            Input AutoCAD color index to be set for entities in the group (color index must be in the range 0 to 256)
        """
        pass
    
    
    def SetHighlight(self):
        """
        SetHighlight -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input Boolean indicating whether to highlight or not
        """
        pass
    
    
    def SetLayer(self):
        """
        SetLayer(ObjectId) -> void
            
            ObjectId value: 
            Input objectId of the layer to use
        SetLayer(string) -> void
            
            string value: 
            Input null terminated string that is the name of the new layer
        """
        pass
    
    
    def SetLinetype(self):
        """
        SetLinetype(ObjectId) -> void
            
            ObjectId value: 
            Input objectId of the line type
        SetLinetype(string) -> void
            
            string value: 
            Input objectId null terminated string that is the name of the new line type
        """
        pass
    
    
    def SetLinetypeScale(self):
        """
        SetLinetypeScale -> void
            
            double value: 
            Input new value for the line type scale
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input enum value for visibility
        """
        pass
    
    
    def Transfer(self):
        """
        Transfer -> void
            
            int fromIndex: 
            Input start index to transfer from
            
            int toIndex: 
            Input start index to transfer to
            
            int numItems: 
            Input number of items to transfer
        """
        pass
    
    
    Description = None
    
    
    IsAnonymous = None
    
    
    IsNotAccessible = None
    
    
    Name = None
    
    
    NumEntities = None
    
    
    Selectable = None
    
    pass

class GsMarkType():
    ArrowMark = 1
    BlockMark = 0x3a9c
    DoglegMark = 0x2711
    LeaderLineMark = 0x1389
    MTextMark = 0x3a99
    MTextUnderLineMark = 0x3a9a
    None = 0
    ToleranceMark = 0x3a9b

class Handle(object):
    """
    
    Handle
        long value : Input all 64 bits of the handle
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
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
    
    
    IsOne = None
    
    
    Value = None
    
    pass

class Hatch(object):
    """
    
    Hatch()
    """
    def AppendLoop(self):
        """
        AppendLoop(HatchLoop) -> void
            
            HatchLoop hatchLoop: 
            Input type of loop
        AppendLoop(HatchLoopTypes, Curve2dCollection, IntegerCollection) -> void
            
            HatchLoopTypes loopType: 
            Input loop type.
            
            Curve2dCollection edgePtrCollection: 
            Input set of curve 2d.
            
            IntegerCollection edgeTypeCollection: 
            Input set of enumerated edge types.
        AppendLoop(HatchLoopTypes, ObjectIdCollection) -> void
            
            HatchLoopTypes loopType: 
            Input loop type
            
            ObjectIdCollection dbObjIds: 
            Input set of object IDs
        AppendLoop(HatchLoopTypes, Point2dCollection, DoubleCollection) -> void
            
            HatchLoopTypes loopType: 
            Input type of loop.
            
            Point2dCollection vertexCollection: 
            Input set of point 2d.
            
            DoubleCollection bulgeCollection: 
            Input set of double values.
        """
        pass
    
    
    def EvaluateGradientColorAt(self):
        """
        EvaluateGradientColorAt -> Autodesk.AutoCAD.Colors.Color
            
            float value: 
            Input normalized value, [0.0...1.0], at which to evaluate the gradient color
        """
        pass
    
    
    def EvaluateHatch(self):
        """
        EvaluateHatch -> void
            
            [MarshalAs(UnmanagedType.U1)] bool underEstimateNumLines: 
            If true, underestimates the count before deciding to abort. That is, if Hatch::EvaluateHatch(true) is used, the function will abort if the count is in excess of 100,000.
        """
        pass
    
    
    def GetAssociatedObjectIds(self):
        """
        GetAssociatedObjectIds -> ObjectIdCollection
        
        """
        pass
    
    
    def GetAssociatedObjectIdsAt(self):
        """
        GetAssociatedObjectIdsAt -> ObjectIdCollection
            
            int loopIndex: 
            Input index for the selected loop
        """
        pass
    
    
    def GetGradientColors(self):
        """
        GetGradientColors -> GradientColor()
        
        """
        pass
    
    
    def GetHatchLineDataAt(self):
        """
        GetHatchLineDataAt -> Line2d
            
            int index: 
            Input number at which the hatch line data will be returned
        """
        pass
    
    
    def GetHatchLinesData(self):
        """
        GetHatchLinesData -> Line2dCollection
        
        """
        pass
    
    
    def GetLoopAt(self):
        """
        GetLoopAt -> HatchLoop
            
            int loopIndex: 
            Input index of selected loop
        """
        pass
    
    
    def GetPatternDefinitionAt(self):
        """
        GetPatternDefinitionAt -> PatternDefinition
            
            int index: 
            Input pattern index
        """
        pass
    
    
    def InsertLoopAt(self):
        """
        InsertLoopAt(int, HatchLoop) -> void
            
            int loopIndex: 
            Input index for the selected loop
            
            HatchLoop hatchLoop: 
            Input loop type
        InsertLoopAt(int, HatchLoopTypes, ObjectIdCollection) -> void
            
            int loopIndex: 
            Input index for the selected loop
            
            HatchLoopTypes loopType: 
            Input loop type
            
            ObjectIdCollection dbObjIds: 
            Input set of object IDs
        """
        pass
    
    
    def LoopTypeAt(self):
        """
        LoopTypeAt -> HatchLoopTypes
            
            int loopIndex: 
            Input index of the selected loop
        """
        pass
    
    
    def RemoveAssociatedObjectIds(self):
        """
        RemoveAssociatedObjectIds -> void
        
        """
        pass
    
    
    def RemoveLoopAt(self):
        """
        RemoveLoopAt -> void
            
            int loopIndex: 
            Input index for the selected loop
        """
        pass
    
    
    def SetGradientColors(self):
        """
        SetGradientColors -> void
            
            GradientColor[] value: 
            Input array of floats representing the interpolation values defining the gradient
        """
        pass
    
    
    def SetGradient(self):
        """
        SetGradient -> void
            
            Autodesk.AutoCAD.DatabaseServices.GradientPatternType gradientType: 
            Input gradient type
            
            string gradientName: 
            Input name of the gradient to apply
        """
        pass
    
    
    def SetHatchPattern(self):
        """
        SetHatchPattern -> void
            
            Autodesk.AutoCAD.DatabaseServices.HatchPatternType patternType: 
            Input enumerated number of pattern type
            
            string patternName: 
            Input name of the pattern
        """
        pass
    
    
    Area = None
    
    
    Associative = None
    
    
    BackgroundColor = None
    
    
    Elevation = None
    
    
    GradientAngle = None
    
    
    GradientName = None
    
    
    GradientOneColorMode = None
    
    
    GradientShift = None
    
    
    GradientType = None
    
    
    HatchObjectType = None
    
    
    HatchStyle = None
    
    
    IsGradient = None
    
    
    IsHatch = None
    
    
    IsSolidFill = None
    
    
    Normal = None
    
    
    NumberOfHatchLines = None
    
    
    NumberOfLoops = None
    
    
    NumberOfPatternDefinitions = None
    
    
    Origin = None
    
    
    PatternAngle = None
    
    
    PatternDouble = None
    
    
    PatternName = None
    
    
    PatternScale = None
    
    
    PatternSpace = None
    
    
    PatternType = None
    
    
    ShadeTintValue = None
    
    pass

class HatchEdgeType():
    CircularArc = 2
    EllipticalArc = 3
    Line = 1
    Spline = 4

class HatchLoop(object):
    """
    
    HatchLoop
        HatchLoopTypes loopType : Input type of loop
    """
    Curves = None
    
    
    IsPolyline = None
    
    
    LoopType = None
    
    
    Polyline = None
    
    pass

class HatchLoopTypes():
    Default = 0
    Derived = 4
    Duplicate = 0x100
    External = 1
    NotClosed = 0x20
    Outermost = 0x10
    Polyline = 2
    SelfIntersecting = 0x40
    Textbox = 8
    TextIsland = 0x80

class HatchObjectType():
    HatchObject = None
    GradientObject = None

class HatchPatternType():
    UserDefined = None
    PreDefined = None
    CustomDefined = None

class HatchStyle():
    Normal = None
    Outer = None
    Ignore = None

class Helix(object):
    """
    
    Helix()
    """
    def CreateHelix(self):
        """
        CreateHelix -> void
        
        """
        pass
    
    
    def GetAxisPoint(self):
        """
        GetAxisPoint -> Point3d
        
        """
        pass
    
    
    def SetAxisPoint(self):
        """
        SetAxisPoint -> void
            
            Point3d axisPoint: 
            Input the 3D point where the axis starts
            
            [MarshalAs(UnmanagedType.U1)] bool moveStartPoint: 
            Input Boolean indicating whether to relocate the start point by the same offset that the axis point moved
        """
        pass
    
    
    AxisVector = None
    
    
    BaseRadius = None
    
    
    Constrain = None
    
    
    Height = None
    
    
    StartPoint = None
    
    
    TopRadius = None
    
    
    TotalLength = None
    
    
    TurnHeight = None
    
    
    Turns = None
    
    
    TurnSlope = None
    
    
    Twist = None
    
    pass

class HelpParameter(object):
    """
    
    HelpParameter()
    """
    ConnectedConstraint = None
    
    
    ConnectedEqualparamConstraints = None
    
    
    ConnectedGeometry = None
    
    
    Value = None
    
    pass

class HighlightOverrule(object):
    """
    
    """
    def Highlight(self):
        """
        Highlight -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def Unhighlight(self):
        """
        Unhighlight -> void
        
        """
        pass
    
    pass

class HighlightStateOverrule(object):
    """
    
    """
    def HighlightState(self):
        """
        HighlightState -> HighlightStyle
        
        """
        pass
    
    
    def PopHighlight(self):
        """
        PopHighlight -> void
        
        """
        pass
    
    
    def PushHighlight(self):
        """
        PushHighlight -> void
        
        """
        pass
    
    pass

class HorizontalConstraint(object):
    """
    
    HorizontalConstraint()
    """

    pass

class HostApplicationServices(object):
    """
    
    """
    def FatalError(self):
        """
        FatalError -> void
            
            string message: 
            The error message.
        """
        pass
    
    
    def GetEnvironmentVariable(self):
        """
        GetEnvironmentVariable -> string
        
        """
        pass
    
    
    def GetRemoteFile(self):
        """
        GetRemoteFile -> string
            
            Uri url: 
            Input URL
            
            [MarshalAs(UnmanagedType.U1)] bool ignoreCache: 
            Input Boolean indicating whether to download the file even if it has be cached earlier in the session
        """
        pass
    
    
    def GetUrl(self):
        """
        GetUrl -> Uri
            
            string localFile: 
            Input local file
        """
        pass
    
    
    def IsUrl(self):
        """
        IsUrl -> bool
            
            string filePath: 
            Input string to be evaluated
        """
        pass
    
    
    def LoadApplication(self):
        """
        LoadApplication -> void
            
            string appName: 
            Input null-terminated string which is the application name (as set in the system registry) of the ObjectARX module to load
            
            ApplicationLoadReasons why: 
            Input LoadReasons values to use during this load
            
            [MarshalAs(UnmanagedType.U1)] bool printIt: 
            Input Boolean indicating whether or not to print load status message
            
            [MarshalAs(UnmanagedType.U1)] bool asCmd: 
            Input Boolean indicating whether to load the application as if by user command
        """
        pass
    
    
    def NotifyCorruptDrawingFoundOnOpen(self):
        """
        NotifyCorruptDrawingFoundOnOpen -> bool
            
            ObjectId id: 
            The ID of the corrupt DB object that cannot be read.
            
            Autodesk.AutoCAD.Runtime.ErrorStatus es: 
            The return code of the attempt to read in the corrupt DB object.
        """
        pass
    
    
    def PutRemoteFile(self):
        """
        PutRemoteFile -> void
            
            Uri url: 
            Input URL to which to upload file
            
            string localFile: 
            Input local file to upload
        """
        pass
    
    
    def UserBreak(self):
        """
        UserBreak -> bool
        
        """
        pass
    
    
    def FindFile(self):
        """
        FindFile -> string
            
            string fileName: 
            Given name of the file to find.
            
            Database database: 
            This will give you the path to the DWG file associated with the database, which may also be searched for the requested file. If this file search is not related to a database, database will be NULL.
            
            Autodesk.AutoCAD.DatabaseServices.FindFileHint hint: 
            Caller may pass you a hint, that you may choose to use to narrow your search.
            Default: 
            Any file
            FontFile: 
            Could be either a shape or TrueType font
            CompiledShapeFile: 
            A shape font file
            TrueTypeFontFile: 
            A TrueType font file
            EmbeddedImageFile: 
            An image file
            XRefDrawing: 
            A drawing template
            PatternFile: 
            A hatch pattern file
            ARXApplication: 
            An ObjectARX program
        """
        pass
    
    
    def GetPassword(self):
        """
        GetPassword -> string
            
            string dwgName: 
            Name of the drawing file that is requiring a password
            
            Autodesk.AutoCAD.DatabaseServices.PasswordOptions options: 
            Boolean indicating whether dwgName refers to an xref'd drawing
        """
        pass
    
    
    AllUsersRootFolder = None
    
    
    AlternateFontName = None
    
    
    ColorBookLocation = None
    
    
    CompanyName = None
    
    
    Current = None
    
    
    FontMapFileName = None
    
    
    LocalRootFolder = None
    
    
    MachineRegistryProductRootKey = None
    
    
    ModelerFlavor = None
    
    
    Product = None
    
    
    Program = None
    
    
    releaseMarketVersion = None
    
    
    RoamableRootFolder = None
    
    
    UserRegistryProductRootKey = None
    
    
    WorkingDatabase = None
    
    pass

class HyperLink(object):
    """
    
    HyperLink()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object other: 
            Object to compare
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    Description = None
    
    
    DisplayString = None
    
    
    IsOutermostContainer = None
    
    
    Name = None
    
    
    NestedLevel = None
    
    
    SubLocation = None
    
    pass

class HyperLinkCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            HyperLink value: 
            Item to add.
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
            
            HyperLink value: 
            Item to check for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            HyperLink[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
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
            
            HyperLink value: 
            Item to look for.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Location to insert at
            
            HyperLink value: 
            Item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            HyperLink value: 
            Object to remove.
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of object to remove.
        """
        pass
    
    
    Count = None
    
    pass

class IBLBackground(object):
    """
    
    IBLBackground()
    """
    DisplayImage = None
    
    
    Enable = None
    
    
    IBLImageName = None
    
    
    Rotation = None
    
    
    SecondaryBackground = None
    
    pass

class ITextEditorSelectable(object):
    """
    
    """

    pass

class IdMapping(object):
    """
    
    IdMapping()
    """
    def Add(self):
        """
        Add -> void
            
            IdPair pairToAdd: 
            Input IdPair to add
        """
        pass
    
    
    def Change(self):
        """
        Change -> void
        
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ObjectId key: 
            Input key to look for
        """
        pass
    
    
    def Delete(self):
        """
        Delete -> void
            
            ObjectId key: 
            Input objectId which is the key of the ID pair to be deleted from the map
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def Lookup(self):
        """
        Lookup -> IdPair
            
            ObjectId key: 
            Input key to look for
        """
        pass
    
    
    DeepCloneContext = None
    
    
    DestinationDatabase = None
    
    
    DuplicateRecordCloning = None
    
    
    OriginalDatabase = None
    
    pass

class IdMappingEventArgs(object):
    """
    
    """
    IdMapping = None
    
    pass

class IdPair(object):
    """
    
    IdPair
        ObjectId key : Input objectId to use as the key
        ObjectId value : Input objectId to use as the value
        [MarshalAs(UnmanagedType.U1)] bool isCloned : Input Boolean indicating if it has been cloned already
        [MarshalAs(UnmanagedType.U1)] bool isPrimary : Input Boolean indicating if it is a primary object
        [MarshalAs(UnmanagedType.U1)] bool isOwnerTranslated : Input Boolean indicating if its owner has already been translated
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Culture-specific format
        """
        pass
    
    
    IsCloned = None
    
    
    IsOwnerTranslated = None
    
    
    IsPrimary = None
    
    
    Key = None
    
    
    Value = None
    
    pass

class Image(object):
    """
    
    """

    pass

class ImageBackground(object):
    """
    
    ImageBackground()
    """
    FitToScreen = None
    
    
    ImageFileName = None
    
    
    MaintainAspectRatio = None
    
    
    Offset = None
    
    
    Scale = None
    
    
    UseTiling = None
    
    pass

class ImageDisplayOptions():
    Clip = 4
    Show = 1
    ShowUnaligned = 2
    Transparent = 8

class ImageQuality():
    Draft = 0
    High = 1
    Invalid = -1

class ImplicitPointType():
    StartImplicit = None
    EndImplicit = None
    MidImplicit = None
    CenterImplicit = None
    DefineImplicit = None

class IndexCreation():
    NoIndex = None
    IndexByLayer = None
    IndexSpatially = None

class InterferenceProtocolExtension(object):
    """
    
    """
    def CreateInterferenceObjects(self):
        """
        CreateInterferenceObjects -> Entity()
            
            Entity ent1: 
            Input entity 1
            
            Entity ent2: 
            Input entity 2
            
            int flags: 
            Input interference flags
        """
        pass
    
    pass

class Intersect():
    OnBothOperands = None
    ExtendThis = None
    ExtendArgument = None
    ExtendBoth = None

class ItemLocator(object):
    """
    
    ItemLocator
        int itemIndex : The input Index relative to the first item. itemIndex >= 0.
        int rowIndex : The input Index relative to the first row. rowIndex >= 0.
        int levelIndex : The input Index relative to the first level. levelIndex >=0.
    """
    ItemIndex = None
    
    
    LevelIndex = None
    
    
    RowIndex = None
    
    pass

class JoinStyle():
    StyleNone = None
    StyleRound = None
    StyleAngle = None
    StyleFlat = None

class LampColorPreset():
    D65White = None
    Fluorescent = None
    CoolWhite = None
    WhiteFluorescent = None
    DaylightFluorescent = None
    Incandescent = None
    Xenon = None
    Halogen = None
    Quartz = None
    MetalHalide = None
    Mercury = None
    PhosphorMercury = None
    HighPressureSodium = None
    LowPressureSodium = None
    Custom = None

class LampColorType():
    Kelvin = None
    Preset = None

class LayerEvaluation():
    NoNewLayerEvaluation = None
    EvalNewXrefLayers = None
    EvalAllNewLayers = None

class LayerStateManager(object):
    """
    
    LayerStateManager
        Database database : Database association constructor.
    """
    def CompareLayerStateToDb(self):
        """
        CompareLayerStateToDb -> bool
            
            string name: 
            Input name of layer state to be compared to the drawing.
            
            ObjectId idVp: 
            Input object ID of the viewport whose VPLAYER settings are to be used when comparing.
        """
        pass
    
    
    def DeleteLayerState(self):
        """
        DeleteLayerState -> void
            
            string name: 
            Input layer state name to delete
        """
        pass
    
    
    def ExportLayerState(self):
        """
        ExportLayerState -> void
            
            string nameToExport: 
            Input layer state name to export
            
            string fileName: 
            Input filename to export layer state to
        """
        pass
    
    
    def GetLayerStateDescription(self):
        """
        GetLayerStateDescription -> string
            
            string name: 
            Input layer state whose description is to be retrieved
        """
        pass
    
    
    def GetLayerStateLayers(self):
        """
        GetLayerStateLayers -> ArrayList
            
            string name: 
            Input the name of the layer state to query
            
            [MarshalAs(UnmanagedType.U1)] bool bInvert: 
            Input if true, the returned array will contain the names of the layers in the current drawing that are NOT saved in the layer state.
        """
        pass
    
    
    def GetLayerStateMask(self):
        """
        GetLayerStateMask -> LayerStateMasks
            
            string name: 
            Input layer state name
        """
        pass
    
    
    def GetLayerStateNames(self):
        """
        GetLayerStateNames -> ArrayList
            
            [MarshalAs(UnmanagedType.U1)] bool bIncludeHidden: 
            Input flag to include names of hidden layer states in array.
            
            [MarshalAs(UnmanagedType.U1)] bool bIncludeXref: 
            Input flag to include XRefs
        """
        pass
    
    
    def HasLayerState(self):
        """
        HasLayerState -> bool
            
            string name: 
            Input layer state name
        """
        pass
    
    
    def ImportLayerState(self):
        """
        ImportLayerState -> void
            
            string fileName: 
            Input file to extract layer states from
        """
        pass
    
    
    def ImportLayerStateFromDb(self):
        """
        ImportLayerStateFromDb -> void
            
            string name: 
            Input the name of the layer state to be imported
            
            Database database: 
            Input a pointer to a valid, readable database from which the layer state is to be imported.
        """
        pass
    
    
    def LayerStateHasViewportData(self):
        """
        LayerStateHasViewportData -> bool
            
            string name: 
            Input layer state to be interrogated
        """
        pass
    
    
    def LayerStatesDictionaryId(self):
        """
        LayerStatesDictionaryId -> ObjectId
            
            [MarshalAs(UnmanagedType.U1)] bool createIfNotPresent: 
            Input flag controlling dictionary creation
        """
        pass
    
    
    def RenameLayerState(self):
        """
        RenameLayerState -> void
            
            string name: 
            Input existing layer state name
            
            string newName: 
            Input new layer state name
        """
        pass
    
    
    def RestoreLayerState(self):
        """
        RestoreLayerState -> void
            
            string name: 
            Input name of layer state to make current
            
            ObjectId id: 
            Input object ID of the viewport whose VPLAYER setting is to be updated with the viewport data stored
            
            int undefinedLayerStatePolicy: 
            Input value that indicates whether to handle undefined layers
            
            LayerStateMasks clientMask: 
            Input layer attribute mask
        """
        pass
    
    
    def SaveLayerState(self):
        """
        SaveLayerState -> void
            
            string name: 
            Input name of layer state to save
            
            LayerStateMasks mask: 
            Input mask to apply to layer state
            
            ObjectId id: 
            Input object ID of the viewport whose VPLAYER setting is to be captured
        """
        pass
    
    
    def SetLayerStateDescription(self):
        """
        SetLayerStateDescription -> void
            
            string name: 
            Input layer state whose description is to be updated
            
            string description: 
            Input description string up to 255 characters
        """
        pass
    
    
    def SetLayerStateMask(self):
        """
        SetLayerStateMask -> void
            
            string name: 
            Input name of layer state to mask
            
            LayerStateMasks mask: 
            Input mask to apply to layer state
        """
        pass
    
    
    LastRestoredLayerState = None
    
    pass

class LayerStateMasks():
    Color = 0x20
    CurrentViewport = 0x200
    Frozen = 2
    LastRestored = 0x10000
    LineType = 0x40
    LineWeight = 0x80
    Locked = 4
    NewViewport = 0x10
    None = 0
    On = 1
    Plot = 8
    PlotStyle = 0x100
    Transparency = 0x400

class LayerTable(object):
    """
    
    """
    def GenerateUsageData(self):
        """
        GenerateUsageData -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> SymbolTableEnumerator
        
        """
        pass
    
    
    def GetUnreconciledLayers(self):
        """
        GetUnreconciledLayers -> ObjectIdCollection
            
            idArray: 
            Input ID of the array to retrieve the unreconciled layers
        """
        pass
    
    
    HasUnreconciledLayers = None
    
    
    IncludingHidden = None
    
    
    SkippingReconciled = None
    
    pass

class LayerTableRecord(object):
    """
    
    LayerTableRecord()
    """
    def GetViewportOverrides(self):
        """
        GetViewportOverrides -> LayerViewportProperties
        
        """
        pass
    
    
    def HasViewportOverrides(self):
        """
        HasViewportOverrides -> bool
            
            ObjectId viewportId: 
            The object id of the viewport.
        """
        pass
    
    
    def RemoveAllOverrides(self):
        """
        RemoveAllOverrides -> void
        
        """
        pass
    
    
    Color = None
    
    
    Description = None
    
    
    EntityColor = None
    
    
    HasOverrides = None
    
    
    IsFrozen = None
    
    
    IsHidden = None
    
    
    IsLocked = None
    
    
    IsOff = None
    
    
    IsPlottable = None
    
    
    IsReconciled = None
    
    
    IsUsed = None
    
    
    LinetypeObjectId = None
    
    
    LineWeight = None
    
    
    MaterialId = None
    
    
    PlotStyleName = None
    
    
    PlotStyleNameId = None
    
    
    Transparency = None
    
    
    ViewportVisibilityDefault = None
    
    pass

class LayerViewportProperties(object):
    """
    
    """
    def RemoveOverrides(self):
        """
        RemoveOverrides -> void
        
        """
        pass
    
    
    Color = None
    
    
    IsColorOverridden = None
    
    
    IsLinetypeOverridden = None
    
    
    IsLineWeightOverridden = None
    
    
    IsPlotStyleOverridden = None
    
    
    IsTransparencyOverridden = None
    
    
    LinetypeObjectId = None
    
    
    LineWeight = None
    
    
    PlotStyleName = None
    
    
    PlotStyleNameId = None
    
    
    Transparency = None
    
    pass

class Layout(object):
    """
    
    Layout()
    """
    def AddToLayoutDictionary(self):
        """
        AddToLayoutDictionary -> void
            
            Database toWhichDatabase: 
            Input database to which to add the layout
            
            ObjectId blockTableRecordId: 
            Input block table record to use
        """
        pass
    
    
    def GetViewports(self):
        """
        GetViewports -> ObjectIdCollection
        
        """
        pass
    
    
    def Initialize(self):
        """
        Initialize -> ObjectId
        
        """
        pass
    
    
    AnnoAllVisible = None
    
    
    BlockTableRecordId = None
    
    
    Extents = None
    
    
    LayoutName = None
    
    
    Limits = None
    
    
    TabOrder = None
    
    
    TabSelected = None
    
    
    Thumbnail = None
    
    pass

class LayoutCopiedEventArgs(object):
    """
    
    """
    Id = None
    
    
    Name = None
    
    
    NewId = None
    
    
    NewName = None
    
    pass

class LayoutEventArgs(object):
    """
    
    """
    Id = None
    
    
    Name = None
    
    pass

class LayoutManager(object):
    """
    
    """
    def CloneLayout(self):
        """
        CloneLayout -> void
            
            string copyName: 
            Input to the old Layout name
            
            string newName: 
            Input the name for new layout
            
            int newTabOrder: 
            Optional input integer specifying new tab order
        """
        pass
    
    
    def CopyLayout(self):
        """
        CopyLayout -> void
            
            string copyName: 
            Input name of Layout object to be copied
            
            string newName: 
            Input name for new copy of Layout object
        """
        pass
    
    
    def CreateLayout(self):
        """
        CreateLayout -> ObjectId
            
            string newName: 
            Input name to give new Layout object
        """
        pass
    
    
    def DeleteLayout(self):
        """
        DeleteLayout -> void
            
            string deleteName: 
            Input name of Layout object to delete
        """
        pass
    
    
    def GetLayoutId(self):
        """
        GetLayoutId -> ObjectId
            
            string name: 
            Input name of Layout object to search for
        """
        pass
    
    
    def GetNonRectangularViewportIdFromClipId(self):
        """
        GetNonRectangularViewportIdFromClipId -> ObjectId
            
            ObjectId clipId: 
            Input ObjectId of clip entity to get the nonrectangular viewport ID from
            
            name: 
            Input name of Layout object to search for.
        """
        pass
    
    
    def LayoutExists(self):
        """
        LayoutExists -> bool
            
            string name: 
            Input name of layout to find.
        """
        pass
    
    
    def RenameLayout(self):
        """
        RenameLayout -> void
            
            string oldName: 
            Input name of Layout object to rename
            
            string newName: 
            Input new name for renamed Layout object
        """
        pass
    
    
    def SetCurrentLayoutId(self):
        """
        SetCurrentLayoutId -> void
        
        """
        pass
    
    
    Current = None
    
    
    CurrentLayout = None
    
    
    LayoutCount = None
    
    pass

class LayoutRenamedEventArgs(object):
    """
    
    """
    Id = None
    
    
    Name = None
    
    
    NewName = None
    
    pass

class Leader(object):
    """
    
    Leader()
    """
    def AppendVertex(self):
        """
        AppendVertex -> bool
            
            Point3d pointToAdd: 
            Input point (in WCS coordinates) to add to the vertex list
        """
        pass
    
    
    def EvaluateLeader(self):
        """
        EvaluateLeader -> void
        
        """
        pass
    
    
    def GetDimstyleData(self):
        """
        GetDimstyleData -> DimStyleTableRecord
        
        """
        pass
    
    
    def RemoveLastVertex(self):
        """
        RemoveLastVertex -> void
        
        """
        pass
    
    
    def SetDimstyleData(self):
        """
        SetDimstyleData -> void
            
            DimStyleTableRecord style: 
            Input objectId of the desired DimensionStyle
        """
        pass
    
    
    def SetPlane(self):
        """
        SetPlane -> void
            
            Plane value: 
            Input desired plane within which the leader will reside
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt -> bool
            
            int index: 
            Input index number (0 based) of the vertex to change
            
            Point3d pointValue: 
            Input new point value (in WCS) to use
        """
        pass
    
    
    def VertexAt(self):
        """
        VertexAt -> Point3d
            
            int value: 
            Input index number (0 based) of the vertex desired
        """
        pass
    
    
    AnnoHeight = None
    
    
    Annotation = None
    
    
    AnnotationOffset = None
    
    
    AnnoType = None
    
    
    AnnoWidth = None
    
    
    Dimasz = None
    
    
    Dimclrd = None
    
    
    DimensionStyle = None
    
    
    DimensionStyleName = None
    
    
    Dimgap = None
    
    
    Dimldrblk = None
    
    
    Dimlwd = None
    
    
    Dimsah = None
    
    
    Dimscale = None
    
    
    Dimtad = None
    
    
    Dimtxt = None
    
    
    FirstVertex = None
    
    
    HasArrowHead = None
    
    
    HasHookLine = None
    
    
    IsSplined = None
    
    
    LastVertex = None
    
    
    Normal = None
    
    
    NumVertices = None
    
    pass

class LeaderDirectionType():
    UnknownLeader = None
    LeftLeader = None
    RightLeader = None
    TopLeader = None
    BottomLeader = None

class LeaderType():
    InVisibleLeader = None
    StraightLeader = None
    SplineLeader = None

class Light(object):
    """
    
    Light()
    """
    def ResultingColor(self):
        """
        ResultingColor -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def SetHotspotAndFalloff(self):
        """
        SetHotspotAndFalloff -> void
            
            double hotspot: 
            Input the hotspot cone angle, in radians. Defines the brightest part of the spot light beam. Must be smaller than or equal to the falloff.
            
            double falloff: 
            Input the falloff cone angle, in radians. Defines the full cone of light. This is also known as the field angle. Must be larger than the hotspot.
        """
        pass
    
    
    Attenuation = None
    
    
    AttenuationType = None
    
    
    Direction = None
    
    
    EndLimitOffset = None
    
    
    FalloffAngle = None
    
    
    HasTarget = None
    
    
    HotspotAngle = None
    
    
    IlluminanceDistance = None
    
    
    Intensity = None
    
    
    IsOn = None
    
    
    IsPlottable = None
    
    
    LampColorPreset = None
    
    
    LampColorRGB = None
    
    
    LampColorTemp = None
    
    
    LampColorType = None
    
    
    LightColor = None
    
    
    LightType = None
    
    
    MapSize = None
    
    
    Name = None
    
    
    PhysicalIntensity = None
    
    
    PhysicalIntensityMethod = None
    
    
    Position = None
    
    
    Shadow = None
    
    
    ShadowType = None
    
    
    Softness = None
    
    
    StartLimitOffset = None
    
    
    TargetLocation = None
    
    
    UseLimits = None
    
    
    WebFile = None
    
    
    WebRotation = None
    
    pass

class LightingUnits():
    LightingUnitsGeneric = None
    LightingUnitsAmerican = None
    LightingUnitsInternational = None

class Line(object):
    """
    
    Line()()
    
    
    Line(Point3d, Point3d)
        Point3d pointer1 : Input line start point (WCS coordinates)
        Point3d pointer2 : Input line end point (WCS coordinates)
    
    
    """
    Angle = None
    
    
    Delta = None
    
    
    EndPoint = None
    
    
    Length = None
    
    
    Normal = None
    
    
    StartPoint = None
    
    
    Thickness = None
    
    pass

class LineAngularDimension2(object):
    """
    
    LineAngularDimension2()()
    
    
    """
    ArcPoint = None
    
    
    XLine1End = None
    
    
    XLine1Start = None
    
    
    XLine2End = None
    
    
    XLine2Start = None
    
    pass

class LineSpacingStyle():
    AtLeast = 1
    Exactly = 2

class LineWeight():
    ByBlock = -2
    ByLayer = -1
    ByLineWeightDefault = -3
    LineWeight000 = 0
    LineWeight005 = 5
    LineWeight009 = 9
    LineWeight013 = 13
    LineWeight015 = 15
    LineWeight018 = 0x12
    LineWeight020 = 20
    LineWeight025 = 0x19
    LineWeight030 = 30
    LineWeight035 = 0x23
    LineWeight040 = 40
    LineWeight050 = 50
    LineWeight053 = 0x35
    LineWeight060 = 60
    LineWeight070 = 70
    LineWeight080 = 80
    LineWeight090 = 90
    LineWeight100 = 100
    LineWeight106 = 0x6a
    LineWeight120 = 120
    LineWeight140 = 140
    LineWeight158 = 0x9e
    LineWeight200 = 200
    LineWeight211 = 0xd3

class LineWeightConverter(object):
    """
    
    """
    def ConvertFrom(self):
        """
        ConvertFrom -> object
            
            ITypeDescriptorContext context: 
            Input context to convert within
            
            CultureInfo culture: 
            Input culture to convert within
            
            object value: 
            Input object to convert from
        """
        pass
    
    
    def CanConvertFrom(self):
        """
        CanConvertFrom -> bool
            
            ITypeDescriptorContext context: 
            Input context with which to handle source
            
            Type sourceType: 
            Input source type
        """
        pass
    
    
    def ConvertTo(self):
        """
        ConvertTo -> object
            
            ITypeDescriptorContext context: 
            Input context within which to handle value
            
            CultureInfo culture: 
            Input culture within which to handle value
            
            object value: 
            Input value to process
        """
        pass
    
    pass

class LinetypeTable(object):
    """
    
    """

    pass

class LinetypeTableRecord(object):
    """
    
    LinetypeTableRecord()
    """
    def DashLengthAt(self):
        """
        DashLengthAt -> double
            
            int index: 
            Input index (0-based) of dash to get length of
        """
        pass
    
    
    def SetDashLengthAt(self):
        """
        SetDashLengthAt -> void
            
            int index: 
            Input index (0-based) of dash to set
            
            double value: 
            Input length value for the dash
        """
        pass
    
    
    def SetShapeIsUcsOrientedAt(self):
        """
        SetShapeIsUcsOrientedAt -> void
            
            int index: 
            Input index (0-based) of shape (or text string) to get
            
            [MarshalAs(UnmanagedType.U1)] bool isOriented: 
            Input Boolean indicating whether or not the shape is to be oriented relative to the current UCS
        """
        pass
    
    
    def SetShapeNumberAt(self):
        """
        SetShapeNumberAt -> void
            
            int index: 
            Input index at which to set the shape
            
            int shapeNumber: 
            Input shape identification number of the shape to use
        """
        pass
    
    
    def SetShapeOffsetAt(self):
        """
        SetShapeOffsetAt -> void
            
            int index: 
            Input index at which to set the shape (or text string) offset
            
            Vector2d offset: 
            Input vector whose X and Y values are the WCS X and Y offsets for the shape
        """
        pass
    
    
    def SetShapeRotationAt(self):
        """
        SetShapeRotationAt -> void
            
            int index: 
            Input index (0-based) of shape (or text string) to get
            
            double rotation: 
            Input rotation angle for the shape (or text string)
        """
        pass
    
    
    def SetShapeScaleAt(self):
        """
        SetShapeScaleAt -> void
            
            int index: 
            Input index at which to set the shape (or text string) scale
            
            double scale: 
            Input scale factor to be applied to the shape
        """
        pass
    
    
    def SetShapeStyleAt(self):
        """
        SetShapeStyleAt -> void
            
            int index: 
            Input index at which to set the shape (or text string) scale
            
            ObjectId id: 
            Input scale factor to be applied to the shape (or text string)
        """
        pass
    
    
    def SetTextAt(self):
        """
        SetTextAt -> void
            
            int index: 
            Input index at which to set the text string
            
            string value: 
            Input pointer to the text to use at index
        """
        pass
    
    
    def ShapeIsUcsOrientedAt(self):
        """
        ShapeIsUcsOrientedAt -> bool
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeNumberAt(self):
        """
        ShapeNumberAt -> Integer
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeOffsetAt(self):
        """
        ShapeOffsetAt -> Vector2d
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeRotationAt(self):
        """
        ShapeRotationAt -> double
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeScaleAt(self):
        """
        ShapeScaleAt -> double
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def ShapeStyleAt(self):
        """
        ShapeStyleAt -> ObjectId
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    def TextAt(self):
        """
        TextAt -> string
            
            int index: 
            Input index (0-based) of shape (or text string) to get
        """
        pass
    
    
    AsciiDescription = None
    
    
    Comments = None
    
    
    IsScaledToFit = None
    
    
    NumDashes = None
    
    
    PatternLength = None
    
    pass

class LinkedData(object):
    """
    
    """
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    IsEmpty = None
    
    
    Name = None
    
    pass

class LinkedTableData(object):
    """
    
    LinkedTableData()
    """
    def AppendColumn(self):
        """
        AppendColumn -> Integer
            
            int columnsNumber: 
            Input number of columns to append
        """
        pass
    
    
    def AppendRow(self):
        """
        AppendRow -> Integer
            
            int rowsNumber: 
            Input number of rows to append
        """
        pass
    
    
    def DataType(self):
        """
        DataType -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def DeleteColumn(self):
        """
        DeleteColumn -> void
            
            int index: 
            Input starting index of the columns to delete
            
            int columnsNumberToDelete: 
            Input number of columns to delete
        """
        pass
    
    
    def DeleteContent(self):
        """
        DeleteContent -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def DeleteRow(self):
        """
        DeleteRow -> void
            
            int index: 
            Input starting index of the rows to delete
            
            int rowsNumberToDelete: 
            Input number of rows to delete
        """
        pass
    
    
    def GetBlockAttributeValue(self):
        """
        GetBlockAttributeValue -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId attributeDefinitionId: 
            Input object ID of the AttributeDefinition object
        """
        pass
    
    
    def GetBlockTableRecordId(self):
        """
        GetBlockTableRecordId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetCellState(self):
        """
        GetCellState -> CellStates
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetColumnName(self):
        """
        GetColumnName -> string
            
            int index: 
            Input column index
        """
        pass
    
    
    def GetContentTypes(self):
        """
        GetContentTypes -> CellContentTypes
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetCustomData(self):
        """
        GetCustomData -> object
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            string key: 
            Input key to retrieve the custom data
        """
        pass
    
    
    def GetDataFormat(self):
        """
        GetDataFormat -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetDataLink(self):
        """
        GetDataLink() -> ObjectIdCollection
        
        GetDataLink(CellRange) -> ObjectIdCollection
            
            CellRange range: 
            Input range to get the data links. If this is NULL it gets all the data links in the table
        GetDataLink(int, int) -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TableEnumerator
        
        GetEnumerator(TableEnumeratorOption) -> TableEnumerator
            
            TableEnumeratorOption option: 
            Input iterator option.
        """
        pass
    
    
    def GetFieldId(self):
        """
        GetFieldId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetToolTip(self):
        """
        GetToolTip -> string
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue(int, int) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        GetValue(int, int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int content: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption formatOption: 
            Input format option for formatting the cell value. See Remarks for description of each option.
        """
        pass
    
    
    def InsertColumn(self):
        """
        InsertColumn -> Integer
            
            int index: 
            Input index at which to insert the new columns
            
            int columnsNumber: 
            Input number of columns to insert
        """
        pass
    
    
    def InsertRow(self):
        """
        InsertRow -> Integer
            
            int index: 
            Input index at which to insert the new rows.
            
            int rowsNumber: 
            Input number of rows to insert
        """
        pass
    
    
    def IsContentEditable(self):
        """
        IsContentEditable -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsLinked(self):
        """
        IsLinked -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def SetBlockAttributeValue(self):
        """
        SetBlockAttributeValue -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId attributeDefinitionId: 
            Input object ID of the AttributeDefinition object
            
            string value: 
            Input attribute value to set
        """
        pass
    
    
    def SetBlockTableRecordId(self):
        """
        SetBlockTableRecordId -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId value: 
            Input attribute value to set
        """
        pass
    
    
    def SetCellState(self):
        """
        SetCellState -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            CellStates value: 
            Cell state to set. This will replace all the bits of the current state.
        """
        pass
    
    
    def SetColumnName(self):
        """
        SetColumnName -> void
            
            int index: 
            Input zero based index of the column
            
            string name: 
            Input column name to set. This can be an empty string.
        """
        pass
    
    
    def SetCustomData(self):
        """
        SetCustomData -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            string key: 
            Input key to use for the custom data
            
            object value: 
            Input custom data to set. This can be NULL. If it is NULL it deletes the custom data.
        """
        pass
    
    
    def SetDataFormat(self):
        """
        SetDataFormat -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            string format: 
            Input data format to set
        """
        pass
    
    
    def SetDataLink(self):
        """
        SetDataLink(CellRange, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            CellRange range: 
            Range of cells to link to external source.
            
            ObjectId dataLinkId: 
            Id of the data link to set
            
            [MarshalAs(UnmanagedType.U1)] bool bUpdate: 
            Input true if the data link has is to be updated after setting it, false if not
        SetDataLink(int, int, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId dataLinkId: 
            Input id of the data link to set
            
            [MarshalAs(UnmanagedType.U1)] bool bUpdate: 
            Input true if the data link is to be updated after setting it, false if not.
        """
        pass
    
    
    def SetDataType(self):
        """
        SetDataType -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.DataType dataType: 
            Input data type to set
            
            Autodesk.AutoCAD.DatabaseServices.UnitType unitType: 
            Input unit type to set
        """
        pass
    
    
    def SetFieldId(self):
        """
        SetFieldId -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId value: 
            Input field id to set
        """
        pass
    
    
    def SetSize(self):
        """
        SetSize -> void
            
            int numRows: 
            Input new row size.
            
            int numCols: 
            Input new column size.
        """
        pass
    
    
    def SetToolTip(self):
        """
        SetToolTip -> void
            
            int row: 
            Input row index. This can be -1. See remarks.
            
            int column: 
            Input column index. This can be -1. See remarks.
            
            string value: 
            Input tool tip string to set
        """
        pass
    
    
    def SetValue(self):
        """
        SetValue(int, int, object) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            object value: 
            Input value to set
        SetValue(int, int, int, object, Autodesk.AutoCAD.DatabaseServices.ParseOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int content: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            object value: 
            Input value to set.
            
            Autodesk.AutoCAD.DatabaseServices.ParseOption parseOption: 
            Input parse option. See remarks.
        """
        pass
    
    
    def UnitType(self):
        """
        UnitType -> Autodesk.AutoCAD.DatabaseServices.UnitType
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def UpdateDataLink(self):
        """
        UpdateDataLink(Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Input direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Input option flag
        UpdateDataLink(int, int, Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Input direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Input option flag
        """
        pass
    
    
    NumberOfColumns = None
    
    
    NumberOfRows = None
    
    pass

class LoftOptions(object):
    """
    
    LoftOptions()()
    
    
    LoftOptions(LoftOptions)
        LoftOptions opts : Input object to be copied into 'this'
    
    
    """
    def CheckCrossSectionCurves(self):
        """
        CheckCrossSectionCurves -> LoftOptionsCheckCurvesOut
            
            Entity[] crossSectionCurves: 
            Input list of cross-section curves
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def CheckGuideCurves(self):
        """
        CheckGuideCurves -> void
            
            Entity[] guideCurves: 
            Input list of guide curves
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def CheckLoftCurves(self):
        """
        CheckLoftCurves -> LoftOptionsCheckCurvesOut
            
            Entity[] crossSectionCurves: 
            Input list of cross-section curves
            
            Entity[] guideCurves: 
            Input list of guide curves
            
            Entity pPathCurve: 
            Input pointer to path curve or null
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def CheckPathCurve(self):
        """
        CheckPathCurve -> void
            
            Entity pathCurve: 
            Input path curve
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean whether or not to display error messages
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    AlignDirection = None
    
    
    ArcLengthParam = None
    
    
    Closed = None
    
    
    DraftEnd = None
    
    
    DraftEndMag = None
    
    
    DraftStart = None
    
    
    DraftStartMag = None
    
    
    NormalOption = None
    
    
    NoTwist = None
    
    
    Ruled = None
    
    
    Simplify = None
    
    
    VirtualGuide = None
    
    pass

class LoftOptionsBuilder(object):
    """
    
    LoftOptionsBuilder()()
    
    
    LoftOptionsBuilder(LoftOptions)
        LoftOptions value : LoftOptions object to create from
    
    
    """
    def SetOptionsFromSysvars(self):
        """
        SetOptionsFromSysvars -> void
        
        """
        pass
    
    
    def ToLoftOptions(self):
        """
        ToLoftOptions -> LoftOptions
        
        """
        pass
    
    
    AlignDirection = None
    
    
    ArcLengthParam = None
    
    
    Closed = None
    
    
    DraftEnd = None
    
    
    DraftEndMag = None
    
    
    DraftStart = None
    
    
    DraftStartMag = None
    
    
    NormalOption = None
    
    
    NoTwist = None
    
    
    Ruled = None
    
    
    Simplify = None
    
    
    VirtualGuide = None
    
    pass

class LoftOptionsCheckCurvesOut(object):
    """
    
    LoftOptionsCheckCurvesOut()
    """
    AllClosed = None
    
    
    AllOpen = None
    
    
    AllPlanar = None
    
    pass

class LoftOptionsNormalOption():
    NoNormal = None
    FirstNormal = None
    LastNormal = None
    EndsNormal = None
    AllNormal = None
    UseDraftAngles = None

class LoftProfile(object):
    """
    
    LoftProfile()()
    
    
    LoftProfile(Entity)()
    
    
    LoftProfile(LoftProfile)()
    
    
    LoftProfile(PathRef)()
    
    
    LoftProfile(Point3d)()
    
    
    """
    def CopyFrom(self):
        """
        CopyFrom(LoftProfile) -> void
        
        CopyFrom(Profile3d) -> void
        
        """
        pass
    
    
    Continuity = None
    
    
    Magnitude = None
    
    pass

class LoftedSurface(object):
    """
    
    LoftedSurface()
    """
    class LoftSurfaceType():
        LoftSurface = None
        BlendSurface = None
        NetworkSurface = None
    
    
    def CreateLoftedSurface(self):
        """
        CreateLoftedSurface -> void
            
            Entity[] crossSections: 
            Input array of curve entities to be used as cross sections for the lofting operation
            
            Entity[] guideCurves: 
            Input optional array of guide curves
            
            Entity pathCurve: 
            Input path curve
            
            Autodesk.AutoCAD.DatabaseServices.LoftOptions loftOptions: 
            Input loft options
        """
        pass
    
    
    def GetCrossSectionProfile(self):
        """
        GetCrossSectionProfile -> LoftProfile
            
            int idx: 
            Input index of cross section.
        """
        pass
    
    
    def GetGuideProfile(self):
        """
        GetGuideProfile -> LoftProfile
            
            int idx: 
            Input index of guide.
        """
        pass
    
    
    Closed = None
    
    
    CrossSectionProfiles = None
    
    
    CrossSections = None
    
    
    EndCrossSectionContinuity = None
    
    
    EndCrossSectionMagnitude = None
    
    
    EndGuideCurveContinuity = None
    
    
    EndGuideCurveMagnitude = None
    
    
    GuideCurves = None
    
    
    GuideProfiles = None
    
    
    LoftOptions = None
    
    
    NumberOfCrossSections = None
    
    
    NumberOfGuideCurves = None
    
    
    PathEntity = None
    
    
    PathProfile = None
    
    
    StartCrossSectionContinuity = None
    
    
    StartCrossSectionMagnitude = None
    
    
    StartGuideCurveContinuity = None
    
    
    StartGuideCurveMagnitude = None
    
    
    SurfaceType = None
    
    pass

class LongTransaction(object):
    """
    
    LongTransaction()
    """
    def AddToWorkSet(self):
        """
        AddToWorkSet -> void
        
        """
        pass
    
    
    def OriginObject(self):
        """
        OriginObject -> ObjectId
        
        """
        pass
    
    
    def RegenWorkSetWithDrawOrder(self):
        """
        RegenWorkSetWithDrawOrder -> void
        
        """
        pass
    
    
    def RemoveFromWorkSet(self):
        """
        RemoveFromWorkSet -> void
        
        """
        pass
    
    
    def SyncWorkSet(self):
        """
        SyncWorkSet -> void
        
        """
        pass
    
    
    def WorkSetHas(self):
        """
        WorkSetHas -> bool
        
        """
        pass
    
    
    ActiveIdMap = None
    
    
    DestinationBlock = None
    
    
    DisallowDrawOrder = None
    
    
    LongTransactionName = None
    
    
    OriginBlock = None
    
    
    Type = None
    
    pass

class LongTransactionType():
    SameDb = None
    XRefDb = None
    UnrelatedDb = None

class MInsertBlock(object):
    """
    
    MInsertBlock()()
    
    
    """
    Columns = None
    
    
    ColumnSpacing = None
    
    
    Rows = None
    
    
    RowSpacing = None
    
    pass

class MLeader(object):
    """
    
    MLeader()
    """
    def AddFirstVertex(self):
        """
        AddFirstVertex -> void
            
            int leaderLineIndex: 
            Input index of the leader line.
            
            Point3d point: 
            Input the vertex position.
        """
        pass
    
    
    def AddLastVertex(self):
        """
        AddLastVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
            
            Point3d point: 
            Input the vertex position.
        """
        pass
    
    
    def AddLeader(self):
        """
        AddLeader -> Integer
        
        """
        pass
    
    
    def AddLeaderLine(self):
        """
        AddLeaderLine(Point3d) -> Integer
            
            Point3d point: 
            Input position of the first(head) vertex of the new leader line.
        AddLeaderLine(int) -> Integer
            
            int leaderIndex: 
            Index of the leader cluster.
        """
        pass
    
    
    def ConnectionPoint(self):
        """
        ConnectionPoint(Vector3d) -> Point3d
            
            Vector3d direction: 
            Input the specific direction.
        ConnectionPoint(Vector3d, Autodesk.AutoCAD.DatabaseServices.TextAttachmentDirection) -> Point3d
            
            Vector3d direction: 
            Input the specific direction.
            
            Autodesk.AutoCAD.DatabaseServices.TextAttachmentDirection textAttachmentDirection: 
            Specify if the leader attaches to the MText horizontally or vertically (Horizontally by default).
        """
        pass
    
    
    def GetArrowSymbolId(self):
        """
        GetArrowSymbolId -> ObjectId
            
            int leaderLineIndex: 
            Input the index of the specific leaderline.
        """
        pass
    
    
    def GetBlockAttribute(self):
        """
        GetBlockAttribute -> AttributeReference
            
            ObjectId attDefId: 
            Input attribute definition id.
        """
        pass
    
    
    def GetContentGeomExtents(self):
        """
        GetContentGeomExtents -> Extents3d
        
        """
        pass
    
    
    def getContextDataManager(self):
        """
        getContextDataManager -> IntPtr
        
        """
        pass
    
    
    def GetDogleg(self):
        """
        GetDogleg -> Vector3d
            
            int leaderIndex: 
            Input leader index.
        """
        pass
    
    
    def GetDoglegLength(self):
        """
        GetDoglegLength -> double
            
            int leaderIndex: 
            Input leader index
        """
        pass
    
    
    def GetFirstVertex(self):
        """
        GetFirstVertex -> Point3d
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def MoveMLeader(self):
        """
        MoveMLeader -> void
            
            Vector3d vec: 
            Input vector indicate direction and distance the MLeader will be moved.
            
            Autodesk.AutoCAD.DatabaseServices.MoveType type: 
            Input MoveType indicate how the MLeader will be moved.
        """
        pass
    
    
    def GetLastVertex(self):
        """
        GetLastVertex -> Point3d
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def GetLeaderIndex(self):
        """
        GetLeaderIndex -> Integer
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def GetLeaderIndexes(self):
        """
        GetLeaderIndexes -> ArrayList
        
        """
        pass
    
    
    def GetLeaderLineIndexes(self):
        """
        GetLeaderLineIndexes -> ArrayList
            
            int leaderIndex: 
            Input leader index.
        """
        pass
    
    
    def getOverridedMLeaderStyle(self):
        """
        getOverridedMLeaderStyle -> void
            
            MLeaderStyle: 
            Input a reference of MLeaderStyle, MLeader object will set its properties to this object.
        """
        pass
    
    
    def GetPlane(self):
        """
        GetPlane -> Plane
        
        """
        pass
    
    
    def GetVertex(self):
        """
        GetVertex -> Point3d
            
            int leaderLineIndex: 
            Input leader line index.
            
            int index: 
            Input index of the vertex.
        """
        pass
    
    
    def HasContent(self):
        """
        HasContent -> bool
        
        """
        pass
    
    
    def PostMLeaderToDb(self):
        """
        PostMLeaderToDb -> void
            
            Database db: 
            Input database into which the current MLeader object should be added.
        """
        pass
    
    
    def recomputeBreakPoints(self):
        """
        recomputeBreakPoints -> void
        
        """
        pass
    
    
    def RemoveFirstVertex(self):
        """
        RemoveFirstVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def RemoveLastVertex(self):
        """
        RemoveLastVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def RemoveLeader(self):
        """
        RemoveLeader -> void
            
            int index: 
            Input the index of the leader to be removed.
        """
        pass
    
    
    def RemoveLeaderLine(self):
        """
        RemoveLeaderLine -> void
            
            int leaderLineIndex: 
            Input the index of leader cluster.
        """
        pass
    
    
    def SetArrowSymbolId(self):
        """
        SetArrowSymbolId -> void
            
            int leaderLineIndex: 
            Input the index of the specific leaderline.
            
            ObjectId id: 
            Input the object id of the arrow head symbol.
        """
        pass
    
    
    def SetBlockAttribute(self):
        """
        SetBlockAttribute -> void
            
            ObjectId attDefId: 
            Input attribute definition id.
            
            AttributeReference attributeValue: 
            Input attribute value.
        """
        pass
    
    
    def SetContextDataManager(self):
        """
        SetContextDataManager -> void
            
            IntPtr contextDataManager: 
            Input the pointer of context data manager.
        """
        pass
    
    
    def SetDogleg(self):
        """
        SetDogleg -> void
            
            int leaderIndex: 
            Input leader index.
            
            Vector3d vector: 
            Input the vector represents the new length and new direction of dog-leg.
        """
        pass
    
    
    def SetDoglegLength(self):
        """
        SetDoglegLength -> void
            
            int leaderIndex: 
            Input leader index
            
            double doglegLength: 
            Input the length of dog-leg leader line
        """
        pass
    
    
    def SetFirstVertex(self):
        """
        SetFirstVertex -> void
            
            int leaderLineIndex: 
            Input the leader line index.
            
            Point3d point: 
            Input the point where the new leader head is on.
        """
        pass
    
    
    def SetLastVertex(self):
        """
        SetLastVertex -> void
            
            int leaderLineIndex: 
            Input the leader line index.
            
            Point3d point: 
            Input the point where the new leader tail is on.
        """
        pass
    
    
    def SetPlane(self):
        """
        SetPlane -> void
            
            Plane value: 
            Input desired plane within which the MLeader will reside.
        """
        pass
    
    
    def SetVertex(self):
        """
        SetVertex -> void
            
            int leaderLineIndex: 
            Input leader line index.
            
            int index: 
            Input the index of vertex.
            
            Point3d point: 
            Input the new position of this vertex.
        """
        pass
    
    
    def VerticesCount(self):
        """
        VerticesCount -> Integer
            
            int leaderLineIndex: 
            Input leader line index.
        """
        pass
    
    
    def GetTextAttachmentType(self):
        """
        GetTextAttachmentType -> Autodesk.AutoCAD.DatabaseServices.TextAttachmentType
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction type
        """
        pass
    
    
    def SetTextAttachmentType(self):
        """
        SetTextAttachmentType -> void
            
            Autodesk.AutoCAD.DatabaseServices.TextAttachmentType textAttachmentType: 
            Input text attachment type
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction types
        """
        pass
    
    
    ArrowSize = None
    
    
    ArrowSymbolId = None
    
    
    BlockColor = None
    
    
    BlockConnectionType = None
    
    
    BlockContentId = None
    
    
    BlockPosition = None
    
    
    BlockRotation = None
    
    
    BlockScale = None
    
    
    ContentType = None
    
    
    DoglegLength = None
    
    
    EnableAnnotationScale = None
    
    
    EnableDogleg = None
    
    
    EnableFrameText = None
    
    
    EnableLanding = None
    
    
    ExtendLeaderToText = None
    
    
    LandingGap = None
    
    
    LeaderCount = None
    
    
    LeaderLineColor = None
    
    
    LeaderLineCount = None
    
    
    LeaderLineType = None
    
    
    LeaderLineTypeId = None
    
    
    LeaderLineWeight = None
    
    
    MLeaderStyle = None
    
    
    MText = None
    
    
    Normal = None
    
    
    Scale = None
    
    
    TextAlignmentType = None
    
    
    TextAngleType = None
    
    
    TextAttachmentDirection = None
    
    
    TextAttachmentType = None
    
    
    TextColor = None
    
    
    TextHeight = None
    
    
    TextLocation = None
    
    
    TextStyleId = None
    
    
    ToleranceLocation = None
    
    pass

class MLeaderStyle(object):
    """
    
    MLeaderStyle()()
    
    
    MLeaderStyle(MLeaderStyle)
        MLeaderStyle : Input object to copy.
    
    
    """
    def OverwritePropChanged(self):
        """
        OverwritePropChanged -> bool
        
        """
        pass
    
    
    def PostMLeaderStyleToDb(self):
        """
        PostMLeaderStyleToDb -> ObjectId
        
        """
        pass
    
    
    def GetTextAttachmentType(self):
        """
        GetTextAttachmentType -> Autodesk.AutoCAD.DatabaseServices.TextAttachmentType
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction type
        """
        pass
    
    
    def SetTextAttachmentType(self):
        """
        SetTextAttachmentType -> void
            
            Autodesk.AutoCAD.DatabaseServices.TextAttachmentType textAttachmentType: 
            Input text attachment type
            
            Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType leaderDirection: 
            Input text leader direction types
        """
        pass
    
    
    ArrowSize = None
    
    
    ArrowSymbolId = None
    
    
    BlockColor = None
    
    
    BlockConnectionType = None
    
    
    BlockId = None
    
    
    BlockRotation = None
    
    
    BlockScale = None
    
    
    BreakSize = None
    
    
    ContentType = None
    
    
    DefaultMText = None
    
    
    DoglegLength = None
    
    
    DrawLeaderOrderType = None
    
    
    DrawMLeaderOrderType = None
    
    
    EnableBlockRotation = None
    
    
    EnableBlockScale = None
    
    
    EnableDogleg = None
    
    
    EnableFrameText = None
    
    
    EnableLanding = None
    
    
    ExtendLeaderToText = None
    
    
    FirstSegmentAngleConstraint = None
    
    
    LandingGap = None
    
    
    LeaderLineColor = None
    
    
    LeaderLineType = None
    
    
    LeaderLineTypeId = None
    
    
    LeaderLineWeight = None
    
    
    MaxLeaderSegmentsPoints = None
    
    
    Name = None
    
    
    Scale = None
    
    
    SecondSegmentAngleConstraint = None
    
    
    TextAlignAlwaysLeft = None
    
    
    TextAlignmentType = None
    
    
    TextAngleType = None
    
    
    TextAttachmentDirection = None
    
    
    TextAttachmentType = None
    
    
    TextColor = None
    
    
    TextHeight = None
    
    
    TextStyleId = None
    
    pass

class MText(object):
    """
    
    MText
        normal : (0.0,0.0,1.0)
        direction : (1.0,0.0,0.0)
        width : 0.0
        textStyle : NULL
        textHeight : 0.0
        attachment : AcDbMText::kTopLeft
        flowDirection : AcDbMText::kByStyle
        contents : NULL
    """
    def ConvertFieldToText(self):
        """
        ConvertFieldToText -> void
        
        """
        pass
    
    
    def CorrectSpelling(self):
        """
        CorrectSpelling -> Integer
        
        """
        pass
    
    
    def ExplodeFragments(self):
        """
        ExplodeFragments(MTextFragmentCallback) -> void
            
            MTextFragmentCallback enumerator: 
            Input fragment elaboration callback function
        ExplodeFragments(MTextFragmentCallback, object) -> void
            
            MTextFragmentCallback enumerator: 
            Input fragment elaboration callback function
            
            object userData: 
            Input user data
        ExplodeFragments(MTextFragmentCallback, object, WorldDraw) -> void
            
            MTextFragmentCallback enumerator: 
            Input fragment elaboration callback function
            
            object userData: 
            Input user data
            
            WorldDraw context: 
            Input WorldDraw object
        """
        pass
    
    
    def GetBoundingPoints(self):
        """
        GetBoundingPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetColumnHeight(self):
        """
        GetColumnHeight -> double
            
            int index: 
            The column's height to get
        """
        pass
    
    
    def SetColumnHeight(self):
        """
        SetColumnHeight -> void
            
            int index: 
            The column's height to set
            
            double height: 
            Column height
        """
        pass
    
    
    def SetContentsRtf(self):
        """
        SetContentsRtf -> Integer
            
            string value: 
            Input RTF-encoded string
        """
        pass
    
    
    def SetDynamicColumns(self):
        """
        SetDynamicColumns -> void
            
            double width: 
            Input new column width
            
            double gutter: 
            Input new column gutter
            
            [MarshalAs(UnmanagedType.U1)] bool auto_height: 
            Input new auto-height setting
        """
        pass
    
    
    def SetStaticColumns(self):
        """
        SetStaticColumns -> void
            
            double width: 
            Input new column width
            
            double gutter: 
            Input new column gutter
            
            int count: 
            Input new auto-height setting
        """
        pass
    
    
    def SetAttachmentMovingLocation(self):
        """
        SetAttachmentMovingLocation -> void
            
            Autodesk.AutoCAD.DatabaseServices.AttachmentPoint value: 
            Input desired AttachmentPoint type value
        """
        pass
    
    
    ActualHeight = None
    
    
    ActualWidth = None
    
    
    AlignChange = None
    
    
    Ascent = None
    
    
    Attachment = None
    
    
    BackgroundFill = None
    
    
    BackgroundFillColor = None
    
    
    BackgroundScaleFactor = None
    
    
    BackgroundTransparency = None
    
    
    BlockBegin = None
    
    
    BlockEnd = None
    
    
    ColorChange = None
    
    
    ColumnAutoHeight = None
    
    
    ColumnCount = None
    
    
    ColumnFlowReversed = None
    
    
    ColumnGutterWidth = None
    
    
    ColumnType = None
    
    
    ColumnWidth = None
    
    
    Contents = None
    
    
    ContentsRTF = None
    
    
    Descent = None
    
    
    Direction = None
    
    
    FlowDirection = None
    
    
    FontChange = None
    
    
    Height = None
    
    
    HeightChange = None
    
    
    LineBreak = None
    
    
    LineSpaceDistance = None
    
    
    LineSpacingFactor = None
    
    
    LineSpacingStyle = None
    
    
    Location = None
    
    
    NonBreakSpace = None
    
    
    Normal = None
    
    
    ObliqueChange = None
    
    
    OverlineOff = None
    
    
    OverlineOn = None
    
    
    ParagraphBreak = None
    
    
    Rotation = None
    
    
    ShowBorders = None
    
    
    StackStart = None
    
    
    StrikethroughOff = None
    
    
    StrikethroughOn = None
    
    
    Text = None
    
    
    TextHeight = None
    
    
    TextStyleId = None
    
    
    TextStyleName = None
    
    
    TrackChange = None
    
    
    UnderlineOff = None
    
    
    UnderlineOn = None
    
    
    UseBackgroundColor = None
    
    
    Width = None
    
    
    WidthChange = None
    
    pass

class MTextFragment(object):
    """
    
    """
    def GetOverLinePoints(self):
        """
        GetOverLinePoints -> Point3d()
        
        """
        pass
    
    
    def GetStrikethroughPoints(self):
        """
        GetStrikethroughPoints -> Point3d()
        
        """
        pass
    
    
    def GetUnderLinePoints(self):
        """
        GetUnderLinePoints -> Point3d()
        
        """
        pass
    
    
    BigFont = None
    
    
    Bold = None
    
    
    CapsHeight = None
    
    
    Color = None
    
    
    Direction = None
    
    
    Extents = None
    
    
    Italic = None
    
    
    Location = None
    
    
    Normal = None
    
    
    ObliqueAngle = None
    
    
    Overlined = None
    
    
    ShxFont = None
    
    
    StackBottom = None
    
    
    StackTop = None
    
    
    Strikethrough = None
    
    
    Text = None
    
    
    TrackingFactor = None
    
    
    TrueTypeFont = None
    
    
    Underlined = None
    
    
    WidthFactor = None
    
    pass

class MTextFragmentCallbackStatus():
    Terminate = None
    Continue = None

class MaintenanceReleaseVersion():
    Release0 = 0
    Release1 = 1
    Release10 = 10
    Release100 = 100
    Release101 = 0x65
    Release102 = 0x66
    Release103 = 0x67
    Release104 = 0x68
    Release105 = 0x69
    Release106 = 0x6a
    Release107 = 0x6b
    Release108 = 0x6c
    Release109 = 0x6d
    Release11 = 11
    Release110 = 110
    Release111 = 0x6f
    Release112 = 0x70
    Release113 = 0x71
    Release114 = 0x72
    Release115 = 0x73
    Release116 = 0x74
    Release117 = 0x75
    Release118 = 0x76
    Release119 = 0x77
    Release12 = 12
    Release120 = 120
    Release121 = 0x79
    Release122 = 0x7a
    Release123 = 0x7b
    Release124 = 0x7c
    Release125 = 0x7d
    Release126 = 0x7e
    Release127 = 0x7f
    Release128 = 0x80
    Release129 = 0x81
    Release13 = 13
    Release130 = 130
    Release131 = 0x83
    Release132 = 0x84
    Release133 = 0x85
    Release134 = 0x86
    Release135 = 0x87
    Release136 = 0x88
    Release137 = 0x89
    Release138 = 0x8a
    Release139 = 0x8b
    Release14 = 14
    Release140 = 140
    Release141 = 0x8d
    Release142 = 0x8e
    Release143 = 0x8f
    Release144 = 0x90
    Release145 = 0x91
    Release146 = 0x92
    Release147 = 0x93
    Release148 = 0x94
    Release149 = 0x95
    Release15 = 15
    Release150 = 150
    Release151 = 0x97
    Release152 = 0x98
    Release153 = 0x99
    Release154 = 0x9a
    Release155 = 0x9b
    Release156 = 0x9c
    Release157 = 0x9d
    Release158 = 0x9e
    Release159 = 0x9f
    Release16 = 0x10
    Release160 = 160
    Release17 = 0x11
    Release18 = 0x12
    Release19 = 0x13
    Release2 = 2
    Release20 = 20
    Release2010Max = 0xff
    Release2010Newest = 0xe2
    Release21 = 0x15
    Release22 = 0x16
    Release23 = 0x17
    Release24 = 0x18
    Release25 = 0x19
    Release26 = 0x1a
    Release27 = 0x1b
    Release28 = 0x1c
    Release29 = 0x1d
    Release3 = 3
    Release30 = 30
    Release31 = 0x1f
    Release32 = 0x20
    Release33 = 0x21
    Release34 = 0x22
    Release35 = 0x23
    Release36 = 0x24
    Release37 = 0x25
    Release38 = 0x26
    Release39 = 0x27
    Release4 = 4
    Release40 = 40
    Release41 = 0x29
    Release42 = 0x2a
    Release43 = 0x2b
    Release44 = 0x2c
    Release45 = 0x2d
    Release46 = 0x2e
    Release47 = 0x2f
    Release48 = 0x30
    Release49 = 0x31
    Release5 = 5
    Release50 = 50
    Release51 = 0x33
    Release52 = 0x34
    Release53 = 0x35
    Release54 = 0x36
    Release55 = 0x37
    Release56 = 0x38
    Release57 = 0x39
    Release58 = 0x3a
    Release59 = 0x3b
    Release6 = 6
    Release60 = 60
    Release61 = 0x3d
    Release62 = 0x3e
    Release63 = 0x3f
    Release64 = 0x40
    Release65 = 0x41
    Release66 = 0x42
    Release67 = 0x43
    Release68 = 0x44
    Release69 = 0x45
    Release7 = 7
    Release70 = 70
    Release71 = 0x47
    Release72 = 0x48
    Release73 = 0x49
    Release74 = 0x4a
    Release75 = 0x4b
    Release76 = 0x4c
    Release77 = 0x4d
    Release78 = 0x4e
    Release79 = 0x4f
    Release8 = 8
    Release80 = 80
    Release81 = 0x51
    Release82 = 0x52
    Release83 = 0x53
    Release84 = 0x54
    Release85 = 0x55
    Release86 = 0x56
    Release87 = 0x57
    Release88 = 0x58
    Release89 = 0x59
    Release9 = 9
    Release90 = 90
    Release91 = 0x5b
    Release92 = 0x5c
    Release93 = 0x5d
    Release94 = 0x5e
    Release95 = 0x5f
    Release96 = 0x60
    Release97 = 0x61
    Release98 = 0x62
    Release99 = 0x63
    ReleaseCheckExtended = 0x7d
    ReleaseCurrent = 0x99
    ReleaseExtendedCurrent = 0xcb
    ReleaseExtendedNewest = 1
    ReleaseMax = 0x7fffffff
    ReleaseNewest = 0x99
    ReleaseUnknown = 0x7ffffffe

class MatchProperties(object):
    """
    
    """
    def CopyProperties(self):
        """
        CopyProperties -> void
            
            Entity sourceEntity: 
            Input entity from which properties will be copied
            
            Entity targetEntity: 
            Input entity to which properties will be copied
            
            int flag: 
            Input bit flags indicating which properties to copy
        """
        pass
    
    pass

class Material(object):
    """
    
    Material()
    """
    Ambient = None
    
    
    Anonymous = None
    
    
    Bump = None
    
    
    ChannelFlags = None
    
    
    ColorBleedScale = None
    
    
    Description = None
    
    
    Diffuse = None
    
    
    FinalGather = None
    
    
    GlobalIllumination = None
    
    
    IlluminationModel = None
    
    
    IndirectBumpScale = None
    
    
    Luminance = None
    
    
    LuminanceMode = None
    
    
    Mode = None
    
    
    Name = None
    
    
    NormalMap = None
    
    
    Opacity = None
    
    
    ReflectanceScale = None
    
    
    Reflection = None
    
    
    Reflectivity = None
    
    
    Refraction = None
    
    
    SelfIllumination = None
    
    
    Specular = None
    
    
    Translucence = None
    
    
    TransmittanceScale = None
    
    
    TwoSided = None
    
    pass

class MeasurementValue():
    English = None
    Metric = None

class MergeCellStyleOption():
    ConvertDuplicatesToOverrrides = 4
    CopyDuplicates = 1
    IgnoreNewStyles = 8
    None = 0
    OverwriteDuplicates = 2

class MeshDataCollection(object):
    """
    
    MeshDataCollection()
    """
    ColorArray = None
    
    
    FaceArray = None
    
    
    MaterialIdArray = None
    
    
    VertexArray = None
    
    pass

class MeshFaceterData(object):
    """
    
    MeshFaceterData()
    """
    FaceterDevNormal = None
    
    
    FaceterDevSurface = None
    
    
    FaceterGridRatio = None
    
    
    FaceterMaxEdgeLength = None
    
    
    FaceterMaxGrid = None
    
    
    FaceterMeshType = None
    
    
    FaceterMinUGrid = None
    
    
    FaceterMinVGrid = None
    
    pass

class MeshPointMaps(object):
    """
    
    MeshPointMaps
        Point2dCollection sourcePts : Input source points collection
        Point2dCollection destPts : Input destination points collection
    """
    DestPonints = None
    
    
    SourcePonints = None
    
    pass

class MidPointConstraint(object):
    """
    
    MidPointConstraint()
    """

    pass

class Mline(object):
    """
    
    Mline()
    """
    def AppendSegment(self):
        """
        AppendSegment -> void
            
            Point3d newVertex: 
            Input new vertex point (in WCS) to be added
        """
        pass
    
    
    def Element(self):
        """
        Element -> Integer
            
            Point3d pt: 
            Input search point
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Point3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input point to find nearest point to
            
            Vector3d normal: 
            Input direction of projection
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input Boolean indicating if search should include "virtual" extension of Mline
            
            [MarshalAs(UnmanagedType.U1)] bool excludeCaps: 
            Input Boolean indicating if endcaps should not be included in nearest point search
        GetClosestPointTo(Point3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Point3d
            
            Point3d givenPoint: 
            Input point to find nearest point to
            
            [MarshalAs(UnmanagedType.U1)] bool extend: 
            Input Boolean indicating if search should include "virtual" extension of Mline
            
            [MarshalAs(UnmanagedType.U1)] bool excludeCaps: 
            Input Boolean indicating if endcaps should not be included in nearest point search
        """
        pass
    
    
    def MoveVertexAt(self):
        """
        MoveVertexAt -> void
            
            int index: 
            Input index of vertex to move in the vertex array
            
            Point3d newPosition: 
            Input new vertex value
        """
        pass
    
    
    def RemoveLastSegment(self):
        """
        RemoveLastSegment -> void
            
            Point3d lastVertex: 
            Returns filled in with the value of the vertex that becomes last when current last is removed
        """
        pass
    
    
    def VertexAt(self):
        """
        VertexAt -> Point3d
            
            int index: 
            Returns the value of the vertex at the index location (0 based) in the MLine object's vertex array.
        """
        pass
    
    
    IsClosed = None
    
    
    Justification = None
    
    
    Normal = None
    
    
    NumberOfVertices = None
    
    
    Scale = None
    
    
    Style = None
    
    
    SupressEndCaps = None
    
    
    SupressStartCaps = None
    
    pass

class MlineJustification():
    Top = None
    Zero = None
    Bottom = None

class MlineStyle(object):
    """
    
    MlineStyle()
    """
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            MlineStyle source: 
            Input MlineStyle to copy from
            
            [MarshalAs(UnmanagedType.U1)] bool checkIfReferenced: 
            Input Boolean indicating whether to check if the style is referenced
        """
        pass
    
    
    Description = None
    
    
    Elements = None
    
    
    EndAngle = None
    
    
    EndInnerArcs = None
    
    
    EndRoundCap = None
    
    
    EndSquareCap = None
    
    
    FillColor = None
    
    
    Filled = None
    
    
    Name = None
    
    
    ShowMiters = None
    
    
    StartAngle = None
    
    
    StartInnerArcs = None
    
    
    StartRoundCap = None
    
    
    StartSquareCap = None
    
    pass

class MlineStyleElement(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture specific format.
        """
        pass
    
    
    Color = None
    
    
    LinetypeId = None
    
    
    Offset = None
    
    pass

class MlineStyleElementCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            MlineStyleElement element: 
            Input element to add
            
            [MarshalAs(UnmanagedType.U1)] bool checkIfReferenced: 
            Input Boolean indicating whether to check if the style is referenced
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MlineStyleElement[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> MlineStyleElementCollectionEnumerator
        
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of item to remove
        """
        pass
    
    
    Count = None
    
    pass

class MlineStyleElementCollectionEnumerator(object):
    """
    
    MlineStyleElementCollectionEnumerator
        MlineStyleElementCollection col : Input collection to generate from
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

class ModelDocViewLabelAlignmentType():
    AlignmentLeft = None
    AlignmentCenter = None
    AlignmentRight = None

class ModelDocViewLabelAttachmentPoint():
    AboveView = None
    BelowView = None

class ModelerFlavor():
    Full = None
    RegionsOnly = None
    ObjectsOnly = None

class MoveType():
    MoveAllPoints = None
    MoveAllExceptArrowHeaderPoints = None
    MoveContentAndDoglegPoints = None

class MultiModesGripPE(object):
    """
    
    MultiModesGripPE()
    """
    class GripType():
        Primary = None
        Secondary = None
    
    
    def CurrentMode(self):
        """
        CurrentMode -> Autodesk.AutoCAD.DatabaseServices.GripMode
            
            Entity entity: 
            The Entity whose current mode is requested.
            
            GripData gripData: 
            The grip whose mode is requested.
        """
        pass
    
    
    def CurrentModeId(self):
        """
        CurrentModeId -> UInteger
            
            Entity entity: 
            The Entity whose current mode id is requested.
            
            GripData gripData: 
            The grip whose mode id is requested.
        """
        pass
    
    
    def GetGripModes(self):
        """
        GetGripModes -> bool
            
            Entity entity: 
            The Entity whose modes are requested. The object needs to be open at least for read.
            
            GripData gripData: 
            The grip whose modes are requested.
            
            GripModeCollection modes: 
            The returned collection of available modes.
            
            ref uint curMode: 
            The returned identifier of current mode.
        """
        pass
    
    
    def GetGripType(self):
        """
        GetGripType -> GripType
            
            Entity entity: 
            The Entity whose grip type is requested.
            
            GripData gripData: 
            The grip whose grip type is requested.
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
            
            Entity entity: 
            The Entity whose current mode is reset to default.
        """
        pass
    
    
    def SetCurrentMode(self):
        """
        SetCurrentMode -> bool
            
            Entity entity: 
            The Entity whose current mode is to be set current.
            
            GripData gripData: 
            The grip whose current mode is to be set current.
            
            uint curMode: 
            The numerical identifier for the new current mode.
        """
        pass
    
    pass

class NewLayerNotification():
    NoNewLayerNotification = 0
    NotifyOnInsert = 0x20
    NotifyOnLayerStateRestore = 8
    NotifyOnOpen = 2
    NotifyOnPlot = 1
    NotifyOnSave = 0x10
    NotifyOnXrefAttachAndReload = 4

class NormalConstraint(object):
    """
    
    NormalConstraint()
    """

    pass

class Notifier(object):
    """
    
    """
    def OnPropertyChanged(self):
        """
        OnPropertyChanged -> void
        
        """
        pass
    
    pass

class NurbSurface(object):
    """
    
    NurbSurface()()
    
    
    NurbSurface(int, int, [MarshalAs(UnmanagedType.U1)] bool, int, int, Point3dCollection, DoubleCollection, KnotCollection, KnotCollection)()
    
    
    """
    def Evaluate(self):
        """
        Evaluate(double, double) -> Point3d
        
        Evaluate(double, double, Point3d, Vector3d, Vector3d) -> void
        
        Evaluate(double, double, Point3d, Vector3d, Vector3d, Vector3d, Vector3d, Vector3d) -> void
        
        Evaluate(double, double, int, Point3d, Vector3dCollection) -> void
        
        """
        pass
    
    
    def GetControlPointAt(self):
        """
        GetControlPointAt -> Point3d
        
        """
        pass
    
    
    def GetIsolineAtU(self):
        """
        GetIsolineAtU -> Curve()
        
        """
        pass
    
    
    def GetIsolineAtV(self):
        """
        GetIsolineAtV -> Curve()
        
        """
        pass
    
    
    def GetNormal(self):
        """
        GetNormal -> Vector3d
        
        """
        pass
    
    
    def GetParameterOfPoint(self):
        """
        GetParameterOfPoint -> void
        
        """
        pass
    
    
    def GetWeight(self):
        """
        GetWeight -> double
        
        """
        pass
    
    
    def InsertControlPointsAtU(self):
        """
        InsertControlPointsAtU -> void
        
        """
        pass
    
    
    def InsertControlPointsAtV(self):
        """
        InsertControlPointsAtV -> void
        
        """
        pass
    
    
    def InsertKnotAtU(self):
        """
        InsertKnotAtU -> void
        
        """
        pass
    
    
    def InsertKnotAtV(self):
        """
        InsertKnotAtV -> void
        
        """
        pass
    
    
    def IsPlanar(self):
        """
        IsPlanar -> bool
        
        """
        pass
    
    
    def IsPointOnSurface(self):
        """
        IsPointOnSurface -> bool
        
        """
        pass
    
    
    def ModifyPosition(self):
        """
        ModifyPosition -> void
        
        """
        pass
    
    
    def ModifyPositionAndTangent(self):
        """
        ModifyPositionAndTangent -> void
        
        """
        pass
    
    
    def Rebuild(self):
        """
        Rebuild(int, int, int, int) -> void
        
        Rebuild(int, int, int, int, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def RemoveControlPointsAtU(self):
        """
        RemoveControlPointsAtU -> void
        
        """
        pass
    
    
    def RemoveControlPointsAtV(self):
        """
        RemoveControlPointsAtV -> void
        
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
        
        """
        pass
    
    
    def SetControlPointAt(self):
        """
        SetControlPointAt -> void
        
        """
        pass
    
    
    def SetControlPoints(self):
        """
        SetControlPoints -> void
        
        """
        pass
    
    
    def SetWeight(self):
        """
        SetWeight -> void
        
        """
        pass
    
    
    ControlPoints = None
    
    
    DegreeInU = None
    
    
    DegreeInV = None
    
    
    IsClosedInU = None
    
    
    IsClosedInV = None
    
    
    IsPeriodicInU = None
    
    
    IsPeriodicInV = None
    
    
    IsRational = None
    
    
    NumberOfControlPointsInU = None
    
    
    NumberOfControlPointsInV = None
    
    
    NumberOfKnotsInU = None
    
    
    NumberOfKnotsInV = None
    
    
    NumberOfSpansInU = None
    
    
    NumberOfSpansInV = None
    
    
    PeriodInU = None
    
    
    PeriodInV = None
    
    
    UKnots = None
    
    
    VKnots = None
    
    pass

class NurbsData(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to check against.
        """
        pass
    
    
    def GetControlPoints(self):
        """
        GetControlPoints -> Point3dCollection
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetKnots(self):
        """
        GetKnots -> DoubleCollection
        
        """
        pass
    
    
    def GetWeights(self):
        """
        GetWeights -> DoubleCollection
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(NurbsData) -> bool
            
            NurbsData other: 
            Object to check against.
        IsEqualTo(NurbsData, Tolerance) -> bool
            
            NurbsData other: 
            Object to check against.
            
            Tolerance tolerance: 
            Tolerance range
        """
        pass
    
    
    Closed = None
    
    
    ControlPointTolerance = None
    
    
    Degree = None
    
    
    KnotTolerance = None
    
    
    Periodic = None
    
    
    Rational = None
    
    pass

class ObjectContext(object):
    """
    
    """
    CollectionName = None
    
    
    Name = None
    
    
    UniqueIdentifier = None
    
    pass

class ObjectContextCollection(object):
    """
    
    """
    def AddContext(self):
        """
        AddContext -> void
            
            ObjectContext ctxt: 
            The context to copy and add to the collection.
        """
        pass
    
    
    def GetContext(self):
        """
        GetContext -> ObjectContext
            
            string contextName: 
            The name of the context to copy and return.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> ObjectContextCollectionEnumerator
        
        """
        pass
    
    
    def HasContext(self):
        """
        HasContext -> bool
            
            string contextName: 
            The name of the context to find.
        """
        pass
    
    
    def RemoveContext(self):
        """
        RemoveContext -> void
            
            string contextName: 
            The name of the context to remove from the collection.
        """
        pass
    
    
    CurrentContext = None
    
    
    Name = None
    
    pass

class ObjectContextCollectionEnumerator(object):
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

class ObjectContextManager(object):
    """
    
    ObjectContextManager()
    """
    def GetContextCollection(self):
        """
        GetContextCollection -> ObjectContextCollection
            
            string collectionName: 
            The name of the desired collection.
        """
        pass
    
    
    def RegisterContextCollection(self):
        """
        RegisterContextCollection -> void
            
            string collectionName: 
            The name of the collection to register with the manager.
            
            ObjectContextCollection collection: 
            The collection to register with the manager.
        """
        pass
    
    
    def UnregisterContextCollection(self):
        """
        UnregisterContextCollection -> void
            
            string collectionName: 
            The name of the collection to unregister with the manager.
        """
        pass
    
    pass

class ObjectErasedEventArgs(object):
    """
    
    """
    DBObject = None
    
    
    Erased = None
    
    pass

class ObjectEventArgs(object):
    """
    
    """
    DBObject = None
    
    pass

class ObjectId(object):
    """
    
    ObjectId
        IntPtr oldId : Input pointer to construct from
    """
    def Compare(self):
        """
        Compare -> bool
            
            ObjectId value1: 
            Input object to compare against
        """
        pass
    
    
    def ConvertToRedirectedId(self):
        """
        ConvertToRedirectedId -> ObjectId
        
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetMetaObject(self):
        """
        GetMetaObject -> DynamicMetaObject
        
        """
        pass
    
    
    Database = None
    
    
    Handle = None
    
    
    IsEffectivelyErased = None
    
    
    IsErased = None
    
    
    IsNull = None
    
    
    IsResident = None
    
    
    IsValid = None
    
    
    NonForwardedHandle = None
    
    
    Null = None
    
    
    ObjectClass = None
    
    
    OldIdPtr = None
    
    
    OriginalDatabase = None
    
    
    IsWellBehaved = None
    
    
    OldId = None
    
    pass

class ObjectIdCollection(object):
    """
    
    ObjectIdCollection()()
    
    
    """
    def Add(self):
        """
        Add -> Integer
            
            ObjectId value: 
            Item to add
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
            
            ObjectId value: 
            Item to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectId[] array: 
            Array to copy from
            
            int index: 
            Index to begin at
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
            
            ObjectId value: 
            Item to search for
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Index to insert at
            
            ObjectId value: 
            Item to add
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            ObjectId value: 
            Object to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Index of object to remove
        """
        pass
    
    
    Count = None
    
    pass

class ObjectIdGraph(object):
    """
    
    ObjectIdGraph()
    """
    def AddNode(self):
        """
        AddNode -> void
            
            ObjectIdGraphNode nodeToAdd: 
            Input ObjectIdGraphNode to add to the graph.
        """
        pass
    
    
    def DelNode(self):
        """
        DelNode -> void
            
            nodeToAdd: 
            Input ObjectIdGraphNode to remove from the graph.
        """
        pass
    
    
    def FindNode(self):
        """
        FindNode -> ObjectIdGraphNode
            
            ObjectId id: 
            Input ObjectId for node to find.
        """
        pass
    
    
    def IdNode(self):
        """
        IdNode -> ObjectIdGraphNode
            
            int index: 
            Input zero based index of the node to get.
        """
        pass
    
    pass

class ObjectIdGraphNode(object):
    """
    
    ObjectIdGraphNode
        ObjectId id : Input ObjectId that the node will contain.
    """
    def Create(self):
        """
        Create -> ObjectIdGraphNode
            
            IntPtr unmanagedPointer: 
            Input pointer to the AcDbObjectIdGraphNode object that the new ObjectIdGraphNode will wrap.
            
            [MarshalAs(UnmanagedType.U1)] bool autoDelete: 
            Input boolean indicating whether the wrapped AcDbObjectIdGraphNode should be deleted when this ObjectIdGraphNode is destroyed.
        """
        pass
    
    
    Id = None
    
    pass

class ObjectOverrule(object):
    """
    
    """
    def Cancel(self):
        """
        Cancel -> void
        
        """
        pass
    
    
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def DeepClone(self):
        """
        DeepClone -> DBObject
        
        """
        pass
    
    
    def Erase(self):
        """
        Erase -> void
        
        """
        pass
    
    
    def Open(self):
        """
        Open -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def WblockClone(self):
        """
        WblockClone -> DBObject
        
        """
        pass
    
    pass

class ObjectSnapContext(object):
    """
    
    """
    GraphicsSystemSelectionMark = None
    
    
    LastPoint = None
    
    
    PickedObject = None
    
    
    PickPoint = None
    
    
    ViewTransform = None
    
    pass

class ObjectSnapInfo(object):
    """
    
    """
    SnapCurves = None
    
    
    SnapPoints = None
    
    pass

class ObjectSnapModes():
    ModeCenter = 3
    ModeEnd = 1
    ModeIns = 7
    ModeMid = 2
    ModeNear = 10
    ModeNode = 4
    ModePerpendicular = 8
    ModeQuad = 5
    ModeTangent = 9

class ObjectTypeAttribute(object):
    """
    
    ObjectTypeAttribute
        Type type : Object type
    """
    ObjectType = None
    
    pass

class Ole2Frame(object):
    """
    
    Ole2Frame()
    """
    class ItemType():
        Embedded = 2
        Link = 1
        Static = 3
    
    
    AutoOutputQuality = None
    
    
    IsLinked = None
    
    
    LinkName = None
    
    
    LinkPath = None
    
    
    Location = None
    
    
    LockAspect = None
    
    
    OleObject = None
    
    
    OutputQuality = None
    
    
    Position2d = None
    
    
    Position3d = None
    
    
    Rotation = None
    
    
    ScaleHeight = None
    
    
    ScaleWidth = None
    
    
    Type = None
    
    
    UserType = None
    
    
    WcsHeight = None
    
    
    WcsWidth = None
    
    pass

class OpenCloseTransaction(object):
    """
    
    """
    def Abort(self):
        """
        Abort -> void
        
        """
        pass
    
    
    def AddNewlyCreatedDBObject(self):
        """
        AddNewlyCreatedDBObject -> void
            
            DBObject obj: 
            Input object to be added or removed
            
            [MarshalAs(UnmanagedType.U1)] bool add: 
            Input Boolean indicating whether to add or remove the object
        """
        pass
    
    
    def Commit(self):
        """
        Commit -> void
        
        """
        pass
    
    
    def GetObject(self):
        """
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
            
            [MarshalAs(UnmanagedType.U1)] bool forceOpenOnLockedLayer: 
            Input true if locked layers should be opened
        """
        pass
    
    
    TransactionManager = None
    
    pass

class OpenMode():
    ForRead = None
    ForWrite = None
    ForNotify = None

class OpenModeAttribute(object):
    """
    
    OpenModeAttribute
        Autodesk.AutoCAD.DatabaseServices.OpenMode mode : Mode of open object
    """
    OpenMode = None
    
    pass

class OrthographicView():
    NonOrthoView = None
    TopView = None
    BottomView = None
    FrontView = None
    BackView = None
    LeftView = None
    RightView = None

class OsnapOverrule(object):
    """
    
    """
    def GetObjectSnapPoints(self):
        """
        GetObjectSnapPoints(Entity, ObjectSnapModes, IntPtr, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection) -> void
        
        GetObjectSnapPoints(Entity, ObjectSnapModes, IntPtr, Point3d, Point3d, Matrix3d, Point3dCollection, IntegerCollection, Matrix3d) -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class PCAdsName(object):
    """
    
    """

    pass

class PaperOrientationStates():
    NotApplicable = None

class ParallelConstraint(object):
    """
    
    ParallelConstraint()
    """

    pass

class ParseOption():
    ParseOptionNone = None
    SetDefaultFormat = None
    PreserveMtextFormat = None

class PasswordOptions():
    Default = None
    UpperCase = None
    IsExternalReference = None

class PathOption():
    AbsolutePath = 3
    NoPath = 1
    PathAndFile = 4
    RelativePath = 2

class PathRef(object):
    """
    
    PathRef()()
    
    
    PathRef(EdgeRef[])()
    
    
    PathRef(FullSubentityPath[], FullSubentityPath[])()
    
    
    """
    def GetEntityArray(self):
        """
        GetEntityArray -> Entity()
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
        
        """
        pass
    
    
    def IsReferencePath(self):
        """
        IsReferencePath -> bool
        
        """
        pass
    
    
    EdgeRefs = None
    
    pass

class PatternDefinition(object):
    """
    
    PatternDefinition
        double patternAngle : Input pattern angle
        Point2d basePoint : Input base coordinates
        Point2d offsetVector : Input offset coordinates
        DoubleCollection dashOffsets : Input dash offsets
    """
    def GetDashes(self):
        """
        GetDashes -> DoubleCollection
        
        """
        pass
    
    
    Angle = None
    
    
    BaseX = None
    
    
    BaseY = None
    
    
    OffsetX = None
    
    
    OffsetY = None
    
    pass

class PdfDefinition(object):
    """
    
    PdfDefinition()
    """

    pass

class PdfReference(object):
    """
    
    PdfReference()
    """

    pass

class PerpendicularConstraint(object):
    """
    
    PerpendicularConstraint()
    """

    pass

class PhysicalIntensityMethod():
    PeakIntensity = None
    Flux = None
    Illuminance = None

class PlaceHolder(object):
    """
    
    PlaceHolder()
    """

    pass

class Planarity():
    NonPlanar = None
    Planar = None
    Linear = None

class PlaneSurface(object):
    """
    
    PlaneSurface()
    """
    def CreateFromRegion(self):
        """
        CreateFromRegion -> void
            
            Region region: 
            Input pointer to any Region object
        """
        pass
    
    pass

class PlotPaperUnit():
    Inches = None
    Millimeters = None
    Pixels = None

class PlotRotation():
    Degrees000 = None
    Degrees090 = None
    Degrees180 = None
    Degrees270 = None

class PlotSettings(object):
    """
    
    PlotSettings
        [MarshalAs(UnmanagedType.U1)] bool modelType : Input Boolean that determines the plot setup type
    """
    def AddToPlotSettingsDictionary(self):
        """
        AddToPlotSettingsDictionary -> void
            
            Database toWhichDatabase: 
            Input database to which to add plot settings object
        """
        pass
    
    
    def SetShadePlot(self):
        """
        SetShadePlot -> void
            
            PlotSettingsShadePlotType type: 
            Input type of the shade plot object
            
            ObjectId shadePlotId: 
            Input object ID of the VisualStyle or RenderSettings object to be used as the shade plot object
        """
        pass
    
    
    CanonicalMediaName = None
    
    
    CurrentStyleSheet = None
    
    
    CustomPrintScale = None
    
    
    DrawViewportsFirst = None
    
    
    ModelType = None
    
    
    PlotAsRaster = None
    
    
    PlotCentered = None
    
    
    PlotConfigurationName = None
    
    
    PlotHidden = None
    
    
    PlotOrigin = None
    
    
    PlotPaperMargins = None
    
    
    PlotPaperSize = None
    
    
    PlotPaperUnits = None
    
    
    PlotPlotStyles = None
    
    
    PlotRotation = None
    
    
    PlotSettingsName = None
    
    
    PlotType = None
    
    
    PlotViewName = None
    
    
    PlotViewportBorders = None
    
    
    PlotWindowArea = None
    
    
    PlotWireframe = None
    
    
    PrintLineweights = None
    
    
    ScaleLineweights = None
    
    
    ShadePlot = None
    
    
    ShadePlotCustomDpi = None
    
    
    ShadePlotId = None
    
    
    ShadePlotResLevel = None
    
    
    ShowPlotStyles = None
    
    
    StdScale = None
    
    
    StdScaleType = None
    
    
    UseStandardScale = None
    
    pass

class PlotSettingsShadePlotType():
    AsDisplayed = None
    Wireframe = None
    Hidden = None
    Rendered = None
    VisualStyle = None
    RenderPreset = None

class PlotSettingsValidator(object):
    """
    
    """
    def GetCanonicalMediaNameList(self):
        """
        GetCanonicalMediaNameList -> StringCollection
            
            PlotSettings plotSet: 
            Input pointer to PlotSettings object
        """
        pass
    
    
    def GetLocaleMediaName(self):
        """
        GetLocaleMediaName(PlotSettings, int) -> string
            
            PlotSettings plotSet: 
            Input
            
            int index: 
            Input index into collection returned by GetCanonicalMediaNameList()
        GetLocaleMediaName(PlotSettings, string) -> string
            
            PlotSettings plotSet: 
            Input
            
            string canonicalName: 
            Input locale independent media name identifier (item type returned by GetCanonicalMediaNameList())
        """
        pass
    
    
    def GetPlotDeviceList(self):
        """
        GetPlotDeviceList -> StringCollection
        
        """
        pass
    
    
    def GetPlotStyleSheetList(self):
        """
        GetPlotStyleSheetList -> StringCollection
        
        """
        pass
    
    
    def RefreshLists(self):
        """
        RefreshLists -> void
            
            PlotSettings plotSet: 
            Input
        """
        pass
    
    
    def SetCanonicalMediaName(self):
        """
        SetCanonicalMediaName -> void
            
            PlotSettings plotSet: 
            Input
            
            string mediaName: 
            Input pointer to canonical media name
        """
        pass
    
    
    def SetClosestMediaName(self):
        """
        SetClosestMediaName -> void
            
            PlotSettings plotSet: 
            _nt_
            
            double paperWidth: 
            _nt_
            
            double paperHeight: 
            _nt_
            
            PlotPaperUnit units: 
            _nt_
            
            [MarshalAs(UnmanagedType.U1)] bool matchPrintableArea: 
            _nt_
        """
        pass
    
    
    def SetCurrentStyleSheet(self):
        """
        SetCurrentStyleSheet -> void
            
            PlotSettings plotSet: 
            Input
            
            string styleSheetName: 
            Input pointer to plot style table name
        """
        pass
    
    
    def SetCustomPrintScale(self):
        """
        SetCustomPrintScale -> void
            
            PlotSettings plotSet: 
            Input
            
            CustomScale scale: 
            Input paperspace units
        """
        pass
    
    
    def SetDefaultPlotConfig(self):
        """
        SetDefaultPlotConfig -> void
            
            PlotSettings plotSet: 
            Input
        """
        pass
    
    
    def SetPlotCentered(self):
        """
        SetPlotCentered -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            [MarshalAs(UnmanagedType.U1)] bool isCentered: 
            Input Boolean indicating whether the plot should be centered
        """
        pass
    
    
    def SetPlotConfigurationName(self):
        """
        SetPlotConfigurationName -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            string plotDeviceName: 
            Input pointer to plot device name
            
            string mediaName: 
            Input media name
        """
        pass
    
    
    def SetPlotOrigin(self):
        """
        SetPlotOrigin -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Point2d origin: 
            Input offset coordinates
        """
        pass
    
    
    def SetPlotPaperUnits(self):
        """
        SetPlotPaperUnits -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            PlotPaperUnit units: 
            Input units by which the margins, offset, and paper size are interpreted
        """
        pass
    
    
    def SetPlotViewName(self):
        """
        SetPlotViewName -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            string viewName: 
            Input named view indicating the portion of the model to plot
        """
        pass
    
    
    def SetPlotWindowArea(self):
        """
        SetPlotWindowArea -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Extents2d windowArea: 
            Input window coordinates (coordinates must be in DCS)
        """
        pass
    
    
    def SetStdScale(self):
        """
        SetStdScale -> void
            
            PlotSettings plotSet: 
            Input
            
            double standardScale: 
            Input standard scale value
        """
        pass
    
    
    def SetUseStandardScale(self):
        """
        SetUseStandardScale -> void
            
            PlotSettings plotSet: 
            Input
            
            [MarshalAs(UnmanagedType.U1)] bool useStandard: 
            Input Boolean indicating whether to use standard scale
        """
        pass
    
    
    def SetZoomToPaperOnUpdate(self):
        """
        SetZoomToPaperOnUpdate -> void
            
            PlotSettings plotSet: 
            Input
            
            [MarshalAs(UnmanagedType.U1)] bool doZoom: 
            Input Boolean indicating whether to zoom
        """
        pass
    
    
    def SetPlotRotation(self):
        """
        SetPlotRotation -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Autodesk.AutoCAD.DatabaseServices.PlotRotation rotationType: 
            Input enumeration indicating rotation
        """
        pass
    
    
    def SetPlotType(self):
        """
        SetPlotType -> void
            
            PlotSettings plotSet: 
            Input PlotSettings object
            
            Autodesk.AutoCAD.DatabaseServices.PlotType plotAreaType: 
            Input enumeration indicating the portion of the layout to plot
        """
        pass
    
    
    def SetStdScaleType(self):
        """
        SetStdScaleType -> void
            
            PlotSettings plotSet: 
            Input plot set
            
            Autodesk.AutoCAD.DatabaseServices.StdScaleType scaleType: 
            Input standard scale
            CustomScale: 
            Scale is not a standard scale
            Scale1To128inAnd1ft: 
            1/128"= 1'
            Scale1To32inchAnd1ft: 
            1/32"= 1'
            StdScale3To32InchIs1ft: 
            3/32"= 1'
            StdScale3To16InchIs1ft: 
            3/16"= 1'
            StdScale3To8InchIs1ft: 
            3/8" = 1'
            StdScale3To4InchIs1ft: 
            3/4" = 1'
            Scale3inIs1ft: 
            3"= 1'
            Scale1ftIs1ft: 
            1'= 1'
            Scale1To4: 
            1:4
            Scale1To10: 
            1:10
            Scale1To20: 
            1:20
            Scale1To30: 
            1:40
            Scale1To100: 
            1:100
            Scale4To1: 
            4:1
            Scale10To1: 
            10:1
            Scale1000To1: 
            1000:1
        """
        pass
    
    
    Current = None
    
    pass

class PlotStyleDescriptor(object):
    """
    
    PlotStyleDescriptor
        ObjectId id : Object ID of plot to create from
        Autodesk.AutoCAD.DatabaseServices.PlotStyleNameType type : New type of plot style name
    """
    def Equals(self):
        """
        Equals -> bool
            
            object unmanagedObjPtr: 
            Object to compare with
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Culture-specific format
        """
        pass
    
    
    Id = None
    
    
    Type = None
    
    pass

class PlotStyleNameType():
    PlotStyleNameByLayer = None
    PlotStyleNameByBlock = None
    PlotStyleNameIsDictionaryDefault = None
    PlotStyleNameById = None

class PlotStyleTableChangedEventArgs(object):
    """
    
    """
    Id = None
    
    
    NewName = None
    
    pass

class PlotType():
    Display = None
    Extents = None
    Limits = None
    View = None
    Window = None
    Layout = None

class Point3AngularDimension(object):
    """
    
    Point3AngularDimension()()
    
    
    """
    ArcPoint = None
    
    
    CenterPoint = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

class PointCloud(object):
    """
    
    PointCloud()
    """
    def RegenPointClouds(self):
        """
        RegenPointClouds -> void
        
        """
        pass
    
    pass

class PointCloudClassificationColorRamp(object):
    """
    
    PointCloudClassificationColorRamp()
    """
    def Color(self):
        """
        Color -> EntityColor
        
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
        
        """
        pass
    
    
    def SetFrom(self):
        """
        SetFrom -> void
        
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
        
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> bool
        
        """
        pass
    
    
    Name = None
    
    
    NumColors = None
    
    pass

class PointCloudColorMap(object):
    """
    
    """
    def ClassificationColorSchemeInUse(self):
        """
        ClassificationColorSchemeInUse -> string()
        
        """
        pass
    
    
    def ClassificationScheme(self):
        """
        ClassificationScheme -> bool
        
        """
        pass
    
    
    def ColorScheme(self):
        """
        ColorScheme -> bool
        
        """
        pass
    
    
    def ColorSchemeInUse(self):
        """
        ColorSchemeInUse -> string()
        
        """
        pass
    
    
    def DeleteClassificationScheme(self):
        """
        DeleteClassificationScheme -> bool
        
        """
        pass
    
    
    def DeleteColorScheme(self):
        """
        DeleteColorScheme -> bool
        
        """
        pass
    
    
    def GetColorMapId(self):
        """
        GetColorMapId -> ObjectId
        
        """
        pass
    
    
    def HasClassificationScheme(self):
        """
        HasClassificationScheme -> bool
        
        """
        pass
    
    
    def HasColorScheme(self):
        """
        HasColorScheme -> bool
        
        """
        pass
    
    
    def SetClassificationScheme(self):
        """
        SetClassificationScheme -> bool
        
        """
        pass
    
    
    def SetColorScheme(self):
        """
        SetColorScheme -> bool
        
        """
        pass
    
    
    ClassificationSchemeGUIDs = None
    
    
    ColorSchemeGUIDs = None
    
    
    DefaultClassificationColorScheme = None
    
    
    DefaultElevationColorScheme = None
    
    
    DefaultIntensityColorScheme = None
    
    pass

class PointCloudColorRamp(object):
    """
    
    PointCloudColorRamp()
    """
    def Color(self):
        """
        Color -> EntityColor
        
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
        
        """
        pass
    
    
    def SetFrom(self):
        """
        SetFrom -> void
        
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
        
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> bool
        
        """
        pass
    
    
    Name = None
    
    
    NumColors = None
    
    pass

class PointCloudCrop(object):
    """
    
    """
    def Clear(self):
        """
        Clear -> void
        
        """
        pass
    
    
    def Create(self):
        """
        Create -> PointCloudCrop
            
            IntPtr unmanagedObjPtr: 
            Specifies the AcDbPointCloudCrop pointer. For a valid pointer, it binds the created PointCloudCrop with it; if it is System::IntPtr::Zero, it creates a non-binded PointCloudCrop.
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def IsValid(self):
        """
        IsValid -> bool
        
        """
        pass
    
    
    CropPlane = None
    
    
    CropType = None
    
    
    Inside = None
    
    
    Inverted = None
    
    
    Vertices = None
    
    pass

class PointCloudCropType():
    Invalid = None
    Rectangular = None
    Polygonal = None
    Circular = None

class PointCloudDefEx(object):
    """
    
    PointCloudDefEx()
    """
    def classVersion(self):
        """
        classVersion -> Integer
        
        """
        pass
    
    
    def getAllRcsFilePaths(self):
        """
        getAllRcsFilePaths -> string()
        
        """
        pass
    
    
    def getRcsFilePath(self):
        """
        getRcsFilePath -> string
            
            string guid: 
            Specifies the GUID of the RCS
        """
        pass
    
    
    def load(self):
        """
        load -> bool
        
        """
        pass
    
    
    def unload(self):
        """
        unload -> bool
        
        """
        pass
    
    
    ActiveFileName = None
    
    
    defaultHeight = None
    
    
    defaultLength = None
    
    
    defaultWidth = None
    
    
    EntityCount = None
    
    
    extents = None
    
    
    FileType = None
    
    
    SourceFileName = None
    
    
    totalPointsCount = None
    
    
    totalRegionsCount = None
    
    
    totalScansCount = None
    
    pass

class PointCloudDispOptionOutOfRange():
    UseMinMaxColors = None
    UseRGBScanColors = None
    HidePoints = None

class PointCloudEx(object):
    """
    
    PointCloudEx()
    """
    def addCroppingBoundary(self):
        """
        addCroppingBoundary -> void
            
            PointCloudCrop cropping: 
            An AcDbPointCloudCrop object which is to be added.
        """
        pass
    
    
    def AttachPointCloud(self):
        """
        AttachPointCloud -> ObjectId
            
            string filename: 
            Point cloud source file path. This represent the original filepath use to cerate the index. This entry can be blank.
            
            Point3d location: 
            Location of point cloud entity. If entity is inserted at 0,0,0 the points will appear where they are located in the point cloud.
            
            double scale: 
            Scale factor. 1.0 is default scale, and cannot less than 0.0
            
            double rotation: 
            Rotation Angle in degrees. 0 is default rotation
            
            Database db: 
            Returns object id of created PointCloudEx
        """
        pass
    
    
    def clearCropping(self):
        """
        clearCropping -> bool
        
        """
        pass
    
    
    def findRegionItem(self):
        """
        findRegionItem -> PointCloudItem
            
            int regionId: 
            The region ID to be returned.
        """
        pass
    
    
    def findScanItem(self):
        """
        findScanItem -> PointCloudItem
        
        """
        pass
    
    
    def GetColorSchemeForStylization(self):
        """
        GetColorSchemeForStylization -> string
            
            PointCloudStylizationType type: 
            Indicates a stylization type.
        """
        pass
    
    
    def getCroppingCount(self):
        """
        getCroppingCount -> Integer
        
        """
        pass
    
    
    def getPointCloudCropping(self):
        """
        getPointCloudCropping -> PointCloudCrop
        
        """
        pass
    
    
    def getPointCloudDataList(self):
        """
        getPointCloudDataList -> List<PointCloudItem>
        
        """
        pass
    
    
    def GetScanViewInfo(self):
        """
        GetScanViewInfo -> bool
        
        """
        pass
    
    
    def HasProperty(self):
        """
        HasProperty -> PointCloudPropertyState
        
        """
        pass
    
    
    def removeLastCropping(self):
        """
        removeLastCropping -> bool
        
        """
        pass
    
    
    def setAllRegionsVisibility(self):
        """
        setAllRegionsVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            The visibility for all regions.
            
            [MarshalAs(UnmanagedType.U1)] bool includeUnassigned: 
            true or false, whether or not set the bVisible to unassigned points
        """
        pass
    
    
    def setAllScansVisibility(self):
        """
        setAllScansVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            The visibility of all scans.
        """
        pass
    
    
    def SetColorSchemeForStylization(self):
        """
        SetColorSchemeForStylization -> void
            
            string name: 
            Indicates the name of a color scheme to be set.
            
            PointCloudStylizationType type: 
            Indicates a stylization type
        """
        pass
    
    
    def setRegionVisibility(self):
        """
        setRegionVisibility -> void
            
            int regionId: 
            The region ID
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            The region's visibility
        """
        pass
    
    
    def setScanVisibility(self):
        """
        setScanVisibility -> void
            
            string scanGuid: 
            The scan GUID
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            Whether or not the scan is visible
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> bool
            
            Matrix3d xform: 
            The input transform matrix.
        """
        pass
    
    
    ActiveFileName = None
    
    
    CroppingInverted = None
    
    
    CurrentColorScheme = None
    
    
    ElevationApplyToFixedRange = None
    
    
    ElevationGradient = None
    
    
    ElevationOutOfRangeBehavior = None
    
    
    GeomExtents = None
    
    
    IntensityGradient = None
    
    
    IntensityOutOfRangeBehavior = None
    
    
    LimitBoxBound = None
    
    
    Location = None
    
    
    MinMaxElevation = None
    
    
    MinMaxIntensity = None
    
    
    NativeExtents = None
    
    
    PointCloudDefExId = None
    
    
    Rotation = None
    
    
    Scale = None
    
    
    ShowCropped = None
    
    
    Stylization = None
    
    pass

class PointCloudItem(object):
    """
    
    PointCloudItem()
    """
    def Clone(self):
        """
        Clone -> PointCloudItem
        
        """
        pass
    
    
    def CompareTo(self):
        """
        CompareTo -> bool
            
            PointCloudItem other: 
            The second point cloud item for comparison.
        """
        pass
    
    
    def CreatePointCloudDataItemCollection(self):
        """
        CreatePointCloudDataItemCollection -> List<PointCloudItem>
            
            IntPtr unmanagedObjPtr: 
            The pointer of array of AcPointCloudItem
        """
        pass
    
    
    def modopt(self):
        """
        modopt -> ValueType
        
        """
        pass
    
    
    def ToCmdString(self):
        """
        ToCmdString -> string
        
        """
        pass
    
    
    CategoryId = None
    
    
    Guid = None
    
    
    ItemId = None
    
    
    Name = None
    
    
    ProjectName = None
    
    
    Visibility = None
    
    pass

class PointCloudItemType():
    LegacyPointCloud = None
    PointCloudProject = None
    IndividualScan = None
    Scan = None
    Region = None
    ScanRootGroup = None
    RegionRootGroup = None
    UnassignedPoint = None

class PointCloudProperty():
    Classification = 3
    Color = 1
    Intensity = 2
    Normal = 4

class PointCloudPropertyState():
    All = 1
    None = -1
    Some = 0

class PointCloudStylizationType():
    ClassificationRamp = 6
    HeightRamp = 4
    IntensityRamp = 5
    NormalRamp = 3
    SingleColor = 2
    TrueColor = 1

class PointCoincidenceConstraint(object):
    """
    
    PointCoincidenceConstraint()
    """

    pass

class PointCurveConstraint(object):
    """
    
    PointCurveConstraint()
    """

    pass

class Poly2dType():
    SimplePoly = None
    FitCurvePoly = None
    QuadSplinePoly = None
    CubicSplinePoly = None

class Poly3dType():
    SimplePoly = None
    QuadSplinePoly = None
    CubicSplinePoly = None

class PolyFaceMesh(object):
    """
    
    PolyFaceMesh()
    """
    def AppendFaceRecord(self):
        """
        AppendFaceRecord -> ObjectId
            
            FaceRecord toAppend: 
            Input FaceRecord to append to the mesh
        """
        pass
    
    
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            PolyFaceMeshVertex vertexToAppend: 
            Input vertex to append to mesh
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    NumFaces = None
    
    
    NumVertices = None
    
    pass

class PolyFaceMeshVertex(object):
    """
    
    PolyFaceMeshVertex()()
    
    
    PolyFaceMeshVertex(Point3d)
        Point3d position : Input WCS position point for the vertex
    
    
    """
    Position = None
    
    pass

class PolyMeshType():
    BezierSurfaceMesh = 8
    CubicSurfaceMesh = 6
    QuadSurfaceMesh = 5
    SimpleMesh = 0

class PolygonMesh(object):
    """
    
    PolygonMesh()()
    
    
    """
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            PolygonMeshVertex toAppend: 
            Input vertex to append to mesh
        """
        pass
    
    
    def ConvertToPolyMeshType(self):
        """
        ConvertToPolyMeshType -> void
            
            Autodesk.AutoCAD.DatabaseServices.PolyMeshType newVal: 
            Input type to which the polygon mesh should be converted
            SimpleMesh: 
            Plain mesh with no surface fitting or smoothing
            QuadSurfaceMesh: 
            Quadratic B-spline surface fit
            CubicSurfaceMesh: 
            Cubic B-spline surface fit
            BezierSurfaceMesh: 
            Bezier surface fit
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def MakeMClosed(self):
        """
        MakeMClosed -> void
        
        """
        pass
    
    
    def MakeMOpen(self):
        """
        MakeMOpen -> void
        
        """
        pass
    
    
    def MakeNClosed(self):
        """
        MakeNClosed -> void
        
        """
        pass
    
    
    def MakeNOpen(self):
        """
        MakeNOpen -> void
        
        """
        pass
    
    
    def Straighten(self):
        """
        Straighten -> void
        
        """
        pass
    
    
    def SurfaceFit(self):
        """
        SurfaceFit() -> void
        
        """
        pass
    
    
    IsMClosed = None
    
    
    IsNClosed = None
    
    
    MSize = None
    
    
    MSurfaceDensity = None
    
    
    NSize = None
    
    
    NSurfaceDensity = None
    
    
    PolyMeshType = None
    
    pass

class PolygonMeshVertex(object):
    """
    
    PolygonMeshVertex()()
    
    
    PolygonMeshVertex(Point3d)
        Point3d point : Input WCS position point for the vertex
    
    
    """
    Position = None
    
    
    VertexType = None
    
    pass

class Polyline(object):
    """
    
    Polyline()()
    
    
    Polyline(int)
        int vertices : Input number of vertices to allocate memory for
    
    
    """
    def AddVertexAt(self):
        """
        AddVertexAt -> void
            
            int index: 
            Input index (0 based) before which to insert the vertex
            
            Point2d pt: 
            Input vertex location point
            
            double bulge: 
            Input bulge value for vertex
            
            double startWidth: 
            Input start width for vertex
            
            double endWidth: 
            Input end width for vertex
        """
        pass
    
    
    def ConvertFrom(self):
        """
        ConvertFrom -> void
            
            Entity entity: 
            Input pointer to the Polyline2d to copy from
            
            [MarshalAs(UnmanagedType.U1)] bool transferId: 
            Input Boolean indicating whether or not to do a HandOverTo between the Polyline2d and the Polyline
        """
        pass
    
    
    def ConvertTo(self):
        """
        ConvertTo -> Polyline2d
            
            [MarshalAs(UnmanagedType.U1)] bool transferId: 
            Input Boolean indicating whether or not to do a handOverTo between the Polyline and the Polyline2d.
        """
        pass
    
    
    def GetArcSegment2dAt(self):
        """
        GetArcSegment2dAt -> CircularArc2d
            
            int index: 
            Input index (0 based) of the vertex for start of arc
        """
        pass
    
    
    def GetArcSegmentAt(self):
        """
        GetArcSegmentAt -> CircularArc3d
            
            int index: 
            Input index (0 based) of the vertex for start of arc
        """
        pass
    
    
    def GetBulgeAt(self):
        """
        GetBulgeAt -> double
            
            int index: 
            Input index (0 based) of the vertex for start of bulge
        """
        pass
    
    
    def GetEndWidthAt(self):
        """
        GetEndWidthAt -> double
            
            int index: 
            Input index (0 based) of the polyline
        """
        pass
    
    
    def GetLineSegment2dAt(self):
        """
        GetLineSegment2dAt -> LineSegment2d
            
            int index: 
            Input index (0 based) of the vertex for start of segment
        """
        pass
    
    
    def GetLineSegmentAt(self):
        """
        GetLineSegmentAt -> LineSegment3d
            
            int index: 
            Input index (0 based) of the vertex for start of segment
        """
        pass
    
    
    def GetPoint2dAt(self):
        """
        GetPoint2dAt -> Point2d
            
            int index: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def GetPoint3dAt(self):
        """
        GetPoint3dAt -> Point3d
            
            int value: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def GetSegmentType(self):
        """
        GetSegmentType -> SegmentType
            
            int index: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def GetStartWidthAt(self):
        """
        GetStartWidthAt -> double
            
            int index: 
            Input index (0 based) of the vertex
        """
        pass
    
    
    def MaximizeMemory(self):
        """
        MaximizeMemory -> void
        
        """
        pass
    
    
    def MinimizeMemory(self):
        """
        MinimizeMemory -> void
        
        """
        pass
    
    
    def OnSegmentAt(self):
        """
        OnSegmentAt -> bool
            
            int index: 
            Input index (0 based) of the vertex
            
            Point2d pt2d: 
            Input point (in polyline OCS coords) to check at vertex index
            
            double value: 
            Output parameter of at vertex index
        """
        pass
    
    
    def RemoveVertexAt(self):
        """
        RemoveVertexAt -> void
            
            int index: 
            Input index (0 based) of the vertex to remove
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
            
            [MarshalAs(UnmanagedType.U1)] bool reuse: 
            Input Boolean indicating whether or not to retain some vertices
            
            int vertices: 
            Input number of vertices to retain
        """
        pass
    
    
    def SetBulgeAt(self):
        """
        SetBulgeAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            double bulge: 
            Input bulge value for the vertex
        """
        pass
    
    
    def SetEndWidthAt(self):
        """
        SetEndWidthAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            double endWidth: 
            Input end width value for vertex index
        """
        pass
    
    
    def SetPointAt(self):
        """
        SetPointAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            Point2d pt: 
            Input location for the vertex
        """
        pass
    
    
    def SetStartWidthAt(self):
        """
        SetStartWidthAt -> void
            
            int index: 
            Input index (0 based) of the vertex
            
            double startWidth: 
            Input start width value for vertex index
        """
        pass
    
    
    Closed = None
    
    
    ConstantWidth = None
    
    
    Elevation = None
    
    
    HasBulges = None
    
    
    HasWidth = None
    
    
    IsOnlyLines = None
    
    
    Length = None
    
    
    Normal = None
    
    
    NumberOfVertices = None
    
    
    Plinegen = None
    
    
    Thickness = None
    
    pass

class Polyline2d(object):
    """
    
    Polyline2d()()
    
    
    """
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            Vertex2d vertexToAppend: 
            Input the vertex to add to the polyline
        """
        pass
    
    
    def ConvertToPolyType(self):
        """
        ConvertToPolyType -> void
            
            Autodesk.AutoCAD.DatabaseServices.Poly2dType newVal: 
            Input type to which the polyline should be converted
        """
        pass
    
    
    def CurveFit(self):
        """
        CurveFit -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def InsertVertexAt(self):
        """
        InsertVertexAt(ObjectId, Vertex2d) -> ObjectId
            
            Vertex2d newVertex: 
            Input vertex to be inserted
            
            indexVertex: 
            Input vertex in polyline after which the new vertex is to be inserted
        InsertVertexAt(Vertex2d, Vertex2d) -> void
            
            Vertex2d newVertex: 
            Input pointer to vertex to be inserted
            
            vertexId: 
            Input objectId of the vertex in the polyline after which the new vertex is to be inserted
        """
        pass
    
    
    def NonDBAppendVertex(self):
        """
        NonDBAppendVertex -> void
            
            Vertex2d vertexToAppend: 
            Input the vertex to add to the polyline
        """
        pass
    
    
    def SplineFit(self):
        """
        SplineFit() -> void
        
        """
        pass
    
    
    def Straighten(self):
        """
        Straighten -> void
        
        """
        pass
    
    
    def VertexPosition(self):
        """
        VertexPosition -> Point3d
            
            Vertex2d vertex: 
            Input vertex object to get the WCS coordinate for
        """
        pass
    
    
    Closed = None
    
    
    ConstantWidth = None
    
    
    DefaultEndWidth = None
    
    
    DefaultStartWidth = None
    
    
    Elevation = None
    
    
    Length = None
    
    
    LinetypeGenerationOn = None
    
    
    Normal = None
    
    
    PolyType = None
    
    
    Thickness = None
    
    pass

class Polyline3d(object):
    """
    
    Polyline3d()()
    
    
    """
    def AppendVertex(self):
        """
        AppendVertex -> ObjectId
            
            PolylineVertex3d vertexToAppend: 
            Input pointer to the vertex to add to the polyline
        """
        pass
    
    
    def ConvertToPolyType(self):
        """
        ConvertToPolyType -> void
            
            Autodesk.AutoCAD.DatabaseServices.Poly3dType newVal: 
            Input type to which the polyline should be converted
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def InsertVertexAt(self):
        """
        InsertVertexAt(ObjectId, PolylineVertex3d) -> ObjectId
            
            ObjectId indexVertexId: 
            Input vertex in polyline after which the new vertex is to be inserted
            
            PolylineVertex3d newVertex: 
            Input vertex to be inserted
        InsertVertexAt(PolylineVertex3d, PolylineVertex3d) -> void
            
            PolylineVertex3d indexVertex: 
            Input objectId of the vertex in the polyline after which the new vertex is to be inserted
            
            PolylineVertex3d newVertex: 
            Input vertex to be inserted
        """
        pass
    
    
    def SplineFit(self):
        """
        SplineFit() -> void
        
        """
        pass
    
    
    def Straighten(self):
        """
        Straighten -> void
        
        """
        pass
    
    
    Closed = None
    
    
    Length = None
    
    
    PolyType = None
    
    pass

class PolylineVertex3d(object):
    """
    
    PolylineVertex3d()()
    
    
    PolylineVertex3d(Point3d)
        Point3d param0 : Input WCS position point for the vertex
    
    
    """
    Position = None
    
    
    VertexType = None
    
    pass

class Profile3d(object):
    """
    
    Profile3d()()
    
    
    Profile3d(Autodesk.AutoCAD.DatabaseServices.Entity)()
    
    
    Profile3d(FullSubentityPath)()
    
    
    Profile3d(PathRef)()
    
    
    Profile3d(Profile3d)()
    
    
    Profile3d(VertexRef)()
    
    
    """
    def ConvertProfile(self):
        """
        ConvertProfile(PathRef[]) -> Profile3d
        
        ConvertProfile([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Profile3d()
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def MergeProfiles(self):
        """
        MergeProfiles -> Profile3d()
        
        """
        pass
    
    
    Entity = None
    
    
    IsClosed = None
    
    
    IsEdge = None
    
    
    IsFace = None
    
    
    IsPlanar = None
    
    
    IsSubent = None
    
    
    IsValid = None
    
    
    ProfilePathRef = None
    
    
    ProfileVertexRef = None
    
    pass

class PropertiesOverrule(object):
    """
    
    """
    def GetClassID(self):
        """
        GetClassID -> Guid
        
        """
        pass
    
    
    def List(self):
        """
        List -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    pass

class ProxyEntity(object):
    """
    
    """
    def GetReferences(self):
        """
        GetReferences -> DBObjectReferenceCollection
        
        """
        pass
    
    
    ApplicationDescription = None
    
    
    GraphicsMetafileType = None
    
    
    OriginalClassName = None
    
    
    OriginalDxfName = None
    
    
    ProxyFlags = None
    
    pass

class ProxyObject(object):
    """
    
    """
    def GetReferences(self):
        """
        GetReferences -> DBObjectReferenceCollection
        
        """
        pass
    
    
    def ResurrectMeNow(self):
        """
        ResurrectMeNow -> void
            
            ObjectId id: 
            Input object ID of object to be resurrected
        """
        pass
    
    
    ApplicationDescription = None
    
    
    OriginalClassName = None
    
    
    OriginalDxfName = None
    
    
    ProxyFlags = None
    
    pass

class ProxyResurrectionCompletedEventArgs(object):
    """
    
    """
    ApplicationName = None
    
    
    Ids = None
    
    pass

class RadialDimension(object):
    """
    
    RadialDimension()()
    
    
    """
    Center = None
    
    
    ChordPoint = None
    
    
    LeaderLength = None
    
    pass

class RadialDimensionLarge(object):
    """
    
    RadialDimensionLarge()()
    
    
    """
    Center = None
    
    
    ChordPoint = None
    
    
    JogAngle = None
    
    
    JogPoint = None
    
    
    OverrideCenter = None
    
    pass

class RadiusDiameterConstraint(object):
    """
    
    RadiusDiameterConstraint()()
    
    
    RadiusDiameterConstraint(RadDiaConstrType)
        RadDiaConstrType type : Input RadDiaConstrType indicating the constraint type.
    
    
    """
    class RadDiaConstrType():
        CircleRadius = None
        CircleDiameter = None
        MinorRadius = None
        MajorRadius = None
    
    
    ConstrType = None
    
    pass

class RapidRTRenderSettings(object):
    """
    
    RapidRTRenderSettings()
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    FilterHeight = None
    
    
    FilterType = None
    
    
    FilterWidth = None
    
    
    LightingModel = None
    
    
    RenderLevel = None
    
    
    RenderTarget = None
    
    
    RenderTime = None
    
    pass

class RapidRTRenderTarget():
    Level = None
    Time = None
    Infinite = None

class RasterImage(object):
    """
    
    RasterImage()
    """
    def AssociateRasterDef(self):
        """
        AssociateRasterDef -> void
            
            RasterImageDef definition: 
            Input raster image def
        """
        pass
    
    
    def EnableReactors(self):
        """
        EnableReactors -> void
            
            [MarshalAs(UnmanagedType.U1)] bool enable: 
            Input boolean switch
        """
        pass
    
    
    def GetClipBoundary(self):
        """
        GetClipBoundary -> Point2dCollection
        
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices -> Point3dCollection
        
        """
        pass
    
    
    def ImageSize(self):
        """
        ImageSize -> Vector2d
            
            [MarshalAs(UnmanagedType.U1)] bool getCachedValue: 
            Input Boolean indicating whether the cached should be used
        """
        pass
    
    
    def SetClipBoundary(self):
        """
        SetClipBoundary(Autodesk.AutoCAD.DatabaseServices.ClipBoundaryType, Point2dCollection) -> void
            
            Autodesk.AutoCAD.DatabaseServices.ClipBoundaryType type: 
            Input clip boundary type
            
            Point2dCollection clipBoundaryVertices: 
            Input collection of clip boundary vertices
        SetClipBoundary(Vector2d) -> void
            
            Vector2d size: 
            Input vector of boundary
        """
        pass
    
    
    def SetClipBoundaryToWholeImage(self):
        """
        SetClipBoundaryToWholeImage -> void
        
        """
        pass
    
    
    Brightness = None
    
    
    ClipBoundaryType = None
    
    
    Contrast = None
    
    
    DisplayOptions = None
    
    
    Fade = None
    
    
    Height = None
    
    
    ImageDefId = None
    
    
    ImageHeight = None
    
    
    ImageTransparency = None
    
    
    ImageWidth = None
    
    
    IsClipped = None
    
    
    Name = None
    
    
    Orientation = None
    
    
    Path = None
    
    
    PixelToModelTransform = None
    
    
    Position = None
    
    
    ReactorId = None
    
    
    Rotation = None
    
    
    Scale = None
    
    
    ShowImage = None
    
    
    Width = None
    
    pass

class RasterImageDef(object):
    """
    
    RasterImageDef()
    """
    def CloseImage(self):
        """
        CloseImage -> void
        
        """
        pass
    
    
    def CreateImageDictionary(self):
        """
        CreateImageDictionary -> ObjectId
            
            Database database: 
            Input AutoCAD database in which to create the dictionary
        """
        pass
    
    
    def Embed(self):
        """
        Embed -> void
        
        """
        pass
    
    
    def GetEntityCount(self):
        """
        GetEntityCount -> Integer
            
            out bool locked: 
            Input locked value
        """
        pass
    
    
    def GetImageDictionary(self):
        """
        GetImageDictionary -> ObjectId
            
            Database database: 
            Input AutoCAD database in which to find the dictionary
        """
        pass
    
    
    def ImageCopy(self):
        """
        ImageCopy -> IntPtr
            
            [MarshalAs(UnmanagedType.U1)] bool forceImageLoad: 
            Input Boolean indicating whether to load the image if it is not currently loaded
        """
        pass
    
    
    def Load(self):
        """
        Load -> void
        
        """
        pass
    
    
    def LocateActivePath(self):
        """
        LocateActivePath -> string
        
        """
        pass
    
    
    def OpenImage(self):
        """
        OpenImage -> IntPtr
        
        """
        pass
    
    
    def SetImage(self):
        """
        SetImage -> void
            
            IntPtr image: 
            Input NULL or pointer to valid Atil::Image object
            
            IntPtr fileDescription: 
            Input NULL or pointer to valid Atil::FileReadDescriptor object
            
            [MarshalAs(UnmanagedType.U1)] bool modifyDatabase: 
            Input Boolean indicating whether to do undo recording
        """
        pass
    
    
    def SuggestName(self):
        """
        SuggestName -> string
            
            DBDictionary imageDictionary: 
            Input pointer to the (previously opened for reading) image dictionary within which this name must be unique
            
            string newImagePathName: 
            Input pointer to a string containing the source image file or path name
        """
        pass
    
    
    def Unload(self):
        """
        Unload -> void
            
            [MarshalAs(UnmanagedType.U1)] bool modifyDatabase: 
            Input Boolean indicating whether or not to do undo recording
        """
        pass
    
    
    def UpdateEntities(self):
        """
        UpdateEntities -> void
        
        """
        pass
    
    
    ActiveFileName = None
    
    
    ColorDepth = None
    
    
    FileDescCopy = None
    
    
    FileType = None
    
    
    ImageModified = None
    
    
    IsEmbedded = None
    
    
    IsLoaded = None
    
    
    Organization = None
    
    
    ResolutionMMPerPixel = None
    
    
    ResolutionUnits = None
    
    
    SearchForActivePath = None
    
    
    Size = None
    
    
    SourceFileName = None
    
    
    UndoStoreSize = None
    
    pass

class RasterVariables(object):
    """
    
    RasterVariables()
    """
    ImageFrame = None
    
    
    ImageQuality = None
    
    
    UserScale = None
    
    pass

class Ray(object):
    """
    
    Ray()
    """
    BasePoint = None
    
    
    SecondPoint = None
    
    
    UnitDir = None
    
    pass

class Rectangle3d(object):
    """
    
    Rectangle3d
        Point3d upperLeft : Input upper left point
        Point3d upperRight : Input upper right point
        Point3d lowerLeft : Input lower left point
        Point3d lowerRight : Input lower right point
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture-specific format.
        """
        pass
    
    
    LowerLeft = None
    
    
    LowerRight = None
    
    
    UpperLeft = None
    
    
    UpperRight = None
    
    pass

class RegAppTable(object):
    """
    
    """

    pass

class RegAppTableRecord(object):
    """
    
    RegAppTableRecord()
    """

    pass

class Region(object):
    """
    
    Region()
    """
    def AreaProperties(self):
        """
        AreaProperties -> RegionAreaProperties
            
            ref Point3d origin: 
            Input point (in WCS coords) for origin of the coordinate system to usefor evaluation.
            
            ref Vector3d xAxis: 
            Input X axis (in WCS coords) of the coordinate system to use forevaluation.
            
            ref Vector3d yAxis: 
            Input Y axis (in WCS coords) of the coordinate system to use forevaluation.
        """
        pass
    
    
    def BooleanOperation(self):
        """
        BooleanOperation -> void
            
            BooleanOperationType operation: 
            Input type of Boolean operation.
            
            Region otherRegion: 
            Input pointer to another region to perform the Boolean operation
        """
        pass
    
    
    def CreateFromCurves(self):
        """
        CreateFromCurves -> DBObjectCollection
            
            DBObjectCollection curveSegments: 
            Input collection to curve entities used to define the region's perimeter(s)
        """
        pass
    
    
    Area = None
    
    
    IsNull = None
    
    
    Normal = None
    
    
    NumChanges = None
    
    
    Perimeter = None
    
    
    UsesGraphicsCache = None
    
    pass

class RegionAreaProperties(object):
    """
    
    """
    Area = None
    
    
    Centroid = None
    
    
    Extents = None
    
    
    MomentsOfInertia = None
    
    
    Perimeter = None
    
    
    PrincipalMoments = None
    
    
    ProductOfInertia = None
    
    
    RadiiOfGyration = None
    
    pass

class RenderEnvironment(object):
    """
    
    RenderEnvironment()
    """
    class DoubleRangeParameter(object):
        """
        
        DoubleRangeParameter
            double n : Near distance
            double f : Far distance
        """
        Far = None
        
        
        Near = None
        
        pass
    
    
    Distances = None
    
    
    EnvironmentImageEnabled = None
    
    
    EnvironmentImageFileName = None
    
    
    FogBackgroundEnabled = None
    
    
    FogColor = None
    
    
    FogDensity = None
    
    
    FogEnabled = None
    
    pass

class RenderGlobal(object):
    """
    
    RenderGlobal()
    """
    class DimensionsParameter(object):
        """
        
        DimensionsParameter
            int w : Width parameter
            int h : Height parameter
        """
        Height = None
        
        
        Width = None
        
        pass
    
    
    class ProcedureAndDestinationParameter(object):
        """
        
        ProcedureAndDestinationParameter
            Autodesk.AutoCAD.DatabaseServices.RenderGlobal.Procedure p : Input a procedure
            Autodesk.AutoCAD.DatabaseServices.RenderGlobal.Destination d : Input a destination
        """
        Destination = None
        
        
        Procedure = None
        
        pass
    
    
    class Destination():
        Window = None
        Viewport = None
    
    
    class Procedure():
        View = None
        Crop = None
        Selected = None
    
    
    Dimensions = None
    
    
    HighInfoLevel = None
    
    
    PredefinedPresetsFirst = None
    
    
    ProcedureAndDestination = None
    
    
    SaveEnabled = None
    
    
    SaveFileName = None
    
    pass

class RenderSettings(object):
    """
    
    RenderSettings()
    """
    BackFacesEnabled = None
    
    
    Description = None
    
    
    DiagnosticBackgroundEnabled = None
    
    
    DisplayIndex = None
    
    
    IsPredefined = None
    
    
    MaterialsEnabled = None
    
    
    Name = None
    
    
    PreviewImageFileName = None
    
    
    ShadowsEnabled = None
    
    
    TextureSampling = None
    
    pass

class ResultBuffer(object):
    """
    
    ResultBuffer()()
    
    
    ResultBuffer(params TypedValue[])
        params TypedValue[] values : Input values
    
    
    """
    def Add(self):
        """
        Add(TypedValue) -> void
            
            TypedValue value: 
            Input object to add
        Add(object) -> void
            
            object value: 
            Input object to add
        """
        pass
    
    
    def AsArray(self):
        """
        AsArray -> TypedValue()
        
        """
        pass
    
    
    def Create(self):
        """
        Create -> ResultBuffer
            
            IntPtr buffer: 
            Input pointer
            
            [MarshalAs(UnmanagedType.U1)] bool autoDelete: 
            Set to true if the pointer should be deleted after creation
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Object to check against
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> ResultBufferEnumerator
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture definition
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format for string
            
            IFormatProvider provider: 
            Input culture definition
        """
        pass
    
    pass

class ResultBufferEnumerator(object):
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

class RevolveOptions(object):
    """
    
    RevolveOptions()()
    
    
    RevolveOptions(RevolveOptions)
        RevolveOptions opts : Input object to be copied.
    
    
    """
    def CheckRevolveCurve(self):
        """
        CheckRevolveCurve -> RevolveOptionsCheckRevolveCurveOut
            
            Point3d axisPnt: 
            Input point on axis of revolution
            
            Vector3d axisDir: 
            Input direction of axis of revolution
            
            [MarshalAs(UnmanagedType.U1)] bool displayErrorMessages: 
            Input Boolean value indicating whether to display error messages
            
            unnamed: 
            Input the curve or region to be revolved
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    CloseToAxis = None
    
    
    DraftAngle = None
    
    
    TwistAngle = None
    
    pass

class RevolveOptionsBuilder(object):
    """
    
    RevolveOptionsBuilder()()
    
    
    RevolveOptionsBuilder(RevolveOptions)
        RevolveOptions value : Input constructor to copy.
    
    
    """
    def ToRevolveOptions(self):
        """
        ToRevolveOptions -> RevolveOptions
        
        """
        pass
    
    
    CloseToAxis = None
    
    
    DraftAngle = None
    
    
    TwistAngle = None
    
    pass

class RevolveOptionsCheckRevolveCurveOut(object):
    """
    
    RevolveOptionsCheckRevolveCurveOut()
    """
    Closed = None
    
    
    EndPointsOnAxis = None
    
    
    Planar = None
    
    pass

class RevolvedSurface(object):
    """
    
    RevolvedSurface()
    """
    def CreateRevolvedSurface(self):
        """
        CreateRevolvedSurface -> void
            
            Entity revolveEntity: 
            Input the planar curve, region, or planar surface that is to be revolved
            
            Point3d axisPoint: 
            Input point on the axis of revolution
            
            Vector3d axisDirection: 
            Input direction on the axis of revolution
            
            double revolveAngle: 
            Input angle of rotation in radians
            
            double startAngle: 
            Input start angle of rotation, in radians. If 0, then rotation will start from current position of revolveEntity
            
            Autodesk.AutoCAD.DatabaseServices.RevolveOptions revolveOptions: 
            Input revolve options
        """
        pass
    
    
    def SetRevolve(self):
        """
        SetRevolve -> void
            
            Point3d axisPoint: 
            Input axis point
            
            Vector3d axisDirection: 
            Input axis vector
            
            double revolveAngle: 
            Input angle of revolution, in radians
            
            Autodesk.AutoCAD.DatabaseServices.RevolveOptions revolveOptions: 
            Input revolve options
        """
        pass
    
    
    AxisDirection = None
    
    
    AxisPoint = None
    
    
    RevolveAngle = None
    
    
    RevolveEntity = None
    
    
    RevolveOptions = None
    
    
    RevolveProfile = None
    
    
    StartAngle = None
    
    pass

class RigidSetTypeInfo():
    NotRigidSet = None
    ScalableRigidSet = None
    NonScalableRigidSet = None

class RotatedDimension(object):
    """
    
    RotatedDimension()()
    
    
    """
    DimLinePoint = None
    
    
    Oblique = None
    
    
    Rotation = None
    
    
    XLine1Point = None
    
    
    XLine2Point = None
    
    pass

class RotationAngle():
    Degrees000 = 0
    Degrees090 = 1
    Degrees180 = 2
    Degrees270 = 3
    DegreesUnknown = -1

class RowType():
    DataRow = 1
    HeaderRow = 4
    TitleRow = 2
    UnknownRow = 0

class SaveType():
    NoSave = None
    Save12 = None
    Save13 = None
    Save14 = None
    Save2000 = None
    Save2004 = None
    Save2007 = None
    Save2010 = None
    Save2013 = None
    Save2018 = None

class Section(object):
    """
    
    Section()()
    
    
    Section(Point3dCollection, Vector3d)
        Point3dCollection pts : Input vertex points on the section line; should contain at least two points
        Vector3d verticalDir : Input vector on the first segment's plane, normal to the section line
    
    
    Section(Point3dCollection, Vector3d, Vector3d)
        Point3dCollection pts : Input vertex points on the section line; should contain at least two points
        Vector3d verticalDir : Input vector on the first segment's plane, normal to the section line
        Vector3d vecViewingDir : Input vector specifying the viewing direction
    
    
    """
    def AddVertex(self):
        """
        AddVertex -> void
            
            int nInsertAt: 
            Input index at which to add the new vertex
            
            Point3d pt: 
            Input position of the new vertex
        """
        pass
    
    
    def CreateJog(self):
        """
        CreateJog -> void
            
            Point3d ptOnSection: 
            Input point on the section line at which to create the jog
        """
        pass
    
    
    def GenerateSectionGeometry(self):
        """
        GenerateSectionGeometry -> void
            
            Entity pEnt: 
            Input sectionable entity
            
            out Array pIntFillEnts: 
            Return array containing intersection boundary geometry
            
            out Array pBackgroundEnts: 
            Return array containing intersection fill annotation geometry
            
            out Array pForegroundEnts: 
            Return array containing background geometry
            
            out Array pFurveTangencyEnts: 
            Return array containing foreground geometry
            
            out Array pCurveTangencyEnts: 
            Return array containing curve tangency geometry
        """
        pass
    
    
    def GetVertex(self):
        """
        GetVertex -> Point3d
            
            int nIndex: 
            Input zero-based index of the vertex to be retrieved; should be less than the number of vertices
        """
        pass
    
    
    def GetVertices(self):
        """
        GetVertices -> void
            
            Point3dCollection pts: 
            Output reference to receive vertices
        """
        pass
    
    
    def Height(self):
        """
        Height -> double
            
            SectionHeight nHeightType: 
            Input one of the SectionHeight enum values
        """
        pass
    
    
    def HitTest(self):
        """
        HitTest -> SectionHitTestInfo
            
            Point3d ptHit: 
            Input point to perform hit test
        """
        pass
    
    
    def RemoveVertex(self):
        """
        RemoveVertex -> void
            
            int nIndex: 
            Input index of the vertex to remove
            
            nHeightType: 
            Input one of the Height enum values
            
            fHeight: 
            Input height
        """
        pass
    
    
    def SetHeight(self):
        """
        SetHeight -> void
            
            SectionHeight nHeightType: 
            Input one of the Height enum val
            
            double fHeight: 
            Input height Sets the height of the section plane above or below the section line. The height is the indicator height when the section plane type is plane or boundary, since the cuts extends infinitely in the vertical direction for these two types.
        """
        pass
    
    
    def SetVertex(self):
        """
        SetVertex -> void
            
            int nIndex: 
            Input zero-based index of the vertex to set; should be less than the number of vertices
            
            Point3d pt: 
            Input new position of the vertex
        """
        pass
    
    
    BottomPlane = None
    
    
    Boundary = None
    
    
    Elevation = None
    
    
    HasJogs = None
    
    
    IndicatorFillColor = None
    
    
    IndicatorTransparency = None
    
    
    IsLiveSectionEnabled = None
    
    
    IsSlice = None
    
    
    Name = None
    
    
    Normal = None
    
    
    NumVertices = None
    
    
    SectionPlaneOffset = None
    
    
    Settings = None
    
    
    State = None
    
    
    ThicknessDepth = None
    
    
    TopPlane = None
    
    
    VerticalDirection = None
    
    
    Vertices = None
    
    
    ViewingDirection = None
    
    pass

class SectionGeneration():
    DestinationFile = 0x40
    DestinationNewBlock = 0x10
    DestinationReplaceBlock = 0x20
    SourceAllObjects = 1
    SourceSelectedObjects = 2

class SectionGeometry():
    BackgroundGeometry = 4
    CurveTangencyLines = 0x10
    ForegroundGeometry = 8
    IntersectionBoundary = 1
    IntersectionFill = 2

class SectionHeight():
    HeightAboveSectionLine = 1
    HeightBelowSectionLine = 2

class SectionHitTestInfo(object):
    """
    
    SectionHitTestInfo()
    """
    Index = None
    
    
    PtOnSegment = None
    
    
    SubItem = None
    
    pass

class SectionManager(object):
    """
    
    SectionManager()
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def GetSection(self):
        """
        GetSection -> ObjectId
            
            string pszName: 
            Input name of the section plane to get
        """
        pass
    
    
    def GetUniqueSectionName(self):
        """
        GetUniqueSectionName -> string
            
            string pszBaseName: 
            Input System.String object.
        """
        pass
    
    
    LiveSection = None
    
    
    NumSections = None
    
    pass

class SectionSettings(object):
    """
    
    SectionSettings()
    """
    def Reset(self):
        """
        Reset() -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type to be reset
        """
        pass
    
    
    def Color(self):
        """
        Color -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def DestinationBlock(self):
        """
        DestinationBlock -> ObjectId
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination block is to be returned
        """
        pass
    
    
    def DestinationFile(self):
        """
        DestinationFile -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination file is to be returned
        """
        pass
    
    
    def DivisionLines(self):
        """
        DivisionLines -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def EdgeTransparency(self):
        """
        EdgeTransparency -> Integer
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def FaceTransparency(self):
        """
        FaceTransparency -> Integer
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def GenerationOptions(self):
        """
        GenerationOptions -> SectionGeneration
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the generation options object is to be returned
        """
        pass
    
    
    def GetHatchPatternName(self):
        """
        GetHatchPatternName -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def GetHatchPatternType(self):
        """
        GetHatchPatternType -> Autodesk.AutoCAD.DatabaseServices.HatchPatternType
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def GetSourceObjects(self):
        """
        GetSourceObjects -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the source objects are to be returned
            
            ObjectIdCollection ids: 
            Output collection of the object IDs
        """
        pass
    
    
    def HatchAngle(self):
        """
        HatchAngle -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HatchScale(self):
        """
        HatchScale -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HatchSpacing(self):
        """
        HatchSpacing -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HatchVisibility(self):
        """
        HatchVisibility -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def HiddenLine(self):
        """
        HiddenLine -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def Layer(self):
        """
        Layer -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def Linetype(self):
        """
        Linetype -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def LinetypeScale(self):
        """
        LinetypeScale -> double
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input section type
        """
        pass
    
    
    def LineWeight(self):
        """
        LineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def PlotStyleName(self):
        """
        PlotStyleName -> string
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color to set
        """
        pass
    
    
    def SetDestinationBlock(self):
        """
        SetDestinationBlock -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination block is to be set
            
            ObjectId id: 
            Input ID of the block to be replaced during section generation
        """
        pass
    
    
    def SetDestinationFile(self):
        """
        SetDestinationFile -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the destination file is to be set
            
            string pszFileName: 
            Input destination file name
        """
        pass
    
    
    def SetDivisionLines(self):
        """
        SetDivisionLines -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bShow: 
            Input true if division lines are to be shown, or false if they are to be hidden
        """
        pass
    
    
    def SetEdgeTransparency(self):
        """
        SetEdgeTransparency -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            int nTransparency: 
            Input edge transparency to set, in the range 0-100
        """
        pass
    
    
    def SetFaceTransparency(self):
        """
        SetFaceTransparency -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            int nTransparency: 
            Input edge transparency to set, in the range 0-100
        """
        pass
    
    
    def SetGenerationOptions(self):
        """
        SetGenerationOptions -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type for which the generation options are to be set
            
            SectionGeneration nOptions: 
            Input options flag to set
        """
        pass
    
    
    def SetHatchPatternType(self):
        """
        SetHatchPatternType -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            Autodesk.AutoCAD.DatabaseServices.HatchPatternType nPatternType: 
            Input pattern type
        """
        pass
    
    
    def SetHatchAngle(self):
        """
        SetHatchAngle -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            double fAngle: 
            Input hatch angle
        """
        pass
    
    
    def SetHatchPatternName(self):
        """
        SetHatchPatternName -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string sNewName: 
            Input hatch pattern name
        """
        pass
    
    
    def SetHatchScale(self):
        """
        SetHatchScale -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def SetHatchSpacing(self):
        """
        SetHatchSpacing -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    def SetHatchVisibility(self):
        """
        SetHatchVisibility -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bVisible: 
            Input visibility value
        """
        pass
    
    
    def SetHiddenLine(self):
        """
        SetHiddenLine -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bHiddenLine: 
            Input visibility value
        """
        pass
    
    
    def SetLayer(self):
        """
        SetLayer -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string pszLayer: 
            Input layer to set
        """
        pass
    
    
    def SetLinetype(self):
        """
        SetLinetype -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string pszLinetype: 
            Input new linetype
        """
        pass
    
    
    def SetLinetypeScale(self):
        """
        SetLinetypeScale -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            double fScale: 
            Input new linetype scale
        """
        pass
    
    
    def SetLineWeight(self):
        """
        SetLineWeight -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight nLineWeight: 
            Input line weight
        """
        pass
    
    
    def SetPlotStyleName(self):
        """
        SetPlotStyleName -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            string pszPlotStyleName: 
            Input plot style name
        """
        pass
    
    
    def SetSourceObjects(self):
        """
        SetSourceObjects -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            ObjectIdCollection ids: 
            Input source object IDs
        """
        pass
    
    
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
            
            [MarshalAs(UnmanagedType.U1)] bool bVisible: 
            Input visibility value
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> bool
            
            Autodesk.AutoCAD.DatabaseServices.SectionType nSecType: 
            Input section type
            
            SectionGeometry nGeometry: 
            Input geometry value
        """
        pass
    
    
    CurrentSectionType = None
    
    pass

class SectionState():
    Boundary = 2
    Plane = 1
    Volume = 4

class SectionSubItem():
    BackLine = 8
    BackLineBottom = 0x20
    BackLineTop = 0x10
    SectionLine = 1
    SectionLineBottom = 4
    SectionLineTop = 2
    SectionSubItemNone = 0
    VerticalLineBottom = 0x80
    VerticalLineTop = 0x40

class SectionSymbol(object):
    """
    
    SectionSymbol()
    """
    def AddSectionPoint(self):
        """
        AddSectionPoint -> void
        
        """
        pass
    
    
    def GetBulgeAt(self):
        """
        GetBulgeAt -> double
            
            int index: 
            Input: zero-based index into the section symbol point bulge collection.
        """
        pass
    
    
    def GetLabelNameAt(self):
        """
        GetLabelNameAt -> string
            
            int index: 
            Input: zero-based index into the section symbol point collection.
        """
        pass
    
    
    def GetLabelOffsetAt(self):
        """
        GetLabelOffsetAt -> Vector3d
            
            int index: 
            Input: zero-based index into the section symbol point collection.
        """
        pass
    
    
    def GetLabelOffsets(self):
        """
        GetLabelOffsets -> Vector3dCollection
        
        """
        pass
    
    
    def GetSectionPointAt(self):
        """
        GetSectionPointAt -> Point3d
            
            int index: 
            Input: zero-based index into the section symbol point collection.
        """
        pass
    
    
    def GetSectionPoints(self):
        """
        GetSectionPoints -> Point3dCollection
        
        """
        pass
    
    
    def RemoveSectionPointAt(self):
        """
        RemoveSectionPointAt -> void
        
        """
        pass
    
    
    def SetLabelNameAt(self):
        """
        SetLabelNameAt -> void
        
        """
        pass
    
    
    def SetLabelOffsetAt(self):
        """
        SetLabelOffsetAt -> void
        
        """
        pass
    
    
    def SetLabelOffsets(self):
        """
        SetLabelOffsets -> void
        
        """
        pass
    
    
    def SetSectionPointAt(self):
        """
        SetSectionPointAt -> void
        
        """
        pass
    
    
    Identifier = None
    
    
    IsHalfSection = None
    
    
    IsViewDirectionLeft = None
    
    
    Scale = None
    
    
    SectionPointsCount = None
    
    
    SymbolStyleId = None
    
    pass

class SectionType():
    LiveSection = 1
    Section2d = 2
    Section3d = 4

class SectionViewArrowDirection():
    TowardsCuttingPlane = None
    AwayFromCuttingPlane = None

class SectionViewIdentifierPosition():
    EndCuttingPlane = None
    AboveDirectionArrowLine = None
    AboveDirectionArrowSymbol = None
    StartDirectionArrow = None
    EndDirectionArrow = None

class SectionViewStyle(object):
    """
    
    SectionViewStyle()
    """
    def DefaultViewName(self):
        """
        DefaultViewName -> string
            
            int index: 
            The index of the default name.
        """
        pass
    
    
    def GetViewLabelPattern(self):
        """
        GetViewLabelPattern -> string
            
            Field field: 
            Input: a field object to be updated with the view label pattern master field.
        """
        pass
    
    
    def PostViewStyleToDb(self):
        """
        PostViewStyleToDb -> ObjectId
            
            Database dataBasePointer: 
            Input: database to be updated
            
            string styleName: 
            Input: name to be used for this view style.
        """
        pass
    
    
    def SetDatabaseDefaults(self):
        """
        SetDatabaseDefaults -> void
            
            Database dataBasePointer: 
            Input: database to be used
        """
        pass
    
    
    def SetViewLabelPattern(self):
        """
        SetViewLabelPattern -> void
            
            string pattern: 
            Input: the pattern string for the view label.
            
            Field field: 
            Input: optional pointer to a Field object to provide the field data to be used in the view label pattern.
        """
        pass
    
    
    def ValidateIdentifierExcludeCharacters(self):
        """
        ValidateIdentifierExcludeCharacters -> bool
            
            string characters: 
            Input: the characters to validate.
        """
        pass
    
    
    def ValidateViewName(self):
        """
        ValidateViewName -> bool
            
            string name: 
            Input: section name to validate.
        """
        pass
    
    
    ArrowEndSymbolId = None
    
    
    ArrowPosition = None
    
    
    ArrowStartSymbolId = None
    
    
    ArrowSymbolColor = None
    
    
    ArrowSymbolExtensionLength = None
    
    
    ArrowSymbolSize = None
    
    
    BendLineColor = None
    
    
    BendLineLength = None
    
    
    BendLineTypeId = None
    
    
    BendLineWeight = None
    
    
    Description = None
    
    
    EndLineLength = None
    
    
    EndLineOvershoot = None
    
    
    HatchAngles = None
    
    
    HatchBackgroundColor = None
    
    
    HatchColor = None
    
    
    HatchPattern = None
    
    
    HatchScale = None
    
    
    HatchTransparency = None
    
    
    IdentifierColor = None
    
    
    IdentifierExcludeCharacters = None
    
    
    IdentifierHeight = None
    
    
    IdentifierOffset = None
    
    
    IdentifierPosition = None
    
    
    IdentifierStyleId = None
    
    
    IsContinuousLabeling = None
    
    
    IsModifiedForRecompute = None
    
    
    Name = None
    
    
    PlaneLineColor = None
    
    
    PlaneLineTypeId = None
    
    
    PlaneLineWeight = None
    
    
    ShowAllBendIndentifiers = None
    
    
    ShowAllPlaneLines = None
    
    
    ShowArrowheads = None
    
    
    ShowEndAndBendLines = None
    
    
    ShowHatching = None
    
    
    ShowViewLabel = None
    
    
    ViewLabelAlignment = None
    
    
    ViewLabelAttachment = None
    
    
    ViewLabelOffset = None
    
    
    ViewLabelPattern = None
    
    
    ViewLabelTextColor = None
    
    
    ViewLabelTextHeight = None
    
    
    ViewLabelTextStyleId = None
    
    pass

class SecurityActions():
    AddTimeStamp = 0x20
    EncryptData = 1
    EncryptProperties = 2
    SignData = 0x10

class SecurityAlgorithm():
    RC4 = 0x6801

class SecurityParameters(object):
    """
    
    SecurityParameters()()
    
    
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
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input System.IFormatProvider object.
        """
        pass
    
    
    Action = None
    
    
    Algorithm = None
    
    
    Comment = None
    
    
    Issuer = None
    
    
    Password = None
    
    
    ProviderName = None
    
    
    SerialNumber = None
    
    
    Subject = None
    
    
    TimeServer = None
    
    pass

class SegmentType():
    Line = None
    Arc = None
    Coincident = None
    Point = None
    Empty = None

class SelectType():
    Crossing = 2
    Window = 1

class SequenceEnd(object):
    """
    
    SequenceEnd()
    """

    pass

class ShadePlotResLevel():
    Draft = None
    Preview = None
    Normal = None
    Presentation = None
    Maximum = None
    Custom = None

class ShadePlotType():
    AsDisplayed = None
    Wireframe = None
    Hidden = None
    Rendered = None
    VisualStyle = None
    RenderPreset = None

class Shape(object):
    """
    
    Shape()()
    
    
    Shape(Point3d, double, double, double)
        Point3d position : Input insertion point of the shape, in WCS coordinates
        double size : Input height of the shape
        double rotation : Input rotation of the shape
        double widthFactor : Input width factor of the shape
    
    
    """
    Name = None
    
    
    Normal = None
    
    
    Oblique = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    ShapeIndex = None
    
    
    ShapeNumber = None
    
    
    Size = None
    
    
    StyleId = None
    
    
    Thickness = None
    
    
    WidthFactor = None
    
    pass

class Solid(object):
    """
    
    Solid()()
    
    
    Solid(Point3d, Point3d, Point3d)
        Point3d pointer1 : Input first point (in WCS) for solid
        Point3d pointer2 : Input second point (in WCS) for solid
        Point3d pointer3 : Input third point (in WCS) for solid
    
    
    Solid(Point3d, Point3d, Point3d, Point3d)
        Point3d pointer1 : Input first point (in WCS) for solid
        Point3d pointer2 : Input second point (in WCS) for solid
        Point3d pointer3 : Input third point (in WCS) for solid
        Point3d pointer4 : Input fourth point (in WCS) for solid
    
    
    """
    def GetPointAt(self):
        """
        GetPointAt -> Point3d
            
            short index: 
            Input index (1-4) of the desired point in the solid
        """
        pass
    
    
    def SetPointAt(self):
        """
        SetPointAt -> void
            
            short index: 
            Input index (1-4) of the point to set in the solid
            
            Point3d pointValue: 
            Input point value
        """
        pass
    
    
    Normal = None
    
    
    Thickness = None
    
    pass

class Solid3d(object):
    """
    
    Solid3d()
    """
    def BooleanOperation(self):
        """
        BooleanOperation -> void
            
            BooleanOperationType operation: 
            Input type of Boolean operation
            
            Solid3d solid: 
            Input the other solid with which to carry out the Boolean operation
        """
        pass
    
    
    def ChamferEdges(self):
        """
        ChamferEdges -> void
            
            SubentityId[] subentityIds: 
            Input object ids of edges at which the chamfer will be applied
            
            SubentityId baseSubentityId: 
            Input object id of the base face where the chamfer will be applied
            
            double baseDist: 
            Input chamfer distance on the base face
            
            double otherDist: 
            Input chamfer distance on the other faces
        """
        pass
    
    
    def CheckInterference(self):
        """
        CheckInterference -> bool
            
            Solid3d otherSolid: 
            Input pointer for other solid
        """
        pass
    
    
    def CleanBody(self):
        """
        CleanBody -> void
        
        """
        pass
    
    
    def ConvertToBrepAtSubentPaths(self):
        """
        ConvertToBrepAtSubentPaths -> void
            
            FullSubentityPath[] paths: 
            Input array of references to history items
        """
        pass
    
    
    def CopyEdge(self):
        """
        CopyEdge -> Entity
            
            SubentityId subEntityId: 
            Input subentity ID of an edge in the Solid3d
        """
        pass
    
    
    def CopyFace(self):
        """
        CopyFace -> Entity
            
            SubentityId subEntityId: 
            Input subentity ID of a face in the Solid3d
        """
        pass
    
    
    def CreateBox(self):
        """
        CreateBox -> void
            
            double lengthAlongX: 
            Input value for length of the box
            
            double lengthAlongY: 
            Input value for width of the box
            
            double lengthAlongZ: 
            Input value for height of the box
        """
        pass
    
    
    def CreateFrustum(self):
        """
        CreateFrustum -> void
            
            double height: 
            Input height for the frustum
            
            double radiusAlongX: 
            Input radius for the frustum in X direction
            
            double radiusAlongY: 
            Input radius for the frustum in Y direction
            
            double topRadius: 
            Input radius for top end of the frustum
        """
        pass
    
    
    def CreateExtrudedSolid(self):
        """
        CreateExtrudedSolid(Entity, SubentityId, Vector3d, SweepOptions) -> void
        
        CreateExtrudedSolid(Entity, SubentityId, double, SweepOptions) -> void
        
        CreateExtrudedSolid(Entity, Vector3d, SweepOptions) -> void
        
        """
        pass
    
    
    def CreatePyramid(self):
        """
        CreatePyramid -> void
            
            double height: 
            Input height for pyramid
            
            int sides: 
            Input number of sides for pyramid
            
            double radius: 
            Input radius for inscribed circle of bottom polygon
            
            double topRadius: 
            Input radius for inscribed circle of top polygon
        """
        pass
    
    
    def CreateSphere(self):
        """
        CreateSphere -> void
            
            double radius: 
            Input radius for the sphere
        """
        pass
    
    
    def CreateLoftedSolid(self):
        """
        CreateLoftedSolid(Entity[], Entity[], Entity, LoftOptions) -> void
        
        CreateLoftedSolid(LoftProfile[], LoftProfile[], LoftProfile, LoftOptions) -> void
        
        """
        pass
    
    
    def CreateTorus(self):
        """
        CreateTorus -> void
            
            double majorRadius: 
            Input major radius for the torus
            
            double minorRadius: 
            Input minor radius for the torus
        """
        pass
    
    
    def CreateWedge(self):
        """
        CreateWedge -> void
            
            double lengthAlongX: 
            Input length for the wedge
            
            double lengthAlongY: 
            Input width for the wedge
            
            double lengthAlongZ: 
            Input height for the wedge
        """
        pass
    
    
    def CreateRevolvedSolid(self):
        """
        CreateRevolvedSolid(Entity, Point3d, Vector3d, double, double, RevolveOptions) -> void
        
        CreateRevolvedSolid(Entity, SubentityId, Point3d, Vector3d, double, double, RevolveOptions) -> void
        
        """
        pass
    
    
    def Extrude(self):
        """
        Extrude -> void
            
            Region region: 
            Input a region object
            
            double height: 
            Input height for extrusion
            
            double taperAngle: 
            Input taper angle in radians
        """
        pass
    
    
    def CreateSculptedSolid(self):
        """
        CreateSculptedSolid -> void
        
        """
        pass
    
    
    def ExtrudeAlongPath(self):
        """
        ExtrudeAlongPath -> void
            
            Region region: 
            Input a region object
            
            Curve path: 
            Input a curve object to extrude along
            
            double taperAngle: 
            Input extrusion taper angle in radians
        """
        pass
    
    
    def ExtrudeFaces(self):
        """
        ExtrudeFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be extruded; these faces must be planar
            
            double height: 
            Input extrusion distance to be applied to the specified faces. Use a positive value to extrude in the direction of the face normals, which point outward from the solid. Use a negative value to extrude faces into the solid.
            
            double taper: 
            Input angle of tapering to be applied to the extrusion; the tapering is relative to the axis formed from the center of each face in the direction of the face normal when a positive height is used or in the opposite direction when a negative height is used; this value should be between half pi and half pi
        """
        pass
    
    
    def CreateSweptSolid(self):
        """
        CreateSweptSolid(Entity, Entity, SweepOptions) -> void
        
        CreateSweptSolid(Entity, SubentityId, Entity, SweepOptions) -> void
        
        """
        pass
    
    
    def ExtrudeFacesAlongPath(self):
        """
        ExtrudeFacesAlongPath -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be extruded; these faces must be planar
            
            Curve path: 
            Input a curve object to extrude along
        """
        pass
    
    
    def FilletEdges(self):
        """
        FilletEdges -> void
            
            SubentityId[] subentityIds: 
            Input object ids of the edges where the fillet will be applied
            
            DoubleCollection radius: 
            Input radius at the corresponding edge
            
            DoubleCollection startSetback: 
            Input start setback at the corresponding edge
            
            DoubleCollection endSetback: 
            Input end setback at the corresponding edge
        """
        pass
    
    
    def GetSection(self):
        """
        GetSection -> Region
            
            Plane plane: 
            Input plane to use as the section cutting plane
        """
        pass
    
    
    def GetSubentityColor(self):
        """
        GetSubentityColor -> Autodesk.AutoCAD.Colors.Color
            
            SubentityId subEntityId: 
            Input subentity Id
        """
        pass
    
    
    def GetSubentityMaterial(self):
        """
        GetSubentityMaterial -> ObjectId
            
            SubentityId subEntityId: 
            Input subentity Id
        """
        pass
    
    
    def GetSubentityMaterialMapper(self):
        """
        GetSubentityMaterialMapper -> Mapper
            
            SubentityId subEntityId: 
            Input subenttity Id
        """
        pass
    
    
    def ImprintEntity(self):
        """
        ImprintEntity -> void
            
            Entity entity: 
            Input entity to be imprinted
        """
        pass
    
    
    def OffsetBody(self):
        """
        OffsetBody -> void
            
            double offsetDistance: 
            Input distance to offset each face
        """
        pass
    
    
    def OffsetFaces(self):
        """
        OffsetFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be offset
            
            double offsetDistance: 
            Input distance to offset each face
        """
        pass
    
    
    def RemoveFaces(self):
        """
        RemoveFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be removed
        """
        pass
    
    
    def Revolve(self):
        """
        Revolve -> void
            
            Region region: 
            Input region object to be revolved
            
            Point3d axisPoint: 
            Input point on the line to be projected to create the axis of revolution
            
            Vector3d axisDir: 
            Input vector representing the direction of the line to be projected to create the axis of revolution
            
            double angleOfRevolution: 
            Input angle of revolution in radians
        """
        pass
    
    
    def SeparateBody(self):
        """
        SeparateBody -> Solid3d()
        
        """
        pass
    
    
    def SetSubentityColor(self):
        """
        SetSubentityColor -> void
            
            SubentityId subEntityId: 
            Input ID of subentity face or edge to be colored
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color for the subentity
        """
        pass
    
    
    def SetSubentityMaterial(self):
        """
        SetSubentityMaterial -> void
            
            SubentityId subEntityId: 
            Input subentity Id
            
            ObjectId materialId: 
            Input object Id of the material
        """
        pass
    
    
    def ProjectOnToSolid(self):
        """
        ProjectOnToSolid -> Entity()
        
        """
        pass
    
    
    def SetSubentityMaterialMapper(self):
        """
        SetSubentityMaterialMapper -> void
            
            SubentityId subEntityId: 
            Input subentity ID
            
            Mapper mapper: 
            Input a Mapper object
        """
        pass
    
    
    def ShellBody(self):
        """
        ShellBody -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be removed from the shell
            
            double offsetDistance: 
            Input distance to offset each face
        """
        pass
    
    
    def Slice(self):
        """
        Slice(Plane) -> void
            
            Plane plane: 
            Input plane to be used for slicing the solid
        Slice(Plane, [MarshalAs(UnmanagedType.U1)] bool) -> Solid3d
            
            Plane plane: 
            Input plane to be used for slicing the solid
            
            [MarshalAs(UnmanagedType.U1)] bool negativeHalfToo: 
            Input flag to indicate whether the other side of the solid is to be generated
        Slice(Autodesk.AutoCAD.DatabaseServices.Surface) -> void
            
            Autodesk.AutoCAD.DatabaseServices.Surface surface: 
            Input the surface entity to be used to slice the solid
        Slice(Autodesk.AutoCAD.DatabaseServices.Surface, [MarshalAs(UnmanagedType.U1)] bool) -> Solid3d
            
            Autodesk.AutoCAD.DatabaseServices.Surface surface: 
            Input the surface entity to be used to slice the solid
            
            [MarshalAs(UnmanagedType.U1)] bool negativeHalfToo: 
            Input flag to indicate whether the other side of the solid is to be generated
        """
        pass
    
    
    def StlOut(self):
        """
        StlOut -> void
            
            string fileName: 
            Input file name
            
            [MarshalAs(UnmanagedType.U1)] bool asciiFormat: 
            Input Boolean indicating file format
        """
        pass
    
    
    def TaperFaces(self):
        """
        TaperFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be tapered
            
            Point3d basePoint: 
            Input origin of the draft plane
            
            Vector3d draftVector: 
            Input draft direction vector
            
            double draftAngle: 
            Input draft angle
        """
        pass
    
    
    def TransformFaces(self):
        """
        TransformFaces -> void
            
            SubentityId[] subentityIds: 
            Input array of subentity IDs of faces to be transformed
            
            Matrix3d matrix: 
            Input rotation and/or translation matrix to be applied to the faces
        """
        pass
    
    
    Area = None
    
    
    IsNull = None
    
    
    MassProperties = None
    
    
    NumChanges = None
    
    
    RecordHistory = None
    
    
    ShowHistory = None
    
    
    UsesGraphicsCache = None
    
    pass

class Solid3dMassProperties(object):
    """
    
    Solid3dMassProperties()
    """
    Centroid = None
    
    
    Extents = None
    
    
    MomentsOfIntertia = None
    
    
    PrincipalMoments = None
    
    
    ProductsOfIntertia = None
    
    
    RadiiOfGyration = None
    
    
    Volume = None
    
    pass

class SolidBackground(object):
    """
    
    SolidBackground()
    """
    Color = None
    
    pass

class SourceType():
    SourceNotDefined = None
    InventorSource = None
    FusionSource = None
    ModelSpaceSource = None

class Spline(object):
    """
    
    Spline()()
    
    
    Spline(Point3d, Vector3d, Vector3d, double, double, double)
        Point3d center : Center point (in WCS coordinates) of the elliptical arc
        Vector3d unitNormal : Vector (in WCS coordinates) representing the normal to the elliptical arc
        Vector3d majorAxis : Major axis vector (in WCS coordinates) of the elliptical arc, measured from the ellipse center point to the ellipse start point
        double radiusRatio : Ratio of minor or major axis length
        double startAngle : Angle (in radians) of start point of elliptical arc
        double endAngle : Angle (in radians) of end point of elliptical arc
    
    
    Spline(Point3dCollection, KnotParameterizationEnum, int, double)()
    
    
    Spline(Point3dCollection, Vector3d, Vector3d, KnotParameterizationEnum, int, double)()
    
    
    Spline(Point3dCollection, Vector3d, Vector3d, int, double)
        Point3dCollection point : Array of points (in WCS coordinates) through which to fit the curve
        Vector3d startTangent : Specifies the tangent at the start of the curve
        Vector3d endTangent : Specifies the tangent at the end of the curve
        int order : Order of the spline to be created (in the range 2 to 26)
        double fitTolerance : Tolerance to which the spline should approximate fitPoints
    
    
    Spline(Point3dCollection, [MarshalAs(UnmanagedType.U1)] bool, KnotParameterizationEnum, int, double)
        Point3dCollection fitPoints : Array of points (in WCS coordinates) through which to fit the curve.
        [MarshalAs(UnmanagedType.U1)] bool isPeriodic : Indicate whether or not a periodic spline fitting the array of points is created.
        KnotParameterizationEnum knotParam : Knot parameterization defining the knot values .
        int degree : Degree of the spline to be created (in the range 1 to 11)
        double fitTolerance : Tolerance to which the spline should approximate fitPoints.
    
    
    Spline(Point3dCollection, int, double)
        Point3dCollection point : Array of points (in WCS coordinates) through which to fit the curve
        int order : Order of the spline to be created (in the range 2 to 26)
        double fitTolerance : Tolerance to which the spline should approximate fitPoints
    
    
    Spline(int, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, Point3dCollection, DoubleCollection, DoubleCollection, double, double)
        int degree : Specifies degree of spline
        [MarshalAs(UnmanagedType.U1)] bool rational : True if the spline is rational
        [MarshalAs(UnmanagedType.U1)] bool closed : True if the spline is closed
        [MarshalAs(UnmanagedType.U1)] bool periodic : True if the spline is periodic
        Point3dCollection controlPoints : Specifies collection of control points (in WCS coordinates) of the spline
        DoubleCollection knots : Collection of doubles that specifies the knot values of the spline
        DoubleCollection weights : Collection of doubles that specifies the weights at each control point
        double controlPointTolerance : Specifies control points tolerance of spline
        double knotTolerance : Specifies knot value tolerance of spline
    
    
    """
    def ElevateDegree(self):
        """
        ElevateDegree -> void
            
            int newDegree: 
            Input new spline degree value (in the range (existing degree) to 25)
        """
        pass
    
    
    def GetControlPointAt(self):
        """
        GetControlPointAt -> Point3d
            
            int index: 
            Input index (0 based) of point to get
        """
        pass
    
    
    def GetFitPointAt(self):
        """
        GetFitPointAt -> Point3d
            
            int index: 
            Input index (0 based) value
        """
        pass
    
    
    def InsertControlPointAt(self):
        """
        InsertControlPointAt -> Autodesk.AutoCAD.Runtime.ErrorStatus
        
        """
        pass
    
    
    def InsertFitPointAt(self):
        """
        InsertFitPointAt -> void
            
            int index: 
            Input index (0 based) where new fit point is to be inserted
            
            Point3d point: 
            Input new fit point (in WCS coordinates)
        """
        pass
    
    
    def InsertKnot(self):
        """
        InsertKnot -> void
            
            double value: 
            Input parameter where knot is to be added
        """
        pass
    
    
    def ModifyPositionAndTangent(self):
        """
        ModifyPositionAndTangent -> Autodesk.AutoCAD.Runtime.ErrorStatus
            
            double param: 
            Parameter
            
            Point3d point: 
            Specify the new location of the point on the spline curve
            
            Vector3d deriv: 
            Specify the tangent vector
        """
        pass
    
    
    def PurgeFitData(self):
        """
        PurgeFitData -> void
        
        """
        pass
    
    
    def Rebuild(self):
        """
        Rebuild -> Autodesk.AutoCAD.Runtime.ErrorStatus
        
        """
        pass
    
    
    def RemoveControlPointAt(self):
        """
        RemoveControlPointAt -> Autodesk.AutoCAD.Runtime.ErrorStatus
        
        """
        pass
    
    
    def RemoveFitPointAt(self):
        """
        RemoveFitPointAt -> void
            
            int index: 
            Index (0 based) of fit point to be removed
        """
        pass
    
    
    def SetControlPointAt(self):
        """
        SetControlPointAt -> void
            
            int index: 
            Input index (0 based) of control point to replace
            
            Point3d point: 
            Input new control point (in WCS coordinates)
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> void
            
            int index: 
            Input index (0 based) of fit point to replace
            
            Point3d point: 
            Input new fit point (in WCS coordinates)
        """
        pass
    
    
    def SetWeightAt(self):
        """
        SetWeightAt -> void
            
            int index: 
            Input index (0 based) of control point at which to change the weight
            
            double weight: 
            Input new weight value
        """
        pass
    
    
    def ToPolyline(self):
        """
        ToPolyline() -> Curve
        
        ToPolyline([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Curve
        
        ToPolyline(uint) -> Curve
            
            uint numOfVertices: 
            Target number of vertices. The resulting polyline will have vertices no more than this value.
        ToPolyline(uint, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Curve
        
        """
        pass
    
    
    def ToPolylineWithPrecision(self):
        """
        ToPolylineWithPrecision(int) -> Curve
            
            int precision: 
            Target precision
        ToPolylineWithPrecision(int, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Curve
        
        """
        pass
    
    
    def UpdateFitData(self):
        """
        UpdateFitData -> void
        
        """
        pass
    
    
    def WeightAt(self):
        """
        WeightAt -> double
            
            int index: 
            Input index (0 based) of control point
        """
        pass
    
    
    Degree = None
    
    
    EndFitTangent = None
    
    
    FitData = None
    
    
    FitTolerance = None
    
    
    HasFitData = None
    
    
    IsNull = None
    
    
    IsPlanar = None
    
    
    IsRational = None
    
    
    NumControlPoints = None
    
    
    NumFitPoints = None
    
    
    NurbsData = None
    
    
    StartFitTangent = None
    
    
    Type = None
    
    pass

class SplineType():
    FitPoints = None
    ControlPoints = None

class StandardScaleType():
    CustomScale = 1
    Scale100To1 = 0x12
    Scale10To1 = 0x11
    Scale1ftAnd1ft = 0x22
    Scale1inAnd1ft = 30
    Scale1To1 = 2
    Scale1To10 = 7
    Scale1To100 = 13
    Scale1To128inAnd1ft = 0x13
    Scale1To16 = 8
    Scale1To16inchAnd1ft = 0x16
    Scale1To2 = 3
    Scale1To20 = 9
    Scale1To2inchAnd1ft = 0x1c
    Scale1To30 = 10
    Scale1To32inchAnd1ft = 0x15
    Scale1To4 = 4
    Scale1To40 = 11
    Scale1To4inchAnd1ft = 0x1a
    Scale1To5 = 5
    Scale1To50 = 12
    Scale1To64inchAnd1ft = 20
    Scale1To8 = 6
    Scale1To8inchAnd1ft = 0x18
    Scale2To1 = 14
    Scale3inAnd1ft = 0x20
    Scale3To16inchAnd1ft = 0x19
    Scale3To32inchAnd1ft = 0x17
    Scale3To4inchAnd1ft = 0x1d
    Scale3To8inchAnd1ft = 0x1b
    Scale4To1 = 15
    Scale6inAnd1ft = 0x21
    Scale8To1 = 0x10
    ScaleToFit = 0

class StdScaleType():
    ScaleToFit = None
    StdScale1To128InchIs1ft = None
    StdScale1To64InchIs1ft = None
    StdScale1To32InchIs1ft = None
    StdScale1To16InchIs1ft = None
    StdScale3To32InchIs1ft = None
    StdScale1To8InchIs1ft = None
    StdScale3To16InchIs1ft = None
    StdScale1To4InchIs1ft = None
    StdScale3To8InchIs1ft = None
    StdScale1To2InchIs1ft = None
    StdScale3To4InchIs1ft = None
    StdScale1InchIs1ft = None
    StdScale3InchIs1ft = None
    StdScale6InchIs1ft = None
    StdScale1ftIs1ft = None
    StdScale1To1 = None
    StdScale1To2 = None
    StdScale1To4 = None
    StdScale1To5 = None
    StdScale1To8 = None
    StdScale1To10 = None
    StdScale1To16 = None
    StdScale1To20 = None
    StdScale1To30 = None
    StdScale1To40 = None
    StdScale1To50 = None
    StdScale1To100 = None
    StdScale2To1 = None
    StdScale4To1 = None
    StdScale8To1 = None
    StdScale10To1 = None
    StdScale100To1 = None
    StdScale1000To1 = None

class SubDMesh(object):
    """
    
    """
    def Cap(self):
        """
        Cap -> void
        
        """
        pass
    
    
    def Collapse(self):
        """
        Collapse -> void
        
        """
        pass
    
    
    def ComputeSurfaceArea(self):
        """
        ComputeSurfaceArea -> double
        
        """
        pass
    
    
    def ComputeVolume(self):
        """
        ComputeVolume -> double
        
        """
        pass
    
    
    def ConvertToSolid(self):
        """
        ConvertToSolid -> Solid3d
        
        """
        pass
    
    
    def ConvertToSurface(self):
        """
        ConvertToSurface([MarshalAs(UnmanagedType.U1)] bool, SubentityId) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        ConvertToSurface([MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        """
        pass
    
    
    def ExtrudeConnectedFaces(self):
        """
        ExtrudeConnectedFaces(FullSubentityPath[], Point3dCollection, double) -> void
        
        ExtrudeConnectedFaces(FullSubentityPath[], double, Vector3d, double) -> void
        
        """
        pass
    
    
    def ExtrudeFaces(self):
        """
        ExtrudeFaces(FullSubentityPath[], Point3dCollection, double) -> void
        
        ExtrudeFaces(FullSubentityPath[], double, Vector3d, double) -> void
        
        """
        pass
    
    
    def GetAdjacentSubentPath(self):
        """
        GetAdjacentSubentPath -> FullSubentityPath()
        
        """
        pass
    
    
    def GetCrease(self):
        """
        GetCrease(FullSubentityPath[]) -> DoubleCollection
        
        GetCrease(SubentityId) -> double
        
        """
        pass
    
    
    def GetFacePlane(self):
        """
        GetFacePlane -> Plane
        
        """
        pass
    
    
    def GetNumberOfSubDividedFacesAt(self):
        """
        GetNumberOfSubDividedFacesAt -> Integer
        
        """
        pass
    
    
    def GetObjectMesh(self):
        """
        GetObjectMesh -> MeshDataCollection
            
            DBObject dbObj: 
            Input object to get the mesh.
            
            MeshFaceterData faceterData: 
            Input faceter setting information.
        """
        pass
    
    
    def GetSubDividedVertexAt(self):
        """
        GetSubDividedVertexAt(SubentityId) -> Point3d
        
        GetSubDividedVertexAt(int) -> Point3d
        
        """
        pass
    
    
    def GetSubentColor(self):
        """
        GetSubentColor -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def GetSubentMaterial(self):
        """
        GetSubentMaterial -> ObjectId
        
        """
        pass
    
    
    def GetSubentMaterialMapper(self):
        """
        GetSubentMaterialMapper -> Mapper
        
        """
        pass
    
    
    def GetSubentPath(self):
        """
        GetSubentPath -> FullSubentityPath()
        
        """
        pass
    
    
    def GetVertexAt(self):
        """
        GetVertexAt(SubentityId) -> Point3d
        
        GetVertexAt(int) -> Point3d
        
        """
        pass
    
    
    def MergeFaces(self):
        """
        MergeFaces -> void
        
        """
        pass
    
    
    def Setbox(self):
        """
        Setbox -> void
        
        """
        pass
    
    
    def SetCone(self):
        """
        SetCone -> void
        
        """
        pass
    
    
    def SetCrease(self):
        """
        SetCrease(FullSubentityPath[], double) -> void
        
        SetCrease(double) -> void
        
        """
        pass
    
    
    def SetCylinder(self):
        """
        SetCylinder -> void
        
        """
        pass
    
    
    def SetDragStatus(self):
        """
        SetDragStatus -> void
            
            DragStatus status: 
            Value describing the status of the drag operation; one of the values from the DragStat enumeration
        """
        pass
    
    
    def SetPyramid(self):
        """
        SetPyramid -> void
        
        """
        pass
    
    
    def SetSphere(self):
        """
        SetSphere -> void
        
        """
        pass
    
    
    def SetSubDMesh(self):
        """
        SetSubDMesh -> void
        
        """
        pass
    
    
    def SetSubentColor(self):
        """
        SetSubentColor -> void
        
        """
        pass
    
    
    def SetSubentMaterial(self):
        """
        SetSubentMaterial -> void
        
        """
        pass
    
    
    def SetSubentMaterialMapper(self):
        """
        SetSubentMaterialMapper -> void
        
        """
        pass
    
    
    def SetTorus(self):
        """
        SetTorus -> void
        
        """
        pass
    
    
    def SetVertexAt(self):
        """
        SetVertexAt(SubentityId, Point3d) -> void
        
        SetVertexAt(int, Point3d) -> void
        
        """
        pass
    
    
    def SetWedge(self):
        """
        SetWedge -> void
        
        """
        pass
    
    
    def Spin(self):
        """
        Spin -> void
        
        """
        pass
    
    
    def SplitFace(self):
        """
        SplitFace -> void
        
        """
        pass
    
    
    def SubdDivideDown(self):
        """
        SubdDivideDown -> void
        
        """
        pass
    
    
    def SubdDivideUp(self):
        """
        SubdDivideUp -> void
        
        """
        pass
    
    
    def SubdRefine(self):
        """
        SubdRefine() -> void
        
        SubdRefine(FullSubentityPath[]) -> void
        
        """
        pass
    
    
    FaceArray = None
    
    
    NormalArray = None
    
    
    NumberOfFaces = None
    
    
    NumberOfSubDividedFaces = None
    
    
    NumberOfSubDividedVertices = None
    
    
    NumberOfVertices = None
    
    
    SmoothLevel = None
    
    
    SubDividedFaceArray = None
    
    
    SubDividedNormalArray = None
    
    
    SubDividedVertices = None
    
    
    VertexColorArray = None
    
    
    VertexNormalArray = None
    
    
    VertexTextureArray = None
    
    
    Vertices = None
    
    
    Watertight = None
    
    pass

class SubentRef(object):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def CreateEntity(self):
        """
        CreateEntity -> Autodesk.AutoCAD.DatabaseServices.Entity
        
        """
        pass
    
    
    Entity = None
    
    
    SubentId = None
    
    pass

class SubentityGeometry(object):
    """
    
    SubentityGeometry()()
    
    
    SubentityGeometry(Curve3d)
        Curve3d curve : The curve is not owned by this SubentityGeometry.
    
    
    SubentityGeometry(Point3d)
        Point3d pnt : The coordinates of the point subentity.
    
    
    """
    Curve = None
    
    
    Point = None
    
    
    Type = None
    
    pass

class SubentityOverrule(object):
    """
    
    """
    def AddSubentPaths(self):
        """
        AddSubentPaths -> void
        
        """
        pass
    
    
    def DeleteSubentPaths(self):
        """
        DeleteSubentPaths -> void
        
        """
        pass
    
    
    def GetCompoundObjectTransform(self):
        """
        GetCompoundObjectTransform -> Matrix3d
        
        """
        pass
    
    
    def GetGripPointsAtSubentPath(self):
        """
        GetGripPointsAtSubentPath -> void
        
        """
        pass
    
    
    def GetGsMarkersAtSubentPath(self):
        """
        GetGsMarkersAtSubentPath -> IntPtr()
        
        """
        pass
    
    
    def GetSubentClassId(self):
        """
        GetSubentClassId -> Guid
        
        """
        pass
    
    
    def GetSubentPathGeomExtents(self):
        """
        GetSubentPathGeomExtents -> Extents3d
        
        """
        pass
    
    
    def GetSubentPathsAtGsMarker(self):
        """
        GetSubentPathsAtGsMarker -> FullSubentityPath()
        
        """
        pass
    
    
    def MoveGripPointsAtSubentPaths(self):
        """
        MoveGripPointsAtSubentPaths -> void
        
        """
        pass
    
    
    def OnSubentGripStatusChanged(self):
        """
        OnSubentGripStatusChanged -> void
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def SubentPtr(self):
        """
        SubentPtr -> Entity
        
        """
        pass
    
    
    def TransformSubentPathsBy(self):
        """
        TransformSubentPathsBy -> void
        
        """
        pass
    
    pass

class SubentityType():
    Null = None
    Face = None
    Edge = None
    Vertex = None
    MlineCache = None
    Class = None

class Sun(object):
    """
    
    Sun()
    """
    Altitude = None
    
    
    Azimuth = None
    
    
    DateTime = None
    
    
    Intensity = None
    
    
    IsDaylightSavingsOn = None
    
    
    IsOn = None
    
    
    ShadowParameters = None
    
    
    SkyParameters = None
    
    
    SunColor = None
    
    
    SunDirection = None
    
    pass

class Surface(object):
    """
    
    """
    class WireframeType():
        Isolines = None
        IsoParms = None
    
    
    def ChamferEdges(self):
        """
        ChamferEdges(SubentityId[], SubentityId, double, double) -> void
        
        ChamferEdges(SubentityId[], SubentityId, double, double, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def SliceBySurface(self):
        """
        SliceBySurface -> SurfaceSliceResults
        
        """
        pass
    
    
    def ConvertToNurbSurface(self):
        """
        ConvertToNurbSurface -> Autodesk.AutoCAD.DatabaseServices.NurbSurface()
        
        """
        pass
    
    
    def CreateBlendSurface(self):
        """
        CreateBlendSurface(LoftProfile, LoftProfile, BlendOptions) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateBlendSurface(LoftProfile, LoftProfile, BlendOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateExtendSurface(self):
        """
        CreateExtendSurface -> ObjectId
        
        """
        pass
    
    
    def CreateExtrudedSurface(self):
        """
        CreateExtrudedSurface(Profile3d, Vector3d, SweepOptions) -> ExtrudedSurface
        
        CreateExtrudedSurface(Profile3d, Vector3d, SweepOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateFilletSurface(self):
        """
        CreateFilletSurface(ObjectId, Point3d, ObjectId, Point3d, double, Autodesk.AutoCAD.DatabaseServices.FilletTrimMode, Vector3d) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateFilletSurface(ObjectId, Point3d, ObjectId, Point3d, double, Autodesk.AutoCAD.DatabaseServices.FilletTrimMode, Vector3d, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateInterferenceObjects(self):
        """
        CreateInterferenceObjects -> Entity()
        
        """
        pass
    
    
    def CreateLoftedSurface(self):
        """
        CreateLoftedSurface(LoftProfile[], LoftProfile[], LoftProfile, LoftOptions) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateLoftedSurface(LoftProfile[], LoftProfile[], LoftProfile, LoftOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateNetworkSurface(self):
        """
        CreateNetworkSurface(Profile3d[], Profile3d[]) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreateNetworkSurface(Profile3d[], Profile3d[], [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateOffsetSurface(self):
        """
        CreateOffsetSurface(Entity, double) -> Entity
        
        CreateOffsetSurface(Entity, double, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreatePatchSurface(self):
        """
        CreatePatchSurface(PathRef, ObjectIdCollection, int, double) -> Autodesk.AutoCAD.DatabaseServices.Surface
        
        CreatePatchSurface(PathRef, ObjectIdCollection, int, double, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateRevolvedSurface(self):
        """
        CreateRevolvedSurface(Profile3d, Point3d, Vector3d, double, double, RevolveOptions) -> RevolvedSurface
        
        CreateRevolvedSurface(Profile3d, Point3d, Vector3d, double, double, RevolveOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        CreateRevolvedSurface(Profile3d, Profile3d, [MarshalAs(UnmanagedType.U1)] bool, double, double, RevolveOptions) -> RevolvedSurface
        
        CreateRevolvedSurface(Profile3d, Profile3d, [MarshalAs(UnmanagedType.U1)] bool, double, double, RevolveOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def CreateSectionObjects(self):
        """
        CreateSectionObjects -> Entity()
        
        """
        pass
    
    
    def CreateSweptSurface(self):
        """
        CreateSweptSurface(Profile3d, Profile3d, SweepOptions) -> SweptSurface
        
        CreateSweptSurface(Profile3d, Profile3d, SweepOptions, [MarshalAs(UnmanagedType.U1)] bool) -> ObjectId
        
        """
        pass
    
    
    def ExtendEdges(self):
        """
        ExtendEdges -> void
        
        """
        pass
    
    
    def FilletEdges(self):
        """
        FilletEdges(SubentityId[], DoubleCollection, DoubleCollection, DoubleCollection) -> void
        
        FilletEdges(SubentityId[], double, [MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def GetSubentityColor(self):
        """
        GetSubentityColor -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def GetSubentityMaterial(self):
        """
        GetSubentityMaterial -> ObjectId
        
        """
        pass
    
    
    def GetSubentityMaterialMapper(self):
        """
        GetSubentityMaterialMapper -> Mapper
        
        """
        pass
    
    
    def ImprintEntity(self):
        """
        ImprintEntity -> void
        
        """
        pass
    
    
    def ProjectOnToSurface(self):
        """
        ProjectOnToSurface -> Entity()
        
        """
        pass
    
    
    def RayTest(self):
        """
        RayTest -> void
        
        """
        pass
    
    
    def SetSubentityColor(self):
        """
        SetSubentityColor -> void
        
        """
        pass
    
    
    def SetSubentityMaterial(self):
        """
        SetSubentityMaterial -> void
        
        """
        pass
    
    
    def SetSubentityMaterialMapper(self):
        """
        SetSubentityMaterialMapper -> void
        
        """
        pass
    
    
    def SliceByPlane(self):
        """
        SliceByPlane -> SurfaceSliceResults
        
        """
        pass
    
    
    def TrimSurface(self):
        """
        TrimSurface -> void
        
        """
        pass
    
    
    CreationActionBodyId = None
    
    
    ModificationActionBodyIds = None
    
    
    Perimeter = None
    
    
    UIsoLineDensity = None
    
    
    UsesGraphicsCache = None
    
    
    WireframeType = None
    
    pass

class SurfaceTrimInfo(object):
    """
    
    SurfaceTrimInfo()
    """
    class TrimRelation():
        InsideTool = None
        OutsideTool = None
    
    
    def SetTrimInfo(self):
        """
        SetTrimInfo(CompoundObjectId, TrimRelation, SubentityId) -> void
        
        SetTrimInfo(CompoundObjectId, Vector3d, TrimRelation) -> void
        
        """
        pass
    
    
    IsCurve = None
    
    
    ProjVector = None
    
    
    Relation = None
    
    
    ToolBodyId = None
    
    pass

class SweepOptionsAlignOption():
    NoAlignment = None
    AlignSweepEntityToPath = None
    TranslateSweepEntityToPath = None
    TranslatePathToSweepEntity = None

class SweptSurface(object):
    """
    
    SweptSurface()
    """
    def CreateSweptSurface(self):
        """
        CreateSweptSurface -> void
            
            Entity sweepEnt: 
            Input the curve, region, or planar surface to be swept
            
            Entity pathEnt: 
            Input the curve entity that specifies the path along which sweepEnt is to be swept
            
            Autodesk.AutoCAD.DatabaseServices.SweepOptions sweepOptions: 
            Input sweep options
        """
        pass
    
    
    Bank = None
    
    
    PathEntity = None
    
    
    PathLength = None
    
    
    PathProfile = None
    
    
    ProfileRotation = None
    
    
    ScaleAlongPath = None
    
    
    SweepEntity = None
    
    
    SweepOptions = None
    
    
    SweepProfile = None
    
    
    TwistAlongPath = None
    
    pass

class SymbolTable(object):
    """
    
    """
    def Add(self):
        """
        Add -> ObjectId
            
            [CallerMustClose] SymbolTableRecord value: 
            Input record to add to the table
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> SymbolTableEnumerator
        
        """
        pass
    
    
    def Has(self):
        """
        Has(ObjectId) -> bool
            
            ObjectId id: 
            Input object ID of record to search for
        Has(string) -> bool
            
            string key: 
            Input name of record to search for
        """
        pass
    
    
    IncludingErased = None
    
    pass

class SymbolTableEnumerator(object):
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

class SymbolTableRecord(object):
    """
    
    """
    IsDependent = None
    
    
    IsResolved = None
    
    
    Name = None
    
    pass

class SymbolUtilityServices(object):
    """
    
    """
    def GetBlockModelSpaceId(self):
        """
        GetBlockModelSpaceId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetBlockNameFromInsertPathName(self):
        """
        GetBlockNameFromInsertPathName -> string
            
            string pathName: 
            Input path name to examine
        """
        pass
    
    
    def GetBlockPaperSpaceId(self):
        """
        GetBlockPaperSpaceId -> ObjectId
            
            Database databasePointer: 
            Input pointer to database to access
        """
        pass
    
    
    def GetInsertPathNameFromBlockName(self):
        """
        GetInsertPathNameFromBlockName -> string
            
            string blockName: 
            Input name of block from which to get the path
        """
        pass
    
    
    def GetLayerDefpointsId(self):
        """
        GetLayerDefpointsId -> ObjectId
            
            Database database: 
            Input database to access
        """
        pass
    
    
    def GetLayerZeroId(self):
        """
        GetLayerZeroId -> ObjectId
            
            Database database: 
            Input database to access
        """
        pass
    
    
    def GetLinetypeByBlockId(self):
        """
        GetLinetypeByBlockId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetLinetypeByLayerId(self):
        """
        GetLinetypeByLayerId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetLinetypeContinuousId(self):
        """
        GetLinetypeContinuousId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetMaxSymbolNameLength(self):
        """
        GetMaxSymbolNameLength -> Integer
            
            [MarshalAs(UnmanagedType.U1)] bool isNewName: 
            Input Boolean to indicate whether we want to the length for extended or legacy symbol names
            
            [MarshalAs(UnmanagedType.U1)] bool compatibilityMode: 
            Input Boolean to indicate extended or legacy symbol names
            
            false: 
            max=31
            
            true: 
            max=31
        """
        pass
    
    
    def GetPathNameFromSymbolName(self):
        """
        GetPathNameFromSymbolName -> string
            
            string symbolName: 
            Input name of block from which to get the path
            
            string extensions: 
            Input list of extensions for which to search
        """
        pass
    
    
    def GetRegAppAcadId(self):
        """
        GetRegAppAcadId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def GetSymbolNameFromPathName(self):
        """
        GetSymbolNameFromPathName -> string
            
            string pathName: 
            Input path name
            
            string extensions: 
            Input list of extensions to consider
        """
        pass
    
    
    def GetTextStyleStandardId(self):
        """
        GetTextStyleStandardId -> ObjectId
            
            Database databasePointer: 
            Input database to access
        """
        pass
    
    
    def IsBlockLayoutName(self):
        """
        IsBlockLayoutName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsBlockModelSpaceName(self):
        """
        IsBlockModelSpaceName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsBlockPaperSpaceName(self):
        """
        IsBlockPaperSpaceName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsCompatibilityMode(self):
        """
        IsCompatibilityMode -> bool
            
            Database database: 
            Input database to access
        """
        pass
    
    
    def IsLayerDefpointsName(self):
        """
        IsLayerDefpointsName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLayerZeroName(self):
        """
        IsLayerZeroName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLinetypeByBlockName(self):
        """
        IsLinetypeByBlockName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLinetypeByLayerName(self):
        """
        IsLinetypeByLayerName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsLinetypeContinuousName(self):
        """
        IsLinetypeContinuousName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsRegAppAcadName(self):
        """
        IsRegAppAcadName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsTextStyleStandardName(self):
        """
        IsTextStyleStandardName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def IsViewportActiveName(self):
        """
        IsViewportActiveName -> bool
            
            string name: 
            Input name to compare
        """
        pass
    
    
    def MakeDependentName(self):
        """
        MakeDependentName -> string
            
            string dwgName: 
            Input the drawing name
            
            string symbolName: 
            Input the symbol name
        """
        pass
    
    
    def PreValidateSymbolName(self):
        """
        PreValidateSymbolName -> string
            
            [MarshalAs(UnmanagedType.U1)] bool preserveCase: 
            Input Boolean to indicate whether to preserve the case of alphabetic letters
        """
        pass
    
    
    def RepairPreExtendedSymbolName(self):
        """
        RepairPreExtendedSymbolName -> string
            
            string oldName: 
            Input symbol name to repair
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate is vertical bars are allowed in the symbol name
        """
        pass
    
    
    def RepairSymbolName(self):
        """
        RepairSymbolName -> string
            
            string oldName: 
            Input symbol name to repair
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate if vertical bars are allowed in the symbol name
        """
        pass
    
    
    def ValidateCompatibleSymbolName(self):
        """
        ValidateCompatibleSymbolName -> ErrorStatus
            
            string name: 
            Input name to validate
            
            [MarshalAs(UnmanagedType.U1)] bool isNewName: 
            Input Boolean to indicate whether to treat the name as a new or an existing name
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate whether to allow vertical bars in the name
            
            [MarshalAs(UnmanagedType.U1)] bool compatibilityMode: 
            Input Boolean to indicate whether the validate the name as an extended or legacy symbol name
        """
        pass
    
    
    def ValidatePreExtendedSymbolName(self):
        """
        ValidatePreExtendedSymbolName -> void
            
            string name: 
            Input name to validate
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate if vertical bars are valid in the symbol name
        """
        pass
    
    
    def ValidateSymbolName(self):
        """
        ValidateSymbolName -> void
            
            string name: 
            Input name to validate
            
            [MarshalAs(UnmanagedType.U1)] bool allowVerticalBar: 
            Input Boolean to indicate if vertical bars are valid in the symbol name
        """
        pass
    
    
    BlockModelSpaceName = None
    
    
    BlockPaperSpaceName = None
    
    
    LayerDefpointsName = None
    
    
    LayerZeroName = None
    
    
    LinetypeByBlockName = None
    
    
    LinetypeByLayerName = None
    
    
    LinetypeContinuousName = None
    
    
    RegAppAcadName = None
    
    
    TextStyleStandardName = None
    
    
    ViewportActiveName = None
    
    pass

class SymmetricConstraint(object):
    """
    
    SymmetricConstraint()
    """

    pass

class Table(object):
    """
    
    Table()
    """
    def Alignment(self):
        """
        Alignment(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which the cell alignment value will be returned
        Alignment(int, int) -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def AttachmentPoint(self):
        """
        AttachmentPoint -> Point3d
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BackgroundColor(self):
        """
        BackgroundColor(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which the Color value is returned
        BackgroundColor(int, int) -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BlockRotation(self):
        """
        BlockRotation -> double
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BlockScale(self):
        """
        BlockScale -> double
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def BlockTableRecordId(self):
        """
        BlockTableRecordId -> ObjectId
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def CanDeleteColumns(self):
        """
        CanDeleteColumns -> bool
            
            int index: 
            Input System.Int32 object to check if a column can be deleted.
            
            int nCount: 
            Input number of columns to delete
        """
        pass
    
    
    def CanDeleteRows(self):
        """
        CanDeleteRows -> bool
            
            int index: 
            Input System.Int32 object to check if a row can be deleted.
            
            int nCount: 
            Input number of rows to delete
        """
        pass
    
    
    def CanInsertColumn(self):
        """
        CanInsertColumn -> bool
            
            int index: 
            Input System.Int32 object to check if new column can be inserted.
        """
        pass
    
    
    def CanInsertRow(self):
        """
        CanInsertRow -> bool
            
            int index: 
            Input System.Int32 object to check if new row can be inserted.
        """
        pass
    
    
    def CellStyleOverrides(self):
        """
        CellStyleOverrides -> TableStyleOverride()
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def CellType(self):
        """
        CellType -> TableCellType
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def ClearSubSelection(self):
        """
        ClearSubSelection -> void
        
        """
        pass
    
    
    def ClearTableStyleOverrides(self):
        """
        ClearTableStyleOverrides -> void
            
            int options: 
            Input System.Int32 object.
        """
        pass
    
    
    def ColumnWidth(self):
        """
        ColumnWidth -> double
            
            int col: 
            Input zero-based column index
        """
        pass
    
    
    def ContentColor(self):
        """
        ContentColor(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input Autodesk.AutoCAD.DatabaseServices.RowType object specifying the row type for which the Color value will be returned
        ContentColor(int, int) -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom(LinkedTableData, TableCopyOptions) -> void
            
            LinkedTableData source: 
            Input source table
            
            TableCopyOptions options: 
            Input copy option
        CopyFrom(LinkedTableData, TableCopyOptions, CellRange, CellRange) -> CellRange
            
            LinkedTableData source: 
            Input source table
            
            TableCopyOptions options: 
            Input copy option
            
            CellRange sourceRange: 
            Input source cell range
            
            CellRange targetRange: 
            Input target cell range
        CopyFrom(Table, TableCopyOptions, CellRange, CellRange) -> CellRange
            
            Table source: 
            Input table source
            
            TableCopyOptions options: 
            Input table copy options
            
            CellRange sourceRange: 
            Input source cell range
            
            CellRange targetRange: 
            Input target cell range
        """
        pass
    
    
    def CreateContent(self):
        """
        CreateContent -> Integer
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def DataType(self):
        """
        DataType(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input Autodesk.AutoCAD.DatabaseServices.RowType object specifying the data type
        DataType(int, int) -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def DeleteCellContent(self):
        """
        DeleteCellContent -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def DeleteColumns(self):
        """
        DeleteColumns -> void
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            int columns: 
            Input System.Int32 object number of columns to delete
        """
        pass
    
    
    def DeleteContent(self):
        """
        DeleteContent(CellRange) -> void
            
            range: 
            Input range of cells to delete the contents
        DeleteContent(int, int) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        DeleteContent(int, int, int) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of row.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def DeleteRows(self):
        """
        DeleteRows -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int rows: 
            Input System.Int32 object number of rows to delete
        """
        pass
    
    
    def FieldId(self):
        """
        FieldId -> ObjectId
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def Fill(self):
        """
        Fill -> void
            
            CellRange fillRange: 
            Input Autodesk.AutoCAD.DatabaseServices.CellRange object. Range to be filled. This shouldn't overlap the source range except when this range is to be cleared instead of filled in which case this range should be contained fully in source range.
            
            CellRange sourceRange: 
            Input Autodesk.AutoCAD.DatabaseServices.CellRange object. Source range to copy or use as pattern. This can be set to invalid range if the fill range is to be cleared.
            
            TableFillOptions options: 
            Input table copy options
        """
        pass
    
    
    def Format(self):
        """
        Format(Autodesk.AutoCAD.DatabaseServices.RowType) -> string
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input cell format type
        Format(int, int) -> string
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
        """
        pass
    
    
    def GenerateLayout(self):
        """
        GenerateLayout -> void
        
        """
        pass
    
    
    def GetBlockAttributeValue(self):
        """
        GetBlockAttributeValue(int, int, ObjectId) -> string
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            ObjectId attributeDefinitionId: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object.
        GetBlockAttributeValue(int, int, int, ObjectId) -> string
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int column: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            ObjectId attDefId: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object.
        """
        pass
    
    
    def GetBlockTableRecordId(self):
        """
        GetBlockTableRecordId -> ObjectId
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int column: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetBreakHeight(self):
        """
        GetBreakHeight -> double
            
            int index: 
            Input table index. It should be more than or equal to 0 and less than the number of multiple tables, when the table breaks.
        """
        pass
    
    
    def GetBreakOffset(self):
        """
        GetBreakOffset -> Vector3d
            
            int index: 
            Input table index. It should be more than or equal to 0 and less than the number of multiple tables, when the table breaks.
        """
        pass
    
    
    def GetBreakSpacing(self):
        """
        GetBreakSpacing -> double
        
        """
        pass
    
    
    def GetCellExtents(self):
        """
        GetCellExtents -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            [MarshalAs(UnmanagedType.U1)] bool isOuterCell: 
            Output System.Boolean object indicating whether the specified cell is an outer cell
            
            Point3dCollection pts: 
            Output Autodesk.AutoCAD.Geometry.Point3dCollection object; point collection containing the cell extents information
        """
        pass
    
    
    def GetCellState(self):
        """
        GetCellState -> CellStates
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetCellStyle(self):
        """
        GetCellStyle -> string
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
        """
        pass
    
    
    def GetColumnName(self):
        """
        GetColumnName -> string
            
            int index: 
            Input zero based index of the column
        """
        pass
    
    
    def GetContentColor(self):
        """
        GetContentColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetContentLayout(self):
        """
        GetContentLayout -> Autodesk.AutoCAD.DatabaseServices.CellContentLayout
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetContentTypes(self):
        """
        GetContentTypes(int, int) -> CellContentTypes
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        GetContentTypes(int, int, int) -> CellContentTypes
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetCustomData(self):
        """
        GetCustomData(int, int) -> Integer
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
        GetCustomData(int, int, string) -> object
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            string key: 
            Input key to store the custom data
        """
        pass
    
    
    def GetDataFormat(self):
        """
        GetDataFormat(int, int) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        GetDataFormat(int, int, int) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetDataLink(self):
        """
        GetDataLink() -> ObjectIdCollection
        
        GetDataLink(CellRange) -> ObjectIdCollection
            
            CellRange range: 
            Input range to get the data links. If this is NULL it gets all the data links in the table.
        GetDataLink(int, int) -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetDataLinkRange(self):
        """
        GetDataLinkRange -> CellRange
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetDataType(self):
        """
        GetDataType -> DataTypeParameter
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator() -> TableEnumerator
        
        GetEnumerator(CellRange, TableEnumeratorOption) -> TableEnumerator
            
            CellRange range: 
            Input range of cells to delete the contents
            
            TableEnumeratorOption option: 
            Input enumerator option
        """
        pass
    
    
    def GetFieldId(self):
        """
        GetFieldId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetFormula(self):
        """
        GetFormula -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetIsAutoScale(self):
        """
        GetIsAutoScale -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetMargin(self):
        """
        GetMargin -> double
            
            int row: 
            Input row index. Pass the value -1 if you are only concerned with the column.
            
            int column: 
            Input row index. Pass the value -1 if you are only concerned with the row.
            
            CellMargins margin: 
            Input margin type to get
        """
        pass
    
    
    def GetMergeAllEnabled(self):
        """
        GetMergeAllEnabled -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetMergeRange(self):
        """
        GetMergeRange -> CellRange
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetNumberOfContents(self):
        """
        GetNumberOfContents -> Integer
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetOverrides(self):
        """
        GetOverrides(int, int, int) -> CellProperties
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            int contentIndex: 
            Input content index.
        GetOverrides(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType) -> CellProperties
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type
        """
        pass
    
    
    def GetRotation(self):
        """
        GetRotation -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetScale(self):
        """
        GetScale -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetTextHeight(self):
        """
        GetTextHeight -> double
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetTextString(self):
        """
        GetTextString(int, int, int) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents
        GetTextString(int, int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> string
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption formatOption: 
            Input null-terminated text string
        """
        pass
    
    
    def GetTextStyleId(self):
        """
        GetTextStyleId -> ObjectId
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def GetToolTip(self):
        """
        GetToolTip -> string
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue(int, int, int) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        GetValue(int, int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption formatOption: 
            Input Autodesk.AutoCAD.DatabaseServices.FormatOption object; format option
        """
        pass
    
    
    def GridColor(self):
        """
        GridColor(int, int, CellEdgeMasks) -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input object specifying the zero-based row index for the cell
            
            int col: 
            Input object specifying the zero-based column index for the cell
            
            CellEdgeMasks edge: 
            Input object specifying the edge index for the cell
        GridColor(Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridlineType: 
            Input grid line type for which to return the Color value
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which to return the Color value
        """
        pass
    
    
    def GridLineWeight(self):
        """
        GridLineWeight(int, int, CellEdgeMasks) -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int row: 
            Input row index. This can be -1.
            
            int col: 
            Input column index. This can be -1.
            
            CellEdgeMasks edge: 
            Input integer specifying the edge index for the cell
        GridLineWeight(Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridlineType: 
            To specify cell pass a valid row and column indices; to specify row pass a valid row index and pass -1 as column index; to specify column pass a valid column index and pass -1 as row index.
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type.
        """
        pass
    
    
    def GridVisibility(self):
        """
        GridVisibility(int, int, CellEdgeMasks) -> bool
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            CellEdgeMasks edge: 
            Input specifying the edge index for the cell
        GridVisibility(Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.RowType) -> bool
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridlineType: 
            Input grid line type for which to return the grid visibility
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which to return the grid visibility
        """
        pass
    
    
    def HasFormula(self):
        """
        HasFormula -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        """
        pass
    
    
    def HitTest(self):
        """
        HitTest -> TableHitTestInfo
            
            Point3d point: 
            Input 3D point in WCS specifying the input picking point
            
            Vector3d viewVector: 
            Input 3D vector in WCS specifying the view direction for the hit test
        """
        pass
    
    
    def InsertColumns(self):
        """
        InsertColumns -> void
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            double width: 
            Input width for the inserted columns
            
            int columns: 
            Input number of columns to insert
        """
        pass
    
    
    def InsertColumnsAndInherit(self):
        """
        InsertColumnsAndInherit -> void
            
            int col: 
            Input index at which to insert the new columns
            
            int inheritFrom: 
            Input index of the column to inherit the format for the new columns. It can be -1. If it is -1 new columns don't inherit any format and they use default format.
            
            int numCols: 
            Input number of columns to insert
        """
        pass
    
    
    def InsertRows(self):
        """
        InsertRows -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            double height: 
            Input height for the inserted rows
            
            int rows: 
            Input number of rows to insert
        """
        pass
    
    
    def InsertRowsAndInherit(self):
        """
        InsertRowsAndInherit -> void
            
            int index: 
            Input index at which to insert the new rows
            
            int inheritFrom: 
            Input index of the row to inherit the format for the new rows. It can be -1. If it is -1 new rows don't inherit any format and they use default format.
            
            int numRows: 
            Input number of rows to insert
        """
        pass
    
    
    def IsAutoScale(self):
        """
        IsAutoScale -> bool
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
        """
        pass
    
    
    def IsBackgroundColorNone(self):
        """
        IsBackgroundColorNone(Autodesk.AutoCAD.DatabaseServices.RowType) -> bool
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type for which to return the Boolean value indicating whether the background color is set to none
        IsBackgroundColorNone(int, int) -> bool
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
        """
        pass
    
    
    def IsContentEditable(self):
        """
        IsContentEditable -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsEmpty(self):
        """
        IsEmpty -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsFormatEditable(self):
        """
        IsFormatEditable -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsLinked(self):
        """
        IsLinked -> bool
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def IsMergedCell(self):
        """
        IsMergedCell -> bool
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            out CellRange range: 
            Output the range of merged cells
        """
        pass
    
    
    def MergeCells(self):
        """
        MergeCells -> void
            
            CellRange range: 
            Input range of cells to merge
        """
        pass
    
    
    def MinimumColumnWidth(self):
        """
        MinimumColumnWidth -> double
            
            int col: 
            Input zero-based column index
        """
        pass
    
    
    def MinimumRowHeight(self):
        """
        MinimumRowHeight -> double
            
            int row: 
            Input zero-based row index
        """
        pass
    
    
    def MoveContent(self):
        """
        MoveContent -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int fromIndex: 
            Input index of the content to move
            
            int toIndex: 
            Input get index to which the content should be moved
        """
        pass
    
    
    def RecomputeTableBlock(self):
        """
        RecomputeTableBlock -> void
            
            [MarshalAs(UnmanagedType.U1)] bool forceUpdate: 
            Input indicating whether to force an update on the screen
        """
        pass
    
    
    def RemoveAllOverrides(self):
        """
        RemoveAllOverrides -> void
            
            int row: 
            Input row index. Insert the value -1 if you are only concerned with a column.
            
            int column: 
            Input column index. Insert the value -1 if you are only concerned with a row.
        """
        pass
    
    
    def RemoveDataLink(self):
        """
        RemoveDataLink() -> void
        
        RemoveDataLink(int, int) -> void
            
            int row: 
            Input row index. Insert the value -1 if you are only concerned with a column.
            
            int column: 
            Input column index. Insert the value -1 if you are only concerned with a row.
        """
        pass
    
    
    def ReselectSubRegion(self):
        """
        ReselectSubRegion -> void
            
            FullSubentityPath[] paths: 
            Output array of FullSubentPath
        """
        pass
    
    
    def ResetValue(self):
        """
        ResetValue -> void
            
            int row: 
            Input object specifying the zero-based row index for the cell
            
            int col: 
            Input object specifying the zero-based column index for the cell
        """
        pass
    
    
    def RowHeight(self):
        """
        RowHeight -> double
            
            int row: 
            Input zero-based row index
        """
        pass
    
    
    def RowType(self):
        """
        RowType -> Autodesk.AutoCAD.DatabaseServices.RowType
            
            int row: 
            Input zero-based row index
        """
        pass
    
    
    def Select(self):
        """
        Select -> TableHitTestInfo
            
            Point3d pickingPoint: 
            Input 3D point in WCS specifying the input picking point
            
            Vector3d hitTestViewDirection: 
            Input 3D vector in WCS specifying the view direction for the hit test
            
            Vector3d hitTestViewOrientation: 
            Input 3D vector in WCS specifying the view orientation for the hit test
            
            [MarshalAs(UnmanagedType.U1)] bool allowOutside: 
            Input indicating whether a pick point outside the table will select a cell
            
            [MarshalAs(UnmanagedType.U1)] bool inPickFirst: 
            Input indicating if the entity is already in the pickfirst set (true) or if the pickfirst logic should attempt to subselect the entity directly (false)
            
            FullSubentityPath[] paths: 
            Output SubentPathArray 
        """
        pass
    
    
    def SetAlignment(self):
        """
        SetAlignment(int, int, Autodesk.AutoCAD.DatabaseServices.CellAlignment) -> void
            
            int row: 
            Input specifying the zero-based row index for the ce
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            Autodesk.AutoCAD.DatabaseServices.CellAlignment align: 
            Input enum value specifying the cell alignment
        SetAlignment(Autodesk.AutoCAD.DatabaseServices.CellAlignment, int) -> void
            
            Autodesk.AutoCAD.DatabaseServices.CellAlignment align: 
            Input cell alignment
            
            int rowTypes: 
            Input row types
        """
        pass
    
    
    def SetAutoScale(self):
        """
        SetAutoScale -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            [MarshalAs(UnmanagedType.U1)] bool autoFit: 
            Input Boolean indicating whether to auto fit the block at the specified cell
        """
        pass
    
    
    def SetBackgroundColor(self):
        """
        SetBackgroundColor(int, int, Autodesk.AutoCAD.Colors.Color) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input background color
        SetBackgroundColor(Autodesk.AutoCAD.Colors.Color, int) -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input background color
            
            int rowTypes: 
            Input row types
        """
        pass
    
    
    def SetBackgroundColorNone(self):
        """
        SetBackgroundColorNone([MarshalAs(UnmanagedType.U1)] bool, int) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input indicating whether to enable the background color for the specified row type
            
            int rowTypes: 
            Input row types
        SetBackgroundColorNone(int, int, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input indicating whether to enable the background color for the specified cell
        """
        pass
    
    
    def SetBlockAttributeValue(self):
        """
        SetBlockAttributeValue(int, int, ObjectId, string) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            ObjectId attributeDefinitionId: 
            Input the object ID of an of AttributeDefinition object
            
            string value: 
            Input character string specifying attribute v
        SetBlockAttributeValue(int, int, int, ObjectId, string) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents
            
            ObjectId attDefId: 
            Input the object ID of the AttributeDefinition object
            
            string value: 
            Input character string specifying attribute value
        """
        pass
    
    
    def SetBlockRotation(self):
        """
        SetBlockRotation -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            double rotationalAngle: 
            Input rotation angle
        """
        pass
    
    
    def SetBlockScale(self):
        """
        SetBlockScale -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            double scale: 
            Input scale factor
        """
        pass
    
    
    def SetBlockTableRecordId(self):
        """
        SetBlockTableRecordId(int, int, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            ObjectId blockId: 
            Input BlockTableRecord object ID
            
            [MarshalAs(UnmanagedType.U1)] bool autoFit: 
            Input indicating whether to auto fit the block into the specified cell
        SetBlockTableRecordId(int, int, int, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            ObjectId blockId: 
            Input block table record id to set
            
            [MarshalAs(UnmanagedType.U1)] bool autoFit: 
            Input System.Boolean object indicating whether to auto fit the block into the specified cell
        """
        pass
    
    
    def SetBreakHeight(self):
        """
        SetBreakHeight -> void
            
            int index: 
            Input table index. It should be more than or equal to 0 and less than the number of multiple tables, when the table breaks.
            
            double height: 
            Input break height
        """
        pass
    
    
    def SetBreakOffset(self):
        """
        SetBreakOffset -> void
            
            int index: 
            Input table index. It should be more than or equal to 0 and less than the number of multiple tables, when the table breaks.
            
            Vector3d offset: 
            Input offset value
        """
        pass
    
    
    def SetBreakSpacing(self):
        """
        SetBreakSpacing -> void
            
            double spacing: 
            Input spacing
        """
        pass
    
    
    def SetCellState(self):
        """
        SetCellState -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            CellStates cellState: 
            Input cell state to set. This will replace all the bits of the current state
        """
        pass
    
    
    def SetCellStyle(self):
        """
        SetCellStyle -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            string styleName: 
            Input cell style to set. The cell style should exist in the table style set in this table.
        """
        pass
    
    
    def SetCellType(self):
        """
        SetCellType -> void
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
            
            TableCellType type: 
            Input enum value specifying the cell type
        """
        pass
    
    
    def SetColumnName(self):
        """
        SetColumnName -> void
            
            int index: 
            Input zero based index of the column
            
            string name: 
            Input column name to set. This can be an empty string.
        """
        pass
    
    
    def SetColumnWidth(self):
        """
        SetColumnWidth(double) -> void
            
            double width: 
            Input uniform width to be used for all the columns in the table
        SetColumnWidth(int, double) -> void
            
            int col: 
            Input zero-based column index
            
            double width: 
            Input width to be used for the specified column
        """
        pass
    
    
    def SetContentColor(self):
        """
        SetContentColor(int, int, int, Autodesk.AutoCAD.Colors.Color) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input Autodesk.AutoCAD.Colors.Color object.
        SetContentColor(int, int, Autodesk.AutoCAD.Colors.Color) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
        SetContentColor(Autodesk.AutoCAD.Colors.Color, int) -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input text color
            
            int rowType: 
            Input row types
        """
        pass
    
    
    def SetCustomData(self):
        """
        SetCustomData(int, int, int) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            int data: 
            Input custom data to set. If this is NULL, it deletes the custom data.
        SetCustomData(int, int, string, object) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            string key: 
            Input key to use for the custom data
            
            object value: 
            Input custom data to set. If this is NULL, it deletes the custom data.
        """
        pass
    
    
    def SetDataFormat(self):
        """
        SetDataFormat(int, int, int, string) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            string format: 
            Input data format to set
        SetDataFormat(int, int, string) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            string format: 
            Input data format to set
        """
        pass
    
    
    def SetDataLink(self):
        """
        SetDataLink(CellRange, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            CellRange range: 
            Input range to get the data links. If this is NULL it gets all the data links in the table.
            
            ObjectId dataLinkId: 
            Output reference to an array to receive the data link IDs.
            
            [MarshalAs(UnmanagedType.U1)] bool bUpdate: 
            Input true if the data link is to be updated after setting it, false if not.
        SetDataLink(int, int, ObjectId, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId dataLinkId: 
            Input the data link object
            
            [MarshalAs(UnmanagedType.U1)] bool bUpdate: 
            Input true if the data link is to be updated after setting it, false if not.
        """
        pass
    
    
    def SetDataType(self):
        """
        SetDataType(Autodesk.AutoCAD.DatabaseServices.DataType, Autodesk.AutoCAD.DatabaseServices.UnitType, int) -> void
            
            Autodesk.AutoCAD.DatabaseServices.DataType nDataType: 
            Input data type to set
            
            Autodesk.AutoCAD.DatabaseServices.UnitType nUnitType: 
            Input unit type to set
            
            int rowTypes: 
            Input row type to set
        SetDataType(int, int, Autodesk.AutoCAD.DatabaseServices.DataType, Autodesk.AutoCAD.DatabaseServices.UnitType) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.DataType nDataType: 
            Input data type to set
            
            Autodesk.AutoCAD.DatabaseServices.UnitType nUnitType: 
            Input unit type to set
        SetDataType(int, int, int, DataTypeParameter) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            DataTypeParameter dataType: 
            Input data type to set
        """
        pass
    
    
    def SetFieldId(self):
        """
        SetFieldId(int, int, ObjectId) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            ObjectId fieldId: 
            Input field id to set
        SetFieldId(int, int, int, ObjectId, Autodesk.AutoCAD.DatabaseServices.CellOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            ObjectId fieldId: 
            Input field id to set
            
            Autodesk.AutoCAD.DatabaseServices.CellOption option: 
            Input one of the CellOption values. If this is InheritCellFormat then the format of the cell will be set in the field.
        """
        pass
    
    
    def SetFormat(self):
        """
        SetFormat(int, int, string) -> void
            
            int row: 
            Input System.Int32 object specifying the zero-based row index for the cell
            
            int col: 
            Input System.Int32 object specifying the zero-based column index for the cell
            
            string pFormat: 
            Input format string to set
        SetFormat(string, int) -> void
            
            string pFormat: 
            Input System.String object.
            
            int rowTypes: 
            Input System.Int32 object.
        """
        pass
    
    
    def SetFormula(self):
        """
        SetFormula -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            string formula: 
            Input formula to set.
        """
        pass
    
    
    def SetGridColor(self):
        """
        SetGridColor(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.Colors.Color) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid color to set
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input grid line types. Multiple grid line types can be combined using OR.
        SetGridColor(int, int, short, Autodesk.AutoCAD.Colors.Color) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            short edges: 
            Input specifying the edge index for the cell
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color to be used for the grid at the specified edge of the cell
        SetGridColor(Autodesk.AutoCAD.Colors.Color, int, int) -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color
            
            int borders: 
            Input grid line types for which to set the color
            
            int rows: 
            Input row types for which to set the color
        """
        pass
    
    
    def SetGridLineWeight(self):
        """
        SetGridLineWeight(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.LineWeight) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight lineWeight: 
            Input grid line weight to set
        SetGridLineWeight(int, int, short, Autodesk.AutoCAD.DatabaseServices.LineWeight) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            short edges: 
            Input specifying the edge index for the cell
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight value: 
            Input lineweight to be used for the grid at the specified edge of the cell
        SetGridLineWeight(Autodesk.AutoCAD.DatabaseServices.LineWeight, int, int) -> void
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight lineWeight: 
            Input lineweight value
            
            int borders: 
            Input grid line types for which to set the lineweight
            
            int rows: 
            Input row types for which to set the lineweight
        """
        pass
    
    
    def SetGridProperty(self):
        """
        SetGridProperty(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, GridPropertyParameter) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            GridPropertyParameter gridProperty: 
            Input grid line properties to set.
        SetGridProperty(CellRange, Autodesk.AutoCAD.DatabaseServices.GridLineType, GridPropertyParameter) -> void
            
            CellRange rangeIn: 
            Input cell range, row range, or column range.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineTypes: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            GridPropertyParameter gridProp: 
            Input grid line properties to set.
        """
        pass
    
    
    def SetGridVisibility(self):
        """
        SetGridVisibility([MarshalAs(UnmanagedType.U1)] bool, int, int) -> void
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            Input visibility
            
            int borders: 
            Input grid line type for which to set the visibility
            
            int rows: 
            Input row type for which to set the visibility
        SetGridVisibility(int, int, short, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            short edges: 
            Input specifying the edge index for the cell
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input visibility to be used for the grid at the specified edge of the cell
        SetGridVisibility(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, Autodesk.AutoCAD.DatabaseServices.Visibility) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.Visibility visibility: 
            Input grid visibility to set
        """
        pass
    
    
    def SetIsAutoScale(self):
        """
        SetIsAutoScale -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            [MarshalAs(UnmanagedType.U1)] bool autoFit: 
            Input status of autofit flag
        """
        pass
    
    
    def SetMargin(self):
        """
        SetMargin -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            CellMargins margin: 
            Input margin type to set. Multiple margin types can be combined using OR
            
            double value: 
            Input margin value to set
        """
        pass
    
    
    def SetMergeAllEnabled(self):
        """
        SetMergeAllEnabled -> void
            
            int row: 
            Input zero-based row index
            
            int column: 
            Input zero-based column index
            
            [MarshalAs(UnmanagedType.U1)] bool enable: 
            Input status of merge all for the cell
        """
        pass
    
    
    def SetOverrides(self):
        """
        SetOverrides(int, int, Autodesk.AutoCAD.DatabaseServices.GridLineType, CellProperties) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type
            
            override: 
            Input override to set
        SetOverrides(int, int, int, CellProperties) -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            int contentIndex: 
            Input content index. This can be -1.
            
            override: 
            Input override to set
        """
        pass
    
    
    def SetRotation(self):
        """
        SetRotation -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            double angle: 
            Input angle in radians
        """
        pass
    
    
    def SetRowHeight(self):
        """
        SetRowHeight(double) -> void
            
            double height: 
            Input height to be used for the specified row
        SetRowHeight(int, double) -> void
            
            int row: 
            Input zero-based row index
            
            double height: 
            Input height to be used for the specified row
        """
        pass
    
    
    def SetScale(self):
        """
        SetScale -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            double scale: 
            Input angle in radians
        """
        pass
    
    
    def SetSize(self):
        """
        SetSize -> void
            
            int numRows: 
            Input number of rows
            
            int numCols: 
            Input number of columns
        """
        pass
    
    
    def SetTextHeight(self):
        """
        SetTextHeight(double, int) -> void
            
            double height: 
            Input text height
            
            int rowTypes: 
            Input row types
        SetTextHeight(int, int, double) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            double height: 
            Input text height
        SetTextHeight(int, int, int, double) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            double height: 
            Input text height
        """
        pass
    
    
    def SetTextString(self):
        """
        SetTextString(int, int, int, string) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents
            
            string text: 
            Input null-terminated text string
        SetTextString(int, int, string) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            string value: 
            Input null-terminated text string
        """
        pass
    
    
    def SetTextStyle(self):
        """
        SetTextStyle(ObjectId, int) -> void
            
            ObjectId id: 
            Input TextStyleTableRecord object ID
            
            int rowTypes: 
            Input row types for which to set the text style
        SetTextStyle(int, int, ObjectId) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            ObjectId id: 
            Input TextStyleTableRecord object ID
        """
        pass
    
    
    def SetTextStyleId(self):
        """
        SetTextStyleId -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            ObjectId id: 
            Input text style
        """
        pass
    
    
    def SetToolTip(self):
        """
        SetToolTip -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            string toolTip: 
            Input tool tip string to set
        """
        pass
    
    
    def SetValue(self):
        """
        SetValue(int, int, int, object) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            object value: 
            Input value to be set
        SetValue(int, int, object) -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            object pValue: 
            Input value to set
        SetValue(int, int, int, object, Autodesk.AutoCAD.DatabaseServices.ParseOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            object value: 
            Input value to be set
            
            Autodesk.AutoCAD.DatabaseServices.ParseOption parseOption: 
            Input Autodesk.AutoCAD.DatabaseServices.ParseOption object; parse option
        SetValue(int, int, int, string, Autodesk.AutoCAD.DatabaseServices.ParseOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            int contentIndex: 
            Input content index. It should be more than or equal to 0 and less than the number of contents.
            
            string value: 
            Input value to set
            
            Autodesk.AutoCAD.DatabaseServices.ParseOption parseOption: 
            Input Autodesk.AutoCAD.DatabaseServices.ParseOption object; parse option
        SetValue(int, int, string, Autodesk.AutoCAD.DatabaseServices.ParseOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            string pText: 
            Input text to convert to value and set
            
            Autodesk.AutoCAD.DatabaseServices.ParseOption nOption: 
            Input parse option.
        """
        pass
    
    
    def SuppressRegenerateTable(self):
        """
        SuppressRegenerateTable -> void
            
            [MarshalAs(UnmanagedType.U1)] bool suppress: 
            Input boolean value to suppress or enable the regeneration of a table object
        """
        pass
    
    
    def TableStyleOverrides(self):
        """
        TableStyleOverrides -> TableStyleOverride()
        
        """
        pass
    
    
    def TextHeight(self):
        """
        TextHeight(Autodesk.AutoCAD.DatabaseServices.RowType) -> double
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input the row type for which the text height is returned
        TextHeight(int, int) -> double
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
        """
        pass
    
    
    def TextRotation(self):
        """
        TextRotation -> Autodesk.AutoCAD.DatabaseServices.RotationAngle
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
        """
        pass
    
    
    def TextString(self):
        """
        TextString(int, int) -> string
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
        TextString(int, int, Autodesk.AutoCAD.DatabaseServices.FormatOption) -> string
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            Autodesk.AutoCAD.DatabaseServices.FormatOption nOption: 
            Input format option
        """
        pass
    
    
    def TextStringConst(self):
        """
        TextStringConst -> string
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
        """
        pass
    
    
    def TextStyle(self):
        """
        TextStyle(Autodesk.AutoCAD.DatabaseServices.RowType) -> ObjectId
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input row type
        TextStyle(int, int) -> ObjectId
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
        """
        pass
    
    
    def UnitType(self):
        """
        UnitType(Autodesk.AutoCAD.DatabaseServices.RowType) -> Autodesk.AutoCAD.DatabaseServices.UnitType
            
            Autodesk.AutoCAD.DatabaseServices.RowType type: 
            Input unit type
        UnitType(int, int) -> Autodesk.AutoCAD.DatabaseServices.UnitType
            
            int row: 
            Input the zero-based row index for the cell
            
            int col: 
            Input the zero-based column index for the cell
        """
        pass
    
    
    def UnmergeCells(self):
        """
        UnmergeCells -> void
            
            CellRange range: 
            Input the cell range
        """
        pass
    
    
    def UpdateDataLink(self):
        """
        UpdateDataLink(int, int, Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Input direction of update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Input options to update
        UpdateDataLink(Autodesk.AutoCAD.DatabaseServices.UpdateDirection, Autodesk.AutoCAD.DatabaseServices.UpdateOption) -> void
            
            Autodesk.AutoCAD.DatabaseServices.UpdateDirection dir: 
            Input direction to update
            
            Autodesk.AutoCAD.DatabaseServices.UpdateOption option: 
            Input options to update
        """
        pass
    
    
    def Value(self):
        """
        Value -> object
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int col: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetGridColor(self):
        """
        GetGridColor -> Autodesk.AutoCAD.Colors.Color
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type
        """
        pass
    
    
    def GetGridDoubleLineSpacing(self):
        """
        GetGridDoubleLineSpacing -> double
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input Autodesk.AutoCAD.DatabaseServices.GridLineType object; grid line type
        """
        pass
    
    
    def GetGridLineStyle(self):
        """
        GetGridLineStyle -> Autodesk.AutoCAD.DatabaseServices.GridLineStyle
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input Autodesk.AutoCAD.DatabaseServices.GridLineType object; grid line type
        """
        pass
    
    
    def GetGridLinetype(self):
        """
        GetGridLinetype -> ObjectId
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input Autodesk.AutoCAD.DatabaseServices.GridLineType object. To specify cell pass a valid row and column indices; to specify row pass a valid row index and pass -1 as column index; to specify column pass a valid column index and pass -1 as row index
        """
        pass
    
    
    def GetGridLineWeight(self):
        """
        GetGridLineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type
        """
        pass
    
    
    def GetGridProperty(self):
        """
        GetGridProperty -> GridPropertyParameter
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input Autodesk.AutoCAD.DatabaseServices.GridLineType object; grid line type
        """
        pass
    
    
    def GetGridVisibility(self):
        """
        GetGridVisibility -> Autodesk.AutoCAD.DatabaseServices.Visibility
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type
        """
        pass
    
    
    def SelectSubRegion(self):
        """
        SelectSubRegion -> CellRange
            
            Point3d cornerPoint1: 
            Input 3D point in WCS specifying the first corner point of the window box selection
            
            Point3d cornerPoint2: 
            Input 3D point in WCS specifying the second corner point of the window box selection
            
            Vector3d selectionViewDirection: 
            Input 3D vector in WCS specifying the view direction of the selection
            
            Vector3d hitTestViewDirection: 
            Input 3D vector in WCS specifying the view orientation of the hit test
            
            Autodesk.AutoCAD.DatabaseServices.SelectType selectionType: 
            Input SelectType enum specifying the selection type
            
            [MarshalAs(UnmanagedType.U1)] bool includeCurrentSelection: 
            Input System.Boolean object indicating whether the selected cells returned will include currently selected cells and newly selected cells or only newly selected cells
            
            [MarshalAs(UnmanagedType.U1)] bool inPickFirst: 
            Input System.Boolean object indicating if the entity is already in the pickfirst set (true) or if the pickfirst logic should attempt to subselect the entity directly (false)
            
            FullSubentityPath[] paths: 
            Output SubentPathArray
        """
        pass
    
    
    def SetContentLayout(self):
        """
        SetContentLayout -> void
            
            int row: 
            Input row index. It should be more than or equal to 0 and less than the number of rows.
            
            int column: 
            Input column index. It should be more than or equal to 0 and less than the number of columns.
            
            Autodesk.AutoCAD.DatabaseServices.CellContentLayout layout: 
            Input layout to set
        """
        pass
    
    
    def SetGridDoubleLineSpacing(self):
        """
        SetGridDoubleLineSpacing -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            double spacing: 
            Input grid double line spacing to set
        """
        pass
    
    
    def SetGridLineStyle(self):
        """
        SetGridLineStyle -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineStyle lineStyle: 
            Input grid line style to set
        """
        pass
    
    
    def SetGridLinetype(self):
        """
        SetGridLinetype -> void
            
            int row: 
            Input row index. This can be -1.
            
            int column: 
            Input column index. This can be -1.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line types. Multiple grid line types can be combined using OR.
            
            lineStyle: 
            Input grid line style to set
        """
        pass
    
    
    def SetTextRotation(self):
        """
        SetTextRotation -> void
            
            int row: 
            Input specifying the zero-based row index for the cell
            
            int col: 
            Input specifying the zero-based column index for the cell
            
            Autodesk.AutoCAD.DatabaseServices.RotationAngle rot: 
            Input specifying the text rotation angle for the cell
            
            Return Values: 
            Description
            Value: 
            Description Description
        """
        pass
    
    
    BreakEnabled = None
    
    
    BreakFlowDirection = None
    
    
    BreakOptions = None
    
    
    Direction = None
    
    
    FlowDirection = None
    
    
    HasSubSelection = None
    
    
    Height = None
    
    
    HorizontalCellMargin = None
    
    
    IsHeaderSuppressed = None
    
    
    IsTitleSuppressed = None
    
    
    MinimumTableHeight = None
    
    
    MinimumTableWidth = None
    
    
    NumColumns = None
    
    
    NumRows = None
    
    
    SubSelection = None
    
    
    TableStyle = None
    
    
    TableStyleName = None
    
    
    VerticalCellMargin = None
    
    
    Width = None
    
    pass

class TableBreakFlowDirection():
    DownOrUp = 2
    Left = 4
    Right = 1

class TableBreakOptions():
    AllowManualHeights = 0x10
    AllowManualPositions = 8
    EnableBreaking = 1
    None = 0
    RepeatBottomLabels = 4
    RepeatTopLabels = 2

class TableCellType():
    UnknownCell = None
    TextCell = None
    BlockCell = None
    MultipleContentCell = None

class TableContent(object):
    """
    
    TableContent()
    """
    def GetCellStyle(self):
        """
        GetCellStyle -> string
            
            int row: 
            Input System.Int32 object; row index. This can be -1.
            
            int column: 
            Input System.Int32 object; column index. This can be -1.
        """
        pass
    
    
    def GetColumnWidth(self):
        """
        GetColumnWidth -> double
            
            int column: 
            Input System.Int32 object; column index. It should be more than or equal to 0 and less than the number of columns.
        """
        pass
    
    
    def GetRowHeight(self):
        """
        GetRowHeight -> double
            
            int row: 
            Input System.Int32 object; row index. It should be more than or equal to 0 and less than the number of rows.
        """
        pass
    
    
    def SetCellStyle(self):
        """
        SetCellStyle -> void
            
            int row: 
            Input System.Int32 object; row index. This can be -1.
            
            int column: 
            Input System.Int32 object; column index. This can be -1.
            
            string cellStyle: 
            Input System.String object; cell style to set. The cell style should exist in the table style set in this table.
        """
        pass
    
    
    def SetColumnWidth(self):
        """
        SetColumnWidth -> void
            
            int column: 
            Input System.Int32 object; column index. It should be more than or equal to 0 and less than the number of columns.
            
            double width: 
            Input System.Double object; column width to set
        """
        pass
    
    
    def SetRowHeight(self):
        """
        SetRowHeight -> void
            
            int row: 
            Input System.Int32 object.
            
            double height: 
            Input System.Double object.
        """
        pass
    
    
    TableStyleId = None
    
    pass

class TableCopyOptions():
    ConvertFormatToOverrides = 0x800
    ExpandOrContractTable = 1
    FillTarget = 0x20000
    None = 0
    OnlyContentModifiedAfterUpdate = 0x400000
    OnlyFormatModifiedAfterUpdate = 0x800000
    OverwriteContentModifiedAfterUpdate = 0x100000
    OverwriteFormatModifiedAfterUpdate = 0x200000
    OverwriteReadOnlyContent = 0x40000
    OverwriteReadOnlyFormat = 0x80000
    SkipBlock = 0x20
    SkipCellState = 0x1000
    SkipCellStyle = 0x400
    SkipContent = 2
    SkipContentFormat = 0x2000
    SkipDataCell = 0x100
    SkipDataLink = 0x40
    SkipDissimilarContentFormat = 0x4000
    SkipField = 8
    SkipFormat = 0x200
    SkipFormula = 0x10
    SkipGeometry = 0x8000
    SkipLabelCell = 0x80
    SkipMerges = 0x10000
    SkipValue = 4
    TableCopyColumnWidth = 0x2000000
    TableCopyRowHeight = 0x1000000

class TableEnumerator(object):
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

class Table():
    IterateColumns = 4
    IterateRows = 2
    IterateSelection = 1
    None = 0
    SkipMerged = 0x40
    SkipReadOnlyContent = 0x10
    SkipReadOnlyFormat = 0x20

class TableFillOptions():
    CopyContent = 8
    CopyFormat = 0x10
    GenerateSeries = 4
    None = 0
    OverwriteReadOnlyContent = 0x20
    OverwriteReadOnlyFormat = 0x40
    Reverse = 2
    Row = 1

class TableHitTestInfo(object):
    """
    
    """
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input culture format
        """
        pass
    
    
    Column = None
    
    
    Row = None
    
    
    Type = None
    
    pass

class TableHitTestType():
    Cell = None

class TableStyle(object):
    """
    
    TableStyle()
    """
    def CellClass(self):
        """
        CellClass -> Autodesk.AutoCAD.DatabaseServices.CellClass
            
            string styleName: 
            Input cell style name
        """
        pass
    
    
    def GridDoubleLineSpacing(self):
        """
        GridDoubleLineSpacing -> double
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type.
            
            string styleName: 
            Input cell style name.
        """
        pass
    
    
    def GridLineStyle(self):
        """
        GridLineStyle -> Autodesk.AutoCAD.DatabaseServices.GridLineStyle
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type.
            
            string styleName: 
            Input cell style name.
        """
        pass
    
    
    def GridLinetype(self):
        """
        GridLinetype -> ObjectId
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input grid line type.
            
            string styleName: 
            Input cell style name.
        """
        pass
    
    
    def Margin(self):
        """
        Margin -> double
        
        """
        pass
    
    
    def Alignment(self):
        """
        Alignment -> Autodesk.AutoCAD.DatabaseServices.CellAlignment
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which the cell alignment value will be returned
        """
        pass
    
    
    def PostTableStyleToDatabase(self):
        """
        PostTableStyleToDatabase -> ObjectId
            
            Database databasePointer: 
            Input the database to which to add the table style
            
            string styleName: 
            Input name for the table style; must be a non-empty string that is less than 256 characters long and conforms to the requirements for Dictionary key strings
        """
        pass
    
    
    def SetBackgroundColor(self):
        """
        SetBackgroundColor -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input value indicating the new background color
            
            int rowTypes: 
            Input row types for which to set the background color
        """
        pass
    
    
    def SetBackgroundColorNone(self):
        """
        SetBackgroundColorNone -> void
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input Boolean indicating whether to enable the background color for the specified row type
            
            int rowTypes: 
            Input row types for which to enable or disable the background color
        """
        pass
    
    
    def SetCellClass(self):
        """
        SetCellClass -> void
            
            Autodesk.AutoCAD.DatabaseServices.CellClass cellClass: 
            Input new cell class value
            
            string styleName: 
            Input cell style name
        """
        pass
    
    
    def BackgroundColor(self):
        """
        BackgroundColor -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which the Color value will be returned
        """
        pass
    
    
    def SetColor(self):
        """
        SetColor -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color
            
            int rowTypes: 
            Input row types for which to set the color
        """
        pass
    
    
    def SetGridColor(self):
        """
        SetGridColor -> void
            
            Autodesk.AutoCAD.Colors.Color color: 
            Input color value
            
            int gridLineTypes: 
            Input types of grid lines for which to set the color
            
            int rowTypes: 
            Input row types for which to set the color
        """
        pass
    
    
    def SetGridDoubleLineSpacing(self):
        """
        SetGridDoubleLineSpacing -> void
            
            double spacing: 
            Input grid double line spacing to set.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineTypes: 
            Input grid line type. Multiple grid line types can be combined using OR.
            
            string styleName: 
            Input cell style name.
        """
        pass
    
    
    def SetGridLineStyle(self):
        """
        SetGridLineStyle -> void
            
            Autodesk.AutoCAD.DatabaseServices.GridLineStyle lineStyle: 
            Input grid line style to set.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineTypes: 
            Input grid line styles. Multiple grid line types can be combined using OR.
            
            string styleName: 
            Input cell style name.
        """
        pass
    
    
    def SetGridLinetype(self):
        """
        SetGridLinetype -> void
            
            ObjectId linetype: 
            Input grid double line spacing to set.
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineTypes: 
            Input grid line type. Multiple grid line types can be combined using OR.
            
            string styleName: 
            Input cell style name.
        """
        pass
    
    
    def Color(self):
        """
        Color -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which the Color value will be returned
        """
        pass
    
    
    def SetGridVisibility(self):
        """
        SetGridVisibility -> void
            
            [MarshalAs(UnmanagedType.U1)] bool visible: 
            Input visibility value
            
            int gridLineTypes: 
            Input grid line types for which to set the visibility
            
            int rowTypes: 
            Input row types for which to set the visibility
        """
        pass
    
    
    def SetMargin(self):
        """
        SetMargin -> void
        
        """
        pass
    
    
    def SetTextHeight(self):
        """
        SetTextHeight -> void
            
            double height: 
            Input value indicating the new text height
            
            int rowTypes: 
            Input row types for which to set the text height
        """
        pass
    
    
    def SetTextStyle(self):
        """
        SetTextStyle(ObjectId, int) -> void
            
            ObjectId id: 
            Input TextStyleTableRecord object ID
            
            int rowTypes: 
            Input row types
        SetTextStyle(ObjectId, string) -> void
            
            ObjectId id: 
            Input TextStyleTableRecord object ID
            
            string styleName: 
            Input cell style name
        """
        pass
    
    
    def DataType(self):
        """
        DataType -> Autodesk.AutoCAD.DatabaseServices.DataType
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which the DataType value will be returned
        """
        pass
    
    
    def TextStyle(self):
        """
        TextStyle(string) -> ObjectId
            
            string styleName: 
            Input cell style
        TextStyle(Autodesk.AutoCAD.DatabaseServices.RowType) -> ObjectId
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input row type
        """
        pass
    
    
    def Format(self):
        """
        Format -> string
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which the string format value will be returned
        """
        pass
    
    
    def GridColor(self):
        """
        GridColor -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input type of grid line for which to return the Color value
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input row type for which to return the color value
        """
        pass
    
    
    def GridLineWeight(self):
        """
        GridLineWeight -> Autodesk.AutoCAD.DatabaseServices.LineWeight
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input type of grid line for which to return the LineWeight value
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input row type for which to return the grid line weight value
        """
        pass
    
    
    def GridVisibility(self):
        """
        GridVisibility -> bool
            
            Autodesk.AutoCAD.DatabaseServices.GridLineType gridLineType: 
            Input type of grid line for which to return the grid visibility value
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input row type for which to return the grid visibility value
        """
        pass
    
    
    def IsBackgroundColorNone(self):
        """
        IsBackgroundColorNone -> bool
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which to return the Boolean indicating whether the background color is set to none
        """
        pass
    
    
    def SetAlignment(self):
        """
        SetAlignment -> void
            
            Autodesk.AutoCAD.DatabaseServices.CellAlignment alignment: 
            Input alignment value
            
            int rowTypes: 
            Input row types for which to set the alignment
        """
        pass
    
    
    def SetDataType(self):
        """
        SetDataType -> void
            
            Autodesk.AutoCAD.DatabaseServices.DataType nDataType: 
            Input data type to set
            
            Autodesk.AutoCAD.DatabaseServices.UnitType nUnitType: 
            Input unit type to set
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowTypes: 
            Input row types for which to set the data type
        """
        pass
    
    
    def SetFormat(self):
        """
        SetFormat -> void
            
            string pFormat: 
            Input format to set
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowTypes: 
            Input row types for which to set the format string
        """
        pass
    
    
    def SetGridLineWeight(self):
        """
        SetGridLineWeight -> void
            
            Autodesk.AutoCAD.DatabaseServices.LineWeight lineWeight: 
            Input lineweight value
            
            int gridLineTypes: 
            Input grid line types for which to set the lineweight
            
            int rowTypes: 
            Input row types for which to set the lineweight
        """
        pass
    
    
    def TextHeight(self):
        """
        TextHeight -> double
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input value specifying the row type for which the text height will be returned
        """
        pass
    
    
    def UnitType(self):
        """
        UnitType -> Autodesk.AutoCAD.DatabaseServices.UnitType
            
            Autodesk.AutoCAD.DatabaseServices.RowType rowType: 
            Input row type
        """
        pass
    
    
    BitFlags = None
    
    
    CellStyles = None
    
    
    Description = None
    
    
    FlowDirection = None
    
    
    HorizontalCellMargin = None
    
    
    IsHeaderSuppressed = None
    
    
    IsTitleSuppressed = None
    
    
    Name = None
    
    
    Template = None
    
    
    VerticalCellMargin = None
    
    pass

class TableStyleFlags():
    HorizontalInsideLineFirst = 1
    HorizontalInsideLineSecond = 2
    HorizontalInsideLineThird = 4
    TableStyleModified = 8

class TableStyleOverride():
    CellAlignment = 130
    CellBackgroundColor = 0x84
    CellBackgroundFillNone = 0x83
    CellBottomGridColor = 0x8a
    CellBottomGridLineWeight = 0x8e
    CellBottomVisibility = 0x92
    CellContentColor = 0x85
    CellDataType = 0x94
    CellLeftGridColor = 0x8b
    CellLeftGridLineWeight = 0x8f
    CellLeftVisibility = 0x93
    CellRightGridColor = 0x89
    CellRightGridLineWeight = 0x8d
    CellRightVisibility = 0x91
    CellTextHeight = 0x87
    CellTextStyle = 0x86
    CellTopGridColor = 0x88
    CellTopGridLineWeight = 140
    CellTopVisibility = 0x90
    DataHorizontalBottomColor = 0x36
    DataHorizontalBottomLineWeight = 0x54
    DataHorizontalBottomVisibility = 0x72
    DataHorizontalInsideColor = 0x35
    DataHorizontalInsideLineWeight = 0x53
    DataHorizontalInsideVisibility = 0x71
    DataHorizontalTopColor = 0x34
    DataHorizontalTopLineWeight = 0x52
    DataHorizontalTopVisibility = 0x70
    DataRowAlignment = 0x11
    DataRowColor = 8
    DataRowDataType = 0x1a
    DataRowFillColor = 14
    DataRowFillNone = 11
    DataRowTextHeight = 0x17
    DataRowTextStyle = 20
    DataVerticalInsideColor = 0x38
    DataVerticalInsideLineWeight = 0x56
    DataVerticalInsideVisibility = 0x74
    DataVerticalLeftColor = 0x37
    DataVerticalLeftLineWeight = 0x55
    DataVerticalLeftVisibility = 0x73
    DataVerticalRightColor = 0x39
    DataVerticalRightLineWeight = 0x57
    DataVerticalRightVisibility = 0x75
    FlowDirection = 3
    HeaderHorizontalBottomColor = 0x30
    HeaderHorizontalBottomLineWeight = 0x4e
    HeaderHorizontalBottomVisibility = 0x6c
    HeaderHorizontalInsideColor = 0x2f
    HeaderHorizontalInsideLineWeight = 0x4d
    HeaderHorizontalInsideVisibility = 0x6b
    HeaderHorizontalTopColor = 0x2e
    HeaderHorizontalTopLineWeight = 0x4c
    HeaderHorizontalTopVisibility = 0x6a
    HeaderRowAlignment = 0x10
    HeaderRowColor = 7
    HeaderRowDataType = 0x19
    HeaderRowFillColor = 13
    HeaderRowFillNone = 10
    HeaderRowTextHeight = 0x16
    HeaderRowTextStyle = 0x13
    HeaderSuppressed = 2
    HeaderVerticalInsideColor = 50
    HeaderVerticalInsideLineWeight = 80
    HeaderVerticalInsideVisibility = 110
    HeaderVerticalLeftColor = 0x31
    HeaderVerticalLeftLineWeight = 0x4f
    HeaderVerticalLeftVisibility = 0x6d
    HeaderVerticalRightColor = 0x33
    HeaderVerticalRightLineWeight = 0x51
    HeaderVerticalRightVisibility = 0x6f
    HorizontalCellMargin = 4
    TitleHorizontalBottomColor = 0x2a
    TitleHorizontalBottomLineWeight = 0x48
    TitleHorizontalBottomVisibility = 0x66
    TitleHorizontalInsideColor = 0x29
    TitleHorizontalInsideLineWeight = 0x47
    TitleHorizontalInsideVisibility = 0x65
    TitleHorizontalTopColor = 40
    TitleHorizontalTopLineWeight = 70
    TitleHorizontalTopVisibility = 100
    TitleRowAlignment = 15
    TitleRowColor = 6
    TitleRowDataType = 0x18
    TitleRowFillColor = 12
    TitleRowFillNone = 9
    TitleRowTextHeight = 0x15
    TitleRowTextStyle = 0x12
    TitleSuppressed = 1
    TitleVerticalInsideColor = 0x2c
    TitleVerticalInsideLineWeight = 0x4a
    TitleVerticalInsideVisibility = 0x68
    TitleVerticalLeftColor = 0x2b
    TitleVerticalLeftLineWeight = 0x49
    TitleVerticalLeftVisibility = 0x67
    TitleVerticalRightColor = 0x2d
    TitleVerticalRightLineWeight = 0x4b
    TitleVerticalRightVisibility = 0x69
    VerticalCellMargin = 5

class TableTemplate(object):
    """
    
    TableTemplate
        Table table : Input table from which to capture the template.
        TableCopyOptions copyOption : Input copy option specifying what to capture while capturing the template.
    """
    def Capture(self):
        """
        Capture -> void
            
            Table table: 
            Input table from which to capture the template.
            
            TableCopyOptions copyOption: 
            Input what to capture while capturing the template.
        """
        pass
    
    
    def CreateTable(self):
        """
        CreateTable -> Table
            
            TableCopyOptions copyOption: 
            Input Autodesk.AutoCAD.DatabaseServices.TableCopyOptions object specifying what to capture while capturing the template.
        """
        pass
    
    pass

class TangentConstraint(object):
    """
    
    TangentConstraint()
    """

    pass

class TextAlignment():
    LeftAlignment = None
    CenterAlignment = None
    RightAlignment = None

class TextAlignmentType():
    LeftAlignment = None
    CenterAlignment = None
    RightAlignment = None

class TextAngleType():
    InsertAngle = None
    HorizontalAngle = None
    AlwaysRightReadingAngle = None

class TextAttachmentDirection():
    AttachmentHorizontal = None
    AttachmentVertical = None

class TextAttachmentType():
    AttachmentTopOfTop = None
    AttachmentMiddleOfTop = None
    AttachmentMiddle = None
    AttachmentMiddleOfBottom = None
    AttachmentBottomOfBottom = None
    AttachmentBottomLine = None
    AttachmentBottomOfTopLine = None
    AttachmentBottomOfTop = None
    AttachmentAllLine = None
    AttachmentCenter = None
    AttachmentLinedCenter = None

class TextEditor(object):
    """
    
    """
    class ExitStatus():
        ExitQuit = None
        ExitSave = None
    
    
    class TextFindFlags():
        HalfFullForm = 4
        IgnoreAccent = 8
        MatchCase = 1
        UseWildcards = 0x10
        WholeWord = 2
    
    
    def ClearSelection(self):
        """
        ClearSelection -> void
        
        """
        pass
    
    
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def CreateTextEditor(self):
        """
        CreateTextEditor -> TextEditor
        
        """
        pass
    
    
    def FindTextW(self):
        """
        FindTextW -> void
        
        """
        pass
    
    
    def GetFont(self):
        """
        GetFont -> Font
        
        """
        pass
    
    
    def MakeSelection(self):
        """
        MakeSelection -> void
        
        """
        pass
    
    
    def Redraw(self):
        """
        Redraw -> void
        
        """
        pass
    
    
    def SelectAll(self):
        """
        SelectAll -> void
        
        """
        pass
    
    
    ActualHeight = None
    
    
    ActualWidth = None
    
    
    Attachment = None
    
    
    AutoCAPS = None
    
    
    AutoListEnabled = None
    
    
    Columns = None
    
    
    Cursor = None
    
    
    DefaultStackAlignment = None
    
    
    DefaultStackScale = None
    
    
    DefinedHeight = None
    
    
    DefinedWidth = None
    
    
    EndOfText = None
    
    
    FontCount = None
    
    
    IsAnnotativeStyle = None
    
    
    NumberingEnabled = None
    
    
    Paragraphs = None
    
    
    Selection = None
    
    
    StackCount = None
    
    
    StartOfText = None
    
    
    Style = None
    
    
    StyleCount = None
    
    
    TabOnlyDelimiter = None
    
    
    TextHeight = None
    
    
    VerticalSHX = None
    
    
    VerticalTTF = None
    
    
    Wipeout = None
    
    pass

class TextEditorColumn(object):
    """
    
    """
    EndOfText = None
    
    
    Height = None
    
    
    StartOfText = None
    
    pass

class TextEditorColumns(object):
    """
    
    """
    AutoHeight = None
    
    
    Count = None
    
    
    Gutter = None
    
    
    IsFlowReversed = None
    
    
    MaxCount = None
    
    
    TotalWidth = None
    
    
    Type = None
    
    
    Width = None
    
    pass

class TextEditorCursor(object):
    """
    
    """
    Column = None
    
    
    Location = None
    
    
    Paragraph = None
    
    pass

class TextEditorLocation(object):
    """
    
    """

    pass

class TextEditorParagraph(object):
    """
    
    """
    class AlignmentType():
        AlignmentDefault = None
        AlignmentLeft = None
        AlignmentCenter = None
        AlignmentRight = None
        AlignmentJustify = None
        AlignmentDistribute = None
    
    
    class LineSpacingStyle():
        LineSpacingDefault = None
        LineSpacingExactly = None
        LineSpacingAtLeast = None
        LineSpacingMultiple = None
    
    
    class NumberingType():
        Off = None
        Bullet = None
        Number = None
        LetterLower = None
        LetterUpper = None
        NumberWide = None
        LetterLowerWide = None
        LetterUpperWide = None
    
    
    def AddTab(self):
        """
        AddTab -> void
        
        """
        pass
    
    
    def ContinueNumbering(self):
        """
        ContinueNumbering -> void
        
        """
        pass
    
    
    def GetTab(self):
        """
        GetTab -> TextEditorParagraphTab
        
        """
        pass
    
    
    def RemoveTab(self):
        """
        RemoveTab -> void
        
        """
        pass
    
    
    def RestartNumbering(self):
        """
        RestartNumbering -> void
        
        """
        pass
    
    
    Alignment = None
    
    
    EndOfText = None
    
    
    FirstIndent = None
    
    
    LeftIndent = None
    
    
    LineSpaceFactor = None
    
    
    LineSpaceStyle = None
    
    
    MaxLineSpacingFactor = None
    
    
    MaxSpacingValue = None
    
    
    MinLineSpacingFactor = None
    
    
    MinSpacingValue = None
    
    
    ParaNumberingType = None
    
    
    RightIndent = None
    
    
    SpaceAfter = None
    
    
    SpaceBefore = None
    
    
    StartOfText = None
    
    
    TabsCount = None
    
    pass

class TextEditorParagraphTab(object):
    """
    
    """
    class ParagraphTabType():
        LeftTab = None
        CenterTab = None
        RightTab = None
        DecimalTab = None
    
    
    DecimalChar = None
    
    
    Offset = None
    
    
    Type = None
    
    pass

class TextEditorSelection(object):
    """
    
    """
    def CanSupportFont(self):
        """
        CanSupportFont -> bool
        
        """
        pass
    
    
    def CanSupportLanguage(self):
        """
        CanSupportLanguage -> bool
        
        """
        pass
    
    
    def ChangeToLowercase(self):
        """
        ChangeToLowercase -> bool
        
        """
        pass
    
    
    def ChangeToUppercase(self):
        """
        ChangeToUppercase -> bool
        
        """
        pass
    
    
    def CombineParagraphs(self):
        """
        CombineParagraphs -> void
        
        """
        pass
    
    
    def ConvertToPlainText(self):
        """
        ConvertToPlainText -> void
        
        """
        pass
    
    
    def RemoveAllFormatting(self):
        """
        RemoveAllFormatting -> void
        
        """
        pass
    
    
    def RemoveCharacterFormatting(self):
        """
        RemoveCharacterFormatting -> void
        
        """
        pass
    
    
    def RemoveParagraphFormatting(self):
        """
        RemoveParagraphFormatting -> void
        
        """
        pass
    
    
    def Stack(self):
        """
        Stack -> void
        
        """
        pass
    
    
    def UnStack(self):
        """
        UnStack -> void
        
        """
        pass
    
    
    def UpdateField(self):
        """
        UpdateField -> void
        
        """
        pass
    
    
    CanChangeCase = None
    
    
    CanStack = None
    
    
    CanUnStack = None
    
    
    FieldObject = None
    
    
    Paragraphs = None
    
    
    SelectionString = None
    
    
    SingleFieldSelected = None
    
    
    SingleStackSelected = None
    
    
    StackSettings = None
    
    pass

class TextEditorSelectionbase(object):
    """
    
    """
    class FlowAlign():
        FlowBase = None
        FlowCenter = None
        FlowTop = None
    
    
    class InsertTextType():
        UnicodeMTextFormat = None
        MTextFormat = None
        RichTextFormat = None
        UnicodeDTextFormat = None
        DTextFormat = None
        UnicodeTextFormat = None
        MultibyteTextFormat = None
    
    
    def InputSpecialChar(self):
        """
        InputSpecialChar -> void
        
        """
        pass
    
    
    def InsertColumnBreak(self):
        """
        InsertColumnBreak -> void
        
        """
        pass
    
    
    def InsertImportedText(self):
        """
        InsertImportedText -> void
        
        """
        pass
    
    
    def InsertString(self):
        """
        InsertString -> void
        
        """
        pass
    
    
    def InsertSymbol(self):
        """
        InsertSymbol -> void
        
        """
        pass
    
    
    Bold = None
    
    
    Color = None
    
    
    FlowAlignment = None
    
    
    Font = None
    
    
    Height = None
    
    
    Italic = None
    
    
    Language = None
    
    
    MaxObliqueAngle = None
    
    
    MaxTrackingFactor = None
    
    
    MaxWidthScale = None
    
    
    MinObliqueAngle = None
    
    
    MinTrackingFactor = None
    
    
    MinWidthScale = None
    
    
    ObliqueAngle = None
    
    
    Overline = None
    
    
    Strikethrough = None
    
    
    TrackingFactor = None
    
    
    Underline = None
    
    
    WidthScale = None
    
    pass

class TextEditorStack(object):
    """
    
    """
    class StackType():
        HorizontalStack = None
        DiagonalStack = None
        ToleranceStack = None
        DecimalStack = None
    
    
    Bottom = None
    
    
    DecimalChar = None
    
    
    FlowAlign = None
    
    
    MaxStackScale = None
    
    
    MinStackScale = None
    
    
    Scale = None
    
    
    Top = None
    
    
    Type = None
    
    pass

class TextEditorWipeout(object):
    """
    
    """
    BackgroundFillColor = None
    
    
    BackgroundFillEnabled = None
    
    
    BackgroundScaleFactor = None
    
    
    MaxBackgroundScaleFactor = None
    
    
    MinBackgroundScaleFactor = None
    
    
    UseBackgroundColor = None
    
    pass

class TextHorizontalMode():
    TextLeft = None
    TextCenter = None
    TextRight = None
    TextAlign = None
    TextMid = None
    TextFit = None

class TextStyleTable(object):
    """
    
    """

    pass

class TextStyleTableRecord(object):
    """
    
    TextStyleTableRecord()
    """
    BigFontFileName = None
    
    
    FileName = None
    
    
    FlagBits = None
    
    
    Font = None
    
    
    IsShapeFile = None
    
    
    IsVertical = None
    
    
    ObliquingAngle = None
    
    
    PriorSize = None
    
    
    TextSize = None
    
    
    XScale = None
    
    pass

class TextVerticalMode():
    TextBase = None
    TextBottom = None
    TextVerticalMid = None
    TextTop = None

class ThreePointAngleConstraint(object):
    """
    
    ThreePointAngleConstraint()()
    
    
    ThreePointAngleConstraint(AngularConstraint.AngularSectorType)
        AngularConstraint.AngularSectorType type : Input SectorType indicating the angle sector which is used to measure the angle.
    
    
    """

    pass

class Transaction(object):
    """
    
    """
    def Abort(self):
        """
        Abort -> void
        
        """
        pass
    
    
    def AddNewlyCreatedDBObject(self):
        """
        AddNewlyCreatedDBObject -> void
            
            DBObject obj: 
            Input object to be added or removed
            
            [MarshalAs(UnmanagedType.U1)] bool add: 
            Input Boolean indicating whether to add or remove the object
        """
        pass
    
    
    def Commit(self):
        """
        Commit -> void
        
        """
        pass
    
    
    def GetAllObjects(self):
        """
        GetAllObjects -> DBObjectCollection
        
        """
        pass
    
    
    def GetObject(self):
        """
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
            
            [MarshalAs(UnmanagedType.U1)] bool forceOpenOnLockedLayer: 
            Input true if locked layers should be opened
        """
        pass
    
    
    NumberOfOpenedObjects = None
    
    
    TransactionManager = None
    
    pass

class TransactionManager(object):
    """
    
    """
    def AddNewlyCreatedDBObject(self):
        """
        AddNewlyCreatedDBObject -> void
            
            DBObject obj: 
            Input object to be added or removed
            
            [MarshalAs(UnmanagedType.U1)] bool add: 
            Input Boolean indicating whether to add or remove the object
        """
        pass
    
    
    def GetAllObjects(self):
        """
        GetAllObjects -> DBObjectCollection
        
        """
        pass
    
    
    def GetObject(self):
        """
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
        GetObject(ObjectId, Autodesk.AutoCAD.DatabaseServices.OpenMode, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool) -> DBObject
            
            ObjectId id: 
            Input objectId of object to obtain
            
            Autodesk.AutoCAD.DatabaseServices.OpenMode mode: 
            Input mode to obtain in
            
            [MarshalAs(UnmanagedType.U1)] bool openErased: 
            Input Boolean indicating whether to obtain erased objects
            
            [MarshalAs(UnmanagedType.U1)] bool forceOpenOnLockedLayer: 
            Input true if locked layers should be opened
        """
        pass
    
    
    def QueueForGraphicsFlush(self):
        """
        QueueForGraphicsFlush -> void
        
        """
        pass
    
    
    def StartOpenCloseTransaction(self):
        """
        StartOpenCloseTransaction -> OpenCloseTransaction
        
        """
        pass
    
    
    def StartTransaction(self):
        """
        StartTransaction -> Transaction
        
        """
        pass
    
    
    NumberOfActiveTransactions = None
    
    
    NumberOfOpenedObjects = None
    
    
    TopTransaction = None
    
    pass

class TransformOverrule(object):
    """
    
    """
    def CloneMeForDragging(self):
        """
        CloneMeForDragging -> bool
        
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> void
        
        """
        pass
    
    
    def GetTransformedCopy(self):
        """
        GetTransformedCopy -> Entity
        
        """
        pass
    
    
    def HideMeForDragging(self):
        """
        HideMeForDragging -> bool
        
        """
        pass
    
    
    def SetCustomFilter(self):
        """
        SetCustomFilter -> void
        
        """
        pass
    
    
    def SetExtensionDictionaryEntryFilter(self):
        """
        SetExtensionDictionaryEntryFilter -> void
            
            string entryName: 
            Input the name of the entry.
        """
        pass
    
    
    def SetIdFilter(self):
        """
        SetIdFilter -> void
            
            ObjectId[] ids: 
            Input an array of ObjectId.
        """
        pass
    
    
    def SetNoFilter(self):
        """
        SetNoFilter -> void
        
        """
        pass
    
    
    def SetXDataFilter(self):
        """
        SetXDataFilter -> void
            
            string registeredApplicationName: 
            Input the name of the registered application.
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
        
        """
        pass
    
    pass

class TypedValue(object):
    """
    
    TypedValue(int)
        int typeCode : Input the type code.
    
    
    TypedValue(int, object)
        int typeCode : Input the type code.
        object value : Input the value.
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare with.
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input.
        """
        pass
    
    
    TypeCode = None
    
    
    Value = None
    
    pass

class UcsTable(object):
    """
    
    """

    pass

class UcsTableRecord(object):
    """
    
    UcsTableRecord()
    """
    def GetUcsBaseOrigin(self):
        """
        GetUcsBaseOrigin -> Point3d
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input orthographic view
        """
        pass
    
    
    def SetUcsBaseOrigin(self):
        """
        SetUcsBaseOrigin -> void
            
            Point3d origin: 
            Input origin point
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input orthographic view
        """
        pass
    
    
    Origin = None
    
    
    XAxis = None
    
    
    YAxis = None
    
    pass

class UnderlayDefinition(object):
    """
    
    """
    def Load(self):
        """
        Load -> void
            
            string password: 
            Input optional password
        """
        pass
    
    
    def SetUnderlayItem(self):
        """
        SetUnderlayItem -> void
            
            string sourceFileName: 
            Input source file path
            
            string activeFileName: 
            Input current or active file path
            
            Autodesk.AutoCAD.DatabaseServices.UnderlayItem item: 
            Input item to be referenced
        """
        pass
    
    
    def Unload(self):
        """
        Unload -> void
        
        """
        pass
    
    
    def GetDictionaryKey(self):
        """
        GetDictionaryKey -> string
            
            System.Type underlayDefinitionType: 
            Input the class descriptor of the underlay type for which to retrieve the dictionary name
        """
        pass
    
    
    ActiveFileName = None
    
    
    ItemName = None
    
    
    Loaded = None
    
    
    SourceFileName = None
    
    
    UnderlayItem = None
    
    pass

class UnderlayFile(object):
    """
    
    """
    Items = None
    
    pass

class UnderlayHost(object):
    """
    
    """
    def GetFile(self):
        """
        GetFile -> UnderlayFile
            
            string path: 
            Input fully qualified path to the file to open
            
            string password: 
            Input optional password
        """
        pass
    
    
    DgnDocHost = None
    
    
    DgnHost = None
    
    
    DwfHost = None
    
    
    PdfHost = None
    
    pass

class UnderlayItem(object):
    """
    
    """
    Extents = None
    
    
    Name = None
    
    
    Thumbnail = None
    
    
    Units = None
    
    
    UsingPartialContent = None
    
    pass

class UnderlayItemCollection(object):
    """
    
    """
    def CopyTo(self):
        """
        CopyTo -> void
            
            UnderlayItem[] array: 
            Input array to copy to
            
            int index: 
            Input index to begin copying from
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class UnderlayLayer(object):
    """
    
    UnderlayLayer()
    """
    Name = None
    
    
    State = None
    
    pass

class UnderlayLayerCollection(object):
    """
    
    """
    def CopyTo(self):
        """
        CopyTo -> void
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    Count = None
    
    pass

class UnderlayLayerState():
    Off = None
    On = None

class UnderlayReference(object):
    """
    
    """
    def GenerateClipBoundaryFromPline(self):
        """
        GenerateClipBoundaryFromPline -> void
        
        """
        pass
    
    
    def GetClipBoundary(self):
        """
        GetClipBoundary -> Point2d()
        
        """
        pass
    
    
    def SetClipBoundary(self):
        """
        SetClipBoundary -> void
            
            Point2d[] points: 
            Input the clip boundary. An array describing a self intersecting polyline is not allowed. An array of two points is allowed and is treated as the minimum, maximum point of a rectangle.
        """
        pass
    
    
    AdjustColorForBackground = None
    
    
    Contrast = None
    
    
    ContrastLowerLimit = None
    
    
    ContrastUpperLimit = None
    
    
    DefaultContrast = None
    
    
    DefaultFade = None
    
    
    DefinitionId = None
    
    
    Fade = None
    
    
    FadeLowerLimit = None
    
    
    FadeUpperLimit = None
    
    
    Height = None
    
    
    IsClipInverted = None
    
    
    IsClipped = None
    
    
    IsOn = None
    
    
    Monochrome = None
    
    
    Name = None
    
    
    NameOfSheet = None
    
    
    Normal = None
    
    
    Path = None
    
    
    Position = None
    
    
    Rotation = None
    
    
    ScaleFactors = None
    
    
    Transform = None
    
    
    UnderlayLayerCollection = None
    
    
    Width = None
    
    pass

class Unit():
    Millimeter = None
    Centimeter = None
    Meter = None
    Kilometer = None
    Inch = None
    Foot = None
    Yard = None
    Mile = None
    Microinches = None
    Mils = None
    Angstroms = None
    Nanometers = None
    Microns = None
    Decimeters = None
    Dekameters = None
    Hectometers = None
    GigaMeters = None
    Astronomical = None
    LightYears = None
    Parsecs = None

class UnitType():
    Angle = 2
    AngleNotTransformed = 0x10000
    Area = 4
    Currency = 0x10
    Distance = 1
    Percentage = 0x20
    Unitless = 0
    Volume = 8

class UnitsConverter(object):
    """
    
    """
    def ConvertFrom(self):
        """
        ConvertFrom -> object
            
            ITypeDescriptorContext context: 
            Input context to convert within
            
            CultureInfo culture: 
            Input culture to convert within
            
            object value: 
            Input object to convert from
        """
        pass
    
    
    def CanConvertFrom(self):
        """
        CanConvertFrom -> bool
            
            ITypeDescriptorContext context: 
            Input context to convert with
            
            Type sourceType: 
            Input source type
        """
        pass
    
    
    def ConvertTo(self):
        """
        ConvertTo -> object
            
            ITypeDescriptorContext context: 
            Input System.ComponentModel.ITypeDescriptorContext object.
            
            CultureInfo culture: 
            Input System.Globalization.CultureInfo object.
            
            object value: 
            Input.
            
            Type destinationType: 
            Input.
        """
        pass
    
    
    def GetConversionFactor(self):
        """
        GetConversionFactor -> double
            
            UnitsValue from: 
            Input Autodesk.AutoCAD.DatabaseServices.UnitsValue object to be converted.
            
            UnitsValue to: 
            Input Autodesk.AutoCAD.DatabaseServices.UnitsValue object converted to
        """
        pass
    
    pass

class UnitsValue():
    Undefined = None
    Inches = None
    Feet = None
    Miles = None
    Millimeters = None
    Centimeters = None
    Meters = None
    Kilometers = None
    MicroInches = None
    Mils = None
    Yards = None
    Angstroms = None
    Nanometers = None
    Microns = None
    Decimeters = None
    Dekameters = None
    Hectometers = None
    Gigameters = None
    Astronomical = None
    LightYears = None
    Parsecs = None
    USSurveyFeet = None
    USSurveyInch = None
    USSurveyYard = None
    USSurveyMile = None

class UnmanagedPointCloudColorSchemeCollectionReactor(object):
    """
    
    """

    pass

class UpdateDirection():
    DataToSource = 2
    SourceToData = 1

class UpdateOption():
    AllowSourceUpdate = 0x100000
    ForceFullSourceUpdate = 0x200000
    ForPreview = 0x1000000
    IncludeXrefs = 0x2000000
    None = 0
    OverwriteContentModifiedAfterUpdate = 0x400000
    OverwriteFormatModifiedAfterUpdate = 0x800000
    SkipFormat = 0x20000
    UpdateColumnWidth = 0x80000
    UpdateRowHeight = 0x40000

class Vertex(object):
    """
    
    """

    pass

class Vertex2d(object):
    """
    
    Vertex2d()()
    
    
    Vertex2d(Point3d, double, double, double, double)
        Point3d position : Input Autodesk.AutoCAD.Geometry.Point3d object.
        double bulge : Input System.Double object.
        double startWidth : Input System.Double object.
        double endWidth : Input System.Double object.
        double tangent : Input System.Double object.
    
    
    """
    Bulge = None
    
    
    EndWidth = None
    
    
    Position = None
    
    
    StartWidth = None
    
    
    Tangent = None
    
    
    TangentUsed = None
    
    
    VertexType = None
    
    pass

class Vertex2dType():
    SimpleVertex = None
    SplineControlVertex = None
    SplineFitVertex = None
    CurveFitVertex = None

class Vertex3dType():
    SimpleVertex = None
    ControlVertex = None
    FitVertex = None

class VertexRef(object):
    """
    
    VertexRef()()
    
    
    VertexRef(CompoundObjectId)()
    
    
    VertexRef(CompoundObjectId, SubentityId)()
    
    
    VertexRef(CompoundObjectId, SubentityId, Point3d)()
    
    
    VertexRef(Entity)()
    
    
    VertexRef(FullSubentityPath)()
    
    
    VertexRef(Point3d)()
    
    
    """
    Point = None
    
    pass

class VerticalConstraint(object):
    """
    
    VerticalConstraint()
    """

    pass

class ViewBorder(object):
    """
    
    ViewBorder()
    """
    def GetSourceType(self):
        """
        GetSourceType -> Autodesk.AutoCAD.DatabaseServices.SourceType
        
        """
        pass
    
    
    def GetViewStyleType(self):
        """
        GetViewStyleType -> Autodesk.AutoCAD.DatabaseServices.ViewStyleType
        
        """
        pass
    
    
    Height = None
    
    
    InsertionPoint = None
    
    
    InventorFileReference = None
    
    
    IsFirstAngleProjection = None
    
    
    RotationAngle = None
    
    
    Scale = None
    
    
    ShadedDPI = None
    
    
    ViewportId = None
    
    
    Width = None
    
    pass

class ViewRepBlockReference(object):
    """
    
    ViewRepBlockReference()
    """
    OwnerViewportId = None
    
    pass

class ViewStyleType():
    FromBase = None
    WireframeVisibleEdges = None
    WireframeHiddenEdges = None
    ShadedVisibleEdges = None
    ShadedHiddenEdges = None

class ViewTable(object):
    """
    
    """

    pass

class ViewTableRecord(object):
    """
    
    ViewTableRecord()
    """
    def DisassociateUcsFromView(self):
        """
        DisassociateUcsFromView -> void
        
        """
        pass
    
    
    AnnotationScale = None
    
    
    CategoryName = None
    
    
    IsPaperspaceView = None
    
    
    IsUcsAssociatedToView = None
    
    
    LayerState = None
    
    
    Layout = None
    
    
    LiveSection = None
    
    
    Thumbnail = None
    
    
    ViewAssociatedToViewport = None
    
    pass

class Viewport(object):
    """
    
    Viewport()
    """
    def FreezeLayersInViewport(self):
        """
        FreezeLayersInViewport -> void
            
            IEnumerator layerIds: 
            Input array of object IDs of layers to be frozen in the viewport
        """
        pass
    
    
    def GetFrozenLayers(self):
        """
        GetFrozenLayers -> ObjectIdCollection
        
        """
        pass
    
    
    def GetPreviousBackground(self):
        """
        GetPreviousBackground -> ObjectId
            
            Autodesk.AutoCAD.GraphicsInterface.DrawableType type: 
            Input type of the preferred previous background object
        """
        pass
    
    
    def GetUcs(self):
        """
        GetUcs -> void
            
            ref Point3d origin: 
            Input origin
            : Input x-axis
            
            ref Vector3d y: 
            Input y-axis
        """
        pass
    
    
    def IsLayerFrozenInViewport(self):
        """
        IsLayerFrozenInViewport -> bool
            
            ObjectId layerId: 
            Input id of the LayerTableRecord in question
        """
        pass
    
    
    def SetPreviousBackground(self):
        """
        SetPreviousBackground -> void
            
            ObjectId value: 
            Input object ID of the new background
            
            Autodesk.AutoCAD.GraphicsInterface.DrawableType type: 
            Input the drawable type
        """
        pass
    
    
    def SetShadePlot(self):
        """
        SetShadePlot -> void
            
            Autodesk.AutoCAD.DatabaseServices.ShadePlotType type: 
            Input type of shade plot
            
            ObjectId shadePlotId: 
            Input object id for VisualStyle or RenderSettings object to be used as the new shade plot object
        """
        pass
    
    
    def SetUcs(self):
        """
        SetUcs(ObjectId) -> void
            
            ObjectId userCoordinateSystemId: 
            Input reference to a valid UcsTableRecord object
        SetUcs(Point3d, Vector3d, Vector3d) -> void
            
            Point3d origin: 
            Input origin
            : Input X axis
            
            Vector3d y: 
            Input Y axis
        SetUcs(Autodesk.AutoCAD.DatabaseServices.OrthographicView) -> void
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input orthographic UCS
        """
        pass
    
    
    def SetSun(self):
        """
        SetSun -> ObjectId
            
            [CallerMustClose] DBObject sun: 
            Input a sun object
        """
        pass
    
    
    def SetUcsToWorld(self):
        """
        SetUcsToWorld -> void
        
        """
        pass
    
    
    def SetViewDirection(self):
        """
        SetViewDirection -> void
            
            Autodesk.AutoCAD.DatabaseServices.OrthographicView view: 
            Input orthographic view
        """
        pass
    
    
    def ThawAllLayersInViewport(self):
        """
        ThawAllLayersInViewport -> void
        
        """
        pass
    
    
    def ThawLayersInViewport(self):
        """
        ThawLayersInViewport -> void
            
            IEnumerator layerIds: 
            Input enumeration of object IDs of layers to be thawed in the viewport
        """
        pass
    
    
    def UpdateDisplay(self):
        """
        UpdateDisplay -> void
        
        """
        pass
    
    
    AmbientLightColor = None
    
    
    AnnotationScale = None
    
    
    BackClipDistance = None
    
    
    BackClipOn = None
    
    
    Background = None
    
    
    Brightness = None
    
    
    CenterPoint = None
    
    
    CircleSides = None
    
    
    Contrast = None
    
    
    CustomScale = None
    
    
    DefaultLightingOn = None
    
    
    DefaultLightingType = None
    
    
    EffectivePlotStyleSheet = None
    
    
    Elevation = None
    
    
    FastZoomOn = None
    
    
    FrontClipAtEyeOn = None
    
    
    FrontClipDistance = None
    
    
    FrontClipOn = None
    
    
    GridAdaptive = None
    
    
    GridBoundToLimits = None
    
    
    GridFollow = None
    
    
    GridIncrement = None
    
    
    GridMajor = None
    
    
    GridOn = None
    
    
    GridSubdivisionRestricted = None
    
    
    Height = None
    
    
    HiddenLinesRemoved = None
    
    
    LensLength = None
    
    
    LinkedToSheetView = None
    
    
    Locked = None
    
    
    NonRectClipEntityId = None
    
    
    NonRectClipOn = None
    
    
    Number = None
    
    
    On = None
    
    
    PerspectiveOn = None
    
    
    PlotAsRaster = None
    
    
    PlotStyleSheet = None
    
    
    PlotWireframe = None
    
    
    ShadePlot = None
    
    
    ShadePlotId = None
    
    
    SnapAngle = None
    
    
    SnapBasePoint = None
    
    
    SnapIncrement = None
    
    
    SnapIsometric = None
    
    
    SnapIsoPair = None
    
    
    SnapOn = None
    
    
    StandardScale = None
    
    
    SunId = None
    
    
    Thumbnail = None
    
    
    ToneOperatorParameters = None
    
    
    Transparent = None
    
    
    TwistAngle = None
    
    
    UcsFollowModeOn = None
    
    
    Ucs = None
    
    
    UcsIconAtOrigin = None
    
    
    UcsIconVisible = None
    
    
    UcsName = None
    
    
    UcsOrthographic = None
    
    
    UcsPerViewport = None
    
    
    ViewCenter = None
    
    
    ViewDirection = None
    
    
    ViewHeight = None
    
    
    ViewOrthographic = None
    
    
    ViewTarget = None
    
    
    VisualStyleId = None
    
    
    Width = None
    
    pass

class ViewportTable(object):
    """
    
    """

    pass

class ViewportTableRecord(object):
    """
    
    ViewportTableRecord()
    """
    def GetPreviousBackground(self):
        """
        GetPreviousBackground -> ObjectId
            
            Autodesk.AutoCAD.GraphicsInterface.DrawableType type: 
            Input type of the preferred previous background object.
        """
        pass
    
    
    def SetPreviousBackground(self):
        """
        SetPreviousBackground -> void
            
            ObjectId value: 
            Input object ID of the new background.
            
            Autodesk.AutoCAD.GraphicsInterface.DrawableType type: 
            Input the drawable type
        """
        pass
    
    
    CircleSides = None
    
    
    FastZoomsEnabled = None
    
    
    GridAdaptive = None
    
    
    GridBoundToLimits = None
    
    
    GridEnabled = None
    
    
    GridFollow = None
    
    
    GridIncrements = None
    
    
    GridMajor = None
    
    
    GridSubdivisionRestricted = None
    
    
    IconAtOrigin = None
    
    
    IconEnabled = None
    
    
    IsometricSnapEnabled = None
    
    
    LowerLeftCorner = None
    
    
    SnapAngle = None
    
    
    SnapBase = None
    
    
    SnapEnabled = None
    
    
    SnapIncrements = None
    
    
    SnapPair = None
    
    
    ToneOperatorParameters = None
    
    
    UcsFollowMode = None
    
    
    UcsSavedWithViewport = None
    
    
    UpperRightCorner = None
    
    pass

class Visibility():
    Visible = None
    Invisible = None

class VisibilityOverrule(object):
    """
    
    VisibilityOverrule()
    """
    def SetVisibility(self):
        """
        SetVisibility -> void
            
            Entity entity: 
            An Autodesk.AutoCAD.DatabaseServices.Entity that this overrule is applied against.
            
            Autodesk.AutoCAD.DatabaseServices.Visibility newVal: 
            The new visibility state.
            
            [MarshalAs(UnmanagedType.U1)] bool doSubents: 
            Pass in true if the new value should apply to subentitites.
        """
        pass
    
    
    def Visibility(self):
        """
        Visibility -> Autodesk.AutoCAD.DatabaseServices.Visibility
            
            Entity entity: 
            An Autodesk.AutoCAD.DatabaseServices.Entity that this overrule is applied against.
        """
        pass
    
    pass

class WblockNoticeEventArgs(object):
    """
    
    """
    To = None
    
    pass

class Wipeout(object):
    """
    
    Wipeout()
    """
    def SetFrom(self):
        """
        SetFrom -> void
            
            Point2dCollection points: 
            Data points for initialization
            
            Vector3d normal: 
            Normal vector for initialization
        """
        pass
    
    
    HasFrame = None
    
    pass

class Xline(object):
    """
    
    Xline()
    """
    BasePoint = None
    
    
    SecondPoint = None
    
    
    UnitDir = None
    
    pass

class Xrecord(object):
    """
    
    Xrecord()
    """
    def Append(self):
        """
        Append -> void
            
            ResultBuffer data: 
            Input first result buffer (not its address) in a linked list of result buffer that contain the data for the xrecord.
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> XrecordEnumerator
        
        """
        pass
    
    
    def IEnumerableGetEnumerator(self):
        """
        IEnumerableGetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def IEnumerableTypedValueGetEnumerator(self):
        """
        IEnumerableTypedValueGetEnumerator -> IEnumerator<TypedValue>
        
        """
        pass
    
    
    Data = None
    
    
    MergeStyle = None
    
    
    XlateReferences = None
    
    pass

class XrecordEnumerator(object):
    """
    
    """
    def InsertAtCurrent(self):
        """
        InsertAtCurrent -> void
            
            ResultBuffer data: 
            Input first result buffer (not its address) in a linked list of result buffer that contain the data for the xrecord.
        """
        pass
    
    
    def MoveNext(self):
        """
        MoveNext -> bool
        
        """
        pass
    
    
    def RemoveCurrent(self):
        """
        RemoveCurrent -> void
        
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    Current = None
    
    
    CurrentTypeCode = None
    
    
    IEnumeratorCurrent = None
    
    
    System.Collections.IEnumerator.Current = None
    
    pass

class XrefBeginOperationEventArgs(object):
    """
    
    """
    FileName = None
    
    
    From = None
    
    pass

class XrefComandeeredEventArgs(object):
    """
    
    """
    From = None
    
    
    Id = None
    
    pass

class XrefGraph(object):
    """
    
    """
    def GetXrefNode(self):
        """
        GetXrefNode(Database) -> XrefGraphNode
            
            Database db: 
            Input Autodesk.AutoCAD.DatabaseServices.Database object; node database to search for
        GetXrefNode(ObjectId) -> XrefGraphNode
            
            ObjectId btrId: 
            Input Autodesk.AutoCAD.DatabaseServices.ObjectId object; Block table record ID to search for
        GetXrefNode(int) -> XrefGraphNode
            
            int idx: 
            Input System.Int32 object; Index into the graph
        GetXrefNode(string) -> XrefGraphNode
            
            string name: 
            Input System.String object; Node name to search for
        """
        pass
    
    
    def MarkUnresolvedTrees(self):
        """
        MarkUnresolvedTrees -> bool
        
        """
        pass
    
    
    HostDrawing = None
    
    pass

class XrefGraphNode(object):
    """
    
    """
    BlockTableRecordId = None
    
    
    Database = None
    
    
    IsNested = None
    
    
    Name = None
    
    
    XrefNotificationStatus = None
    
    
    XrefStatus = None
    
    pass

class XrefNotificationStatus():
    ResolvedMatch = None
    ResolvedElsewhere = None
    ResolvedWithUpdate = None
    ResolvedUpdateAvailable = None

class XrefObjectId(object):
    """
    
    XrefObjectId(Autodesk.AutoCAD.DatabaseServices.ObjectId)
        Autodesk.AutoCAD.DatabaseServices.ObjectId LocalId : Input Autodesk.AutoCAD.DatabaseServices.ObjectId  object.
    
    
    XrefObjectId(Autodesk.AutoCAD.DatabaseServices.ObjectId, Autodesk.AutoCAD.DatabaseServices.Handle)
        Autodesk.AutoCAD.DatabaseServices.ObjectId XrefBlockTableRecordId : Input Autodesk.AutoCAD.DatabaseServices.ObjectId  object.
        Autodesk.AutoCAD.DatabaseServices.Handle hand : Input Autodesk.AutoCAD.DatabaseServices.Handle object.
    
    
    """
    def Deserialize(self):
        """
        Deserialize -> XrefObjectId
            
            ResultBuffer rbStart: 
            Input Autodesk.AutoCAD.DatabaseServices.ResultBuffer object.
            
            out ResultBuffer rbEnd: 
            Input Autodesk.AutoCAD.DatabaseServices.ResultBuffer object.
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input System.Object object.
        """
        pass
    
    
    def ResolveObjectId(self):
        """
        ResolveObjectId -> Autodesk.AutoCAD.DatabaseServices.ObjectId
        
        """
        pass
    
    
    def Serialize(self):
        """
        Serialize -> ResultBuffer
        
        """
        pass
    
    
    Handle = None
    
    
    IsNull = None
    
    
    IsValid = None
    
    
    IsXref = None
    
    
    ObjectId = None
    
    pass

class XrefOperation():
    XrefAttachOperation = 0
    XrefBindOperation = 1
    XrefDetachOperation = 2
    XrefOverlayOperation = 3
    XrefPathOperation = 4
    XrefReloadOperation = 5
    XrefResolveOperation = 6
    XrefUnloadOperation = 7
    XrefXBindOperation = 1

class XrefPreXrefLockFileEventArgs(object):
    """
    
    """
    btrId = None
    
    pass

class XrefRedirectedEventArgs(object):
    """
    
    """
    NewId = None
    
    
    OldId = None
    
    pass

class XrefStatus():
    NotAnXref = None
    Resolved = None
    Unloaded = None
    Unreferenced = None
    FileNotFound = None
    Unresolved = None

class XrefSubCommandEventArgs(object):
    """
    
    """
    btrIds = None
    
    
    btrNames = None
    
    
    paths = None
    
    
    xrefOp = None
    
    pass

class XrefVetoableSubCommandEventArgs(object):
    """
    
    """
    abortOp = None
    
    pass