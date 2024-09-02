import gc as _gc

import moderngl as _moderngl
import numpy as _numpy
import moderngl_window as _moderngl_window

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize

class OpenGLIntermediary:
    def __init__(self):
        _initialize(self, unique_instance=Constants.OPENGL_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        if Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            if Registry.display_initialized is False:
                log_warning("No OpenGL ready display available.")

                log_development("The OpenGL module requires a PMMA \
display object to have already been created, with OpenGL support. Make \
sure to also call the 'create' function in the 'Display' class to create it.")

                raise Exception("No OpenGL ready display available.")
        else:
            log_development("The OpenGL module requires a PMMA display \
object to have already been created, with OpenGL support. Make sure to \
instantiate the 'Display' class first!")

            raise Exception("No OpenGL ready display instantiated.")

        try:
            if Registry.context is None:
                Registry.context = _moderngl.create_context()
                _moderngl_window.activate_context(Registry.window_context, Registry.context)
        except Exception as error:
            log_error("Failed to create OpenGL context.")
            log_development("Failed to create OpenGL context. The most \
likely cause for this error is that there is no available display with OpenGL \
support initiated; make sure to also call the 'create' function in the 'Display' \
class to create it. Should that also not work, make sure that you have the \
appropriate graphics drivers installed and make sure that your GPU supports OpenGL. \
If this fails, try to run another OpenGL application first to attempt to isolate the problem.")

            raise error

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_context(self):
        return Registry.context

    def blit_image_to_texture(self, image, texture):
        texture.write(image)