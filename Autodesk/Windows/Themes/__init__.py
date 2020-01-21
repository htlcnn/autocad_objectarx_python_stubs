class ColorDictionary(Dictionary<string, Color>):
    """
    
    """

    pass

class FontInfo(Freezable):
    """
    
    F
    
    o
    
    n
    
    t
    
    I
    
    n
    
    f
    
    o
    
    (
    
    )
    """
    FontFamily = None
    
    
    FontSize = None
    
    
    FontStyle = None
    
    
    FontWeight = None
    
    
    def CreateInstanceCore(self):
        """
        CreateInstanceCore -> Freezable
        
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
        
        """
        pass
    
    
    def GetFontFamily(self):
        """
        GetFontFamily -> System.Windows.Media.FontFamily
        
        """
        pass
    
    
    def GetFontSize(self):
        """
        GetFontSize -> double
        
        """
        pass
    
    
    def GetFontStyle(self):
        """
        GetFontStyle -> System.Windows.FontStyle
        
        """
        pass
    
    
    def GetFontWeight(self):
        """
        GetFontWeight -> System.Windows.FontWeight
        
        """
        pass
    
    
    def SetFontFamily(self):
        """
        SetFontFamily -> void
        
        """
        pass
    
    
    def SetFontSize(self):
        """
        SetFontSize -> void
        
        """
        pass
    
    
    def SetFontStyle(self):
        """
        SetFontStyle -> void
        
        """
        pass
    
    
    def SetFontWeight(self):
        """
        SetFontWeight -> void
        
        """
        pass
    
    
    FontFamily = None
    
    
    FontSize = None
    
    
    FontStyle = None
    
    
    FontWeight = None
    
    pass

class HSBColor(public class HSBColor):
    """
    
    H
    
    S
    
    B
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    H
    
    S
    
    B
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    C
    
    o
    
    l
    
    o
    
    r
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    l
    
    o
    
    r
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    C
    
    o
    
    l
    
    o
    
    r
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    u
    
    s
    
    e
    
    d
    
     
    
    t
    
    o
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    H
    
    S
    
    B
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    ,
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    h
    
    u
    
    e
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    h
    
    u
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    H
    
    S
    
    B
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    s
    
    a
    
    t
    
    u
    
    r
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    a
    
    t
    
    u
    
    r
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    f
    
    o
    
    r
    
     
    
    H
    
    S
    
    B
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    b
    
    r
    
    i
    
    g
    
    h
    
    t
    
    n
    
    e
    
    s
    
    s
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    b
    
    r
    
    i
    
    g
    
    h
    
    t
    
    n
    
    e
    
    s
    
    s
    
     
    
    f
    
    o
    
    r
    
     
    
    H
    
    S
    
    B
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    o
    
    p
    
    a
    
    c
    
    i
    
    t
    
    y
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    p
    
    a
    
    c
    
    i
    
    t
    
    y
    
     
    
    f
    
    o
    
    r
    
     
    
    H
    
    S
    
    B
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
    .
    
    
    
    
    
    
    
    
    
    
    H
    
    S
    
    B
    
    C
    
    o
    
    l
    
    o
    
    r
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    h
    
    s
    
    b
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    :
    
     
    
    S
    
    p
    
    e
    
    c
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    f
    
     
    
    H
    
    S
    
    B
    
     
    
    c
    
    o
    
    l
    
    o
    
    r
    
    .
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    f
    
    o
    
    r
    
    m
    
    a
    
    t
    
    :
    
     
    
    "
    
    0
    
    ,
    
    0
    
    ,
    
    3
    
    2
    
    "
    """
    class OperationType():
        None
        Add
        Subtract
        Multiply
    
    
    def FromColor(self):
        """
        FromColor -> HSBColor
            
            Color rgbColor: 
            Specify the Color object.
        """
        pass
    
    
    def SetHSB(self):
        """
        SetHSB -> void
            
            double hue: 
            Specify the hue for HSB color.
            
            double saturation: 
            Specify the saturation for HSB color.
            
            double brightness: 
            Specify the brightness for HSB color.
            
            double opacity: 
            Specify the opacity for HSB color.
        """
        pass
    
    
    def ToColor(self):
        """
        ToColor -> Color
        
        """
        pass
    
    
    def ToString(self):
        """
        ToString() -> string
        
        ToString(int) -> string
            
            int flag: 
             If 0, return string as "H:{0} S:{1} B:{2} A:{3} format". Otherwise, return string as "H:{0} S:{1} B:{2} A:{3} Operation:{4}" format. 
        """
        pass
    
    
    Brightness = None
    
    
    Hue = None
    
    
    Opacity = None
    
    
    Operation = None
    
    
    Saturation = None
    
    pass

class HSBColorDictionary(Dictionary<string, HSBColor>):
    """
    
    """

    pass

class HSBColorUtil(public class HSBColorUtil):
    """
    
    """
    def GetPaletteThemeHSBColors(self):
        """
        GetPaletteThemeHSBColors -> HSBColorDictionary
        
        """
        pass
    
    pass

class HSBColors(List<HSBColor>):
    """
    
    """
    BaseColorKey = None
    
    pass

class HSBColorsDictionary(Dictionary<string, HSBColors>):
    """
    
    """

    pass

class ImageSources(INotifyPropertyChanged, INotifyPropertyChanging):
    """
    
    """
    Images Field = None
    
    
    Uris Field = None
    
    pass

