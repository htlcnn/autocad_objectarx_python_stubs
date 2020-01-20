class AdoOutput(public class AdoOutput):
    """
    
    """
    def DeleteDataFile(self):
        """
        DeleteDataFile -> void
            
            string filename: 
            Input string; name of the data file to delete
        """
        pass
    
    
    def ExportDataSetViaDatabaseConnection(self):
        """
        ExportDataSetViaDatabaseConnection -> void
            
            Autodesk.AutoCAD.OleDb64.OleDbConnection conn: 
            Input the database connection object
            
            DataSet ds2: 
            Input the dataset to export
            
            OutputType ot: 
            Input the format of the output
        """
        pass
    
    
    def SaveDataSetToFileImp(self):
        """
        SaveDataSetToFileImp -> void
            
            string filename: 
            Input filename to save the data set to
            
            DataSet ds: 
            Input data set to be saved
            
            OutputType ot: 
            Input the format of the output
        """
        pass
    
    
    def SaveDataSetToFile(self):
        """
        SaveDataSetToFile -> void
            
            string filename: 
            Input filename to save the data set to
            
            DataSet ds: 
            Input data set to be saved
            
            OutputType ot: 
            Input the format of the output
        """
        pass
    
    
    def SaveDataTableToFile(self):
        """
        SaveDataTableToFile -> void
            
            string filename: 
            Input filename to save the DataTable to
            
            DataTable dt: 
            Input data table to be saved
            
            OutputType ot: 
            Input the format of the output
        """
        pass
    
    pass

class DxDrawingDataExtractor(IDxDrawingDataExtractor, ISerializable):
    """
    
    """
    def DiscoverTypesAndProperties(self):
        """
        DiscoverTypesAndProperties -> bool
            
            string rootdir: 
            Input the path that will be used for resolving relative file paths. Typically, this is the path to the DXE file
        """
        pass
    
    
    def ExtractData(self):
        """
        ExtractData -> bool
            
            string rootdir: 
            Input the path which will be used for resolving relative file paths. Typically this is the path to the DXE file
        """
        pass
    
    
    DiscoveredTypesAndProperties = None
    
    
    ExtractedData = None
    
    
    Settings = None
    
    pass

class DxDrawingDataExtractorSettings(IDxDrawingDataExtractorSettings, ISerializable):
    """
    
    D
    
    x
    
    D
    
    r
    
    a
    
    w
    
    i
    
    n
    
    g
    
    D
    
    a
    
    t
    
    a
    
    E
    
    x
    
    t
    
    r
    
    a
    
    c
    
    t
    
    o
    
    r
    
    S
    
    e
    
    t
    
    t
    
    i
    
    n
    
    g
    
    s
    
    (
    
    )
    """
    def SetSelectedTypesAndProperties(self):
        """
        SetSelectedTypesAndProperties -> void
            
            List<IDxTypeDescriptor> discoveredTypesAndProps: 
            Input a list of IDxTypeDescriptor objects. This should come from the DiscoveredTypesAndProperties property of the DxDrawingDataExtractor
        """
        pass
    
    
    DrawingList = None
    
    
    ExtractFlags = None
    
    
    SelectedTypesAndProperties = None
    
    pass

class DxExtractionSettings(IDxExtractionSettings, ISerializable):
    """
    
    D
    
    x
    
    E
    
    x
    
    t
    
    r
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    t
    
    t
    
    i
    
    n
    
    g
    
    s
    
    (
    
    )
    """
    def Save(self):
        """
        Save -> void
            
            string filename: 
            Input the name of the file to save to
        """
        pass
    
    
    def FromFile(self):
        """
        FromFile -> IDxExtractionSettings
            
            string filename: 
            Input filename to retrieve the extraction settings from
        """
        pass
    
    
    DrawingDataExtractor = None
    
    
    Filename = None
    
    pass

