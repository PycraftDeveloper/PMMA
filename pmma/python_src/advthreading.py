import sys as _sys
import threading as _threading

class Thread(_threading.Thread):
    def __init__(self, *args, **keywords):
        _threading.Thread.__init__(self, *args, **keywords)

        self._killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        _threading.Thread.start(self)

    def __run(self):
        _sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self._killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self._killed = True