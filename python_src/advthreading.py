import sys as _sys
import threading as _threading

from pmma.python_src.general import *
from pmma.python_src.registry import Registry

class Thread(_threading.Thread):
    def __init__(self, *args, **keywords):
        _threading.Thread.__init__(self, *args, **keywords)

        initialize(self)

        self.killed = False

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
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True