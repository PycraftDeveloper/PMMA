class Constants:
    DECIMAL = "decimal"
    PERCENTAGE = "percentage"

    VALUE = "value"
    UPDATING = "updating"
    MANUALLY_SET = "manually_set"

    class HatStates:
        NOT_PRESSED = "HAT NOT PRESSED"
        PRESSED_UP = "HAT PRESSED UP"
        PRESSED_RIGHT = "HAT PRESSED RIGHT"
        PRESSED_DOWN = "HAT PRESSED DOWN"
        PRESSED_LEFT = "HAT PRESSED LEFT"
        PRESSED_UP_RIGHT = "HAT PRESSED UP-RIGHT"
        PRESSED_DOWN_RIGHT = "HAT PRESSED DOWN-RIGHT"
        PRESSED_DOWN_LEFT = "HAT PRESSED DOWN-LEFT"
        PRESSED_UP_LEFT = "HAT PRESSED UP-LEFT"

    class OperatingSystems:
        ANDROID = "Android"
        BSD = "BSD"
        EMSCRIPTEN = "Emscripten"
        HAIKU = "Haiku"
        HURD = "Hurd"
        IOS = "iOS"
        LINUX = "Linux"
        NX = "Nintendo Switch"
        MACOS = "MacOS"
        PS4 = "Play Station 4"
        PS5 = "Play Station 5"
        VISIONOS = "VisionOS"
        WINDOWS = "Windows"
        WINRT = "WinRT"
        XBOXONE = "XboxOne"
        UNKNOWN = "Unknown"

    class GraphicsBackends:
        NO_RENDERER = "No Renderer"
        DIRECT3D11 = "Direct3D 11.0"
        DIRECT3D12 = "Direct3D 12.0"
        GNM = "GNM" # PlayStation (Developer license needed)
        METAL = "Metal"
        NVN = "NVN" # Nintendo Switch
        OPENGL_ES = "OpenGL ES"
        OPENGL = "OpenGL"
        VULKAN = "Vulkan"
        UNKNOWN = "Unknown"

    class TkinterStyles:
        BUTTON = "TButton"
        CHECKBUTTON = "TCheckbutton"
        COMBOBOX = "TCombobox"
        ENTRY = "TEntry"
        FRAME = "TFrame"
        LABEL = "TLabel"
        LABELFRAME = "TLabelFrame"
        MENUBUTTON = "TMenubutton"
        NOTEBOOK = "TNotebook"
        PANEDWINDOW = "TPanedwindow"
        HORIZONTAL_PROGRESSBAR = "Horizontal.TProgressbar"
        VERTICAL_PROGRESSBAR = "Vertical.TProgressbar"
        RADIOBUTTON = "TRadiobutton"
        HORIZONTAL_SCALE = "Horizontal.TScale"
        VERTICAL_SCALE = "Vertical.TScale"
        HORIZONTAL_SCROLLBAR = "Horizontal.TScrollbar"
        VERTICAL_SCROLLBAR = "Vertical.TScrollbar"
        SEPARATOR = "TSeparator"
        SIZEGRIP = "TSizegrip"
        TREEVIEW = "Treeview"

    class Colors:
        RED = "red"
        ORANGE = "ora"
        YELLOW = "yel"
        GREEN = "gre"
        BLUE = "blu"
        INDIGO = "ind"
        VIOLET = "vio"
        BLACK = "blk"
        WHITE = "wht"
        GRAY = "gry"
        CYAN = "cya"
        MAGENTA = "mag"
        LIGHT_RED = "lrd"
        LIGHT_ORANGE = "lor"
        LIGHT_YELLOW = "lyl"
        LIGHT_GREEN = "lgr"
        LIGHT_BLUE = "lbl"
        LIGHT_INDIGO = "lin"
        LIGHT_VIOLET = "lvi"
        SKY_BLUE = "sky"
        GOLD = "gol"
        SILVER = "slv"
        BROWN = "brn"
        PEA_GREEN = "pea"
        OLIVE = "olv"
        TAN = "tan"
        NAVY = "nav"
        MAROON = "mar"
        PURPLE = "pur"
        CORAL = "cor"
        TEAL = "tea"
        CHERRY = "che"
        LIME = "lim"
        MOCCASIN = "moc"
        BEIGE = "bei"
        DUSK = "dus"
        SALT = "slt"
        LAVENDER = "lav"
        PEACH = "pch"
        MINT = "mnt"
        ROSE = "rse"
        BRONZE = "brz"
        AQUAMARINE = "aqu"
        PERIWINKLE = "per"
        ICE_BLUE = "ice"
        PLUM = "plm"
        COPPER = "cop"
        CREAM = "crm"
        PINK = "pnk"
        FOREST = "for"
        SAND = "snd"
        AMBER = "amb"
        AZURE = "azr"
        TURQUOISE = "trq"
        COBALT = "cob"
        CHARCOAL = "chc"
        IVORY = "ivr"
        MUSCAT = "mus"
        OLIVE_DRAB = "old"
        SAGE_GREEN = "sgr"
        WHEAT = "whe"
        RUBY = "rub"
        EMERALD = "emr"
        SLIME_GREEN = "slm"
        ONYX = "ony"
        SPEARMINT = "spe"
        CHARTREUSE = "chr"
        BLOOD_RED = "bld"
        SPRING_GREEN = "spg"
        DARK_RED = "dre"
        DARK_ORANGE = "dor"
        DARK_YELLOW = "dye"
        DARK_GREEN = "dgr"
        DARK_BLUE = "dbl"
        DARK_INDIGO = "din"
        DARK_VIOLET = "dvi"
        DARK_GREY = "dgy"
        LIGHT_GREY = "lgy"
        OCHRE = "och"
        UMBER = "umb"
        TERRACOTTA = "ter"
        MUD_BROWN = "mud"
        SAPPHIRE = "sap"
        AMYTHYST = "amy"
        GARNET = "gnt"
        TAUPE = "tpe"
        BUBBLEGUM = "bub"
        MIST_ROSE = "mrs"
        HONEY = "hny"
        SEAFOAM = "sea"
        NEON_GREEN = "neo"
        ELECTRIC_PINK = "elc"
        SUNFLOWER = "sun"
        CRIMSON = "crl"
        CERULIAN = "cyl"
        MOSS_GREEN = "mgn"
        SAFFRON = "sfr"
        APRICOT = "apr"
        FLAX = "flx"
        MYSTIC_PURPLE = "mys"

