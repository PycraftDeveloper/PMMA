import gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class RenderPipeline:
    def __init__(self):
        self.render_points = []

        self.attributes = []

        Registry.pmma_object_instances[id(self)] = self
        self._shut_down = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add(self, render_class):
        if hasattr(render_class, "attributes"):
            if Constants.RENDER_PIPELINE_ABLE in render_class.attributes:
                self.render_points.append(render_class)
        else:
            pass