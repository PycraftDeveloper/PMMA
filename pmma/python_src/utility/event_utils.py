from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Backspace_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.BACKSPACE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._time__module = _ModuleManager.import_module("time")

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Tab_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.TAB_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Clear_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.CLEAR_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Return_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RETURN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Pause_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PAUSE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Escape_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.ESCAPE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Space_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SPACE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class ExclamationMark_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.EXCLAMATIONMARK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class DoubleQuote_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DOUBLEQUOTE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Hashtag_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.HASHTAG_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Dollar_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DOLLAR_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Ampersand_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.AMPERSAND_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class SingleQuote_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SINGLEQUOTE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftParenthesis_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTPARENTHESIS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightParenthesis_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Asterisk_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.ASTERISK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Plus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PLUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Comma_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.COMMA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Minus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MINUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Period_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PERIOD_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class ForwardSlash_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FORWARDSLASH_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary0_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY0_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary1_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY1_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary2_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY2_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary3_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY3_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary4_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY4_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary5_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY5_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary6_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY6_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary7_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY7_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary8_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY8_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Primary9_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARY9_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Colon_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.COLON_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class SemiColon_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SEMICOLON_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LessThan_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LESSTHAN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Equals_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.EQUALS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class GreaterThan_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.GREATERTHAN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class QuestionMark_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.QUESTIONMARK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class At_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.AT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftBracket_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTBRACKET_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class BackSlash_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.BACKSLASH_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightBracket_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTBRACKET_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Caret_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.CARET_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Underscore_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.UNDERSCORE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Grave_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.GRAVE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryA_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryB_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYB_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryC_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYC_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryD_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYD_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryE_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryF_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYF_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryG_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYG_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryH_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYH_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryI_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYI_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryJ_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYJ_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryK_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryL_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryM_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYM_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryN_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryO_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYO_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryP_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryQ_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYQ_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryR_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYR_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryS_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryT_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryU_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYU_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryV_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYV_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryW_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYW_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryX_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYX_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryY_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYY_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PrimaryZ_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRIMARYZ_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Delete_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DELETE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad0_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD0_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad1_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD1_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad2_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD2_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad3_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD3_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad4_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD4_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad5_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD5_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad6_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD6_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad7_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD7_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad8_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD8_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Numpad9_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPAD9_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadPeriod_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADPERIOD_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadDivide_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADDIVIDE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadMultiply_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADMULTIPLY_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadMinus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADMINUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadPlus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADPLUS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadEnter_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADENTER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumpadEquals_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMPADEQUALS_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Up_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.UP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Down_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DOWN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Right_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Left_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Insert_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.INSERT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Home_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.HOME_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class End_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.END_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PageUp_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PAGEUP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class PageDown_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PAGEDOWN_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function1_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION1_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function2_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION2_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function3_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION3_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function4_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION4_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function5_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION5_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function6_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION6_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function7_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION7_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function8_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION8_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function9_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION9_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function10_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION10_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function11_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION11_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function12_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION12_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function13_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION13_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function14_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION14_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Function15_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FUNCTION15_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class NumLock_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.NUMLOCK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class CapsLock_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.CAPSLOCK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class ScrollLock_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SCROLLLOCK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightShift_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTSHIFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftShift_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTSHIFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Shift_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SHIFT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightControl_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTCONTROL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftControl_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTCONTROL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Control_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.CONTROL_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightAlt_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTALT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftAlt_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTALT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Alt_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.ALT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightMeta_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTMETA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftMeta_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTMETA_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Meta_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.META_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftSuper_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTSUPER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightSuper_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTSUPER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Super_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SUPER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Mode_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MODE_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Help_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.HELP_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Print_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.PRINT_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class SystemRequest_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SYSTEMREQUEST_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Break_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.BREAK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Menu_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MENU_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Power_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.POWER_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Euro_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.EURO_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class AndroidBack_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.ANDROIDBACK_KEY_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Y_BUTTON: # 3
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class B_BUTTON: # 2
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class A_BUTTON: # 1
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class X_BUTTON: # 0
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Home_BUTTON: # 12
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightJoystick_BUTTON: # 11
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftJoystick_BUTTON: # 10
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Options_BUTTON: # 9
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Track_BALL:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self.id = None
        self.x_motion = 0
        self.y_motion = 0

    def get_id(self):
        """
        🟩 **R** -
        """
        return self.id

    def set_id(self, value):
        """
        🟩 **R** -
        """
        self.id = value

    def get_x_motion(self):
        """
        🟩 **R** -
        """
        return self.x_motion

    def set_x_motion(self, value):
        """
        🟩 **R** -
        """
        self.x_motion = value

    def get_y_motion(self):
        """
        🟩 **R** -
        """
        return self.y_motion

    def set_y_motion(self, value):
        """
        🟩 **R** -
        """
        self.y_motion = value