class InPlaceEditorTheme(ThemeBase):
    """
    
    I
    
    n
    
    P
    
    l
    
    a
    
    c
    
    e
    
    E
    
    d
    
    i
    
    t
    
    o
    
    r
    
    T
    
    h
    
    e
    
    m
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    I
    
    n
    
    P
    
    l
    
    a
    
    c
    
    e
    
    E
    
    d
    
    i
    
    t
    
    o
    
    r
    
    T
    
    h
    
    e
    
    m
    
    e
    
    (
    
    H
    
    S
    
    B
    
    C
    
    o
    
    l
    
    o
    
    r
    
    )
    
    (
    
    )
    """
    CompositeHardShadowColor = None
    
    
    CompositeSoftShadowColor = None
    
    
    CornerResizeColor = None
    
    
    CornerResizeShadowColor = None
    
    
    FillColor = None
    
    
    GlyphColor = None
    
    
    GlyphShadowColor = None
    
    
    IsDark = None
    
    
    OutlineColor = None
    
    
    OverallColor = None
    
    
    OverallTextColor = None
    
    
    ShadowLineColor = None
    
    
    def CreateInstanceCore(self):
        """
        CreateInstanceCore -> Freezable
        
        """
        pass
    
    
    def Equals(self):
        """
        Equals -> bool
        
        """
        pass
    
    
    CompositeHardShadowColor = None
    
    
    CompositeSoftShadowColor = None
    
    
    CornerResizeColor = None
    
    
    CornerResizeShadowColor = None
    
    
    FillColor = None
    
    
    GlyphColor = None
    
    
    GlyphShadowColor = None
    
    
    IsDark = None
    
    
    OutlineColor = None
    
    
    OverallColor = None
    
    
    OverallTextColor = None
    
    
    ShadowLineColor = None
    
    pass

class InPlaceEditorThemeDefaults(public static class InPlaceEditorThemeDefaults):
    """
    
    """
    DarkOverallColor Field = None
    
    
    DarkTextColor Field = None
    
    
    LightOverallColor Field = None
    
    
    LightTextColor Field = None
    
    pass

class ThemeBase(Freezable):
    """
    
    T
    
    h
    
    e
    
    m
    
    e
    
    B
    
    a
    
    s
    
    e
    
    (
    
    )
    """
    def CloneBrush(self):
        """
        CloneBrush -> Brush
        
        """
        pass
    
    
    def CreateInstanceCore(self):
        """
        CreateInstanceCore -> Freezable
        
        """
        pass
    
    
    def GenerateColors(self):
        """
        GenerateColors -> ColorDictionary
        
        """
        pass
    
    
    def RegisterBrushDependencyProperty(self):
        """
        RegisterBrushDependencyProperty -> DependencyProperty
        
        """
        pass
    
    
    def RegisterColorDependencyProperty(self):
        """
        RegisterColorDependencyProperty(string, Color, Type) -> DependencyProperty
        
        RegisterColorDependencyProperty(string, ColorDictionary, Type) -> DependencyProperty
        
        """
        pass
    
    
    def RegisterFontDependencyProperty(self):
        """
        RegisterFontDependencyProperty -> DependencyProperty
        
        """
        pass
    
    pass

class ThemeColorGenerator(public class ThemeColorGenerator):
    """
    
    T
    
    h
    
    e
    
    m
    
    e
    
    C
    
    o
    
    l
    
    o
    
    r
    
    G
    
    e
    
    n
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    )
    """
    def GenerateColor(self):
        """
        GenerateColor(HSBColor) -> Color
        
        GenerateColor(HSBColor, HSBColor) -> Color
        
        """
        pass
    
    
    def GenerateHSBColor(self):
        """
        GenerateHSBColor(HSBColor) -> HSBColor
        
        GenerateHSBColor(HSBColor, HSBColor) -> HSBColor
        
        GenerateHSBColor(HSBColors, HSBColorDictionary) -> HSBColor
        
        """
        pass
    
    
    OverallColor = None
    
    pass

class ThemeManager(DependencyObject):
    """
    
    """
    ImageSources Field = None
    
    
    InPlaceEditorSettings Field = None
    
    
    Instance Field = None
    
    
    OverridePaletteTheme = None
    
    
    PaletteSettings Field = None
    
    
    def GetOverridePaletteTheme(self):
        """
        GetOverridePaletteTheme -> OverridePaletteTheme
        
        """
        pass
    
    
    def GetTransparency(self):
        """
        GetTransparency -> double
        
        """
        pass
    
    
    def SetOverridePaletteTheme(self):
        """
        SetOverridePaletteTheme -> void
        
        """
        pass
    
    
    CurrentInPlaceEditorTheme = None
    
    
    CurrentPaletteTheme = None
    
    pass

class ThemeResources(public class ThemeResources):
    """
    
    T
    
    h
    
    e
    
    m
    
    e
    
    R
    
    e
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    s
    
    (
    
    )
    """
    def GetObject(self):
        """
        GetObject -> object
        
        """
        pass
    
    
    def GetThemedObject(self):
        """
        GetThemedObject -> object
        
        """
        pass
    
    pass

class ThemedImageSource(ThemedImageUri):
    """
    
    T
    
    h
    
    e
    
    m
    
    e
    
    d
    
    I
    
    m
    
    a
    
    g
    
    e
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
    (
    
    )
    """
    this Field = None
    
    pass

class ThemedImageUri(public class ThemedImageUri):
    """
    
    T
    
    h
    
    e
    
    m
    
    e
    
    d
    
    I
    
    m
    
    a
    
    g
    
    e
    
    U
    
    r
    
    i
    
    (
    
    )
    """

    pass