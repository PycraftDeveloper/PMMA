from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.logging_utils import LoggerIntermediary, _LoggingNotInitializedError
from pmma.python_src.utility.general_utils import initialize as _initialize

class Logger:
    def __init__(self):
        _initialize(self)

        if not Constants.LOGGING_INTERMEDIARY_OBJECT in Registry.pmma_module_spine.keys():
            raise _LoggingNotInitializedError()

        self._logger_intermediary: "LoggerIntermediary" = Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT]

    def set_log_development_messages_to_terminal(self, value):
        self._logger_intermediary.set_external_log_development_messages_to_terminal()(value)

    def set_log_information_messages_to_terminal(self, value):
        self._logger_intermediary.set_external_log_information_messages_to_terminal(value)

    def set_log_warning_messages_to_terminal(self, value):
        self._logger_intermediary.set_external_log_warning_messages_to_terminal(value)

    def set_log_error_messages_to_terminal(self, value):
        self._logger_intermediary.set_external_log_error_messages_to_terminal(value)

    def set_log_development_messages_to_file(self, value):
        self._logger_intermediary.set_external_log_development_messages_to_file(value)

    def set_log_information_messages_to_file(self, value):
        self._logger_intermediary.set_external_log_information_messages_to_file(value)

    def set_log_warning_messages_to_file(self, value):
        self._logger_intermediary.set_external_log_warning_messages_to_file(value)

    def set_log_error_messages_to_file(self, value):
        self._logger_intermediary.set_external_log_error_messages_to_file(value)

    def get_log_development_messages_to_terminal(self):
        return self._logger_intermediary.get_external_log_development_messages_to_terminal()

    def get_log_information_messages_to_terminal(self):
        return self._logger_intermediary.get_external_log_information_messages_to_terminal()

    def get_log_warning_messages_to_terminal(self):
        return self._logger_intermediary.get_external_log_warning_messages_to_terminal()

    def get_log_error_messages_to_terminal(self):
        return self._logger_intermediary.get_external_log_error_messages_to_terminal()

    def get_log_development_messages_to_file(self):
        return self._logger_intermediary.get_external_log_development_messages_to_file()

    def get_log_information_messages_to_file(self):
        return self._logger_intermediary.get_external_log_information_messages_to_file()

    def get_log_warning_messages_to_file(self):
        return self._logger_intermediary.get_external_log_warning_messages_to_file()

    def get_log_error_messages_to_file(self):
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

        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_external_log_development_messages_to_terminal(Registry.development_mode)
        else:
            self._logger_intermediary.set_external_log_development_messages_to_terminal(log_development_messages_to_terminal)
        self._logger_intermediary.set_external_log_information_messages_to_terminal(log_information_messages_to_terminal)
        self._logger_intermediary.set_external_log_warning_messages_to_terminal(log_warning_messages_to_terminal)
        self._logger_intermediary.set_external_log_error_messages_to_terminal(log_error_messages_to_terminal)

        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_external_log_development_messages_to_file(Registry.development_mode)
        else:
            self._logger_intermediary.set_external_log_development_messages_to_file(log_development_messages_to_file)
        self._logger_intermediary.set_external_log_information_messages_to_file(log_information_messages_to_file)
        self._logger_intermediary.set_external_log_warning_messages_to_file(log_warning_messages_to_file)
        self._logger_intermediary.set_external_log_error_messages_to_file(log_error_messages_to_file)

    def log_development(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.DEVELOPMENT, False, variables=variables)

    def log_information(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.INFORMATION, False, variables=variables)

    def log_warning(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.WARNING, False, variables=variables)

    def log_error(self, message,  variables=[], do_traceback=True, repeat_for_effect=False):
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.ERROR, False, variables=variables)