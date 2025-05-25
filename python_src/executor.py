from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class Executor:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._threading__module = _ModuleManager.import_module("threading")
        self._subprocess__module = _ModuleManager.import_module("subprocess")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

        self._exit_code = None
        self._result = None
        self._thread = None

        self._logger = self._logging_utils__module.InternalLogger()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def run(self, command, blocking=True, hide_window=True):
        """
        🟩 **R** -
        """
        self._exit_code = None
        self._result = None

        self._thread = self._threading__module.Thread(target=self._run, args=(command, hide_window,))
        self._thread.name = "Executor:Execution_Thread"
        if blocking is False:
            self._thread.daemon = True
        self._thread.start()

        if blocking:
            self._thread.join()

    def _run(self, command, hide_window):
        """
        🟩 **R** -
        """
        command_type = type(command)

        try:
            if command_type == list or command_type == tuple:
                if hide_window and self._internal_general_utils.get_operating_system() == _Constants.WINDOWS:
                    result = self._subprocess__module.run(command, capture_output=True, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
                else:
                    result = self._subprocess__module.run(command, capture_output=True, text=True)
            else:
                self._logger.log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

                if hide_window and self._internal_general_utils.get_operating_system() == _Constants.WINDOWS:
                    result = self._subprocess__module.run(command, shell=True, capture_output=True, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
                else:
                    result = self._subprocess__module.run(command, shell=True, capture_output=True, text=True)

            self._result = result.stdout
            self._exit_code = result.returncode
        except self._subprocess__module.CalledProcessError as result:
            self._result = result.output
            self._exit_code = result.returncode

    def get_exit_code(self):
        """
        🟩 **R** -
        """
        return self._exit_code

    def get_result(self):
        """
        🟩 **R** -
        """
        if type(self._result) == str:
            return self._result.strip()
        else:
            return self._result

class AdvancedExecutor:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._threading__module = _ModuleManager.import_module("threading")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._exit_code = None
        self._result = ""
        self._thread = None

        self._command_running = False

        self._logger = self._logging_utils__module.InternalLogger()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def run(self, command, hide_window=True):
        """
        🟩 **R** -
        """
        if self._command_running is False:
            self._command_running = True

            self._exit_code = None
            self._result = ""

            self._thread = self._threading__module.Thread(target=self._update_result, args=(command, hide_window,))
            self._thread.daemon = True
            self._thread.name = "AdvancedExecutor:Execution_Thread"
            self._thread.start()

    def get_busy(self):
        """
        🟩 **R** -
        """
        return self._command_running

    def get_result(self):
        """
        🟩 **R** -
        """
        return self._result.strip()

    def _update_result(self, command, hide_window):
        """
        🟩 **R** -
        """
        for path in self._run(command, hide_window):
            self._result += path.strip() + "\n"
        self._command_running = False

    def _run(self, command, hide_window):
        """
        🟩 **R** -
        """
        command_type = type(command)
        if command_type == list or command_type == tuple:
            if hide_window and self._internal_general_utils.get_operating_system() == _Constants.WINDOWS:
                process = self._subprocess__module.Popen(command, stdout=self._subprocess__module.PIPE, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
            else:
                process = self._subprocess__module.Popen(command, stdout=self._subprocess__module.PIPE, text=True)
        else:
            self._logger.log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

            if hide_window and self._internal_general_utils.get_operating_system() == _Constants.WINDOWS:
                process = self._subprocess__module.Popen(command, stdout=self._subprocess__module.PIPE, shell=True, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
            else:
                process = self._subprocess__module.Popen(command, stdout=self._subprocess__module.PIPE, shell=True, text=True)

        result = ""
        while True:
            output = process.stdout.readline()
            output = output.strip()
            if output == '' and process.poll() is not None:
                self._exit_code = process.returncode
                break
            if output:
                result += output.strip()
                yield output.strip()
        rc = process.poll()
        yield str(rc)