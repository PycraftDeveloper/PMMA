from math import pi as _math__pi
from os import sep as _os__sep
from os import cpu_count as _os__cpu_count

class Constants:
    """
    🟩 **R** -
    """
    TKINTER_STYLE_BUTTON = "TButton"
    TKINTER_STYLE_CHECKBUTTON = "TCheckbutton"
    TKINTER_STYLE_COMBOBOX = "TCombobox"
    TKINTER_STYLE_ENTRY = "TEntry"
    TKINTER_STYLE_FRAME = "TFrame"
    TKINTER_STYLE_LABEL = "TLabel"
    TKINTER_STYLE_LABELFRAME = "TLabelFrame"
    TKINTER_STYLE_MENUBUTTON = "TMenubutton"
    TKINTER_STYLE_NOTEBOOK = "TNotebook"
    TKINTER_STYLE_PANEDWINDOW = "TPanedwindow"
    TKINTER_STYLE_HORIZONTAL_PROGRESSBAR = "Horizontal.TProgressbar"
    TKINTER_STYLE_VERTICAL_PROGRESSBAR = "Vertical.TProgressbar"
    TKINTER_STYLE_RADIOBUTTON = "TRadiobutton"
    TKINTER_STYLE_HORIZONTAL_SCALE = "Horizontal.TScale"
    TKINTER_STYLE_VERTICAL_SCALE = "Vertical.TScale"
    TKINTER_STYLE_HORIZONTAL_SCROLLBAR = "Horizontal.TScrollbar"
    TKINTER_STYLE_VERTICAL_SCROLLBAR = "Vertical.TScrollbar"
    TKINTER_STYLE_SEPARATOR = "TSeparator"
    TKINTER_STYLE_SIZEGRIP = "TSizegrip"
    TKINTER_STYLE_TREEVIEW = "Treeview"

    LINEAR_TRANSITION = "linear transition" # constant velocity (kwargs: None)
    SMOOTH_TRANSITION = "smooth transition" # accelerates, moves constant, decelerates (kwargs: Max Velocity)
    TRANSITION_MOVEMENT_TYPES = [
        LINEAR_TRANSITION,
        SMOOTH_TRANSITION
    ]

    SINGLE_PERCENTAGES = []
    for i in range(1, 101):
        SINGLE_PERCENTAGES.append(i / 100)

    VALUE_TRANSITION = "value transition"
    COORDINATE_TRANSITION = "coordinate transition"
    TRANSITION_TYPES = [
        VALUE_TRANSITION,
        COORDINATE_TRANSITION
    ]

    DISPLAY_FRAME_BUFFER = "display frame buffer"
    TWO_DIMENSION_FRAME_BUFFER = "2d frame buffer"
    THREE_DIMENSION_FRAME_BUFFER = "3d frame buffer"

    BOTH = "both"
    VERTEX_ONLY = "vertex"
    FRAGMENT_ONLY = "fragment"

    DATA_INTERPRETATIONS = [
        "1f",
        "2f",
        "3f",
        "4f",
        "1i",
        "2i",
        "3i",
        "4i",
        "1u",
        "2u",
        "3u",
        "4u",
        "1d",
        "2d",
        "3d",
        "4d"
    ]

    DEGREES = "degrees"
    RADIANS = "radians"
    GRADIANS = "gradians"

    DECIMAL = "decimal"
    PERCENTAGE = "percentage"

    CONVENTIONAL_COORDINATES = "conventional coordinates"
    OPENGL_COORDINATES = "opengl coordinates"

    VALUE = "value"
    UPDATING = "updating"
    MANUALLY_SET = "manually set"
    DATA_COLLECTION_METHODS = "data collection methods"

    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
    SECONDS_PER_DAY = SECONDS_PER_HOUR * 24
    DAYS_PER_YEAR = 365.25  # accounting for leap years
    DAYS_PER_MONTH = DAYS_PER_YEAR / 12
    HOURS_PER_DAY = 24
    MINUTES_PER_HOUR = 60
    MICROSECONDS_PER_SECOND = 1e6

    WINDOWS = "windows"
    LINUX = "linux"
    MACOS = "macOS"
    JAVA = "java"
    ANDROID = "android"

    LIGHT = "light"
    DARK = "dark"

    AUTOMATIC = "automatic"

    LARGE_APPLICATION = "large"
    MEDIUM_APPLICATION = "medium"
    SMALL_APPLICATION = "small"
    MICRO_APPLICATION = "micro"

    DEVELOPMENT = "development"
    INFORMATION = "information"
    WARNING = "warning"
    ERROR = "error"

    CLASS = "class"
    CLASS_INSTANCE = "class instance"
    FUNCTION = "function"
    UNKNOWN = "unknown"

    CHARACTERS = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    CENTER = "center"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"

    CORE_COUNT = _os__cpu_count()
    THREAD_COUNT = CORE_COUNT * 2

    CARTESIAN = "cartesian"
    POLAR = "polar"

    COMPILED_PERLIN_NOISE = "compiled Perlin noise"

    PYTHON1 = "Python"
    PYTHON2 = "Python2"
    PYTHON3 = "Python3"

    MAJOR_PYTHON_VERSIONS = [
        PYTHON1,
        PYTHON2,
        PYTHON3]

    PYTHON1_4 = "Python1.4"
    PYTHON1_5 = "Python1.5"
    PYTHON1_6 = "Python1.6"

    PYTHON2_0 = "Python2.0"
    PYTHON2_1 = "Python2.1"
    PYTHON2_2 = "Python2.2"
    PYTHON2_3 = "Python2.3"
    PYTHON2_4 = "Python2.4"
    PYTHON2_5 = "Python2.5"
    PYTHON2_6 = "Python2.6"
    PYTHON2_7 = "Python2.7"

    PYTHON3_0 = "Python3.0"
    PYTHON3_1 = "Python3.1"
    PYTHON3_2 = "Python3.2"
    PYTHON3_3 = "Python3.3"
    PYTHON3_4 = "Python3.4"
    PYTHON3_5 = "Python3.5"
    PYTHON3_6 = "Python3.6"
    PYTHON3_7 = "Python3.7"
    PYTHON3_8 = "Python3.8"
    PYTHON3_9 = "Python3.9"
    PYTHON3_10 = "Python3.10"
    PYTHON3_11 = "Python3.11"
    PYTHON3_12 = "Python3.12"

    MAJOR_MINOR_PYTHON_VERSIONS = [
        PYTHON1_4,
        PYTHON1_5,
        PYTHON1_6,
        PYTHON2_0,
        PYTHON2_1,
        PYTHON2_2,
        PYTHON2_3,
        PYTHON2_4,
        PYTHON2_5,
        PYTHON2_6,
        PYTHON2_7,
        PYTHON3_0,
        PYTHON3_1,
        PYTHON3_2,
        PYTHON3_3,
        PYTHON3_4,
        PYTHON3_5,
        PYTHON3_6,
        PYTHON3_7,
        PYTHON3_8,
        PYTHON3_9,
        PYTHON3_10,
        PYTHON3_11,
        PYTHON3_12
    ]

    PATH_SEPARATOR = _os__sep

    DEFAULT = "default"
    TAU = _math__pi * 2

    XYZ = "xyz"
    XZY = "xzy"
    YXZ = "yxz"
    ZXY = "zxy"
    YZX = "yzx"
    ZYX = "zyx"

    SPATIAL_COORDINATES = [
        XYZ,
        XZY,
        YXZ,
        ZXY,
        YZX,
        ZYX]

    XY = "xy"
    YX = "yx"

    PLANAR_COORDINATES = [
        XY,
        YX]

    ALPHA = "alpha"

    MAROON = (128,0,0)
    DARK_RED = (139,0,0)
    BROWN = (165,42,42)
    FIREBRICK = (178,34,34)
    CRIMSON = (220,20,60)
    RED = (255,0,0)
    TOMATO = (255,99,71)
    CORAL = (255,127,80)
    INDIAN_RED = (205,92,92)
    LIGHT_CORAL = (240,128,128)
    DARK_SALMON = (233,150,122)
    SALMON = (250,128,114)
    LIGHT_SALMON = (255,160,122)
    ORANGE_RED = (255,69,0)
    DARK_ORANGE = (255,140,0)
    ORANGE = (255,165,0)
    GOLD = (255,215,0)
    DARK_GOLDEN_ROD = (184,134,11)
    GOLDEN_ROD = (218,165,32)
    PALE_GOLDEN_ROD = (238,232,170)
    DARK_KHAKI = (189,183,107)
    KHAKI = (240,230,140)
    OLIVE = (128,128,0)
    YELLOW = (255,255,0)
    YELLOW_GREEN = (154,205,50)
    DARK_OLIVE_GREEN = (85,107,47)
    OLIVE_DRAB = (107,142,35)
    LAWN_GREEN = (124,252,0)
    CHARTREUSE = (127,255,0)
    GREEN_YELLOW = (173,255,47)
    DARK_GREEN = (0,100,0)
    GREEN = (0,128,0)
    FOREST_GREEN = (34,139,34)
    LIME = (0,255,0)
    LIME_GREEN = (50,205,50)
    LIGHT_GREEN = (144,238,144)
    PALE_GREEN = (152,251,152)
    DARK_SEA_GREEN = (143,188,143)
    MEDIUM_SPRING_GREEN = (0,250,154)
    SPRING_GREEN = (0,255,127)
    SEA_GREEN = (46,139,87)
    MEDIUM_AQUA_MARINE = (102,205,170)
    MEDIUM_SEA_GREEN = (60,179,113)
    LIGHT_SEA_GREEN = (32,178,170)
    DARK_SLATE_GRAY = (47,79,79)
    TEAL = (0,128,128)
    DARK_CYAN = (0,139,139)
    AQUA = (0,255,255)
    CYAN = (0,255,255)
    LIGHT_CYAN = (224,255,255)
    DARK_TURQUOISE = (0,206,209)
    TURQUOISE = (64,224,208)
    MEDIUM_TURQUOISE = (72,209,204)
    PALE_TURQUOISE = (175,238,238)
    AQUA_MARINE = (127,255,212)
    POWDER_BLUE = (176,224,230)
    CADET_BLUE = (95,158,160)
    STEEL_BLUE = (70,130,180)
    CORN_FLOWER_BLUE = (100,149,237)
    DEEP_SKY_BLUE = (0,191,255)
    DODGER_BLUE = (30,144,255)
    LIGHT_BLUE = (173,216,230)
    SKY_BLUE = (135,206,235)
    LIGHT_SKY_BLUE = (135,206,250)
    MIDNIGHT_BLUE = (25,25,112)
    NAVY = (0,0,128)
    DARK_BLUE = (0,0,139)
    MEDIUM_BLUE = (0,0,205)
    BLUE = (0,0,255)
    ROYAL_BLUE = (65,105,225)
    BLUE_VIOLET = (138,43,226)
    INDIGO = (75,0,130)
    DARK_SLATE_BLUE = (72,61,139)
    SLATE_BLUE = (106,90,205)
    MEDIUM_SLATE_BLUE = (123,104,238)
    MEDIUM_PURPLE = (147,112,219)
    DARK_MAGENTA = (139,0,139)
    DARK_VIOLET = (148,0,211)
    DARK_ORCHID = (153,50,204)
    MEDIUM_ORCHID = (186,85,211)
    PURPLE = (128,0,128)
    THISTLE = (216,191,216)
    PLUM = (221,160,221)
    VIOLET = (238,130,238)
    MAGENTA = (255,0,255)
    FUCHSIA = (255,0,255)
    ORCHID = (218,112,214)
    MEDIUM_VIOLET_RED = (199,21,133)
    PALE_VIOLET_RED = (219,112,147)
    DEEP_PINK = (255,20,147)
    HOT_PINK = (255,105,180)
    LIGHT_PINK = (255,182,193)
    PINK = (255,192,203)
    ANTIQUE_WHITE = (250,235,215)
    BEIGE = (245,245,220)
    BISQUE = (255,228,196)
    BLANCHED_ALMOND = (255,235,205)
    WHEAT = (245,222,179)
    CORN_SILK = (255,248,220)
    LEMON_CHIFFON = (255,250,205)
    LIGHT_GOLDEN_ROD_YELLOW = (250,250,210)
    LIGHT_YELLOW = (255,255,224)
    SADDLE_BROWN = (139,69,19)
    SIENNA = (160,82,45)
    CHOCOLATE = (210,105,30)
    PERU = (205,133,63)
    SANDY_BROWN = (244,164,96)
    BURLY_WOOD = (222,184,135)
    TAN = (210,180,140)
    ROSY_BROWN = (188,143,143)
    MOCCASIN = (255,228,181)
    NAVAJO_WHITE = (255,222,173)
    PEACH_PUFF = (255,218,185)
    MISTY_ROSE = (255,228,225)
    LAVENDER_BLUSH = (255,240,245)
    LINEN = (250,240,230)
    OLD_LACE = (253,245,230)
    PAPAYA_WHIP = (255,239,213)
    SEA_SHELL = (255,245,238)
    MINT_CREAM = (245,255,250)
    SLATE_GRAY = (112,128,144)
    LIGHT_SLATE_GRAY = (119,136,153)
    LIGHT_STEEL_BLUE = (176,196,222)
    LAVENDER = (230,230,250)
    FLORAL_WHITE = (255,250,240)
    ALICE_BLUE = (240,248,255)
    GHOST_WHITE = (248,248,255)
    HONEYDEW = (240,255,240)
    IVORY = (255,255,240)
    AZURE = (240,255,255)
    SNOW = (255,250,250)
    BLACK = (0,0,0)
    DIM_GREY = (105,105,105)
    GRAY = (128,128,128)
    DARK_GREY = (169,169,169)
    SILVER = (192,192,192)
    LIGHT_GREY = (211,211,211)
    GAINSBORO = (220,220,220)
    WHITE_SMOKE = (245,245,245)
    WHITE = (255,255,255)

    TEXT_BASED_COLORS = {
        "MAROON": [128,0,0],
        "DARK_RED": [139,0,0],
        "BROWN": [165,42,42],
        "FIREBRICK": [178,34,34],
        "CRIMSON": [220,20,60],
        "RED": [255,0,0],
        "TOMATO": [255,99,71],
        "CORAL": [255,127,80],
        "INDIAN_RED": [205,92,92],
        "LIGHT_CORAL": [240,128,128],
        "DARK_SALMON": [233,150,122],
        "SALMON": [250,128,114],
        "LIGHT_SALMON": [255,160,122],
        "ORANGE_RED": [255,69,0],
        "DARK_ORANGE": [255,140,0],
        "ORANGE": [255,165,0],
        "GOLD": [255,215,0],
        "DARK_GOLDEN_ROD": [184,134,11],
        "GOLDEN_ROD": [218,165,32],
        "PALE_GOLDEN_ROD": [238,232,170],
        "DARK_KHAKI": [189,183,107],
        "KHAKI": [240,230,140],
        "OLIVE": [128,128,0],
        "YELLOW": [255,255,0],
        "YELLOW_GREEN": [154,205,50],
        "DARK_OLIVE_GREEN": [85,107,47],
        "OLIVE_DRAB": [107,142,35],
        "LAWN_GREEN": [124,252,0],
        "CHARTREUSE": [127,255,0],
        "GREEN_YELLOW": [173,255,47],
        "DARK_GREEN": [0,100,0],
        "GREEN": [0,128,0],
        "FOREST_GREEN": [34,139,34],
        "LIME": [0,255,0],
        "LIME_GREEN": [50,205,50],
        "LIGHT_GREEN": [144,238,144],
        "PALE_GREEN": [152,251,152],
        "DARK_SEA_GREEN": [143,188,143],
        "MEDIUM_SPRING_GREEN": [0,250,154],
        "SPRING_GREEN": [0,255,127],
        "SEA_GREEN": [46,139,87],
        "MEDIUM_AQUA_MARINE": [102,205,170],
        "MEDIUM_SEA_GREEN": [60,179,113],
        "LIGHT_SEA_GREEN": [32,178,170],
        "DARK_SLATE_GRAY": [47,79,79],
        "TEAL": [0,128,128],
        "DARK_CYAN": [0,139,139],
        "AQUA": [0,255,255],
        "CYAN": [0,255,255],
        "LIGHT_CYAN": [224,255,255],
        "DARK_TURQUOISE": [0,206,209],
        "TURQUOISE": [64,224,208],
        "MEDIUM_TURQUOISE": [72,209,204],
        "PALE_TURQUOISE": [175,238,238],
        "AQUA_MARINE": [127,255,212],
        "POWDER_BLUE": [176,224,230],
        "CADET_BLUE": [95,158,160],
        "STEEL_BLUE": [70,130,180],
        "CORN_FLOWER_BLUE": [100,149,237],
        "DEEP_SKY_BLUE": [0,191,255],
        "DODGER_BLUE": [30,144,255],
        "LIGHT_BLUE": [173,216,230],
        "SKY_BLUE": [135,206,235],
        "LIGHT_SKY_BLUE": [135,206,250],
        "MIDNIGHT_BLUE": [25,25,112],
        "NAVY": [0,0,128],
        "DARK_BLUE": [0,0,139],
        "MEDIUM_BLUE": [0,0,205],
        "BLUE": [0,0,255],
        "ROYAL_BLUE": [65,105,225],
        "BLUE_VIOLET": [138,43,226],
        "INDIGO": [75,0,130],
        "DARK_SLATE_BLUE": [72,61,139],
        "SLATE_BLUE": [106,90,205],
        "MEDIUM_SLATE_BLUE": [123,104,238],
        "MEDIUM_PURPLE": [147,112,219],
        "DARK_MAGENTA": [139,0,139],
        "DARK_VIOLET": [148,0,211],
        "DARK_ORCHID": [153,50,204],
        "MEDIUM_ORCHID": [186,85,211],
        "PURPLE": [128,0,128],
        "THISTLE": [216,191,216],
        "PLUM": [221,160,221],
        "VIOLET": [238,130,238],
        "MAGENTA": [255,0,255],
        "FUCHSIA": [255,0,255],
        "ORCHID": [218,112,214],
        "MEDIUM_VIOLET_RED": [199,21,133],
        "PALE_VIOLET_RED": [219,112,147],
        "DEEP_PINK": [255,20,147],
        "HOT_PINK": [255,105,180],
        "LIGHT_PINK": [255,182,193],
        "PINK": [255,192,203],
        "ANTIQUE_WHITE": [250,235,215],
        "BEIGE": [245,245,220],
        "BISQUE": [255,228,196],
        "BLANCHED_ALMOND": [255,235,205],
        "WHEAT": [245,222,179],
        "CORN_SILK": [255,248,220],
        "LEMON_CHIFFON": [255,250,205],
        "LIGHT_GOLDEN_ROD_YELLOW": [250,250,210],
        "LIGHT_YELLOW": [255,255,224],
        "SADDLE_BROWN": [139,69,19],
        "SIENNA": [160,82,45],
        "CHOCOLATE": [210,105,30],
        "PERU": [205,133,63],
        "SANDY_BROWN": [244,164,96],
        "BURLY_WOOD": [222,184,135],
        "TAN": [210,180,140],
        "ROSY_BROWN": [188,143,143],
        "MOCCASIN": [255,228,181],
        "NAVAJO_WHITE": [255,222,173],
        "PEACH_PUFF": [255,218,185],
        "MISTY_ROSE": [255,228,225],
        "LAVENDER_BLUSH": [255,240,245],
        "LINEN": [250,240,230],
        "OLD_LACE": [253,245,230],
        "PAPAYA_WHIP": [255,239,213],
        "SEA_SHELL": [255,245,238],
        "MINT_CREAM": [245,255,250],
        "SLATE_GRAY": [112,128,144],
        "LIGHT_SLATE_GRAY": [119,136,153],
        "LIGHT_STEEL_BLUE": [176,196,222],
        "LAVENDER": [230,230,250],
        "FLORAL_WHITE": [255,250,240],
        "ALICE_BLUE": [240,248,255],
        "GHOST_WHITE": [248,248,255],
        "HONEYDEW": [240,255,240],
        "IVORY": [255,255,240],
        "AZURE": [240,255,255],
        "SNOW": [255,250,250],
        "BLACK": [0,0,0],
        "DIM_GREY": [105,105,105],
        "GRAY": [128,128,128],
        "DARK_GREY": [169,169,169],
        "SILVER": [192,192,192],
        "LIGHT_GREY": [211,211,211],
        "GAINSBORO": [220,220,220],
        "WHITE_SMOKE": [245,245,245],
        "WHITE": [255,255,255]
    }

    TEXT = "text"

    HEX = "hex"
    HEXA = "hexa"

    HEX_RANGE = ([0, 16], [0, 16], [0, 16])
    HEXA_RANGE = (*HEX_RANGE, [0, 16])
    RGB_RANGE = ([0, 255], [0, 255], [0, 255])
    RGBA_RANGE = (*RGB_RANGE, [0, 255])
    SMALL_RGB_RANGE = ([0, 1], [0, 1], [0, 1])
    SMALL_RGBA_RANGE = (*SMALL_RGB_RANGE, [0, 1])
    HSL_RANGE = ([0, 360], [0, 100], [0, 100])
    HSLA_RANGE = (*HSL_RANGE, [0, 1])
    # larger value for alpha means more opaque :)

    RGB = "rgb"
    RBG = "rbg"
    GRB = "grb"
    GBR = "gbr"
    BRG = "brg"
    BGR = "bgr"

    RGB_SWIZZLES = [
        RGB,
        RBG,
        GRB,
        GBR,
        BRG,
        BGR]

    RGBA = "rgba"
    RGAB = "rgab"
    RBGA = "rbga"
    RBAG = "rbag"
    RAGB = "ragb"
    RABG = "rabg"
    GRBA = "grba"
    GRAB = "grab"
    GBRA = "gbra"
    GBAR = "gbar"
    GARB = "garb"
    GABR = "gabr"
    BRGA = "brga"
    BRAG = "brag"
    BGRA = "bgra"
    BGAR = "bgar"
    BARG = "barg"
    BAGR = "bagr"
    ARGB = "argb"
    ARBG = "arbg"
    AGRB = "agrb"
    AGBR = "agbr"
    ABRG = "abrg"
    ABGR = "abgr"

    RGBA_SWIZZLES = [
        RGBA,
        RGAB,
        RBGA,
        RBAG,
        RAGB,
        RABG,
        GRBA,
        GRAB,
        GBRA,
        GBAR,
        GARB,
        GABR,
        BRGA,
        BRAG,
        BGRA,
        BGAR,
        BARG,
        BAGR,
        ARGB,
        ARBG,
        AGRB,
        AGBR,
        ABRG,
        ABGR]

    SMALL_RGB = "small_rgb"
    SMALL_RBG = "small_rbg"
    SMALL_GRB = "small_grb"
    SMALL_GBR = "small_gbr"
    SMALL_BRG = "small_brg"
    SMALL_BGR = "small_bgr"

    SMALL_RGB_SWIZZLES = [
        SMALL_RGB,
        SMALL_RBG,
        SMALL_GRB,
        SMALL_GBR,
        SMALL_BRG,
        SMALL_BGR]

    SMALL_RGBA = "small_rgba"
    SMALL_RGAB = "small_rgab"
    SMALL_RBGA = "small_rbga"
    SMALL_RBAG = "small_rbag"
    SMALL_RAGB = "small_ragb"
    SMALL_RABG = "small_rabg"
    SMALL_GRBA = "small_grba"
    SMALL_GRAB = "small_grab"
    SMALL_GBRA = "small_gbra"
    SMALL_GBAR = "small_gbar"
    SMALL_GARB = "small_garb"
    SMALL_GABR = "small_gabr"
    SMALL_BRGA = "small_brga"
    SMALL_BRAG = "small_brag"
    SMALL_BGRA = "small_bgra"
    SMALL_BGAR = "small_bgar"
    SMALL_BARG = "small_barg"
    SMALL_BAGR = "small_bagr"
    SMALL_ARGB = "small_argb"
    SMALL_ARBG = "small_arbg"
    SMALL_AGRB = "small_agrb"
    SMALL_AGBR = "small_agbr"
    SMALL_ABRG = "small_abrg"
    SMALL_ABGR = "small_abgr"

    SMALL_RGBA_SWIZZLES = [
        SMALL_RGBA,
        SMALL_RGAB,
        SMALL_RBGA,
        SMALL_RBAG,
        SMALL_RAGB,
        SMALL_RABG,
        SMALL_GRBA,
        SMALL_GRAB,
        SMALL_GBRA,
        SMALL_GBAR,
        SMALL_GARB,
        SMALL_GABR,
        SMALL_BRGA,
        SMALL_BRAG,
        SMALL_BGRA,
        SMALL_BGAR,
        SMALL_BARG,
        SMALL_BAGR,
        SMALL_ARGB,
        SMALL_ARBG,
        SMALL_AGRB,
        SMALL_AGBR,
        SMALL_ABRG,
        SMALL_ABGR]

    HSL = "hsl"
    HLS = "hls"
    SHL = "shl"
    SLH = "slh"
    LHS = "lhs"
    LSH = "lsh"

    HSL_SWIZZLES = [
        HSL,
        HLS,
        SHL,
        SLH,
        LHS,
        LSH]

    HSLA = "hsla"
    HSAL = "hsal"
    HLSA = "hlsa"
    HLAS = "hlas"
    HASL = "hasl"
    HALS = "hals"
    SHLA = "shla"
    SHAL = "shal"
    SLHA = "slha"
    SLAH = "slah"
    SAHL = "sahl"
    SALH = "salh"
    LHSA = "lhsa"
    LHAS = "lhas"
    LSHA = "lsha"
    LSAH = "lsah"
    LAHS = "lahs"
    LASH = "lash"
    AHSL = "ahsl"
    AHLS = "ahls"
    ASHL = "ashl"
    ASLH = "aslh"
    ALHS = "alhs"
    ALSH = "alsh"

    HSLA_SWIZZLES = [
        HSLA,
        HSAL,
        HLSA,
        HLAS,
        HASL,
        HALS,
        SHLA,
        SHAL,
        SLHA,
        SLAH,
        SAHL,
        SALH,
        LHSA,
        LHAS,
        LSHA,
        LSAH,
        LAHS,
        LASH,
        AHSL,
        AHLS,
        ASHL,
        ASLH,
        ALHS,
        ALSH]

    SMALL_HSL = "small_hsl"
    SMALL_HLS = "small_hls"
    SMALL_SHL = "small_shl"
    SMALL_SLH = "small_slh"
    SMALL_LHS = "small_lhs"
    SMALL_LSH = "small_lsh"

    SMALL_HSL_SWIZZLES = [
        SMALL_HSL,
        SMALL_HLS,
        SMALL_SHL,
        SMALL_SLH,
        SMALL_LHS,
        SMALL_LSH]

    SMALL_HSLA = "small_hsla"
    SMALL_HSAL = "small_hsal"
    SMALL_HLSA = "small_hlsa"
    SMALL_HLAS = "small_hlas"
    SMALL_HASL = "small_hasl"
    SMALL_HALS = "small_hals"
    SMALL_SHLA = "small_shla"
    SMALL_SHAL = "small_shal"
    SMALL_SLHA = "small_slha"
    SMALL_SLAH = "small_slah"
    SMALL_SAHL = "small_sahl"
    SMALL_SALH = "small_salh"
    SMALL_LHSA = "small_lhsa"
    SMALL_LHAS = "small_lhas"
    SMALL_LSHA = "small_lsha"
    SMALL_LSAH = "small_lsah"
    SMALL_LAHS = "small_lahs"
    SMALL_LASH = "small_lash"
    SMALL_AHSL = "small_ahsl"
    SMALL_AHLS = "small_ahls"
    SMALL_ASHL = "small_ashl"
    SMALL_ASLH = "small_aslh"
    SMALL_ALHS = "small_alhs"
    SMALL_ALSH = "small_alsh"

    SMALL_HSLA_SWIZZLES = [
        SMALL_HSLA,
        SMALL_HSAL,
        SMALL_HLSA,
        SMALL_HLAS,
        SMALL_HASL,
        SMALL_HALS,
        SMALL_SHLA,
        SMALL_SHAL,
        SMALL_SLHA,
        SMALL_SLAH,
        SMALL_SAHL,
        SMALL_SALH,
        SMALL_LHSA,
        SMALL_LHAS,
        SMALL_LSHA,
        SMALL_LSAH,
        SMALL_LAHS,
        SMALL_LASH,
        SMALL_AHSL,
        SMALL_AHLS,
        SMALL_ASHL,
        SMALL_ASLH,
        SMALL_ALHS,
        SMALL_ALSH]

    COLOR_FORMATS = [
        RGB,
        RBG,
        GRB,
        GBR,
        BRG,
        BGR,
        RGBA,
        RGAB,
        RBGA,
        RBAG,
        RAGB,
        RABG,
        GRBA,
        GRAB,
        GBRA,
        GBAR,
        GARB,
        GABR,
        BRGA,
        BRAG,
        BGRA,
        BGAR,
        BARG,
        BAGR,
        ARGB,
        ARBG,
        AGRB,
        AGBR,
        ABRG,
        ABGR,
        HSL,
        HLS,
        SHL,
        SLH,
        LHS,
        LSH,
        HSLA,
        HSAL,
        HLSA,
        HLAS,
        HASL,
        HALS,
        SHLA,
        SHAL,
        SLHA,
        SLAH,
        SAHL,
        SALH,
        LHSA,
        LHAS,
        LSHA,
        LSAH,
        LAHS,
        LASH,
        AHSL,
        AHLS,
        ASHL,
        ASLH,
        ALHS,
        ALSH,
        SMALL_HSL,
        SMALL_HLS,
        SMALL_SHL,
        SMALL_SLH,
        SMALL_LHS,
        SMALL_LSH,
        SMALL_HSLA,
        SMALL_HSAL,
        SMALL_HLSA,
        SMALL_HLAS,
        SMALL_HASL,
        SMALL_HALS,
        SMALL_SHLA,
        SMALL_SHAL,
        SMALL_SLHA,
        SMALL_SLAH,
        SMALL_SAHL,
        SMALL_SALH,
        SMALL_LHSA,
        SMALL_LHAS,
        SMALL_LSHA,
        SMALL_LSAH,
        SMALL_LAHS,
        SMALL_LASH,
        SMALL_AHSL,
        SMALL_AHLS,
        SMALL_ASHL,
        SMALL_ASLH,
        SMALL_ALHS,
        SMALL_ALSH]

    SORTED_RGB = sorted(RGB)
    SORTED_RGBA = sorted(RGBA)
    SORTED_SMALL_RGB = sorted(SMALL_RGB)
    SORTED_SMALL_RGBA = sorted(SMALL_RGBA)
    SORTED_HSL = sorted(HSL)
    SORTED_HSLA = sorted(HSLA)
    SORTED_SMALL_HSL = sorted(SMALL_HSL)
    SORTED_SMALL_HSLA = sorted(SMALL_HSLA)