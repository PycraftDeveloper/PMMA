from gc import collect as _gc__collect

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class RenderPipelineManager:
    def __init__(self):
        _initialize(self, unique_instance=_Constants.RENDER_PIPELINE_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self.renderable_objects = []
        self.render_queue = []

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def evaluate_render_queue(self):
        for renderable_object in self.renderable_objects:
            if _Constants.RENDER_PIPELINEABLE in renderable_object._attributes:
                if type(self.render_queue[-1]) == RenderPipeline:
                    self.render_queue[-1].add_object(renderable_object)
                elif self.render_queue[-1]._attributes == _Constants.RENDER_PIPELINEABLE:
                    initial_object = self.render_queue.pop()
                    self.render_queue.append(RenderPipeline())
                    self.render_queue[-1].add_object(initial_object)
                    self.render_queue[-1].add_object(renderable_object)
                else:
                    self.render_queue.append(renderable_object)
            else:
                self.render_queue.append(renderable_object)

    def add_renderable_object(self, renderable_object):
        self.renderable_objects.append(renderable_object)

    def render(self):
        self.evaluate_render_queue()
        for renderable_object in self.render_queue:
            renderable_object.render()
        self.render_queue = []

class RenderPipeline:
    def __init__(self):
        _initialize(self)