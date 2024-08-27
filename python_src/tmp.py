import gc as _gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Backspace_KEY:
    def __init__(self):
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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

class LeftHat_BUTTON:
    def __init__(self):
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

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
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppTerminating_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppLowMemory_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppWillEnterBackground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppDidEnterBackground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppWillEnterForeground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AppDidEnterForeground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AudioDeviceAdded_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class AudioDeviceRemoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class ClipBoardUpdate_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DollarGesture_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DollarCord_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropFile_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropText_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropBegin_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class DropComplete_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class FingerMotion_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class FingerDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class FingerUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class KeyDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class KeyUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class KeyMapChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class LocaleChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseMotion_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseButtonDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseButtonUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MouseWheel_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MultiGesture_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class NoEvent_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class Quit_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class RenderTargetsReset_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class RenderDeviceReset_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class SysWMEvent_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class TextInput_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class TextEditing_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class VideoResize_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class VideoExpose_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MidiIn_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MidiOut_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowShown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowHidden_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowExposed_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowMoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowResized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowSizeChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowMinimized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowMaximized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowRestored_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowEnter_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowLeave_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowFocusGained_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowFocusLost_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowClose_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowTakeFocus_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowHitTest_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowICCPROFChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class WindowDisplayChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value