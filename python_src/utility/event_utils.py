from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Backspace_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.BACKSPACE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Tab_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.TAB_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Clear_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.CLEAR_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Return_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RETURN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Pause_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PAUSE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Escape_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.ESCAPE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Space_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SPACE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class ExclamationMark_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.EXCLAMATIONMARK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class DoubleQuote_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.DOUBLEQUOTE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Hashtag_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.HASHTAG_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Dollar_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.DOLLAR_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Ampersand_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.AMPERSAND_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class SingleQuote_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SINGLEQUOTE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftParenthesis_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTPARENTHESIS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightParenthesis_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTPARENTHESIS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Asterisk_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.ASTERISK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Plus_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PLUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Comma_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.COMMA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Minus_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.MINUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Period_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PERIOD_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class ForwardSlash_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FORWARDSLASH_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary0_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY0_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary1_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY1_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary2_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY2_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary3_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY3_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary4_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY4_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary5_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY5_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary6_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY6_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary7_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY7_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary8_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY8_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Primary9_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARY9_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Colon_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.COLON_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class SemiColon_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SEMICOLON_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LessThan_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LESSTHAN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Equals_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.EQUALS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class GreaterThan_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.GREATERTHAN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class QuestionMark_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.QUESTIONMARK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class At_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.AT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftBracket_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTBRACKET_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class BackSlash_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.BACKSLASH_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightBracket_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTBRACKET_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Caret_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.CARET_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Underscore_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.UNDERSCORE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Grave_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.GRAVE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryA_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryB_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYB_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryC_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYC_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryD_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYD_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryE_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryF_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYF_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryG_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYG_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryH_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYH_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryI_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYI_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryJ_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYJ_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryK_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryL_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryM_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYM_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryN_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryO_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYO_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryP_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryQ_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYQ_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class primaryR_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYR_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryS_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryT_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryU_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYU_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryV_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYV_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryW_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYW_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryX_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYX_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryY_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYY_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PrimaryZ_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRIMARYZ_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Delete_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.DELETE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad0_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD0_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad1_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD1_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad2_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD2_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad3_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD3_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad4_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD4_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad5_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD5_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad6_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD6_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad7_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD7_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad8_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD8_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Numpad9_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPAD9_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadPeriod_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADPERIOD_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadDivide_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADDIVIDE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadMultiply_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADMULTIPLY_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadMinus_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADMINUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadPlus_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADPLUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadEnter_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADENTER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumpadEquals_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMPADEQUALS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Up_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.UP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Down_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.DOWN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Right_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Left_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Insert_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.INSERT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Home_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.HOME_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class End_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.END_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PageUp_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PAGEUP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class PageDown_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PAGEDOWN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function1_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION1_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function2_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION2_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function3_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION3_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function4_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION4_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function5_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION5_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function6_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION6_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function7_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION7_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function8_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION8_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function9_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION9_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function10_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION10_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function11_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION11_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function12_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION12_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function13_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION13_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function14_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION14_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Function15_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.FUNCTION15_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class NumLock_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.NUMLOCK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class CapsLock_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.CAPSLOCK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class ScrollLock_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SCROLLLOCK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightShift_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTSHIFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftShift_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTSHIFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Shift_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SHIFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightControl_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTCONTROL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftControl_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTCONTROL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Control_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.CONTROL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightAlt_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTALT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftAlt_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTALT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Alt_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.ALT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightMeta_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTMETA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftMeta_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTMETA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Meta_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.META_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftSuper_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTSUPER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightSuper_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTSUPER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Super_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SUPER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Mode_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.MODE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Help_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.HELP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Print_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.PRINT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class SystemRequest_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.SYSTEMREQUEST_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Break_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.BREAK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Menu_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.MENU_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Power_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.POWER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Euro_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.EURO_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class AndroidBack_KEY:
    def __init__(self):
        initialize(self, unique_instance=Constants.ANDROIDBACK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Y_BUTTON: # 3
    def __init__(self):
        initialize(self, unique_instance=Constants.Y_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class B_BUTTON: # 2
    def __init__(self):
        initialize(self, unique_instance=Constants.B_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class A_BUTTON: # 1
    def __init__(self):
        initialize(self, unique_instance=Constants.A_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class X_BUTTON: # 0
    def __init__(self):
        initialize(self, unique_instance=Constants.X_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Home_BUTTON: # 12
    def __init__(self):
        initialize(self, unique_instance=Constants.HOME_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightJoystick_BUTTON: # 11
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTJOYSTICK_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftJoystick_BUTTON: # 10
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTJOYSTICK_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Options_BUTTON: # 9
    def __init__(self):
        initialize(self, unique_instance=Constants.OPTIONS_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Share_BUTTON: # 8
    def __init__(self):
        initialize(self, unique_instance=Constants.SHARE_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Right_TRIGGER: # 7
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHT_TRIGGER_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Left_TRIGGER: # 6
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFT_TRIGGER_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Right_BUMPER: # 5
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHT_BUMPER_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Left_BUMPER: # 4
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFT_BUMPER_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Center_BUTTON: # 13
    def __init__(self):
        initialize(self, unique_instance=Constants.CENTER_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftJoystick_AXIS:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTJOYSTICK_AXIS_OBJECT, add_to_pmma_module_spine=True)

        self._x_axis = 0
        self._y_axis = 0

    def get_x_axis(self):
        return self._x_axis

    def get_y_axis(self):
        return self._y_axis

    def set_x_axis(self, value):
        self._x_axis = value

    def set_y_axis(self, value):
        self._y_axis = value

class RightJoystick_AXIS:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTJOYSTICK_AXIS_OBJECT, add_to_pmma_module_spine=True)

        self._x_axis = 0
        self._y_axis = 0

    def get_x_axis(self):
        return self._x_axis

    def get_y_axis(self):
        return self._y_axis

    def set_x_axis(self, value):
        self._x_axis = value

    def set_y_axis(self, value):
        self._y_axis = value

class UpHat_BUTTON:
    def __init__(self):
        initialize(self, unique_instance=Constants.UPHAT_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class DownHat_BUTTON:
    def __init__(self):
        initialize(self, unique_instance=Constants.DOWNHAT_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftHat_Button:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTHAT_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightHat_BUTTON:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTHAT_BUTTON_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class LeftButton_MOUSE:
    def __init__(self):
        initialize(self, unique_instance=Constants.LEFTBUTTON_MOUSE_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class MiddleButton_MOUSE:
    def __init__(self):
        initialize(self, unique_instance=Constants.MIDDLEBUTTON_MOUSE_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class RightButton_MOUSE:
    def __init__(self):
        initialize(self, unique_instance=Constants.RIGHTBUTTON_MOUSE_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        self._double_tapped = value

    def get_double_tapped(self):
        return self._double_tapped

    def get_last_tap_time(self):
        return self._last_tap_time

    def set_last_tap_time(self, value):
        self._last_tap_time = value

    def get_pressed(self):
        return self._currently_pressed

    def set_pressed(self, value):
        self._currently_pressed = value

    def get_double_tap_timing(self):
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        self._double_tap_timing = value

class Mouse_SCROLL:
    def __init__(self):
        initialize(self, unique_instance=Constants.MOUSE_SCROLL_OBJECT, add_to_pmma_module_spine=True)

        self._scroll_value = 0
        self._scroll_displacement = 0

    def get_scroll_displacement(self):
        return self._scroll_displacement

    def get_scroll_value(self):
        return self._scroll_value

    def set_scroll_value(self, value):
        self._scroll_value = value

class Mouse_POSITION:
    def __init__(self):
        initialize(self, unique_instance=Constants.MOUSE_POSITION_OBJECT, add_to_pmma_module_spine=True)

        self._x_axis = 0
        self._y_axis = 0
        self._x_axis_displacement = 0
        self._y_axis_displacement = 0

    def get_axis_displacement(self):
        return self._x_axis_displacement, self._y_axis_displacement

    def get_x_axis_displacement(self):
        return self._x_axis_displacement

    def get_y_axis_displacement(self):
        return self._y_axis_displacement

    def get_x_axis(self):
        return self._x_axis

    def get_y_axis(self):
        return self._y_axis

    def set_x_axis(self, value):
        self._x_axis = value

    def set_y_axis(self, value):
        self._y_axis = value

class Active_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.ACTIVE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppTerminating_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.APPTERMINATING_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppLowMemory_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.APPLOWMEMORY_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppWillEnterBackground_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppDidEnterBackground_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppWillEnterForeground_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppDidEnterForeground_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AudioDeviceAdded_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.AUDIODEVICEADDED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AudioDeviceRemoved_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.AUDIODEVICEREMOVED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class ClipBoardUpdate_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.CLIPBOARDUPDATE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DollarGesture_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.DOLLARGESTURE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DollarCord_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.DOLLARCORD_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropFile_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.DROPFILE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropText_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.DROPTEXT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropBegin_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.DROPBEGIN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropComplete_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.DROPCOMPLETE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class FingerMotion_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.FINGERMOTION_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class FingerDown_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.FINGERDOWN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class FingerUp_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.FINGERUP_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class KeyDown_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.KEYDOWN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class KeyUp_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.KEYUP_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class KeyMapChanged_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.KEYMAPCHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class LocaleChanged_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.LOCALECHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseMotion_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MOUSEMOTION_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseButtonDown_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MOUSEBUTTONDOWN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseButtonUp_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MOUSEBUTTONUP_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseWheel_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MOUSEWHEEL_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MultiGesture_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MULTIGESTURE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class NoEvent_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.NOEVENT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class Quit_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.QUIT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class RenderTargetsReset_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.RENDERTARGETSRESET_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class RenderDeviceReset_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.RENDERDEVICERESET_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class SysWMEvent_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.SYSWMEVENT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class TextInput_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.TEXTINPUT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class TextEditing_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.TEXTEDITING_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class VideoResize_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.VIDEORESIZE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class VideoExpose_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.VIDEOEXPOSE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MidiIn_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MIDIIN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MidiOut_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.MIDIOUT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowShown_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWSHOWN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowHidden_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWHIDDEN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowExposed_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWEXPOSED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowMoved_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWMOVED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowResized_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWRESIZED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowSizeChanged_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWSIZECHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowMinimized_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWMINIMIZED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowMaximized_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWMAXIMIZED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowRestored_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWRESTORED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowEnter_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWENTER_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowLeave_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWLEAVE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowFocusGained_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWFOCUSGAINED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowFocusLost_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWFOCUSLOST_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowClose_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWCLOSE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowTakeFocus_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWTAKEFOCUS_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowHitTest_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWHITTEST_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowICCPROFChanged_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowDisplayChanged_EVENT:
    def __init__(self):
        initialize(self, unique_instance=Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value