class InternalConstants:
    DATA_COLLECTION_METHODS = "data_collection_methods"

    SMI = "smi"
    WMI = "wmi"
    PYADL = "pyadl"

    CREATE_NO_WINDOW = 0x08000000

    TKINTER_STYLES = [
        Constants.TkinterStyles.BUTTON,
        Constants.TkinterStyles.CHECKBUTTON,
        Constants.TkinterStyles.COMBOBOX,
        Constants.TkinterStyles.ENTRY,
        Constants.TkinterStyles.FRAME,
        Constants.TkinterStyles.LABEL,
        Constants.TkinterStyles.LABELFRAME,
        Constants.TkinterStyles.MENUBUTTON,
        Constants.TkinterStyles.NOTEBOOK,
        Constants.TkinterStyles.PANEDWINDOW,
        Constants.TkinterStyles.HORIZONTAL_PROGRESSBAR,
        Constants.TkinterStyles.VERTICAL_PROGRESSBAR,
        Constants.TkinterStyles.RADIOBUTTON,
        Constants.TkinterStyles.HORIZONTAL_SCALE,
        Constants.TkinterStyles.VERTICAL_SCALE,
        Constants.TkinterStyles.HORIZONTAL_SCROLLBAR,
        Constants.TkinterStyles.VERTICAL_SCROLLBAR,
        Constants.TkinterStyles.SEPARATOR,
        Constants.TkinterStyles.SIZEGRIP,
        Constants.TkinterStyles.TREEVIEW
    ]

    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
    SECONDS_PER_DAY = SECONDS_PER_HOUR * 24
    DAYS_PER_YEAR = 365.25  # accounting for leap years
    DAYS_PER_MONTH = DAYS_PER_YEAR / 12
    HOURS_PER_DAY = 24
    MINUTES_PER_HOUR = 60
    MICROSECONDS_PER_SECOND = 1e6