class Share_BUTTON: # 8
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Right_TRIGGER:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self.value = 0

    def get_value(self):
        """
        🟩 **R** -
        """
        return self.value

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self.value = value

class Left_TRIGGER:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self.value = 0

    def get_value(self):
        """
        🟩 **R** -
        """
        return self.value

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self.value = value

class Right_BUMPER: # 5
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Left_BUMPER: # 4
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Center_BUTTON: # 15
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftJoystick_AXIS:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._x_axis = 0
        self._y_axis = 0

    def get_x_axis(self):
        """
        🟩 **R** -
        """
        return self._x_axis

    def get_y_axis(self):
        """
        🟩 **R** -
        """
        return self._y_axis

    def set_x_axis(self, value):
        """
        🟩 **R** -
        """
        self._x_axis = value

    def set_y_axis(self, value):
        """
        🟩 **R** -
        """
        self._y_axis = value

class RightJoystick_AXIS:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._x_axis = 0
        self._y_axis = 0

    def get_x_axis(self):
        """
        🟩 **R** -
        """
        return self._x_axis

    def get_y_axis(self):
        """
        🟩 **R** -
        """
        return self._y_axis

    def set_x_axis(self, value):
        """
        🟩 **R** -
        """
        self._x_axis = value

    def set_y_axis(self, value):
        """
        🟩 **R** -
        """
        self._y_axis = value

class UpHat_BUTTON:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class DownHat_BUTTON:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftHat_BUTTON:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightHat_BUTTON:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class LeftButton_MOUSE:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LEFTBUTTON_MOUSE_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class MiddleButton_MOUSE:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class RightButton_MOUSE:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RIGHTBUTTON_MOUSE_OBJECT, add_to_pmma_module_spine=True)

        self._currently_pressed = False
        self._double_tap_timing = 0.25
        self._last_tap_time = 0
        self._double_tapped = False

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._double_tapped = value

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._double_tapped

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._last_tap_time

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        if value-self.get_last_tap_time() <= self.get_double_tap_timing():
            self.set_double_tapped(True)
        else:
            self.set_double_tapped(False)

        self._last_tap_time = value

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._currently_pressed

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        if value:
            self.set_last_tap_time(self._time__module.perf_counter())
        else:
            self.set_double_tapped(False)

        self._currently_pressed = value

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._double_tap_timing

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._double_tap_timing = value

class Mouse_SCROLL:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MOUSE_SCROLL_OBJECT, add_to_pmma_module_spine=True)

        self._x_value = 0
        self._x_displacement = 0
        self._y_value = 0
        self._y_displacement = 0

    def get_x_displacement(self):
        """
        🟩 **R** -
        """
        return self._x_displacement

    def set_x_displacement(self, value):
        """
        🟩 **R** -
        """
        self._x_displacement = value

    def get_x_value(self):
        """
        🟩 **R** -
        """
        return self._x_value

    def set_x_value(self, value):
        """
        🟩 **R** -
        """
        self._x_value = value

    def get_y_displacement(self):
        """
        🟩 **R** -
        """
        return self._y_displacement

    def set_y_displacement(self, value):
        """
        🟩 **R** -
        """
        self._y_displacement = value

    def get_y_value(self):
        """
        🟩 **R** -
        """
        return self._y_value

    def set_y_value(self, value):
        """
        🟩 **R** -
        """
        self._y_value = value

