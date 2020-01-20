  Current = -1
  Degrees = 0
  DegreesMinutesSeconds = 1
  Grads = 2
  Radians = 3
  Surveyor = 4

class CommandClassAttribute(Attribute):
    """
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    C
    
    l
    
    a
    
    s
    
    s
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    T
    
    y
    
    p
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    """
    Type = None
    
    pass

  ActionMacro = &H8000000
  Defun = &H800
  DocExclusiveLock = &H100000
  DocReadLock = &H80000
  InProgress = &H400
  Interruptible = &H400000
  Modal = 0
  NoActionRecording = &H4000000
  NoBlockEditor = &H2000000
  NoHistory = &H800000
  NoInferConstraint = &H40000000
  NoInternalLock = &H20000
  NoMultiple = &H10
  NoNewStack = &H10000
  NoOem = &H100
  NoPaperSpace = &H40
  NoPerspective = 8
  NoTileMode = &H20
  NoUndoMarker = &H1000000
  Redraw = 4
  Session = &H200000
  TempShowDynDimension = -2147483648
  Transparent = 1
  Undefined = &H200
  UsePickSet = 2

class CommandMethodAttribute(Attribute, ICommandLineCallable):
    """
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    ,
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    n
    
    a
    
    m
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    I
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
    ,
    
     
    
    T
    
    y
    
    p
    
    e
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    o
    
    c
    
    a
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    I
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    y
    
    p
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
    M
    
    e
    
    n
    
    u
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
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
    
     
    
    c
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
    ,
    
     
    
    T
    
    y
    
    p
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    I
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    y
    
    p
    
    e
    
     
    
    c
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
    M
    
    e
    
    n
    
    u
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
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
    
     
    
    c
    
    o
    
    n
    
    t
    
    e
    
    x
    
    t
    
     
    
    m
    
    e
    
    n
    
    u
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    h
    
    e
    
    l
    
    p
    
    F
    
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
    
     
    
    h
    
    e
    
    l
    
    p
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
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
    
     
    
    h
    
    e
    
    l
    
    p
    
    T
    
    o
    
    p
    
    i
    
    c
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    h
    
    e
    
    l
    
    p
    
     
    
    t
    
    o
    
    p
    
    i
    
    c
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
    
    
    
    
    
    
    
    
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    M
    
    e
    
    t
    
    h
    
    o
    
    d
    
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
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
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
    
     
    
    g
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    r
    
    o
    
    u
    
    p
    
     
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
    I
    
    d
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    I
    
    d
    
    
    
    
     
    
     
    
     
    
     
    
    C
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
    F
    
    l
    
    a
    
    g
    
    s
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    o
    
    m
    
    m
    
    a
    
    n
    
    d
    
     
    
    f
    
    l
    
    a
    
    g
    
    s
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    h
    
    e
    
    l
    
    p
    
    T
    
    o
    
    p
    
    i
    
    c
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    h
    
    e
    
    l
    
    p
    
     
    
    t
    
    o
    
    p
    
    i
    
    c
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    """
    ContextMenuExtensionType = None
    
    
    Flags = None
    
    
    GlobalName = None
    
    
    GroupName = None
    
    
    HelpFileName = None
    
    
    HelpTopic = None
    
    
    LocalizedNameId = None
    
    pass

class Converter(public sealed class Converter):
    """
    
    """
    def AngleToString(self):
        """
        AngleToString(double) -> string
            
            double value: 
            Input value to convert
        AngleToString(double, AngularUnitFormat, int) -> string
            
            double value: 
            Input value to convert
            
            AngularUnitFormat units: 
            Input units to convert in
            
            int precision: 
            Input precision
        """
        pass
    
    
    def DistanceToString(self):
        """
        DistanceToString(double) -> string
            
            double value: 
            Input value to convert
        DistanceToString(double, DistanceUnitFormat, int) -> string
            
            double value: 
            Input value to convert
            
            DistanceUnitFormat units: 
            Input units to convert in
            
            int precision: 
            Input precision
        """
        pass
    
    
    def RawAngleToString(self):
        """
        RawAngleToString(double) -> string
            
            double value: 
            Input value to convert
        RawAngleToString(double, AngularUnitFormat, int) -> string
            
            double value: 
            Input value to convert
            
            AngularUnitFormat units: 
            Input units to convert in
            
            int precision: 
            Input precision
        """
        pass
    
    
    def StringToAngle(self):
        """
        StringToAngle(string) -> double
            
            string value: 
            Input value to convert
        StringToAngle(string, AngularUnitFormat) -> double
            
            string value: 
            Input value to convert
            
            AngularUnitFormat units: 
            Input units to convert in
        """
        pass
    
    
    def StringToDistance(self):
        """
        StringToDistance(string) -> double
            
            string value: 
            Input value to convert
        StringToDistance(string, DistanceUnitFormat) -> double
            
            string value: 
            Input value to convert
            
            DistanceUnitFormat units: 
            Input conversion units
        """
        pass
    
    
    def StringToRawAngle(self):
        """
        StringToRawAngle(string) -> double
            
            string value: 
            Input value to convert
        StringToRawAngle(string, AngularUnitFormat) -> double
            
            string value: 
            Input value to convert
            
            AngularUnitFormat units: 
            Input units to convert in
        """
        pass
    
    pass

class Dictionary(RXObject, IDictionary):
    """
    
    """
    def At(self):
        """
        At(int) -> RXObject
            
            int id: 
            Input dictionary entry ID of the object to retrieve.
        At(string) -> RXObject
            
            string key: 
            Input lookup key string to search for.
        """
        pass
    
    
    def AtKeyAndIdPut(self):
        """
        AtKeyAndIdPut -> void
            
            string newKey: 
            Input lookup key string to use.
            
            int id: 
            Input dictionary entry ID at which to put value.
            
            RXObject value: 
            Input object to add to the dictionary.
        """
        pass
    
    
    def AtPut(self):
        """
        AtPut(int, RXObject) -> RXObject
            
            int id: 
            Input dictionary entry ID at which to put value.
            
            RXObject value: 
            Input object to add to the dictionary.
        AtPut(string, RXObject) -> RXObject
            
            string key: 
            Input lookup key string to use.
            
            RXObject value: 
            Input item to add to the dictionary.
        AtPut(string, RXObject, out int) -> RXObject
            
            string key: 
            Input lookup key string to use.
            
            RXObject value: 
            Input object to add to the dictionary.
            
            out int retId: 
            Output dictionary entry ID for the newly entered value.
        """
        pass
    
    
    def Contains(self):
        """
        Contains(int) -> bool
            
            int id: 
            Input dictionary entry ID.
        Contains(string) -> bool
            
            string key: 
            Input key to check for
        """
        pass
    
    
    def CopyTo(self):
        """
        CopyTo -> void
            
            DictionaryEntry[] array: 
            Input array to copy to
            
            int index: 
            Input index to begin copying from
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IDictionaryEnumerator
        
        """
        pass
    
    
    def IdAt(self):
        """
        IdAt -> Integer
            
            string key: 
            Input lookup key string to search for.
        """
        pass
    
    
    def KeyAt(self):
        """
        KeyAt -> string
            
            int id: 
            Input dictionary entry ID to search for.
        """
        pass
    
    
    def Remove(self):
        """
        Remove(int) -> RXObject
            
            int id: 
            Input dictionary entry ID of the entry to remove.
        Remove(string) -> RXObject
            
            string key: 
            Input lookup key string for entry to be removed.
        """
        pass
    
    
    def ResetKey(self):
        """
        ResetKey(int, string) -> void
            
            int id: 
            Input dictionary entry ID at which to put value.
            
            string newKey: 
            Input new lookup key string to use.
        ResetKey(string, string) -> void
            
            string oldKey: 
            Input lookup key string to be found and changed.
            
            string newKey: 
            Input new lookup key string to use.
        """
        pass
    
    
    Count = None
    
    
    DeletesObjects = None
    
    
    IsCaseSensitive = None
    
    
    IsSorted = None
    
    pass

