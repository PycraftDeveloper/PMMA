from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

def set_development_mode(value, internal=True):
    """
    🟩 **R** -
    """
    _Registry.development_mode = value
    if internal is False:
        _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_development("Welcome to developer mode. Setting this \
will allow for more developer focused information to be displayed to you - handy \
for building and debugging applications using PMMA!")

def get_development_mode():
    """
    🟩 **R** -
    """
    return _Registry.development_mode

def set_allow_compilation_of_math_functions(value):
    """
    🟩 **R** -
    """
    _Registry.compile_math_functions = value

def get_allow_compilation_of_math_functions():
    """
    🟩 **R** -
    """
    return _Registry.compile_math_functions

def get_application_running():
    """
    🟩 **R** -
    """
    return _Registry.running

def set_application_running(value):
    """
    🟩 **R** -
    """
    _Registry.running = value

def set_allow_anti_aliasing(value, internal=True):
    """
    🟩 **R** -
    """
    _Registry.manually_set_do_anti_aliasing = value
    original = get_allow_anti_aliasing()
    if original != value:
        _Registry.do_anti_aliasing = value
        if internal is False:
            _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_development("You have changed if anti-aliasing will be used in \
PMMA - this wont effect your own textures for compatibility reasons. However, excessive changes \
to this value can cause uncomfortable flickering and other rendering issues as content already \
on the display is cleared in this process. Excessive changes to this value can also negatively \
effect performance too, so this setting is best used sparingly (for example as a toggle with an \
application's setting menu).")
        if _Registry.display_initialized:
            _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].on_window_size_changed()

def get_allow_anti_aliasing():
    """
    🟩 **R** -
    """
    return _Registry.do_anti_aliasing

def set_anti_aliasing_level(value, internal=True):
    """
    🟩 **R** -
    """
    _Registry.manually_set_anti_aliasing_level = value
    original = get_anti_aliasing_level()
    if original != value:
        _Registry.anti_aliasing_level = value
        if _Registry.do_anti_aliasing:
            if internal is False:
                _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_development("You have changed the quality of the anti-aliasing that will be used in \
PMMA - this wont effect your own textures for compatibility reasons. However, excessive changes \
to this value can cause uncomfortable flickering and other rendering issues as content already \
on the display is cleared in this process. Excessive changes to this value can also negatively \
effect performance too, so this setting is best used sparingly (for example as a toggle with an \
application's setting menu).")
            if _Registry.display_initialized:
                _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].on_window_size_changed()

def get_anti_aliasing_level():
    """
    🟩 **R** -
    """
    return _Registry.anti_aliasing_level

def get_language():
    """
    🟩 **R** -
    """
    return _Registry.language

def set_language(value):
    """
    🟩 **R** -
    """
    _Registry.language = value

def set_shape_quality(value, format=_Constants.PERCENTAGE):
    """
    🟩 **R** -
    """
    from pmma.python_src.number_converter import ProportionConverter as _ProportionConverter
    proportion = _ProportionConverter()
    proportion.set_value(value, format)
    _Registry.shape_quality = proportion.get_value(format=_Constants.DECIMAL)

def get_shape_quality(format=_Constants.PERCENTAGE):
    """
    🟩 **R** -
    """
    from pmma.python_src.number_converter import ProportionConverter as _ProportionConverter
    proportion = _ProportionConverter()
    proportion.set_value(_Registry.shape_quality, _Constants.DECIMAL)
    return proportion.get_value(format=format)

def set_in_game_loop(value):
    """
    🟩 **R** -
    """
    _Registry.in_game_loop = value

def get_in_game_loop():
    """
    🟩 **R** -
    """
    return _Registry.in_game_loop

def set_profile_result_path(path):
    """
    🟩 **R** -
    """
    _Registry.profile_result_path = path

def get_profile_result_path():
    """
    🟩 **R** -
    """
    return _Registry.profile_result_path