class Color(DisposableWrapper, IComparable, ICloneable):
    """
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    )
    """
    def Audit(self):
        """
        Audit -> void
            
            AuditInfo auditInfo: 
            Input an AuditInfo object
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    def CompareTo(self):
        """
        CompareTo -> Integer
            
            object obj: 
            Input object to compare
        """
        pass
    
    
    def DwgIn(self):
        """
        DwgIn -> Autodesk.AutoCAD.Colors.Color
            
            DwgFiler inputFiler: 
            DWG filer to be used for this filing operation
        """
        pass
    
    
    def DwgOut(self):
        """
        DwgOut -> void
            
            DwgFiler outputFiler: 
            DWG filer to be used for this filing operation
        """
        pass
    
    
    def DxfIn(self):
        """
        DxfIn -> Autodesk.AutoCAD.Colors.Color
            
            DxfFiler inputFiler: 
            Input full path of the DXF file to be read into database
            
            int groupCodeOffset: 
            Input group code offset
        """
        pass
    
    
    def DxfOut(self):
        """
        DxfOut -> void
            
            DxfFiler outputFiler: 
            Input full path of the DXF file to write
            
            int groupCodeOffset: 
            Input group code offset
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to find the equivalency
        """
        pass
    
    
    def FromColor(self):
        """
        FromColor(System.Drawing.Color) -> Autodesk.AutoCAD.Colors.Color
            
            System.Drawing.Color value: 
            Input object to obtain color from
        FromColor(System.Windows.Media.Color) -> Autodesk.AutoCAD.Colors.Color
        
        """
        pass
    
    
    def FromColorIndex(self):
        """
        FromColorIndex -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.Colors.ColorMethod colorMethod: 
            Input Autodesk.AutoCAD.Colors.ColorMethod object to check.
            
            short colorIndex: 
            Input object to obtain color index from.
        """
        pass
    
    
    def FromDictionaryName(self):
        """
        FromDictionaryName -> Autodesk.AutoCAD.Colors.Color
            
            string name: 
            Input System.String dictionary key
        """
        pass
    
    
    def FromEntityColor(self):
        """
        FromEntityColor -> Autodesk.AutoCAD.Colors.Color
            
            Autodesk.AutoCAD.Colors.EntityColor eclr: 
            Input the EntityColor from which to create a new Color object
        """
        pass
    
    
    def FromNames(self):
        """
        FromNames -> Autodesk.AutoCAD.Colors.Color
            
            string colorName: 
            Input color name
            
            string bookName: 
            Input optional book name
        """
        pass
    
    
    def FromRgb(self):
        """
        FromRgb -> Autodesk.AutoCAD.Colors.Color
            
            byte red: 
            Input color value 0 to 255
            
            byte green: 
            Input color value 0 to 255
            
            byte blue: 
            Input color value 0 to 255
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
            Input for culture-specific format
        """
        pass
    
    
    Blue = None
    
    
    BookName = None
    
    
    ColorIndex = None
    
    
    ColorMethod = None
    
    
    ColorName = None
    
    
    ColorNameForDisplay = None
    
    
    ColorValue = None
    
    
    Description = None
    
    
    DictionaryKey = None
    
    
    DictionaryKeyLength = None
    
    
    EntityColor = None
    
    
    Explanation = None
    
    
    Green = None
    
    
    HasBookName = None
    
    
    HasColorName = None
    
    
    IsByAci = None
    
    
    IsByBlock = None
    
    
    IsByColor = None
    
    
    IsByLayer = None
    
    
    IsByPen = None
    
    
    IsForeground = None
    
    
    IsNone = None
    
    
    PenIndex = None
    
    
    Red = None
    
    pass

class ColorConverter(TypeConverter):
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
    
    
    def ConvertTo(self):
        """
        ConvertTo -> object
            
            ITypeDescriptorContext context: 
            Input context to convert within
            
            CultureInfo culture: 
            Input culture to convert within
            
            object value: 
            Input object to convert from
            
            Type destinationType: 
            Input System.Type to convert to
        """
        pass
    
    
    def CanConvertFrom(self):
        """
        CanConvertFrom -> bool
            
            ITypeDescriptorContext context: 
            Input an object for the context
            
            Type sourceType: 
            Input object to change to
        """
        pass
    
    pass

  ByAci = 0xc3
  ByBlock = 0xc1
  ByColor = 0xc2
  ByLayer = 0xc0
  ByPen = 0xc4
  Foreground = 0xc5
  LayerFrozen = 0xc7
  LayerOff = 0xc6
  None = 200

class EntityColor(public struct EntityColor {
}):
    """
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
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
    
    C
    
    o
    
    l
    
    o
    
    r
    
    s
    
    .
    
    C
    
    o
    
    l
    
    o
    
    r
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    C
    
    o
    
    l
    
    o
    
    r
    
    s
    
    .
    
    C
    
    o
    
    l
    
    o
    
    r
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
     
    
    m
    
    e
    
    t
    
    h
    
    o
    
    d
    
    
    
    
    
    
    
    
    
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
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
    
    C
    
    o
    
    l
    
    o
    
    r
    
    s
    
    .
    
    C
    
    o
    
    l
    
    o
    
    r
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
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
    
    C
    
    o
    
    l
    
    o
    
    r
    
    s
    
    .
    
    C
    
    o
    
    l
    
    o
    
    r
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
     
    
    m
    
    e
    
    t
    
    h
    
    o
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
    
    
    
    
    
    
    
    
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    b
    
    y
    
    t
    
    e
    
    ,
    
     
    
    b
    
    y
    
    t
    
    e
    
    ,
    
     
    
    b
    
    y
    
    t
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    y
    
    t
    
    e
    
     
    
    r
    
    e
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    r
    
    e
    
    d
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    0
    
     
    
    t
    
    o
    
     
    
    2
    
    5
    
    5
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    y
    
    t
    
    e
    
     
    
    g
    
    r
    
    e
    
    e
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    g
    
    r
    
    e
    
    e
    
    n
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    0
    
     
    
    t
    
    o
    
     
    
    2
    
    5
    
    5
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    y
    
    t
    
    e
    
     
    
    b
    
    l
    
    u
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    b
    
    l
    
    u
    
    e
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    0
    
     
    
    t
    
    o
    
     
    
    2
    
    5
    
    5
    
    
    
    
    
    
    
    
    
    
    E
    
    n
    
    t
    
    i
    
    t
    
    y
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    t
    
    r
    
    u
    
    e
    
    C
    
    o
    
    l
    
    o
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
    .
    """
    def LookUpAci(self):
        """
        LookUpAci -> byte
            
            byte red: 
            Input red value from 0 to 255
            
            byte green: 
            Input green value from 0 to 255
            
            byte blue: 
            Input blue value from 0 to 255
        """
        pass
    
    
    def LookUpRgb(self):
        """
        LookUpRgb -> Integer
            
            byte colorIndex: 
            Input color value and color method
        """
        pass
    
    
    Blue = None
    
    
    ColorIndex = None
    
    
    ColorMethod = None
    
    
    Green = None
    
    
    IsByAci = None
    
    
    IsByBlock = None
    
    
    IsByColor = None
    
    
    IsByLayer = None
    
    
    IsByPen = None
    
    
    IsForeground = None
    
    
    IsLayerFrozen = None
    
    
    IsLayerFrozenOrOff = None
    
    
    IsLayerOff = None
    
    
    IsNone = None
    
    
    LayerIndex = None
    
    
    PenIndex = None
    
    
    Red = None
    
    
    TrueColor = None
    
    pass

class Transparency(public struct Transparency {
}):
    """
    
    T
    
    r
    
    a
    
    n
    
    s
    
    p
    
    a
    
    r
    
    e
    
    n
    
    c
    
    y
    
    (
    
    T
    
    r
    
    a
    
    n
    
    s
    
    p
    
    a
    
    r
    
    e
    
    n
    
    c
    
    y
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    r
    
    a
    
    n
    
    s
    
    p
    
    a
    
    r
    
    e
    
    n
    
    c
    
    y
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
     
    
    m
    
    e
    
    t
    
    h
    
    o
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    r
    
    a
    
    n
    
    s
    
    p
    
    a
    
    r
    
    e
    
    n
    
    c
    
    y
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
    
    
    
    
    
    
    
    
    
    T
    
    r
    
    a
    
    n
    
    s
    
    p
    
    a
    
    r
    
    e
    
    n
    
    c
    
    y
    
    (
    
    b
    
    y
    
    t
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    y
    
    t
    
    e
    
     
    
    a
    
    l
    
    p
    
    h
    
    a
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
    l
    
    p
    
    h
    
    a
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    """
    def Equals(self):
        """
        Equals -> bool
            
            object obj: 
            Input object to compare.
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
    
    
    Alpha = None
    
    
    IsByAlpha = None
    
    
    IsByBlock = None
    
    
    IsByLayer = None
    
    
    IsClear = None
    
    
    IsInvalid = None
    
    
    IsSolid = None
    
    pass

  ByLayer
  ByBlock
  ByAlpha
  ErrorValue