class DisposableWrapper(MarshalByRefObject, IDisposable):
    """
    
    D
    
    i
    
    s
    
    p
    
    o
    
    s
    
    a
    
    b
    
    l
    
    e
    
    W
    
    r
    
    a
    
    p
    
    p
    
    e
    
    r
    
    (
    
    )
    
    (
    
    )
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
    
    
    AutoDelete = None
    
    
    IsDisposed = None
    
    
    UnmanagedObject = None
    
    pass

  Architectural = 4
  Current = -1
  Decimal = 2
  Engineering = 3
  Fractional = 5
  Scientific = 1

class DynamicLinker(RXObject):
    """
    
    """
    def GetLoadedModules(self):
        """
        GetLoadedModules -> StringCollection
        
        """
        pass
    
    
    def IsAppBusy(self):
        """
        IsAppBusy -> bool
            
            string moduleName: 
            Input.
        """
        pass
    
    
    def IsApplicationLocked(self):
        """
        IsApplicationLocked -> bool
            
            string moduleName: 
            Input name of loaded ObjectARX program.
        """
        pass
    
    
    def IsAppMdiAware(self):
        """
        IsAppMdiAware -> bool
            
            string moduleName: 
            Input name of the module to check.
        """
        pass
    
    
    def IsModuleLoaded(self):
        """
        IsModuleLoaded -> bool
            
            string fileName: 
            Input name of the file to load.
        """
        pass
    
    
    def LoadApp(self):
        """
        LoadApp -> void
            
            string appName: 
            Input null-terminated string which is the application name (as set in the system registry) of the ObjectARX module to load
            
            [MarshalAs(UnmanagedType.U1)] bool printIt: 
            Input indicating whether or not to print load status message.
            
            [MarshalAs(UnmanagedType.U1)] bool asCmd: 
            Input indicating whether to load the application as if by user command.
        """
        pass
    
    
    def LoadModule(self):
        """
        LoadModule -> void
            
            string fileName: 
            Input name of the file to load.
            
            [MarshalAs(UnmanagedType.U1)] bool printIt: 
            Input indicating whether or not to print load status message.
            
            [MarshalAs(UnmanagedType.U1)] bool asCmd: 
            Input indicating whether to load the application as if by user command.
        """
        pass
    
    
    def SetAppBusy(self):
        """
        SetAppBusy -> void
            
            string moduleName: 
            Input.
            
            [MarshalAs(UnmanagedType.U1)] bool busyFlag: 
            Input.
        """
        pass
    
    
    def UnloadApp(self):
        """
        UnloadApp -> void
            
            string appName: 
            Input null-terminated string which is the application name (as set in the system registry) of the ObjectARX module to unload.
            
            [MarshalAs(UnmanagedType.U1)] bool asCmd: 
            Input indicating whether to unload the application as if by user command.
        """
        pass
    
    
    def UnloadModule(self):
        """
        UnloadModule -> void
            
            string fileName: 
            Input null-terminated string which is the file name of the program to unload.
            
            [MarshalAs(UnmanagedType.U1)] bool asCmd: 
            Input indicating whether to unload the application as if by user command.
        """
        pass
    
    
    ProductLcid = None
    
    pass

class DynamicLinkerEventArgs(EventArgs):
    """
    
    D
    
    y
    
    n
    
    a
    
    m
    
    i
    
    c
    
    L
    
    i
    
    n
    
    k
    
    e
    
    r
    
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
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    """
    FileName = None
    
    pass

class EnvVarExistsConditionAttribute(Attribute, ICondition):
    """
    
    E
    
    n
    
    v
    
    V
    
    a
    
    r
    
    E
    
    x
    
    i
    
    s
    
    t
    
    s
    
    C
    
    o
    
    n
    
    d
    
    i
    
    t
    
    i
    
    o
    
    n
    
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
    """
    def Evaluate(self):
        """
        Evaluate -> bool
        
        """
        pass
    
    pass

AlreadyActive = 0x4e53
AlreadyInactive = 0x4e54
AlreadyInDB = 0x1a
AlreadyInGroup = 260
AmbiguousInput = 4
AmbiguousOutput = 5
AnonymousEntry = 0x26
AtMaxReaders = 90
BackgroundPlotInProgress = 0x20f
BadColor = 0xd0
BadColorIndex = 0xca
BadDwgHeader = 0x13a
BadDxfFile = 0x170
BadDxfSequence = 0x34
BadLayerName = 200
BadLinetypeName = 0xcb
BadLinetypeScale = 0xcc
BadLineWeightValue = 0xcf
BadlyNestedAppData = 0x17a
BadPaperspaceView = 0xa9
BadPlotStyleName = 0x180
BadPlotStyleNameHandle = 0x183
BadPlotStyleType = 0x182
BadUcs = 0xa8
BadVisibilityValue = 0xcd
BinaryDataSizeExceeded = 0x187
BlockDefInEntitySection = 0x17d
BrokenHandle = 12
BufferTooSmall = 7
CannotBeErasedByCaller = 0x69
CannotBeResurrected = 0x6a
CannotChangeActiveViewport = 140
CannotChangeColumnType = 0x1b9
CannotExplodeEntity = 0x9f
CannotNestBlockDefinitions = 0x3b
CannotPlotToFile = 0x20c
CannotRestoreFromAcisFile = 300
CannotScaleNonUniformly = 0x88
CantOpenFile = 0x16c
CloseFailObjectDamaged = 0x68
CloseModifyAborted = 0x66
ClosePartialFailure = 0x67
CloseWasNotifying = 0x65
CommandWasInProgress = 0x8e
ContainerNotEmpty = 0x12
CopyDoesNotExist = 0x162
CopyFailed = 0x164
CopyInvalidName = 0x165
CopyIsModelSpace = 0x163
CopyNameExists = 0x166
CreateFailed = 0x151
CreateInvalidName = 0x152
CustomSizeNotPossible = 0x202
DatabaseObjectsOpen = 0x142
DataLinkAdapterNotFound = 650
DataLinkBadConnectionString = 0x28d
DataLinkConnectionFailed = 0x290
DataLinkInvalidAdapterId = 0x28b
DataLinkNotFound = 0x28c
DataLinkNotUpdatedYet = 0x28e
DataLinkOtherError = 660
DataLinkSourceIsWriteProtected = 0x292
DataLinkSourceNotFound = 0x28f
DegenerateGeometry = 0x99
DelDoesNotExist = 0x156
DeletedEntry = 0x1c
DeleteEntity = 0xbf
DelIsModelSpace = 0x157
DelLastLayout = 0x158
DelUnableToFind = 0x15a
DelUnableToSetCurrent = 0x159
DeviceNotFound = 0x1f8
DocumentSwitchDisabled = 0x14e
DuplicateBlockDefinition = 0x185
DuplicateBlockName = 0x181
DuplicateDxfField = 0x31
DuplicateIndex = 0x19
DuplicateKey = 0x17
DuplicateLayerName = 0x17f
DuplicateRecordName = 0x5f
DwgCrcDoesNotMatch = 0x41
DwgNeedsAFullSave = 0x45
DwgNeedsRecovery = 190
DwgNotRecoverable = 0x3d
DwgObjectImproperlyRead = 0x43
DwgRecoveredOK = 60
DwgSentinelDoesNotMatch = 0x42
DwgShareDemandLoad = 500
DwgShareReadAccess = 0x1f5
DwgShareWriteAccess = 0x1f6
DwkLockFileFound = 0x4d
DxbPartiallyRead = 0x40
DxbReadAborted = 70
DxfPartiallyRead = 0x3e
DxfReadAborted = 0x3f
EndOfFile = 0x29
EndOfObject = 40
EntityInInactiveLayout = 9
ExcessiveItemCount = 0xa6
ExplodeBeforeTransform = 0x87
ExternalDataSizeExceeded = 0x7d
FileAccessErr = 0x48
FileExists = 0x16a
FileInternalErr = 0x4a
FileLockedByAutoCAD = 0x47
FileMissingSections = 0x1b4
FileNotFound = 0x4c
FilerError = 0x35
FileSharingViolation = 0x1b1
FileSystemErr = 0x49
FileTooManyOpen = 0x4b
FiniteStateMachineError = 0xc1
FixedAllErrors = 120
GeneralModelingFailure = 150
GraphicsNotGenerated = 0x20b
GuidNoAddress = 0x18a
HadMultipleReaders = 0x5e
HandleExists = 10
HandleInUse = 14
HatchTooDense = 420
IgnoredLinetypeRedefinition = 0xa7
IllegalEntityType = 0x15
IllegalReplacement = 0x27
IncompatiblePlotSettings = 0x1fc
IncompleteBlockDefinition = 0x17b
IncompleteComplexObject = 380
InProcessOfCommitting = 0xfd
InsertAfter = 110
InternetBadPath = 0x4e23
InternetBase = 0x4e20
InternetCreateInternetSessionFailed = 0x4e33
InternetDirectoryFull = 0x4e27
InternetDiskFull = 0x4e2a
InternetFileAccessDenied = 0x4e25
InternetFileGenericError = 0x4e2b
InternetFileNotFound = 0x4e22
InternetFileOpenFailed = 0x4e37
InternetGenericException = 0x4e51
InternetHardwareError = 0x4e28
InternetHttpAccessDenied = 0x4e3b
InternetHttpBadGateway = 0x4e4c
InternetHttpBadMethod = 0x4e3f
InternetHttpBadRequest = 0x4e3a
InternetHttpConflict = 0x4e43
InternetHttpGatewayTimeout = 0x4e4e
InternetHttpLengthRequired = 0x4e45
InternetHttpNoAcceptableResponse = 0x4e40
InternetHttpNotSupported = 0x4e4b
InternetHttpObjectNotFound = 0x4e3e
InternetHttpOpenRequestFailed = 0x4e38
InternetHttpPaymentRequired = 0x4e3c
InternetHttpPreconditionFailure = 0x4e46
InternetHttpProxyAuthorizationRequired = 0x4e41
InternetHttpRequestForbidden = 0x4e3d
InternetHttpRequestTooLarge = 0x4e47
InternetHttpResourceGone = 0x4e44
InternetHttpServerError = 0x4e4a
InternetHttpServiceUnavailable = 0x4e4d
InternetHttpTimedOut = 0x4e42
InternetHttpUnsupportedMedia = 0x4e49
InternetHttpUriTooLong = 0x4e48
InternetHttpVersionNotSupported = 0x4e4f
InternetInCache = 0x4e21
InternetInternetError = 0x4e50
InternetInternetSessionConnectFailed = 0x4e34
InternetInternetSessionOpenFailed = 0x4e35
InternetInvalidAccessType = 0x4e36
InternetInvalidFileHandle = 0x4e26
InternetNoInternetSupport = 0x4e30
InternetNotAnUrl = 0x4e2d
InternetNotImplemented = 0x4e31
InternetNoWinInternet = 0x4e2e
InternetOK = 0x4e20
InternetOldWinInternet = 0x4e2f
InternetProtocolNotSupported = 0x4e32
InternetSharingViolation = 0x4e29
InternetTooManyOpenFiles = 0x4e24
InternetUnknownError = 0x4e52
InternetUserCancelledTransfer = 0x4e39
InternetValidUrl = 0x4e2c
InvalidAdsName = 0x1f
InvalidAxis = 0x9a
InvalidBlockName = 0x2f
InvalidContext = 0x14f
InvalidDimStyle = 0xac
InvalidDwgVersion = 0x25
InvalidDxf2dPoint = 0x177
InvalidDxf3dPoint = 0x178
InvalidDxfCode = 50
InvalidDxfSectionName = 0x173
InvalidEngineState = 0x205
InvalidExtents = 30
InvalidFaceVertexIndex = 0x37
InvalidFileExtension = 360
InvalidFix = 0xc0
InvalidIdMap = 220
InvalidIndex = 0x18
InvalidInput = 3
InvalidInterfaceId = 290
InvalidKey = 0x21
InvalidLayer = 0xad
InvalidMeshVertexIndex = 0x38
InvalidNormal = 0x123
InvalidObjectId = 600
InvalidOffset = 0x9d
InvalidOpenState = 8
InvalidOwnerObject = 0xdd
InvalidPlotArea = 0x201
InvalidPlotInfo = 520
InvalidProfileName = 0x169
InvalidResultBuffer = 0x33
InvalidStyle = 0x124
InvalidSymbolTableName = 0x20
InvalidSymTableFlag = 0xa1
InvalidTextStyle = 0xa3
InvalidView = 0x1ff
InvalidWindowArea = 0x200
InvalidXrefObjectId = 0x259
IsAnEntity = 0x8b
IsReading = 0x2a
IsWriteProtected = 0x5b
IsWriting = 0x2b
IsXRefObject = 0x5c
IteratorDone = 0x81
KeyNotFound = 0x16
LayerGroupCodeMissing = 0xc9
LayoutNotCurrent = 0x20a
LeftErrorsUnfixed = 0x7a
LispActive = 0x14c
LoadFailed = 0x1f7
LockChangeInProgress = 0x143
LockConflict = 0x141
LockViolation = 320
LongTransReferenceError = 0xff
MakeMeProxy = 0x12d
MakeMeProxyAndResurrect = 0x1b0
MaxLayouts = 0x198
MissingBlockName = 390
MissingDxfField = 0x30
MissingDxfSection = 370
MissingSymbolTable = 0x62
MissingSymbolTableRecord = 0x63
MustBe0to2 = 0x18b
MustBe0to3 = 0x18c
MustBe0to4 = 0x18d
MustBe0to5 = 0x18e
MustBe0to8 = 0x18f
MustBe1to15 = 0x191
MustBe1to6 = 0x195
MustBe1to8 = 400
MustBeNonNegative = 0x193
MustBeNonZero = 0x194
MustBePositive = 0x192
MustFirstAddBlockToDB = 0x3a
MustOpenThruOwner = 0x58
MustPlotToFile = 0x20d
NegativeValueNotAllowed = 0x1d
NlsFileNotAvailable = 0x12e
NoActiveTransactions = 250
NoBlockBegin = 0x17e
NoClassId = 0x199
NoCurrentConfig = 0x1f9
NoDatabase = 0x7c
NoDocument = 330
NoErrorHandler = 0x207
NoFileName = 0x16d
NoInputFiler = 0x44
NoInternalSpace = 0xab
NoLabelBlock = 0x25b
NoLayout = 0x1fb
NoMatchingMedia = 510
NonCoplanarGeometry = 0x98
NonePlotDevice = 0x1fd
NonPlanarEntity = 0x9e
NoPlotStyleTranslationTable = 0x196
NotAllowedForThisProxy = 0x12f
NotAnEntity = 0x5d
NotApplicable = 2
NotCurrentDatabase = 0x8a
NotDxfHeaderGroupCode = 0x174
NotFromThisDocument = 0x14b
NotHandled = 0x1af
NoThumbnailBitmap = 0x189
NotImplementedYet = 1
NotInBlock = 0x83
NotInDatabase = 0x89
NotInGroup = 0x105
NotInitializedYet = 0x176
NotInPaperspace = 0x8d
NotMultiPageCapable = 0x20e
NotNewlyCreated = 0xfe
NotOpenForRead = 0x2c
NotOpenForWrite = 0x2d
NotSupportedInDwgApi = 310
NotThatKindOfClass = 0x2e
NotTopTransaction = 0xfb
NoViewAssociation = 0x25a
NoWorkSet = 0x100
NullBlockName = 0x11
NullEntityPointer = 20
NullExtents = 0x138
NullHandle = 11
NullIterator = 130
NullObjectId = 0x10
NullObjectPointer = 15
NullPtr = 0x1fa
NumberOfCopiesNotSupported = 0x209
ObjectIsReferenced = 0x188
ObjectToBeDeleted = 0x24
ObsoleteFileFormat = 0x1b3
OK = 0
OnLockedLayer = 0x57
OpenFileCancelled = 430
OtherObjectsBusy = 0x39
OutOfDisk = 0x1b
OutOfMemory = 6
OutOfPagerMemory = 0xd3
OutOfRange = 0x97
OwnerNotInDatabase = 0x84
OwnerNotOpenForRead = 0x85
OwnerNotOpenForWrite = 0x86
OwnerNotSet = 0xde
PageCancelled = 0x203
PagerError = 210
PagerWriteError = 0xd4
PermanentlyErased = 0x51
PlotAlreadyStarted = 0x206
PlotCancelled = 0x204
PlotStyleInColorDependentMode = 0x197
PointNotOnEntity = 0x9b
PolyWidthLost = 0x137
ProfileDoesNotExist = 0x167
ProfileIsInUse = 0x16b
ProperClassSeparatorExpected = 0xce
RecordNotInTable = 0x80
RegisteredApplicationIdNotFound = 0x7e
RegistryAccessError = 0x16e
RegistryCreateError = 0x16f
RenameDoesNotExist = 0x15c
RenameInvalidLayoutName = 350
RenameInvalidName = 0x160
RenameIsModelSpace = 0x15d
RenameLayoutAlreadyExists = 0x15f
RepeatedDwgRead = 0x1b5
RepeatEntity = 0x7f
RowsMustMatchColumns = 0x1ba
SecErrorCipherNotSupported = 0x4b2
SecErrorComputingSignature = 0x44f
SecErrorDecryptingData = 0x4b3
SecErrorEncryptingData = 0x4b1
SecErrorGeneratingTimestamp = 0x44e
SecErrorReadingFile = 0x3ea
SecErrorWritingFile = 0x3eb
SecErrorWritingSignature = 0x450
SecInitializationFailure = 0x3e9
SecInvalidDigitalId = 0x44d
SelfReference = 0x61
SetFailed = 340
SingularPoint = 0x9c
SomeInputDataLeftUnread = 170
StringTooLong = 160
SubentitiesStillOpen = 0x59
SubSelectionSetEmpty = 550
TargetDocNotQuiescent = 0x14d
TooFewLineTypeElements = 0xa4
TooFewVertices = 0xe8
TooManyLineTypeElements = 0xa5
TooManyVertices = 0xe7
TransactionOpenWhileCommandEnded = 0xfc
UnableToGetLabelBlock = 0x25f
UnableToGetViewAssociation = 0x25d
UnableToRemoveAssociation = 0x260
UnableToSetLabelBlock = 0x25e
UnableToSetViewAssociation = 0x25c
UnableToSyncModelView = 0x261
UndefinedDxfGroupCode = 0x175
UndefinedLineType = 0xa2
UndefineShapeName = 0x184
UndoNoGroupBegin = 0x19b
UndoOperationNotAvailable = 410
UnknownDxfFileFormat = 0x171
UnknownHandle = 13
UnrecoverableErrors = 0x7b
UnsupportedFileFormat = 0x1b2
UserBreak = 180
VertexAfterFace = 0x36
Vetoed = 0x145
WasErased = 80
WasNotErased = 0x6b
WasNotForwarding = 0xd5
WasNotifying = 0x55
WasNotOpenForWrite = 100
WasOpenForNotify = 0x56
WasOpenForRead = 0x52
WasOpenForUndo = 0x54
WasOpenForWrite = 0x53
WrongCellType = 440
WrongDatabase = 0x23
WrongObjectType = 0x22
WrongSubentityType = 230
XRefDependent = 0x60

class Exception(System.Exception, ISerializable):
    """
    
    E
    
    x
    
    c
    
    e
    
    p
    
    t
    
    i
    
    o
    
    n
    
    (
    
    )
    
    (
    
    )
    """
    def GetObjectData(self):
        """
        GetObjectData -> void
            
            SerializationInfo info: 
            Input serialization info
            
            StreamingContext context: 
            Input context
        """
        pass
    
    
    ErrorStatus = None
    
    pass

class ExtensionApplicationAttribute(Attribute):
    """
    
    E
    
    x
    
    t
    
    e
    
    n
    
    s
    
    i
    
    o
    
    n
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    .
    
    T
    
    y
    
    p
    
    e
    
     
    
    e
    
    n
    
    t
    
    r
    
    y
    
    P
    
    o
    
    i
    
    n
    
    t
    
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
    
     
    
    a
    
     
    
    t
    
    y
    
    p
    
    e
    
     
    
    o
    
    f
    
     
    
    e
    
    n
    
    t
    
    r
    
    y
    
     
    
    p
    
    o
    
    i
    
    n
    
    t
    """
    Type = None
    
    pass

class ExtractOption(public class ExtractOption):
    """
    
    """
    ExtractType Field = None
    
    
    FillGap Field = None
    
    
    MiniumSegmentLength Field = None
    
    
    ProcessPoints Field = None
    
    
    SnapAngle Field = None
    
    
    UseLineSegmentOnly Field = None
    
    pass

  OutLine
  AllLine

class FileExistsConditionAttribute(Attribute, ICondition):
    """
    
    F
    
    i
    
    l
    
    e
    
    E
    
    x
    
    i
    
    s
    
    t
    
    s
    
    C
    
    o
    
    n
    
    d
    
    i
    
    t
    
    i
    
    o
    
    n
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
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
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
    .
    """
    def Evaluate(self):
        """
        Evaluate -> bool
        
        """
        pass
    
    pass

class IJavaScriptCallable(public interface IJavaScriptCallable):
    """
    
    """
    EntryPoint = None
    
    pass

class IMenuItem(public interface IMenuItem):
    """
    
    """
    def OnClicked(self):
        """
        OnClicked -> void
        
        """
        pass
    
    
    Checked = None
    
    
    Enabled = None
    
    
    Icon = None
    
    
    Items = None
    
    
    Text = None
    
    
    Visible = None
    
    pass

class IPointCloudExtractionProgressCallback(public interface IPointCloudExtractionProgressCallback):
    """
    
    """
    def Cancel(self):
        """
        Cancel -> void
        
        """
        pass
    
    
    def Cancelled(self):
        """
        Cancelled -> bool
        
        """
        pass
    
    
    def End(self):
        """
        End -> void
        
        """
        pass
    
    
    def UpdateCaption(self):
        """
        UpdateCaption -> void
            
            string caption: 
            The caption
        """
        pass
    
    
    def UpdateProgress(self):
        """
        UpdateProgress -> void
            
            int progress: 
            The progress, from 0~99.
        """
        pass
    
    
    def UpdateRemainTime(self):
        """
        UpdateRemainTime -> void
        
        """
        pass
    
    pass

class Interop(public sealed class Interop):
    """
    
    """
    def AttachUnmanagedObject(self):
        """
        AttachUnmanagedObject -> void
            
            DisposableWrapper obj: 
            Input Autodesk.AutoCAD.Runtime.DisposableWrapper object. The wrapper.
            
            IntPtr unmanagedPointer: 
            Input System.IntPtr object. The unmanaged resource.
            
            [MarshalAs(UnmanagedType.U1)] bool autoDelete: 
            Input System.Boolean object. Boolean indicating whether the given wrapper object owns the underlying unmanaged resource. When the wrapper owns the resource the Dispose method will delete the resource.
        """
        pass
    
    
    def Check(self):
        """
        Check -> void
            
            int returnValue: 
            Input System.Int32 object.
        """
        pass
    
    
    def CheckAds(self):
        """
        CheckAds -> void
            
            int returnValue: 
            Input System.Int32 object.
        """
        pass
    
    
    def CheckAdsForCancel(self):
        """
        CheckAdsForCancel -> bool
            
            int returnValue: 
            Input System.Int32 object.
        """
        pass
    
    
    def CheckBool(self):
        """
        CheckBool -> void
            
            [MarshalAs(UnmanagedType.U1)] bool returnValue: 
            Input System.Boolean object.
        """
        pass
    
    
    def CheckBoolean(self):
        """
        CheckBoolean -> void
            
            int returnValue: 
            Input System.Int32 object.
        """
        pass
    
    
    def CheckNull(self):
        """
        CheckNull -> void
        
        """
        pass
    
    
    def DetachUnmanagedObject(self):
        """
        DetachUnmanagedObject -> void
            
            DisposableWrapper obj: 
            Input Autodesk.AutoCAD.Runtime.DisposableWrapper object. The wrapper.
        """
        pass
    
    
    def SetAutoDelete(self):
        """
        SetAutoDelete -> void
            
            DisposableWrapper obj: 
            Input Autodesk.AutoCAD.Runtime.DisposableWrapper object. The wrapper.
            
            [MarshalAs(UnmanagedType.U1)] bool value: 
            Input System.Boolean object. Boolean that is true if the wrapper is to own the object; otherwise, false.
        """
        pass
    
    
    def ThrowExceptionForErrorStatus(self):
        """
        ThrowExceptionForErrorStatus -> void
            
            int errorStatus: 
            Input System.Int32 object.
        """
        pass
    
    pass

class JavaScriptCallbackAttribute(Attribute, IJavaScriptCallable):
    """
    
    J
    
    a
    
    v
    
    a
    
    S
    
    c
    
    r
    
    i
    
    p
    
    t
    
    C
    
    a
    
    l
    
    l
    
    b
    
    a
    
    c
    
    k
    
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
    """
    EntryPoint = None
    
    pass

class JavaScriptClassAttribute(Attribute):
    """
    
    J
    
    a
    
    v
    
    a
    
    S
    
    c
    
    r
    
    i
    
    p
    
    t
    
    C
    
    l
    
    a
    
    s
    
    s
    
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
    """
    Type = None
    
    pass

class LenientResourceManager(ResourceManager):
    """
    
    L
    
    e
    
    n
    
    i
    
    e
    
    n
    
    t
    
    R
    
    e
    
    s
    
    o
    
    u
    
    r
    
    c
    
    e
    
    M
    
    a
    
    n
    
    a
    
    g
    
    e
    
    r
    
    
    
    
     
    
     
    
     
    
     
    
    T
    
    y
    
    p
    
    e
    
     
    
    t
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
    .
    """

    pass

  Angle = 0x138c
  DottedPair = 0x139a
  Double = 0x1389
  Int16 = 0x138b
  Int32 = 0x1392
  ListBegin = 0x1398
  ListEnd = 0x1399
  Nil = 0x139b
  None = 0x1388
  ObjectId = 0x138e
  Orientation = 0x1390
  Point2d = 0x138a
  Point3d = 0x1391
  SelectionSet = 0x138f
  T_atom = 0x139d
  Text = 0x138d
  Void = 0x1396

class LispFunctionAttribute(Attribute, ICommandLineCallable):
    """
    
    L
    
    i
    
    s
    
    p
    
    F
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    L
    
    i
    
    s
    
    p
    
    F
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    L
    
    i
    
    s
    
    p
    
    F
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
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
    
     
    
    h
    
    e
    
    l
    
    p
    
    T
    
    o
    
    p
    
    i
    
    c
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    h
    
    e
    
    l
    
    p
    
     
    
    t
    
    o
    
    p
    
    i
    
    c
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    f
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    
    
    
    
    
    
    
    
    
    
    L
    
    i
    
    s
    
    p
    
    F
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
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
    
    )
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
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
    
     
    
    g
    
    l
    
    o
    
    b
    
    a
    
    l
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
    N
    
    a
    
    m
    
    e
    
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
    
     
    
    l
    
    o
    
    c
    
    a
    
    l
    
    i
    
    z
    
    e
    
    d
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    t
    
    h
    
    e
    
     
    
    L
    
    i
    
    s
    
    p
    
     
    
    f
    
    u
    
    n
    
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
    
     
    
    h
    
    e
    
    l
    
    p
    
    F
    
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
    
     
    
    s
    
    p
    
    e
    
    c
    
    i
    
    f
    
    i
    
    e
    
    s
    
     
    
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
    
     
    
    a
    
    n
    
    d
    
     
    
    f
    
    i
    
    l
    
    e
    
     
    
    n
    
    a
    
    m
    
    e
    
     
    
    o
    
    f
    
     
    
    y
    
    o
    
    u
    
    r
    
     
    
    H
    
    e
    
    l
    
    p
    
     
    
    f
    
    i
    
    l
    
    e
    
    .
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    h
    
    e
    
    l
    
    p
    
    T
    
    o
    
    p
    
    i
    
    c
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    h
    
    e
    
    l
    
    p
    
     
    
    t
    
    o
    
    p
    
    i
    
    c
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    f
    
    o
    
    r
    
     
    
    t
    
    h
    
    i
    
    s
    
     
    
    f
    
    u
    
    n
    
    c
    
    t
    
    i
    
    o
    
    n
    
    .
    """
    GlobalName = None
    
    
    HelpFileName = None
    
    
    HelpTopic = None
    
    
    LocalizedNameId = None
    
    pass

class Marshaler(public sealed class Marshaler):
    """
    
    """
    def AcValueToObject(self):
        """
        AcValueToObject -> object
            
            IntPtr acValueObj: 
            Input AcValue object
        """
        pass
    
    
    def BitmapInfoToBitmap(self):
        """
        BitmapInfoToBitmap -> Bitmap
            
            IntPtr bitmapInfo: 
            Input bitmap info object
        """
        pass
    
    
    def BitmapToBitmapInfo(self):
        """
        BitmapToBitmapInfo -> IntPtr
            
            Bitmap bitmap: 
            Input bitmap
        """
        pass
    
    
    def CopyToManagedFullSubentityPath(self):
        """
        CopyToManagedFullSubentityPath -> FullSubentityPath
            
            IntPtr path: 
            Input path to copy
        """
        pass
    
    
    def CopyToUnmanagedFullSubentityPath(self):
        """
        CopyToUnmanagedFullSubentityPath -> void
            
            FullSubentityPath path: 
            Input path to copy
            
            IntPtr newPath: 
            Input new path
        """
        pass
    
    
    def ObjectsToResbuf(self):
        """
        ObjectsToResbuf -> IntPtr
        
        """
        pass
    
    
    def ObjectToAcValue(self):
        """
        ObjectToAcValue -> void
            
            object obj: 
            Input.
        """
        pass
    
    
    def ObjectToResbuf(self):
        """
        ObjectToResbuf -> IntPtr
        
        """
        pass
    
    pass

class Overrule(RXObject):
    """
    
    """
    def AddOverrule(self):
        """
        AddOverrule -> void
        
        """
        pass
    
    
    def HasOverrule(self):
        """
        HasOverrule -> bool
        
        """
        pass
    
    
    def IsApplicable(self):
        """
        IsApplicable -> bool
        
        """
        pass
    
    
    def RemoveOverrule(self):
        """
        RemoveOverrule -> void
        
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
    
    
    Overruling = None
    
    pass

