import datetime as _datetime
import traceback as _traceback
import gc as _gc
import threading as _threading

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.error_utils import LoggingNotInitializedError as _LoggingNotInitializedError

class LoggerIntermediary:
    def __init__(self):
        _initialize(self, unique_instance=Constants.LOGGING_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True, logging_instantiation=True)

        self._logged_messages = []

        self._file_log_buffer = []

        self._internal_log_development_messages_to_terminal = Registry.development_mode
        self._internal_log_information_messages_to_terminal = True
        self._internal_log_warning_messages_to_terminal = False
        self._internal_log_error_messages_to_terminal = True

        self._internal_log_development_messages_to_file = Registry.development_mode
        self._internal_log_information_messages_to_file = True
        self._internal_log_warning_messages_to_file = True
        self._internal_log_error_messages_to_file = True

        self._external_log_development_messages_to_terminal = Registry.development_mode
        self._external_log_information_messages_to_terminal = True
        self._external_log_warning_messages_to_terminal = False
        self._external_log_error_messages_to_terminal = True

        self._external_log_development_messages_to_file = Registry.development_mode
        self._external_log_information_messages_to_file = True
        self._external_log_warning_messages_to_file = True
        self._external_log_error_messages_to_file = True

    def set_external_log_development_messages_to_terminal(self, value):
        self._external_log_development_messages_to_terminal = value

    def set_external_log_information_messages_to_terminal(self, value):
        self._external_log_information_messages_to_terminal = value

    def set_external_log_warning_messages_to_terminal(self, value):
        self._external_log_warning_messages_to_terminal = value

    def set_external_log_error_messages_to_terminal(self, value):
        self._external_log_error_messages_to_terminal = value

    def set_external_log_development_messages_to_file(self, value):
        self._external_log_development_messages_to_file = value

    def set_external_log_information_messages_to_file(self, value):
        self._external_log_information_messages_to_file = value

    def set_external_log_warning_messages_to_file(self, value):
        self._external_log_warning_messages_to_file = value

    def set_external_log_error_messages_to_file(self, value):
        self._external_log_error_messages_to_file = value

    def get_external_log_development_messages_to_terminal(self):
        return self._external_log_development_messages_to_terminal

    def get_external_log_information_messages_to_terminal(self):
        return self._external_log_information_messages_to_terminal

    def get_external_log_warning_messages_to_terminal(self):
        return self._external_log_warning_messages_to_terminal

    def get_external_log_error_messages_to_terminal(self):
        return self._external_log_error_messages_to_terminal

    def get_external_log_development_messages_to_file(self):
        return self._external_log_development_messages_to_file

    def get_external_log_information_messages_to_file(self):
        return self._external_log_information_messages_to_file

    def get_external_log_warning_messages_to_file(self):
        return self._external_log_warning_messages_to_file

    def get_external_log_error_messages_to_file(self):
        return self._external_log_error_messages_to_file

    def set_internal_log_development_messages_to_terminal(self, value):
        self._internal_log_development_messages_to_terminal = value

    def set_internal_log_information_messages_to_terminal(self, value):
        self._internal_log_information_messages_to_terminal = value

    def set_internal_log_warning_messages_to_terminal(self, value):
        self._internal_log_warning_messages_to_terminal = value

    def set_internal_log_error_messages_to_terminal(self, value):
        self._internal_log_error_messages_to_terminal = value

    def set_internal_log_development_messages_to_file(self, value):
        self._internal_log_development_messages_to_file = value

    def set_internal_log_information_messages_to_file(self, value):
        self._internal_log_information_messages_to_file = value

    def set_internal_log_warning_messages_to_file(self, value):
        self._internal_log_warning_messages_to_file = value

    def set_internal_log_error_messages_to_file(self, value):
        self._internal_log_error_messages_to_file = value

    def get_internal_log_development_messages_to_terminal(self):
        return self._internal_log_development_messages_to_terminal

    def get_internal_log_information_messages_to_terminal(self):
        return self._internal_log_information_messages_to_terminal

    def get_internal_log_warning_messages_to_terminal(self):
        return self._internal_log_warning_messages_to_terminal

    def get_internal_log_error_messages_to_terminal(self):
        return self._internal_log_error_messages_to_terminal

    def get_internal_log_development_messages_to_file(self):
        return self._internal_log_development_messages_to_file

    def get_internal_log_information_messages_to_file(self):
        return self._internal_log_information_messages_to_file

    def get_internal_log_warning_messages_to_file(self):
        return self._internal_log_warning_messages_to_file

    def get_internal_log_error_messages_to_file(self):
        return self._internal_log_error_messages_to_file

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def logger_core(self, message, do_traceback, repeat_for_effect, log_level, internal):
        if internal:
            if log_level == Constants.DEVELOPMENT:
                log_to_file = self._internal_log_development_messages_to_file
                log_to_terminal = self._internal_log_development_messages_to_terminal
            elif log_level == Constants.INFORMATION:
                log_to_file = self._internal_log_information_messages_to_file
                log_to_terminal = self._internal_log_information_messages_to_terminal
            elif log_level == Constants.WARNING:
                log_to_file = self._internal_log_warning_messages_to_file
                log_to_terminal = self._internal_log_warning_messages_to_terminal
            elif log_level == Constants.ERROR:
                log_to_file = self._internal_log_error_messages_to_file
                log_to_terminal = self._internal_log_error_messages_to_terminal
        else:
            if log_level == Constants.DEVELOPMENT:
                log_to_file = self._external_log_development_messages_to_file
                log_to_terminal = self._external_log_development_messages_to_terminal
            elif log_level == Constants.INFORMATION:
                log_to_file = self._external_log_information_messages_to_file
                log_to_terminal = self._external_log_information_messages_to_terminal
            elif log_level == Constants.WARNING:
                log_to_file = self._external_log_warning_messages_to_file
                log_to_terminal = self._external_log_warning_messages_to_terminal
            elif log_level == Constants.ERROR:
                log_to_file = self._external_log_error_messages_to_file
                log_to_terminal = self._external_log_error_messages_to_terminal

        if log_to_file or log_to_terminal:
            if repeat_for_effect is False:
                if type(message) == str:
                    if message in self._logged_messages:
                        return False
                elif message[0] in self._logged_messages:
                    return False
                self._logged_messages.append(message[0])

            if type(message) == str:
                inserted_variables_to_message = message
            elif type(message) == list or type(message) == tuple:
                if len(message) == 2:
                    inserted_variables_to_message = message[0].format(*message[1])
                else:
                    inserted_variables_to_message = message

            message = ""
            now = _datetime.datetime.now()
            now.microsecond
            date_time_stamp = now.strftime("[%d/%m/%Y @ %H:%M:%S.%f] ")
            message += date_time_stamp
            if log_level == Constants.DEVELOPMENT:
                message += "- DEVELOPMENT - "
            elif log_level == Constants.INFORMATION:
                message += "- INFORMATION - "
            elif log_level == Constants.WARNING:
                message += "- WARNING - "
            elif log_level == Constants.ERROR:
                message += "- ERROR - "
            message += inserted_variables_to_message

            if do_traceback:
                try:
                    trace = _traceback.print_exc()
                    if trace == None:
                        trace = "".join(_traceback.format_stack())
                except:
                    trace = ""
            else:
                trace = ""

            message += f"\n{trace}"

            message = message.strip()

            formatted_message = ""
            first_line = True
            for line in message.split("\n"):
                if first_line is False:
                    prefix = "...    "
                else:
                    prefix = ""
                formatted_message += prefix + line.strip() + "\n"
                first_line = False

            formatted_message = formatted_message.strip()

            if log_to_terminal:
                print(formatted_message)
            if log_to_file:
                self._file_log_buffer.append((formatted_message, log_level, internal))

        return False

    def log_development(self, message, do_traceback=False, repeat_for_effect=False):
        self.logger_core(message, do_traceback, repeat_for_effect, Constants.DEVELOPMENT, True)

    def log_information(self, message, do_traceback=False, repeat_for_effect=False):
        self.logger_core(message, do_traceback, repeat_for_effect, Constants.INFORMATION, True)

    def log_warning(self, message, do_traceback=False, repeat_for_effect=False):
        self.logger_core(message, do_traceback, repeat_for_effect, Constants.WARNING, True)

    def log_error(self, message, do_traceback=True, repeat_for_effect=False):
        self.logger_core(message, do_traceback, repeat_for_effect, Constants.ERROR, True)

