import datetime as _datetime
import traceback as _traceback
import gc as _gc
import threading as _threading

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize

class LoggerIntermediary:
    def __init__(self):
        _initialize(self, unique_instance=Constants.LOGGING_OBJECT, add_to_pmma_module_spine=True)

        self._logged_messages = []

        self._file_log_buffer = []

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def logger_core(self, message, do_traceback, repeat_for_effect, log_level, log_to_file, log_to_terminal, internal):
        if log_to_file or log_to_terminal:
            if repeat_for_effect is False:
                if message[0] in self._logged_messages:
                    return False
                self._logged_messages.append(message[0])

            if len(message) == 2:
                inserted_variables_to_message = message[0].format(*message[1])
            else:
                inserted_variables_to_message = message[0]

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

class InternalLogger:
    def __init__(self):
        self._log_development_messages_to_terminal = False
        self._log_information_messages_to_terminal = False
        self._log_warning_messages_to_terminal = False
        self._log_error_messages_to_terminal = False

        self._log_development_messages_to_file = False
        self._log_information_messages_to_file = False
        self._log_warning_messages_to_file = False
        self._log_error_messages_to_file = False

        self.logger_intermediary = Registry.pmma_module_spine[Constants.LOGGING_OBJECT]

    # def set_log_levels(self, ---all with defaults---):
    # def set---log level--(self, value): exct

    def log_development(self, message, do_traceback=False, repeat_for_effect=False):
        self.logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.DEVELOPMENT, self._log_development_messages_to_file, self._log_development_messages_to_terminal, True)

    def log_information(self, message, do_traceback=False, repeat_for_effect=False):
        self.logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.INFORMATION, self._log_information_messages_to_file, self._log_information_messages_to_terminal, True)

    def log_warning(self, message, do_traceback=False, repeat_for_effect=False):
        self.logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.WARNING, self._log_warning_messages_to_file, self._log_warning_messages_to_terminal, True)

    def log_error(self, message, do_traceback=True, repeat_for_effect=False):
        self.logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, Constants.ERROR, self._log_error_messages_to_file, self._log_error_messages_to_terminal, True)