class PerDocumentClassAttribute(Attribute):
    """
    
    P
    
    e
    
    r
    
    D
    
    o
    
    c
    
    u
    
    m
    
    e
    
    n
    
    t
    
    C
    
    l
    
    a
    
    s
    
    s
    
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
    """
    Type = None
    
    pass

class PointCloudExtractResult(public class PointCloudExtractResult):
    """
    
    """
    Curves Field = None
    
    
    transform Field = None
    
    pass

class PointCloudExtractor(DisposableWrapper):
    """
    
    """
    def AppendLineProfile(self):
        """
        AppendLineProfile -> ObjectIdCollection
            
            PointCloudExtractResult profile: 
            The output of extraction.
            
            ObjectId spaceId: 
            The space to be added in of lines.
            
            string layer: 
            Layer of lines.
            
            Autodesk.AutoCAD.Colors.Color color: 
            Color of lines.
        """
        pass
    
    
    def AppendPolylineProfile(self):
        """
        AppendPolylineProfile -> ObjectIdCollection
            
            PointCloudExtractResult profile: 
            The output of extraction.
            
            ObjectId spaceId: 
            The space to be added in the lines.
            
            string layer: 
            Layer of lines.
            
            Autodesk.AutoCAD.Colors.Color color: 
            Color of lines.
            
            double polylineWidth: 
            Polyline width.
        """
        pass
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def Extract(self):
        """
        Extract -> PointCloudExtractResult
            
            PointCloudEx pointCloud: 
            The point cloud to be extracted.
            
            Vector3d planZDirection: 
            The plan's normal direction.
            
            Vector3d planXDirection: 
            The plan's X direction.
            
            Point3d pointOnPlan: 
            A point on plan.
            
            Autodesk.AutoCAD.Runtime.ExtractOption extractOption: 
            The extract option.
            
            IPointCloudExtractionProgressCallback progress: 
            The callback of extraction, which can manulate the extract to cancel, update, etc.
        """
        pass
    
    pass

