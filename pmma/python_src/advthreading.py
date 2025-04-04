from threading import Thread as _threading__Thread

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

class Thread(_threading__Thread):
    """
    🟩 **R** -
    """
    def __init__(self, *args, **keywords):
        """
        🟩 **R** -
        """
        self._sys__module = _ModuleManager.import_module("sys")

        _threading__Thread.__init__(self, *args, **keywords)

        self._killed = False

    def start(self):
        """
        🟩 **R** -
        """
        self.__run_backup = self.run
        self.run = self.__run
        _threading__Thread.start(self)

    def __run(self):
        """
        🟩 **R** -
        """
        self._sys__module.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        """
        🟩 **R** -
        """
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        """
        🟩 **R** -
        """
        if self._killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        """
        🟩 **R** -
        """
        self._killed = True