class InternalLogger:
    def __init__(self):
        _initialize(self)

        if not Constants.LOGGING_INTERMEDIARY_OBJECT in Registry.pmma_module_spine.keys():
            raise _LoggingNotInitializedError()

        self._logger_intermediary: "LoggerIntermediary" = Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT]

    def set_log_development_messages_to_terminal(self, value):
        self._logger_intermediary.set_internal_log_development_messages_to_terminal()(value)

    def set_log_information_messages_to_terminal(self, value):
        self._logger_intermediary.set_internal_log_information_messages_to_terminal(value)

    def set_log_warning_messages_to_terminal(self, value):
        self._logger_intermediary.set_internal_log_warning_messages_to_terminal(value)

    def set_log_error_messages_to_terminal(self, value):
        self._logger_intermediary.set_internal_log_error_messages_to_terminal(value)

    def set_log_development_messages_to_file(self, value):
        self._logger_intermediary.set_internal_log_development_messages_to_file(value)

    def set_log_information_messages_to_file(self, value):
        self._logger_intermediary.set_internal_log_information_messages_to_file(value)

    def set_log_warning_messages_to_file(self, value):
        self._logger_intermediary.set_internal_log_warning_messages_to_file(value)

    def set_log_error_messages_to_file(self, value):
        self._logger_intermediary.set_internal_log_error_messages_to_file(value)

    def get_log_development_messages_to_terminal(self):
        return self._logger_intermediary.get_internal_log_development_messages_to_terminal()

    def get_log_information_messages_to_terminal(self):
        return self._logger_intermediary.get_internal_log_information_messages_to_terminal()

    def get_log_warning_messages_to_terminal(self):
        return self._logger_intermediary.get_internal_log_warning_messages_to_terminal()

    def get_log_error_messages_to_terminal(self):
        return self._logger_intermediary.get_internal_log_error_messages_to_terminal()

    def get_log_development_messages_to_file(self):
        return self._logger_intermediary.get_internal_log_development_messages_to_file()

    def get_log_information_messages_to_file(self):
        return self._logger_intermediary.get_internal_log_information_messages_to_file()

    def get_log_warning_messages_to_file(self):
        return self._logger_intermediary.get_internal_log_warning_messages_to_file()

    def get_log_error_messages_to_file(self):
        return self._logger_intermediary.get_internal_log_error_messages_to_file()

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
            self._logger_intermediary.set_internal_log_development_messages_to_terminal(Registry.development_mode)
        else:
            self._logger_intermediary.set_internal_log_development_messages_to_terminal(log_development_messages_to_terminal)
        self._logger_intermediary.set_internal_log_information_messages_to_terminal(log_information_messages_to_terminal)
        self._logger_intermediary.set_internal_log_warning_messages_to_terminal(log_warning_messages_to_terminal)
        self._logger_intermediary.set_internal_log_error_messages_to_terminal(log_error_messages_to_terminal)

        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_internal_log_development_messages_to_file(Registry.development_mode)
        else:
            self._logger_intermediary.set_internal_log_development_messages_to_file(log_development_messages_to_file)
        self._logger_intermediary.set_internal_log_information_messages_to_file(log_information_messages_to_file)
        self._logger_intermediary.set_internal_log_warning_messages_to_file(log_warning_messages_to_file)
        self._logger_intermediary.set_internal_log_error_messages_to_file(log_error_messages_to_file)

    def log_development(self, message, do_traceback=False, repeat_for_effect=False):
        self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.DEVELOPMENT, True)

    def log_information(self, message, do_traceback=False, repeat_for_effect=False):
        self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.INFORMATION, True)

    def log_warning(self, message, do_traceback=False, repeat_for_effect=False):
        self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.WARNING, True)

    def log_error(self, message, do_traceback=True, repeat_for_effect=False):
        self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.ERROR, True)