class DxFileList(IDxFileList, ISerializable):
    """
    
    D
    
    x
    
    F
    
    i
    
    l
    
    e
    
    L
    
    i
    
    s
    
    t
    
    (
    
    )
    """
    def AddFile(self):
        """
        AddFile -> void
            
            IDxFileReference fileref: 
            Input file to add
        """
        pass
    
    
    def AddFolder(self):
        """
        AddFolder -> void
            
            IDxFolder folder: 
            Input folder object to add
        """
        pass
    
    
    def GetAllFiles(self):
        """
        GetAllFiles -> List<IDxFileReference>
            
            string rootdir: 
            Input path that will be used for resolving relative file paths. Typically, this is the path to the DXE file
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator<FileInfo>
            
            string rootdir: 
            Input path that will be used for resolving relative file paths. Typically, this is the path to the DXE file
        """
        pass
    
    
    def RemoveFile(self):
        """
        RemoveFile -> void
            
            IDxFileReference fileref: 
            Input file to remove
        """
        pass
    
    
    def RemoveFolder(self):
        """
        RemoveFolder -> void
            
            IDxFolder folder: 
            Input folder to remove
        """
        pass
    
    
    CurrentFile = None
    
    
    Files = None
    
    
    Folders = None
    
    pass

class DxFileReference(IDxFileReference, ISerializable):
    """
    
    D
    
    x
    
    F
    
    i
    
    l
    
    e
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    x
    
    F
    
    i
    
    l
    
    e
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
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
    
     
    
    r
    
    o
    
    o
    
    t
    
    d
    
    i
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    b
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    r
    
    e
    
    l
    
    a
    
    t
    
    i
    
    v
    
    e
    
     
    
    t
    
    o
    
    
    
    
     
    
     
    
     
    
     
    
    f
    
    i
    
    l
    
    e
    
    n
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    f
    
    i
    
    l
    
    e
    
    n
    
    a
    
    m
    
    e
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    """
    def Resolve(self):
        """
        Resolve -> string
            
            string rootdir: 
            Input path to use for resolving relative paths. Typically, this is the path to the DXE file
        """
        pass
    
    
    def Set(self):
        """
        Set -> bool
            
            string rootdir: 
            Input base path from which the path will be relative to
            
            string target: 
            Input filename to set
        """
        pass
    
    
    def ToString(self):
        """
        ToString -> string
        
        """
        pass
    
    pass

class DxFolder(IDxFolder, ISerializable):
    """
    
    D
    
    x
    
    F
    
    o
    
    l
    
    d
    
    e
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    D
    
    x
    
    F
    
    i
    
    l
    
    e
    
    R
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    f
    
    o
    
    l
    
    d
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    o
    
    l
    
    d
    
    e
    
    r
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    w
    
    i
    
    l
    
    d
    
    C
    
    a
    
    r
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    w
    
    i
    
    l
    
    d
    
    c
    
    a
    
    r
    
    d
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    u
    
    s
    
    e
    
    d
    
     
    
    f
    
    o
    
    r
    
     
    
    m
    
    a
    
    t
    
    c
    
    h
    
    i
    
    n
    
    g
    
     
    
    f
    
    i
    
    l
    
    e
    
    n
    
    a
    
    m
    
    e
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    i
    
    n
    
    c
    
    l
    
    u
    
    d
    
    e
    
    S
    
    u
    
    b
    
    D
    
    i
    
    r
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    r
    
    u
    
    e
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    c
    
    l
    
    u
    
    d
    
    e
    
     
    
    s
    
    u
    
    b
    
    f
    
    o
    
    l
    
    d
    
    e
    
    r
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    u
    
    s
    
    i
    
    n
    
    g
    
    W
    
    i
    
    l
    
    d
    
    c
    
    a
    
    r
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    r
    
    u
    
    e
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    l
    
    d
    
    c
    
    a
    
    r
    
    d
    
     
    
    m
    
    a
    
    t
    
    c
    
    h
    
    i
    
    n
    
    g
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    l
    
    i
    
    v
    
    e
    
    F
    
    o
    
    l
    
    d
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    r
    
    u
    
    e
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    a
    
    b
    
    l
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    l
    
    i
    
    v
    
    e
    
     
    
    f
    
    o
    
    l
    
    d
    
    e
    
    r
    
     
    
    o
    
    p
    
    t
    
    i
    
    o
    
    n
    """
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator<FileInfo>
            
            string rootdir: 
            Input path which will be used for resolving relative file paths
        """
        pass
    
    
    Folder = None
    
    
    IncludeSubFolders = None
    
    
    LiveFolder = None
    
    
    SelectedFiles = None
    
    
    UnSelectedFiles = None
    
    
    UsingWildcard = None
    
    
    WildcardPattern = None
    
    pass