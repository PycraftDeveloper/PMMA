from math import pi as _math__pi
from os import sep as _os__sep
from os import cpu_count as _os__cpu_count

class Constants:
    """
    🟩 **R** -
    """
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

    CREATE_NO_WINDOW = 0x08000000

    WINDOWS = "windows"
    LINUX = "linux"
    MACOS = "macOS"
    JAVA = "java"
    ANDROID = "android"

    SMI = "nvidia-smi"
    WMI = "wmi"
    PYADL = "pyadl"

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

    DISPLAY_OBJECT = "display"
    EVENTS_OBJECT = "events"
    DRAW_OBJECT = "draw"
    ADVMATH_OBJECT = "advanced math"
    THREAD_OBJECT = "thread"
    TKINTER_OBJECT = "tkinter"
    BACKPACK_OBJECT = "backpack"
    COLOR_OBJECT = "color"
    CONSTANTS_OBJECT = "constants"
    COORDINATE_OBJECT = "coordinate"
    FILE_OBJECT = "file"
    FILECORE_OBJECT = "file core"
    PERLIN_OBJECT = "perlin"
    BENCHMARK_OBJECT = "benchmark"
    PASSPORT_OBJECT = "passport"
    SAMPLER_OBJECT = "sampler"
    REGISTRY_OBJECT = "registry"
    TEXT_OBJECT = "text"
    MEMORY_MANAGER_OBJECT = "memory manager"
    MEMORY_MANAGER_INTERMEDIARY_OBJECT = "memory manager intermediary"
    IMAGE_OBJECT = "image"
    LOGGING_OBJECT = "logging"
    LOGGING_INTERMEDIARY_OBJECT = "logging intermediary"
    OPENGL_OBJECT = "opengl"
    OPENGL_INTERMEDIARY_OBJECT = "opengl intermediary"
    GPUS_OBJECT = "GPUs"
    GPUS_INTERMEDIARY_OBJECT = "GPUs intermediary"
    CONTROLLER_INTERMEDIARY_OBJECT = "controller intermediary"
    SHADER_REFERENCE_MANAGER_OBJECT = "shader reference manager"
    TRANSITION_OBJECT =  "transition"
    TRANSITION_MANAGER_OBJECT = "transition manager"
    GPU_DISTRIBUTION_MANAGER_OBJECT = "gpu distribution manager"
    GPU_DISTRIBUTION_OBJECT = "gpu distribution"
    PROJECTION_INTERMEDIARY_OBJECT = "projection intermediary"
    SHAPE_GEOMETRY_MANAGER_OBJECT = "shape geometry manager"

    BACKSPACE_KEY_OBJECT = "backspace_key_object"
    TAB_KEY_OBJECT = "tab_key_object"
    CLEAR_KEY_OBJECT = "clear_key_object"
    RETURN_KEY_OBJECT = "return_key_object"
    PAUSE_KEY_OBJECT = "pause_key_object"
    ESCAPE_KEY_OBJECT = "escape_key_object"
    SPACE_KEY_OBJECT = "space_key_object"
    EXCLAMATIONMARK_KEY_OBJECT = "exclamationmark_key_object"
    DOUBLEQUOTE_KEY_OBJECT = "doublequote_key_object"
    HASHTAG_KEY_OBJECT = "hashtag_key_object"
    DOLLAR_KEY_OBJECT = "dollar_key_object"
    AMPERSAND_KEY_OBJECT = "ampersand_key_object"
    SINGLEQUOTE_KEY_OBJECT = "singlequote_key_object"
    LEFTPARENTHESIS_KEY_OBJECT = "leftparenthesis_key_object"
    RIGHTPARENTHESIS_KEY_OBJECT = "rightparenthesis_key_object"
    ASTERISK_KEY_OBJECT = "asterisk_key_object"
    PLUS_KEY_OBJECT = "plus_key_object"
    COMMA_KEY_OBJECT = "comma_key_object"
    MINUS_KEY_OBJECT = "minus_key_object"
    PERIOD_KEY_OBJECT = "period_key_object"
    FORWARDSLASH_KEY_OBJECT = "forwardslash_key_object"
    PRIMARY0_KEY_OBJECT = "primary0_key_object"
    PRIMARY1_KEY_OBJECT = "primary1_key_object"
    PRIMARY2_KEY_OBJECT = "primary2_key_object"
    PRIMARY3_KEY_OBJECT = "primary3_key_object"
    PRIMARY4_KEY_OBJECT = "primary4_key_object"
    PRIMARY5_KEY_OBJECT = "primary5_key_object"
    PRIMARY6_KEY_OBJECT = "primary6_key_object"
    PRIMARY7_KEY_OBJECT = "primary7_key_object"
    PRIMARY8_KEY_OBJECT = "primary8_key_object"
    PRIMARY9_KEY_OBJECT = "primary9_key_object"
    COLON_KEY_OBJECT = "colon_key_object"
    SEMICOLON_KEY_OBJECT = "semicolon_key_object"
    LESSTHAN_KEY_OBJECT = "lessthan_key_object"
    EQUALS_KEY_OBJECT = "equals_key_object"
    GREATERTHAN_KEY_OBJECT = "greaterthan_key_object"
    QUESTIONMARK_KEY_OBJECT = "questionmark_key_object"
    AT_KEY_OBJECT = "at_key_object"
    LEFTBRACKET_KEY_OBJECT = "leftbracket_key_object"
    BACKSLASH_KEY_OBJECT = "backslash_key_object"
    RIGHTBRACKET_KEY_OBJECT = "rightbracket_key_object"
    CARET_KEY_OBJECT = "caret_key_object"
    UNDERSCORE_KEY_OBJECT = "underscore_key_object"
    GRAVE_KEY_OBJECT = "grave_key_object"
    PRIMARYA_KEY_OBJECT = "primarya_key_object"
    PRIMARYB_KEY_OBJECT = "primaryb_key_object"
    PRIMARYC_KEY_OBJECT = "primaryc_key_object"
    PRIMARYD_KEY_OBJECT = "primaryd_key_object"
    PRIMARYE_KEY_OBJECT = "primarye_key_object"
    PRIMARYF_KEY_OBJECT = "primaryf_key_object"
    PRIMARYG_KEY_OBJECT = "primaryg_key_object"
    PRIMARYH_KEY_OBJECT = "primaryh_key_object"
    PRIMARYI_KEY_OBJECT = "primaryi_key_object"
    PRIMARYJ_KEY_OBJECT = "primaryj_key_object"
    PRIMARYK_KEY_OBJECT = "primaryk_key_object"
    PRIMARYL_KEY_OBJECT = "primaryl_key_object"
    PRIMARYM_KEY_OBJECT = "primarym_key_object"
    PRIMARYN_KEY_OBJECT = "primaryn_key_object"
    PRIMARYO_KEY_OBJECT = "primaryo_key_object"
    PRIMARYP_KEY_OBJECT = "primaryp_key_object"
    PRIMARYQ_KEY_OBJECT = "primaryq_key_object"
    PRIMARYR_KEY_OBJECT = "primaryr_key_object"
    PRIMARYS_KEY_OBJECT = "primarys_key_object"
    PRIMARYT_KEY_OBJECT = "primaryt_key_object"
    PRIMARYU_KEY_OBJECT = "primaryu_key_object"
    PRIMARYV_KEY_OBJECT = "primaryv_key_object"
    PRIMARYW_KEY_OBJECT = "primaryw_key_object"
    PRIMARYX_KEY_OBJECT = "primaryx_key_object"
    PRIMARYY_KEY_OBJECT = "primaryy_key_object"
    PRIMARYZ_KEY_OBJECT = "primaryz_key_object"
    DELETE_KEY_OBJECT = "delete_key_object"
    NUMPAD0_KEY_OBJECT = "numpad0_key_object"
    NUMPAD1_KEY_OBJECT = "numpad1_key_object"
    NUMPAD2_KEY_OBJECT = "numpad2_key_object"
    NUMPAD3_KEY_OBJECT = "numpad3_key_object"
    NUMPAD4_KEY_OBJECT = "numpad4_key_object"
    NUMPAD5_KEY_OBJECT = "numpad5_key_object"
    NUMPAD6_KEY_OBJECT = "numpad6_key_object"
    NUMPAD7_KEY_OBJECT = "numpad7_key_object"
    NUMPAD8_KEY_OBJECT = "numpad8_key_object"
    NUMPAD9_KEY_OBJECT = "numpad9_key_object"
    NUMPADPERIOD_KEY_OBJECT = "numpadperiod_key_object"
    NUMPADDIVIDE_KEY_OBJECT = "numpaddivide_key_object"
    NUMPADMULTIPLY_KEY_OBJECT = "numpadmultiply_key_object"
    NUMPADMINUS_KEY_OBJECT = "numpadminus_key_object"
    NUMPADPLUS_KEY_OBJECT = "numpadplus_key_object"
    NUMPADENTER_KEY_OBJECT = "numpadenter_key_object"
    NUMPADEQUALS_KEY_OBJECT = "numpadequals_key_object"
    UP_KEY_OBJECT = "up_key_object"
    DOWN_KEY_OBJECT = "down_key_object"
    RIGHT_KEY_OBJECT = "right_key_object"
    LEFT_KEY_OBJECT = "left_key_object"
    INSERT_KEY_OBJECT = "insert_key_object"
    HOME_KEY_OBJECT = "home_key_object"
    END_KEY_OBJECT = "end_key_object"
    PAGEUP_KEY_OBJECT = "pageup_key_object"
    PAGEDOWN_KEY_OBJECT = "pagedown_key_object"
    FUNCTION1_KEY_OBJECT = "function1_key_object"
    FUNCTION2_KEY_OBJECT = "function2_key_object"
    FUNCTION3_KEY_OBJECT = "function3_key_object"
    FUNCTION4_KEY_OBJECT = "function4_key_object"
    FUNCTION5_KEY_OBJECT = "function5_key_object"
    FUNCTION6_KEY_OBJECT = "function6_key_object"
    FUNCTION7_KEY_OBJECT = "function7_key_object"
    FUNCTION8_KEY_OBJECT = "function8_key_object"
    FUNCTION9_KEY_OBJECT = "function9_key_object"
    FUNCTION10_KEY_OBJECT = "function10_key_object"
    FUNCTION11_KEY_OBJECT = "function11_key_object"
    FUNCTION12_KEY_OBJECT = "function12_key_object"
    FUNCTION13_KEY_OBJECT = "function13_key_object"
    FUNCTION14_KEY_OBJECT = "function14_key_object"
    FUNCTION15_KEY_OBJECT = "function15_key_object"
    NUMLOCK_KEY_OBJECT = "numlock_key_object"
    CAPSLOCK_KEY_OBJECT = "capslock_key_object"
    SCROLLLOCK_KEY_OBJECT = "scrolllock_key_object"
    RIGHTSHIFT_KEY_OBJECT = "rightshift_key_object"
    LEFTSHIFT_KEY_OBJECT = "leftshift_key_object"
    SHIFT_KEY_OBJECT = "shift_key_object"
    RIGHTCONTROL_KEY_OBJECT = "rightcontrol_key_object"
    LEFTCONTROL_KEY_OBJECT = "leftcontrol_key_object"
    CONTROL_KEY_OBJECT = "control_key_object"
    RIGHTALT_KEY_OBJECT = "rightalt_key_object"
    LEFTALT_KEY_OBJECT = "leftalt_key_object"
    ALT_KEY_OBJECT = "alt_key_object"
    RIGHTMETA_KEY_OBJECT = "rightmeta_key_object"
    LEFTMETA_KEY_OBJECT = "leftmeta_key_object"
    META_KEY_OBJECT = "meta_key_object"
    LEFTSUPER_KEY_OBJECT = "leftsuper_key_object"
    RIGHTSUPER_KEY_OBJECT = "rightsuper_key_object"
    SUPER_KEY_OBJECT = "super_key_object"
    MODE_KEY_OBJECT = "mode_key_object"
    HELP_KEY_OBJECT = "help_key_object"
    PRINT_KEY_OBJECT = "print_key_object"
    SYSTEMREQUEST_KEY_OBJECT = "systemrequest_key_object"
    BREAK_KEY_OBJECT = "break_key_object"
    MENU_KEY_OBJECT = "menu_key_object"
    POWER_KEY_OBJECT = "power_key_object"
    EURO_KEY_OBJECT = "euro_key_object"
    ANDROIDBACK_KEY_OBJECT = "androidback_key_object"

    Y_BUTTON_OBJECT = "y_button_object"
    B_BUTTON_OBJECT = "b_button_object"
    A_BUTTON_OBJECT = "a_button_object"
    X_BUTTON_OBJECT = "x_button_object"
    HOME_BUTTON_OBJECT = "home_button_object"
    RIGHTJOYSTICK_BUTTON_OBJECT = "rightjoystick_button_object"
    LEFTJOYSTICK_BUTTON_OBJECT = "leftjoystick_button_object"
    OPTIONS_BUTTON_OBJECT = "options_button_object"
    SHARE_BUTTON_OBJECT = "share_button_object"
    RIGHT_TRIGGER_OBJECT = "right_trigger_object"
    LEFT_TRIGGER_OBJECT = "left_trigger_object"
    RIGHT_BUMPER_OBJECT = "right_bumper_object"
    LEFT_BUMPER_OBJECT = "left_bumper_object"
    CENTER_BUTTON_OBJECT = "center_button_object"
    LEFTJOYSTICK_AXIS_OBJECT = "leftjoystick_axis_object"
    RIGHTJOYSTICK_AXIS_OBJECT = "rightjoystick_axis_object"
    UPHAT_BUTTON_OBJECT = "uphat_button_object"
    DOWNHAT_BUTTON_OBJECT = "downhat_button_object"
    LEFTHAT_BUTTON_OBJECT = "lefthat_button_object"
    RIGHTHAT_BUTTON_OBJECT = "righthat_button_object"

    LEFTBUTTON_MOUSE_OBJECT = "leftbutton_mouse_object"
    MIDDLEBUTTON_MOUSE_OBJECT = "middlebutton_mouse_object"
    RIGHTBUTTON_MOUSE_OBJECT = "rightbutton_mouse_object"
    MOUSE_SCROLL_OBJECT = "mouse_scroll_object"
    MOUSE_POSITION_OBJECT = "mouse_position_object"

    APPTERMINATING_EVENT_OBJECT = "appterminating_event_object"
    APPLOWMEMORY_EVENT_OBJECT = "applowmemory_event_object"
    APPWILLENTERBACKGROUND_EVENT_OBJECT = "appwillenterbackground_event_object"
    APPDIDENTERBACKGROUND_EVENT_OBJECT = "appdidenterbackground_event_object"
    APPWILLENTERFOREGROUND_EVENT_OBJECT = "appwillenterforeground_event_object"
    APPDIDENTERFOREGROUND_EVENT_OBJECT = "appdidenterforeground_event_object"
    AUDIODEVICEADDED_EVENT_OBJECT = "audiodeviceadded_event_object"
    AUDIODEVICEREMOVED_EVENT_OBJECT = "audiodeviceremoved_event_object"
    CLIPBOARDUPDATE_EVENT_OBJECT = "clipboardupdate_event_object"
    DROPFILE_EVENT_OBJECT = "dropfile_event_object"
    DROPTEXT_EVENT_OBJECT = "droptext_event_object"
    DROPBEGIN_EVENT_OBJECT = "dropbegin_event_object"
    DROPCOMPLETE_EVENT_OBJECT = "dropcomplete_event_object"
    FINGERMOTION_EVENT_OBJECT = "fingermotion_event_object"
    FINGERDOWN_EVENT_OBJECT = "fingerdown_event_object"
    FINGERUP_EVENT_OBJECT = "fingerup_event_object"
    KEYMAPCHANGED_EVENT_OBJECT = "keymapchanged_event_object"
    LOCALECHANGED_EVENT_OBJECT = "localechanged_event_object"
    MULTIGESTURE_EVENT_OBJECT = "multigesture_event_object"
    QUIT_EVENT_OBJECT = "quit_event_object"
    RENDERTARGETSRESET_EVENT_OBJECT = "rendertargetsreset_event_object"
    RENDERDEVICERESET_EVENT_OBJECT = "renderdevicereset_event_object"
    SYSWMEVENT_EVENT_OBJECT = "syswmevent_event_object"
    VIDEORESIZE_EVENT_OBJECT = "videoresize_event_object"
    VIDEOEXPOSE_EVENT_OBJECT = "videoexpose_event_object"
    WINDOWSHOWN_EVENT_OBJECT = "windowshown_event_object"
    WINDOWHIDDEN_EVENT_OBJECT = "windowhidden_event_object"
    WINDOWEXPOSED_EVENT_OBJECT = "windowexposed_event_object"
    WINDOWMOVED_EVENT_OBJECT = "windowmoved_event_object"
    WINDOWRESIZED_EVENT_OBJECT = "windowresized_event_object"
    WINDOWSIZECHANGED_EVENT_OBJECT = "windowsizechanged_event_object"
    WINDOWMINIMIZED_EVENT_OBJECT = "windowminimized_event_object"
    WINDOWMAXIMIZED_EVENT_OBJECT = "windowmaximized_event_object"
    WINDOWRESTORED_EVENT_OBJECT = "windowrestored_event_object"
    WINDOWENTER_EVENT_OBJECT = "windowenter_event_object"
    WINDOWLEAVE_EVENT_OBJECT = "windowleave_event_object"
    WINDOWFOCUSGAINED_EVENT_OBJECT = "windowfocusgained_event_object"
    WINDOWFOCUSLOST_EVENT_OBJECT = "windowfocuslost_event_object"
    WINDOWCLOSE_EVENT_OBJECT = "windowclose_event_object"
    WINDOWTAKEFOCUS_EVENT_OBJECT = "windowtakefocus_event_object"
    WINDOWHITTEST_EVENT_OBJECT = "windowhittest_event_object"
    WINDOWICCPROFCHANGED_EVENT_OBJECT = "windowiccprofchanged_event_object"
    WINDOWDISPLAYCHANGED_EVENT_OBJECT = "windowdisplaychanged_event_object"
    JOYDEVICEADDED_OBJECT = "joydeviceadded_event_object"
    JOYDEVICEREMOVED_OBJECT = "joydeviceremoved_event_object"
    WINDOWFULLSCREENSTATECHANGED_OBJECT = "windowfullscreenstatuschanged_object"

    OBJECT_IDENTIFIERS = [
        DISPLAY_OBJECT,
        EVENTS_OBJECT,
        DRAW_OBJECT,
        ADVMATH_OBJECT,
        THREAD_OBJECT,
        TKINTER_OBJECT,
        BACKPACK_OBJECT,
        COLOR_OBJECT,
        CONSTANTS_OBJECT,
        COORDINATE_OBJECT,
        FILE_OBJECT,
        FILECORE_OBJECT,
        PERLIN_OBJECT,
        BENCHMARK_OBJECT,
        PASSPORT_OBJECT,
        SAMPLER_OBJECT,
        REGISTRY_OBJECT,
        TEXT_OBJECT,
        MEMORY_MANAGER_OBJECT,
        MEMORY_MANAGER_INTERMEDIARY_OBJECT,
        IMAGE_OBJECT,
        LOGGING_OBJECT,
        OPENGL_OBJECT,
        OPENGL_INTERMEDIARY_OBJECT,
        CONTROLLER_INTERMEDIARY_OBJECT,
        LOGGING_INTERMEDIARY_OBJECT,
        SHADER_REFERENCE_MANAGER_OBJECT,
        TRANSITION_MANAGER_OBJECT,
        TRANSITION_OBJECT,
        GPU_DISTRIBUTION_MANAGER_OBJECT,
        GPU_DISTRIBUTION_OBJECT,
        PROJECTION_INTERMEDIARY_OBJECT,
        SHAPE_GEOMETRY_MANAGER_OBJECT,

        GPUS_OBJECT,
        GPUS_INTERMEDIARY_OBJECT,
        BACKSPACE_KEY_OBJECT,
        TAB_KEY_OBJECT,
        CLEAR_KEY_OBJECT,
        RETURN_KEY_OBJECT,
        PAUSE_KEY_OBJECT,
        ESCAPE_KEY_OBJECT,
        SPACE_KEY_OBJECT,
        EXCLAMATIONMARK_KEY_OBJECT,
        DOUBLEQUOTE_KEY_OBJECT,
        HASHTAG_KEY_OBJECT,
        DOLLAR_KEY_OBJECT,
        AMPERSAND_KEY_OBJECT,
        SINGLEQUOTE_KEY_OBJECT,
        LEFTPARENTHESIS_KEY_OBJECT,
        RIGHTPARENTHESIS_KEY_OBJECT,
        ASTERISK_KEY_OBJECT,
        PLUS_KEY_OBJECT,
        COMMA_KEY_OBJECT,
        MINUS_KEY_OBJECT,
        PERIOD_KEY_OBJECT,
        FORWARDSLASH_KEY_OBJECT,
        PRIMARY0_KEY_OBJECT,
        PRIMARY1_KEY_OBJECT,
        PRIMARY2_KEY_OBJECT,
        PRIMARY3_KEY_OBJECT,
        PRIMARY4_KEY_OBJECT,
        PRIMARY5_KEY_OBJECT,
        PRIMARY6_KEY_OBJECT,
        PRIMARY7_KEY_OBJECT,
        PRIMARY8_KEY_OBJECT,
        PRIMARY9_KEY_OBJECT,
        COLON_KEY_OBJECT,
        SEMICOLON_KEY_OBJECT,
        LESSTHAN_KEY_OBJECT,
        EQUALS_KEY_OBJECT,
        GREATERTHAN_KEY_OBJECT,
        QUESTIONMARK_KEY_OBJECT,
        AT_KEY_OBJECT,
        LEFTBRACKET_KEY_OBJECT,
        BACKSLASH_KEY_OBJECT,
        RIGHTBRACKET_KEY_OBJECT,
        CARET_KEY_OBJECT,
        UNDERSCORE_KEY_OBJECT,
        GRAVE_KEY_OBJECT,
        PRIMARYA_KEY_OBJECT,
        PRIMARYB_KEY_OBJECT,
        PRIMARYC_KEY_OBJECT,
        PRIMARYD_KEY_OBJECT,
        PRIMARYE_KEY_OBJECT,
        PRIMARYF_KEY_OBJECT,
        PRIMARYG_KEY_OBJECT,
        PRIMARYH_KEY_OBJECT,
        PRIMARYI_KEY_OBJECT,
        PRIMARYJ_KEY_OBJECT,
        PRIMARYK_KEY_OBJECT,
        PRIMARYL_KEY_OBJECT,
        PRIMARYM_KEY_OBJECT,
        PRIMARYN_KEY_OBJECT,
        PRIMARYO_KEY_OBJECT,
        PRIMARYP_KEY_OBJECT,
        PRIMARYQ_KEY_OBJECT,
        PRIMARYR_KEY_OBJECT,
        PRIMARYS_KEY_OBJECT,
        PRIMARYT_KEY_OBJECT,
        PRIMARYU_KEY_OBJECT,
        PRIMARYV_KEY_OBJECT,
        PRIMARYW_KEY_OBJECT,
        PRIMARYX_KEY_OBJECT,
        PRIMARYY_KEY_OBJECT,
        PRIMARYZ_KEY_OBJECT,
        DELETE_KEY_OBJECT,
        NUMPAD0_KEY_OBJECT,
        NUMPAD1_KEY_OBJECT,
        NUMPAD2_KEY_OBJECT,
        NUMPAD3_KEY_OBJECT,
        NUMPAD4_KEY_OBJECT,
        NUMPAD5_KEY_OBJECT,
        NUMPAD6_KEY_OBJECT,
        NUMPAD7_KEY_OBJECT,
        NUMPAD8_KEY_OBJECT,
        NUMPAD9_KEY_OBJECT,
        NUMPADPERIOD_KEY_OBJECT,
        NUMPADDIVIDE_KEY_OBJECT,
        NUMPADMULTIPLY_KEY_OBJECT,
        NUMPADMINUS_KEY_OBJECT,
        NUMPADPLUS_KEY_OBJECT,
        NUMPADENTER_KEY_OBJECT,
        NUMPADEQUALS_KEY_OBJECT,
        UP_KEY_OBJECT,
        DOWN_KEY_OBJECT,
        RIGHT_KEY_OBJECT,
        LEFT_KEY_OBJECT,
        INSERT_KEY_OBJECT,
        HOME_KEY_OBJECT,
        END_KEY_OBJECT,
        PAGEUP_KEY_OBJECT,
        PAGEDOWN_KEY_OBJECT,
        FUNCTION1_KEY_OBJECT,
        FUNCTION2_KEY_OBJECT,
        FUNCTION3_KEY_OBJECT,
        FUNCTION4_KEY_OBJECT,
        FUNCTION5_KEY_OBJECT,
        FUNCTION6_KEY_OBJECT,
        FUNCTION7_KEY_OBJECT,
        FUNCTION8_KEY_OBJECT,
        FUNCTION9_KEY_OBJECT,
        FUNCTION10_KEY_OBJECT,
        FUNCTION11_KEY_OBJECT,
        FUNCTION12_KEY_OBJECT,
        FUNCTION13_KEY_OBJECT,
        FUNCTION14_KEY_OBJECT,
        FUNCTION15_KEY_OBJECT,
        NUMLOCK_KEY_OBJECT,
        CAPSLOCK_KEY_OBJECT,
        SCROLLLOCK_KEY_OBJECT,
        RIGHTSHIFT_KEY_OBJECT,
        LEFTSHIFT_KEY_OBJECT,
        SHIFT_KEY_OBJECT,
        RIGHTCONTROL_KEY_OBJECT,
        LEFTCONTROL_KEY_OBJECT,
        CONTROL_KEY_OBJECT,
        RIGHTALT_KEY_OBJECT,
        LEFTALT_KEY_OBJECT,
        ALT_KEY_OBJECT,
        RIGHTMETA_KEY_OBJECT,
        LEFTMETA_KEY_OBJECT,
        META_KEY_OBJECT,
        LEFTSUPER_KEY_OBJECT,
        RIGHTSUPER_KEY_OBJECT,
        SUPER_KEY_OBJECT,
        MODE_KEY_OBJECT,
        HELP_KEY_OBJECT,
        PRINT_KEY_OBJECT,
        SYSTEMREQUEST_KEY_OBJECT,
        BREAK_KEY_OBJECT,
        MENU_KEY_OBJECT,
        POWER_KEY_OBJECT,
        EURO_KEY_OBJECT,
        ANDROIDBACK_KEY_OBJECT,
        Y_BUTTON_OBJECT,
        B_BUTTON_OBJECT,
        A_BUTTON_OBJECT,
        X_BUTTON_OBJECT,
        HOME_BUTTON_OBJECT,
        RIGHTJOYSTICK_BUTTON_OBJECT,
        LEFTJOYSTICK_BUTTON_OBJECT,
        OPTIONS_BUTTON_OBJECT,
        SHARE_BUTTON_OBJECT,
        RIGHT_TRIGGER_OBJECT,
        LEFT_TRIGGER_OBJECT,
        RIGHT_BUMPER_OBJECT,
        LEFT_BUMPER_OBJECT,
        CENTER_BUTTON_OBJECT,
        LEFTJOYSTICK_AXIS_OBJECT,
        RIGHTJOYSTICK_AXIS_OBJECT,
        UPHAT_BUTTON_OBJECT,
        DOWNHAT_BUTTON_OBJECT,
        LEFTHAT_BUTTON_OBJECT,
        RIGHTHAT_BUTTON_OBJECT,
        LEFTBUTTON_MOUSE_OBJECT,
        MIDDLEBUTTON_MOUSE_OBJECT,
        RIGHTBUTTON_MOUSE_OBJECT,
        MOUSE_SCROLL_OBJECT,
        MOUSE_POSITION_OBJECT,
        APPTERMINATING_EVENT_OBJECT,
        APPLOWMEMORY_EVENT_OBJECT,
        APPWILLENTERBACKGROUND_EVENT_OBJECT,
        APPDIDENTERBACKGROUND_EVENT_OBJECT,
        APPWILLENTERFOREGROUND_EVENT_OBJECT,
        APPDIDENTERFOREGROUND_EVENT_OBJECT,
        AUDIODEVICEADDED_EVENT_OBJECT,
        AUDIODEVICEREMOVED_EVENT_OBJECT,
        CLIPBOARDUPDATE_EVENT_OBJECT,
        DROPFILE_EVENT_OBJECT,
        DROPTEXT_EVENT_OBJECT,
        DROPBEGIN_EVENT_OBJECT,
        DROPCOMPLETE_EVENT_OBJECT,
        FINGERMOTION_EVENT_OBJECT,
        FINGERDOWN_EVENT_OBJECT,
        FINGERUP_EVENT_OBJECT,
        KEYMAPCHANGED_EVENT_OBJECT,
        LOCALECHANGED_EVENT_OBJECT,
        MULTIGESTURE_EVENT_OBJECT,
        QUIT_EVENT_OBJECT,
        RENDERTARGETSRESET_EVENT_OBJECT,
        RENDERDEVICERESET_EVENT_OBJECT,
        SYSWMEVENT_EVENT_OBJECT,
        VIDEORESIZE_EVENT_OBJECT,
        VIDEOEXPOSE_EVENT_OBJECT,
        WINDOWSHOWN_EVENT_OBJECT,
        WINDOWHIDDEN_EVENT_OBJECT,
        WINDOWEXPOSED_EVENT_OBJECT,
        WINDOWMOVED_EVENT_OBJECT,
        WINDOWRESIZED_EVENT_OBJECT,
        WINDOWSIZECHANGED_EVENT_OBJECT,
        WINDOWMINIMIZED_EVENT_OBJECT,
        WINDOWMAXIMIZED_EVENT_OBJECT,
        WINDOWRESTORED_EVENT_OBJECT,
        WINDOWENTER_EVENT_OBJECT,
        WINDOWLEAVE_EVENT_OBJECT,
        WINDOWFOCUSGAINED_EVENT_OBJECT,
        WINDOWFOCUSLOST_EVENT_OBJECT,
        WINDOWCLOSE_EVENT_OBJECT,
        WINDOWTAKEFOCUS_EVENT_OBJECT,
        WINDOWHITTEST_EVENT_OBJECT,
        WINDOWICCPROFCHANGED_EVENT_OBJECT,
        WINDOWDISPLAYCHANGED_EVENT_OBJECT,
        JOYDEVICEADDED_OBJECT,
        JOYDEVICEREMOVED_OBJECT,

        WINDOWFULLSCREENSTATECHANGED_OBJECT
    ]

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