class ColorDictionary(object):
    """
    
    """

    pass

class FontInfo(object):
    """
    
    FontInfo()
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

class HSBColor(object):
    """
    
    HSBColor()()
    
    
    HSBColor(Color)
        Color color : Specify the Color object that is used to create new object.
    
    
    HSBColor(double, double, double, double)
        double hue : Specify the hue for HSB color.
        double saturation : Specify the saturation for HSB color.
        double brightness : Specify the brightness for HSB color.
        double opacity : Specify the opacity for HSB color.
    
    
    HSBColor(string)
        string hsbString : Specify the string of HSB color. String format: "0,0,32"
    
    
    """
    class OperationType():
        None = None
        Add = None
        Subtract = None
        Multiply = None
    
    
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

class HSBColorDictionary(object):
    """
    
    """

    pass

class HSBColorUtil(object):
    """
    
    """
    def GetPaletteThemeHSBColors(self):
        """
        GetPaletteThemeHSBColors -> HSBColorDictionary
        
        """
        pass
    
    pass

class HSBColors(object):
    """
    
    """
    BaseColorKey = None
    
    pass

class HSBColorsDictionary(object):
    """
    
    """

    pass

class ImageSources(object):
    """
    
    """
    Images Field = None
    
    
    Uris Field = None
    
    pass

class InPlaceEditorTheme(object):
    """
    
    InPlaceEditorTheme()()
    
    
    InPlaceEditorTheme(HSBColor)()
    
    
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

class InPlaceEditorThemeDefaults(object):
    """
    
    """
    DarkOverallColor Field = None
    
    
    DarkTextColor Field = None
    
    
    LightOverallColor Field = None
    
    
    LightTextColor Field = None
    
    pass

class ThemeBase(object):
    """
    
    ThemeBase()
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

class ThemeColorGenerator(object):
    """
    
    ThemeColorGenerator()
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

class ThemeManager(object):
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

class ThemeResources(object):
    """
    
    ThemeResources()
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

class ThemedImageSource(object):
    """
    
    ThemedImageSource()
    """
    this Field = None
    
    pass

class ThemedImageUri(object):
    """
    
    ThemedImageUri()
    """

    pass