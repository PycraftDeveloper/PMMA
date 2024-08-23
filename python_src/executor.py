import subprocess as _subprocess
import threading as _threading
import gc as _gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Executor:
    def __init__(self):
        initialize(self)

        self._exit_code = None
        self._result = None
        self._thread = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def run(self, command, blocking=True, hide_window=True):
        self._exit_code = None
        self._result = None

        self._thread = _threading.Thread(target=self._run, args=(command, hide_window,))
        self._thread.name = "Executor:Execution_Thread"
        if blocking is False:
            self._thread.daemon = True
        self._thread.start()

        if blocking:
            self._thread.join()

    def _run(self, command, hide_window):
        command_type = type(command)

        try:
            if command_type == list or command_type == tuple:
                if hide_window:
                    result = _subprocess.run(command, capture_output=True, text=True, creationflags=Constants.CREATE_NO_WINDOW)
                else:
                    result = _subprocess.run(command, capture_output=True, text=True)
            else:
                log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

                if hide_window:
                    result = _subprocess.run(command, shell=True, capture_output=True, text=True, creationflags=Constants.CREATE_NO_WINDOW)
                else:
                    result = _subprocess.run(command, shell=True, capture_output=True, text=True)

            self._result = result.stdout
            self._exit_code = result.returncode
        except _subprocess.CalledProcessError as result:
            self._result = result.output
            self._exit_code = result.returncode

    def get_exit_code(self):
        return self._exit_code

    def get_result(self):
        return self._result.strip()

class AdvancedExecutor:
    def __init__(self):
        initialize(self)

        self._exit_code = None
        self._result = ""
        self._thread = None

        self._command_running = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def run(self, command, hide_window=True):
        if self._command_running is False:
            self._command_running = True

            self._exit_code = None
            self._result = ""

            self._thread = _threading.Thread(target=self._update_result, args=(command, hide_window,))
            self._thread.daemon = True
            self._thread.name = "AdvancedExecutor:Execution_Thread"
            self._thread.start()

    def get_busy(self):
        return self._command_running

    def get_result(self):
        return self._result.strip()

    def _update_result(self, command, hide_window):
        for path in self._run(command, hide_window):
            self._result += path.strip() + "\n"
        self._command_running = False

    def _run(self, command, hide_window):
        command_type = type(command)
        if command_type == list or command_type == tuple:
            if hide_window:
                process = _subprocess.Popen(command, stdout=_subprocess.PIPE, text=True, creationflags=Constants.CREATE_NO_WINDOW)
            else:
                process = _subprocess.Popen(command, stdout=_subprocess.PIPE, text=True)
        else:
            log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

            if hide_window:
                process = _subprocess.Popen(command, stdout=_subprocess.PIPE, shell=True, text=True, creationflags=Constants.CREATE_NO_WINDOW)
            else:
                process = _subprocess.Popen(command, stdout=_subprocess.PIPE, shell=True, text=True)

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