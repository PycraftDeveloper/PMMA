import subprocess
import threading

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Executor:
    def __init__(self):
        initialize(self)

        self.exit_code = None
        self.result = None
        self.thread = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def run(self, command, blocking=True, hide_window=True):
        self.exit_code = None
        self.result = None

        self.thread = threading.Thread(target=self._run, args=(command, hide_window,))
        self.thread.name = "Executor:Execution_Thread"
        if blocking is False:
            self.thread.daemon = True
        self.thread.start()

        if blocking:
            self.thread.join()

    def _run(self, command, hide_window):
        command_type = type(command)

        try:
            if command_type == list or command_type == tuple:
                if hide_window:
                    result = subprocess.run(command, capture_output=True, text=True, creationflags=Constants.CREATE_NO_WINDOW)
                else:
                    result = subprocess.run(command, capture_output=True, text=True)
            else:
                log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

                if hide_window:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, creationflags=Constants.CREATE_NO_WINDOW)
                else:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)

            self.result = result.stdout
            self.exit_code = result.returncode
        except subprocess.CalledProcessError as result:
            self.result = result.output
            self.exit_code = result.returncode

    def get_exit_code(self):
        return self.exit_code

    def get_result(self):
        return self.result.strip()

class AdvancedExecutor:
    def __init__(self):
        initialize(self)

        self.exit_code = None
        self.result = ""
        self.thread = None

        self.command_running = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def run(self, command, hide_window=True):
        if self.command_running is False:
            self.command_running = True

            self.exit_code = None
            self.result = ""

            self.thread = threading.Thread(target=self._update_result, args=(command, hide_window,))
            self.thread.daemon = True
            self.thread.name = "AdvancedExecutor:Execution_Thread"
            self.thread.start()

    def get_busy(self):
        return self.command_running

    def get_result(self):
        return self.result.strip()

    def _update_result(self, command, hide_window):
        for path in self._run(command, hide_window):
            self.result += path.strip() + "\n"
        self.command_running = False

    def _run(self, command, hide_window):
        command_type = type(command)
        if command_type == list or command_type == tuple:
            if hide_window:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, creationflags=Constants.CREATE_NO_WINDOW)
            else:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        else:
            log_development("You are not using an array of arguments as your command. \
This has the potential to be less secure, especially when using the user's input as a \
command. It is strongly recommended that you change your approach to use a list to avoid \
'shell injection vulnerabilities' where the end user specifies the command to be run, not \
its arguments, leading to unsecure commands being run on the host system!")

            if hide_window:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, text=True, creationflags=Constants.CREATE_NO_WINDOW)
            else:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, text=True)

        result = ""
        while True:
            output = process.stdout.readline()
            output = output.strip()
            if output == '' and process.poll() is not None:
                self.exit_code = process.returncode
                break
            if output:
                result += output.strip()
                yield output.strip()
        rc = process.poll()
        yield str(rc)