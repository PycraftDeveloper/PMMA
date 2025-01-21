from datetime import datetime as _datetime__datetime
from traceback import format_stack as _traceback__format_stack
from traceback import print_exc as _traceback__print_exec
from gc import collect as _gc__collect
from threading import Lock as _threading__Lock
from threading import Thread as _threading__Thread
from os import mkdir as _os__mkdir
from os import listdir as _os__listdir
from shutil import rmtree as _shutil__rmtree

from waiting import wait as _waiting__wait

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class LoggerIntermediary:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_Constants.LOGGING_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True, logging_instantiation=True)

        self._logged_messages = []

        self._file_log_buffer = []

        self._internal_log_development_messages_to_terminal = _Registry.development_mode
        self._internal_log_information_messages_to_terminal = True
        self._internal_log_warning_messages_to_terminal = False
        self._internal_log_error_messages_to_terminal = True

        self._internal_log_development_messages_to_file = _Registry.development_mode
        self._internal_log_information_messages_to_file = True
        self._internal_log_warning_messages_to_file = True
        self._internal_log_error_messages_to_file = True

        self._external_log_development_messages_to_terminal = _Registry.development_mode
        self._external_log_information_messages_to_terminal = True
        self._external_log_warning_messages_to_terminal = False
        self._external_log_error_messages_to_terminal = True

        self._external_log_development_messages_to_file = _Registry.development_mode
        self._external_log_information_messages_to_file = True
        self._external_log_warning_messages_to_file = True
        self._external_log_error_messages_to_file = True

        self._logging_thread_lock = _threading__Lock()
        self._logging_thread_active = True

        self._log_to_file_thread = _threading__Thread(target=self._file_logger_thread)
        self._log_to_file_thread.daemon = True
        self._log_to_file_thread.name = "LoggingIntermediary: Log_To_Files_Thread"

        self._project_log_folder = None

        self._log_directory = _path_builder(_Registry.base_path, "logs")
        try:
            _os__mkdir(self._log_directory)
        except:
            pass

        now = _datetime__datetime.now()
        log_file_identifier = now.strftime("log %d-%m-%Y @ %H-%M-%S")

        self._log_folders_directory = _path_builder(_Registry.base_path, "logs", log_file_identifier)
        try:
            _os__mkdir(self._log_folders_directory)
        except:
            pass

        self._internal_log_directory = _path_builder(_Registry.base_path, "logs", log_file_identifier, "pmma")
        try:
            _os__mkdir(self._internal_log_directory)
        except:
            pass

        if _PassportIntermediary.name is not None:
            name = _PassportIntermediary.name
        else:
            name = "application"
        self._external_log_directory = _path_builder(_Registry.base_path, "logs", log_file_identifier, name)
        try:
            _os__mkdir(self._external_log_directory)
        except:
            pass

        _Registry.logging_path = [_path_builder(self._internal_log_directory, "profile.txt"), _path_builder(self._external_log_directory, "profile.txt")]

        self._log_to_file_thread.start()

    def set_external_log_development_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._external_log_development_messages_to_terminal = value

    def set_external_log_information_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._external_log_information_messages_to_terminal = value

    def set_external_log_warning_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._external_log_warning_messages_to_terminal = value

    def set_external_log_error_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._external_log_error_messages_to_terminal = value

    def set_external_log_development_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._external_log_development_messages_to_file = value

    def set_external_log_information_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._external_log_information_messages_to_file = value

    def set_external_log_warning_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._external_log_warning_messages_to_file = value

    def set_external_log_error_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._external_log_error_messages_to_file = value

    def get_external_log_development_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._external_log_development_messages_to_terminal

    def get_external_log_information_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._external_log_information_messages_to_terminal

    def get_external_log_warning_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._external_log_warning_messages_to_terminal

    def get_external_log_error_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._external_log_error_messages_to_terminal

    def get_external_log_development_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._external_log_development_messages_to_file

    def get_external_log_information_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._external_log_information_messages_to_file

    def get_external_log_warning_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._external_log_warning_messages_to_file

    def get_external_log_error_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._external_log_error_messages_to_file

    def set_internal_log_development_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_development_messages_to_terminal = value

    def set_internal_log_information_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_information_messages_to_terminal = value

    def set_internal_log_warning_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_warning_messages_to_terminal = value

    def set_internal_log_error_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_error_messages_to_terminal = value

    def set_internal_log_development_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_development_messages_to_file = value

    def set_internal_log_information_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_information_messages_to_file = value

    def set_internal_log_warning_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_warning_messages_to_file = value

    def set_internal_log_error_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._internal_log_error_messages_to_file = value

    def get_internal_log_development_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._internal_log_development_messages_to_terminal

    def get_internal_log_information_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._internal_log_information_messages_to_terminal

    def get_internal_log_warning_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._internal_log_warning_messages_to_terminal

    def get_internal_log_error_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._internal_log_error_messages_to_terminal

    def get_internal_log_development_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._internal_log_development_messages_to_file

    def get_internal_log_information_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._internal_log_information_messages_to_file

    def get_internal_log_warning_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._internal_log_warning_messages_to_file

    def get_internal_log_error_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._internal_log_error_messages_to_file

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._logging_thread_active = False
            self._log_to_file_thread.join()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _file_logger_thread_wait_for_load(self):
        """
        🟩 **R** -
        """
        return len(self._file_log_buffer) > 0 or self._logging_thread_active is False

    def _determine_project_log_folder(self):
        """
        🟩 **R** -
        """
        if _PassportIntermediary.project_log_directory is None:
            if _PassportIntermediary.project_directory is None:
                project_log_directory = None
            else:
                project_log_directory = _path_builder(_PassportIntermediary.project_directory, "logs")
        else:
            project_log_directory = _PassportIntermediary.project_log_directory

        return project_log_directory

    def _project_log_folder_has_changed(self):
        """
        🟩 **R** -
        """
        new_folder = self._determine_project_log_folder()
        if self._project_log_folder != new_folder:
            self._project_log_folder = new_folder
            return True
        return False

    def clear_internal_logs(self):
        """
        🟩 **R** -
        """
        old_logs = _os__listdir(self._log_directory)
        now = _datetime__datetime.now()
        for log_folder in old_logs:
            original_log_folder = log_folder
            log_folder = log_folder.split("log ")[-1]
            split_date = log_folder.split(" @ ")
            date = split_date[0].split("-")
            time = split_date[1].split("-")
            day, month, year = date[0], date[1], date[2]
            hour, minute, second = time[0], time[1], time[2]
            past = _datetime__datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute), second=int(second))
            time_difference = abs(past-now).days
            if time_difference > _Registry.internal_log_duration:
                self.log_information(
                    "Removing internal log: {}, which was {} days old.",
                    variables=[original_log_folder, time_difference],
                    repeat_for_effect=True)

                _shutil__rmtree(
                _path_builder(self._log_directory, original_log_folder),
                ignore_errors=True)

    def clear_external_logs(self):
        """
        🟩 **R** -
        """
        project_log_directory = self._determine_project_log_folder()
        if project_log_directory is not None:
            old_logs = _os__listdir(project_log_directory)
            now = _datetime__datetime.now()
            for log_folder in old_logs:
                original_log_folder = log_folder
                log_folder = log_folder.split("log ")[-1]
                split_date = log_folder.split(" @ ")
                date = split_date[0].split("-")
                time = split_date[1].split("-")
                day, month, year = date[0], date[1], date[2]
                hour, minute, second = time[0], time[1], time[2]
                past = _datetime__datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute), second=int(second))
                time_difference = abs(past-now).days
                if time_difference > _Registry.external_log_duration:
                    self.log_information(
                    "Removing external log: {}, which was {} days old.",
                    variables=[original_log_folder, time_difference],
                    repeat_for_effect=True)

                    _shutil__rmtree(
                    _path_builder(self._log_directory, original_log_folder),
                    ignore_errors=True)

    def _file_logger_thread(self): # self._file_log_buffer.append((formatted_message, log_level, internal))
        """
        🟩 **R** -
        """
        self.clear_internal_logs()
        self.clear_external_logs()

        while self._logging_thread_active:
            _waiting__wait(self._file_logger_thread_wait_for_load)
            if not len(self._file_log_buffer) > 0:
                continue

            with self._logging_thread_lock:
                for message in self._file_log_buffer:
                    formatted_message, log_level, internal = message
                    if internal:
                        with open(_path_builder(self._internal_log_directory, "log.txt"), "a") as file:
                            file.write(formatted_message+"\n")
                            if self._project_log_folder is not None:
                                with open(_path_builder(self._project_log_folder, "pmma", "log.txt"), "a") as file:
                                    file.write(formatted_message+"\n")

                    with open(_path_builder(self._log_folders_directory, "all.txt"), "a") as file:
                        file.write(formatted_message+"\n")
                    if self._project_log_folder is not None:
                        with open(_path_builder(self._project_log_folder, "all.txt"), "a") as file:
                                file.write(formatted_message+"\n")

                self._file_log_buffer = []


    def logger_core(self, message, do_traceback, repeat_for_effect, log_level, internal, variables=[]):
        """
        🟩 **R** -
        """
        if message == "":
            return False
        if internal:
            if log_level == _Constants.DEVELOPMENT:
                log_to_file = self._internal_log_development_messages_to_file
                log_to_terminal = self._internal_log_development_messages_to_terminal
            elif log_level == _Constants.INFORMATION:
                log_to_file = self._internal_log_information_messages_to_file
                log_to_terminal = self._internal_log_information_messages_to_terminal
            elif log_level == _Constants.WARNING:
                log_to_file = self._internal_log_warning_messages_to_file
                log_to_terminal = self._internal_log_warning_messages_to_terminal
            elif log_level == _Constants.ERROR:
                log_to_file = self._internal_log_error_messages_to_file
                log_to_terminal = self._internal_log_error_messages_to_terminal
        else:
            if log_level == _Constants.DEVELOPMENT:
                log_to_file = self._external_log_development_messages_to_file
                log_to_terminal = self._external_log_development_messages_to_terminal
            elif log_level == _Constants.INFORMATION:
                log_to_file = self._external_log_information_messages_to_file
                log_to_terminal = self._external_log_information_messages_to_terminal
            elif log_level == _Constants.WARNING:
                log_to_file = self._external_log_warning_messages_to_file
                log_to_terminal = self._external_log_warning_messages_to_terminal
            elif log_level == _Constants.ERROR:
                log_to_file = self._external_log_error_messages_to_file
                log_to_terminal = self._external_log_error_messages_to_terminal

        if log_to_file or log_to_terminal:
            if not repeat_for_effect:
                if message in self._logged_messages:
                    return False
                else:
                    self._logged_messages.append(message)

            inserted_variables_to_message = message.format(*variables)

            message = ""
            now = _datetime__datetime.now()
            date_time_stamp = now.strftime("[%d/%m/%Y @ %H:%M:%S.%f] ")
            message += date_time_stamp
            if log_level == _Constants.DEVELOPMENT:
                message += "- DEVELOPMENT - "
            elif log_level == _Constants.INFORMATION:
                message += "- INFORMATION - "
            elif log_level == _Constants.WARNING:
                message += "- WARNING - "
            elif log_level == _Constants.ERROR:
                message += "- ERROR - "
            message += inserted_variables_to_message

            if do_traceback:
                try:
                    trace = _traceback__print_exec()
                    if trace == None:
                        trace = "".join(_traceback__format_stack())
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

            logged = False

            if log_to_terminal:
                print(formatted_message)
                logged = True
            if log_to_file:
                with self._logging_thread_lock:
                    self._file_log_buffer.append((formatted_message, log_level, internal))
                logged = True

            return logged

        return False

    def log_development(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self.logger_core(message, do_traceback, repeat_for_effect, _Constants.DEVELOPMENT, True, variables=variables)

    def log_information(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self.logger_core(message, do_traceback, repeat_for_effect, _Constants.INFORMATION, True, variables=variables)

    def log_warning(self, message,  variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self.logger_core(message, do_traceback, repeat_for_effect, _Constants.WARNING, True, variables=variables)

    def log_error(self, message,  variables=[], do_traceback=True, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self.logger_core(message, do_traceback, repeat_for_effect, _Constants.ERROR, True, variables=variables)

class InternalLogger:
    """
    🟩 **R** -
    """
    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if not _Constants.LOGGING_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LOGGING_INTERMEDIARY_OBJECT)
            LoggerIntermediary()

        self._logger_intermediary: "LoggerIntermediary" = _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT]

    def set_log_development_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_development_messages_to_terminal()(value)

    def set_log_information_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_information_messages_to_terminal(value)

    def set_log_warning_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_warning_messages_to_terminal(value)

    def set_log_error_messages_to_terminal(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_error_messages_to_terminal(value)

    def set_log_development_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_development_messages_to_file(value)

    def set_log_information_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_information_messages_to_file(value)

    def set_log_warning_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_warning_messages_to_file(value)

    def set_log_error_messages_to_file(self, value):
        """
        🟩 **R** -
        """
        self._logger_intermediary.set_internal_log_error_messages_to_file(value)

    def get_log_development_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_development_messages_to_terminal()

    def get_log_information_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_information_messages_to_terminal()

    def get_log_warning_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_warning_messages_to_terminal()

    def get_log_error_messages_to_terminal(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_error_messages_to_terminal()

    def get_log_development_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_development_messages_to_file()

    def get_log_information_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_information_messages_to_file()

    def get_log_warning_messages_to_file(self):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.get_internal_log_warning_messages_to_file()

    def get_log_error_messages_to_file(self):
        """
        🟩 **R** -
        """
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
        """
        🟩 **R** -
        """
        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_internal_log_development_messages_to_terminal(_Registry.development_mode)
        else:
            self._logger_intermediary.set_internal_log_development_messages_to_terminal(log_development_messages_to_terminal)
        self._logger_intermediary.set_internal_log_information_messages_to_terminal(log_information_messages_to_terminal)
        self._logger_intermediary.set_internal_log_warning_messages_to_terminal(log_warning_messages_to_terminal)
        self._logger_intermediary.set_internal_log_error_messages_to_terminal(log_error_messages_to_terminal)

        if log_development_messages_to_terminal is None:
            self._logger_intermediary.set_internal_log_development_messages_to_file(_Registry.development_mode)
        else:
            self._logger_intermediary.set_internal_log_development_messages_to_file(log_development_messages_to_file)
        self._logger_intermediary.set_internal_log_information_messages_to_file(log_information_messages_to_file)
        self._logger_intermediary.set_internal_log_warning_messages_to_file(log_warning_messages_to_file)
        self._logger_intermediary.set_internal_log_error_messages_to_file(log_error_messages_to_file)

    def log_development(self, message, variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.DEVELOPMENT, True, variables=variables)

    def log_information(self, message, variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.INFORMATION, True, variables=variables)

    def log_warning(self, message, variables=[], do_traceback=False, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.WARNING, True, variables=variables)

    def log_error(self, message, variables=[], do_traceback=True, repeat_for_effect=False):
        """
        🟩 **R** -
        """
        return self._logger_intermediary.logger_core(message, do_traceback, repeat_for_effect, _Constants.ERROR, True, variables=variables)