class Mouse_POSITION:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MOUSE_POSITION_OBJECT, add_to_pmma_module_spine=True)

        self._x_axis = 0
        self._y_axis = 0
        self._x_axis_displacement = 0
        self._y_axis_displacement = 0

    def get_axis_displacement(self):
        """
        🟩 **R** -
        """
        return self._x_axis_displacement, self._y_axis_displacement

    def get_x_axis_displacement(self):
        """
        🟩 **R** -
        """
        return self._x_axis_displacement

    def get_y_axis_displacement(self):
        """
        🟩 **R** -
        """
        return self._y_axis_displacement

    def get_x_axis(self):
        """
        🟩 **R** -
        """
        return self._x_axis

    def get_y_axis(self):
        """
        🟩 **R** -
        """
        return self._y_axis

    def set_x_axis(self, value):
        """
        🟩 **R** -
        """
        self._x_axis = value

    def set_y_axis(self, value):
        """
        🟩 **R** -
        """
        self._y_axis = value

    def set_x_axis_displacement(self, value):
        """
        🟩 **R** -
        """
        self._x_axis_displacement = value

    def set_y_axis_displacement(self, value):
        """
        🟩 **R** -
        """
        self._y_axis_displacement = value

class AppTerminating_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.APPTERMINATING_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AppLowMemory_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.APPLOWMEMORY_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AppWillEnterBackground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AppDidEnterBackground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AppWillEnterForeground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AppDidEnterForeground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AudioDeviceAdded_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class AudioDeviceRemoved_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class ClipBoardUpdate_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class DropFile_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DROPFILE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._file = None

    def set_file(self, file):
        """
        🟩 **R** -
        """
        self._file = file

    def get_file(self):
        """
        🟩 **R** -
        """
        return self._file

class DropText_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DROPTEXT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._text = None

    def set_text(self, text):
        """
        🟩 **R** -
        """
        self._text = text

    def get_text(self):
        """
        🟩 **R** -
        """
        return self._text

class DropBegin_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DROPBEGIN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class DropComplete_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.DROPCOMPLETE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class FingerMotion_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FINGERMOTION_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class FingerDown_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FINGERDOWN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class FingerUp_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.FINGERUP_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class KeyMapChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.KEYMAPCHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class LocaleChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LOCALECHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class MultiGesture_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.MULTIGESTURE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._gesture_center_x = None
        self._gesture_center_y = None
        self._pinched_value = 0
        self._rotated_value = 0
        self._number_of_fingers = 0

    def get_gesture_center_x(self):
        """
        🟩 **R** -
        """
        return self._gesture_center_x

    def get_gesture_center_y(self):
        """
        🟩 **R** -
        """
        return self._gesture_center_y

    def get_pinched_value(self):
        """
        🟩 **R** -
        """
        return self._pinched_value

    def get_rotated_value(self):
        """
        🟩 **R** -
        """
        return self._rotated_value

    def get_number_of_fingers(self):
        """
        🟩 **R** -
        """
        return self._number_of_fingers

    def set_gesture_center_x(self, value):
        """
        🟩 **R** -
        """
        self._gesture_center_x = value

    def set_gesture_center_y(self, value):
        """
        🟩 **R** -
        """
        self._gesture_center_y = value

    def set_pinched_value(self, value):
        """
        🟩 **R** -
        """
        self._pinched_value = value

    def set_rotated_value(self, value):
        """
        🟩 **R** -
        """
        self._rotated_value = value

    def set_number_of_fingers(self, value):
        """
        🟩 **R** -
        """
        self._number_of_fingers = value

class Quit_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.QUIT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class RenderTargetsReset_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class RenderDeviceReset_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RENDERDEVICERESET_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class SysWMEvent_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SYSWMEVENT_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowShown_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWSHOWN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowHidden_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWHIDDEN_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowExposed_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWEXPOSED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowMoved_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWMOVED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowResized_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWRESIZED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowMinimized_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowMaximized_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowRestored_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWRESTORED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowEnter_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWENTER_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowLeave_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWLEAVE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowFocusGained_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowFocusLost_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowClose_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWCLOSE_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowTakeFocus_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowHitTest_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWHITTEST_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowICCPROFChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class WindowDisplayChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class JoyDeviceAdded_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.JOYDEVICEADDED_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value

class JoyDeviceRemoved_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.JOYDEVICEREMOVED_OBJECT, add_to_pmma_module_spine=True)

        self._value = None

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._value = value

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._value