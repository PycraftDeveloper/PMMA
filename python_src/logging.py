import datetime as _datetime
import traceback as _traceback
import gc as _gc
import threading as _threading

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize

class Logger:
    def __init__(
            self,
            log_information_to_file=True,
            log_information_to_terminal=True,
            log_development_to_file=True,
            log_development_to_terminal=None,
            log_warning_to_file=True,
            log_warning_to_terminal=True,
            log_error_to_file=True,
            log_error_to_terminal=True):

        _initialize(self, unique_instance=Constants.LOGGING_OBJECT, add_to_pmma_module_spine=True)

        if log_development is None:
            log_development = Registry.development_mode

        self._do_log_development = log_development
        self._do_log_information = log_information
        self._do_log_warning = log_warning
        self._do_log_error = log_error
        self._do_log_to_file = log_to_file and log_file is not None
        self._do_log_to_terminal = log_to_terminal
        self._log_file = log_file
        self._development_messages = []

        self._file_log_buffer = []

        self.log_information("Logging object initialized")
        self.log_information("Date format: DD/MM/YYYY @ HH:MM:SS:μS")

        self.log_development("When logging, this is how development messages will appear.")
        self.log_information("When logging, this is how information messages will appear.")
        self.log_warning("When logging, this is how warning messages will appear.")
        self.log_error("When logging, this is how error messages will appear.", do_traceback=False)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def initial_formatting(self, log_level):
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
        return message

    def logger_core(self, message, do_traceback, log_level):
        formatted_message = ""
        first_line = True
        for line in message.split("\n"):
            if first_line is False:
                prefix = "...    "
            else:
                prefix = ""
            formatted_message += prefix + line.strip() + "\n"
            first_line = False
        #message = f"{message.strip()} "
        start_of_message = self.initial_formatting(log_level)

        if do_traceback:
            trace = _traceback.print_exc()
            if trace == None:
                trace = "".join(_traceback.format_stack())
        else:
            trace = ""
        finished_message = start_of_message + formatted_message + trace
        finished_message = finished_message.strip()

        conveyed_message = False

        if self._do_log_to_terminal:
            print(finished_message)
            conveyed_message = True

        self._file_log_buffer.append((finished_message, log_level))

        if self._do_log_to_file:
            with open(self._log_file, "a") as log_file:
                log_file.write(finished_message + "\n")

            conveyed_message = True

        return conveyed_message

    def log_development(
            self,
            message,
            do_traceback=False,
            repeat_for_effect=False):

        if self._do_log_development and message.strip() != "":
            if repeat_for_effect is False and message in self._development_messages:
                return False
            self._development_messages.append(message)
            return self.logger_core(message, do_traceback, Constants.DEVELOPMENT)
        return False

    def log_information(self, message, do_traceback=False):
        if self._do_log_information and message.strip() != "":
            return self.logger_core(message, do_traceback, Constants.INFORMATION)
        return False

    def log_warning(self, message, do_traceback=False):
        if self._do_log_warning and message.strip() != "":
            return self.logger_core(message, do_traceback, Constants.WARNING)
        return False

    def log_error(self, message, do_traceback=True):
        if self._do_log_error and message.strip() != "":
            return self.logger_core(message, do_traceback, Constants.ERROR)
        return False