class ProfileCurve2d(DisposableWrapper):
    """
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    C
    
    u
    
    r
    
    v
    
    e
    
    2
    
    d
    
    (
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    C
    
    u
    
    r
    
    v
    
    e
    
    2
    
    d
    
    (
    
    C
    
    i
    
    r
    
    c
    
    u
    
    l
    
    a
    
    r
    
    A
    
    r
    
    c
    
    2
    
    d
    
    )
    
    (
    
    )
    
    
    
    
    
    
    
    
    
    
    P
    
    r
    
    o
    
    f
    
    i
    
    l
    
    e
    
    C
    
    u
    
    r
    
    v
    
    e
    
    2
    
    d
    
    (
    
    L
    
    i
    
    n
    
    e
    
    S
    
    e
    
    g
    
    m
    
    e
    
    n
    
    t
    
    2
    
    d
    
    )
    
    (
    
    )
    """
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    Arc = None
    
    
    IsArc = None
    
    
    IsSegment = None
    
    
    LineSeg = None
    
    pass

  LineSeg
  Arc

class ProgressMeter(DisposableWrapper):
    """
    
    """
    def MeterProgress(self):
        """
        MeterProgress -> void
        
        """
        pass
    
    
    def SetLimit(self):
        """
        SetLimit -> void
            
            int max: 
            Input maximum number of meter updates.
        """
        pass
    
    
    def Start(self):
        """
        Start() -> void
        
        Start(string) -> void
            
            string displayString: 
            Input optional string to display with the meter.
        """
        pass
    
    
    def Stop(self):
        """
        Stop -> void
        
        """
        pass
    
    pass

