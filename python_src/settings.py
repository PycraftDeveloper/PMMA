from pmma.python_src.constants import Constants

from pmma.python_src.utility.settings_utils import set_development_mode as _set_development_mode
from pmma.python_src.utility.settings_utils import get_development_mode as _get_development_mode
from pmma.python_src.utility.settings_utils import set_allow_compilation_of_math_functions as _set_allow_compilation_of_math_functions
from pmma.python_src.utility.settings_utils import get_allow_compilation_of_math_functions as _get_allow_compilation_of_math_functions
from pmma.python_src.utility.settings_utils import get_application_running as _get_application_running
from pmma.python_src.utility.settings_utils import set_application_running as _set_application_running
from pmma.python_src.utility.settings_utils import set_allow_anti_aliasing as _set_allow_anti_aliasing
from pmma.python_src.utility.settings_utils import get_allow_anti_aliasing as _get_allow_anti_aliasing
from pmma.python_src.utility.settings_utils import set_anti_aliasing_level as _set_anti_aliasing_level
from pmma.python_src.utility.settings_utils import get_anti_aliasing_level as _get_anti_aliasing_level
from pmma.python_src.utility.settings_utils import get_language as _get_language
from pmma.python_src.utility.settings_utils import set_language as _set_language
from pmma.python_src.utility.settings_utils import get_display_mode as _get_display_mode
from pmma.python_src.utility.settings_utils import set_display_mode as _set_display_mode
from pmma.python_src.utility.settings_utils import set_shape_quality as _set_shape_quality
from pmma.python_src.utility.settings_utils import get_shape_quality as _get_shape_quality
from pmma.python_src.utility.settings_utils import set_in_game_loop as _set_in_game_loop
from pmma.python_src.utility.settings_utils import get_in_game_loop as _get_in_game_loop
from pmma.python_src.utility.settings_utils import set_profile_result_path as _set_profile_result_path
from pmma.python_src.utility.settings_utils import get_profile_result_path as _get_profile_result_path

def set_profile_result_path(value):
    _set_profile_result_path(value)

def get_profile_result_path():
    return _get_profile_result_path()

def set_development_mode(value):
    _set_development_mode(value, internal=False)

def get_development_mode():
    return _get_development_mode()

def set_allow_compilation_of_math_functions(value):
    _set_allow_compilation_of_math_functions(value)

def get_allow_compilation_of_math_functions():
    return _get_allow_compilation_of_math_functions()

def get_application_running():
    return _get_application_running()

def set_application_running(value):
    _set_application_running(value)

def set_allow_anti_aliasing(value):
    _set_allow_anti_aliasing(value, internal=False)

def get_allow_anti_aliasing():
    return _get_allow_anti_aliasing()

def set_anti_aliasing_level(value):
    _set_anti_aliasing_level(value, internal=False)

def get_anti_aliasing_level():
    return _get_anti_aliasing_level()

def get_language():
    return _get_language()

def set_language(value):
    _set_language(value)

def get_display_mode():
    return _get_display_mode()

def set_display_mode(mode):
    _set_display_mode(mode, internal=False)

def set_shape_quality(value, format=Constants.PERCENTAGE):
    _set_shape_quality(value, format=format)

def get_shape_quality(format=Constants.PERCENTAGE):
    return _get_shape_quality(format=format)

def set_in_game_loop(value):
    _set_in_game_loop(value)

def get_in_game_loop():
    return _get_in_game_loop()