from gc import collect as _gc__collect
import importlib as _importlib

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class RenderPipelineManager:
    def __init__(self):
        _initialize(self, unique_instance=_Constants.RENDER_PIPELINE_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        if _Registry.cython_acceleration_available:
            self.render_pipeline_module = _importlib.import_module(
                "pmma.bin.render_pipeline_utils")

        else:
            self.render_pipeline_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.render_pipeline_utils")

        _Registry.render_pipeline_acceleration_available = True

        ### (anything below this is heuristic) ###

        self.render_queue = []

        self.old_order = {}
        self.new_order = {}

        self.current_location = [0, 0]

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            _Registry.render_pipeline_acceleration_available = False
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add_object(self, new_object):
        if self.render_queue == []:
            self.render_queue.append(new_object)
            location = self.current_location
            self.current_location[0] += 1
            return location
        else:
            if type(self.render_queue[-1]) == RenderPipeline:
                identifier = self.render_queue[-1].add_object(new_object) # place holder
                location = self.current_location
                self.current_location[1] = identifier
                return location
            elif self.render_queue[-1]._properties[_Constants.RENDER_PIPELINE_COMPATIBLE]:
                pass