class RXClass(RXObject):
    """
    
    """
    def AddX(self):
        """
        AddX -> IntPtr
            
            RXClass runtimeClass: 
            Input object for the protocol extension class.
            
            RXObject protocolExtension: 
            Input protocol extension object.
        """
        pass
    
    
    def Create(self):
        """
        Create -> RXObject
        
        """
        pass
    
    
    def DelX(self):
        """
        DelX -> IntPtr
            
            RXClass runtimeClass: 
            Input object for the protocol extension class.
        """
        pass
    
    
    def GetRuntimeType(self):
        """
        GetRuntimeType -> System.Type
        
        """
        pass
    
    
    def GetX(self):
        """
        GetX -> IntPtr
            
            RXClass runtimeClass: 
            Input object for the protocol extension class.
        """
        pass
    
    
    def IsDerivedFrom(self):
        """
        IsDerivedFrom -> bool
            
            RXClass runtimeClass: 
            Input object for the desired base class.
        """
        pass
    
    
    def QueryX(self):
        """
        QueryX -> IntPtr
            
            RXClass runtimeClass: 
            Input Autodesk.AutoCAD.Runtime.RXClass object for the protocol extension class.
        """
        pass
    
    
    AppName = None
    
    
    ClassVersion = None
    
    
    DxfName = None
    
    
    MyParent = None
    
    
    Name = None
    
    
    ProxyFlags = None
    
    pass

