from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class Logger:
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

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        if not _InternalConstants.LOGGING_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LOGGING_INTERMEDIARY_OBJECT)
            self._logging_utils__module.LoggerIntermediary()

        self._logger_intermediary = _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT]

    def set_pmma_log_lifetime(self, value):
        """
        🟩 **R** -
        """
        _Registry.internal_log_duration = value
        self._logger_intermediary.log_development("Note that updating this will automatically \
remove all logs older than {} days old.", variables=[value])
        if value > 7:
            self._logger_intermediary.log_development("You have set the log lifetime to more \
than 1 week, please note that in most situations its not necessary to do this, and may cause \
excessive storage usage.")
        self._logger_intermediary.clear_internal_logs()

    def set_application_log_lifetime(self, value):
        """
        🟩 **R** -
        """
        _Registry.external_log_duration = value
        self._logger_intermediary.log_development("Note that updating this will automatically \
remove all logs older than {} days old.", variables=[value])
        if value > 7:
            self._logger_intermediary.log_development("You have set the log lifetime to more \
than 1 week, please note that in most situations its not necessary to do this, and may cause \
excessive storage usage.")
        self._logger_intermediary.clear_external_logs()

    def set_log_development_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_development_messages_to_terminal(value)

    def set_log_information_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_information_messages_to_terminal(value)

    def set_log_warning_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_warning_messages_to_terminal(value)

    def set_log_error_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_error_messages_to_terminal(value)

    def set_log_development_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_development_messages_to_file(value)

    def set_log_information_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_information_messages_to_file(value)

    def set_log_warning_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_warning_messages_to_file(value)

    def set_log_error_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_external_log_error_messages_to_file(value)

    def get_log_development_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_development_messages_to_terminal()

    def get_log_information_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_information_messages_to_terminal()

    def get_log_warning_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_warning_messages_to_terminal()

    def get_log_error_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_error_messages_to_terminal()

    def get_log_development_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_development_messages_to_file()

    def get_log_information_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_information_messages_to_file()

    def get_log_warning_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_warning_messages_to_file()

    def get_log_error_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_external_log_error_messages_to_file()

    def set_log_levels(
            self,
            log_development_messages_to_terminal=None,
            log_information_messages_to_terminal=True,
            log_warning_messages_to_terminal=False,
            log_error_messages_to_terminal=True,
            log_development_messages_to_file=None,
            log_information_messages_to_file=True,
            log_warning_messages_to_file=True,
            log_error_messages_to_file=True):
        """
        🟩 **R** -
        """

        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_external_log_development_messages_to_terminal(_Registry.development_mode)
        else:
            self._logger_intermediary.set_external_log_development_messages_to_terminal(log_development_messages_to_terminal)
        self._logger_intermediary.set_external_log_information_messages_to_terminal(log_information_messages_to_terminal)
        self._logger_intermediary.set_external_log_warning_messages_to_terminal(log_warning_messages_to_terminal)
        self._logger_intermediary.set_external_log_error_messages_to_terminal(log_error_messages_to_terminal)

        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_external_log_development_messages_to_file(_Registry.development_mode)
        else:
            self._logger_intermediary.set_external_log_development_messages_to_file(log_development_messages_to_file)
        self._logger_intermediary.set_external_log_information_messages_to_file(log_information_messages_to_file)
        self._logger_intermediary.set_external_log_warning_messages_to_file(log_warning_messages_to_file)
        self._logger_intermediary.set_external_log_error_messages_to_file(log_error_messages_to_file)

    def log_development(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.DEVELOPMENT, False, variables=variables)

    def log_information(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.INFORMATION, False, variables=variables)

    def log_warning(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.WARNING, False, variables=variables)

    def log_error(self, message,  variables=[], do_traceback=True, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.ERROR, False, variables=variables)