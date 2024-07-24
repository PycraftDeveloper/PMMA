import datetime
import traceback

import pmma.python_src.core as core
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Logger:
    def __init__(self, log_development=None, log_information=False, log_warning=False, log_error=True, log_to_file=False, log_file=None, log_to_terminal=True):
        if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
            core.log_warning("Logging object already exists")
            core.log_development("Some PMMA objects can only be initialized once. This is to avoid creating unexpected behavior.")
            raise Exception("Logging object already exists")

        if log_development is None:
            log_development = Registry.development_mode

        self.do_log_development = log_development
        self.do_log_information = log_information
        self.do_log_warning = log_warning
        self.do_log_error = log_error
        self.do_log_to_file = log_to_file and log_file is not None
        self.do_log_to_terminal = log_to_terminal
        self.log_file = log_file
        self.development_messages = []

        Registry.pmma_module_spine[Constants.LOGGING_OBJECT] = self

        self.log_information("Logging object initialized")
        self.log_information("Date format: DD/MM/YYYY @ HH:MM:SS:μS")

    def initial_formatting(self, log_level):
        message = ""
        now = datetime.datetime.now()
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
        message = f"{message.strip()} "
        start_of_message = self.initial_formatting(log_level)
        if do_traceback:
            trace = traceback.print_exc()
            if trace == None:
                trace = "".join(traceback.format_stack())
        else:
            trace = ""
        finished_message = start_of_message + message + trace
        finished_message = finished_message.strip()

        if self.do_log_to_terminal:
            print(finished_message)

        if self.do_log_to_file:
            with open(self.log_file, "a") as log_file:
                log_file.write(finished_message + "\n")

    def log_development(self, message, do_traceback=False, repeat_for_effect=False):
        if self.do_log_development and message.strip() != "":
            if repeat_for_effect is False and message in self.development_messages:
                return
            self.development_messages.append(message)
            self.logger_core(message, do_traceback, Constants.DEVELOPMENT)

    def log_information(self, message, do_traceback=False):
        if self.do_log_information and message.strip() != "":
            self.logger_core(message, do_traceback, Constants.INFORMATION)

    def log_warning(self, message, do_traceback=False):
        if self.do_log_warning and message.strip() != "":
            self.logger_core(message, do_traceback, Constants.WARNING)

    def log_error(self, message, do_traceback=True):
        if self.do_log_error and message.strip() != "":
            self.logger_core(message, do_traceback, Constants.ERROR)