class RXObject(DisposableWrapper, ICloneable):
    """
    
    """
    def Clone(self):
        """
        Clone -> object
        
        """
        pass
    
    
    def CompareTo(self):
        """
        CompareTo -> Integer
            
            object obj: 
            Input object to compare with.
        """
        pass
    
    
    def CopyFrom(self):
        """
        CopyFrom -> void
            
            RXObject source: 
            Input object to copy from.
        """
        pass
    
    
    def GetClass(self):
        """
        GetClass -> RXClass
            
            System.Type type: 
            Input type to get
        """
        pass
    
    
    def GetRXClass(self):
        """
        GetRXClass -> RXClass
        
        """
        pass
    
    
    def QueryX(self):
        """
        QueryX -> IntPtr
            
            RXClass protocolClass: 
            Input protocol to query with
        """
        pass
    
    
    def X(self):
        """
        X -> IntPtr
            
            RXClass protocolClass: 
            Input protocol class
        """
        pass
    
    pass

class Registry(public sealed class Registry):
    """
    
    """
    ClassesRoot = None
    
    
    CurrentConfig = None
    
    
    CurrentUser = None
    
    
    LocalMachine = None
    
    pass

class RegistryKey(IDisposable):
    """
    
    R
    
    e
    
    g
    
    i
    
    s
    
    t
    
    r
    
    y
    
    K
    
    e
    
    y
    
    (
    
    )
    """
    def Close(self):
        """
        Close -> void
        
        """
        pass
    
    
    def CreateSubKey(self):
        """
        CreateSubKey(string) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        CreateSubKey(string, RegistryKeyPermissionCheck) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        CreateSubKey(string, RegistryKeyPermissionCheck, RegistryOptions) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        CreateSubKey(string, RegistryKeyPermissionCheck, RegistryOptions, RegistrySecurity) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        CreateSubKey(string, RegistryKeyPermissionCheck, RegistrySecurity) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        """
        pass
    
    
    def DeleteSubKey(self):
        """
        DeleteSubKey -> void
        
        """
        pass
    
    
    def DeleteSubKeyTree(self):
        """
        DeleteSubKeyTree -> void
        
        """
        pass
    
    
    def DeleteValue(self):
        """
        DeleteValue -> void
        
        """
        pass
    
    
    def Dispose(self):
        """
        Dispose() -> void
        
        Dispose([MarshalAs(UnmanagedType.U1)] bool) -> void
        
        """
        pass
    
    
    def GetBaseKey(self):
        """
        GetBaseKey(RegistryHive) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        GetBaseKey(RegistryHive, RegistryView) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        """
        pass
    
    
    def GetSubKeyNames(self):
        """
        GetSubKeyNames -> string()
        
        """
        pass
    
    
    def GetValue(self):
        """
        GetValue(string) -> object
        
        GetValue(string, object) -> object
        
        GetValue(string, object, RegistryValueOptions) -> object
        
        """
        pass
    
    
    def GetValueKind(self):
        """
        GetValueKind -> RegistryValueKind
        
        """
        pass
    
    
    def GetValueNames(self):
        """
        GetValueNames -> string()
        
        """
        pass
    
    
    def OpenBaseKey(self):
        """
        OpenBaseKey -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        """
        pass
    
    
    def OpenSubKey(self):
        """
        OpenSubKey(string) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        OpenSubKey(string, RegistryKeyPermissionCheck) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        OpenSubKey(string, RegistryKeyPermissionCheck, RegistryRights) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        OpenSubKey(string, [MarshalAs(UnmanagedType.U1)] bool) -> Autodesk.AutoCAD.Runtime.RegistryKey
        
        """
        pass
    
    
    def SetValue(self):
        """
        SetValue(string, object) -> void
        
        SetValue(string, object, RegistryValueKind) -> void
        
        """
        pass
    
    
    SubKeyCount = None
    
    
    ValueCount = None
    
    pass

