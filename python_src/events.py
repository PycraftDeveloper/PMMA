import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.backpack import Backpack as _Backpack

class Events:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        initialize(self, unique_instance=Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True, requires_display_mode_set=True)

    def handle(self, automatically_apply_events_to_application=True):
        if Registry.display_mode == Constants.PYGAME:
            raw_events = _pygame.event.get()
            for event in raw_events:
                if event.type == _pygame.QUIT:
                    pass

class Backspace_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_double_tap_timing(value)

class Tab_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_double_tap_timing(value)

class Clear_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_double_tap_timing(value)

class Return_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_double_tap_timing(value)

class Pause_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_double_tap_timing(value)

class Escape_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_double_tap_timing(value)

class Space_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_double_tap_timing(value)

class ExclamationMark_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_double_tap_timing(value)

class DoubleQuote_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_double_tap_timing(value)

class Hashtag_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_double_tap_timing(value)

class Dollar_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_double_tap_timing(value)

class Ampersand_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_double_tap_timing(value)

class SingleQuote_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_double_tap_timing(value)

class LeftParenthesis_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_double_tap_timing(value)

class RightParenthesis_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_double_tap_timing(value)

class Asterisk_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_double_tap_timing(value)

class Plus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_double_tap_timing(value)

class Comma_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_double_tap_timing(value)

class Minus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_double_tap_timing(value)

class Period_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_double_tap_timing(value)

class ForwardSlash_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_double_tap_timing(value)

class Primary0_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_double_tap_timing(value)

class Primary1_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_double_tap_timing(value)

class Primary2_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_double_tap_timing(value)

class Primary3_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_double_tap_timing(value)

class Primary4_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_double_tap_timing(value)

class Primary5_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_double_tap_timing(value)

class Primary6_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_double_tap_timing(value)

class Primary7_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_double_tap_timing(value)

class Primary8_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_double_tap_timing(value)

class Primary9_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_double_tap_timing(value)

class Colon_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_double_tap_timing(value)

class SemiColon_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_double_tap_timing(value)

class LessThan_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_double_tap_timing(value)

class Equals_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_double_tap_timing(value)

class GreaterThan_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_double_tap_timing(value)

class QuestionMark_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_double_tap_timing(value)

class At_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_double_tap_timing(value)

class LeftBracket_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_double_tap_timing(value)

class BackSlash_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_double_tap_timing(value)

class RightBracket_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_double_tap_timing(value)

class Caret_KEY: # ^
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_double_tap_timing(value)

class Underscore_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_double_tap_timing(value)

class Grave_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryA_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryB_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryC_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryD_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryE_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryF_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryG_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryH_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryI_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryJ_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryK_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryL_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryM_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryN_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryO_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryP_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryQ_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_double_tap_timing(value)

class primaryR_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryS_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryT_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryU_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryV_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryW_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryX_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryY_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryZ_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_double_tap_timing(value)

class Delete_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_double_tap_timing(value)

class Numpad0_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_double_tap_timing(value)

class Numpad1_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_double_tap_timing(value)

class Numpad2_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_double_tap_timing(value)

class Numpad3_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_double_tap_timing(value)

class Numpad4_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_double_tap_timing(value)

class Numpad5_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_double_tap_timing(value)

class Numpad6_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_double_tap_timing(value)

class Numpad7_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_double_tap_timing(value)

class Numpad8_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_double_tap_timing(value)

class Numpad9_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_double_tap_timing(value)

class NumpadPeriod_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_double_tap_timing(value)

class NumpadDivide_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_double_tap_timing(value)

class NumpadMultiply_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_double_tap_timing(value)

class NumpadMinus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_double_tap_timing(value)

class NumpadPlus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_double_tap_timing(value)

class NumpadEnter_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_double_tap_timing(value)

class NumpadEquals_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_double_tap_timing(value)

class Up_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_double_tap_timing(value)

class Down_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_double_tap_timing(value)

class Right_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_double_tap_timing(value)

class Left_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_double_tap_timing(value)

class Insert_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_double_tap_timing(value)

