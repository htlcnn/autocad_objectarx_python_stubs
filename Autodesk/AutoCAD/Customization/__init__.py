class AbstractRibbonSubPanel(RibbonItem, ICustomizationContainer):
    """
    
    A
    
    b
    
    s
    
    t
    
    r
    
    a
    
    c
    
    t
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    S
    
    u
    
    b
    
    P
    
    a
    
    n
    
    e
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
        
        """
        pass
    
    
    ContainerCollection = None
    
    
    Items = None
    
    
    ResizePriority = None
    
    
    TopJustify = None
    
    pass

class AcceleratorCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            MenuAccelerator menuAccelerator: 
            Input object item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            MenuAccelerator value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MenuAccelerator[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            MenuAccelerator value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input a zero-based index.
            
            MenuAccelerator value: 
            Input an item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(MenuAccelerator) -> void
            
            MenuAccelerator element: 
            Input the item to remove.
        """
        pass
    
    pass

class AliasCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add(string) -> void
            
            string alias: 
            Input the item to add.
        Add(string, string) -> void
            
            string alias: 
            Input the name of the CUI file to load as a partial.
            
            string insertBefore: 
            Input the name of the CUI file to be inserted before. If null, the CUI file is appended to the end of the list.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string alias: 
            Input the name of the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            string[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string alias: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero based index.
            
            string alias: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(string) -> void
            
            string alias: 
            Input the name of the alias to remove.
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            string newAlias: 
            Input the new alias.
            
            string oldAlias: 
            Input the alias to be replaced.
        """
        pass
    
    pass

  AllOff = 0
  AllOn = 2
  ApplicationOnly = 1
  DrawingStatusBarOnly = 3

  BUTTONS
  AUX

class ButtonGroup(CustomizationElement, ICustomizationContainer):
    """
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    B
    
    U
    
    T
    
    T
    
    O
    
    N
    
    P
    
    R
    
    E
    
    F
    
    I
    
    X
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    L
    
    i
    
    s
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    U
    
    T
    
    T
    
    O
    
    N
    
    P
    
    R
    
    E
    
    F
    
    I
    
    X
    
     
    
    p
    
    r
    
    e
    
    f
    
    i
    
    x
    
     
    
    :
    
     
    
    I
    
    d
    
    e
    
    n
    
    t
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    a
    
    s
    
     
    
    e
    
    i
    
    t
    
    h
    
    e
    
    r
    
     
    
    B
    
    U
    
    T
    
    T
    
    O
    
    N
    
    S
    
     
    
    (
    
    d
    
    i
    
    g
    
    i
    
    t
    
    i
    
    z
    
    e
    
    r
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    s
    
    )
    
     
    
    o
    
    r
    
     
    
    A
    
    U
    
    X
    
     
    
    (
    
    m
    
    o
    
    u
    
    s
    
    e
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    s
    
    )
    
    .
    
    
    
    
    
    
    
    
    
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    (
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    B
    
    U
    
    T
    
    T
    
    O
    
    N
    
    P
    
    R
    
    E
    
    F
    
    I
    
    X
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    i
    
    n
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    U
    
    T
    
    T
    
    O
    
    N
    
    P
    
    R
    
    E
    
    F
    
    I
    
    X
    
     
    
    p
    
    r
    
    e
    
    f
    
    i
    
    x
    
     
    
    :
    
     
    
    I
    
    d
    
    e
    
    n
    
    t
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    a
    
    s
    
     
    
    e
    
    i
    
    t
    
    h
    
    e
    
    r
    
     
    
    B
    
    U
    
    T
    
    T
    
    O
    
    N
    
    S
    
     
    
    (
    
    d
    
    i
    
    g
    
    i
    
    t
    
    i
    
    z
    
    e
    
    r
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    s
    
    )
    
     
    
    o
    
    r
    
     
    
    A
    
    U
    
    X
    
     
    
    (
    
    m
    
    o
    
    u
    
    s
    
    e
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    s
    
    )
    
    .
    """
    ButtonItems Field = None
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Parent = None
    
    pass

class ButtonGroupCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ButtonGroup buttonGroup: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ButtonGroup value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ButtonGroup[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def GetCustomGroups(self):
        """
        GetCustomGroups -> ArrayList
        
        """
        pass
    
    
    def GetGroupByAlias(self):
        """
        GetGroupByAlias -> ButtonGroup
            
            string searchAlias: 
            Input the alias being searched for.
        """
        pass
    
    
    def GetGroupByNumber(self):
        """
        GetGroupByNumber -> ButtonGroup
            
            int groupNumber: 
            Input the number of the button group to find.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ButtonGroup value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input a zero-based index.
            
            ButtonGroup value: 
            Input the item to insert.
        """
        pass
    
    
    def NextAlias(self):
        """
        NextAlias -> string
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ButtonGroup) -> void
            
            ButtonGroup element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ButtonItem(CustomizationReference):
    """
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
    (
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
    
    
    
    
    
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
    (
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    i
    
    s
    
     
    
    c
    
    o
    
    p
    
    i
    
    e
    
    d
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
     
    
    P
    
    a
    
    s
    
    s
    
     
    
    i
    
    n
    
     
    
    -
    
    1
    
     
    
    t
    
    o
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
    (
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
    (
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    BlankLine = None
    
    
    Parent = None
    
    pass

class ButtonItemCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ButtonItem buttonItem: 
            Input the item to add
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ButtonItem value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ButtonItem[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ButtonItem value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ButtonItem value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ButtonItem) -> void
            
            ButtonItem element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

  Full = 0
  FullWithoutFocus = 2
  Merged = 1

  _3DNavPointTriplet1 = &H138c
  _3DNavPointTriplet2 = &H138d
  _3DNavStepSizeSliderControl = &H138a
  _3DNavStepsPerSecSliderControl = &H138b
  _3DNavViewComboCtrl = &H1388
  _3DNavZoomSliderControl = &H1389
  ArrayEditNameControl = 6
  CustomControl = 20
  DimStyleControl = 11
  FindTextControl = &H13
  LayerControl = 1
  LayerFilterComboControl = &H13a2
  LayerLockTransparencySliderControl = &H13a1
  LayerStateComboControl = &H13a0
  LightColorCorrectCtrl = &H1393
  LightSliderControl1 = &H138e
  LightSliderControl2 = &H138f
  LightSliderControl3 = &H1390
  LightSliderControl4 = &H1391
  LightSliderControl5 = &H1392
  LineTypeControl = 2
  LineWeightControl = 4
  MldStyleControl = &H12
  NamedViewControl = &H10
  OPTColorControl = 3
  PlotStyleControl = 9
  RedoSkinnyButtonControl = 13
  RefblknameControl = 5
  RenderImageQualityControl = &H1396
  RenderOutputFileControl = &H1397
  RenderOutputSizeControl = &H1398
  RenderProgressControl = &H1395
  RenderStyleControl = &H1394
  TblStyleControl = 15
  TextHeightComboControl = &H13a3
  TxtStyleControl = 14
  UCSControl = 10
  UndoSkinnyButtonControl = 12
  ViewControl = 8
  ViewportScaleControl = 7
  VSEdgeColorControl = &H139a
  VSEdgeOverhangSliderControl = &H139b
  VSIntersectionEdgeColorControl = &H139f
  VSJitterEdgeSliderControl = &H139c
  VSObscuredEdgeColorControl = &H139e
  VSSilhouetteEdgeWidthSliderControl = &H139d
  VSStylesComboControl = &H1399
  WorkspacesControl = &H11

class CuiFileCollectionBase(StringCollection):
    """
    
    """
    def Add(self):
        """
        Add(string) -> Integer
            
            string fileName: 
            Input the filename to add, with or without path.
        Add(string, object) -> void
            
            string fileName: 
            Input the filename to add, with or without path..
            
            object insertBefore: 
            Input the object to insert ahead of. If null, the file is appended to the end of the list.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string fileName: 
            Input the item to find
        """
        pass
    
    
    def GetFileNameByIndex(self):
        """
        GetFileNameByIndex -> string
            
            int index: 
            The index of the file.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string fileName: 
            Input the item to find
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index entry
            
            string fileName: 
            Input the filename to insert, with or without path..
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            string fileName: 
            filename to remove, with or without path.
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            string newFile: 
            Input the new filename.
            
            string oldFile: 
            Input the old filename to replace.
        """
        pass
    
    pass

class CustomizationCollection(CollectionBase):
    """
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    """
    def Contains(self):
        """
        Contains -> bool
            
            CustomizationElement customElement: 
            Input the element to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string elementId: 
            Input the unique ID of the element to search for
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            CustomizationElement existElement: 
            Input the existing element
            
            CustomizationElement newElement: 
            Input the new element
        """
        pass
    
    pass

class CustomizationElement(VersionableElement):
    """
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    (
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
     
    
    w
    
    i
    
    t
    
    h
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    (
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
    ,
    
     
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
     
    
    w
    
    i
    
    t
    
    h
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
     
    
    r
    
    e
    
    v
    
    i
    
    s
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    r
    
    e
    
    v
    
    i
    
    s
    
    i
    
    o
    
    n
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    """
    ElementID = None
    
    
    PreserveTargetElementID = None
    
    pass

class CustomizationReference(CustomizationElement, IReference):
    """
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
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
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
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
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    I
    
    D
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
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
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    I
    
    D
    
    
    
    
     
    
     
    
     
    
     
    
    V
    
    e
    
    r
    
    s
    
    i
    
    o
    
    n
    
     
    
    r
    
    e
    
    v
    
    i
    
    s
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    r
    
    e
    
    v
    
    i
    
    s
    
    i
    
    o
    
    n
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    """
    MacroID = None
    
    
    MenuMacroReference = None
    
    pass

class CustomizationSection(ElementBase):
    """
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
     
    
    f
    
    i
    
    l
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    C
    
    U
    
    I
    
     
    
    f
    
    i
    
    l
    
    e
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    f
    
    i
    
    l
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    C
    
    U
    
    I
    
     
    
    f
    
    i
    
    l
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    r
    
    e
    
    a
    
    d
    
    O
    
    n
    
    l
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    o
    
    p
    
    e
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    a
    
    s
    
     
    
    r
    
    e
    
    a
    
    d
    
    -
    
    o
    
    n
    
    l
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    f
    
    i
    
    l
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    C
    
    U
    
    I
    
     
    
    f
    
    i
    
    l
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    r
    
    e
    
    a
    
    d
    
    O
    
    n
    
    l
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    n
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    o
    
    p
    
    e
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    a
    
    s
    
     
    
    r
    
    e
    
    a
    
    d
    
    -
    
    o
    
    n
    
    l
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    s
    
    h
    
    o
    
    w
    
    M
    
    e
    
    s
    
    s
    
    a
    
    g
    
    e
    
    B
    
    o
    
    x
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    e
    
    r
    
    r
    
    o
    
    r
    
     
    
    a
    
    n
    
    d
    
     
    
    w
    
    a
    
    r
    
    n
    
    i
    
    n
    
    g
    
     
    
    m
    
    e
    
    s
    
    s
    
    a
    
    g
    
    e
    
    s
    
     
    
    a
    
    r
    
    e
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
    e
    
    d
    
     
    
    i
    
    n
    
     
    
    a
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    :
    
     
    
    I
    
    f
    
     
    
    s
    
    e
    
    t
    
     
    
    t
    
    o
    
     
    
    t
    
    r
    
    u
    
    e
    
    ,
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
    s
    
     
    
    i
    
    n
    
     
    
    a
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    ;
    
     
    
    o
    
    t
    
    h
    
    e
    
    r
    
    w
    
    i
    
    s
    
    e
    
    ,
    
     
    
    p
    
    r
    
    i
    
    n
    
    t
    
    s
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    i
    
    n
    
    e
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
     
    
    f
    
    i
    
    l
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
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
    
    u
    
    l
    
    l
    
     
    
    p
    
    a
    
    t
    
    h
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    b
    
    e
    
    i
    
    n
    
    g
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
     
    
    T
    
    h
    
    i
    
    s
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    r
    
    e
    
    e
    
     
    
    v
    
    i
    
    e
    
    w
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    C
    
    U
    
    I
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
     
    
    a
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    C
    
    U
    
    I
    
    L
    
    o
    
    a
    
    d
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    .
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    [
    
    ]
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
    [
    
    ]
    
    )
    
    (
    
    )
    """
    EXTENSION_BAK Field = None
    
    
    EXTENSION_OPC Field = None
    
    
    EXTENSION_BACKUP Field = None
    
    
    EXTENSION_COMPILED Field = None
    
    
    EXTENSION_RESOURCE Field = None
    
    
    EXTENSION_SOURCE Field = None
    
    
    EXTENSION_TEMPLATE Field = None
    
    
    EXTENSION_XML Field = None
    
    
    def AddPartialMenu(self):
        """
        AddPartialMenu -> bool
            
            filename: 
            The menu filename. Can be provided with or without a path, though if provided without a path, it is expected that the file is located on the current support files search path.
        """
        pass
    
    
    def RemovePartialMenu(self):
        """
        RemovePartialMenu -> bool
            
            string menuGroupName: 
            Optional; may be null. The menu group name used in the partial menu. When the partial menu is not found or not loaded, the menu group name can be used to ensure the workspaces are "cleaned up" properly.
            
            filename: 
            The filename of the partial menu. Can be supplied with or without a path to the file, but the filename extension, .CUIX, must either be supplied, or will be assumed. (All legacy menu formats, such as .MNU and .CUI, are converted to .CUIX before they are loaded into AutoCAD. Therefore, only .CUIX menu files can be removed.)
        """
        pass
    
    
    def CloneMenuMacro(self):
        """
        CloneMenuMacro -> MenuMacro
            
            MenuMacro sourceMenuMacro: 
            Input the macro to duplicate.
            
            bool useSimilarMacro: 
            Input whether to re-use existing macros with the same Command string.
        """
        pass
    
    
    def FindMenuMacro(self):
        """
        FindMenuMacro -> MenuMacro
            
            string macroId: 
            Input the ID of the macro to search for.
        """
        pass
    
    
    def FireModifiedEvent(self):
        """
        FireModifiedEvent -> void
        
        """
        pass
    
    
    def LookupElement(self):
        """
        LookupElement -> CustomizationElement
            
            string id: 
            Input the ID for the element within this file.
        """
        pass
    
    
    def Save(self):
        """
        Save() -> bool
        
        Save(bool) -> bool
            
            bool createBackup: 
            Input the full path for file to be created.
        """
        pass
    
    
    CUIFileBaseName = None
    
    
    CUIParseError = None
    
    
    CUIFileName = None
    
    
    CuiFileVersion = None
    
    
    CurrMajorVer = None
    
    
    CurrMinorVer = None
    
    
    MenuGroupDisplayName = None
    
    
    HostServices = None
    
    
    IsModified = None
    
    
    MenuGroup = None
    
    
    MenuGroupName = None
    
    
    PartialCuiFiles = None
    
    
    ReadOnly = None
    
    
    Workspaces = None
    
    pass

  AddToWorkspace = 1
  DoNotAddToWorkspace = 0

class DigitizerButtonGroupCollection(ButtonGroupCollection):
    """
    
    """

    pass

  bottom = 3
  floating = 1
  ignore = 6
  left = 4
  right = 5
  top = 2

  docked = 0
  floating = 1
  ignore = 2

class DoubleClickAction(CustomizationElement):
    """
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
    -
    
    b
    
    a
    
    s
    
    e
    
    d
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
    -
    
    b
    
    a
    
    s
    
    e
    
    d
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
    -
    
    b
    
    a
    
    s
    
    e
    
    d
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    x
    
    f
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    x
    
    f
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    x
    
    f
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    x
    
    f
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
    -
    
    b
    
    a
    
    s
    
    e
    
    d
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    x
    
    f
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    x
    
    f
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    x
    
    f
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    x
    
    f
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
     
    
    c
    
    l
    
    i
    
    c
    
    k
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    z
    
    e
    
    r
    
    o
    
    -
    
    b
    
    a
    
    s
    
    e
    
    d
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    e
    
    d
    
    .
    """
    Description = None
    
    
    DoubleClickCmd = None
    
    
    DxfName = None
    
    
    Name = None
    
    
    Parent = None
    
    pass

class DoubleClickCmd(CustomizationReference):
    """
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
    (
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
    (
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
    
    
    
    
    
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    C
    
    m
    
    d
    
    (
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    .
    """

    pass

class DoubleClickCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            DoubleClickAction doubleclickAction: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            DoubleClickAction value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DoubleClickAction[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            DoubleClickAction value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            DoubleClickAction value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(DoubleClickAction) -> void
            
            DoubleClickAction element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class DoubleClickDxfNameChangedEventArgs(public sealed class DoubleClickDxfNameChangedEventArgs):
    """
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    D
    
    x
    
    f
    
    N
    
    a
    
    m
    
    e
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    d
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    D
    
    o
    
    u
    
    b
    
    l
    
    e
    
    C
    
    l
    
    i
    
    c
    
    k
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    DoubleClickActionChanged = None
    
    
    OldDoubleClickDxfName = None
    
    pass

class ElementBase(public abstract class ElementBase):
    """
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    B
    
    a
    
    s
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    def SetIsModified(self):
        """
        SetIsModified -> void
        
        """
        pass
    
    
    Parent = None
    
    pass

class FileOpenException(IOException):
    """
    
    """

    pass

class FileSaveException(IOException):
    """
    
    """

    pass

  ComboBox = 1
  LargeButton = 2
  StandardButton = 3
  Window = 0

class ICustomizationContainer(public interface ICustomizationContainer):
    """
    
    """
    ContainerCollection = None
    
    pass

class IHostServices(public interface IHostServices):
    """
    
    """
    def DisplayMessage(self):
        """
        DisplayMessage -> void
            
            string message: 
            Input the message to display.
            
            string title: 
            Input the title for the dialog box.
        """
        pass
    
    
    def EnterpriseCUIFile(self):
        """
        EnterpriseCUIFile -> CustomizationSection
        
        """
        pass
    
    
    def FindFile(self):
        """
        FindFile -> string
            
            string fileName: 
            Input the file name
        """
        pass
    
    
    def GetDieselEvalString(self):
        """
        GetDieselEvalString -> string
            
            string dieselExpression: 
            Input the expression
        """
        pass
    
    
    def GetLoadedMenuGroupNames(self):
        """
        GetLoadedMenuGroupNames -> ArrayList
        
        """
        pass
    
    
    def InsertMenuOnMenuBar(self):
        """
        InsertMenuOnMenuBar -> void
            
            string menuGroupName: 
            Input the menu group to add to
            
            string alias: 
            Input a new alias
        """
        pass
    
    
    def IsOEM(self):
        """
        IsOEM -> bool
        
        """
        pass
    
    
    def RegistryProductRootKey(self):
        """
        RegistryProductRootKey -> string
        
        """
        pass
    
    
    def WriteMessage(self):
        """
        WriteMessage -> void
            
            string message: 
            Input the message to display.
        """
        pass
    
    pass

class IImageContainer(public interface IImageContainer):
    """
    
    """

    pass

class IReference(public interface IReference):
    """
    
    """
    MacroID = None
    
    
    MenuMacroReference = None
    
    pass

class IShortcutKeyCombo(public interface IShortcutKeyCombo):
    """
    
    """
    def ShortcutKey(self):
        """
        ShortcutKey -> string
        
        """
        pass
    
    
    def ShortcutName(self):
        """
        ShortcutName -> string
        
        """
        pass
    
    pass

class ImageMenu(CustomizationElement, ICustomizationContainer):
    """
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
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
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
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
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    h
    
    e
    
    r
    
    e
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    b
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    e
    
    d
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
     
    
    o
    
    f
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    s
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    T
    
    i
    
    t
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    '
    
    s
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    T
    
    i
    
    t
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    '
    
    s
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    T
    
    i
    
    t
    
    l
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    i
    
    a
    
    l
    
    o
    
    g
    
    '
    
    s
    
     
    
    t
    
    i
    
    t
    
    l
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
    .
    """
    def AddBlankLine(self):
        """
        AddBlankLine -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    DialogTitle = None
    
    
    ImageMenuItems = None
    
    
    Parent = None
    
    pass

class ImageMenuCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ImageMenu imageMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ImageMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ImageMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ImageMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ImageMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ImageMenu) -> void
            
            ImageMenu element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ImageMenuItem(CustomizationReference):
    """
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
     
    
    Y
    
    o
    
    u
    
     
    
    m
    
    a
    
    y
    
     
    
    p
    
    a
    
    s
    
    s
    
     
    
    i
    
    n
    
     
    
    -
    
    1
    
     
    
    t
    
    o
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
     
    
    Y
    
    o
    
    u
    
     
    
    m
    
    a
    
    y
    
     
    
    p
    
    a
    
    s
    
    s
    
     
    
    i
    
    n
    
     
    
    -
    
    1
    
     
    
    t
    
    o
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    o
    
    r
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    a
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
     
    
    l
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
     
    
    t
    
    o
    
     
    
    s
    
    h
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
    L
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
     
    
    l
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
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
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    o
    
    r
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    a
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
     
    
    l
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
     
    
    t
    
    o
    
     
    
    s
    
    h
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
    L
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
     
    
    l
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
     
    
    Y
    
    o
    
    u
    
     
    
    m
    
    a
    
    y
    
     
    
    p
    
    a
    
    s
    
    s
    
     
    
    i
    
    n
    
     
    
    -
    
    1
    
     
    
    t
    
    o
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
    
    
    
    
    
    
    
    
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    m
    
    a
    
    g
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    h
    
    o
    
    l
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    o
    
    r
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    a
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
     
    
    l
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
     
    
    t
    
    o
    
     
    
    s
    
    h
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
    L
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    l
    
    i
    
    d
    
    e
    
     
    
    l
    
    i
    
    b
    
    r
    
    a
    
    r
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    
     
    
    Y
    
    o
    
    u
    
     
    
    m
    
    a
    
    y
    
     
    
    p
    
    a
    
    s
    
    s
    
     
    
    i
    
    n
    
     
    
    -
    
    1
    
     
    
    t
    
    o
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
    .
    """
    BlankLine = None
    
    
    Name = None
    
    
    Parent = None
    
    
    SlideLibrary = None
    
    
    SlideName = None
    
    pass

class ImageMenuItemCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ImageMenuItem imageMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ImageMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ImageMenuItem[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ImageMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ImageMenuItem value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(ImageMenuItem) -> void
            
            ImageMenuItem element: 
            Input the item to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class ImageUpdatedEventArgs(public sealed class ImageUpdatedEventArgs):
    """
    
    I
    
    m
    
    a
    
    g
    
    e
    
    U
    
    p
    
    d
    
    a
    
    t
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    I
    
    m
    
    a
    
    g
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    l
    
    d
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    n
    
    e
    
    w
    
    I
    
    m
    
    a
    
    g
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    """
    NewImageName = None
    
    
    OldImageName = None
    
    pass

class LspFileCollection(CuiFileCollectionBase):
    """
    
    """
    def InsertRange(self):
        """
        InsertRange -> void
            
            int startIndex: 
            Input the index to start inserting.
            
            ArrayList newItems: 
            Input an array of new items
        """
        pass
    
    pass

class MacroCollection(IEnumerable, ICollection):
    """
    
    """
    def Add(self):
        """
        Add -> Integer
            
            Macro macro: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Macro value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Array array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Macro value: 
            Input the item to find.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Index of item to remove
        """
        pass
    
    pass

class MacroGroup(ElementBase):
    """
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    """
    def AddMacro(self):
        """
        AddMacro -> void
            
            MenuMacro menuMac: 
            Input the MenuMacro to add.
        """
        pass
    
    
    def CreateMenuMacro(self):
        """
        CreateMenuMacro(string, string, string) -> MenuMacro
            
            string name: 
            Input the name of the macro.
            
            string command: 
            Input the command macro string.
            
            string tag: 
            Input the UID attribute.
        CreateMenuMacro(string, string, string, string, MacroType, string, string, string) -> MenuMacro
            
            string name: 
            Input the name of the macro
            
            string command: 
            Input the command macro string
            
            string tag: 
            Input the UID attribute
            
            string help: 
            Input the macro description
            
            MacroType macroType: 
            Input the category in which to put the macro.
            
            string smallImage: 
            Input a small Image Resource ID or file name.
            
            string largeImage: 
            Input a large Image Resource ID or file name.
            
            string labelId: 
            Input an ID to assign to the name string. Pass in null to have one generated.
        """
        pass
    
    
    def IsClassA(self):
        """
        IsClassA -> bool
        
        """
        pass
    
    
    Name = None
    
    
    Parent = None
    
    
    MenuMacros = None
    
    pass

class MacroGroupCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            MacroGroup macroGroup: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(MacroGroup) -> bool
            
            MacroGroup value: 
            Input the item to find.
        Contains(string) -> bool
            
            string name: 
            Input the name to search for.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MacroGroup[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            MacroGroup value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            MacroGroup value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> void
            
            int index: 
            Input the index of item to remove.
        """
        pass
    
    pass

class MacroNameChangedEventArgs(public sealed class MacroNameChangedEventArgs):
    """
    
    M
    
    a
    
    c
    
    r
    
    o
    
    N
    
    a
    
    m
    
    e
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    c
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    l
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
    .
    """
    MacroChanged = None
    
    
    OldMacroName = None
    
    pass

  Any = 0
  Dimension = 8
  Draw = 7
  Edit = 2
  File = 1
  Format = 5
  Help = 11
  Insert = 4
  Legacy = 13
  Modify = 9
  Overrides = 12
  Tools = 6
  View = 3
  Window = 10

class MacroUIDChangedEventArgs(public sealed class MacroUIDChangedEventArgs):
    """
    
    M
    
    a
    
    c
    
    r
    
    o
    
    U
    
    I
    
    D
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    U
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    l
    
    d
    
     
    
    I
    
    D
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    n
    
    e
    
    w
    
    U
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    I
    
    D
    """
    NewMacroUID = None
    
    
    OldMacroUID = None
    
    pass

class MenuAccelerator(CustomizationReference, IShortcutKeyCombo):
    """
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
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
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
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
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    i
    
    g
    
    n
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    k
    
    e
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    i
    
    g
    
    n
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    k
    
    e
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    i
    
    g
    
    n
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    k
    
    e
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    K
    
    e
    
    y
    
    C
    
    o
    
    m
    
    b
    
    i
    
    n
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    S
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
    K
    
    e
    
    y
    
     
    
    p
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    i
    
    g
    
    n
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    k
    
    e
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    K
    
    e
    
    y
    
    C
    
    o
    
    m
    
    b
    
    i
    
    n
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    A
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    S
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
    K
    
    e
    
    y
    
     
    
    p
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    c
    
    e
    
    l
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    def ShortcutKey(self):
        """
        ShortcutKey -> string
        
        """
        pass
    
    
    def ShortcutName(self):
        """
        ShortcutName -> string
        
        """
        pass
    
    
    Name = None
    
    
    Parent = None
    
    pass

class MenuGroup(ElementBase):
    """
    
    """
    def IsModified(self):
        """
        IsModified -> bool
            
            ItemsCollection ic: 
            A single enum value indicating which menu collection to test.
        """
        pass
    
    
    def FindMacroGroup(self):
        """
        FindMacroGroup -> MacroGroup
            
            string groupName: 
            Input the name of MacroGroup to find.
        """
        pass
    
    
    def SetModifiedItems(self):
        """
        SetModifiedItems -> void
            
            ItemsCollection ic: 
            A single enum value indicating which menu collection contains modifications.
        """
        pass
    
    
    Accelerators = None
    
    
    AnyModified = None
    
    
    RibbonRoot = None
    
    
    DigitizerButtons = None
    
    
    DoubleClickActions = None
    
    
    ImageMenus = None
    
    
    LspFiles = None
    
    
    MacroGroups = None
    
    
    MouseButtons = None
    
    
    Name = None
    
    
    QuickAccessToolbars = None
    
    
    PopMenus = None
    
    
    QuickPropertiesObjectTypes = None
    
    
    ScreenMenus = None
    
    
    TabletMenus = None
    
    
    TemporaryOverrides = None
    
    
    Toolbars = None
    
    
    ToolPanels = None
    
    
      Accelerators
      DashboardPanelSets
      DashboardToolPanels
      DigitizerButtons
      DoubleClickActions
      ImageMenus
      MacroGroups
      MouseButtons
      QuickPropertiesObjectTypes
      RolloverTooltipObjectTypes
      PopMenus
      RibbonRoot
      ScreenMenus
      TabletMenus
      TemporaryOverrides
      Toolbars
      QuickAccessToobars
      LspFile
    
    pass

class MenuGroupItemsCollection(CollectionBase):
    """
    
    """
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            string elementId: 
            Input the unique ID of the element to find.
        """
        pass
    
    
    Owner = None
    
    pass

class MenuGroupNameChangedEventArgs(public sealed class MenuGroupNameChangedEventArgs):
    """
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    N
    
    a
    
    m
    
    e
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    l
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
    .
    """
    OldName = None
    
    pass

class MenuMacro(CustomizationElement):
    """
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    (
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
    e
    
    d
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    i
    
    s
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    a
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    u
    
    n
    
    i
    
    q
    
    u
    
    e
    
     
    
    I
    
    D
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    (
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    T
    
    y
    
    p
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
    e
    
    d
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    i
    
    s
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    a
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    u
    
    n
    
    i
    
    q
    
    u
    
    e
    
     
    
    I
    
    D
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    T
    
    y
    
    p
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    T
    
    y
    
    p
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    t
    
    o
    
     
    
    o
    
    n
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    T
    
    y
    
    p
    
    e
    
     
    
    e
    
    n
    
    u
    
    m
    
    s
    
    .
    
    
    
    
    
    
    
    
    
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    s
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    D
    
    e
    
    e
    
    p
    
    C
    
    l
    
    o
    
    n
    
    e
    
     
    
    :
    
     
    
    I
    
    f
    
     
    
    t
    
    r
    
    u
    
    e
    
    ,
    
     
    
    a
    
    l
    
    l
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    s
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    d
    
    .
    
     
    
    O
    
    t
    
    h
    
    e
    
    r
    
    w
    
    i
    
    s
    
    e
    
    ,
    
     
    
    o
    
    n
    
    l
    
    y
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    u
    
    r
    
    r
    
    e
    
    n
    
    t
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    i
    
    s
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    d
    
    .
    """
    def isCitizenA(self):
        """
        isCitizenA -> bool
        
        """
        pass
    
    
    def isModified(self):
        """
        isModified -> bool
        
        """
        pass
    
    
    def isUserSource(self):
        """
        isUserSource -> bool
        
        """
        pass
    
    
    def ResetToDefault(self):
        """
        ResetToDefault -> void
        
        """
        pass
    
    
    def SetRevision(self):
        """
        SetRevision -> void
        
        """
        pass
    
    
    ElementID = None
    
    
    Macros = None
    
    
    macro = None
    
    
    Parent = None
    
    pass

class MenuMacroCollection(CollectionBase):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            MenuMacro menuMacro: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            MenuMacro value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            MenuMacro[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf(MenuMacro) -> Integer
            
            MenuMacro item: 
            Input the item to find.
        IndexOf(string) -> Integer
            
            string macroID: 
            Input the ID of item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            MenuMacro value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(MenuMacro) -> void
            
            MenuMacro element: 
            Input the item to remove.
        """
        pass
    
    pass

  ignore = 2
  Layout = 1
  Model = 0

class ObjectProperty(ObjectPropertyBase):
    """
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    y
    
    p
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    o
    
    f
    
     
    
    n
    
    e
    
    w
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    f
    
    o
    
    r
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    """
    state = None
    
    pass

class ObjectPropertyCategory(ObjectPropertyBase):
    """
    
    """
    def setSubItemState(self):
        """
        setSubItemState -> void
            
            int newVal: 
            Input new value
        """
        pass
    
    
     = None
    
    
    state = None
    
    pass

class ObjectType(CustomizationElement, INotifyPropertyChanged, ICustomizationContainer):
    """
    
    """
    ClassName = None
    
    
    ContainerCollection = None
    
    
    DisplayName = None
    
    
    Parent = None
    
    
    PropCollection = None
    
    
    SubtypeList = None
    
    pass

class ObjectTypeCollection(MenuGroupItemsCollection, INotifyCollectionChanged):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ObjectType ObjectType: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(ObjectType) -> bool
            
            ObjectType value: 
            Input the item to find.
        Contains(string) -> bool
            
            string className: 
            Input the class name item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectType[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindWithName(self):
        """
        FindWithName -> ObjectType
            
            string className: 
            Input item's class name
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ObjectType value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ObjectType value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(ObjectType) -> void
            
            ObjectType element: 
            Input the item to remove.
        """
        pass
    
    
    def SortByDisplayName(self):
        """
        SortByDisplayName -> void
        
        """
        pass
    
    pass

  ignore = 3
  off = 2
  on = 1

  Horizontal = 0
  Vertical = 1

class OverrideItem(ElementBase, IReference):
    """
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    I
    
    t
    
    e
    
    m
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    d
    
     
    
    b
    
    y
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    K
    
    e
    
    y
    
    S
    
    t
    
    a
    
    t
    
    e
    
     
    
    k
    
    e
    
    y
    
    S
    
    t
    
    a
    
    t
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    "
    
    U
    
    p
    
    "
    
     
    
    o
    
    r
    
     
    
    "
    
    D
    
    o
    
    w
    
    n
    
    "
    
     
    
    k
    
    e
    
    y
    
     
    
    s
    
    t
    
    a
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    """
    KeyState = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    Parent = None
    
    pass

  Down
  Up

class Panel(CustomizationElement, IImageContainer):
    """
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    e
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    e
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
    
    
    
    
    
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    e
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
    '
    
    s
    
     
    
    n
    
    a
    
    m
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    e
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    e
    
    t
    
    ,
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    e
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    Aliases = None
    
    
    Description = None
    
    
    LargeImage = None
    
    
    LowerPanel = None
    
    
    LowerToolPanel = None
    
    
    Name = None
    
    
    Parent = None
    
    
    SmallImage = None
    
    
    UpperPanel = None
    
    
    UpperToolPanel = None
    
    pass

class PanelCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Panel panel: 
            Input the new panel
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Panel value: 
            Input the panel to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Panel[] array: 
            Input the array to copy to
            
            int index: 
            Input the zero-based array index
        """
        pass
    
    
    def FindPanelWithAlias(self):
        """
        FindPanelWithAlias -> Panel
            
            string panelAlias: 
            Input the alias to search for.
        """
        pass
    
    
    def FindPanelWithName(self):
        """
        FindPanelWithName -> Panel
            
            string panelName: 
            Input the name to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Panel value: 
            Input the item to search for.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the array position.
            
            Panel value: 
            Input the object to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string panelName: 
            Input the name to search for.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the Panel index in the collection.
        Remove(Panel) -> void
            
            Panel element: 
            Input the object to remove.
        """
        pass
    
    
    AllAliases = None
    
    pass

  Upper
  Lower

class PanelSet(CustomizationElement, ICustomizationContainer):
    """
    
    """
    ContainerCollection = None
    
    
    Panels = None
    
    pass

class PartialCuiFileCollection(CuiFileCollectionBase):
    """
    
    """

    pass

class PopMenu(CustomizationElement, ICustomizationContainer):
    """
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    L
    
    i
    
    s
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    l
    
    i
    
    s
    
    t
    
     
    
    o
    
    f
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    .
    
     
    
    I
    
    f
    
     
    
    y
    
    o
    
    u
    
     
    
    i
    
    n
    
    t
    
    e
    
    n
    
    d
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    a
    
     
    
    s
    
    u
    
    b
    
    -
    
    m
    
    e
    
    n
    
    u
    
     
    
    o
    
    f
    
     
    
    a
    
    n
    
    o
    
    t
    
    h
    
    e
    
    r
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    L
    
    i
    
    s
    
    t
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    b
    
    e
    
     
    
    n
    
    u
    
    l
    
    l
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    t
    
    a
    
    g
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    U
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    m
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    (
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    o
    
    p
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    m
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
     
    
    S
    
    i
    
    n
    
    c
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    s
    
     
    
    a
    
    r
    
    e
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    d
    
     
    
    b
    
    y
    
     
    
    t
    
    h
    
    e
    
    i
    
    r
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
    I
    
    D
    
     
    
    o
    
    r
    
     
    
    A
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    v
    
    a
    
    l
    
    u
    
    e
    
     
    
    c
    
    a
    
    n
    
     
    
    n
    
    o
    
    r
    
    m
    
    a
    
    l
    
    l
    
    y
    
     
    
    b
    
    e
    
     
    
    -
    
    1
    
    ,
    
     
    
    t
    
    o
    
     
    
    s
    
    i
    
    m
    
    p
    
    l
    
    y
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    DisplayName = None
    
    
    HasDiesel = None
    
    
    IsShortcut = None
    
    
    Name = None
    
    
    Parent = None
    
    
    PopAlias = None
    
    
    PopMenuItems = None
    
    
    ShortcutAlias = None
    
    
    TopLevelMenu = None
    
    pass

class PopMenuCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            PopMenu popMenu: 
            Input the item to add.
        """
        pass
    
    
    def AddPopMenu(self):
        """
        AddPopMenu -> bool
            
            PopMenu popMenu: 
            Input the PopMenu to add.
            
            PopMenu insertBefore: 
            Input the PopMenu before which to insert.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            PopMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            PopMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based collection index at which copying begins.
        """
        pass
    
    
    def FindPopWithAlias(self):
        """
        FindPopWithAlias -> PopMenu
            
            string pmAlias: 
            Input the alias you seek.
        """
        pass
    
    
    def FindPopWithName(self):
        """
        FindPopWithName -> PopMenu
            
            string pmName: 
            Input the name which is sought.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            PopMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            PopMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string pmName: 
            Input the name you seek.
        """
        pass
    
    
    def NextAlias(self):
        """
        NextAlias -> string
            
            bool isContext: 
            Input whether to get the next pulldown menu alias or context menu alias.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(PopMenu) -> void
            
            PopMenu popMenu: 
            Input the item to remove.
        """
        pass
    
    
    AllAliases = None
    
    pass

class PopMenuItem(PopMenuItemBase, IReference):
    """
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    a
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    ,
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    a
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    ,
    
     
    
    i
    
    f
    
     
    
    d
    
    i
    
    f
    
    f
    
    e
    
    r
    
    e
    
    n
    
    t
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ;
    
     
    
    o
    
    t
    
    h
    
    e
    
    r
    
    w
    
    i
    
    s
    
    e
    
    ,
    
     
    
    c
    
    a
    
    n
    
     
    
    b
    
    e
    
     
    
    n
    
    u
    
    l
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    a
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
    
    
    
    
    
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    B
    
    a
    
    s
    
    e
    
    ,
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    f
    
     
    
    d
    
    i
    
    f
    
    f
    
    e
    
    r
    
    e
    
    n
    
    t
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ;
    
     
    
    o
    
    t
    
    h
    
    e
    
    r
    
    w
    
    i
    
    s
    
    e
    
    ,
    
     
    
    c
    
    a
    
    n
    
     
    
    b
    
    e
    
     
    
    n
    
    u
    
    l
    
    l
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    B
    
    a
    
    s
    
    e
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    B
    
    e
    
    f
    
    o
    
    r
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    b
    
    e
    
    f
    
    o
    
    r
    
    e
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    a
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    DisplayName = None
    
    
    HasDiesel = None
    
    
    IsSeparator = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    Name = None
    
    pass

class PopMenuItemBase(CustomizationElement):
    """
    
    """
    Parent = None
    
    pass

class PopMenuItemCollection(CustomizationCollection):
    """
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    def Add(self):
        """
        Add -> void
            
            PopMenuItemBase popMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            PopMenuItemBase element: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            PopMenuItemBase[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in the array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            PopMenuItemBase element: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            PopMenuItemBase element: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(PopMenuItemBase) -> void
            
            PopMenuItemBase element: 
            Input the item to remove.
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
            
            PopMenuItemBase existElement: 
            Input the old PopMenuItemBase element.
            
            PopMenuItemBase newElement: 
            Input the new PopMenuItemBase element.
        """
        pass
    
    pass

class PopMenuRef(PopMenuItemBase):
    """
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    R
    
    e
    
    f
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
     
    
    s
    
    u
    
    b
    
    -
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    p
    
    o
    
    p
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    R
    
    e
    
    f
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
     
    
    -
    
    1
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    a
    
    p
    
    p
    
    e
    
    n
    
    d
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    p
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    e
    
    n
    
    d
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    MenuReference = None
    
    
    Parent = None
    
    pass

class PropertyCollection(CustomizationCollection, INotifyCollectionChanged):
    """
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
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
    
    s
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    y
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    (
    
    O
    
    b
    
    j
    
    e
    
    c
    
    t
    
    T
    
    y
    
    p
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    y
    
    p
    
    e
    """
    def Add(self):
        """
        Add -> void
            
            ObjectPropertyBase objPropBase: 
            Input new object
        """
        pass
    
    
    def Contains(self):
        """
        Contains(ObjectPropertyBase) -> bool
            
            ObjectPropertyBase value: 
            Input value to check for
        Contains(string) -> bool
            
            string name: 
            Input item name
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ObjectPropertyBase[] array: 
            Input target array
            
            int index: 
            Input the zero-based index in array at which copying begins
        """
        pass
    
    
    def FindWithName(self):
        """
        FindWithName -> ObjectPropertyBase
            
            string name: 
            Input name
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ObjectPropertyBase value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ObjectPropertyBase value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ObjectPropertyBase) -> void
            
            ObjectPropertyBase element: 
            Input item to remove
        """
        pass
    
    
    Initialized = None
    
    
    ObjectTypeInfo = None
    
    pass

class QuickAccessToolbar(CustomizationElement, ICustomizationContainer):
    """
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    U
    
    I
    
    D
    
     
    
    :
    
     
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    I
    
    d
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
     
    
    I
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    I
    
    D
    
     
    
    i
    
    s
    
     
    
    n
    
    o
    
    t
    
     
    
    u
    
    n
    
    i
    
    q
    
    u
    
    e
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    i
    
    l
    
    e
    
    ,
    
     
    
    a
    
     
    
    u
    
    n
    
    i
    
    q
    
    u
    
    e
    
     
    
    I
    
    D
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    g
    
    e
    
    n
    
    e
    
    r
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    """
    class QuickAccessToolbarNameChangedEventArgs(public sealed class QuickAccessToolbarNameChangedEventArgs):
        """
        
        Q
        
        u
        
        i
        
        c
        
        k
        
        A
        
        c
        
        c
        
        e
        
        s
        
        s
        
        T
        
        o
        
        o
        
        l
        
        b
        
        a
        
        r
        
        N
        
        a
        
        m
        
        e
        
        C
        
        h
        
        a
        
        n
        
        g
        
        e
        
        d
        
        E
        
        v
        
        e
        
        n
        
        t
        
        A
        
        r
        
        g
        
        s
        
        
        
        
         
        
         
        
         
        
         
        
        Q
        
        u
        
        i
        
        c
        
        k
        
        A
        
        c
        
        c
        
        e
        
        s
        
        s
        
        T
        
        o
        
        o
        
        l
        
        b
        
        a
        
        r
        
         
        
        t
        
        o
        
        o
        
        l
        
        b
        
        a
        
        r
        
         
        
        :
        
         
        
        T
        
        h
        
        e
        
         
        
        m
        
        o
        
        d
        
        i
        
        f
        
        i
        
        e
        
        d
        
         
        
        t
        
        o
        
        o
        
        l
        
        b
        
        a
        
        r
        
        
        
        
         
        
         
        
         
        
         
        
        s
        
        t
        
        r
        
        i
        
        n
        
        g
        
         
        
        o
        
        l
        
        d
        
        N
        
        a
        
        m
        
        e
        
         
        
        :
        
         
        
        T
        
        h
        
        e
        
         
        
        o
        
        l
        
        d
        
         
        
        n
        
        a
        
        m
        
        e
        """
        OldToolbarName = None
        
        
        ToolbarChanged = None
        
        pass
    
    
    Aliases = None
    
    
    Description = None
    
    
    Name = None
    
    
    Parent = None
    
    
    RibbonItems = None
    
    pass

class QuickAccessToolbarCollection(MenuGroupItemsCollection):
    """
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    :
    
     
    
    O
    
    w
    
    n
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    def Add(self):
        """
        Add -> void
            
            QuickAccessToolbar qatToolbar: 
            Item to add.
        """
        pass
    
    
    def AddQATToolbar(self):
        """
        AddQATToolbar -> bool
            
            QuickAccessToolbar qatToolbar: 
            Toolbar to add.
            
            object obj: 
            Toolbar in the collection in front of which qatToolbar is to be inserted.If NULL, or obj is not found in the collection, then qatToolbar is appended to the end.
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> QuickAccessToolbar
            
            QuickAccessToolbar source: 
            Source QuickAccessToolbar.
            
            QuickAccessToolbar insertBefore: 
            QuickAccessToolbar to insert this one before.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            QuickAccessToolbar value: 
            Item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            QuickAccessToolbar[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindToolbarWithAlias(self):
        """
        FindToolbarWithAlias -> QuickAccessToolbar
            
            string toolbarAlias: 
            Alias to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            QuickAccessToolbar value: 
            Item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Zero-based index.
            
            QuickAccessToolbar value: 
            Item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string toolbarName: 
            Name to search for.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(QuickAccessToolbar) -> void
            
            QuickAccessToolbar qatToolbar: 
            Item to remove.
        Remove(int) -> void
            
            int index: 
            Index of item to remove.
        """
        pass
    
    pass

  Above = 0
  Below = 1

  None
  HidePanelBar
  HidePanel
  TruncatePanelBar

class RibbonButton(RibbonItem):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy.
        """
        pass
    
    
    ButtonStyle = None
    
    
    KeyTip = None
    
    pass

  LargeWithHorizontalText = 1
  LargeWithoutText = 4
  LargeWithText = 0
  SmallWithoutText = 3
  SmallWithText = 2

class RibbonCommandButton(RibbonItem, IImageContainer, IReference):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    ImageUpdated Field = None
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    
    GroupName = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    TooltipTitle = None
    
    
    ButtonStyle = None
    
    
    KeyTip = None
    
    pass

class RibbonControl(RibbonControlBase, IImageContainer):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    
    MaxWidth = None
    
    
    MinWidth = None
    
    
    LargeImage = None
    
    
    SmallImage = None
    
    
    KeyTip = None
    
    pass

class RibbonDataBoundDropDown(RibbonItem, IImageContainer):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    
    ButtonStyle = None
    
    
    ListStyle = None
    
    
    SmallImage = None
    
    
    LargeImage = None
    
    
    KeyTip = None
    
    pass

class RibbonDialogBoxLauncher(RibbonCommandHolder):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    D
    
    i
    
    a
    
    l
    
    o
    
    g
    
    B
    
    o
    
    x
    
    L
    
    a
    
    u
    
    n
    
    c
    
    h
    
    e
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    r
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
    .
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            item: 
            The RibbonItem from which to copy the data.
        """
        pass
    
    
    KeyTip = None
    
    pass

class RibbonFoldPanel(AbstractRibbonSubPanel):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    F
    
    o
    
    l
    
    d
    
    P
    
    a
    
    n
    
    e
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
        
        """
        pass
    
    
    def IsAllowedChildType(self):
        """
        IsAllowedChildType -> bool
        
        """
        pass
    
    
    def IsValidChildType(self):
        """
        IsValidChildType -> bool
        
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
        
        """
        pass
    
    
    DefaultSize = None
    
    
    MaximumSize = None
    
    
    MinimumSize = None
    
    
    ResizeStyle = None
    
    pass

  Large = 3
  Medium = 2
  Small = 1

  DoNotResize = 1
  None = 0

class RibbonGalleryControl(RibbonControl, IImageContainer):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    G
    
    a
    
    l
    
    l
    
    e
    
    r
    
    y
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem source from which to copy the data.
        """
        pass
    
    pass

  Large = 3
  None = 0
  Standard = 1

class RibbonItem(CustomizationElement):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    I
    
    t
    
    e
    
    m
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def Clone(self):
        """
        Clone -> RibbonItem
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem item: 
            The RibbonItem from which to copy the data.
        """
        pass
    
    
    def IsAllowedChildType(self):
        """
        IsAllowedChildType -> bool
        
        """
        pass
    
    
    Id = None
    
    
    Text = None
    
    pass

class RibbonItemCollection(RibbonItemsCollectionBase):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            RibbonItem item: 
            The RibbonItem being added to the collection.
        """
        pass
    
    
    def Clone(self):
        """
        Clone -> RibbonItem
            
            RibbonItem source: 
            The RibbonItem to clone and insert.
            
            RibbonItem insertBefore: 
            Then RibbonItem in the collection before which the source is to be inserted.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Zero-based index.
            
            RibbonItem value: 
            RibbonItem to insert.
        """
        pass
    
    pass

  Large = 3
  Medium = 2
  Standard = 1

  LockAll = 7
  LockDockedPanels = 1
  LockFloatingPanels = 2
  LockTabs = 4
  None = 0

class RibbonPanelBreak(RibbonItem):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    B
    
    r
    
    e
    
    a
    
    k
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """

    pass

  CollapseLast = 2
  Default = 0
  NoCollapse = 1

class RibbonPanelSource(RibbonItem, ICustomizationContainer):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            The RibbonItem from which the data is copied.
        """
        pass
    
    
    def FindItem(self):
        """
        FindItem -> RibbonItem
            
            string id: 
            Id of the ribbon item to find.
        """
        pass
    
    
    def GetMenuMacros(self):
        """
        GetMenuMacros() -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Items = None
    
    
    KeyTip = None
    
    
    Name = None
    
    
    DialogBoxLauncher = None
    
    pass

class RibbonPanelSourceCollection(RibbonItemsCollectionBase):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonPanelSource
            
            RibbonPanelSource sourcePanel: 
            The RibbonPanelSource to clone and insert.
            
            RibbonPanelSource insertBefore: 
            The RibbonPanelSource in the collection before which sourcePanel is to be inserted.
        """
        pass
    
    
    def FindRibbonPanelWithText(self):
        """
        FindRibbonPanelWithText -> RibbonPanelSource
            
            string ribbonPanelName: 
            Input name of ribbon panel.
        """
        pass
    
    
    def IsTextFree(self):
        """
        IsTextFree -> bool
            
            string ribbonPanelName: 
            The name of the panel being searched for.
        """
        pass
    
    pass

class RibbonPanelSourceReference(RibbonItem):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    t
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
    .
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input RibbonItem from which to copy the data.
        """
        pass
    
    
    PanelId = None
    
    pass

class RibbonPanelSourceReferenceCollection(RibbonItemsCollectionBase):
    """
    
    """
    def Clone(self):
        """
        Clone -> RibbonPanelSourceReference
            
            RibbonPanelSourceReference source: 
            Input the source RibbonPanelSourceReference.
            
            RibbonPanelSourceReference insertBefore: 
            Input RibbonPanelSourceReference before which the source is being inserted.
        """
        pass
    
    pass

class RibbonRoot(CustomizationElement):
    """
    
    """
    def FindPanel(self):
        """
        FindPanel -> RibbonPanelSource
            
            string id: 
            Input the string id of the RibbonPanelSource to find.
        """
        pass
    
    
    def FindPanelSource(self):
        """
        FindPanelSource -> RibbonPanelSource
            
            Collection<CustomizationSection> cuiFiles: 
            _nt_
            
            string sMenuGroupName: 
            _nt_
            
            string sId: 
            _nt_
        """
        pass
    
    
    def FindPanelWithAlias(self):
        """
        FindPanelWithAlias -> RibbonPanelSource
            
            string ribbonPanelAlias: 
            Input the ribbon panel alias being searched for.
        """
        pass
    
    
    def FindTab(self):
        """
        FindTab -> RibbonTabSource
            
            string id: 
            Input the string identifying the RibbonTabSource to find.
        """
        pass
    
    
    def FindTabWithAlias(self):
        """
        FindTabWithAlias -> RibbonTabSource
            
            string ribbonTabAlias: 
            Input the ribbon tab alias to search for.
        """
        pass
    
    
    def RemovePanel(self):
        """
        RemovePanel -> void
            
            RibbonPanelSource panelSource: 
            Input the RibbonPanelSource to remove.
        """
        pass
    
    
    RibbonPanelSources = None
    
    
    RibbonTabSelectors = None
    
    
    RibbonTabSources = None
    
    pass

class RibbonRowPanel(AbstractRibbonSubPanel):
    """
    
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to copy the data.
        """
        pass
    
    
    def IsValidChildType(self):
        """
        IsValidChildType -> bool
        
        """
        pass
    
    
    def Replace(self):
        """
        Replace -> void
        
        """
        pass
    
    
    ResizeStyle = None
    
    pass

  DoNotResize = 4
  NeverHideText = 1
  NeverShrink = 3
  NeverWrap = 2
  None = 0

class RibbonSeparator(RibbonItem):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    S
    
    e
    
    p
    
    a
    
    r
    
    a
    
    t
    
    o
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to copy the data.
        """
        pass
    
    
    SeparatorStyle = None
    
    pass

  Line = 1
  Spacer = 2

class RibbonSplitButton(RibbonItem, IImageContainer, ICustomizationContainer):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    S
    
    p
    
    l
    
    i
    
    t
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input RibbonItem being copied from.
        """
        pass
    
    
    Command = None
    
    
    Grouping = None
    
    
    ListStyle = None
    
    
    TooltipTitle = None
    
    
    ButtonStyle = None
    
    
    Behavior = None
    
    
    Items = None
    
    
    ContainerCollection = None
    
    
    SmallImage = None
    
    
    LargeImage = None
    
    
    KeyTip = None
    
    pass

  DropDownFollow = 1
  DropDownNoFollow = 2
  SplitFollow = 3
  SplitFollowStaticText = 5
  SplitNoFollow = 4

  Descriptive = 3
  Icon = 1
  IconText = 2

class RibbonTabSelector(RibbonItem):
    """
    
    """
    def Append(self):
        """
        Append -> bool
            
            string sId: 
            Input the identifier of the tab to be added.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            string sId: 
            Input the identifier of the tab to find.
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which the to copy the data.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> bool
            
            string sId: 
            Id of the tab to be inserted.
            
            string sInsertBefore: 
            The new tab will be placed before this tab.
        """
        pass
    
    
    def Remove(self):
        """
        Remove -> bool
            
            string sId: 
            Input the string Id of the tab to be removed.
        """
        pass
    
    
    Rule = None
    
    
    Tabs = None
    
    pass

class RibbonTabSelectorCollection(RibbonItemsCollectionBase):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    e
    
    l
    
    e
    
    c
    
    t
    
    o
    
    r
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    o
    
    w
    
    n
    
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
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
    .
    """
    def Clone(self):
        """
        Clone -> RibbonTabSelector
            
            RibbonTabSelector source: 
            Source RibbonTabSelector
            
            RibbonTabSelector insertBefore: 
            RibbonTabSelector to insert this one before.
        """
        pass
    
    pass

class RibbonTabSource(RibbonItem, ICustomizationContainer):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    r
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
    .
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to copy the data.
        """
        pass
    
    
    def Find(self):
        """
        Find -> RibbonPanelSourceReference
            
            string id: 
            Input the string that identifies the RibbonPanelSourceReference to find.
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    DefaultDisplay = None
    
    
    DisplayType = None
    
    
    Items = None
    
    
    Name = None
    
    
    WorkspaceBehavior = None
    
    
    KeyTip = None
    
    pass

class RibbonTabSourceCollection(RibbonItemsCollectionBase<RibbonTabSource>):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    o
    
    w
    
    n
    
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
    
     
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    b
    
    e
    
    l
    
    o
    
    n
    
    g
    
    s
    
    .
    """
    def Clone(self):
        """
        Clone -> RibbonTabSource
            
            RibbonTabSource source: 
            Input the source RibbonTabSource to clone and insert.
            
            RibbonTabSource insertBefore: 
            Input the RibbonTabSource before which the source is to be inserted in the collection.
        """
        pass
    
    pass

class RibbonToggleButton(RibbonItem):
    """
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    o
    
    g
    
    g
    
    l
    
    e
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RibbonItem source: 
            Input the RibbonItem from which to the copy the data.
        """
        pass
    
    
    ButtonStyle = None
    
    
    KeyTip = None
    
    pass

class ScreenMenu(CustomizationElement, ICustomizationContainer):
    """
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    (
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    (
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    l
    
    o
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
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
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    L
    
    i
    
    s
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    n
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    i
    
    n
    
    g
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    B
    
    l
    
    a
    
    n
    
    k
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    s
    
     
    
    :
    
     
    
    I
    
    f
    
     
    
    t
    
    r
    
    u
    
    e
    
    ,
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    s
    
     
    
    a
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    2
    
    2
    
     
    
    b
    
    l
    
    a
    
    n
    
    k
    
     
    
    l
    
    i
    
    n
    
    e
    
    s
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    s
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    l
    
    i
    
    n
    
    e
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    n
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    s
    
    t
    
    a
    
    r
    
    t
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    i
    
    n
    
    g
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    B
    
    l
    
    a
    
    n
    
    k
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    s
    
     
    
    :
    
     
    
    I
    
    f
    
     
    
    t
    
    r
    
    u
    
    e
    
    ,
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    s
    
     
    
    a
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    2
    
    2
    
     
    
    b
    
    l
    
    a
    
    n
    
    k
    
     
    
    l
    
    i
    
    n
    
    e
    
    s
    
    .
    """
    def AddBlankLine(self):
        """
        AddBlankLine -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    Name = None
    
    
    NumLines = None
    
    
    Parent = None
    
    
    ScreenMenuItems = None
    
    
    StartLine = None
    
    pass

class ScreenMenuCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ScreenMenu screenMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ScreenMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ScreenMenu[] array: 
            Input the target array
            
            int index: 
            Input the zero-based index in array at which copying begins
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ScreenMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ScreenMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ScreenMenu) -> void
            
            ScreenMenu element: 
            Input item to remove
        """
        pass
    
    pass

class ScreenMenuItem(CustomizationReference):
    """
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
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
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
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
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    :
    
     
    
    L
    
    o
    
    c
    
    a
    
    t
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    a
    
    t
    
     
    
    a
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    c
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    ,
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    s
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    s
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
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
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    .
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    ,
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
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
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    I
    
    n
    
    t
    
    3
    
    2
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
     
    
    L
    
    o
    
    c
    
    a
    
    t
    
    e
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    a
    
    t
    
     
    
    a
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    c
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    w
    
    i
    
    t
    
    h
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    S
    
    c
    
    r
    
    e
    
    e
    
    n
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    BlankLine = None
    
    
    Name = None
    
    
    Parent = None
    
    pass

class ScreenMenuItemCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ScreenMenuItem screenMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ScreenMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ScreenMenuItem[] array: 
            Input the target array
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ScreenMenuItem value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ScreenMenuItem value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(ScreenMenuItem) -> void
            
            ScreenMenuItem element: 
            Input the item to remove.
        """
        pass
    
    
    def RemoveRange(self):
        """
        RemoveRange -> void
            
            int startIndex: 
            Input the index at which to begin removal. The item at this index is included in the items removed.
            
            int endIndex: 
            Input the index at which to stop removing items. The item at this index is included in the items removed.
        """
        pass
    
    pass

  NameChanged
  KeyChanged

class ShortcutKeyChangedEventArgs(public sealed class ShortcutKeyChangedEventArgs):
    """
    
    S
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
    K
    
    e
    
    y
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    I
    
    S
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
    K
    
    e
    
    y
    
    C
    
    o
    
    m
    
    b
    
    o
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
    K
    
    e
    
    y
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    s
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
     
    
    k
    
    e
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    h
    
    o
    
    r
    
    t
    
    c
    
    u
    
    t
    
    K
    
    e
    
    y
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    A
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    e
    
    w
    
     
    
    a
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    ShortcutKeyAction = None
    
    
    ShortcutKeyChanged = None
    
    pass

class TabletMenu(CustomizationElement, ICustomizationContainer):
    """
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    d
    
    d
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    d
    
    d
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    i
    
    n
    
    t
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    d
    
    d
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    t
    
    r
    
    i
    
    n
    
    g
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
    e
    
    s
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    r
    
    o
    
    w
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    r
    
    o
    
    w
    
    s
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    t
    
    a
    
    b
    
    l
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
    
    
    
     
    
     
    
     
    
     
    
    i
    
    n
    
    t
    
     
    
    c
    
    o
    
    l
    
    u
    
    m
    
    n
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    u
    
    m
    
    b
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    c
    
    o
    
    l
    
    u
    
    m
    
    n
    
    s
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    t
    
    a
    
    b
    
    l
    
    e
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    (
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
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
    
     
    
    p
    
    o
    
    p
    
    u
    
    l
    
    a
    
    t
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    d
    
    d
    
    e
    
    d
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    (
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    M
    
    e
    
    n
    
    u
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
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
    
     
    
    p
    
    o
    
    p
    
    u
    
    l
    
    a
    
    t
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    t
    
    o
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    a
    
    d
    
    d
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    a
    
    b
    
    l
    
    e
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    def AddBlankLine(self):
        """
        AddBlankLine -> void
        
        """
        pass
    
    
    Aliases = None
    
    
    Columns = None
    
    
    ContainerCollection = None
    
    
    Parent = None
    
    
    Rows = None
    
    
    TabletArea = None
    
    
    TabletMenuItems = None
    
    pass

class TabletMenuCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            TabletMenu tabletMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            TabletMenu value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TabletMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            TabletMenu value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            TabletMenu value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove.
        Remove(TabletMenu) -> void
            
            TabletMenu element: 
            Input the item to remove.
        """
        pass
    
    pass

class TabletMenuItem(CustomizationReference):
    """
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    m
    
    e
    
    n
    
    t
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    m
    
    e
    
    n
    
    t
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    m
    
    e
    
    n
    
    t
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    i
    
    t
    
    e
    
    m
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    (
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    ,
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    m
    
    e
    
    n
    
    t
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    t
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    a
    
    b
    
    l
    
    e
    
    t
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    d
    
    a
    
    t
    
    a
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    t
    
    e
    
    m
    
    .
    """
    BlankLine = None
    
    
    Parent = None
    
    pass

class TabletMenuItemCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            TabletMenuItem tabletMenuItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            TabletMenuItem item: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TabletMenuItem[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            TabletMenuItem item: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            TabletMenuItem item: 
            Input the item to insert.
        """
        pass
    
    
    def InsertRange(self):
        """
        InsertRange -> void
            
            int startIndex: 
            Input the index at which to begin inserting.
            
            ArrayList newItems: 
            Input the array of items to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(TabletMenuItem) -> void
            
            TabletMenuItem element: 
            Input the item to remove.
        """
        pass
    
    
    def RemoveRange(self):
        """
        RemoveRange -> void
            
            int startIndex: 
            Input the index at which to begin removal. The item at this index is included in the items removed.
            
            int endIndex: 
            Input the index at which to stop removing items. The item at this index is included in the items removed.
        """
        pass
    
    pass

class TemporaryOverride(CustomizationElement, IShortcutKeyCombo):
    """
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    K
    
    e
    
    y
    
    D
    
    o
    
    w
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
     
    
    o
    
    n
    
     
    
    k
    
    e
    
    y
    
     
    
    d
    
    o
    
    w
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    m
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    K
    
    e
    
    y
    
    U
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    e
    
    x
    
    e
    
    c
    
    u
    
    t
    
    e
    
     
    
    o
    
    n
    
     
    
    k
    
    e
    
    y
    
     
    
    u
    
    p
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    o
    
    v
    
    e
    
    r
    
    r
    
    i
    
    d
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    e
    
    m
    
    p
    
    o
    
    r
    
    a
    
    r
    
    y
    
    O
    
    v
    
    e
    
    r
    
    r
    
    r
    
    i
    
    d
    
    e
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    """
    def ShortcutKey(self):
        """
        ShortcutKey -> string
        
        """
        pass
    
    
    def ShortcutName(self):
        """
        ShortcutName -> string
        
        """
        pass
    
    
    Description = None
    
    
    DownOverride = None
    
    
    Name = None
    
    
    OverrideShortcutKey = None
    
    
    Parent = None
    
    
    UpOverride = None
    
    pass

class TemporaryOverrideCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            TemporaryOverride temporaryOverride: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            TemporaryOverride value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            TemporaryOverride[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            TemporaryOverride value: 
            Input the item to find.
        """
        pass
    
    
    def FindTemporaryOverrideWithName(self):
        """
        FindTemporaryOverrideWithName -> TemporaryOverride
            
            name: 
            The name of the override.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            TemporaryOverride value: 
            Input the item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string name: 
            Input the name for which to search.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(TemporaryOverride) -> void
            
            TemporaryOverride element: 
            Input the item to remove.
        """
        pass
    
    pass

class ToolPanel(Toolbar, ICustomizationContainer):
    """
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    b
    
    F
    
    o
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    r
    
    u
    
    e
    
     
    
    i
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
     
    
    s
    
    h
    
    o
    
    u
    
    l
    
    d
    
     
    
    h
    
    a
    
    v
    
    e
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    s
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    a
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    a
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    U
    
    I
    
    D
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    a
    
     
    
    u
    
    n
    
    i
    
    q
    
    u
    
    e
    
     
    
    I
    
    D
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    (
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
     
    
    t
    
    o
    
    o
    
    l
    
    p
    
    a
    
    n
    
    e
    
    l
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    i
    
    t
    
    s
    
     
    
    a
    
    r
    
    r
    
    a
    
    y
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
    .
    """
    def indexOfRowBreak(self):
        """
        indexOfRowBreak -> Integer
            
            int row: 
            Input row index
        """
        pass
    
    
    def indexOfRowStart(self):
        """
        indexOfRowStart -> Integer
            
            int row: 
            Input row index
        """
        pass
    
    
    Parent = None
    
    
    Rows = None
    
    pass

class ToolPanelCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            ToolPanel toolpanel: 
            Input the object to add.
        """
        pass
    
    
    def AddToolPanel(self):
        """
        AddToolPanel -> bool
            
            ToolPanel toolpanel: 
            Input the tool panel to append to.
            
            object obj: 
            Input the object to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ToolPanel value: 
            Input the object to check.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ToolPanel[] array: 
            Input the object to be copied.
            
            int index: 
            Input the object acting as the array index.
        """
        pass
    
    
    def FindToolPanelWithAlias(self):
        """
        FindToolPanelWithAlias -> ToolPanel
            
            string toolpanelAlias: 
            Input the alias to search by.
        """
        pass
    
    
    def FindToolPanelWithName(self):
        """
        FindToolPanelWithName -> ToolPanel
            
            string toolpanelName: 
            Input the name of the tool panel.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ToolPanel value: 
            Input a tool panel to seek.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input a zero-based array index.
            
            ToolPanel value: 
            Input an object to add.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string toolpanelName: 
            Input the object name to seek.
        """
        pass
    
    
    def NextName(self):
        """
        NextName -> string
        
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ToolPanel) -> void
            
            ToolPanel toolpanel: 
            Input the item to remove
        """
        pass
    
    
    AllAliases = None
    
    pass

class ToolPanelNameChangedEventArgs(public sealed class ToolPanelNameChangedEventArgs):
    """
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    N
    
    a
    
    m
    
    e
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
     
    
    t
    
    o
    
    o
    
    l
    
    p
    
    a
    
    n
    
    e
    
    l
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    r
    
    e
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    l
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
    .
    """
    OldToolPanelName = None
    
    
    ToolPanelChanged = None
    
    pass

class ToolPanelRef(VersionableElement):
    """
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
    R
    
    e
    
    f
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    P
    
    a
    
    n
    
    e
    
    l
    
     
    
    t
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    ,
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    
     
    
    t
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    ,
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    s
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    a
    
    n
    
    e
    
    l
    
    P
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    n
    
    e
    
    l
    
     
    
    p
    
    o
    
    s
    
    i
    
    t
    
    i
    
    o
    
    n
    
    ,
    
     
    
    w
    
    h
    
    e
    
    t
    
    h
    
    e
    
    r
    
     
    
    u
    
    p
    
    p
    
    e
    
    r
    
     
    
    o
    
    r
    
     
    
    l
    
    o
    
    w
    
    e
    
    r
    
    .
    """
    PanelReference = None
    
    
    Parent = None
    
    pass

class ToolTip(ElementBase):
    """
    
    T
    
    o
    
    o
    
    l
    
    T
    
    i
    
    p
    
    (
    
    M
    
    a
    
    c
    
    r
    
    o
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    T
    
    i
    
    p
    
    (
    
    M
    
    a
    
    c
    
    r
    
    o
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    T
    
    i
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    T
    
    i
    
    p
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    """
    BasicContent = None
    
    
    CommandName = None
    
    
    EnableHelp = None
    
    
    ExtendedHelpFile = None
    
    
    HasBasicContent = None
    
    
    HasCommandName = None
    
    
    HasEnableHelp = None
    
    
    HasHelpSource = None
    
    
    HasHelpTopic = None
    
    
    HelpSource = None
    
    
    HelpTopic = None
    
    
    Parent = None
    
    pass

class ToolTipContent(public sealed class ToolTipContent):
    """
    
    """
    SourceKey = None
    
    
    UriSource = None
    
    pass

class Toolbar(CustomizationElement, ICustomizationContainer):
    """
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    c
    
    o
    
    p
    
    i
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    M
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    Aliases = None
    
    
    ContainerCollection = None
    
    
    Description = None
    
    
    Name = None
    
    
    Parent = None
    
    
    Rows = None
    
    
    ToolbarItems = None
    
    
    ToolbarOrient = None
    
    
    ToolbarVisible = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class ToolbarButton(ToolbarItemBase, IReference):
    """
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
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
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    a
    
    c
    
    r
    
    o
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    U
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
     
    
    t
    
    o
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    e
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    a
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
    '
    
    s
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    t
    
    i
    
    p
    
    ,
    
     
    
    i
    
    f
    
     
    
    d
    
    i
    
    f
    
    f
    
    e
    
    r
    
    e
    
    n
    
    t
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    M
    
    e
    
    n
    
    u
    
    M
    
    a
    
    c
    
    r
    
    o
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    n
    
    e
    
    w
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    I
    
    t
    
    e
    
    m
    
     
    
    i
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    (
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    (
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
     
    
    i
    
    n
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    (
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    B
    
    u
    
    t
    
    t
    
    o
    
    n
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
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
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
     
    
    d
    
    a
    
    t
    
    a
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    b
    
    u
    
    t
    
    t
    
    o
    
    n
    
     
    
    i
    
    n
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    """
    DrawSeparator = None
    
    
    IsRowBreak = None
    
    
    IsSeparator = None
    
    
    Loader = None
    
    
    MacroID = None
    
    
    MenuMacroReference = None
    
    
    Name = None
    
    pass

class ToolbarCollection(MenuGroupItemsCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Toolbar toolbar: 
            Input the item to add.
        """
        pass
    
    
    def AddToolbar(self):
        """
        AddToolbar -> bool
            
            Toolbar toolbar: 
            Input the toolbar to add.
            
            object obj: 
            Input the toolbar to insert at beginning of the collection. If obj is null or is not found in the collection, the toolbar is appended to the end.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Toolbar value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Toolbar[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindToolbarWithAlias(self):
        """
        FindToolbarWithAlias -> Toolbar
            
            string toolbarAlias: 
            Input the alias for which to search.
        """
        pass
    
    
    def FindToolbarWithName(self):
        """
        FindToolbarWithName -> Toolbar
            
            string toolbarName: 
            Input the name for which to search.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Toolbar value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            Toolbar value: 
            Input the item to insert.
        """
        pass
    
    
    def IsNameFree(self):
        """
        IsNameFree -> bool
            
            string toolbarName: 
            Input the name for which to search.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(Toolbar) -> void
            
            Toolbar toolbar: 
            Input the item to remove
        """
        pass
    
    
    AllAliases = None
    
    pass

class ToolbarControl(ToolbarItemBase):
    """
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    C
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    t
    
    o
    
     
    
    d
    
    u
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    r
    
    o
    
    l
    
     
    
    i
    
    n
    
    t
    
    o
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    """
    ControlType = None
    
    
    Loader = None
    
    pass

class ToolbarFlyout(ToolbarItemBase):
    """
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    b
    
    o
    
    o
    
    l
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
     
    
    i
    
    f
    
     
    
    d
    
    i
    
    f
    
    f
    
    e
    
    r
    
    e
    
    n
    
    t
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
     
    
    T
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    a
    
    s
    
     
    
    a
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    t
    
    i
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    u
    
    i
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    u
    
    n
    
    i
    
    q
    
    u
    
    e
    
     
    
    I
    
    D
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
     
    
    I
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    g
    
    i
    
    v
    
    e
    
    n
    
     
    
    I
    
    D
    
     
    
    i
    
    s
    
     
    
    a
    
    l
    
    r
    
    e
    
    a
    
    d
    
    y
    
     
    
    i
    
    n
    
     
    
    u
    
    s
    
    e
    
    ,
    
     
    
    a
    
     
    
    n
    
    e
    
    w
    
     
    
    o
    
    n
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    b
    
    e
    
     
    
    g
    
    e
    
    n
    
    e
    
    r
    
    a
    
    t
    
    e
    
    d
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    r
    
    e
    
    f
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
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
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    t
    
    o
    
     
    
    r
    
    e
    
    f
    
    e
    
    r
    
    e
    
    n
    
    c
    
    e
    
     
    
    a
    
    s
    
     
    
    a
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    m
    
    l
    
    I
    
    m
    
    a
    
    g
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    w
    
    h
    
    e
    
    n
    
     
    
    i
    
    t
    
     
    
    i
    
    s
    
     
    
    s
    
    e
    
    t
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    s
    
    m
    
    a
    
    l
    
    l
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    l
    
    g
    
    I
    
    m
    
    a
    
    g
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    w
    
    h
    
    e
    
    n
    
     
    
    i
    
    t
    
     
    
    i
    
    s
    
     
    
    s
    
    e
    
    t
    
     
    
    t
    
    o
    
     
    
    u
    
    s
    
    e
    
     
    
    l
    
    a
    
    r
    
    g
    
    e
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    b
    
    o
    
    o
    
    l
    
     
    
    b
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    O
    
    w
    
    n
    
    I
    
    c
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    f
    
     
    
    s
    
    e
    
    t
    
     
    
    t
    
    o
    
     
    
    t
    
    r
    
    u
    
    e
    
    ,
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    u
    
    s
    
    e
    
    s
    
     
    
    i
    
    t
    
    s
    
     
    
    o
    
    w
    
    n
    
     
    
    i
    
    m
    
    a
    
    g
    
    e
    
    s
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
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
    
    ,
    
     
    
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
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
     
    
    i
    
    f
    
     
    
    d
    
    i
    
    f
    
    f
    
    e
    
    r
    
    e
    
    n
    
    t
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
     
    
    T
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    a
    
    s
    
     
    
    a
    
     
    
    t
    
    o
    
    o
    
    l
    
     
    
    t
    
    i
    
    p
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    e
    
    s
    
    c
    
    r
    
    i
    
    p
    
    t
    
    i
    
    o
    
    n
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    .
    
     
    
    T
    
    h
    
    i
    
    s
    
     
    
    w
    
    i
    
    l
    
    l
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    o
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    t
    
    a
    
    t
    
    u
    
    s
    
     
    
    b
    
    a
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    m
    
    e
    
    n
    
    u
    
    G
    
    r
    
    o
    
    u
    
    p
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    a
    
    r
    
    g
    
    e
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    s
    
    e
    
    a
    
    r
    
    c
    
    h
    
    A
    
    l
    
    i
    
    a
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    a
    
    l
    
    i
    
    a
    
    s
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    t
    
    a
    
    r
    
    g
    
    e
    
    t
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
    (
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
    (
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    ,
    
     
    
    i
    
    n
    
    t
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
     
    
    f
    
    l
    
    y
    
    I
    
    n
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    F
    
    l
    
    y
    
    o
    
    u
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    l
    
    o
    
    n
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    i
    
    n
    
    d
    
    e
    
    x
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    a
    
    t
    
     
    
    w
    
    h
    
    i
    
    c
    
    h
    
     
    
    t
    
    o
    
     
    
    i
    
    n
    
    s
    
    e
    
    r
    
    t
    
     
    
    f
    
    l
    
    y
    
    o
    
    u
    
    t
    
    .
    """
    Description = None
    
    
    FlyoutName = None
    
    
    IsCircular = None
    
    
    LargeImage = None
    
    
    Loader = None
    
    
    MenuGroup = None
    
    
    SmallImage = None
    
    
    ToolbarReference = None
    
    
    UnqualifiedAlias = None
    
    
    UseOwnIcon = None
    
    pass

class ToolbarItemBase(CustomizationElement):
    """
    
    """
    Parent = None
    
    pass

class ToolbarItemCollection(CustomizationCollection):
    """
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    I
    
    t
    
    e
    
    m
    
    C
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    E
    
    l
    
    e
    
    m
    
    e
    
    n
    
    t
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    o
    
    w
    
    n
    
    e
    
    r
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    c
    
    o
    
    l
    
    l
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    """
    def Add(self):
        """
        Add -> void
            
            ToolbarItemBase toolbarItem: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            ToolbarItemBase value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            ToolbarItemBase[] array: 
            Input the target array
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            ToolbarItemBase value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            ToolbarItemBase value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove
        Remove(ToolbarItemBase) -> void
            
            ToolbarItemBase element: 
            Input the item to remove
        """
        pass
    
    pass

class ToolbarNameChangedEventArgs(public sealed class ToolbarNameChangedEventArgs):
    """
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    N
    
    a
    
    m
    
    e
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
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
    
     
    
    m
    
    o
    
    d
    
    i
    
    f
    
    i
    
    e
    
    d
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    l
    
    d
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    l
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
    .
    """
    OldToolbarName = None
    
    
    ToolbarChanged = None
    
    pass

  bottom = 3
  floating = 1
  left = 4
  right = 5
  top = 2

  hide = 0
  show = 1

  None
  New
  Modified

class Util(public class Util):
    """
    
    """
    def IsEmpty(self):
        """
        IsEmpty -> bool
            
            string s: 
            Input the object which is to be tested.
        """
        pass
    
    
    def IsEqualNoCase(self):
        """
        IsEqualNoCase -> bool
            
            string s1: 
            Input System.String object, the first string to compare.
            
            string s2: 
            Input System.String object, the second string to compare.
        """
        pass
    
    pass

CurrentVersion = 12
TwoThousandEight = 2
TwoThousandEleven = 5
TwoThousandFifteen = 9
TwoThousandFourteen = 8
TwoThousandNine = 3
TwoThousandSeven = 1
TwoThousandSeventeen = 11
TwoThousandSix = 0
TwoThousandSixteen = 10
TwoThousandTen = 4
TwoThousandThirteen = 7
TwoThousandTwelve = 6
Unknown = 13

class VersionableElement(ElementBase):
    """
    
    """
    def addInternalUseProperties(self):
        """
        addInternalUseProperties -> void
        
        """
        pass
    
    
    def FireModifiedEvent(self):
        """
        FireModifiedEvent -> void
        
        """
        pass
    
    
    def SetRevision(self):
        """
        SetRevision -> void
        
        """
        pass
    
    
    def UserModified(self):
        """
        UserModified -> bool
        
        """
        pass
    
    
    ModifiedRevision = None
    
    pass

class WSRibbonPanelSourceReference(CustomizationElement):
    """
    
    W
    
    S
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    P
    
    a
    
    n
    
    e
    
    l
    
    S
    
    o
    
    u
    
    r
    
    c
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    S
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
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
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    """
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            WSRibbonPanelSourceReference item: 
            Input the WSRibbonPanelSourceReference from which to copy the data.
        """
        pass
    
    
    def Create(self):
        """
        Create -> WSRibbonPanelSourceReference
            
            RibbonPanelSourceReference panelSourceref: 
            Input the RibbonPanelSourceReference from which the item is to be created.
        """
        pass
    
    
    def FindPanelSource(self):
        """
        FindPanelSource -> RibbonPanelSource
            
            Collection<CustomizationSection> cuiFiles: 
            CUI files to be searched.
        """
        pass
    
    
    FloatingGroup = None
    
    
    FloatingOrder = None
    
    
    FloatingOrientation = None
    
    
    Orientation = None
    
    
    PanelId = None
    
    
    Show = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class WSRibbonRoot(CustomizationElement):
    """
    
    """
    def Clone(self):
        """
        Clone -> WSRibbonRoot
        
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            WSRibbonRoot item: 
            Input the WSRibbonRoot from which to copy the data.
        """
        pass
    
    
    def FindTabReference(self):
        """
        FindTabReference -> WSRibbonTabSourceReference
            
            string sMenuGroupName: 
            Input the name of the menu group.
            
            string id: 
            Input the string Id of the WSRibbonTabSourceReference to find.
        """
        pass
    
    
    AutoHideMode = None
    
    
    LockMode = None
    
    
    ShowPanelTitleInHorizontalOrientation = None
    
    
    ShowPanelTitleInVerticalOrientation = None
    
    
    WorkspaceTabs = None
    
    pass

class WSRibbonTabSourceReference(CustomizationElement):
    """
    
    W
    
    S
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    T
    
    a
    
    b
    
    S
    
    o
    
    u
    
    r
    
    c
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    S
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    W
    
    S
    
    R
    
    i
    
    b
    
    b
    
    o
    
    n
    
    R
    
    o
    
    o
    
    t
    
    .
    """
    TabId Field = None
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            WSRibbonTabSourceReference item: 
            Input the WSRibbonTabSourceReference from which to copy the data.
        """
        pass
    
    
    def Create(self):
        """
        Create -> WSRibbonTabSourceReference
            
            RibbonTabSource tabSource: 
            input the RibbonTabSource from which to create the WSRibbonTabSourceReference object.
        """
        pass
    
    
    def Find(self):
        """
        Find -> WSRibbonPanelSourceReference
            
            string panelId: 
            Input the string Id of the WSRibbonPanelSourceReference to find.
        """
        pass
    
    
    def FindTabSource(self):
        """
        FindTabSource -> RibbonTabSource
            
            Collection<CustomizationSection> cuiFiles: 
            CUI files to be searched.
        """
        pass
    
    
    IsActive = None
    
    
    MenuGroup = None
    
    
    Panels = None
    
    
    Show = None
    
    pass

class WSToolbarChangedEventArgs(public sealed class WSToolbarChangedEventArgs):
    """
    
    W
    
    S
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    C
    
    h
    
    a
    
    n
    
    g
    
    e
    
    d
    
    E
    
    v
    
    e
    
    n
    
    t
    
    A
    
    r
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    w
    
    s
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
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
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    """
    WorkspaceToolbarChanged = None
    
    pass

class Workspace(CustomizationElement):
    """
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    u
    
    s
    
    t
    
    o
    
    m
    
    i
    
    z
    
    a
    
    t
    
    i
    
    o
    
    n
    
    S
    
    e
    
    c
    
    t
    
    i
    
    o
    
    n
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    t
    
    o
    
     
    
    s
    
    e
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    """
    DefaultWorkspace = None
    
    
    Description = None
    
    
    WorkspaceRibbonRoot = None
    
    
    DockableWindows = None
    
    
    LayoutModelTabs = None
    
    
    Name = None
    
    
    Parent = None
    
    
    ScreenMenus = None
    
    
    Script = None
    
    
    ScrollBars = None
    
    
    StatusBar = None
    
    
    StartOn = None
    
    
    WorkspacePopMenus = None
    
    
    WorkspaceToolbars = None
    
    pass

class WorkspaceCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            Workspace workspace: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            Workspace value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            Workspace[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            Workspace value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            Workspace value: 
            Input the item to insert.
        """
        pass
    
    
    def SetDefaultWorkspaceByName(self):
        """
        SetDefaultWorkspaceByName -> bool
            
            workspaceName: 
            The name of a workspace to set as the default in the menu.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of the item to remove.
        Remove(Workspace) -> void
            
            Workspace Workspace: 
            Input the item to remove.
        """
        pass
    
    
    def SetDefaultWorkspace(self):
        """
        SetDefaultWorkspace -> bool
            
            string elementId: 
            Input the ID of the workspace.
        """
        pass
    
    
    Owner = None
    
    pass

class WorkspaceDockableWindow(CustomizationElement):
    """
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    D
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    l
    
    a
    
    s
    
    s
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    G
    
    U
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    l
    
    a
    
    s
    
    s
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    s
    
    t
    
    o
    
    r
    
    e
    
    d
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    e
    
    g
    
    i
    
    s
    
    t
    
    r
    
    y
    
     
    
    t
    
    o
    
     
    
    i
    
    d
    
    e
    
    n
    
    t
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    
    
    
    
    
    
    
    
    
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    D
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
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
    
    ,
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    l
    
    a
    
    s
    
    s
    
    N
    
    a
    
    m
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    G
    
    U
    
    I
    
    D
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    l
    
    a
    
    s
    
    s
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    i
    
    s
    
     
    
    s
    
    t
    
    o
    
    r
    
    e
    
    d
    
     
    
    i
    
    n
    
     
    
    t
    
    h
    
    e
    
     
    
    r
    
    e
    
    g
    
    i
    
    s
    
    t
    
    r
    
    y
    
     
    
    t
    
    o
    
     
    
    i
    
    d
    
    e
    
    n
    
    t
    
    i
    
    f
    
    y
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
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
    
     
    
    t
    
    h
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    a
    
    s
    
    s
    
    o
    
    c
    
    i
    
    a
    
    t
    
    e
    
    d
    
     
    
    w
    
    i
    
    t
    
    h
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
     
    
    i
    
    n
    
     
    
    o
    
    r
    
    d
    
    e
    
    r
    
     
    
    t
    
    o
    
     
    
    d
    
    i
    
    s
    
    p
    
    l
    
    a
    
    y
    
     
    
    i
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    D
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    D
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    D
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
    W
    
    i
    
    n
    
    d
    
    o
    
    w
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    d
    
    o
    
    c
    
    k
    
    a
    
    b
    
    l
    
    e
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
     
    
    w
    
    h
    
    o
    
    s
    
    e
    
     
    
    p
    
    r
    
    o
    
    p
    
    e
    
    r
    
    t
    
    i
    
    e
    
    s
    
     
    
    a
    
    r
    
    e
    
     
    
    t
    
    o
    
     
    
    b
    
    e
    
     
    
    a
    
    p
    
    p
    
    l
    
    i
    
    e
    
    d
    
     
    
    t
    
    o
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    w
    
    i
    
    n
    
    d
    
    o
    
    w
    
    .
    """
    AllowDock = None
    
    
    AutoHide = None
    
    
    ClassName = None
    
    
    DefaultGroup = None
    
    
    Display = None
    
    
    DockColumn = None
    
    
    DockFloat = None
    
    
    DockHeight = None
    
    
    DockRow = None
    
    
    DockWidth = None
    
    
    Height = None
    
    
    Name = None
    
    
    Orientation = None
    
    
    Parent = None
    
    
    TransparencyAmount = None
    
    
    UseTransparency = None
    
    
    Width = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class WorkspaceDockableWindowCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WorkspaceDockableWindow workspaceDockableWindow: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WorkspaceDockableWindow value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WorkspaceDockableWindow[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def FindDockableWindow(self):
        """
        FindDockableWindow -> WorkspaceDockableWindow
            
            string windowName: 
            Input the name to search for.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WorkspaceDockableWindow value: 
            Input the item to find.
        """
        pass
    
    
    def IndexOfClassName(self):
        """
        IndexOfClassName -> Integer
            
            string className: 
            Input a GUID that is read from the registry and uniquely identifies a dockable window.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            WorkspaceDockableWindow value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(WorkspaceDockableWindow) -> void
            
            WorkspaceDockableWindow workspaceDockableWindow: 
            Input the item to remove.
        """
        pass
    
    pass

class WorkspacePopMenu(CustomizationElement):
    """
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    p
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    p
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    P
    
    o
    
    p
    
    M
    
    e
    
    n
    
    u
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    o
    
    p
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    t
    
    h
    
    a
    
    t
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
     
    
    r
    
    e
    
    p
    
    r
    
    e
    
    s
    
    e
    
    n
    
    t
    
    s
    
    .
    """
    Display Field = None
    
    
    MenuGroup Field = None
    
    
    PopMenuID Field = None
    
    
    Parent = None
    
    pass

class WorkspacePopMenuCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WorkspacePopMenu workspacePopMenu: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WorkspacePopMenu element: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WorkspacePopMenu[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index in array at which copying begins.
        """
        pass
    
    
    def FindWorkspacePopMenu(self):
        """
        FindWorkspacePopMenu -> WorkspacePopMenu
            
            string popMenuElementId: 
            Input the pop menu to be found.
            
            string MenuGroup: 
            Input the menu group of given pop menu.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WorkspacePopMenu element: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            WorkspacePopMenu element: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(WorkspacePopMenu) -> void
            
            WorkspacePopMenu workspacePopMenu: 
            Input the item to remove.
        """
        pass
    
    pass

class WorkspaceQuickAccessToolbar(CustomizationElement):
    """
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    P
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    q
    
    a
    
    t
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    :
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    .
    
    
    
    
    
    
    
    
    
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    S
    
    e
    
    t
    
    s
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    Q
    
    u
    
    i
    
    c
    
    k
    
    A
    
    c
    
    c
    
    e
    
    s
    
    s
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    f
    
    r
    
    o
    
    m
    
    W
    
    Q
    
    A
    
    T
    
     
    
    :
    
     
    
    S
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
    t
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
     
    
    f
    
    r
    
    o
    
    m
    
    .
    """
    MenuGroup = None
    
    
    Parent = None
    
    
    ToolbarId = None
    
    pass

class WorkspaceRibbonPanelCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WSRibbonPanelSourceReference wsPanel: 
            Input the WSRibbonPanelSourceReference to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WSRibbonPanelSourceReference value: 
            Input the WSRibbonPanelSourceReference to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WSRibbonPanelSourceReference[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based index of the target array where the copy begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WSRibbonPanelSourceReference value: 
            Input the WSRibbonPanelSourceReference to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index where the insert is to take place.
            
            WSRibbonPanelSourceReference value: 
            Input the WSRibbonPanelSourceReference to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(WSRibbonPanelSourceReference) -> void
            
            WSRibbonPanelSourceReference panel: 
            Input the WSRibbonPanelSourceReference to remove.
        Remove(int) -> void
            
            int index: 
            Input the index of the WSRibbonPanelSourceReference to remove.
        """
        pass
    
    pass

class WorkspaceRibbonTabCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WSRibbonTabSourceReference wsTab: 
            Item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WSRibbonTabSourceReference value: 
            Item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WSRibbonTabSourceReference[] array: 
            Target array.
            
            int index: 
            The zero-based index in array at which copying begins.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WSRibbonTabSourceReference value: 
            Item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Zero based index.
            
            WSRibbonTabSourceReference value: 
            Item to insert
        """
        pass
    
    
    def Remove(self):
        """
        Remove(WSRibbonTabSourceReference) -> void
            
            WSRibbonTabSourceReference wsTab: 
            Item to remove.
        Remove(int) -> void
            
            int index: 
            Index of item to remove.
        """
        pass
    
    pass

class WorkspaceToolbar(CustomizationElement):
    """
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    t
    
    o
    
    o
    
    l
    
    b
    
    a
    
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
    
     
    
    c
    
    o
    
    n
    
    t
    
    a
    
    i
    
    n
    
    m
    
    e
    
    n
    
    t
    
     
    
    o
    
    b
    
    j
    
    e
    
    c
    
    t
    
    .
    
    
    
    
    
    
    
    
    
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    (
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    ,
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    p
    
    a
    
    r
    
    e
    
    n
    
    t
    
     
    
    w
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    W
    
    o
    
    r
    
    k
    
    s
    
    p
    
    a
    
    c
    
    e
    
    T
    
    o
    
    o
    
    l
    
    b
    
    a
    
    r
    
     
    
    f
    
    r
    
    o
    
    m
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    t
    
    h
    
    e
    
     
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
     
    
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
    
    o
    
     
    
    c
    
    o
    
    p
    
    y
    
    .
    """
    Display = None
    
    
    DockColumn = None
    
    
    DockRow = None
    
    
    MenuGroup = None
    
    
    Parent = None
    
    
    Rows = None
    
    
    ToolbarId = None
    
    
    ToolbarOrient = None
    
    
    XCoordinate = None
    
    
    YCoordinate = None
    
    pass

class WorkspaceToolbarCollection(CustomizationCollection):
    """
    
    """
    def Add(self):
        """
        Add -> void
            
            WorkspaceToolbar workspaceToolbar: 
            Input the item to add.
        """
        pass
    
    
    def Contains(self):
        """
        Contains -> bool
            
            WorkspaceToolbar value: 
            Input the item to find.
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            WorkspaceToolbar[] array: 
            Input the target array.
            
            int index: 
            Input the zero-based array index at which copying begins.
        """
        pass
    
    
    def FindWorkspaceToolbar(self):
        """
        FindWorkspaceToolbar -> WorkspaceToolbar
            
            string toolbarElementId: 
            Input the element ID of toolbar to be found.
            
            string menuGroup: 
            Input the menu group of toolbar to be found.
        """
        pass
    
    
    def IndexOf(self):
        """
        IndexOf -> Integer
            
            WorkspaceToolbar value: 
            Input the item to find.
        """
        pass
    
    
    def Insert(self):
        """
        Insert -> void
            
            int index: 
            Input the zero-based index.
            
            WorkspaceToolbar value: 
            Input the item to insert.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> void
            
            int index: 
            Input the index of item to remove.
        Remove(WorkspaceToolbar) -> void
            
            WorkspaceToolbar workspaceToolbar: 
            Input the item to remove.
        """
        pass
    
    pass

  ignore = 2
  no = 0
  yes = 1