from subprocess import run as _subprocess__run
from subprocess import CalledProcessError as _subprocess__CalledProcessError
from subprocess import Popen as _subprocess__Popen
from subprocess import PIPE as _subprocess__PIPE
from threading import Thread as _threading__Thread

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.general import get_operating_system as _get_operating_system

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
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

        self._exit_code = None
        self._result = None
        self._thread = None

        self._logger = _InternalLogger()

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

        self._thread = _threading__Thread(target=self._run, args=(command, hide_window,))
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
                if hide_window and _get_operating_system() == _Constants.WINDOWS:
                    result = _subprocess__run(command, capture_output=True, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
                else:
                    result = _subprocess__run(command, capture_output=True, text=True)
            else:
                self._logger.log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

                if hide_window and _get_operating_system() == _Constants.WINDOWS:
                    result = _subprocess__run(command, shell=True, capture_output=True, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
                else:
                    result = _subprocess__run(command, shell=True, capture_output=True, text=True)

            self._result = result.stdout
            self._exit_code = result.returncode
        except _subprocess__CalledProcessError as result:
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

        self._exit_code = None
        self._result = ""
        self._thread = None

        self._command_running = False

        self._logger = _InternalLogger()

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

            self._thread = _threading__Thread(target=self._update_result, args=(command, hide_window,))
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
            if hide_window and _get_operating_system() == _Constants.WINDOWS:
                process = _subprocess__Popen(command, stdout=_subprocess__PIPE, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
            else:
                process = _subprocess__Popen(command, stdout=_subprocess__PIPE, text=True)
        else:
            self._logger.log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

            if hide_window and _get_operating_system() == _Constants.WINDOWS:
                process = _subprocess__Popen(command, stdout=_subprocess__PIPE, shell=True, text=True, creationflags=_InternalConstants.CREATE_NO_WINDOW)
            else:
                process = _subprocess__Popen(command, stdout=_subprocess__PIPE, shell=True, text=True)

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