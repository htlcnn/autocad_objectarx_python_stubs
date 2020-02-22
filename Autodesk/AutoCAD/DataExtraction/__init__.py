class AdoOutput(object):
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

class DxDrawingDataExtractor(object):
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

class DxDrawingDataExtractorSettings(object):
    """
    
    DxDrawingDataExtractorSettings()
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

class DxExtractionSettings(object):
    """
    
    DxExtractionSettings()
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

class DxFileList(object):
    """
    
    DxFileList()
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

class DxFileReference(object):
    """
    
    DxFileReference()()
    
    
    DxFileReference(string, string)
        string rootdir : Input base path from which the path will be relative to
        filename : Input filename to set
    
    
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

class DxFolder(object):
    """
    
    DxFolder
        IDxFileReference folder : Input the folder reference
        string wildCard : Input a wildcard string used for matching filenames
        bool includeSubDirs : Input a value of true to include subfolders
        bool usingWildcard : Input a value of true to enable wildcard matching
        bool liveFolder : Input a value of true to enable the live folder option
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