class RuntimeSystem(public sealed class RuntimeSystem):
    """
    
    """
    def Initialize(self):
        """
        Initialize -> void
            
            HostApplicationServices hostServices: 
            Input Autodesk.AutoCAD.DatabaseServices.HostApplicationServices object.
            
            int localId: 
            Input.
        """
        pass
    
    
    def Main(self):
        """
        Main -> Integer
            
            string pwzArgument: 
            Input System.String; argument is not used, it’s there to satisfy ExecuteInDefaultAppDomain which calls the method and loads the acdbmgd assembly.
        """
        pass
    
    
    def Terminate(self):
        """
        Terminate -> void
        
        """
        pass
    
    pass

class SecuredApplicationAttribute(Attribute):
    """
    
    S
    
    e
    
    c
    
    u
    
    r
    
    e
    
    d
    
    A
    
    p
    
    p
    
    l
    
    i
    
    c
    
    a
    
    t
    
    i
    
    o
    
    n
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    l
    
    i
    
    c
    
    e
    
    n
    
    s
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    l
    
    i
    
    c
    
    e
    
    n
    
    s
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    o
    
    u
    
    r
    
    S
    
    i
    
    g
    
    n
    
    a
    
    t
    
    u
    
    r
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    s
    
    i
    
    g
    
    n
    
    a
    
    t
    
    u
    
    r
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    l
    
    i
    
    e
    
    n
    
    t
    
    S
    
    i
    
    g
    
    n
    
    a
    
    t
    
    u
    
    r
    
    e
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
     
    
    c
    
    l
    
    i
    
    e
    
    n
    
    t
    
     
    
    s
    
    i
    
    g
    
    n
    
    a
    
    t
    
    u
    
    r
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    c
    
    l
    
    i
    
    e
    
    n
    
    t
    
    P
    
    u
    
    b
    
    l
    
    i
    
    c
    
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
    
     
    
    c
    
    l
    
    i
    
    e
    
    n
    
    t
    
    '
    
    s
    
     
    
    p
    
    u
    
    b
    
    l
    
    i
    
    c
    
     
    
    k
    
    e
    
    y
    """
    ClientPublicKey = None
    
    
    ClientSignature = None
    
    
    License = None
    
    
    OurSignature = None
    
    pass