class Home_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_double_tap_timing(value)

class End_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_double_tap_timing(value)

class PageUp_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_double_tap_timing(value)

class PageDown_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_double_tap_timing(value)

class Function1_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_double_tap_timing(value)

class Function2_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_double_tap_timing(value)

class Function3_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_double_tap_timing(value)

class Function4_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_double_tap_timing(value)

class Function5_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_double_tap_timing(value)

class Function6_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_double_tap_timing(value)

class Function7_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_double_tap_timing(value)

class Function8_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_double_tap_timing(value)

class Function9_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_double_tap_timing(value)

class Function10_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_double_tap_timing(value)

class Function11_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_double_tap_timing(value)

class Function12_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_double_tap_timing(value)

class Function13_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_double_tap_timing(value)

class Function14_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_double_tap_timing(value)

class Function15_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_double_tap_timing(value)

class NumLock_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_double_tap_timing(value)

class CapsLock_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_double_tap_timing(value)

class ScrollLock_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_double_tap_timing(value)

class RightShift_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_double_tap_timing(value)

class LeftShift_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_double_tap_timing(value)

class Shift_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_double_tap_timing(value)

class RightControl_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_double_tap_timing(value)

class LeftControl_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_double_tap_timing(value)

class Control_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_double_tap_timing(value)

class RightAlt_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_double_tap_timing(value)

class LeftAlt_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_double_tap_timing(value)

class Alt_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_double_tap_timing(value)

class RightMeta_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_double_tap_timing(value)

class LeftMeta_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_double_tap_timing(value)

class Meta_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_double_tap_timing(value)

class LeftSuper_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_double_tap_timing(value)

class RightSuper_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_double_tap_timing(value)

class Super_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_double_tap_timing(value)

class Mode_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_double_tap_timing(value)

class Help_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_double_tap_timing(value)

class Print_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_double_tap_timing(value)

class SystemRequest_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_double_tap_timing(value)

class Break_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_double_tap_timing(value)

class Menu_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_double_tap_timing(value)

class Power_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_double_tap_timing(value)

class Euro_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_double_tap_timing(value)

class AndroidBack_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_double_tap_timing(value)

class Y_BUTTON: # 3
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.Y_BUTTON_OBJECT].set_double_tap_timing(value)

class B_BUTTON: # 2
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.B_BUTTON_OBJECT].set_double_tap_timing(value)

class A_BUTTON: # 1
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.A_BUTTON_OBJECT].set_double_tap_timing(value)

class X_BUTTON: # 0
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.X_BUTTON_OBJECT].set_double_tap_timing(value)

class Home_BUTTON: # 12
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HOME_BUTTON_OBJECT].set_double_tap_timing(value)

class RightJoystick_BUTTON: # 11
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_BUTTON_OBJECT].set_double_tap_timing(value)

class LeftJoystick_BUTTON: # 10
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTJOYSTICK_BUTTON_OBJECT].set_double_tap_timing(value)

class Options_BUTTON: # 9
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.OPTIONS_BUTTON_OBJECT].set_double_tap_timing(value)

class Share_BUTTON: # 8
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SHARE_BUTTON_OBJECT].set_double_tap_timing(value)

class Right_TRIGGER: # 7
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_TRIGGER_OBJECT].set_double_tap_timing(value)

class Left_TRIGGER: # 6
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[ConstantsLEFT_TRIGGER_OBJECT.].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFT_TRIGGER_OBJECT].set_double_tap_timing(value)

class Right_BUMPER: # 5
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_BUMPER_OBJECT].set_double_tap_timing(value)

class Left_BUMPER: # 4
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFT_BUMPER_OBJECT].set_double_tap_timing(value)

class Center_BUTTON: # 13
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CENTER_BUTTON_OBJECT].set_double_tap_timing(value)

