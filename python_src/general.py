from pmma.python_src.utility.general_utils import up as _up
from pmma.python_src.utility.general_utils import set_display_mode as _set_display_mode
from pmma.python_src.utility.general_utils import random_real_number as _random_real_number
from pmma.python_src.utility.general_utils import is_battery_saver_enabled as _is_battery_saver_enabled
from pmma.python_src.utility.general_utils import get_operating_system as _get_operating_system
from pmma.python_src.utility.general_utils import register_application as _register_application
from pmma.python_src.utility.general_utils import compute as _compute
from pmma.python_src.utility.general_utils import quit as _quit
from pmma.python_src.utility.general_utils import convert_number_to_text as _convert_number_to_text
from pmma.python_src.utility.general_utils import get_language as _get_language
from pmma.python_src.utility.general_utils import get_theme as _get_theme
from pmma.python_src.utility.general_utils import check_if_object_is_class_or_function as _check_if_object_is_class_or_function

def check_if_object_is_class_or_function(param):
    return _check_if_object_is_class_or_function(param)

def get_theme():
    return _get_theme()

def get_language():
    return _get_language()

def convert_number_to_text(value):
    return _convert_number_to_text(value)

def quit(show_statistics=None, terminate_application=True):
    _quit(show_statistics=show_statistics, terminate_application=terminate_application)

def compute():
    _compute()

def register_application():
    _register_application()

def get_operating_system():
    return _get_operating_system()

def is_battery_saver_enabled(fallback_battery_power_saving_threshold_percentage=30, care_if_running_on_battery=True):
    return _is_battery_saver_enabled(fallback_battery_power_saving_threshold_percentage=fallback_battery_power_saving_threshold_percentage, care_if_running_on_battery=care_if_running_on_battery)

def random_real_number(negatives=True):
    return _random_real_number(negatives=negatives)

def set_display_mode(display_mode):
    _set_display_mode(display_mode)

def up(path):
    return _up(path)