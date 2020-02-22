class AugmentedPolylineCurve3d(object):
    """
    
    AugmentedPolylineCurve3d()()
    
    
    AugmentedPolylineCurve3d(Curve3d, double, double, double)
        Curve3d curve : Input any 3D curve
        double fromParameter : Input parameter value on curve
        double toParameter : Input parameter value on curve (must be larger than fromParam)
        double eps : Input approximation distance
    
    
    AugmentedPolylineCurve3d(KnotCollection, Point3dCollection, Vector3dCollection)
        KnotCollection knots : Input knot vector
        Point3dCollection controlPoints : Input control point collection
        Vector3dCollection vectorBundle : Input vector bundle collection
    
    
    AugmentedPolylineCurve3d(Point3dCollection, Vector3dCollection)
        Point3dCollection controlPoints : Input control point array
        Vector3dCollection vectorBundle : Input vector array
    
    
    """
    def GetD2VectorAt(self):
        """
        GetD2VectorAt -> Vector3d
            
            int index: 
            Input index of a vector
        """
        pass
    
    
    def GetPointAt(self):
        """
        GetPointAt -> Point3d
            
            int index: 
            Input index of a point
        """
        pass
    
    
    def GetVectorAt(self):
        """
        GetVectorAt -> Vector3d
            
            int index: 
            Input index of a vector
        """
        pass
    
    
    def SetD2VectorAt(self):
        """
        SetD2VectorAt -> void
            
            int index: 
            Input index of a vector
            
            Vector3d point: 
            Input vector point
        """
        pass
    
    
    def SetPointAt(self):
        """
        SetPointAt -> void
            
            int index: 
            Input index of a vector
            
            Point3d point: 
            Input 3d point
        """
        pass
    
    
    def SetVectorAt(self):
        """
        SetVectorAt -> void
            
            int index: 
            Input index of a vector
            
            Vector3d point: 
            Input vector point
        """
        pass
    
    
    ApproximateTolerance = None
    
    
    D1Vectors = None
    
    
    D2Vectors = None
    
    
    Points = None
    
    pass

class BoundBlock2d(object):
    """
    
    BoundBlock2d()()
    
    
    BoundBlock2d(Point2d, Point2d)
        Point2d point1 : Input point 1
        Point2d point2 : Input point 2
    
    
    BoundBlock2d(Point2d, Vector2d, Vector2d)
        Point2d basePoint : Input origin vertex a corner of the bounding area
        Vector2d direction1 : Input direction and size for first side of the bounding area
        Vector2d direction2 : Input direction and size for second side of the bounding area
    
    
    """
    def Contains(self):
        """
        Contains -> bool
            
            Point2d point: 
            Input point to test whether the point belongs to the block
        """
        pass
    
    
    def Extend(self):
        """
        Extend -> void
            
            Point2d point: 
            Input extension point
        """
        pass
    
    
    def GetMaximumPoint(self):
        """
        GetMaximumPoint -> Point2d
        
        """
        pass
    
    
    def GetMinimumPoint(self):
        """
        GetMinimumPoint -> Point2d
        
        """
        pass
    
    
    def IsDisjoint(self):
        """
        IsDisjoint -> bool
            
            BoundBlock2d block: 
            Input another Autodesk.AutoCAD.Geometry.BoundBlock2d object.
        """
        pass
    
    
    def Set(self):
        """
        Set(Point2d, Point2d) -> void
            
            Point2d firstPoint: 
            Input first point
            
            Point2d secondPoint: 
            Input second point
        Set(Point2d, Vector2d, Vector2d) -> void
            
            Point2d basePoint: 
            Input origin vertex a corner of the bounding area
            
            Vector2d direction1: 
            Input direction and size for first side of the bounding area
            
            Vector2d direction2: 
            Input direction and size for second side of the bounding area
        """
        pass
    
    
    def Swell(self):
        """
        Swell -> void
            
            double distance: 
            Input distance to expand the block
        """
        pass
    
    
    BasePoint = None
    
    
    Direction1 = None
    
    
    Direction2 = None
    
    
    IsBox = None
    
    pass

class BoundBlock3d(object):
    """
    
    BoundBlock3d()()
    
    
    BoundBlock3d(Point3d, Vector3d, Vector3d, Vector3d)
        Point3d point1 : Input origin vertex a corner of the bounding box
        Vector3d dir1 : Input direction and size for first side of the bounding box
        Vector3d dir2 : Input direction and size for second side of the bounding box
        Vector3d dir3 : Input direction and size for third side of the bounding box
    
    
    """
    def Contains(self):
        """
        Contains -> bool
            
            Point3d pointToTest: 
            Input point to test whether the point belongs to the block
        """
        pass
    
    
    def Extend(self):
        """
        Extend -> void
            
            Point3d pointToInclude: 
            Input extension point
        """
        pass
    
    
    def GetMaximumPoint(self):
        """
        GetMaximumPoint -> Point3d
        
        """
        pass
    
    
    def GetMinimumPoint(self):
        """
        GetMinimumPoint -> Point3d
        
        """
        pass
    
    
    def IsDisjoint(self):
        """
        IsDisjoint -> bool
            
            BoundBlock3d block: 
            Input another Autodesk.AutoCAD.Geometry.BoundBlock3d object.
        """
        pass
    
    
    def Set(self):
        """
        Set(Point3d, Point3d) -> void
            
            Point3d basePoint: 
            Input first point
            
            Point3d maximumPoint: 
            Input second point
        Set(Point3d, Vector3d, Vector3d, Vector3d) -> void
            
            Point3d basePoint: 
            Input origin vertex a corner of the bounding box
            
            Vector3d dir1: 
            Input direction and size for first side of the bounding box
            
            Vector3d dir2: 
            Input direction and size for second side of the bounding box
            
            Vector3d dir3: 
            Input direction and size for third side of the bounding box
        """
        pass
    
    
    def Swell(self):
        """
        Swell -> void
            
            double distance: 
            Input distance to expand the block
        """
        pass
    
    
    BasePoint = None
    
    
    Direction1 = None
    
    
    Direction2 = None
    
    
    Direction3 = None
    
    
    IsBox = None
    
    pass

class BoundedPlane(object):
    """
    
    BoundedPlane()()
    
    
    BoundedPlane(Point3d, Point3d, Point3d)
        Point3d p1 : Input point
        Point3d origin : Input origin point
        Point3d p2 : Input point
    
    
    BoundedPlane(Point3d, Vector3d, Vector3d)
        Point3d origin : Input plane origin
        Vector3d u : Input U direction
        Vector3d v : Input V direction
    
    
    """
    def IntersectWith(self):
        """
        IntersectWith(BoundedPlane) -> LineSegment3d
            
            BoundedPlane plane: 
            Input bounded plane
        IntersectWith(BoundedPlane, Tolerance) -> LineSegment3d
            
            BoundedPlane plane: 
            Input bounded plane
            
            Tolerance tolerance: 
            Input tolerance value
        IntersectWith(Plane) -> LineSegment3d
            
            Plane plane: 
            Input bounded plane
        IntersectWith(Plane, Tolerance) -> LineSegment3d
            
            Plane plane: 
            Input bounded plane
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        """
        pass
    
    
    def Set(self):
        """
        Set(Point3d, Point3d, Point3d) -> void
            
            Point3d p1: 
            Input first point on plane
            
            Point3d origin: 
            Input origin point
            
            Point3d p2: 
            Input second point on plane
        Set(Point3d, Vector3d, Vector3d) -> void
            
            Point3d origin: 
            Input origin point
            
            Vector3d u: 
            Input u vector
            
            Vector3d v: 
            Input Autodesk.AutoCAD.Geometry.Vector3d object, v vector
        """
        pass
    
    pass

