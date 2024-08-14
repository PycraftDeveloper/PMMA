import sys
import threading

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Thread(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)

        self.attributes = []

        Registry.pmma_object_instances[id(self)] = self
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
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