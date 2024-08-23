import gc as _gc

import moderngl as _moderngl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class OpenGL:
    def __init__(self):
        initialize(self)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _check_if_opengl_backend_initialized(self):
        if not Constants.OPENGL_INTERMEDIARY_OBJECT in Registry.pmma_module_spine:
            log_development("OpenGL backend has not been initialized yet. This is \
most likely due to not having created a Display through PMMA. You must do this \
first if you want to be able to use these OpenGL functions.")

            raise OpenGLNotYetInitializedError()

    def get_simple_texture_rendering_program(self):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].get_simple_texture_rendering_program()

    def get_texture_aggregation_program(self):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].get_texture_aggregation_program()

    def get_simple_shape_rendering_program(self):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].get_simple_shape_rendering_program()

    def get_context(self):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].get_context()

    def create_fbo(
            self,
            width,
            height,
            texture=None,
            color_format=Constants.RGBA):

        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_fbo(
            width,
            height,
            texture=texture,
            color_format=color_format)

    def create_texture(
            self,
            width,
            height,
            color_format=Constants.RGBA,
            x_scaling_method=_moderngl.LINEAR,
            y_scaling_method=_moderngl.LINEAR):

        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_texture(
            width,
            height,
            color_format=color_format,
            x_scaling_method=x_scaling_method,
            y_scaling_method=y_scaling_method)

    def blit_image_to_texture(self, image, texture):
        self._check_if_opengl_backend_initialized()
        Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].blit_image_to_texture(image, texture)

    def create_buffer_object(self, data):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_buffer_object(data)

    def create_vbo(self, data):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_buffer_object(data)

    def create_cbo(self, data):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_buffer_object(data)

    def create_ibo(self, data):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_buffer_object(data)

    def create_vao(
            self,
            program,
            data_or_vbo,
            attributes=None,
            index_buffer=None):

        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].create_vao(
            program,
            data_or_vbo,
            attributes=attributes,
            index_buffer=index_buffer)