class SynchronizationContext(System.Threading.SynchronizationContext):
    """
    
    """
    def CreateCopy(self):
        """
        CreateCopy -> System.Threading.SynchronizationContext
        
        """
        pass
    
    
    def OperationCompleted(self):
        """
        OperationCompleted -> void
        
        """
        pass
    
    
    def OperationStarted(self):
        """
        OperationStarted -> void
        
        """
        pass
    
    
    def Post(self):
        """
        Post -> void
        
        """
        pass
    
    
    def Send(self):
        """
        Send -> void
        
        """
        pass
    
    
    def Wait(self):
        """
        Wait -> Integer
        
        """
        pass
    
    pass

class SystemObjects(public sealed class SystemObjects):
    """
    
    """
    ClassDictionary = None
    
    
    DynamicLinker = None
    
    
    ServiceDictionary = None
    
    pass

class SystemVariableEnumerator(DisposableWrapper, IEnumerator):
    """
    
    S
    
    y
    
    s
    
    t
    
    e
    
    m
    
    V
    
    a
    
    r
    
    i
    
    a
    
    b
    
    l
    
    e
    
    E
    
    n
    
    u
    
    m
    
    e
    
    r
    
    a
    
    t
    
    o
    
    r
    
    (
    
    )
    """
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
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

class Variable(DisposableWrapper):
    """
    
    V
    
    a
    
    r
    
    i
    
    a
    
    b
    
    l
    
    e
    
    (
    
    )
    """
    class RangeInfo(DisposableWrapper):
        """
        
        R
        
        a
        
        n
        
        g
        
        e
        
        I
        
        n
        
        f
        
        o
        
        (
        
        )
        
        (
        
        )
        
        
        
        
        
        
        
        
        
        
        R
        
        a
        
        n
        
        g
        
        e
        
        I
        
        n
        
        f
        
        o
        
        (
        
        i
        
        n
        
        t
        
        ,
        
         
        
        i
        
        n
        
        t
        
        )
        
        (
        
        )
        """
        def DeleteUnmanagedObject(self):
            """
            DeleteUnmanagedObject -> void
            
            """
            pass
        
        
        LowerBound = None
        
        
        UpperBound = None
        
        pass
    
    
      Angle = 5
      Area = 3
      Boolean = 1
      Distance = 4
      Last = 6
      None = 0
      SymbolName = 2
      UnitlessReal = 6
    
    
      PerSession
      PerUser
      PerProfile
      PerDatabase
      PerViewport
    
    
      Chatty = 8
      DotMeansEmpty = 2
      None = 0
      NoUndo = 4
      SpacesAllowed = 1
    
    
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
        
        """
        pass
    
    
    IsLocked = None
    
    
    IsReadOnly = None
    
    
    Name = None
    
    
    PrimaryType = None
    
    
    Range = None
    
    
    SecondaryType = None
    
    
    Storage = None
    
    
    TypeFlags = None
    
    
    Value = None
    
    pass

class VariableChangedEventArgs(EventArgs, IDisposable):
    """
    
    """
    NewValue = None
    
    
    OldValue = None
    
    pass

def VariableChangedEventHandler(self):
    """
    VariableChangedEventHandler -> void
        
        sender: 
        Object that fired the event
        
        e: 
        VariableChangedEventArgs
    """
    pass

class VariableChangingEventArgs(EventArgs, IDisposable):
    """
    
    """
    def Veto(self):
        """
        Veto -> void
            
            string reason: 
            Optional. If more information is available about the failure then it should be be passed via this parameter 
        """
        pass
    
    
    IsResetting = None
    
    
    NewValue = None
    
    
    OldValue = None
    
    pass

def VariableChangingEventHandler(self):
    """
    VariableChangingEventHandler -> void
        
        sender: 
        Object that fired the event
        
        e: 
        VariableChangingEventArgs
    """
    pass

class Variables(DisposableWrapper, IEnumerable<Variable>):
    """
    
    """
    def DeleteUnmanagedObject(self):
        """
        DeleteUnmanagedObject -> void
        
        """
        pass
    
    
    def GetAllNames(self):
        """
        GetAllNames -> string()
        
        """
        pass
    
    
    def GetEnumerator(self):
        """
        GetEnumerator -> IEnumerator<Variable>
        
        """
        pass
    
    
    def Reset(self):
        """
        Reset -> void
            
            Variable.StorageType filter: 
            Strorage type of variable to reset.
        """
        pass
    
    pass

class WrapperAttribute(Attribute):
    """
    
    W
    
    r
    
    a
    
    p
    
    p
    
    e
    
    r
    
    A
    
    t
    
    t
    
    r
    
    i
    
    b
    
    u
    
    t
    
    e
    
    
    
    
     
    
     
    
     
    
     
    
    s
    
    t
    
    r
    
    i
    
    n
    
    g
    
     
    
    w
    
    r
    
    a
    
    p
    
    p
    
    e
    
    d
    
    C
    
    l
    
    a
    
    s
    
    s
    
     
    
    :
    
     
    
    I
    
    n
    
    p
    
    u
    
    t
    
    .
    """
    WrappedClass = None
    
    pass