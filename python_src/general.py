from pmma.python_src.utility.registry_utils import Registry as _Registry

from pmma.python_src.utility.general_utils import up as _up
from pmma.python_src.utility.general_utils import random_real_number as _random_real_number
from pmma.python_src.utility.general_utils import is_battery_saver_enabled as _is_battery_saver_enabled
from pmma.python_src.utility.general_utils import get_operating_system as _get_operating_system
from pmma.python_src.utility.general_utils import register_application as _register_application
from pmma.python_src.utility.general_utils import compute as _compute
from pmma.python_src.utility.general_utils import quit as _quit
from pmma.python_src.utility.general_utils import convert_number_to_text as _convert_number_to_text
from pmma.python_src.utility.general_utils import get_theme as _get_theme
from pmma.python_src.utility.general_utils import check_if_object_is_class_or_function as _check_if_object_is_class_or_function
from pmma.python_src.utility.general_utils import targeted_profile_end as _targeted_profile_end
from pmma.python_src.utility.general_utils import targeted_profile_start as _targeted_profile_start

def targeted_profile_start():
    _targeted_profile_start()

def targeted_profile_end():
    _targeted_profile_end()

def profile_this(func):
    def wrapper(*args, **kwargs):
        if _Registry.profiler is None:
            _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                "Just a quick heads up, you are attempting to profile this specific method \
however you haven't enabled profiling in 'pmma.init()'. Therefore this has no effect.")
            return func(*args, **kwargs)
        if _Registry.targeted_profile_application:
            _Registry.profiler.enable()

            # Call the original function
            result = func(*args, **kwargs)

            # Stop the profiler
            _Registry.profiler.disable()       # Stop profiling
            return result
        else:
            _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                "Just a quick heads up, you are attempting to profile this specific method \
however you already specified that you want to profile everything, so this has no effect. \
This behavior can be configured in 'pmma.init()'.")
            return func(*args, **kwargs)
    return wrapper

def check_if_object_is_class_or_function(param):
    return _check_if_object_is_class_or_function(param)

def get_theme():
    return _get_theme()

def convert_number_to_text(value):
    return _convert_number_to_text(value)

def quit(show_statistics=None, terminate_application=True):
    _quit(show_statistics=show_statistics, terminate_application=terminate_application)

def compute(allow_anti_aliasing_adjustments_for_low_power_mode=True):
    _compute(allow_anti_aliasing_adjustments_for_low_power_mode)

def register_application():
    _register_application()

def get_operating_system():
    return _get_operating_system()

def is_battery_saver_enabled(fallback_battery_power_saving_threshold_percentage=30, care_if_running_on_battery=True):
    return _is_battery_saver_enabled(fallback_battery_power_saving_threshold_percentage=fallback_battery_power_saving_threshold_percentage, care_if_running_on_battery=care_if_running_on_battery)

def random_real_number(negatives=True):
    return _random_real_number(negatives=negatives)

def up(path):
    return _up(path)