from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class RenderPipeline:
    def __init__(self):
        self.compute_functions = []

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True