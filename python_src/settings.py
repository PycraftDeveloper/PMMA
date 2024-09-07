from pmma.python_src.constants import Constants
from pmma.python_src.utility.registry_utils import Registry as _Registry

def set_development_mode(value):
    _Registry.development_mode = value
    _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("Welcome to developer mode. Setting this \
will allow for more developer focused information to be displayed to you - handy \
for building and debugging applications using PMMA!")

def get_development_mode():
    return _Registry.development_mode

def set_allow_compilation_of_math_functions(value):
    _Registry.compile_math_functions = value

def get_allow_compilation_of_math_functions():
    return _Registry.compile_math_functions

def get_application_running():
    return _Registry.running

def set_application_running(value):
    _Registry.running = value

def set_allow_anti_aliasing(value):
    _Registry.manually_set_do_anti_aliasing = value
    original = get_allow_anti_aliasing()
    if original != value:
        _Registry.do_anti_aliasing = value
        _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("You have changed if anti-aliasing will be used in \
PMMA - this wont effect your own textures for compatibility reasons. However, excessive changes \
to this value can cause uncomfortable flickering and other rendering issues as content already \
on the display is cleared in this process. Excessive changes to this value can also negatively \
effect performance too, so this setting is best used sparingly (for example as a toggle with an \
application's setting menu).")
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].display_resize()

def get_allow_anti_aliasing():
    return _Registry.do_anti_aliasing

def set_anti_aliasing_level(value):
    _Registry.manually_set_anti_aliasing_level = value
    original = get_anti_aliasing_level()
    if original != value:
        _Registry.anti_aliasing_level = value
        if _Registry.do_anti_aliasing:
            _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("You have changed the quality of the anti-aliasing that will be used in \
PMMA - this wont effect your own textures for compatibility reasons. However, excessive changes \
to this value can cause uncomfortable flickering and other rendering issues as content already \
on the display is cleared in this process. Excessive changes to this value can also negatively \
effect performance too, so this setting is best used sparingly (for example as a toggle with an \
application's setting menu).")
            if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine:
                _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].display_resize()

def get_anti_aliasing_level():
    return _Registry.anti_aliasing_level

def get_language():
    return _Registry.language

def set_language(value):
    _Registry.language = value

def get_display_mode():
    if _Registry.display_mode_set:
        return _Registry.display_mode

def set_display_mode(mode):
    if _Registry.display_mode_set:
        _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("You \
have attempted to set a display mode after it has already been set. If this is a surprise \
to you, its probably because you are already using PMMA functions that use a display mode \
so its been set for you. If you want to use a specific display mode, consider calling this \
IMMEDIATELY before 'pmma.init()' to avoid this behavior. If this isn't a surprise to you, \
then know that you can only set the display mode once whilst the application is running.")
    else:
        _Registry.display_mode_set = True
        _Registry.display_mode = mode