class LeftJoystick_AXIS:
    def __init__(self):
        initialize(self)

    def get_x_axis(self):
        return Registry.pmma_module_spine[Constants.LEFTJOYSTICK_AXIS_OBJECT].get_x_axis()

    def get_y_axis(self):
        return Registry.pmma_module_spine[Constants.LEFTJOYSTICK_AXIS_OBJECT].get_y_axis()

    def set_x_axis(self, value):
        Registry.pmma_module_spine[Constants.LEFTJOYSTICK_AXIS_OBJECT].set_x_axis(value)

    def set_y_axis(self, value):
        Registry.pmma_module_spine[Constants.LEFTJOYSTICK_AXIS_OBJECT].set_y_axis(value)

class RightJoystick_AXIS:
    def __init__(self):
        initialize(self)

    def get_x_axis(self):
        return Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_AXIS_OBJECT].get_x_axis()

    def get_y_axis(self):
        return Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_AXIS_OBJECT].get_y_axis()

    def set_x_axis(self, value):
        Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_AXIS_OBJECT].set_x_axis(value)

    def set_y_axis(self, value):
        Registry.pmma_module_spine[Constants.RIGHTJOYSTICK_AXIS_OBJECT].set_y_axis(value)

class UpHat_BUTTON:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.UPHAT_BUTTON_OBJECT].set_double_tap_timing(value)

class DownHat_BUTTON:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOWNHAT_BUTTON_OBJECT].set_double_tap_timing(value)

class LeftHat_BUTTON:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTHAT_BUTTON_OBJECT].set_double_tap_timing(value)

class RightHat_BUTTON:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTHAT_BUTTON_OBJECT].set_double_tap_timing(value)

class LeftButton_MOUSE:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_double_tap_timing(value)

class MiddleButton_MOUSE:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_double_tap_timing(value)

class RightButton_MOUSE:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_double_tap_timing(value)

class Mouse_SCROLL:
    def __init__(self):
        initialize(self)

        self._scroll_value = 0
        self._scroll_displacement = 0

    def get_scroll_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].get_scroll_displacement()

    def get_scroll_value(self):
        return Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].get_scroll_value()

    def set_scroll_value(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].set_scroll_value(value)

class Mouse_POSITION:
    def __init__(self):
        initialize(self)

    def get_axis_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_axis_displacement()

    def get_x_axis_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_x_axis_displacement()

    def get_y_axis_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_y_axis_displacement()

    def get_x_axis(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_x_axis()

    def get_y_axis(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_y_axis()

    def set_x_axis(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].set_x_axis(value)

    def set_y_axis(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].set_y_axis(value)

class Active_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.ACTIVE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.ACTIVE_EVENT_OBJECT].get_value()

class AppTerminating_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPTERMINATING_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPTERMINATING_EVENT_OBJECT].get_value()

class AppLowMemory_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPLOWMEMORY_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPLOWMEMORY_EVENT_OBJECT].get_value()

class AppWillEnterBackground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT].get_value()

class AppDidEnterBackground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT].get_value()

class AppWillEnterForeground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT].get_value()

class AppDidEnterForeground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT].get_value()

class AudioDeviceAdded_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.AUDIODEVICEADDED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.AUDIODEVICEADDED_EVENT_OBJECT].get_value()

class AudioDeviceRemoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.AUDIODEVICEREMOVED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.AUDIODEVICEREMOVED_EVENT_OBJECT].get_value()

class ClipBoardUpdate_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.CLIPBOARDUPDATE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.CLIPBOARDUPDATE_EVENT_OBJECT].get_value()

class DollarGesture_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DOLLARGESTURE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DOLLARGESTURE_EVENT_OBJECT].get_value()

class DollarCord_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DOLLARCORD_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DOLLARCORD_EVENT_OBJECT].get_value()

class DropFile_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPFILE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPFILE_EVENT_OBJECT].get_value()

class DropText_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPTEXT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPTEXT_EVENT_OBJECT].get_value()

class DropBegin_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPBEGIN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPBEGIN_EVENT_OBJECT].get_value()

class DropComplete_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPCOMPLETE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPCOMPLETE_EVENT_OBJECT].get_value()

class FingerMotion_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.FINGERMOTION_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.FINGERMOTION_EVENT_OBJECT].get_value()

class FingerDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.FINGERDOWN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.FINGERDOWN_EVENT_OBJECT].get_value()

class FingerUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.FINGERUP_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.FINGERUP_EVENT_OBJECT].get_value()

class KeyDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.KEYDOWN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.KEYDOWN_EVENT_OBJECT].get_value()

class KeyUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.KEYUP_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.KEYUP_EVENT_OBJECT].get_value()

class KeyMapChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.KEYMAPCHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.KEYMAPCHANGED_EVENT_OBJECT].get_value()

class LocaleChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.LOCALECHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.LOCALECHANGED_EVENT_OBJECT].get_value()

class MouseMotion_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MOUSEMOTION_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MOUSEMOTION_EVENT_OBJECT].get_value()

class MouseButtonDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MOUSEBUTTONDOWN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MOUSEBUTTONDOWN_EVENT_OBJECT].get_value()

class MouseButtonUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MOUSEBUTTONUP_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MOUSEBUTTONUP_EVENT_OBJECT].get_value()

class MouseWheel_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MOUSEWHEEL_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MOUSEWHEEL_EVENT_OBJECT].get_value()

class MultiGesture_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MULTIGESTURE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MULTIGESTURE_EVENT_OBJECT].get_value()

class NoEvent_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.NOEVENT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.NOEVENT_EVENT_OBJECT].get_value()

class Quit_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.QUIT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.QUIT_EVENT_OBJECT].get_value()

class RenderTargetsReset_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.RENDERTARGETSRESET_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.RENDERTARGETSRESET_EVENT_OBJECT].get_value()

class RenderDeviceReset_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.RENDERDEVICERESET_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.RENDERDEVICERESET_EVENT_OBJECT].get_value()

class SysWMEvent_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.SYSWMEVENT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.SYSWMEVENT_EVENT_OBJECT].get_value()

class TextInput_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.TEXTINPUT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.TEXTINPUT_EVENT_OBJECT].get_value()

class TextEditing_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.TEXTEDITING_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.TEXTEDITING_EVENT_OBJECT].get_value()

class VideoResize_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.VIDEORESIZE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.VIDEORESIZE_EVENT_OBJECT].get_value()

class VideoExpose_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.VIDEOEXPOSE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.VIDEOEXPOSE_EVENT_OBJECT].get_value()

class MidiIn_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MIDIIN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MIDIIN_EVENT_OBJECT].get_value()

class MidiOut_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MIDIOUT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MIDIOUT_EVENT_OBJECT].get_value()

class WindowShown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWSHOWN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWSHOWN_EVENT_OBJECT].get_value()

class WindowHidden_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWHIDDEN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWHIDDEN_EVENT_OBJECT].get_value()

class WindowExposed_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWEXPOSED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWEXPOSED_EVENT_OBJECT].get_value()

class WindowMoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWMOVED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWMOVED_EVENT_OBJECT].get_value()

class WindowResized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWRESIZED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWRESIZED_EVENT_OBJECT].get_value()

class WindowSizeChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWSIZECHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWSIZECHANGED_EVENT_OBJECT].get_value()

class WindowMinimized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWMINIMIZED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWMINIMIZED_EVENT_OBJECT].get_value()

class WindowMaximized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWMAXIMIZED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWMAXIMIZED_EVENT_OBJECT].get_value()

class WindowRestored_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWRESTORED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWRESTORED_EVENT_OBJECT].get_value()

class WindowEnter_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWENTER_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWENTER_EVENT_OBJECT].get_value()

class WindowLeave_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWLEAVE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWLEAVE_EVENT_OBJECT].get_value()

class WindowFocusGained_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].get_value()

class WindowFocusLost_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWFOCUSLOST_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWFOCUSLOST_EVENT_OBJECT].get_value()

class WindowClose_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWCLOSE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWCLOSE_EVENT_OBJECT].get_value()

class WindowTakeFocus_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWTAKEFOCUS_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWTAKEFOCUS_EVENT_OBJECT].get_value()

class WindowHitTest_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWHITTEST_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWHITTEST_EVENT_OBJECT].get_value()

class WindowICCPROFChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT].get_value()

class WindowDisplayChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].get_value()