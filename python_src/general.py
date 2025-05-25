from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class General:
    def __init__(self):
        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

    def set_clean_profiling(self, can_clean_profile):
        """
        🟩 **R** -
        """
        self._internal_general_utils.set_clean_profiling(can_clean_profile)

    def get_clean_profiling(self):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_clean_profiling()

    def clean_up(self):
        """
        🟩 **R** -
        """
        print("PMMA is about to perform a clean up operation that is \
    designed to make its un-installation easier. This is best run \
    before pmma.init().")
        _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_development("PMMA is about to perform a clean up operation that is \
    designed to make its un-installation easier. This is best run \
    before pmma.init().")
        self._internal_general_utils.clean_up()

    def get_application_startup_duration(self):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_application_startup_duration()

    def get_application_run_time(self):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_application_run_time()

    def get_execution_time(self, function, *args, **kwargs):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_execution_time(function, *args, **kwargs)

    def get_execution_inverse_time(self, function, *args, **kwargs):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_execution_inverse_time(function, *args, **kwargs)

    def targeted_profile_start(self):
        """
        🟩 **R** -
        """
        self._internal_general_utils.targeted_profile_start()

    def targeted_profile_end(self):
        """
        🟩 **R** -
        """
        self._internal_general_utils.targeted_profile_end()

    def profile_this(self, func):
        """
        🟩 **R** -
        """
        def wrapper(*args, **kwargs):
            """
            🟩 **R** -
            """
            if _Registry.profiler is None:
                _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_development(
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
                _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                    "Just a quick heads up, you are attempting to profile this specific method \
    however you already specified that you want to profile everything, so this has no effect. \
    This behavior can be configured in 'pmma.init()'.")
                return func(*args, **kwargs)
        return wrapper

    def check_if_object_is_class_or_function(self, param):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.check_if_object_is_class_or_function(param)

    def get_theme(self):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_theme()

    def convert_number_to_text(self, value):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.convert_number_to_text(value)

    def quit(self, show_statistics=None, terminate_application=True):
        """
        🟩 **R** -
        """
        self._internal_general_utils.quit(show_statistics=show_statistics, terminate_application=terminate_application)

    def compute(self, allow_anti_aliasing_adjustments_for_low_power_mode=True):
        """
        🟩 **R** -
        """
        self._internal_general_utils.compute(allow_anti_aliasing_adjustments_for_low_power_mode)

    def register_application(self):
        """
        🟩 **R** -
        """
        self._internal_general_utils.register_application()

    def get_operating_system(self):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.get_operating_system()

    def is_battery_saver_enabled(
            self,
            fallback_battery_power_saving_threshold_percentage=30,
            care_if_running_on_battery=True):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.is_battery_saver_enabled(
            fallback_battery_power_saving_threshold_percentage=fallback_battery_power_saving_threshold_percentage,
            care_if_running_on_battery=care_if_running_on_battery)

    def random_real_number(self, negatives=True):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.random_real_number(negatives=negatives)

    def up(self, path):
        """
        🟩 **R** -
        """
        return self._internal_general_utils.up(path)