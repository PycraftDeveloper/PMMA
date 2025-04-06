from pmma.python_src.constants import Constants as _Constants

class InternalConstants:
    TKINTER_STYLES = [
        _Constants.TKINTER_STYLE_BUTTON,
        _Constants.TKINTER_STYLE_CHECKBUTTON,
        _Constants.TKINTER_STYLE_COMBOBOX,
        _Constants.TKINTER_STYLE_ENTRY,
        _Constants.TKINTER_STYLE_FRAME,
        _Constants.TKINTER_STYLE_LABEL,
        _Constants.TKINTER_STYLE_LABELFRAME,
        _Constants.TKINTER_STYLE_MENUBUTTON,
        _Constants.TKINTER_STYLE_NOTEBOOK,
        _Constants.TKINTER_STYLE_PANEDWINDOW,
        _Constants.TKINTER_STYLE_HORIZONTAL_PROGRESSBAR,
        _Constants.TKINTER_STYLE_VERTICAL_PROGRESSBAR,
        _Constants.TKINTER_STYLE_RADIOBUTTON,
        _Constants.TKINTER_STYLE_HORIZONTAL_SCALE,
        _Constants.TKINTER_STYLE_VERTICAL_SCALE,
        _Constants.TKINTER_STYLE_HORIZONTAL_SCROLLBAR,
        _Constants.TKINTER_STYLE_VERTICAL_SCROLLBAR,
        _Constants.TKINTER_STYLE_SEPARATOR,
        _Constants.TKINTER_STYLE_SIZEGRIP,
        _Constants.TKINTER_STYLE_TREEVIEW
    ]
    LINE = "line"
    RADIAL_POLYGON = "radial polygon"
    RECTANGLE = "rectangle"
    ARC = "arc"
    ELLIPSE = "ellipse"
    POLYGON = "polygon"

    SMI = "nvidia-smi"
    WMI = "wmi"
    PYADL = "pyadl"

    CREATE_NO_WINDOW = 0x08000000

    RENDER_PIPELINE_COMPATIBLE = "render pipeline compatible"
    PMMA_OBJECT_IDENTIFIER = "PMMA object identifier"
    ADDITIONAL_INTERNAL_RENDER_DATA = "additional internal render data"

    DISPLAY_OBJECT = "display"
    EVENTS_OBJECT = "events"
    FILECORE_OBJECT = "file core"
    MEMORY_MANAGER_INTERMEDIARY_OBJECT = "memory manager intermediary"
    LOGGING_INTERMEDIARY_OBJECT = "logging intermediary"
    OPENGL_OBJECT = "opengl"
    GPUS_INTERMEDIARY_OBJECT = "GPUs intermediary"
    CONTROLLER_INTERMEDIARY_OBJECT = "controller intermediary"
    SHADER_REFERENCE_MANAGER_OBJECT = "shader reference manager"
    TRANSITION_MANAGER_OBJECT = "transition manager"
    GPU_DISTRIBUTION_MANAGER_OBJECT = "gpu distribution manager"
    SHAPE_GEOMETRY_MANAGER_OBJECT = "shape geometry manager"
    RENDER_PIPELINE_MANAGER_OBJECT = "render pipeline manager"
    CONVERTER_INTERMEDIARY_MANAGER_OBJECT = "converter intermediary manager object"
    CAMERA_MANAGER_OBJECT = "camera intermediary object"

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
        FILECORE_OBJECT,
        MEMORY_MANAGER_INTERMEDIARY_OBJECT,
        OPENGL_OBJECT,
        CONTROLLER_INTERMEDIARY_OBJECT,
        LOGGING_INTERMEDIARY_OBJECT,
        SHADER_REFERENCE_MANAGER_OBJECT,
        TRANSITION_MANAGER_OBJECT,
        GPU_DISTRIBUTION_MANAGER_OBJECT,
        SHAPE_GEOMETRY_MANAGER_OBJECT,
        RENDER_PIPELINE_MANAGER_OBJECT,
        CONVERTER_INTERMEDIARY_MANAGER_OBJECT,
        CAMERA_MANAGER_OBJECT,
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