class CircularArc2d(object):
    """
    
    CircularArc2d()()
    
    
    CircularArc2d(Point2d, Point2d, Point2d)
        Point2d startPoint : Input start point of arc
        Point2d point : Input point on arc
        Point2d endPoint : Input endpoint of arc
    
    
    CircularArc2d(Point2d, Point2d, double, [MarshalAs(UnmanagedType.U1)] bool)
        Point2d startPoint : Input start point of arc
        Point2d endPoint : Input endpoint of arc
        double bulge : Input bulge distance
        [MarshalAs(UnmanagedType.U1)] bool bulgeFlag : Input how to interpret bulge distance for arc calculation
    
    
    CircularArc2d(Point2d, double)
        Point2d center : Input center of circle
        double radius : Input radius of circle
    
    
    CircularArc2d(Point2d, double, double, double, Vector2d, [MarshalAs(UnmanagedType.U1)] bool)
        Point2d center : Input center of arc
        double radius : Input radius of arc
        double startAngle : Input angle of start point of arc
        double endAngle : Input angle of endpoint of arc
        Vector2d referenceVector : Input reference vector from which arc angles are measured
        [MarshalAs(UnmanagedType.U1)] bool isClockWise : Input direction of arc
    
    
    """
    def GetTangent(self):
        """
        GetTangent(Point2d) -> Line2d
            
            Point2d point: 
            Input point on full circle
        GetTangent(Point2d, Tolerance) -> Line2d
            
            Point2d point: 
            Input point on full circle
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(CircularArc2d) -> Point2d()
            
            CircularArc2d arc: 
            Input any 2D arc
        IntersectWith(CircularArc2d, Tolerance) -> Point2d()
            
            CircularArc2d arc: 
            Input any 2D arc
            
            Tolerance tolerance: 
            Input tolerance value
        IntersectWith(LinearEntity2d) -> Point2d()
            
            LinearEntity2d line: 
            Input any 2D linear entity
        IntersectWith(LinearEntity2d, Tolerance) -> Point2d()
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsInside(self):
        """
        IsInside(Point2d) -> bool
            
            Point2d point: 
            Input any 2D point
        IsInside(Point2d, Tolerance) -> bool
            
            Point2d point: 
            Input any 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(Curve2d, Curve2d, Curve2d, double, double, double) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
            
            Curve2d curve3: 
            Input any 2D curve
            
            double parameter1: 
            Input parameter value on curve1 where arc touches curve
            
            double parameter2: 
            Input parameter value on curve2 where arc touches curve
            
            double parameter3: 
            Input parameter value on curve3 where arc touches curve
        Set(Curve2d, Curve2d, double, double, double) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
            
            double radius: 
            Input any 2D curve
            
            double parameter1: 
            Input parameter value on curve1 where arc touches curve
            
            double parameter2: 
            Input parameter value on curve2 where arc touches curve
        Set(Point2d, Point2d, Point2d) -> void
            
            Point2d startPoint: 
            Input start point
            
            Point2d point: 
            Input point
            
            Point2d endPoint: 
            Input end point
        Set(Point2d, Point2d, double, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            Point2d startPoint: 
            Input start point of arc
            
            Point2d endPoint: 
            Input end point of arc
            
            double bulge: 
            Input bulge distance
            
            [MarshalAs(UnmanagedType.U1)] bool bulgeFlag: 
            Input how to interpret bulge distance for arc calculation
        Set(Point2d, double) -> void
            
            Point2d center: 
            Input center of circle
            
            double radius: 
            Input radius of circle
        Set(Point2d, double, double, double, Vector2d, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            Point2d center: 
            Input center of circle
            
            double radius: 
            Input radius of circle
            
            double angle1: 
            Input angle of start point of arc
            
            double angle2: 
            Input angle of endpoint of arc
            
            Vector2d referenceVector: 
            Input reference vector from which arc angles are measured
            
            [MarshalAs(UnmanagedType.U1)] bool isClockWise: 
            Input direction of arc
        """
        pass
    
    
    def SetAngles(self):
        """
        SetAngles -> void
            
            double startAngle: 
            Input start angle of arc
            
            double endAngle: 
            Input end angle of arc
        """
        pass
    
    
    def SetToComplement(self):
        """
        SetToComplement -> void
        
        """
        pass
    
    
    Center = None
    
    
    EndAngle = None
    
    
    EndPoint = None
    
    
    IsClockWise = None
    
    
    Radius = None
    
    
    ReferenceVector = None
    
    
    StartAngle = None
    
    
    StartPoint = None
    
    pass

class CircularArc3d(object):
    """
    
    CircularArc3d()()
    
    
    CircularArc3d(Point3d, Point3d, Point3d)
        Point3d startPoint : Input start point of arc
        Point3d endPoint : Input endpoint of arc
        pnt : Input point on arc
    
    
    CircularArc3d(Point3d, Vector3d, Vector3d, double, double, double)
        Point3d center : Input Autodesk.AutoCAD.Geometry.Point3d object.
        Vector3d normal : Input Autodesk.AutoCAD.Geometry.Vector3d object.
        Vector3d referenceVector : Input Autodesk.AutoCAD.Geometry.Vector3d object.
        double radius : Input.
        double startAngle : Input.
        double endAngle : Input.
    
    
    CircularArc3d(Point3d, Vector3d, double)
        Point3d center : Input center of arc
        Vector3d normal : Input normal vector of arc
        double radius : Input radius of arc
    
    
    """
    def ClosestPointToPlane(self):
        """
        ClosestPointToPlane(PlanarEntity) -> Point3d()
            
            PlanarEntity plane: 
            Input plane
        ClosestPointToPlane(PlanarEntity, Tolerance) -> Point3d()
            
            PlanarEntity plane: 
            Input plane
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetPlane(self):
        """
        GetPlane -> Plane
        
        """
        pass
    
    
    def GetTangent(self):
        """
        GetTangent(Point3d) -> Line3d
            
            Point3d pointValue: 
            Input point on full circle
        GetTangent(Point3d, Tolerance) -> Line3d
            
            Point3d pointValue: 
            Input point on full circle
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(CircularArc3d) -> Point3d()
            
            CircularArc3d arc: 
            Input any 3D arc
        IntersectWith(CircularArc3d, Tolerance) -> Point3d()
            
            CircularArc3d arc: 
            Input any 3D arc
            
            Tolerance tolerance: 
            Input tolerance value
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        IntersectWith(PlanarEntity) -> Point3d()
            
            PlanarEntity plane: 
            Input any plane
        IntersectWith(PlanarEntity, Tolerance) -> Point3d()
            
            PlanarEntity plane: 
            Input any plane
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsInside(self):
        """
        IsInside(Point3d) -> bool
            
            Point3d pointValue: 
            Input any 3D point
        IsInside(Point3d, Tolerance) -> bool
            
            Point3d pointValue: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def ProjectedIntersectWith(self):
        """
        ProjectedIntersectWith(LinearEntity3d, Vector3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Vector3d projectionDirection: 
            Input direction of projection
        ProjectedIntersectWith(LinearEntity3d, Vector3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Vector3d projectionDirection: 
            Input direction of projection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(Curve3d, Curve3d, Curve3d, double, double, double) -> void
            
            Curve3d curve1: 
            Input any 3D curve
            
            Curve3d curve2: 
            Input any 3D curve
            
            Curve3d curve3: 
            Input any 3D curve
            
            double param1: 
            Input parameter value on curve1 where arc touches curve
            
            double param2: 
            Input parameter value on curve2 where arc touches curve
            
            double param3: 
            Input parameter value on curve3 where arc touches curve
        Set(Curve3d, Curve3d, double, double, double) -> void
            
            Curve3d curve1: 
            Input any 3D curve
            
            Curve3d curve2: 
            Input any 3D curve
            
            double radius: 
            Input radius of arc
            
            double param1: 
            Input parameter value on curve1 where arc touches curve
            
            double param2: 
            Input parameter value on curve2 where arc touches curve
        Set(Point3d, Point3d, Point3d) -> void
            
            Point3d startPoint: 
            Input start point of arc
            
            Point3d pointOnArc: 
            Input point on arc
            
            Point3d endPoint: 
            Input endpoint of arc
        Set(Point3d, Vector3d, Vector3d, double, double, double) -> void
            
            Point3d center: 
            Input center of arc
            
            Vector3d normal: 
            Input normal vector of arc
            
            Vector3d referenceVector: 
            Input reference vector from which arc angles are measured
            
            double radius: 
            Input radius of arc
            
            double startAngle: 
            Input angle of start point of arc
            
            double endAngle: 
            Input angle of endpoint of arc
        Set(Point3d, Vector3d, double) -> void
            
            Point3d center: 
            Input center of arc
            
            Vector3d normal: 
            Input normal vector of arc
            
            double radius: 
            Input radius of arc
        """
        pass
    
    
    def SetAngles(self):
        """
        SetAngles -> void
            
            double startAngle: 
            Input start angle of arc
            
            double endAngle: 
            Input end angle of arc
        """
        pass
    
    
    def SetAxes(self):
        """
        SetAxes -> void
            
            Vector3d normal: 
            Input normal vector of arc
            
            Vector3d referenceVector: 
            Input reference vector of arc
        """
        pass
    
    
    Center = None
    
    
    EndAngle = None
    
    
    EndPoint = None
    
    
    Normal = None
    
    
    Radius = None
    
    
    ReferenceVector = None
    
    
    StartAngle = None
    
    
    StartPoint = None
    
    pass

class ClipBoundary2d(object):
    """
    
    ClipBoundary2d()()
    
    
    ClipBoundary2d(Point2d, Point2d)
        Point2d firstCorner : Input corner of a rectangle
        Point2d secondCorner : Input corner of a rectangle
    
    
    ClipBoundary2d(Point2dCollection)
        Point2dCollection clipBoundary : Input 2d point array
    
    
    """
    def ClipPolygon(self):
        """
        ClipPolygon -> ClipBoundary2dData
            
            Point2dCollection rawVertices: 
            Input 2d point array defining the input polygon. Self-intersecting and winding polygons are allowed.
        """
        pass
    
    
    def ClipPolyline(self):
        """
        ClipPolyline -> ClipBoundary2dData
            
            Point2dCollection rawVertices: 
            Input 2d point array defining the input polyline. Self-intersecting and winding polylines are allowed.
        """
        pass
    
    
    def Set(self):
        """
        Set(Point2d, Point2d) -> Autodesk.AutoCAD.Geometry.ClipError
            
            Point2d firstCorner: 
            Input first corner of a rectangle
            
            Point2d secondCorner: 
            Input second corner of a rectangle
        Set(Point2dCollection) -> Autodesk.AutoCAD.Geometry.ClipError
            
            Point2dCollection clipBoundary: 
            Input 2d point array
        """
        pass
    
    pass

class ClipBoundary2dData(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            ClipBoundary2dData a: 
            Input object to check against
        """
        pass
    
    
    ClipCondition = None
    
    
    ClippedSegmentSourceLabel = None
    
    
    ClippedVertices = None
    
    pass

class ClipCondition():
    Invalid = None
    AllSegmentsInside = None
    SegmentsIntersect = None
    AllSegmentsOutsideZeroWinds = None
    AllSegmentsOutsideOddWinds = None
    AllSegmentsOutsideEvenWinds = None

class ClipError():
    OK = None
    InvalidClipBoundary = None
    NotInitialized = None

class CompositeCurve2d(object):
    """
    
    CompositeCurve2d
        curveList : Input list of curves forming a composite curve
    """
    def GetCurves(self):
        """
        GetCurves -> Curve2d[]
        
        """
        pass
    
    
    def GlobalToLocalParameter(self):
        """
        GlobalToLocalParameter -> CompositeParameter
            
            double value: 
            Input global parameter value
        """
        pass
    
    
    def LocalToGlobalParameter(self):
        """
        LocalToGlobalParameter -> double
            
            CompositeParameter value: 
            Input local parameter value
        """
        pass
    
    
    def SetCurves(self):
        """
        SetCurves -> void
            
            Curve2d[] curves: 
            Input Autodesk.AutoCAD.Geometry.Curve2d[] object; array of curves in the composite curve
        """
        pass
    
    pass

class CompositeCurve3d(object):
    """
    
    CompositeCurve3d
        curveList : Input list of curves in the composite curve
    """
    def GetCurves(self):
        """
        GetCurves -> Curve3d[]
        
        """
        pass
    
    
    def GlobalToLocalParameter(self):
        """
        GlobalToLocalParameter -> CompositeParameter
            
            double value: 
            Input global parameter value
        """
        pass
    
    
    def LocalToGlobalParameter(self):
        """
        LocalToGlobalParameter -> double
            
            CompositeParameter value: 
            Input local parameter
        """
        pass
    
    pass

class CompositeParameter(object):
    """
    
    CompositeParameter
        int segmentIndex : Input segment index
        double localParameter : Input local parameter
    """
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
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(CompositeParameter) -> bool
            
            CompositeParameter a: 
            Input object to compare with
        IsEqualTo(CompositeParameter, Tolerance) -> bool
            
            CompositeParameter a: 
            Input Autodesk.AutoCAD.Geometry.CompositeParameter object.
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        """
        pass
    
    
    LocalParameter = None
    
    
    SegmentIndex = None
    
    pass

class Cone(object):
    """
    
    Cone()()
    
    
    Cone(double, double, Point3d, double, Vector3d)
        double cosineAngle : Input cosine of the angle formed by cone generator and its axis
        double sineAngle : Input sine of the angle formed by cone generator and its axis
        Point3d baseOrigin : Input center of the circular base
        double baseRadius : Input radius of the circular base
        Vector3d axisOfSymmetry : Input cone's axis of rotation
    
    
    Cone(double, double, Point3d, double, Vector3d, Vector3d, Interval, double, double)
        double cosineAngle : Input cosine of the angle formed by cone generator and its axis
        double sineAngle : Input sine of the angle formed by cone generator and its axis
        Point3d baseOrigin : Input center of the circular base
        double baseRadius : Input radius of the circular base
        Vector3d axisOfSymmetry : Input cone's axis of rotation
        Interval height : Input height of the cone
        double startAngle : Input start parameter on the base circle
        double endAngle : Input end parameter on the base circle
        refAxis : Input reference vector on base
    
    
    """
    def GetAngles(self):
        """
        GetAngles -> double()
        
        """
        pass
    
    
    def GetHalfAngles(self):
        """
        GetHalfAngles -> double()
        
        """
        pass
    
    
    def GetHeightAt(self):
        """
        GetHeightAt -> double
            
            double parameter: 
            Input output interval on the axis
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsClosed(self):
        """
        IsClosed() -> bool
        
        IsClosed(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(double, double, Point3d, double, Vector3d) -> void
            
            double cosineAngle: 
            Input cosine of the angle between axis and a generator
            
            double sineAngle: 
            Input sine of the angle between axis and a generator
            
            Point3d baseCenter: 
            Input center of the base
            
            double baseRadius: 
            Input radius of the base
            
            Vector3d axisOfSymmetry: 
            Input axis of rotation
        Set(double, double, Point3d, double, Vector3d, Vector3d, Interval, double, double) -> void
            
            double cosineAngle: 
            Input cosine of the angle between axis and a generator
            
            double sineAngle: 
            Input sine of the angle between axis and a generator
            
            Point3d baseCenter: 
            Input center of the base
            
            double baseRadius: 
            Input radius of the base
            
            Vector3d axisOfSymmetry: 
            Input axis of rotation
            
            Vector3d refAxis: 
            Input reference vector on the base circle
            
            Interval height: 
            Input interval on cone's axis
            
            double startAngle: 
            Input start parameter on base circle
            
            double endAngle: 
            Input end parameter on base circle
        """
        pass
    
    
    def SetAngles(self):
        """
        SetAngles -> void
            
            double startAngle: 
            Input start parameter on base circle
            
            double endAngle: 
            Input end parameter on base circle
        """
        pass
    
    
    Apex = None
    
    
    AxisOfSymmetry = None
    
    
    BaseCenter = None
    
    
    BaseRadius = None
    
    
    HalfAngle = None
    
    
    Height = None
    
    
    IsOuterNormal = None
    
    
    ReferenceAxis = None
    
    pass

class CoordinateSystem2d(object):
    """
    
    CoordinateSystem2d()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(CoordinateSystem2d) -> bool
            
            CoordinateSystem2d a: 
            Input object to compare with
        IsEqualTo(CoordinateSystem2d, Tolerance) -> bool
            
            CoordinateSystem2d a: 
            Input object to compare with
            
            Tolerance tolerance: 
            Input tolerance value
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
    
    
    Origin = None
    
    
    Xaxis = None
    
    
    Yaxis = None
    
    pass

class CoordinateSystem3d(object):
    """
    
    CoordinateSystem3d()
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(CoordinateSystem3d) -> bool
            
            CoordinateSystem3d a: 
            Input object to compare with
        IsEqualTo(CoordinateSystem3d, Tolerance) -> bool
            
            CoordinateSystem3d a: 
            Input object to compare with
            
            Tolerance tolerance: 
            Input tolerance value
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
    
    
    Origin = None
    
    
    Xaxis = None
    
    
    Yaxis = None
    
    
    Zaxis = None
    
    pass

class CubicSplineCurve2d(object):
    """
    
    CubicSplineCurve2d()()
    
    
    CubicSplineCurve2d(Curve2d, double)
        Curve2d curve : Input generic 2D curve
        double epsilon : Input approximation tolerance value
    
    
    CubicSplineCurve2d(Point2dCollection)
        Point2dCollection fitPoints : Input interpolating points
    
    
    CubicSplineCurve2d(Point2dCollection, Tolerance)
        Point2dCollection fitPoints : Input interpolating points
        Tolerance tolerance : Input tolerance object
    
    
    CubicSplineCurve2d(Point2dCollection, Vector2d, Vector2d)
        Point2dCollection fitPoints : Input interpolating points
        Vector2d startDerivative : Input derivative at the beginning of spline
        Vector2d endDerivative : Input derivative at the end of spline
    
    
    CubicSplineCurve2d(Point2dCollection, Vector2d, Vector2d, Tolerance)
        Point2dCollection fitPoints : Input interpolating points
        Vector2d startDerivative : Input derivative at the beginning of spline
        Vector2d endDerivative : Input derivative at the end of spline
        Tolerance tolerance : Input tolerance object
    
    
    """
    def GetFirstDerivativeAt(self):
        """
        GetFirstDerivativeAt -> Vector2d
            
            int index: 
            Input index of an interpolation point
        """
        pass
    
    
    def GetFitPointAt(self):
        """
        GetFitPointAt -> Point2d
            
            int index: 
            Input index of a fitPoint point
        """
        pass
    
    
    def SetFirstDerivativeAt(self):
        """
        SetFirstDerivativeAt -> void
            
            int index: 
            Input index of a fit point
            
            Vector2d derivative: 
            Input derivative
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> void
            
            int index: 
            Input index of a fit point
            
            Point2d point: 
            Input fit point
        """
        pass
    
    
    NumFitPoints = None
    
    pass

class CubicSplineCurve3d(object):
    """
    
    CubicSplineCurve3d()()
    
    
    CubicSplineCurve3d(Curve3d, double)
        Curve3d curve : Input generic 3D curve
        double epsilon : Input approximation tolerance value
    
    
    CubicSplineCurve3d(Point3dCollection)
        Point3dCollection points : Input interpolating points
    
    
    CubicSplineCurve3d(Point3dCollection, Tolerance)
        Point3dCollection points : Input interpolating points
        Tolerance tolerance : Input tolerance object
    
    
    CubicSplineCurve3d(Point3dCollection, Vector3d, Vector3d)
        Point3dCollection points : Input interpolating points
        Vector3d startDerivative : Input derivative at the beginning of spline
        Vector3d endDerivative : Input derivative at the end of spline
    
    
    CubicSplineCurve3d(Point3dCollection, Vector3d, Vector3d, Tolerance)
        Point3dCollection points : Input interpolating points
        Vector3d startDerivative : Input derivative at the beginning of spline
        Vector3d endDerivative : Input derivative at the end of spline
        Tolerance tolerance : Input tolerance object
    
    
    """
    def FirstDerivativeAt(self):
        """
        FirstDerivativeAt -> Vector3d
            
            int i: 
            Input index of an interpolation point
        """
        pass
    
    
    def FitPointAt(self):
        """
        FitPointAt -> Point3d
            
            int i: 
            Input index of a fitPoint point
        """
        pass
    
    
    def SetFirstDerivativeAt(self):
        """
        SetFirstDerivativeAt -> void
            
            int i: 
            Input index of a fit point
            
            Vector3d derivative: 
            Input derivative
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> void
            
            int i: 
            Input index of a fit point
            
            Point3d point: 
            Input fit point
        """
        pass
    
    
    NumberOfFitPoints = None
    
    pass

class Curve2d(object):
    """
    
    """
    def EvaluatePoint(self):
        """
        EvaluatePoint -> Point2d
            
            double parameter: 
            Input parameter value at which curve is to be evaluated
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> Curve2d()
            
            Interval interval: 
            Input interval of curve that is to be exploded
        """
        pass
    
    
    def GetArea(self):
        """
        GetArea(double, double) -> double
            
            double startParameter: 
            Input parameter value of interval start
            
            double endParameter: 
            Input parameter value of interval end (must be larger than startParameter)
        GetArea(double, double, Tolerance) -> double
            
            double startParameter: 
            Input parameter value of interval start
            
            double endParameter: 
            Input parameter value of interval end (must be larger than startParameter)
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetBoundBlockOf(self):
        """
        GetBoundBlockOf -> BoundBlock2d
            
            Interval range: 
            Input sub-interval of curve
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Curve2d) -> PointOnCurve2d()
            
            Curve2d curve: 
            Input any 2D curve
        GetClosestPointTo(Curve2d, Tolerance) -> PointOnCurve2d()
            
            Curve2d curve: 
            Input any 2D curve
            
            Tolerance tolerance: 
            Input tolerance value
        GetClosestPointTo(Point2d) -> PointOnCurve2d
            
            Point2d point: 
            Input any 2D point
        GetClosestPointTo(Point2d, Tolerance) -> PointOnCurve2d
            
            Point2d point: 
            Input any 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetDistanceTo(self):
        """
        GetDistanceTo(Curve2d) -> double
            
            Curve2d curve: 
            Input any 2D curve
        GetDistanceTo(Curve2d, Tolerance) -> double
            
            Curve2d curve: 
            Input any 2D curve
            
            Tolerance tolerance: 
            Input tolerance value
        GetDistanceTo(Point2d) -> double
            
            Point2d point: 
            Input any 2D point
        GetDistanceTo(Point2d, Tolerance) -> double
            
            Point2d point: 
            Input any 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetInterval(self):
        """
        GetInterval -> Interval
        
        """
        pass
    
    
    def GetLength(self):
        """
        GetLength(double, double) -> double
            
            double fromParameter: 
            Input first parameter value
            
            double toParameter: 
            Input second parameter value
        GetLength(double, double, Tolerance) -> double
            
            double fromParameter: 
            Input first parameter value
            
            double toParameter: 
            Input second parameter value
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetNormalPoint(self):
        """
        GetNormalPoint(Point2d) -> PointOnCurve2d
            
            Point2d point: 
            Input any 2D point
        GetNormalPoint(Point2d, Tolerance) -> PointOnCurve2d
            
            Point2d point: 
            Input any 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetOrthoBoundBlockOf(self):
        """
        GetOrthoBoundBlockOf -> BoundBlock2d
            
            Interval range: 
            Input sub-interval of curve
        """
        pass
    
    
    def GetParameterAtLength(self):
        """
        GetParameterAtLength(double, double, [MarshalAs(UnmanagedType.U1)] bool) -> double
            
            double datumParameter: 
            Input parameter value
            
            double length: 
            Input arc length
            
            [MarshalAs(UnmanagedType.U1)] bool parameterDirection: 
            Input parameter direction
        GetParameterAtLength(double, double, [MarshalAs(UnmanagedType.U1)] bool, Tolerance) -> double
            
            double datumParameter: 
            Input parameter value
            
            double length: 
            Input arc length
            
            [MarshalAs(UnmanagedType.U1)] bool parameterDirection: 
            Input parameter direction
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetParameterOf(self):
        """
        GetParameterOf(Point2d) -> double
            
            Point2d point: 
            Input point on the curve
        GetParameterOf(Point2d, Tolerance) -> double
            
            Point2d point: 
            Input point on the curve
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetReverseParameterCurve(self):
        """
        GetReverseParameterCurve -> Curve2d
        
        """
        pass
    
    
    def GetSamplePoints(self):
        """
        GetSamplePoints(double, double, double) -> PointOnCurve2d()
            
            double fromParameter: 
            Input starting parameter
            
            double toParameter: 
            Input ending parameter
            
            double approxEps: 
            Input chord-height tolerance
        GetSamplePoints(int) -> Point2d()
            
            int numSample: 
            Input number of points that are to be returned
        """
        pass
    
    
    def GetSplitCurves(self):
        """
        GetSplitCurves -> Curve2d()
            
            double value: 
            Input parameter value at which curve is to be split
        """
        pass
    
    
    def GetTrimmedOffset(self):
        """
        GetTrimmedOffset(double, OffsetCurveExtensionType) -> Curve2d()
            
            double distance: 
            Input offset distance
            
            OffsetCurveExtensionType extensionType: 
            Input determines how offset curve will be extended at points of C1 discontinuity
        GetTrimmedOffset(double, OffsetCurveExtensionType, Tolerance) -> Curve2d()
            
            double distance: 
            Input offset distance
            
            OffsetCurveExtensionType extensionType: 
            Input determines how offset curve will be extended at points of C1 discontinuity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsClosed(self):
        """
        IsClosed() -> bool
        
        IsClosed(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsDegenerate(self):
        """
        IsDegenerate(out Entity2d) -> bool
            
            out Entity2d result: 
            Output type of degenerate entity
        IsDegenerate(out Entity2d, Tolerance) -> bool
            
            out Entity2d result: 
            Output type of degenerate entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsLinear(self):
        """
        IsLinear(out Line2d) -> bool
            
            out Line2d line: 
            Output line on which this curve lies if it is linear
        IsLinear(out Line2d, Tolerance) -> bool
            
            out Line2d line: 
            Output line on which this curve lies if it is linear
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn(Point2d) -> bool
            
            Point2d point: 
            Input any 2D point
        IsOn(Point2d, Tolerance) -> bool
            
            Point2d point: 
            Input any 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        IsOn(Point2d, out double) -> bool
            
            Point2d point: 
            Input any 2D point
            
            out double value: 
            Output parameter value of point if point lies on curve
        IsOn(Point2d, out double, Tolerance) -> bool
            
            Point2d point: 
            Input any 2D point
            
            out double value: 
            Output parameter value of point if point lies on curve
            
            Tolerance tolerance: 
            Input tolerance value
        IsOn(double) -> bool
            
            double parameter: 
            Input parameter value
        IsOn(double, Tolerance) -> bool
            
            double parameter: 
            Input parameter value
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPeriodic(self):
        """
        IsPeriodic -> bool
            
            out double period: 
            Input period of curve parameter
        """
        pass
    
    
    def SetInterval(self):
        """
        SetInterval -> void
            
            Interval value: 
            Input interval
        """
        pass
    
    
    BoundBlock = None
    
    
    EndPoint = None
    
    
    HasEndPoint = None
    
    
    HasStartPoint = None
    
    
    OrthoBoundBlock = None
    
    
    StartPoint = None
    
    pass

class Curve2dCollection(object):
    """
    
    Curve2dCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            Curve2d value: 
            Input curve to add
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
            
            Curve2d value: 
            Input object to check for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Curve2d[] array: 
            Input array to copy to
            
            int index: 
            Input index to begin copying at
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
            
            Curve2d value: 
            Input object to get the index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            Curve2d value: 
            Input value to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            Curve2d value: 
            Input object to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index of object to remove
        """
        pass
    
    
    Count = None
    
    
    IsFixedSize = None
    
    
    IsReadOnly = None
    
    pass

class Curve3d(object):
    """
    
    """
    def EvaluatePoint(self):
        """
        EvaluatePoint -> Point3d
            
            double value: 
            Input parameter value at which curve is to be evaluated
        """
        pass
    
    
    def Explode(self):
        """
        Explode -> Curve3d()
            
            Interval interval: 
            Input interval of curve that is to be exploded
        """
        pass
    
    
    def GetArea(self):
        """
        GetArea(double, double) -> double
            
            double startingParameter: 
            Input parameter value of interval start
            
            double endingParameter: 
            Input parameter value of interval end (must be larger than startParameter)
        GetArea(double, double, Tolerance) -> double
            
            double startingParameter: 
            Input parameter value of interval start
            
            double endingParameter: 
            Input parameter value of interval end (must be larger than startParameter)
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetBoundBlockOf(self):
        """
        GetBoundBlockOf -> BoundBlock3d
            
            Interval range: 
            Input sub-interval of curve
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Curve3d) -> PointOnCurve3d()
            
            Curve3d curve3d: 
            Input any 3D curve
        GetClosestPointTo(Curve3d, Tolerance) -> PointOnCurve3d()
            
            Curve3d curve3d: 
            Input any 3D curve
            
            Tolerance tolerance: 
            Input tolerance value
        GetClosestPointTo(Point3d) -> PointOnCurve3d
            
            Point3d point: 
            Input any 3D point
        GetClosestPointTo(Point3d, Tolerance) -> PointOnCurve3d
            
            Point3d point: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetDistanceTo(self):
        """
        GetDistanceTo(Curve3d) -> double
            
            Curve3d curve: 
            Input any 3D curve
        GetDistanceTo(Curve3d, Tolerance) -> double
            
            Curve3d curve: 
            Input any 3D curve
            
            Tolerance tolerance: 
            Input tolerance value
        GetDistanceTo(Point3d) -> double
            
            Point3d point: 
            Input any 3D point
        GetDistanceTo(Point3d, Tolerance) -> double
            
            Point3d point: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetInterval(self):
        """
        GetInterval -> Interval
        
        """
        pass
    
    
    def GetLength(self):
        """
        GetLength -> double
            
            double fromParameter: 
            Input parameter value of interval start
            
            double toParameter: 
            Input parameter value of interval end (must be larger than fromParameter)
            
            double tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetNewSamplePoints(self):
        """
        GetNewSamplePoints -> PointOnCurve3d()
            
            double fromParameter: 
            Input starting parameter
            
            double toParameter: 
            Input ending parameter
            
            double chordHeight: 
            Input chord-height tolerance
        """
        pass
    
    
    def GetNormalPoint(self):
        """
        GetNormalPoint(Point3d) -> PointOnCurve3d
            
            Point3d point: 
            Input any 3D point
        GetNormalPoint(Point3d, Tolerance) -> PointOnCurve3d
            
            Point3d point: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetOrthoBoundBlockOf(self):
        """
        GetOrthoBoundBlockOf -> BoundBlock3d
            
            Interval range: 
            Input sub-interval of curve
        """
        pass
    
    
    def GetOrthoProjectEntity(self):
        """
        GetOrthoProjectEntity(Plane) -> Entity3d
            
            Plane projectionPlane: 
            Input plane on which curve is to be projected
        GetOrthoProjectEntity(Plane, Tolerance) -> Entity3d
            
            Plane projectionPlane: 
            Input plane on which curve is to be projected
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetParameterAtLength(self):
        """
        GetParameterAtLength -> double
            
            double datumParameter: 
            Input parameter value
            
            double length: 
            Input arc length
            
            [MarshalAs(UnmanagedType.U1)] bool direction: 
            Input parameter direction
            
            double tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetParameterOf(self):
        """
        GetParameterOf(Point3d) -> double
            
            Point3d point: 
            Input any 3D point
        GetParameterOf(Point3d, Tolerance) -> double
            
            Point3d point: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetProjectedClosestPointTo(self):
        """
        GetProjectedClosestPointTo(Curve3d, Vector3d) -> PointOnCurve3d()
            
            Curve3d curve3d: 
            Input any 3D curve
            
            Vector3d projectDirection: 
            Input direction of projection
        GetProjectedClosestPointTo(Curve3d, Vector3d, Tolerance) -> PointOnCurve3d()
            
            Curve3d curve3d: 
            Input any 3D curve
            
            Vector3d projectDirection: 
            Input direction of projection
            
            Tolerance tolerance: 
            Input tolerance value
        GetProjectedClosestPointTo(Point3d, Vector3d) -> PointOnCurve3d
            
            Point3d point: 
            Input any 3D point
            
            Vector3d projectDirection: 
            Input direction of projection
        GetProjectedClosestPointTo(Point3d, Vector3d, Tolerance) -> PointOnCurve3d
            
            Point3d point: 
            Input any 3D point
            
            Vector3d projectDirection: 
            Input direction of projection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetProjectedEntity(self):
        """
        GetProjectedEntity(Plane, Vector3d) -> Entity3d
            
            Plane projectionPlane: 
            Input plane on which curve is to be projected
            
            Vector3d projectDirection: 
            Input direction in which curve is to be projected
        GetProjectedEntity(Plane, Vector3d, Tolerance) -> Entity3d
            
            Plane projectionPlane: 
            Input plane on which curve is to be projected
            
            Vector3d projectDirection: 
            Input direction in which curve is to be projected
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetReverseParameterCurve(self):
        """
        GetReverseParameterCurve -> Curve3d
        
        """
        pass
    
    
    def GetSamplePoints(self):
        """
        GetSamplePoints(double, double, double) -> PointOnCurve3d()
            
            double fromParameter: 
            Input starting parameter
            
            double toParameter: 
            Input ending parameter
            
            double chordHeight: 
            Input chord-height tolerance
        GetSamplePoints(int) -> PointOnCurve3d()
            
            int numSample: 
            Input number of points that are to be returned
        """
        pass
    
    
    def GetSplitCurves(self):
        """
        GetSplitCurves -> Curve3d()
            
            double value: 
            Input parameter value at which curve is to be split
        """
        pass
    
    
    def GetTrimmedOffset(self):
        """
        GetTrimmedOffset(double, Vector3d, OffsetCurveExtensionType) -> Curve3d()
            
            double distance: 
            Input offset distance
            
            Vector3d planeNormal: 
            Input normal vector to plane of curve
            
            OffsetCurveExtensionType extensionType: 
            Input determines how offset curve will be extended at points of C1 discontinuity
        GetTrimmedOffset(double, Vector3d, OffsetCurveExtensionType, Tolerance) -> Curve3d()
            
            double distance: 
            Input offset distance
            
            Vector3d planeNormal: 
            Input normal vector to plane of curve
            
            OffsetCurveExtensionType extensionType: 
            Input determines how offset curve will be extended at points of C1 discontinuity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsClosed(self):
        """
        IsClosed() -> bool
        
        IsClosed(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsCoplanarWith(self):
        """
        IsCoplanarWith(Curve3d, out Plane) -> bool
            
            Curve3d curve3d: 
            Input any 3D curve
            
            out Plane plane: 
            Input plane in which this curve and input curve lie
        IsCoplanarWith(Curve3d, out Plane, Tolerance) -> bool
            
            Curve3d curve3d: 
            Input any 3D curve
            
            out Plane plane: 
            Input plane in which this curve and input curve lie
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsDegenerate(self):
        """
        IsDegenerate(out Entity3d) -> bool
            
            out Entity3d result: 
            Output type of degenerate entity
        IsDegenerate(out Entity3d, Tolerance) -> bool
            
            out Entity3d result: 
            Output type of degenerate entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsLinear(self):
        """
        IsLinear(out Line3d) -> bool
            
            out Line3d line: 
            Input line on which this curve lies if it is linear
        IsLinear(out Line3d, Tolerance) -> bool
            
            out Line3d line: 
            Input line on which this curve lies if it is linear
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn(Point3d) -> bool
            
            Point3d point: 
            Input any 3D point
        IsOn(Point3d, Tolerance) -> bool
            
            Point3d point: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        IsOn(Point3d, out double) -> bool
            
            Point3d point: 
            Input any 3D point
            
            out double value: 
            Input parameter value of point if point lies on curve
        IsOn(Point3d, out double, Tolerance) -> bool
            
            Point3d point: 
            Input any 3D point
            
            out double value: 
            Input parameter value of point if point lies on curve
            
            Tolerance tolerance: 
            Input tolerance value
        IsOn(double) -> bool
            
            double value: 
            Input parameter value
        IsOn(double, Tolerance) -> bool
            
            double value: 
            Input parameter value
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPeriodic(self):
        """
        IsPeriodic -> bool
            
            out double period: 
            Input period of curve parameter
        """
        pass
    
    
    def IsPlanar(self):
        """
        IsPlanar(out Plane) -> bool
            
            out Plane plane: 
            Input plane on which this curve lies if it is planar
        IsPlanar(out Plane, Tolerance) -> bool
            
            out Plane plane: 
            Input plane on which this curve lies if it is planar
            
            Tolerance tolerance: 
            EvaluatePoint
        """
        pass
    
    
    def SetInterval(self):
        """
        SetInterval -> void
            
            Interval value: 
            Input parametric interval on which this curve is defined
        """
        pass
    
    
    BoundBlock = None
    
    
    EndPoint = None
    
    
    HasEndPoint = None
    
    
    HasStartPoint = None
    
    
    OrthoBoundBlock = None
    
    
    StartPoint = None
    
    pass

class Curve3dCollection(object):
    """
    
    Curve3dCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            Curve3d value: 
            Input item to add
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
            
            Curve3d value: 
            Input value to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Curve3d[] array: 
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
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Curve3d value: 
            Input value to retrieve index
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            Curve3d value: 
            Input item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            Curve3d value: 
            Input item to remove
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

class CurveBoundary(object):
    """
    
    CurveBoundary()()
    
    
    """
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            int numElements: 
            Input number of elements in curve boundary
            
            Entity3d[] curve3ds: 
            Input array of 3D space geometry of each element of curve boundary
            
            Curve2d[] curve2ds: 
            Input array of parameter space geometry of each element of curve boundary
            
            [MarshalAs(UnmanagedType.U1)] bool orientation3d: 
            Input logical orientation applicable to each element of 3dGeometry
            
            [MarshalAs(UnmanagedType.U1)] bool orientation2d: 
            Input logical orientation applied to each element of paramGeometry
        """
        pass
    
    
    def SetToOwnCurves(self):
        """
        SetToOwnCurves -> void
        
        """
        pass
    
    
    Contour = None
    
    
    DegenerateCurve = None
    
    
    DegeneratePosition = None
    
    
    IsDegenerate = None
    
    
    IsOwnerOfCurves = None
    
    
    NumElements = None
    
    pass

class CurveBoundaryData(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetCurve2ds(self):
        """
        GetCurve2ds -> Curve2d()
        
        """
        pass
    
    
    def GetCurve3ds(self):
        """
        GetCurve3ds -> Entity3d()
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            CurveBoundaryData a: 
            Input object to check equivalency
        """
        pass
    
    
    Orientation2d = None
    
    
    Orientation3d = None
    
    pass

class CurveCurveIntersector2d(object):
    """
    
    CurveCurveIntersector2d()()
    
    
    CurveCurveIntersector2d(Curve2d, Curve2d)
        Curve2d curve1 : Input first curve
        Curve2d curve2 : Input second curve
    
    
    CurveCurveIntersector2d(Curve2d, Curve2d, Interval, Interval)
        Curve2d curve1 : Input first curve
        Curve2d curve2 : Input second curve
        Interval range1 : Input first range interval
        Interval range2 : Input second range interval
    
    
    """
    def ChangeCurveOrder(self):
        """
        ChangeCurveOrder -> void
        
        """
        pass
    
    
    def GetIntersectionParameters(self):
        """
        GetIntersectionParameters -> double()
            
            int intersection: 
            Input intersection point
        """
        pass
    
    
    def GetIntersectionPoint(self):
        """
        GetIntersectionPoint -> Point2d
            
            int number: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetIntersectionPointTolerance(self):
        """
        GetIntersectionPointTolerance -> double
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetIntersectionRanges(self):
        """
        GetIntersectionRanges -> Interval()
        
        """
        pass
    
    
    def GetOverlapRanges(self):
        """
        GetOverlapRanges -> Interval()
            
            int overlapNumber: 
            Input number of overlaps to get intervals for
        """
        pass
    
    
    def GetPointOnCurve1(self):
        """
        GetPointOnCurve1 -> PointOnCurve2d
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetPointOnCurve2(self):
        """
        GetPointOnCurve2 -> PointOnCurve2d
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def IsTangential(self):
        """
        IsTangential -> bool
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def IsTransversal(self):
        """
        IsTransversal -> bool
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def OrderWithRegardsTo1(self):
        """
        OrderWithRegardsTo1 -> void
        
        """
        pass
    
    
    def OrderWithRegardsTo2(self):
        """
        OrderWithRegardsTo2 -> void
        
        """
        pass
    
    
    def Set(self):
        """
        Set(Curve2d, Curve2d) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
        Set(Curve2d, Curve2d, Autodesk.AutoCAD.Geometry.Tolerance) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
            
            Autodesk.AutoCAD.Geometry.Tolerance tolerance: 
            Input tolerance value
        Set(Curve2d, Curve2d, Interval, Interval) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
            
            Interval range1: 
            Input subset of curve1 domain
            
            Interval range2: 
            Input subset of curve2 domain
        Set(Curve2d, Curve2d, Interval, Interval, Autodesk.AutoCAD.Geometry.Tolerance) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
            
            Interval range1: 
            Input subset of curve1 domain
            
            Interval range2: 
            Input subset of curve2 domain
            
            Autodesk.AutoCAD.Geometry.Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    Curve1 = None
    
    
    Curve2 = None
    
    
    NumberOfIntersectionPoints = None
    
    
    OverlapCount = None
    
    
    OverlapDirection = None
    
    
    Tolerance = None
    
    pass

class CurveCurveIntersector3d(object):
    """
    
    CurveCurveIntersector3d()()
    
    
    CurveCurveIntersector3d(Curve3d, Curve3d, Interval, Interval, Vector3d)
        Curve3d curve1 : Input first curve
        Curve3d curve2 : Input second curve
        Interval range1 : Input first range interval
        Interval range2 : Input second range interval
        Vector3d planeNormal : Input optional plane normal
    
    
    CurveCurveIntersector3d(Curve3d, Curve3d, Vector3d)
        Curve3d curve1 : Input first curve
        Curve3d curve2 : Input second curve
        Vector3d planeNormal : Input optional plane normal
    
    
    """
    def ChangeCurveOrder(self):
        """
        ChangeCurveOrder -> void
        
        """
        pass
    
    
    def GetIntersectionParameters(self):
        """
        GetIntersectionParameters -> double()
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetIntersectionPoint(self):
        """
        GetIntersectionPoint -> Point3d
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetIntersectionPointTolerance(self):
        """
        GetIntersectionPointTolerance -> double
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetIntersectionRanges(self):
        """
        GetIntersectionRanges -> Interval()
        
        """
        pass
    
    
    def GetOverlapRanges(self):
        """
        GetOverlapRanges -> Interval()
            
            int overlap: 
            Input number of overlaps to get intervals for
        """
        pass
    
    
    def GetPointOnCurve1(self):
        """
        GetPointOnCurve1 -> PointOnCurve3d
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def GetPointOnCurve2(self):
        """
        GetPointOnCurve2 -> PointOnCurve3d
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def IsTangential(self):
        """
        IsTangential -> bool
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def IsTransversal(self):
        """
        IsTransversal -> bool
            
            int intersection: 
            Input index to the intersection desired
        """
        pass
    
    
    def OrderWithRegardsTo1(self):
        """
        OrderWithRegardsTo1 -> void
        
        """
        pass
    
    
    def OrderWithRegardsTo2(self):
        """
        OrderWithRegardsTo2 -> void
        
        """
        pass
    
    
    def OverlapCount(self):
        """
        OverlapCount -> Integer
        
        """
        pass
    
    
    def OverlapDirection(self):
        """
        OverlapDirection -> bool
        
        """
        pass
    
    
    def Set(self):
        """
        Set(Curve3d, Curve3d, Interval, Interval, Vector3d) -> void
            
            Curve3d curve1: 
            Output Autodesk.AutoCAD.Geometry.Curve3d object; first curve
            
            Curve3d curve2: 
            Output Autodesk.AutoCAD.Geometry.Curve3d object; second curve
            
            Interval range1: 
            Output Autodesk.AutoCAD.Geometry.Interval object; first range interval
            
            Interval range2: 
            Output Autodesk.AutoCAD.Geometry.Interval object; second range interval
            
            Vector3d planeNormal: 
            Input optional plane normal
        Set(Curve3d, Curve3d, Interval, Interval, Vector3d, Autodesk.AutoCAD.Geometry.Tolerance) -> void
            
            Curve3d curve1: 
            Output Autodesk.AutoCAD.Geometry.Curve3d object; first curve
            
            Curve3d curve2: 
            Output Autodesk.AutoCAD.Geometry.Curve3d object; second curve
            
            Interval range1: 
            Output Autodesk.AutoCAD.Geometry.Interval object; first range interval
            
            Interval range2: 
            Output Autodesk.AutoCAD.Geometry.Interval object; second range interval
            
            Vector3d planeNormal: 
            Input optional plane normal
            
            Autodesk.AutoCAD.Geometry.Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        Set(Curve3d, Curve3d, Vector3d) -> void
            
            Curve3d curve1: 
            Input first curve
            
            Curve3d curve2: 
            Input second curve
            
            Vector3d planeNormal: 
            Input optional plane normal
        Set(Curve3d, Curve3d, Vector3d, Autodesk.AutoCAD.Geometry.Tolerance) -> void
            
            Curve3d curve1: 
            Input first curve
            
            Curve3d curve2: 
            Input second curve
            
            Vector3d planeNormal: 
            Input optional plane normal
            
            Autodesk.AutoCAD.Geometry.Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Vector3d object.
        """
        pass
    
    
    Curve1 = None
    
    
    Curve2 = None
    
    
    NumberOfIntersectionPoints = None
    
    
    PlaneNormal = None
    
    
    Tolerance = None
    
    pass

class Cylinder(object):
    """
    
    Cylinder()()
    
    
    Cylinder(double, Point3d, Vector3d)
        double radius : Input cylinder radius
        Point3d origin : Input reference point on the cylinder axis
        Vector3d axisOfSymmetry : Input rotation axis
    
    
    Cylinder(double, Point3d, Vector3d, Vector3d, Interval, double, double)
        double radius : Input cylinder radius
        Point3d origin : Input base point on the cylinder axis
        Vector3d axisOfSymmetry : Input axis of rotation
        Vector3d referenceAxis : Input reference vector on the base circle
        Interval height : Input interval on the axis referred by the origin
        double startAngle : Input start angle on the base circle
        double endAngle : Input end angle on the base circle
    
    
    """
    def GetAngles(self):
        """
        GetAngles -> double()
        
        """
        pass
    
    
    def GetHeightAt(self):
        """
        GetHeightAt -> double
            
            double parameter: 
            Input parameter from cylinder domain
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsClosed(self):
        """
        IsClosed() -> bool
        
        IsClosed(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(double, Point3d, Vector3d) -> void
            
            double radius: 
            Input radius
            
            Point3d origin: 
            Input origin
            
            Vector3d axisOfSymmetry: 
            Input axis of rotation
        Set(double, Point3d, Vector3d, Vector3d, Interval, double, double) -> void
            
            double radius: 
            Input radius
            
            Point3d origin: 
            Input origin
            
            Vector3d axisOfSymmetry: 
            Input axis of rotation
            
            Vector3d referenceAxis: 
            Input reference vector
            
            Interval height: 
            Input height interval
            
            double startAngle: 
            Input start angle
            
            double endAngle: 
            Input end angle
        """
        pass
    
    
    def SetAngles(self):
        """
        SetAngles -> void
            
            double startAngle: 
            Input start angle
            
            double endAngle: 
            Input end angle
        """
        pass
    
    
    AxisOfSymmetry = None
    
    
    Height = None
    
    
    IsOuterNormal = None
    
    
    Origin = None
    
    
    Radius = None
    
    
    ReferenceAxis = None
    
    pass

class EllipticalArc2d(object):
    """
    
    EllipticalArc2d()()
    
    
    EllipticalArc2d(CircularArc2d)
        CircularArc2d arc : Input any 2D circular arc
    
    
    EllipticalArc2d(Point2d, Vector2d, Vector2d, double, double)
        Point2d center : Input ellipse center
        Vector2d majorAxis : Input ellipse major axis
        Vector2d minorAxis : Input ellipse minor axis
        double majorRadius : Input ellipse major radius
        double minorRadius : Input ellipse minor radius
    
    
    EllipticalArc2d(Point2d, Vector2d, Vector2d, double, double, double, double)
        Point2d center : Input ellipse center
        Vector2d majorAxis : Input ellipse major axis
        Vector2d minorAxis : Input ellipse minor axis
        double majorRadius : Input ellipse major radius
        double minorRadius : Input ellipse minor radius
        double startAngle : Input angle of ellipse start point
        double endAngle : Input angle of ellipse end point
    
    
    """
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity2d) -> Point2d()
            
            LinearEntity2d line: 
            Input any 2D linear entity
        IntersectWith(LinearEntity2d, Tolerance) -> Point2d()
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsCircular(self):
        """
        IsCircular() -> bool
        
        IsCircular(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsInside(self):
        """
        IsInside(Point2d) -> bool
            
            Point2d point: 
            Input any 2D point
        IsInside(Point2d, Tolerance) -> bool
            
            Point2d point: 
            Input any 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(CircularArc2d) -> void
            
            CircularArc2d arc: 
            Input any 2D circular arc
        Set(Point2d, Vector2d, Vector2d, double, double) -> void
            
            Point2d center: 
            Input ellipse center
            
            Vector2d majorAxis: 
            Input ellipse major axis
            
            Vector2d minorAxis: 
            Input ellipse minor axis
            
            double majorRadius: 
            Input ellipse major radius
            
            double minorRadius: 
            Input ellipse minor radius
        Set(Point2d, Vector2d, Vector2d, double, double, double, double) -> void
            
            Point2d center: 
            Input ellipse center
            
            Vector2d majorAxis: 
            Input ellipse major axis
            
            Vector2d minorAxis: 
            Input ellipse minor axis
            
            double majorRadius: 
            Input ellipse major radius
            
            double minorRadius: 
            Input ellipse minor radius
            
            double startAngle: 
            Input angle of ellipse start point
            
            double endAngle: 
            Input angle of ellipse endpoint
        """
        pass
    
    
    def SetAngles(self):
        """
        SetAngles -> void
            
            double startAngle: 
            Input angle of ellipse startpoint
            
            double endAngle: 
            Input angle of ellipse endpoint
        """
        pass
    
    
    def SetAxes(self):
        """
        SetAxes -> void
            
            Vector2d majorAxis: 
            Input ellipse major axis
            
            Vector2d minorAxis: 
            Input ellipse minor axis
        """
        pass
    
    
    Center = None
    
    
    EndAngle = None
    
    
    EndPoint = None
    
    
    IsClockWise = None
    
    
    MajorAxis = None
    
    
    MajorRadius = None
    
    
    MinorAxis = None
    
    
    MinorRadius = None
    
    
    StartAngle = None
    
    
    StartPoint = None
    
    pass

class EllipticalArc3d(object):
    """
    
    EllipticalArc3d()()
    
    
    EllipticalArc3d(Point3d, Vector3d, Vector3d, double, double)
        Point3d center : Input ellipse center
        Vector3d majorAxis : Input ellipse major axis
        Vector3d minorAxis : Input ellipse minor axis
        double majorRadius : Input ellipse major radius
        double minorRadius : Input ellipse minor radius
    
    
    EllipticalArc3d(Point3d, Vector3d, Vector3d, double, double, double, double)
        Point3d center : Input ellipse center
        Vector3d majorAxis : Input ellipse major axis
        Vector3d minorAxis : Input ellipse minor axis
        double majorRadius : Input ellipse major radius
        double minorRadius : Input ellipse minor radius
        double startAngle : Input angle of ellipse start point
        double endAngle : Input angle of ellipse end point
    
    
    """
    def ClosestPointToPlane(self):
        """
        ClosestPointToPlane(PlanarEntity) -> Point3d()
            
            PlanarEntity plane: 
            Input plane
        ClosestPointToPlane(PlanarEntity, Tolerance) -> Point3d()
            
            PlanarEntity plane: 
            Input plane
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetPlane(self):
        """
        GetPlane -> Plane
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        IntersectWith(PlanarEntity) -> Point3d()
            
            PlanarEntity plane: 
            Input any plane
        IntersectWith(PlanarEntity, Tolerance) -> Point3d()
            
            PlanarEntity plane: 
            Input any plane
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsCircular(self):
        """
        IsCircular() -> bool
        
        IsCircular(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsInside(self):
        """
        IsInside(Point3d) -> bool
            
            Point3d pointValue: 
            Input any 3D point
        IsInside(Point3d, Tolerance) -> bool
            
            Point3d pointValue: 
            Input any 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def ProjectedIntersectWith(self):
        """
        ProjectedIntersectWith(LinearEntity3d, Vector3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Vector3d projectionDirection: 
            Input direction of projection
        ProjectedIntersectWith(LinearEntity3d, Vector3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Vector3d projectionDirection: 
            Input direction of projection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(Point3d, Vector3d, Vector3d, double, double) -> void
            
            Point3d center: 
            Input ellipse center
            
            Vector3d majorAxis: 
            Input ellipse major axis
            
            Vector3d minorAxis: 
            Input ellipse minor axis
            
            double majorRadius: 
            Input ellipse major radius
            
            double minorRadius: 
            Input ellipse minor radius
        Set(Point3d, Vector3d, Vector3d, double, double, double, double) -> void
            
            Point3d center: 
            Input ; ellipse center
            
            Vector3d majorAxis: 
            Input ellipse major axis
            
            Vector3d minorAxis: 
            Input ellipse minor axis
            
            double majorRadius: 
            Input ellipse major radius
            
            double minorRadius: 
            Input ellipse minor radius
            
            double startAngle: 
            Input angle of ellipse start point
            
            double endAngle: 
            Input angle of ellipse end point
        """
        pass
    
    
    def SetAngles(self):
        """
        SetAngles -> void
            
            double startAngle: 
            Input angle of ellipse start point
            
            double endAngle: 
            Input angle of ellipse end point
        """
        pass
    
    
    def SetAxes(self):
        """
        SetAxes -> void
            
            Vector3d majorAxis: 
            Input ellipse major axis
            
            Vector3d minorAxis: 
            Input ellipse minor axis
        """
        pass
    
    
    Center = None
    
    
    EndAngle = None
    
    
    EndPoint = None
    
    
    MajorAxis = None
    
    
    MajorRadius = None
    
    
    MinorAxis = None
    
    
    MinorRadius = None
    
    
    Normal = None
    
    
    StartAngle = None
    
    
    StartPoint = None
    
    pass

class Entity2d(object):
    """
    
    """
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Entity2d) -> bool
            
            Entity2d entity: 
            Input entity to check against
        IsEqualTo(Entity2d, Tolerance) -> bool
            
            Entity2d entity: 
            Input entity to check against
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn(Point2d) -> bool
            
            Point2d point: 
            Input 2D point
        IsOn(Point2d, Tolerance) -> bool
            
            Point2d point: 
            Input 2D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> void
            
            Line2d line: 
            Input 2D mirror line
        """
        pass
    
    
    def RotateBy(self):
        """
        RotateBy -> void
            
            double angle: 
            Input angle of rotation
            
            Point2d point: 
            Input point about which to rotate
        """
        pass
    
    
    def ScaleBy(self):
        """
        ScaleBy -> void
            
            double scaleFactor: 
            Input amount by which entity is to be scaled
            
            Point2d point: 
            Input point about which entity is to be scaled
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
            
            Matrix2d transform: 
            Input transformation matrix
        """
        pass
    
    
    def TranslateBy(self):
        """
        TranslateBy -> void
            
            Vector2d translateVector: 
            Input vector by which entity is to be translated
        """
        pass
    
    pass

class Entity3d(object):
    """
    
    """
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Entity3d) -> bool
            
            Entity3d entity: 
            Input entity to check against
        IsEqualTo(Entity3d, Tolerance) -> bool
            
            Entity3d entity: 
            Input 3D mirror line
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn(Point3d) -> bool
            
            Point3d point: 
            Input 3D point
        IsOn(Point3d, Tolerance) -> bool
            
            Point3d point: 
            Input 3D point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> void
            
            Plane plane: 
            Input 3D mirror line
        """
        pass
    
    
    def RotateBy(self):
        """
        RotateBy -> void
            
            double angle: 
            Input angle of rotation
            
            Vector3d vector: 
            Input vector about which entity is to be rotated
            
            Point3d point: 
            Input point about which to rotate
        """
        pass
    
    
    def ScaleBy(self):
        """
        ScaleBy -> void
            
            double scaleFactor: 
            Input amount by which entity is to be scaled
            
            Point3d point: 
            Input point about which entity is to be scaled
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> void
            
            Matrix3d transform: 
            Input transformation matrix
        """
        pass
    
    
    def TranslateBy(self):
        """
        TranslateBy -> void
            
            Vector3d translateVector: 
            Input vector by which entity is to be translated
        """
        pass
    
    pass

class ErrorCondition():
    OK = None
    This = None
    Arg1 = None
    Arg2 = None
    PerpendicularArg1Arg2 = None
    EqualArg1Arg2 = None
    EqualArg1Arg3 = None
    EqualArg2Arg3 = None
    LinearlyDependentArg1Arg2Arg3 = None
    Arg1TooBig = None
    Arg1OnThis = None
    Arg1InsideThis = None

class ExternalBoundedSurface(object):
    """
    
    ExternalBoundedSurface()()
    
    
    """
    def GetContours(self):
        """
        GetContours -> CurveBoundary()
        
        """
        pass
    
    
    def Set(self):
        """
        Set -> void
            
            IntPtr surfaceDef: 
            Input definition of the external bounded surface
            
            Autodesk.AutoCAD.Geometry.ExternalEntityKind surfaceKind: 
            Input information about the system in which the surface definition was created
        """
        pass
    
    
    def SetToOwnSurface(self):
        """
        SetToOwnSurface -> void
        
        """
        pass
    
    
    BaseSurface = None
    
    
    ExternalBaseSurface = None
    
    
    ExternalSurfaceDefinition = None
    
    
    ExternalSurfaceKind = None
    
    
    IsCone = None
    
    
    IsCylinder = None
    
    
    IsDefined = None
    
    
    IsExternalSurface = None
    
    
    IsNurbs = None
    
    
    IsOwnerOfSurface = None
    
    
    IsPlane = None
    
    
    IsSphere = None
    
    
    IsTorus = None
    
    
    NumContours = None
    
    pass

class ExternalCurve2d(object):
    """
    
    ExternalCurve2d()()
    
    
    """
    def Set(self):
        """
        Set -> void
            
            surfaceDef: 
            Input new definition for the external surface
            
            surfaceKind: 
            Input information concerning the system in which the surface definition was created
        """
        pass
    
    
    def SetToOwnCurve(self):
        """
        SetToOwnCurve -> void
        
        """
        pass
    
    
    ExternalCurve = None
    
    
    ExternalCurveKind = None
    
    
    IsDefined = None
    
    
    IsNurbCurve = None
    
    
    IsOwnerOfCurve = None
    
    
    NurbCurve = None
    
    pass

class ExternalCurve3d(object):
    """
    
    """
    ExternalCurveKind = None
    
    
    IsCircularArc = None
    
    
    IsDefined = None
    
    
    IsEllipticalArc = None
    
    
    IsLine = None
    
    
    IsLineSegment = None
    
    
    IsNativeCurve = None
    
    
    IsNurbCurve = None
    
    
    IsRay = None
    
    
    NativeCurve = None
    
    pass

class ExternalEntityKind():
    AcisEntity = None
    ExternalEntityUndefined = None

class ExternalSurface(object):
    """
    
    ExternalSurface()()
    
    
    """
    def Set(self):
        """
        Set -> void
            
            IntPtr surfaceDef: 
            Input definition of the external bounded surface
            
            Autodesk.AutoCAD.Geometry.ExternalEntityKind surfaceKind: 
            Input information about the system in which the surface definition was created
        """
        pass
    
    
    def SetToOwnSurface(self):
        """
        SetToOwnSurface -> void
        
        """
        pass
    
    
    ExternalSurfaceDefiniton = None
    
    
    ExternalSurfaceKind = None
    
    
    IsCone = None
    
    
    IsCylinder = None
    
    
    IsDefined = None
    
    
    IsNativeSurface = None
    
    
    IsNurbSurface = None
    
    
    IsOwnerOfSurface = None
    
    
    IsPlane = None
    
    
    IsSphere = None
    
    
    IsTorus = None
    
    
    nativeSurface = None
    
    pass

class Interval(object):
    """
    
    Interval(Interval)
        Interval other : Input the interval to be copied into this object
    
    
    Interval([MarshalAs(UnmanagedType.U1)] bool, double, double)
        [MarshalAs(UnmanagedType.U1)] bool boundedBelow : Whether to set a lower bound or leave interval unbounded below
        double bound : Upper or lower bound
        double tolerance : Input tolerance value
    
    
    Interval(double)
        double tolerance : Input tolerance value
    
    
    Interval(double, double, double)
        double lower : Lower bound
        double upper : Upper bound
        double tolerance : Input tolerance value
    
    
    """
    def Contains(self):
        """
        Contains(Interval) -> bool
            
            Interval otherInterval: 
            Input interval against which to test
        Contains(double) -> bool
            
            double value: 
            Input value
        """
        pass
    
    
    def GetBounds(self):
        """
        GetBounds -> double()
        
        """
        pass
    
    
    def GetMerge(self):
        """
        GetMerge -> Interval
            
            Interval otherInterval: 
            Input interval with which to merge
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith -> Interval
            
            Interval otherInterval: 
            Input interval with which to merge
        """
        pass
    
    
    def IsContinuousAtUpper(self):
        """
        IsContinuousAtUpper -> bool
            
            Interval otherInterval: 
            Input terval against which to test
        """
        pass
    
    
    def IsDisjoint(self):
        """
        IsDisjoint -> bool
            
            Interval otherInterval: 
            Input terval against which to test
        """
        pass
    
    
    def IsEqualAtLower(self):
        """
        IsEqualAtLower(Interval) -> bool
            
            Interval otherInterval: 
            Input value against which to test
        IsEqualAtLower(double) -> bool
            
            double value: 
            Input value against which to test
        """
        pass
    
    
    def IsEqualAtUpper(self):
        """
        IsEqualAtUpper(Interval) -> bool
            
            Interval otherInterval: 
            Input value against which to test
        IsEqualAtUpper(double) -> bool
            
            double value: 
            Input value against which to test
        """
        pass
    
    
    def IsOverlapAtUpper(self):
        """
        IsOverlapAtUpper -> bool
            
            Interval otherInterval: 
            Input interval against which to test
            
            Interval overlap: 
            Output intersection interval, if true
        """
        pass
    
    
    def IsPeriodicallyOn(self):
        """
        IsPeriodicallyOn -> bool
            
            double period: 
            Input period length
            
            out double value: 
            Output System.Double object; Output value, if True
        """
        pass
    
    
    def Subtract(self):
        """
        Subtract -> Interval()
            
            Interval otherInterval: 
            Input interval with which to merge
        """
        pass
    
    
    Element = None
    
    
    IsBounded = None
    
    
    IsBoundedAbove = None
    
    
    IsBoundedBelow = None
    
    
    IsSingleton = None
    
    
    IsUnbounded = None
    
    
    Length = None
    
    
    LowerBound = None
    
    
    Tolerance = None
    
    
    Unbounded = None
    
    
    UpperBound = None
    
    pass

class KnotCollection(object):
    """
    
    KnotCollection()
    """
    def Add(self):
        """
        Add -> Integer
            
            double value: 
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
            
            double value: 
            Input value to check existence of
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            double[] array: 
            Input array to copy to
            
            int index: 
            Input index to begin copying at
        """
        pass
    
    
    def GetDistinctKnots(self):
        """
        GetDistinctKnots -> DoubleCollection
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator
        
        """
        pass
    
    
    def GetInterval(self):
        """
        GetInterval -> Integer
            
            int order: 
            Input order of a spline
            
            double parameter: 
            Input parameter
            
            out Interval interval: 
            Output containing knot interval
        """
        pass
    
    
    def GetMultiplicityAt(self):
        """
        GetMultiplicityAt -> Integer
            
            int i: 
            Input index
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            double value: 
            Input value to insert
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn -> bool
            
            double knot: 
            Input value
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index of item to remove
        """
        pass
    
    
    def Reverse(self):
        """
        Reverse -> void
        
        """
        pass
    
    
    def SetRange(self):
        """
        SetRange -> void
            
            double lower: 
            Input new lower knot
            
            double upper: 
            Input new upper knot
        """
        pass
    
    
    def Split(self):
        """
        Split -> KnotCollection()
            
            double parameter: 
            Input split parameter
            
            int multiplicityLast: 
            Input multiplicity of the last knot in the head fraction.
            
            int multiplicityFirst: 
            Input multiplicity of the first knot in the tail fraction
        """
        pass
    
    
    Count = None
    
    
    EndParameter = None
    
    
    NumberOfIntervals = None
    
    
    StartParameter = None
    
    
    Tolerance = None
    
    pass

class KnotParameterization():
    Chord = 0
    CustomParameterization = 15
    NotDefinedParameterization = 0x10
    SqrtChord = 1
    Uniform = 2

class Line2d(object):
    """
    
    Line2d()()
    
    
    Line2d(Point2d, Point2d)
        Point2d point1 : Input any 2D point
        Point2d point2 : Input any 2D point different from point1
    
    
    Line2d(Point2d, Vector2d)
        Point2d point : Input any 2D point
        Vector2d vector : Input any 2D vector
    
    
    """
    def Set(self):
        """
        Set(Point2d, Point2d) -> void
            
            Point2d point1: 
            Input any 2D point
            
            Point2d point2: 
            Input any 2D point different from point1
        Set(Point2d, Vector2d) -> void
            
            Point2d point: 
            Input any 2D point
            
            Vector2d vector: 
            Input any 2D vector
        """
        pass
    
    pass

class Line2dCollection(object):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            Line2d value: 
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
            
            Line2d value: 
            Input value to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Line2d[] array: 
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
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Line2d value: 
            Input value to retrieve index of
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            Line2d value: 
            Input item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            Line2d value: 
            Input value to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index of value to be removed
        """
        pass
    
    
    Count = None
    
    pass

class Line3d(object):
    """
    
    Line3d()()
    
    
    Line3d(Point3d, Point3d)
        Point3d point1 : Input any 3D point
        Point3d point2 : Input any 3D point different from point1
    
    
    Line3d(Point3d, Vector3d)
        Point3d point : Input any 3D point
        Vector3d vector : Input any 3D vector
    
    
    """
    def Set(self):
        """
        Set(Point3d, Point3d) -> void
            
            Point3d point1: 
            Input any 3D point
            
            Point3d point2: 
            Input any 3D point different from point1
        Set(Point3d, Vector3d) -> void
            
            Point3d point: 
            Input any 3D point
            
            Vector3d vector: 
            Input any 3D vector
        """
        pass
    
    pass

class LineSegment2d(object):
    """
    
    LineSegment2d()()
    
    
    LineSegment2d(Point2d, Point2d)
        Point2d point1 : Input start point of line segment
        Point2d point2 : Input end point of line segment
    
    
    LineSegment2d(Point2d, Vector2d)
        Point2d point : Input start point of line segment
        Vector2d vector : Input vector between endpoint and start point of line segment
    
    
    """
    def BaryComb(self):
        """
        BaryComb -> Point2d
            
            double blendCoefficient: 
            Input any real number
        """
        pass
    
    
    def GetBisector(self):
        """
        GetBisector -> Line2d
        
        """
        pass
    
    
    def GetSegmentLength(self):
        """
        GetSegmentLength(double, double) -> double
            
            double fromParameter: 
            Input start point parameter
            
            double toParameter: 
            Input end point parameter
        GetSegmentLength(double, double, Tolerance) -> double
            
            double fromParameter: 
            Input start point parameter
            
            double toParameter: 
            Input end point parameter
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        """
        pass
    
    
    def Set(self):
        """
        Set(Curve2d, Curve2d, double, double) -> void
            
            Curve2d curve1: 
            Input any 2D curve
            
            Curve2d curve2: 
            Input any 2D curve
            
            double parameter1: 
            Input point on curve1 where line segment is tangent to curve
            
            double parameter2: 
            Input point on curve2 where line segment is tangent to curve
        Set(Curve2d, Point2d, double) -> void
            
            Curve2d curve: 
            Input any 2D curve
            
            Point2d point: 
            Input any 2D point
            
            double parameter: 
            Input point on curve where line segment is tangent to curve
        Set(Point2d, Point2d) -> void
            
            Point2d point1: 
            Input start point of line segment
            
            Point2d point2: 
            Input end point of line segment
        Set(Point2d, Vector2d) -> void
            
            Point2d point: 
            Input start point of line segment
            
            Vector2d vector: 
            Input vector between endpoint and start point of line segment
        """
        pass
    
    
    EndPoint = None
    
    
    Length = None
    
    
    MidPoint = None
    
    
    StartPoint = None
    
    pass

class LineSegment3d(object):
    """
    
    LineSegment3d()()
    
    
    LineSegment3d(Point3d, Point3d)
        Point3d point1 : Input start point of line segment
        Point3d point2 : Input end point of line segment
    
    
    LineSegment3d(Point3d, Vector3d)
        Point3d point : Input start point of line segment
        Vector3d vector : Input vector between endpoint and start point of line segment
    
    
    """
    def BaryComb(self):
        """
        BaryComb -> Point3d
            
            double blendCoefficient: 
            Input y real number
        """
        pass
    
    
    def GetBisector(self):
        """
        GetBisector -> Plane
        
        """
        pass
    
    
    def Set(self):
        """
        Set(Curve3d, Curve3d, double, double) -> void
            
            Curve3d curve1: 
            Input any 3D curve
            
            Curve3d curve2: 
            Input any 3D curve
            
            double parameter1: 
            Input point on curve1 where line segment is tangent to curve
            
            double parameter2: 
            Input point on curve2 where line segment is tangent to curve
        Set(Curve3d, Point3d, double) -> void
            
            Curve3d curve: 
            Input any 3D curve
            
            Point3d point: 
            Input any 3D point
            
            double parameter: 
            Input point on curve where line segment is tangent to curve
        Set(Point3d, Point3d) -> void
            
            Point3d point1: 
            Input start point of line segment
            
            Point3d point2: 
            Input end point of line segment
        Set(Point3d, Vector3d) -> void
            
            Point3d point: 
            Input start point of line segment
            
            Vector3d vector: 
            Input vector between endpoint and start point of line segment
        """
        pass
    
    
    EndPoint = None
    
    
    Length = None
    
    
    MidPoint = None
    
    
    StartPoint = None
    
    pass

class LinearEntity2d(object):
    """
    
    """
    def GetLine(self):
        """
        GetLine -> Line2d
        
        """
        pass
    
    
    def GetPerpendicularLine(self):
        """
        GetPerpendicularLine -> Line2d
            
            Point2d point: 
            Input any 2D point
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity2d) -> Point2d()
            
            LinearEntity2d line: 
            Input any 2D linear entity
        IntersectWith(LinearEntity2d, Tolerance) -> Point2d()
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsColinearTo(self):
        """
        IsColinearTo(LinearEntity2d) -> bool
            
            LinearEntity2d line: 
            Input any 2D linear entity
        IsColinearTo(LinearEntity2d, Tolerance) -> bool
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsParallelTo(self):
        """
        IsParallelTo(LinearEntity2d) -> bool
            
            LinearEntity2d line: 
            Input any 2D linear entity
        IsParallelTo(LinearEntity2d, Tolerance) -> bool
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPerpendicularTo(self):
        """
        IsPerpendicularTo(LinearEntity2d) -> bool
            
            LinearEntity2d line: 
            Input any 2D linear entity
        IsPerpendicularTo(LinearEntity2d, Tolerance) -> bool
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Overlap(self):
        """
        Overlap(LinearEntity2d) -> LinearEntity2d
            
            LinearEntity2d line: 
            Input any 2D linear entityDetermines if two lines overlap and if so returns the line that coincides with their region of overlap. The returned overlap line may be an object of any derived class of LinearEnt2d, depending on the types of the two lines.This method calls LinearEnt2d.Overlap(LinearEntity2d line, Tolerance tolerance) with tolerance set to Global.
        Overlap(LinearEntity2d, Tolerance) -> LinearEntity2d
            
            LinearEntity2d line: 
            Input any 2D linear entity
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        """
        pass
    
    
    Direction = None
    
    
    PointOnLine = None
    
    pass

class LinearEntity3d(object):
    """
    
    """
    def GetLine(self):
        """
        GetLine -> Line3d
        
        """
        pass
    
    
    def GetPerpendicularPlane(self):
        """
        GetPerpendicularPlane -> Plane
            
            Point3d intersectionPoint: 
            Input any 3D point
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        IntersectWith(PlanarEntity) -> Point3d()
            
            PlanarEntity plane: 
            Input any planar entity
        IntersectWith(PlanarEntity, Tolerance) -> Point3d()
            
            PlanarEntity plane: 
            Input any planar entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsColinearTo(self):
        """
        IsColinearTo(LinearEntity3d) -> bool
            
            LinearEntity3d line: 
            Input any 3D linear entity
        IsColinearTo(LinearEntity3d, Tolerance) -> bool
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn(Plane) -> bool
            
            Plane plane: 
            Input any plane
        IsOn(Plane, Tolerance) -> bool
            
            Plane plane: 
            Input any plane
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsParallelTo(self):
        """
        IsParallelTo(LinearEntity3d) -> bool
            
            LinearEntity3d line: 
            Input any 3D linear entity
        IsParallelTo(LinearEntity3d, Tolerance) -> bool
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        IsParallelTo(PlanarEntity) -> bool
            
            PlanarEntity plane: 
            Input any planar entity
        IsParallelTo(PlanarEntity, Tolerance) -> bool
            
            PlanarEntity plane: 
            Input any planar entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPerpendicularTo(self):
        """
        IsPerpendicularTo(LinearEntity3d) -> bool
            
            LinearEntity3d line: 
            Input any 3D linear entity
        IsPerpendicularTo(LinearEntity3d, Tolerance) -> bool
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        IsPerpendicularTo(PlanarEntity) -> bool
            
            PlanarEntity plane: 
            Input any planar entity
        IsPerpendicularTo(PlanarEntity, Tolerance) -> bool
            
            PlanarEntity plane: 
            Input any planar entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Overlap(self):
        """
        Overlap(LinearEntity3d) -> LinearEntity3d
            
            LinearEntity3d line: 
            Input any 3D linear entity
        Overlap(LinearEntity3d, Tolerance) -> LinearEntity3d
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def ProjectedIntersectWith(self):
        """
        ProjectedIntersectWith(LinearEntity3d, Vector3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Vector3d projectionDirection: 
            Input direction of projection
        ProjectedIntersectWith(LinearEntity3d, Vector3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any 3D linear entity
            
            Vector3d projectionDirection: 
            Input direction of projection
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        """
        pass
    
    
    Direction = None
    
    
    PointOnLine = None
    
    pass

class Matrix2d(object):
    """
    
    Matrix2d
        array : Input matrix array
    """
    def AlignCoordinateSystem(self):
        """
        AlignCoordinateSystem -> Matrix2d
            
            Point2d fromOrigin: 
            Input point that defines the origin of the from coordinate system
            
            Vector2d fromE0: 
            Input vector that defines the x axis of the from coordinate system
            
            Vector2d fromE1: 
            Input vector that defines the y axis of the from coordinate system
            
            Point2d toOrigin: 
            Input point that defines the origin of the to coordinate system
            
            Vector2d toE0: 
            Input vector that defines the x axis of the to coordinate system
            
            Vector2d toE1: 
            Input vector that defines the y axis of the to coordinate system
        """
        pass
    
    
    def Displacement(self):
        """
        Displacement -> Matrix2d
            
            Vector2d vector: 
            Input vector to calculate displacement from
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetDeterminant(self):
        """
        GetDeterminant -> double
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetScale(self):
        """
        GetScale -> double
        
        """
        pass
    
    
    def Inverse(self):
        """
        Inverse -> Matrix2d
        
        """
        pass
    
    
    def IsConformal(self):
        """
        IsConformal -> bool
            
            Matrix2dInfo info: 
            Input matrix to check with
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Matrix2d) -> bool
            
            Matrix2d a: 
            Input matrix to compare against
        IsEqualTo(Matrix2d, Tolerance) -> bool
            
            Matrix2d a: 
            Input matrix to compare against
            
            Tolerance tolerance: 
            Input tolerance data value
        """
        pass
    
    
    def IsScaledOrtho(self):
        """
        IsScaledOrtho() -> bool
        
        IsScaledOrtho(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance data value
        """
        pass
    
    
    def IsSingular(self):
        """
        IsSingular() -> bool
        
        IsSingular(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance data value
        """
        pass
    
    
    def IsUniscaledOrtho(self):
        """
        IsUniscaledOrtho() -> bool
        
        IsUniscaledOrtho(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance data value
        """
        pass
    
    
    def Mirroring(self):
        """
        Mirroring(Line2d) -> Matrix2d
            
            Line2d line: 
            Input the mirror line
        Mirroring(Point2d) -> Matrix2d
            
            Point2d point: 
            Input point that defines the mirror line
        """
        pass
    
    
    def Multiply(self):
        """
        Multiply -> Matrix2d
            
            Matrix2d matrix: 
            Input matrix to multiply
        """
        pass
    
    
    def PostMultiplyBy(self):
        """
        PostMultiplyBy -> Matrix2d
            
            Matrix2d rightSide: 
            Input right side of matrix
        """
        pass
    
    
    def PreMultiplyBy(self):
        """
        PreMultiplyBy -> Matrix2d
            
            Matrix2d leftSide: 
            Input left side of matrix
        """
        pass
    
    
    def Rotation(self):
        """
        Rotation -> Matrix2d
            
            double angle: 
            Input rotation angle
            
            Point2d center: 
            Input center of rotation
        """
        pass
    
    
    def Scaling(self):
        """
        Scaling -> Matrix2d
            
            double scaleAll: 
            Input scale factor
            
            Point2d center: 
            Input origin of the scale
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    def Transpose(self):
        """
        Transpose -> Matrix2d
        
        """
        pass
    
    
    CoordinateSystem2d = None
    
    
    Translation = None
    
    pass

class Matrix2dBuilder(object):
    """
    
    Matrix2dBuilder()()
    
    
    Matrix2dBuilder(Matrix2d)
        Matrix2d value : Input matrix
    
    
    """
    def ToMatrix2d(self):
        """
        ToMatrix2d -> Matrix2d
        
        """
        pass
    
    pass

class Matrix2dInfo(object):
    """
    
    """
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
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Matrix2dInfo) -> bool
            
            Matrix2dInfo a: 
            Input object to check against
        IsEqualTo(Matrix2dInfo, Tolerance) -> bool
            
            Matrix2dInfo a: 
            Input object to check against
            
            Tolerance tolerance: 
            Input tolerance value
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
    
    
    Angle = None
    
    
    IsMirror = None
    
    
    Reflex = None
    
    
    Scale = None
    
    pass

class Matrix3d(object):
    """
    
    Matrix3d
        double[] data : Input matrix array
    """
    def AlignCoordinateSystem(self):
        """
        AlignCoordinateSystem -> Matrix3d
            
            Point3d fromOrigin: 
            Input origin point of the from coordinate system
            
            Vector3d fromXAxis: 
            Input vector defining the x axis of the from coordinate system
            
            Vector3d fromYAxis: 
            Input vector defining the y axis of the from coordinate system
            
            Vector3d fromZAxis: 
            Input vector defining the z axis of the from coordinate system
            
            Point3d toOrigin: 
            Input origin point of the to coordinate system
            
            Vector3d toXAxis: 
            Input vector defining the x axis of the to coordinate system
            
            Vector3d toYAxis: 
            Input vector defining the y axis of the to coordinate system
            
            Vector3d toZAxis: 
            Input vector defining the z axis of the to coordinate system
        """
        pass
    
    
    def Displacement(self):
        """
        Displacement -> Matrix3d
            
            Vector3d vector: 
            Input vector to calculate displacement from
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetDeterminant(self):
        """
        GetDeterminant -> double
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetScale(self):
        """
        GetScale -> double
        
        """
        pass
    
    
    def Inverse(self):
        """
        Inverse -> Matrix3d
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Matrix3d) -> bool
            
            Matrix3d mat: 
            Input matrix to compare against
        IsEqualTo(Matrix3d, Tolerance) -> bool
            
            Matrix3d mat: 
            Input matrix to compare against
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsInverse(self):
        """
        IsInverse(Matrix3d) -> bool
            
            Matrix3d inv: 
            Input inverse matrix
        IsInverse(Matrix3d, Tolerance) -> bool
            
            Matrix3d inv: 
            Input inverse matrix
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsScaledOrtho(self):
        """
        IsScaledOrtho() -> bool
        
        IsScaledOrtho(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsSingular(self):
        """
        IsSingular() -> bool
        
        IsSingular(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsUniscaledOrtho(self):
        """
        IsUniscaledOrtho() -> bool
        
        IsUniscaledOrtho(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirroring(self):
        """
        Mirroring(Line3d) -> Matrix3d
            
            Line3d line: 
            Input line of symmetry
        Mirroring(Plane) -> Matrix3d
            
            Plane plane: 
            Input mirror plane
        Mirroring(Point3d) -> Matrix3d
            
            Point3d pointValue: 
            Input point of symmetry
        """
        pass
    
    
    def PlaneToWorld(self):
        """
        PlaneToWorld(Plane) -> Matrix3d
            
            Plane plane: 
            Input transformation plane
        PlaneToWorld(Vector3d) -> Matrix3d
            
            Vector3d normal: 
            Input normal to the plane for transformation
        """
        pass
    
    
    def PostMultiplyBy(self):
        """
        PostMultiplyBy -> Matrix3d
            
            Matrix3d rightSide: 
            Input right side of matrix
        """
        pass
    
    
    def PreMultiplyBy(self):
        """
        PreMultiplyBy -> Matrix3d
            
            Matrix3d leftSide: 
            Input left side of matrix
        """
        pass
    
    
    def Projection(self):
        """
        Projection -> Matrix3d
            
            Plane projectionPlane: 
            Input projection plane
            
            Vector3d projectDir: 
            Input projection direction
        """
        pass
    
    
    def Rotation(self):
        """
        Rotation -> Matrix3d
            
            double angle: 
            Input angle of rotation
            
            Vector3d axis: 
            Input axis of rotation
            
            Point3d center: 
            Input origin point of rotation
        """
        pass
    
    
    def Scaling(self):
        """
        Scaling -> Matrix3d
            
            double scaleAll: 
            Input scale factor
            
            Point3d center: 
            Input origin point of the scale
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    def Transpose(self):
        """
        Transpose -> Matrix3d
        
        """
        pass
    
    
    def WorldToPlane(self):
        """
        WorldToPlane(Plane) -> Matrix3d
            
            Plane plane: 
            Input transformation plane.
        WorldToPlane(Vector3d) -> Matrix3d
            
            Vector3d normal: 
            Input normal vector to the plane
        """
        pass
    
    
    CoordinateSystem3d = None
    
    
    Identity = None
    
    
    Normal = None
    
    
    Translation = None
    
    pass

class Matrix3dBuilder(object):
    """
    
    Matrix3dBuilder()()
    
    
    Matrix3dBuilder(Matrix3d)
        Matrix3d value : Input matrix
    
    
    """
    def ToMatrix3d(self):
        """
        ToMatrix3d -> Matrix3d
        
        """
        pass
    
    pass

class NurbCurve2d(object):
    """
    
    NurbCurve2d()()
    
    
    NurbCurve2d(EllipticalArc2d)
        EllipticalArc2d ellipse : Input elliptic arc
    
    
    NurbCurve2d(LineSegment2d)
        LineSegment2d linSegment : Input line segment
    
    
    NurbCurve2d(Point2dCollection)
        Point2dCollection fitPoints : Input points interpolating the spline curve
    
    
    NurbCurve2d(Point2dCollection, Tolerance)
        Point2dCollection fitPoints : Input points interpolating the spline curve
        Tolerance fitTolerance : Input maximal deviation of the curve from the fitPoints
    
    
    NurbCurve2d(Point2dCollection, Vector2d, Vector2d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, KnotParameterizationEnum)()
    
    
    NurbCurve2d(Point2dCollection, Vector2d, Vector2d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, KnotParameterizationEnum, Tolerance)()
    
    
    NurbCurve2d(int, KnotCollection, Point2dCollection, DoubleCollection, [MarshalAs(UnmanagedType.U1)] bool)
        int degree : Input the degree of the spline.
        KnotCollection knots : Input an array of knot values, partitioning the spline's domain into rational pieces.
        Point2dCollection controlPoints : Input an array of 2D control points.
        DoubleCollection weights : Input an array of weight values.
        [MarshalAs(UnmanagedType.U1)] bool periodic : Input a flag indicating whether the spline is a periodic.
    
    
    NurbCurve2d(int, KnotCollection, Point2dCollection, [MarshalAs(UnmanagedType.U1)] bool)()
    
    
    """
    def AddControlPointAt(self):
        """
        AddControlPointAt -> void
        
        """
        pass
    
    
    def AddFitPointAt(self):
        """
        AddFitPointAt -> bool
            
            int index: 
            Input index of fit point that is to be added
            
            Point2d point: 
            Input new fit point
        """
        pass
    
    
    def AddKnot(self):
        """
        AddKnot -> void
            
            double newKnot: 
            Input new knot value to be inserted into the knot vector of the spline
        """
        pass
    
    
    def DeleteControlPointAt(self):
        """
        DeleteControlPointAt -> void
        
        """
        pass
    
    
    def DeleteFitPointAt(self):
        """
        DeleteFitPointAt -> bool
            
            int index: 
            Input index of fit point that is to be deleted
        """
        pass
    
    
    def ElevateDegree(self):
        """
        ElevateDegree -> void
            
            int plusDegree: 
            Input amount by which degree is to be increased
        """
        pass
    
    
    def GetFitPointAt(self):
        """
        GetFitPointAt -> Point2d
            
            int index: 
            Input index of fit point
        """
        pass
    
    
    def GetFitTangents(self):
        """
        GetFitTangents -> Vector2d()
        
        """
        pass
    
    
    def GetParametersOfC1Discontinuity(self):
        """
        GetParametersOfC1Discontinuity() -> DoubleCollection
        
        GetParametersOfC1Discontinuity(Tolerance) -> DoubleCollection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetParametersOfG1Discontinuity(self):
        """
        GetParametersOfG1Discontinuity() -> DoubleCollection
        
        GetParametersOfG1Discontinuity(Tolerance) -> DoubleCollection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetWeightAt(self):
        """
        GetWeightAt -> double
            
            int index: 
            Input index to weights
        """
        pass
    
    
    def HardTrimByParams(self):
        """
        HardTrimByParams -> void
            
            double newStartParameter: 
            Input new start parameter of spline
            
            double newEndParameter: 
            Input new end parameter of spline
        """
        pass
    
    
    def InsertKnot(self):
        """
        InsertKnot -> void
            
            double newKnot: 
            Input new knot value to be inserted into the knot vector of the spline
        """
        pass
    
    
    def JoinWith(self):
        """
        JoinWith -> void
            
            NurbCurve2d curve: 
            Input spline to be joined with this spline
        """
        pass
    
    
    def MakeClosed(self):
        """
        MakeClosed -> void
        
        """
        pass
    
    
    def MakeNonPeriodic(self):
        """
        MakeNonPeriodic -> void
        
        """
        pass
    
    
    def MakeOpen(self):
        """
        MakeOpen -> void
        
        """
        pass
    
    
    def MakePeriodic(self):
        """
        MakePeriodic -> void
        
        """
        pass
    
    
    def MakeRational(self):
        """
        MakeRational -> void
            
            double weight: 
            Input weight to be assigned to each control point
        """
        pass
    
    
    def PurgeFitData(self):
        """
        PurgeFitData -> bool
        
        """
        pass
    
    
    def SetEvaluateMode(self):
        """
        SetEvaluateMode -> void
            
            [MarshalAs(UnmanagedType.U1)] bool evaluateMode: 
            Input state of the evaluation mode
        """
        pass
    
    
    def SetFitData(self):
        """
        SetFitData(KnotCollection, Point2dCollection, Vector2d, Vector2d, Tolerance, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            KnotCollection fitKnots: 
            Input new knot values
            
            Point2dCollection fitPoints: 
            Input new fit points
            
            Vector2d startTangent: 
            Input new start tangent vector
            
            Vector2d endTangent: 
            Input new end tangent vector
            
            Tolerance fitTolerance: 
            Input tolerance to which spline will fit the interpolation points
            
            [MarshalAs(UnmanagedType.U1)] bool periodic: 
            Input indicating whether spline should be made periodic
        SetFitData(KnotCollection, Point2dCollection, Vector2d, Vector2d, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            KnotCollection fitKnots: 
            Input new knot values
            
            Point2dCollection fitPoints: 
            Input new fit points
            
            Vector2d startTangent: 
            Input new start tangent vector
            
            Vector2d endTangent: 
            Input new end tangent vector
            
            [MarshalAs(UnmanagedType.U1)] bool periodic: 
            Input indicating whether spline should be made
        SetFitData(Point2dCollection, Vector2d, Vector2d) -> void
            
            Point2dCollection fitPoints: 
            Input new fit points
            
            Vector2d startTangent: 
            Input new start tangent vector
            
            Vector2d endTangent: 
            Input new end tangent vector
        SetFitData(Point2dCollection, Vector2d, Vector2d, KnotParameterizationEnum, Tolerance) -> void
        
        SetFitData(Point2dCollection, Vector2d, Vector2d, Tolerance) -> void
            
            Point2dCollection fitPoints: 
            Input new fit points
            
            Vector2d startTangent: 
            Input new start tangent
            
            Vector2d endTangent: 
            Input new end tangent
            
            Tolerance fitTolerance: 
            Input tolerance to which spline will fit the interpolation points
        SetFitData(int, Point2dCollection) -> void
            
            int degree: 
            Input new degree of spline
            
            Point2dCollection fitPoints: 
            Input new fit points
        SetFitData(int, Point2dCollection, Tolerance) -> void
            
            int degree: 
            Input new degree of spline
            
            Point2dCollection fitPoints: 
            Input new fit points
            
            Tolerance fitTolerance: 
            Input tolerance to which spline will fit the interpolation points
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> bool
            
            int index: 
            Input index of fit point that is to be modified
            
            Point2d point: 
            Input new fit point
        """
        pass
    
    
    def SetFitTangents(self):
        """
        SetFitTangents -> bool
            
            Vector2d startTangent: 
            Input new start tangent vector
            
            Vector2d endTangent: 
            Input new end tangent vector
        """
        pass
    
    
    def SetWeightAt(self):
        """
        SetWeightAt -> void
            
            int index: 
            Input index of control point
            
            double value: 
            Input new weight to be assigned to control point
        """
        pass
    
    
    DefinitionData = None
    
    
    EvalMode = None
    
    
    FitData = None
    
    
    FitKnotParameterization = None
    
    
    FitTolerance = None
    
    
    NumFitPoints = None
    
    
    NumWeights = None
    
    pass

class NurbCurve2dData(object):
    """
    
    """
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
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            NurbCurve2dData a: 
            Input object to check with
        """
        pass
    
    
    ControlPoints = None
    
    
    Degree = None
    
    
    Knots = None
    
    
    Periodic = None
    
    
    Rational = None
    
    
    Weights = None
    
    pass

class NurbCurve2dFitData(object):
    """
    
    """
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
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            NurbCurve2dFitData a: 
            Input object to check against
        """
        pass
    
    
    Degree = None
    
    
    EndTangent = None
    
    
    FitPoints = None
    
    
    FitTolerance = None
    
    
    StartTangent = None
    
    
    TangentsExist = None
    
    pass

class NurbCurve3d(object):
    """
    
    NurbCurve3d()()
    
    
    NurbCurve3d(EllipticalArc3d)
        EllipticalArc3d ellipse : Input elliptic arc
    
    
    NurbCurve3d(LineSegment3d)
        linSegment : Input line segment
    
    
    NurbCurve3d(Point3dCollection)
        Point3dCollection fitPoints : Input points interpolating the spline curve
    
    
    NurbCurve3d(Point3dCollection, Tolerance)
        Point3dCollection fitPoints : Input points interpolating the spline curve
        Tolerance fitTolerance : Input maximal deviation of the curve from the fitPoints
    
    
    NurbCurve3d(Point3dCollection, Vector3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, KnotParameterizationEnum)()
    
    
    NurbCurve3d(Point3dCollection, Vector3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool, [MarshalAs(UnmanagedType.U1)] bool, KnotParameterizationEnum, Tolerance)()
    
    
    NurbCurve3d(int, KnotCollection, Point3dCollection, DoubleCollection, [MarshalAs(UnmanagedType.U1)] bool)
        int degree : Input the degree of spline.
        KnotCollection knots : Input an array of knot values, partitioning the spline's domain into rational pieces.
        Point3dCollection controlPoints : Input an array of 3d control points.
        DoubleCollection weights : Input an array of weight values.
        [MarshalAs(UnmanagedType.U1)] bool periodic : Input a flag indicating whether the spline is a periodic.
    
    
    NurbCurve3d(int, KnotCollection, Point3dCollection, [MarshalAs(UnmanagedType.U1)] bool)()
    
    
    """
    def AddControlPointAt(self):
        """
        AddControlPointAt -> void
        
        """
        pass
    
    
    def AddFitPointAt(self):
        """
        AddFitPointAt -> bool
            
            int index: 
            Input index of fit point that is to be added
            
            Point3d point: 
            Input new fit point
        """
        pass
    
    
    def AddKnot(self):
        """
        AddKnot -> void
            
            double newKnot: 
            Input new knot value to be inserted into the knot vector of the spline
        """
        pass
    
    
    def DeleteControlPointAt(self):
        """
        DeleteControlPointAt -> void
        
        """
        pass
    
    
    def DeleteFitPointAt(self):
        """
        DeleteFitPointAt -> bool
            
            int index: 
            Input index of fit point that is to be deleted
        """
        pass
    
    
    def ElevateDegree(self):
        """
        ElevateDegree -> void
            
            int plusDegree: 
            Input amount by which degree is to be increased
        """
        pass
    
    
    def GetFitPointAt(self):
        """
        GetFitPointAt -> Point3d
            
            int index: 
            Input index of fit point
        """
        pass
    
    
    def GetFitTangents(self):
        """
        GetFitTangents -> Vector3d()
        
        """
        pass
    
    
    def GetParametersOfC1Discontinuity(self):
        """
        GetParametersOfC1Discontinuity() -> DoubleCollection
        
        GetParametersOfC1Discontinuity(Tolerance) -> DoubleCollection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetParametersOfG1Discontinuity(self):
        """
        GetParametersOfG1Discontinuity() -> DoubleCollection
        
        GetParametersOfG1Discontinuity(Tolerance) -> DoubleCollection
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetWeightAt(self):
        """
        GetWeightAt -> double
            
            int index: 
            Input index of control point
        """
        pass
    
    
    def HardTrimByParams(self):
        """
        HardTrimByParams -> void
            
            double newStartParameter: 
            Input new start parameter of spline
            
            double newEndParameter: 
            Input new end parameter of spline
        """
        pass
    
    
    def InsertKnot(self):
        """
        InsertKnot -> void
            
            double newKnot: 
            Input new knot value to be inserted into the knot vector of the spline
        """
        pass
    
    
    def JoinWith(self):
        """
        JoinWith -> void
            
            NurbCurve3d curve: 
            Input spline to be joined with this spline
        """
        pass
    
    
    def MakeClosed(self):
        """
        MakeClosed -> void
        
        """
        pass
    
    
    def MakeNonPeriodic(self):
        """
        MakeNonPeriodic -> void
        
        """
        pass
    
    
    def MakeOpen(self):
        """
        MakeOpen -> void
        
        """
        pass
    
    
    def MakePeriodic(self):
        """
        MakePeriodic -> void
        
        """
        pass
    
    
    def MakeRational(self):
        """
        MakeRational -> void
            
            double weight: 
            Input weight to be assigned to each control point
        """
        pass
    
    
    def PurgeFitData(self):
        """
        PurgeFitData -> bool
        
        """
        pass
    
    
    def SetEvaluateMode(self):
        """
        SetEvaluateMode -> void
            
            [MarshalAs(UnmanagedType.U1)] bool evaluateMode: 
            Input state of the evaluation mode
        """
        pass
    
    
    def SetFitData(self):
        """
        SetFitData(KnotCollection, Point3dCollection, Vector3d, Vector3d, Tolerance, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            KnotCollection fitKnots: 
            Input new knot values
            
            Point3dCollection fitPoints: 
            Input new fit points
            
            Vector3d startTangent: 
            Input new start tangent vector
            
            Vector3d endTangent: 
            Input new end tangent vector
            
            Tolerance fitTolerance: 
            Input tolerance to which spline will fit the interpolation points
            
            [MarshalAs(UnmanagedType.U1)] bool periodic: 
            Input indicating whether spline should be made periodic
        SetFitData(KnotCollection, Point3dCollection, Vector3d, Vector3d, [MarshalAs(UnmanagedType.U1)] bool) -> void
            
            KnotCollection fitKnots: 
            Input new knot values
            
            Point3dCollection fitPoints: 
            Input new fit points
            
            Vector3d startTangent: 
            Input new start tangent vector
            
            Vector3d endTangent: 
            Input new end tangent vector
            
            [MarshalAs(UnmanagedType.U1)] bool periodic: 
            Input indicating whether spline should be made periodic
        SetFitData(Point3dCollection, Vector3d, Vector3d) -> void
            
            Point3dCollection fitPoints: 
            Input new fit points
            
            Vector3d startTangent: 
            Input new start tangent vector
            
            Vector3d endTangent: 
            Input new end tangent vector
        SetFitData(Point3dCollection, Vector3d, Vector3d, KnotParameterizationEnum, Tolerance) -> void
        
        SetFitData(Point3dCollection, Vector3d, Vector3d, Tolerance) -> void
            
            Point3dCollection fitPoints: 
            Input new knot values
            
            Vector3d startTangent: 
            Input new start tangent vector
            
            Vector3d endTangent: 
            Input new end tangent vector
            
            Tolerance fitTolerance: 
            Input tolerance to which spline will fit the interpolation points
        SetFitData(int, Point3dCollection) -> void
            
            int degree: 
            Input new degree of spline
            
            Point3dCollection fitPoints: 
            Input new knot values
        SetFitData(int, Point3dCollection, Tolerance) -> void
            
            int degree: 
            Input new degree of spline
            
            Point3dCollection fitPoints: 
            Input new knot values
            
            Tolerance fitTolerance: 
            Input tolerance to which spline will fit the interpolation points
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> bool
            
            int index: 
            Input index of fit point that is to be modified
            
            Point3d point: 
            Input new fit point
        """
        pass
    
    
    def SetFitTangents(self):
        """
        SetFitTangents -> bool
            
            Vector3d startTangent: 
            Input new start tangent vector
            
            Vector3d endTangent: 
            Input new end tangent vector
        """
        pass
    
    
    def SetWeightAt(self):
        """
        SetWeightAt -> void
            
            int index: 
            Input index of control point
            
            double value: 
            Input new weight to be assigned to control point
        """
        pass
    
    
    DefinitionData = None
    
    
    EvalMode = None
    
    
    FitData = None
    
    
    FitKnotParameterization = None
    
    
    FitTolerance = None
    
    
    NumFitPoints = None
    
    
    NumWeights = None
    
    pass

class NurbCurve3dData(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            NurbCurve3dData a: 
            Input object to compare against
        """
        pass
    
    
    ControlPoints = None
    
    
    Degree = None
    
    
    Knots = None
    
    
    Periodic = None
    
    
    Rational = None
    
    
    Weights = None
    
    pass

class NurbCurve3dFitData(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            NurbCurve3dFitData a: 
            Input object to compare against
        """
        pass
    
    
    Degree = None
    
    
    EndTangent = None
    
    
    FitPoints = None
    
    
    FitTolerance = None
    
    
    StartTangent = None
    
    
    TangentsExist = None
    
    pass

class NurbSurface(object):
    """
    
    NurbSurface()()
    
    
    NurbSurface(int, int, int, int, int, int, Point3dCollection, DoubleCollection, KnotCollection, KnotCollection)
        int degreeU : Input U degree
        int degreeV : Input V degree
        int propsInU : Input U properties (uses NurbSurfaceProperties values)
        int propertiesInV : Input V properties (uses NurbSurfaceProperties values)
        int numberControlPointsInU : Input number of control points in U direction
        int numberControlPointsInV : Input number of control points in V direction
        Point3dCollection controlPoints : Input collection of control points
        DoubleCollection weights : Input collection of weights
        KnotCollection knotsInU : Input U collection of knots
        KnotCollection knotsInV : Input V collection of knots
    
    
    NurbSurface(int, int, int, int, int, int, Point3dCollection, DoubleCollection, KnotCollection, KnotCollection, Tolerance)
        int degreeU : Input U degree
        int degreeV : Input V degree
        int propsInU : Input U properties (uses NurbSurfaceProperties values)
        int propertiesInV : Input V properties (uses NurbSurfaceProperties values)
        int numberControlPointsInU : Input number of control points in U direction
        int numberControlPointsInV : Input number of control points in V direction
        Point3dCollection controlPoints : Input array of control points
        DoubleCollection weights : Input array of weights
        KnotCollection knotsInU : Input U array of knots
        KnotCollection knotsInV : Input V array of knots
        Tolerance tolerance : Input tolerance value
    
    
    """
    def GetDefinition(self):
        """
        GetDefinition -> NurbSurfaceDefinition
        
        """
        pass
    
    
    def Set(self):
        """
        Set(int, int, int, int, int, int, Point3dCollection, DoubleCollection, KnotCollection, KnotCollection) -> void
            
            int degreeU: 
            Input U degree
            
            int degreeV: 
            Input V degree
            
            int propsInU: 
            Input U properties (uses NurbSurfaceProperties values)
            
            int propsInV: 
            Input V properties (uses NurbSurfaceProperties values)
            
            int numControlPointsInU: 
            Input number of control points in U direction
            
            int numControlPointsInV: 
            Input number of control points in V direction
            
            Point3dCollection controlPoints: 
            Input array of control points
            
            DoubleCollection weights: 
            Input array of weights
            
            KnotCollection knotsInU: 
            Input U array of knots
            
            KnotCollection knotsInV: 
            Input U array of knots
        Set(int, int, int, int, int, int, Point3dCollection, DoubleCollection, KnotCollection, KnotCollection, Tolerance) -> void
            
            int degreeU: 
            Input U degree
            
            int degreeV: 
            Input V degree
            
            int propsInU: 
            Input U properties (uses NurbSurfaceProperties values)
            
            int propsInV: 
            Input V properties (uses NurbSurfaceProperties values)
            
            int numControlPointsInU: 
            Input number of control points in U directio
            
            int numControlPointsInV: 
            Input number of control points in V direction
            
            Point3dCollection controlPoints: 
            Input array of control points
            
            DoubleCollection weights: 
            Input array of weights
            
            KnotCollection knotsInU: 
            Input U array of knots
            
            KnotCollection knotsInV: 
            Input U array of knots
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    ControlPoints = None
    
    
    DegreeInU = None
    
    
    DegreeInV = None
    
    
    IsPeriodicInU = None
    
    
    IsPeriodicInV = None
    
    
    IsRationalInU = None
    
    
    IsRationalInV = None
    
    
    NumControlPointsInU = None
    
    
    NumControlPointsInV = None
    
    
    NumKnotsInU = None
    
    
    NumKnotsInV = None
    
    
    PeriodicInU = None
    
    
    PeriodicInV = None
    
    
    SingularityInU = None
    
    
    SingularityInV = None
    
    
    UKnots = None
    
    
    VKnots = None
    
    
    Weights = None
    
    pass

class NurbSurfaceDefinition(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            NurbSurfaceDefinition a: 
            Input object to compare against
        """
        pass
    
    
    ControlPoints = None
    
    
    DegreeInU = None
    
    
    DegreeInV = None
    
    
    NumberOfControlPointsInU = None
    
    
    NumberOfControlPointsInV = None
    
    
    PropertiesInU = None
    
    
    PropertiesInV = None
    
    
    UKnots = None
    
    
    VKnots = None
    
    
    Weights = None
    
    pass

class OffsetCurve2d(object):
    """
    
    OffsetCurve2d
        Curve2d baseCurve : Input base curve
        double offsetDistance : Input offset distance
    """
    Curve = None
    
    
    OffsetDistance = None
    
    
    ParameterDirection = None
    
    
    Transformation = None
    
    pass

class OffsetCurve3d(object):
    """
    
    OffsetCurve3d
        Curve3d baseCurve : Input base curve
        Vector3d planeNormal : Input plane normal
        double offsetDistance : Input offset distance
    """
    Curve = None
    
    
    Normal = None
    
    
    OffsetDistance = None
    
    
    ParameterDirection = None
    
    
    Transformation = None
    
    pass

class OffsetCurveExtensionType():
    Fillet = None
    Chamfer = None
    Extend = None

class OffsetSurface(object):
    """
    
    OffsetSurface()()
    
    
    OffsetSurface(Surface, double)
        Surface baseSurface : Input base surface
        double offsetDistance : Input offset distance
    
    
    """
    def Set(self):
        """
        Set -> void
            
            Surface surface: 
            Input base surface
            
            double offsetDistance: 
            Input offset distance
        """
        pass
    
    
    ConstructionSurface = None
    
    
    IsBoundedPlane = None
    
    
    IsCone = None
    
    
    IsCylinder = None
    
    
    IsPlane = None
    
    
    IsSphere = None
    
    
    IsTorus = None
    
    
    OffsetDist = None
    
    
    OriginalSurface = None
    
    pass

class PlanarEntity(object):
    """
    
    """
    def ClosestPointToLinearEntity(self):
        """
        ClosestPointToLinearEntity(LinearEntity3d) -> Point3d()
            
            LinearEntity3d line: 
            Input any LinearEntity3d object
        ClosestPointToLinearEntity(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d line: 
            Input any LinearEntity3d object
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def ClosestPointToPlanarEntity(self):
        """
        ClosestPointToPlanarEntity(PlanarEntity) -> Point3d()
            
            PlanarEntity otherPlane: 
            Input any PlanarEntity object
        ClosestPointToPlanarEntity(PlanarEntity, Tolerance) -> Point3d()
            
            PlanarEntity otherPlane: 
            Input any PlanarEntity object
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetCoordinateSystem(self):
        """
        GetCoordinateSystem -> CoordinateSystem3d
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsCoplanarTo(self):
        """
        IsCoplanarTo(PlanarEntity) -> bool
            
            PlanarEntity otherPlanarEntity: 
            Input other planar entity
        IsCoplanarTo(PlanarEntity, Tolerance) -> bool
            
            PlanarEntity otherPlanarEntity: 
            Input other planar entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsParallelTo(self):
        """
        IsParallelTo(LinearEntity3d) -> bool
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IsParallelTo(LinearEntity3d, Tolerance) -> bool
            
            LinearEntity3d linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance valueDetermines if line is parallel to input plane.
        IsParallelTo(PlanarEntity) -> bool
            
            PlanarEntity otherPlanarEntity: 
            Input other planar entity
        IsParallelTo(PlanarEntity, Tolerance) -> bool
            
            PlanarEntity otherPlanarEntity: 
            Input other planar entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPerpendicularTo(self):
        """
        IsPerpendicularTo(LinearEntity3d) -> bool
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IsPerpendicularTo(LinearEntity3d, Tolerance) -> bool
            
            LinearEntity3d linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        IsPerpendicularTo(PlanarEntity) -> bool
            
            PlanarEntity linearEntity: 
            Input linear entity
        IsPerpendicularTo(PlanarEntity, Tolerance) -> bool
            
            PlanarEntity linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    Coefficients = None
    
    
    Normal = None
    
    
    PointOnPlane = None
    
    pass

class PlanarEquationCoefficients(object):
    """
    
    PlanarEquationCoefficients
        double a : Input.
        double b : Input.
        double c : Input.
        double d : Input.
    """
    A = None
    
    
    B = None
    
    
    C = None
    
    
    D = None
    
    pass

class Plane(object):
    """
    
    Plane()()
    
    
    Plane(Plane)
        Plane source : Another plane
    
    
    Plane(Point3d, Point3d, Point3d)
        Point3d u : Input point U on U axis
        Point3d origin : Input origin
        Point3d v : Input point V on V axis
    
    
    Plane(Point3d, Vector3d)
        Point3d origin : Input origin of plane
        Vector3d normal : Input normal vector
    
    
    Plane(Point3d, Vector3d, Vector3d)
        Point3d origin : Input origin
        Vector3d u : Input point U on U axis
        Vector3d v : Input point V on V axis
    
    
    Plane(double, double, double, double)
        double a : Input coordinate a
        double b : Input coordinate b
        double c : Input coordinate c
        double d : Input coordinate d
    
    
    """
    def GetSignedDistanceTo(self):
        """
        GetSignedDistanceTo -> double
            
            Point3d pointValue: 
            Input point
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(BoundedPlane) -> LineSegment3d
            
            BoundedPlane boundPlane: 
            Input bounded plane
        IntersectWith(BoundedPlane, Tolerance) -> LineSegment3d
            
            BoundedPlane boundPlane: 
            Input bounded plane
            
            Tolerance tolerance: 
            Input tolerance value
        IntersectWith(Plane) -> Line3d
            
            Plane otherPlane: 
            Input other plane
        IntersectWith(Plane, Tolerance) -> Line3d
            
            Plane otherPlane: 
            Input other plane
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(Point3d, Point3d, Point3d) -> void
            
            Point3d u: 
            Input point U
            
            Point3d origin: 
            Input origin
            
            Point3d v: 
            Input point V
        Set(Point3d, Vector3d) -> void
            
            Point3d pointValue: 
            Input origin point
            
            Vector3d normal: 
            Input vector normal
        Set(Point3d, Vector3d, Vector3d) -> void
            
            Point3d origin: 
            Input origin
            
            Vector3d u: 
            Input point u
            
            Vector3d v: 
            Input point v
        Set(double, double, double, double) -> void
            
            double a: 
            Input coordinate a
            
            double b: 
            Input coordinate b
            
            double c: 
            Input coordinate c
            
            double d: 
            Input coordinate d
        """
        pass
    
    pass

class Point2d(object):
    """
    
    Point2d(double, double)()
    
    
    Point2d(double[])
        double[] xy : Input coordinate array
    
    
    """
    def Add(self):
        """
        Add -> Point2d
            
            Vector2d value: 
            Input object to be added.
        """
        pass
    
    
    def DivideBy(self):
        """
        DivideBy -> Point2d
            
            double value: 
            Input for dividing the 2D point.
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetAsVector(self):
        """
        GetAsVector -> Vector2d
        
        """
        pass
    
    
    def GetDistanceTo(self):
        """
        GetDistanceTo -> double
            
            Point2d point: 
            Input point to measure to
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetVectorTo(self):
        """
        GetVectorTo -> Vector2d
            
            Point2d point: 
            Input point to measure to
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Point2d) -> bool
            
            Point2d a: 
            Input object to check against
        IsEqualTo(Point2d, Tolerance) -> bool
            
            Point2d a: 
            Input object to check against
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> Point2d
            
            Line2d line: 
            Input line of symmetry
        """
        pass
    
    
    def MultiplyBy(self):
        """
        MultiplyBy -> Point2d
            
            double value: 
            Input object to be multiplied with the 2D point.
        """
        pass
    
    
    def RotateBy(self):
        """
        RotateBy -> Point2d
            
            double angle: 
            Input rotation angle
            
            Point2d origin: 
            Input center of rotation
        """
        pass
    
    
    def ScaleBy(self):
        """
        ScaleBy -> Point2d
            
            double scaleFactor: 
            Input scale factor
            
            Point2d origin: 
            Input center of scaling
        """
        pass
    
    
    def Subtract(self):
        """
        Subtract -> Point2d
            
            Vector2d value: 
            Input value to subtract.
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> Point2d
            
            Matrix2d leftSide: 
            Input left side of the matrix
        """
        pass
    
    
    Origin = None
    
    
    X = None
    
    
    Y = None
    
    pass

class Point3d(object):
    """
    
    Point3d(PlanarEntity, Point2d)
        PlanarEntity plane : Input plane
        Point2d point : Input 2D point
    
    
    Point3d(double, double, double)()
    
    
    Point3d(double[])
        double[] xyz : Input array of coordinates
    
    
    """
    def Add(self):
        """
        Add -> Point3d
            
            Vector3d value: 
            Input object to be added.
        """
        pass
    
    
    def Convert2d(self):
        """
        Convert2d -> Point2d
            
            PlanarEntity plane: 
            Input plane
        """
        pass
    
    
    def DistanceTo(self):
        """
        DistanceTo -> double
            
            Point3d point: 
            Input point to measure to
        """
        pass
    
    
    def DivideBy(self):
        """
        DivideBy -> Point3d
            
            double value: 
            Input for dividing the 3D point.
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetAsVector(self):
        """
        GetAsVector -> Vector3d
        
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetVectorTo(self):
        """
        GetVectorTo -> Vector3d
            
            Point3d point: 
            Input point to measure to
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Point3d) -> bool
            
            Point3d point: 
            Input object to check against
        IsEqualTo(Point3d, Tolerance) -> bool
            
            Point3d point: 
            Input object to check against
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> Point3d
            
            Plane plane: 
            Input line of symmetry
        """
        pass
    
    
    def MultiplyBy(self):
        """
        MultiplyBy -> Point3d
            
            double value: 
            Input object to be multiplied with the 3D point
        """
        pass
    
    
    def OrthoProject(self):
        """
        OrthoProject -> Point3d
            
            Plane plane: 
            Input plane
        """
        pass
    
    
    def Project(self):
        """
        Project -> Point3d
            
            Plane plane: 
            Input plane
            
            Vector3d vector: 
            Input vector Input axis of rotation
            
            angle: 
            Input rotation angle
            
            centerPoint: 
            Input center of rotation
        """
        pass
    
    
    def RotateBy(self):
        """
        RotateBy -> Point3d
            
            double angle: 
            Input angle of rotation
            
            Vector3d vector: 
            Input vector about which entity is to be rotated
            
            Point3d centerPoint: 
            Input point about which to rotate
        """
        pass
    
    
    def ScaleBy(self):
        """
        ScaleBy -> Point3d
            
            double scaleFactor: 
            Input scale factor
            
            Point3d centerPoint: 
            Input center of scaling
        """
        pass
    
    
    def Subtract(self):
        """
        Subtract -> Point3d
            
            Vector3d value: 
            Input object to be subtracted from the 3D point.
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> Point3d
            
            Matrix3d leftSide: 
            Input transform matrix
        """
        pass
    
    
    Origin = None
    
    
    X = None
    
    
    Y = None
    
    
    Z = None
    
    pass

class Point3dCollection(object):
    """
    
    Point3dCollection()()
    
    
    Point3dCollection(Point3d[])
        Point3d[] values : Input array
    
    
    """
    def Add(self):
        """
        Add -> Integer
            
            Point3d value: 
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
            
            Point3d value: 
            Input object to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Point3d[] array: 
            Input array to copy into
            
            int index: 
            Input index to begin copying
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
            
            Point3d value: 
            Input index of object
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input index to insert at
            
            Point3d value: 
            Input object to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            Point3d value: 
            Input object to remove
        """
        pass
    
    
    def RemoveAt(self):
        """
        RemoveAt -> void
            
            int index: 
            Input index of object to remove at
        """
        pass
    
    
    Count = None
    
    pass

class PointEntity2d(object):
    """
    
    """
    Point = None
    
    pass

class PointEntity3d(object):
    """
    
    """
    def GetPoint(self):
        """
        GetPoint -> Point3d
        
        """
        pass
    
    pass

class PointOnCurve2d(object):
    """
    
    PointOnCurve2d()()
    
    
    PointOnCurve2d(Curve2d)
        src : Input any 2D curve
    
    
    PointOnCurve2d(Curve2d, double)
        Curve2d curve : Input any 2D curve
        double parameter : Input parameter value on curve
    
    
    """
    def GetDerivative(self):
        """
        GetDerivative(int) -> Vector2d
            
            int order: 
            Input order of derivative
        GetDerivative(int, Curve2d, double) -> Vector2d
            
            int order: 
            Input order of derivative
            
            Curve2d curve: 
            Input any 2D curve
            
            double parameter: 
            Input parameter value on curve
        GetDerivative(int, double) -> Vector2d
            
            int order: 
            Input order of derivative
            
            double parameter: 
            Input parameter value on curve
        """
        pass
    
    
    def GetPointAtParameter(self):
        """
        GetPointAtParameter -> Point2d
            
            double parameter: 
            Input parameter value
        """
        pass
    
    
    def GetPointOnCurve(self):
        """
        GetPointOnCurve -> Point2d
            
            Curve2d curve: 
            Input any 2D curve
            
            double parameter: 
            Input parameter value
        """
        pass
    
    
    Curve = None
    
    
    Parameter = None
    
    
    Point = None
    
    pass

class PointOnCurve3d(object):
    """
    
    PointOnCurve3d()()
    
    
    PointOnCurve3d(Curve3d, double)
        Curve3d curve : Input any 3D curve
        double parameter : Input parameter value on curve
    
    
    """
    def GetCurvature(self):
        """
        GetCurvature() -> double
        
        GetCurvature(double) -> double
            
            double parameter: 
            Input parameter value on curve
        """
        pass
    
    
    def GetDerivative(self):
        """
        GetDerivative(int) -> Vector3d
            
            int order: 
            Input order of derivative
        GetDerivative(int, Curve3d, double) -> Vector3d
            
            int order: 
            Input order of derivative
            
            Curve3d curve: 
            Input any 3D curve
            
            double parameter: 
            Input parameter value on curve
        GetDerivative(int, double) -> Vector3d
            
            int order: 
            Input order of derivative
            
            double parameter: 
            Input parameter value on curve
        """
        pass
    
    
    def GetPointAtParameter(self):
        """
        GetPointAtParameter -> Point3d
            
            double parameter: 
            Input parameter value
        """
        pass
    
    
    def GetPointOnCurve(self):
        """
        GetPointOnCurve -> Point3d
            
            Curve3d curve: 
            Input any 3D curve
            
            double parameter: 
            Input parameter value
        """
        pass
    
    
    def IsSingular(self):
        """
        IsSingular() -> bool
        
        IsSingular(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
        """
        pass
    
    
    Curve = None
    
    
    Parameter = None
    
    
    Point = None
    
    pass

class PointOnSurface(object):
    """
    
    PointOnSurface()()
    
    
    """
    def GetInverseTangentVector(self):
        """
        GetInverseTangentVector(Vector3d) -> Vector2d
            
            Vector3d vector: 
            Input any 3D vector
        GetInverseTangentVector(Vector3d, Autodesk.AutoCAD.Geometry.Surface, Point2d) -> Vector2d
            
            Vector3d vector: 
            Input any 3D vector
            
            Autodesk.AutoCAD.Geometry.Surface surf: 
            Input any surface
            
            Point2d point: 
            Input parameter value
        GetInverseTangentVector(Vector3d, Point2d) -> Vector2d
            
            Vector3d vector: 
            Input any 3D vector
            
            Point2d point: 
            Input any 2D point
        """
        pass
    
    
    def GetMixedPartial(self):
        """
        GetMixedPartial() -> Vector3d
        
        GetMixedPartial(Point2d) -> Vector3d
            
            Point2d point: 
            Input parameter value
        """
        pass
    
    
    def GetNormal(self):
        """
        GetNormal() -> Vector3d
        
        GetNormal(Point2d) -> Vector3d
            
            Point2d point: 
            Input parameter value
        """
        pass
    
    
    def GetPoint(self):
        """
        GetPoint(Autodesk.AutoCAD.Geometry.Surface, Point2d) -> Point3d
            
            Autodesk.AutoCAD.Geometry.Surface surface: 
            Input any surface
            
            Point2d point: 
            Input parameter value
        GetPoint(Point2d) -> Point3d
            
            Point2d point: 
            Input parameter value
        """
        pass
    
    
    def GetTangentVector(self):
        """
        GetTangentVector(Vector2d) -> Vector3d
            
            Vector2d vector: 
            Input any 2D vector
        GetTangentVector(Vector2d, Autodesk.AutoCAD.Geometry.Surface, Point2d) -> Vector3d
            
            Vector2d vector: 
            Input any 2D vector
            
            Autodesk.AutoCAD.Geometry.Surface vectorSurface: 
            Input any surface
            
            Point2d pointer: 
            Input Autodesk.AutoCAD.Geometry.Point2d object.; parameter value
        GetTangentVector(Vector2d, Point2d) -> Vector3d
            
            Vector2d vector: 
            Input any 2D vector
            
            Point2d point: 
            Input parameter value
        """
        pass
    
    
    def GetUDerivative(self):
        """
        GetUDerivative(int) -> Vector3d
        
        GetUDerivative(int, Autodesk.AutoCAD.Geometry.Surface, Point2d) -> Vector3d
            
            int order: 
            Input order of derivative
            
            Autodesk.AutoCAD.Geometry.Surface surface: 
            Input any surface
            
            Point2d point: 
            Input parameter value
        GetUDerivative(int, Point2d) -> Vector3d
            
            int order: 
            Input order of derivative
            
            Point2d point: 
            Input parameter value
        """
        pass
    
    
    def GetVDerivative(self):
        """
        GetVDerivative(int) -> Vector3d
            
            int order: 
            Input order of derivative
        GetVDerivative(int, Autodesk.AutoCAD.Geometry.Surface, Point2d) -> Vector3d
            
            int order: 
            Input order of derivative
            
            Autodesk.AutoCAD.Geometry.Surface surface: 
            Input any surface
            
            Point2d point: 
            Input parameter value
        GetVDerivative(int, Point2d) -> Vector3d
            
            int order: 
            Input order of derivative
            
            Point2d point: 
            Input parameter value
        """
        pass
    
    
    Parameter = None
    
    
    Surface = None
    
    pass

class PolylineCurve2d(object):
    """
    
    PolylineCurve2d()()
    
    
    PolylineCurve2d(Curve2d, double)
        Curve2d curve : Input curve to be approximated by polyline
        double epsilon : Input approximation epsilon
    
    
    PolylineCurve2d(KnotCollection, Point2dCollection)
        KnotCollection knots : Input knot vectors
        Point2dCollection controlPoints : Input collection of fit points
    
    
    PolylineCurve2d(Point2dCollection)
        Point2dCollection points : Input collection of fit points
    
    
    """
    def FitPointAt(self):
        """
        FitPointAt -> Point2d
            
            int i: 
            Input index of a fit point
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> void
            
            int i: 
            Input index of a fit point
            
            Point2d point: 
            Input fit point
        """
        pass
    
    
    NumberOfFitPoints = None
    
    pass

class PolylineCurve3d(object):
    """
    
    PolylineCurve3d()()
    
    
    PolylineCurve3d(Curve3d, double)
        Curve3d curve : Input curve to be approximated by polyline
        double epsilon : Input approximation epsilon
    
    
    PolylineCurve3d(KnotCollection, Point3dCollection)
        KnotCollection knots : Input knot vectors
        Point3dCollection controlPoints : Input collection of fit points
    
    
    PolylineCurve3d(Point3dCollection)
        Point3dCollection points : Input collection of fit points
    
    
    """
    def FitPointAt(self):
        """
        FitPointAt -> Point3d
            
            int i: 
            Input index of a fit point
        """
        pass
    
    
    def SetFitPointAt(self):
        """
        SetFitPointAt -> void
            
            int i: 
            Input index of a fit point
            
            Point3d point: 
            Input fit point
        """
        pass
    
    
    NumberOfFitPoints = None
    
    pass

class Position2d(object):
    """
    
    Position2d()()
    
    
    Position2d(Point2d)
        Point2d point : Input any 2D point object
    
    
    Position2d(double, double)()
    
    
    """
    def Set(self):
        """
        Set(Point2d) -> void
            
            Point2d point: 
            Input any 2D point
        Set(double, double) -> void
            
            double y: 
            _nt_
        """
        pass
    
    pass

class Position3d(object):
    """
    
    Position3d()()
    
    
    Position3d(Point3d)
        Point3d point : Input any 3D point object
    
    
    Position3d(double, double, double)()
    
    
    """
    def Set(self):
        """
        Set(Point3d) -> void
            
            Point3d point: 
            Input any 3D point
        Set(double, double, double) -> void
        
        """
        pass
    
    pass

class Ray2d(object):
    """
    
    Ray2d()()
    
    
    Ray2d(Point2d, Point2d)
        Point2d point1 : Input start point of ray
        Point2d point2 : Input any 2D point different from point1
    
    
    Ray2d(Point2d, Vector2d)
        Point2d point : Input start point of ray
        Vector2d vector : Input direction vector of ray
    
    
    """
    def Set(self):
        """
        Set(Point2d, Point2d) -> void
            
            Point2d point1: 
            Input start point of ray
            
            Point2d point2: 
            Input any 2D point different from point1
        Set(Point2d, Vector2d) -> void
            
            Point2d point: 
            Input start point of ray
            
            Vector2d vector: 
            Input direction vector of ray
        """
        pass
    
    pass

class Ray3d(object):
    """
    
    Ray3d()()
    
    
    Ray3d(Point3d, Point3d)
        Point3d point1 : Input start point of ray
        Point3d point2 : Input any 3D point different from point1
    
    
    Ray3d(Point3d, Vector3d)
        Point3d point : Input start point of ray
        Vector3d vector : Input direction vector of ray
    
    
    """
    def Set(self):
        """
        Set(Point3d, Point3d) -> void
            
            Point3d point1: 
            Input any 3D point
            
            Point3d point2: 
            Input any 3D point different from point1
        Set(Point3d, Vector3d) -> void
            
            Point3d point: 
            Input start point of ray
            
            Vector3d vector: 
            Input direction vector of ray
        """
        pass
    
    pass

class Scale2d(object):
    """
    
    Scale2d(double)
        double factor : Input uniform scale factor
    
    
    Scale2d(double, double)()
    
    
    Scale2d(double[])
        double[] xy : Input array
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def ExtractScale(self):
        """
        ExtractScale -> Scale2d
            
            Matrix2d mat: 
            Input matrix
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetMatrix(self):
        """
        GetMatrix -> Matrix2d
        
        """
        pass
    
    
    def Inverse(self):
        """
        Inverse -> Scale2d
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Scale2d) -> bool
            
            Scale2d a: 
            Input scale vector to test equality for
        IsEqualTo(Scale2d, Tolerance) -> bool
            
            Scale2d a: 
            Input scale vector to test equality for
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsProportional(self):
        """
        IsProportional() -> bool
        
        IsProportional(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def MultiplyBy(self):
        """
        MultiplyBy -> Scale2d
            
            double factor: 
            Input scale factor
        """
        pass
    
    
    def PostMultiplyBy(self):
        """
        PostMultiplyBy -> Scale2d
            
            Scale2d rightSide: 
            Input scale vector
        """
        pass
    
    
    def PreMultiplyBy(self):
        """
        PreMultiplyBy -> Scale2d
            
            Scale2d leftSide: 
            Input scale vector
        """
        pass
    
    
    def RemoveScale(self):
        """
        RemoveScale -> Scale2d
            
            Matrix2d mat: 
            Input matrix
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double[]
        
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
    
    
    X = None
    
    
    Y = None
    
    pass

class Scale3d(object):
    """
    
    Scale3d(double)
        double factor : Input uniform scale factor
    
    
    Scale3d(double, double, double)()
    
    
    Scale3d(double[])
        double[] xyz : Input array
    
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def ExtractScale(self):
        """
        ExtractScale -> Scale3d
            
            Matrix3d mat: 
            Input matrix
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetMatrix(self):
        """
        GetMatrix -> Matrix3d
        
        """
        pass
    
    
    def Inverse(self):
        """
        Inverse -> Scale3d
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Scale3d) -> bool
            
            scale: 
            Input scale vector to test equality for
        IsEqualTo(Scale3d, Tolerance) -> bool
            
            Scale3d scaleVector: 
            Input scale vector to test equality for
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsProportional(self):
        """
        IsProportional() -> bool
        
        IsProportional(Tolerance) -> bool
        
        """
        pass
    
    
    def MultiplyBy(self):
        """
        MultiplyBy -> Scale3d
            
            double s: 
            Input scale factor
        """
        pass
    
    
    def PostMultiplyBy(self):
        """
        PostMultiplyBy -> Scale3d
            
            Scale3d rightSide: 
            Input scale vector
        """
        pass
    
    
    def PreMultiplyBy(self):
        """
        PreMultiplyBy -> Scale3d
            
            Scale3d leftSide: 
            Input scale vector
        """
        pass
    
    
    def RemoveScale(self):
        """
        RemoveScale -> Scale3d
            
            Matrix3d mat: 
            Input matrix
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double[]
        
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
    
    
    X = None
    
    
    Y = None
    
    
    Z = None
    
    pass

class Sphere(object):
    """
    
    Sphere()()
    
    
    Sphere(double, Point3d)
        double radius : Input radius
        Point3d center : Input center
    
    
    Sphere(double, Point3d, Vector3d, Vector3d, double, double, double, double)
        double radius : Input radius for the sphere
        Point3d center : Input center point for the sphere
        Vector3d northAxis : Input direction to the north pole
        Vector3d referenceAxis : Input direction to the zero meridian
        double startAngleU : Input start longitude
        double endAngleU : Input end longitude
        double startAngleV : Input start latitude
        double endAngleV : Input end latitude
    
    
    """
    def GetAnglesInU(self):
        """
        GetAnglesInU -> double()
        
        """
        pass
    
    
    def GetAnglesInV(self):
        """
        GetAnglesInV -> double()
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input liner entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsClosed(self):
        """
        IsClosed() -> bool
        
        IsClosed(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(double, Point3d) -> void
            
            double radius: 
            Input radius of sphere
            
            Point3d center: 
            Input center of sphere
        Set(double, Point3d, Vector3d, Vector3d, double, double, double, double) -> void
            
            double radius: 
            Input radius of sphere
            
            Point3d center: 
            Input center of sphere
            
            Vector3d northAxis: 
            Input axis of sphere
            
            Vector3d referenceAxis: 
            Input reference axis
            
            double startAngleU: 
            Input start longitude
            
            double endAngleU: 
            Input end longitude
            
            double startAngleV: 
            Input start latitude
            
            double endAngleV: 
            Input end latitude
        """
        pass
    
    
    def SetAnglesInU(self):
        """
        SetAnglesInU -> void
            
            double startAngle: 
            Input start longitude
            
            double endAngle: 
            Input end longitude
        """
        pass
    
    
    def SetAnglesInV(self):
        """
        SetAnglesInV -> void
            
            double startAngle: 
            Input start latitude
            
            double endAngle: 
            Input end latitude
        """
        pass
    
    
    Center = None
    
    
    IsOuterNormal = None
    
    
    NorthAxis = None
    
    
    NorthPole = None
    
    
    Radius = None
    
    
    ReferenceAxis = None
    
    
    SouthPole = None
    
    pass

class SplineEntity2d(object):
    """
    
    """
    def GetContinuityAtKnot(self):
        """
        GetContinuityAtKnot(int) -> Integer
            
            int index: 
            Input knot index
        GetContinuityAtKnot(int, Tolerance) -> Integer
            
            int index: 
            Input knot index
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetControlPointAt(self):
        """
        GetControlPointAt -> Point2d
            
            int index: 
            Input index of a control point
        """
        pass
    
    
    def GetKnotAt(self):
        """
        GetKnotAt -> double
            
            int index: 
            Input index of a knot
        """
        pass
    
    
    def SetControlPointAt(self):
        """
        SetControlPointAt -> void
            
            int index: 
            Input index of a control point in the control array
            
            Point2d point: 
            Input value of the point
        """
        pass
    
    
    def SetKnotAt(self):
        """
        SetKnotAt -> void
            
            int index: 
            Input index of knot
            
            double value: 
            Input value of knot
        """
        pass
    
    
    Degree = None
    
    
    EndParameter = None
    
    
    EndPoint = None
    
    
    HasFitData = None
    
    
    IsRational = None
    
    
    Knots = None
    
    
    NumControlPoints = None
    
    
    NumKnots = None
    
    
    Order = None
    
    
    StartParameter = None
    
    
    StartPoint = None
    
    pass

class SplineEntity3d(object):
    """
    
    """
    def ControlPointAt(self):
        """
        ControlPointAt -> Point3d
            
            int i: 
            index of a control point
        """
        pass
    
    
    def GetContinuityAtKnot(self):
        """
        GetContinuityAtKnot(int) -> Integer
            
            int i: 
            Input knot index
        GetContinuityAtKnot(int, Tolerance) -> Integer
            
            Tolerance tolerance: 
            Input Autodesk.AutoCAD.Geometry.Tolerance object.
            
            index: 
            Input knot index
        """
        pass
    
    
    def KnotAt(self):
        """
        KnotAt -> double
            
            int i: 
            Input index of a knot
        """
        pass
    
    
    def SetControlPointAt(self):
        """
        SetControlPointAt -> void
            
            int i: 
            Input index of a control point in the control array
            
            Point3d point: 
            Input value of the point
        """
        pass
    
    
    def SetKnotAt(self):
        """
        SetKnotAt -> void
            
            int i: 
            Input index of knot
            
            double value: 
            Input value of knot
        """
        pass
    
    
    Degree = None
    
    
    EndParameter = None
    
    
    EndPoint = None
    
    
    HasFitData = None
    
    
    IsRational = None
    
    
    Knots = None
    
    
    NumberOfControlPoints = None
    
    
    NumberOfKnots = None
    
    
    Order = None
    
    
    StartParameter = None
    
    
    StartPoint = None
    
    pass

class Surface(object):
    """
    
    """
    def ClosestPointTo(self):
        """
        ClosestPointTo(Point3d) -> Point3d
            
            Point3d point: 
            Input point on surface
        ClosestPointTo(Point3d, Tolerance) -> Point3d
            
            Point3d point: 
            Input point on surface
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def DistanceTo(self):
        """
        DistanceTo(Point3d) -> double
            
            Point3d point: 
            Input point on surface
        DistanceTo(Point3d, Tolerance) -> double
            
            Point3d point: 
            Input point on surface
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def EvaluatePoint(self):
        """
        EvaluatePoint -> Point3d
            
            Point2d parameter: 
            Input parameter point
        """
        pass
    
    
    def GetClosestPointTo(self):
        """
        GetClosestPointTo(Point3d) -> PointOnSurface
            
            Point3d point: 
            Input point on surface
        GetClosestPointTo(Point3d, Tolerance) -> PointOnSurface
            
            Point3d point: 
            Input point on surface
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetEnvelope(self):
        """
        GetEnvelope -> Interval()
        
        """
        pass
    
    
    def IsClosedInU(self):
        """
        IsClosedInU() -> bool
        
        IsClosedInU(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsClosedInV(self):
        """
        IsClosedInV() -> bool
        
        IsClosedInV(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsOn(self):
        """
        IsOn(Point3d, Point2d) -> bool
            
            Point3d point: 
            Input point on surface
            
            Point2d parameterPoint: 
            Input parameter point
        IsOn(Point3d, Point2d, Tolerance) -> bool
            
            Point3d point: 
            Input point on surface
            
            Point2d parameterPoint: 
            Input parameter point
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def ParameterOf(self):
        """
        ParameterOf(Point3d) -> Point2d
            
            Point3d point: 
            Input point on surface
        ParameterOf(Point3d, Tolerance) -> Point2d
            
            Point3d point: 
            Input point on surface
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    IsNormalReversed = None
    
    
    ReverseNormal = None
    
    pass

class SurfaceSurfaceIntersector(object):
    """
    
    SurfaceSurfaceIntersector()()
    
    
    SurfaceSurfaceIntersector(Surface, Surface)
        Surface surface2 : Input second surface object
        Surface surface1 : Input first surface object
    
    
    """
    def GetDimension(self):
        """
        GetDimension -> Integer
            
            int number: 
            Input index of the intersection
        """
        pass
    
    
    def GetIntersectionConfigurations(self):
        """
        GetIntersectionConfigurations -> SurfaceSurfaceIntersectorConfigurations
            
            int number: 
            Input index of the intersection
        """
        pass
    
    
    def GetIntersectPointParameters(self):
        """
        GetIntersectPointParameters -> Point2d()
            
            int number: 
            Input index of the intersection
        """
        pass
    
    
    def GetType(self):
        """
        GetType -> SurfaceSurfaceIntersectorType
            
            int number: 
            Input index of the intersection
        """
        pass
    
    
    def IntersectCurve(self):
        """
        IntersectCurve -> Curve3d
            
            int number: 
            Input index of the intersection
            
            [MarshalAs(UnmanagedType.U1)] bool isExternal: 
            Input Boolean to return curve on first or second surface
        """
        pass
    
    
    def IntersectParameterCurve(self):
        """
        IntersectParameterCurve -> Curve2d
            
            int number: 
            Input index of the intersection
            
            [MarshalAs(UnmanagedType.U1)] bool isExternal: 
            Input Boolean to return curve on first or second surface
            
            [MarshalAs(UnmanagedType.U1)] bool isFirst: 
            Input Boolean flag to return curve on first or second surface
        """
        pass
    
    
    def IntersectPoint(self):
        """
        IntersectPoint -> Point3d
            
            int number: 
            Input index of the intersection
        """
        pass
    
    
    def Set(self):
        """
        Set(Surface, Surface) -> void
            
            Surface surface1: 
            Input first surface object
            
            Surface surface2: 
            Input second surface object
        Set(Surface, Surface, Autodesk.AutoCAD.Geometry.Tolerance) -> void
            
            Surface surface1: 
            Input first surface object
            
            Surface surface2: 
            Input second surface object
            
            Autodesk.AutoCAD.Geometry.Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    NumResults = None
    
    
    Surface1 = None
    
    
    Surface2 = None
    
    
    Tolerance = None
    
    pass

class SurfaceSurfaceIntersectorConfiguration():
    Unknown = None
    Out = None
    In = None
    Coincident = None

class SurfaceSurfaceIntersectorConfigurations(object):
    """
    
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare against
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo -> bool
            
            SurfaceSurfaceIntersectorConfigurations a: 
            Input object to compare against
        """
        pass
    
    
    Dimension = None
    
    
    IntersectionType = None
    
    
    Surface1Left = None
    
    
    Surface1Right = None
    
    
    Surface2Left = None
    
    
    Surface2Right = None
    
    pass

class SurfaceSurfaceIntersectorType():
    Transverse = None
    Tangent = None
    AntiTangent = None

class Tolerance(object):
    """
    
    Tolerance
        double equalVector : Input default vector
        double equalPoint : Input default point
    """
    EqualPoint = None
    
    
    EqualVector = None
    
    
    Global = None
    
    pass

class Torus(object):
    """
    
    Torus()()
    
    
    Torus(double, double, Point3d, Vector3d)
        double majorRadius : Input major radius
        double minorRadius : Input minor radius
        Point3d origin : Input center
        Vector3d axisOfSymmetry : Input axis of rotation
    
    
    Torus(double, double, Point3d, Vector3d, Vector3d, double, double, double, double)
        double majorRadius : Input major radius
        double minorRadius : Input minor radius
        Point3d origin : Input center
        Vector3d axisOfSymmetry : Input axis of rotation
        Vector3d referenceAxis : Input direction to the zero meridian
        double startAngleU : Input start longitude
        double endAngleU : Input end longitude
        double startAngleV : Input start latitude
        double endAngleV : Input end latitude
    
    
    """
    def GetAnglesInU(self):
        """
        GetAnglesInU -> double()
        
        """
        pass
    
    
    def GetAnglesInV(self):
        """
        GetAnglesInV -> double()
        
        """
        pass
    
    
    def IntersectWith(self):
        """
        IntersectWith(LinearEntity3d) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
        IntersectWith(LinearEntity3d, Tolerance) -> Point3d()
            
            LinearEntity3d linearEntity: 
            Input linear entity
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Set(self):
        """
        Set(double, double, Point3d, Vector3d) -> void
            
            double majorRadius: 
            Input major radius
            
            double minorRadius: 
            Input minor radius
            
            Point3d origin: 
            Input center
            
            Vector3d axisOfSymmetry: 
            Input axis of rotation
        Set(double, double, Point3d, Vector3d, Vector3d, double, double, double, double) -> void
            
            double majorRadius: 
            Input major radius
            
            double minorRadius: 
            Input minor radius
            
            Point3d origin: 
            Input center
            
            Vector3d axisOfSymmetry: 
            Input axis of rotation
            
            Vector3d refAxis: 
            Input reference axis
            
            double startAngleU: 
            Input start longitude
            
            double endAngleU: 
            Input end longitude
            
            double startAngleV: 
            Input start latitude
            
            double endAngleV: 
            Input end latitude
        """
        pass
    
    
    def SetAnglesInU(self):
        """
        SetAnglesInU -> void
            
            double startAngle: 
            Input start longitude
            
            double endAngle: 
            Input end longitude
        """
        pass
    
    
    def SetAnglesInV(self):
        """
        SetAnglesInV -> void
            
            double startAngle: 
            Input start latitude
            
            double endAngle: 
            Input end latitude
        """
        pass
    
    
    AxisOfSymmetry = None
    
    
    Center = None
    
    
    IsApple = None
    
    
    IsDegenerate = None
    
    
    IsDoughnut = None
    
    
    IsHollow = None
    
    
    IsLemon = None
    
    
    IsOuterNormal = None
    
    
    IsVortex = None
    
    
    MajorRadius = None
    
    
    MinorRadius = None
    
    
    ReferenceAxis = None
    
    pass

class Vector2d(object):
    """
    
    Vector2d(double, double)()
    
    
    Vector2d(double[])
        unnamed : Input coordinate array
    
    
    """
    def Add(self):
        """
        Add -> Vector2d
            
            Vector2d v: 
            Input vector to add
        """
        pass
    
    
    def DivideBy(self):
        """
        DivideBy -> Vector2d
            
            double value: 
            Input value to divide by
        """
        pass
    
    
    def DotProduct(self):
        """
        DotProduct -> double
            
            Vector2d v: 
            Input vector to perform the dot product with
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetAngleTo(self):
        """
        GetAngleTo -> double
            
            Vector2d vector: 
            Input vector to get angle to
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetNormal(self):
        """
        GetNormal() -> Vector2d
        
        GetNormal(Tolerance) -> Vector2d
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetPerpendicularVector(self):
        """
        GetPerpendicularVector -> Vector2d
        
        """
        pass
    
    
    def IsCodirectionalTo(self):
        """
        IsCodirectionalTo(Vector2d) -> bool
            
            Vector2d vector: 
            Input vector
        IsCodirectionalTo(Vector2d, Tolerance) -> bool
            
            Vector2d vector: 
            Input vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Vector2d) -> bool
            
            Vector2d vector: 
            Input vector
        IsEqualTo(Vector2d, Tolerance) -> bool
            
            Vector2d vector: 
            Input vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsParallelTo(self):
        """
        IsParallelTo(Vector2d) -> bool
            
            Vector2d vector: 
            Input vector
        IsParallelTo(Vector2d, Tolerance) -> bool
            
            Vector2d vector: 
            Input vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPerpendicularTo(self):
        """
        IsPerpendicularTo(Vector2d) -> bool
            
            Vector2d vector: 
            Input vector
        IsPerpendicularTo(Vector2d, Tolerance) -> bool
            
            Vector2d vector: 
            Input vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsUnitLength(self):
        """
        IsUnitLength() -> bool
        
        IsUnitLength(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsZeroLength(self):
        """
        IsZeroLength() -> bool
        
        IsZeroLength(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> Vector2d
            
            Vector2d line: 
            Input any 2D line
        """
        pass
    
    
    def MultiplyBy(self):
        """
        MultiplyBy -> Vector2d
            
            double value: 
            Input value to multiply by
        """
        pass
    
    
    def Negate(self):
        """
        Negate -> Vector2d
        
        """
        pass
    
    
    def RotateBy(self):
        """
        RotateBy -> Vector2d
            
            double angle: 
            Input rotation angle
        """
        pass
    
    
    def Subtract(self):
        """
        Subtract -> Vector2d
            
            Vector2d v: 
            Input value to subtract by
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> Vector2d
            
            Matrix2d leftSide: 
            Input 2D matrix
        """
        pass
    
    
    Angle = None
    
    
    Length = None
    
    
    LengthSqrd = None
    
    
    X = None
    
    
    XAxis = None
    
    
    Y = None
    
    
    YAxis = None
    
    pass

class Vector3d(object):
    """
    
    Vector3d(PlanarEntity, Vector2d)
        PlanarEntity plane : Input plane
        Vector2d vector2d : Input vector
    
    
    Vector3d(double, double, double)()
    
    
    Vector3d(double[])
        double[] xyz : Input coordinate array
    
    
    """
    def Add(self):
        """
        Add -> Vector3d
            
            Vector3d v: 
            Input vector to add
        """
        pass
    
    
    def AngleOnPlane(self):
        """
        AngleOnPlane -> double
            
            PlanarEntity plane: 
            Input input plane
        """
        pass
    
    
    def Convert2d(self):
        """
        Convert2d -> Vector2d
            
            PlanarEntity plane: 
            Input input plane
        """
        pass
    
    
    def CrossProduct(self):
        """
        CrossProduct -> Vector3d
            
            Vector3d vector: 
            Input any 3D vector
        """
        pass
    
    
    def DivideBy(self):
        """
        DivideBy -> Vector3d
            
            double value: 
            Input a figure to divide by
        """
        pass
    
    
    def DotProduct(self):
        """
        DotProduct -> double
            
            Vector3d v: 
            Input vector to perform dot product with
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to check against
        """
        pass
    
    
    def GetAngleTo(self):
        """
        GetAngleTo(Vector3d) -> double
            
            Vector3d vector: 
            Input any 3D vector
        GetAngleTo(Vector3d, Vector3d) -> double
            
            Vector3d vector: 
            Input any 3D vector
            
            Vector3d referenceVector: 
            Input reference vector
        """
        pass
    
    
    def GetHashCode(self):
        """
        GetHashCode -> Integer
        
        """
        pass
    
    
    def GetNormal(self):
        """
        GetNormal() -> Vector3d
        
        GetNormal(Tolerance) -> Vector3d
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def GetPerpendicularVector(self):
        """
        GetPerpendicularVector -> Vector3d
        
        """
        pass
    
    
    def IsCodirectionalTo(self):
        """
        IsCodirectionalTo(Vector3d) -> bool
            
            Vector3d vector: 
            Input any 3D vector
        IsCodirectionalTo(Vector3d, Tolerance) -> bool
            
            Vector3d vector: 
            Input any 3D vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsEqualTo(self):
        """
        IsEqualTo(Vector3d) -> bool
            
            Vector3d vector: 
            Input any 3D vector
        IsEqualTo(Vector3d, Tolerance) -> bool
            
            Vector3d vector: 
            Input any 3D vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsParallelTo(self):
        """
        IsParallelTo(Vector3d) -> bool
            
            Vector3d vector: 
            Input Autodesk.AutoCAD.Geometry.Vector3d object.
        IsParallelTo(Vector3d, Tolerance) -> bool
            
            Vector3d vector: 
            Input any 3D vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsPerpendicularTo(self):
        """
        IsPerpendicularTo(Vector3d) -> bool
            
            Vector3d vector: 
            Input any 3D vector
        IsPerpendicularTo(Vector3d, Tolerance) -> bool
            
            Vector3d vector: 
            Input any 3D vector
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsUnitLength(self):
        """
        IsUnitLength() -> bool
        
        IsUnitLength(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def IsZeroLength(self):
        """
        IsZeroLength() -> bool
        
        IsZeroLength(Tolerance) -> bool
            
            Tolerance tolerance: 
            Input tolerance value
        """
        pass
    
    
    def Mirror(self):
        """
        Mirror -> Vector3d
            
            Vector3d normalToPlane: 
            Input plane normal
        """
        pass
    
    
    def MultiplyBy(self):
        """
        MultiplyBy -> Vector3d
            
            double value: 
            Input value to multiply against
        """
        pass
    
    
    def Negate(self):
        """
        Negate -> Vector3d
        
        """
        pass
    
    
    def OrthoProjectTo(self):
        """
        OrthoProjectTo -> Vector3d
            
            Vector3d planeNormal: 
            Input plane normal
        """
        pass
    
    
    def ProjectTo(self):
        """
        ProjectTo -> Vector3d
            
            Vector3d planeNormal: 
            Input plane normal
            
            Vector3d projectDirection: 
            Input direction of projection
        """
        pass
    
    
    def RotateBy(self):
        """
        RotateBy -> Vector3d
            
            double angle: 
            Input angle of rotation
            
            Vector3d axis: 
            Input axis of rotation
        """
        pass
    
    
    def Subtract(self):
        """
        Subtract -> Vector3d
            
            Vector3d v: 
            Input value to subtract by
        """
        pass
    
    
    def ToArray(self):
        """
        ToArray -> double()
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(IFormatProvider) -> string
            
            IFormatProvider provider: 
            Input for culture-specific format
        ToString(string, IFormatProvider) -> string
            
            string format: 
            Input format
            
            IFormatProvider provider: 
            Input for culture-specific format
        """
        pass
    
    
    def TransformBy(self):
        """
        TransformBy -> Vector3d
            
            Matrix3d leftSide: 
            Input 3D matrix
        """
        pass
    
    
    LargestElement = None
    
    
    Length = None
    
    
    LengthSqrd = None
    
    
    X = None
    
    
    XAxis = None
    
    
    Y = None
    
    
    YAxis = None
    
    
    Z = None
    
    
    ZAxis = None
    
    pass