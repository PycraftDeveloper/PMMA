from shutil import rmtree as _shutil__rmtree

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class LoggerIntermediary:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.LOGGING_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True, logging_instantiation=True)

        self._datetime__module = _ModuleManager.import_module("datetime")
        self._traceback__module = _ModuleManager.import_module("traceback")
        self._threading__module = _ModuleManager.import_module("threading")
        self._os__module = _ModuleManager.import_module("os")
        self._waiting__module = _ModuleManager.import_module("waiting")

        self._file__module = _ModuleManager.import_module("pmma.python_src.file")

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

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

        self._logging_thread_lock = self._threading__module.Lock()
        self._logging_thread_active = True

        self._log_to_file_thread = self._threading__module.Thread(target=self._file_logger_thread)
        self._log_to_file_thread.daemon = True
        self._log_to_file_thread.name = "LoggingIntermediary: Log_To_Files_Thread"

        self._project_log_folder = None

        self._log_directory = self._file__module.path_builder(_Registry.base_path, "logs")
        try:
            self._os__module.mkdir(self._log_directory)
        except:
            pass

        now = self._datetime__module.datetime.now()
        log_file_identifier = now.strftime("log %d-%m-%Y @ %H-%M-%S")

        self._log_folders_directory = self._file__module.path_builder(_Registry.base_path, "logs", log_file_identifier)
        try:
            self._os__module.mkdir(self._log_folders_directory)
        except:
            pass

        self._internal_log_directory = self._file__module.path_builder(_Registry.base_path, "logs", log_file_identifier, "pmma")
        try:
            self._os__module.mkdir(self._internal_log_directory)
        except:
            pass

        if self._passport_utils__module.PassportIntermediary.name is not None:
            name = self._passport_utils__module.PassportIntermediary.name
        else:
            name = "application"
        self._external_log_directory = self._file__module.path_builder(_Registry.base_path, "logs", log_file_identifier, name)
        try:
            self._os__module.mkdir(self._external_log_directory)
        except:
            pass

        _Registry.logging_path = [self._file__module.path_builder(self._internal_log_directory, "profile.txt"), self._file__module.path_builder(self._external_log_directory, "profile.txt")]

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

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._logging_thread_active = False
            self._log_to_file_thread.join()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
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
        if self._passport_utils__module.PassportIntermediary.project_log_directory is None:
            if self._passport_utils__module.PassportIntermediary.project_directory is None:
                project_log_directory = None
            else:
                project_log_directory = self._file__module.path_builder(self._passport_utils__module.PassportIntermediary.project_directory, "logs")
        else:
            project_log_directory = self._passport_utils__module.PassportIntermediary.project_log_directory

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
        old_logs = self._os__module.listdir(self._log_directory)
        now = self._datetime__module.datetime.now()
        for log_folder in old_logs:
            original_log_folder = log_folder
            log_folder = log_folder.split("log ")[-1]
            split_date = log_folder.split(" @ ")
            date = split_date[0].split("-")
            time = split_date[1].split("-")
            day, month, year = date[0], date[1], date[2]
            hour, minute, second = time[0], time[1], time[2]
            past = self._datetime__module.datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute), second=int(second))
            time_difference = abs(past-now).days
            if time_difference > _Registry.internal_log_duration:
                self.log_information(
                    "Removing internal log: {}, which was {} days old.",
                    variables=[original_log_folder, time_difference],
                    repeat_for_effect=True)

                _shutil__rmtree(
                self._file__module.path_builder(self._log_directory, original_log_folder),
                ignore_errors=True)

    def clear_external_logs(self):
        """
        🟩 **R** -
        """
        project_log_directory = self._determine_project_log_folder()
        if project_log_directory is not None:
            old_logs = self._os__module.listdir(project_log_directory)
            now = self._datetime__module.datetime.now()
            for log_folder in old_logs:
                original_log_folder = log_folder
                log_folder = log_folder.split("log ")[-1]
                split_date = log_folder.split(" @ ")
                date = split_date[0].split("-")
                time = split_date[1].split("-")
                day, month, year = date[0], date[1], date[2]
                hour, minute, second = time[0], time[1], time[2]
                past = self._datetime__module.datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute), second=int(second))
                time_difference = abs(past-now).days
                if time_difference > _Registry.external_log_duration:
                    self.log_information(
                    "Removing external log: {}, which was {} days old.",
                    variables=[original_log_folder, time_difference],
                    repeat_for_effect=True)

                    _shutil__rmtree(
                    self._file__module.path_builder(self._log_directory, original_log_folder),
                    ignore_errors=True)

    def _file_logger_thread(self): # self._file_log_buffer.append((formatted_message, log_level, internal))
        """
        🟩 **R** -
        """
        self.clear_internal_logs()
        self.clear_external_logs()

        while self._logging_thread_active:
            self._waiting__module.wait(self._file_logger_thread_wait_for_load)
            if not len(self._file_log_buffer) > 0:
                continue

            with self._logging_thread_lock:
                for message in self._file_log_buffer:
                    formatted_message, log_level, internal = message
                    if internal:
                        with open(self._file__module.path_builder(self._internal_log_directory, "log.txt"), "a") as file:
                            file.write(formatted_message+"\n")
                            if self._project_log_folder is not None:
                                with open(self._file__module.path_builder(self._project_log_folder, "pmma", "log.txt"), "a") as file:
                                    file.write(formatted_message+"\n")

                    with open(self._file__module.path_builder(self._log_folders_directory, "all.txt"), "a") as file:
                        file.write(formatted_message+"\n")
                    if self._project_log_folder is not None:
                        with open(self._file__module.path_builder(self._project_log_folder, "all.txt"), "a") as file:
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
            now = self._datetime__module.datetime.now()
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
                    trace = self._traceback__module.print_exec()
                    if trace == None:
                        trace = "".join(self._traceback__module.format_stack())
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

        if not _InternalConstants.LOGGING_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LOGGING_INTERMEDIARY_OBJECT)
            LoggerIntermediary()

        self._logger_intermediary = _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT]

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