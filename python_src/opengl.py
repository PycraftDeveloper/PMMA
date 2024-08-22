import gc as _gc

import moderngl as _moderngl
import numpy as _numpy

from pmma.python_src.shader import Shader as _Shader
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class OpenGL:
    def __init__(self):
        initialize(self)

        if Constants.OPENGL_OBJECT not in Registry.pmma_module_spine.keys():
            Registry.pmma_module_spine[Constants.OPENGL_OBJECT] = self

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
        except Exception as error:
            log_error("Failed to create OpenGL context.")
            log_development("Failed to create OpenGL context. The most \
likely cause for this error is that there is no available display with OpenGL \
support initiated; make sure to also call the 'create' function in the 'Display' \
class to create it. Should that also not work, make sure that you have the \
appropriate graphics drivers installed and make sure that your GPU supports OpenGL. \
If this fails, try to run another OpenGL application first to attempt to isolate the problem.")

            raise error

        self.simple_texture_rendering_program = _Shader()
        self.simple_texture_rendering_program.create_from_location(
            _path_builder(
                Registry.base_path,
                "shaders",
                "simple_texture_rendering"))

        self.texture_aggregation_program = _Shader()
        self.texture_aggregation_program.create_from_location(
            _path_builder(
                Registry.base_path,
                "shaders",
                "texture_aggregation"))

        self.simple_shape_rendering_program = _Shader()
        self.simple_shape_rendering_program.create_from_location(
            _path_builder(
                Registry.base_path,
                "shaders",
                "simple_shape_renderer"))

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_simple_texture_rendering_program(self):
        return self.simple_texture_rendering_program

    def get_texture_aggregation_program(self):
        return self.texture_aggregation_program

    def get_context(self):
        return Registry.context

    def create_fbo(
            self,
            width,
            height,
            texture=None,
            color_format=Constants.RGBA):

        if texture is None:
            fbo_texture = self.create_texture(
                width,
                height,
                color_format)

        else:
            if type(texture) == OpenGLObject:
                fbo_texture = texture.get()
            else:
                fbo_texture = texture

        fbo = Registry.context.framebuffer(
            color_attachments=[fbo_texture])

        return OpenGLObject(fbo)

    def create_texture(
            self,
            width,
            height,
            color_format=Constants.RGBA,
            x_scaling_method=_moderngl.LINEAR,
            y_scaling_method=_moderngl.LINEAR):

        color_component = len(color_format)

        texture = Registry.context.texture(
            (width, height),
            color_component)

        texture.filter = (x_scaling_method, y_scaling_method)
        return OpenGLObject(texture)

    def blit_image_to_texture(self, image, texture):
        if type(texture) == OpenGLObject:
            texture = texture.get()
        texture.write(image)

    def create_buffer_object(self, data):
        if type(data) == _numpy.ndarray:
            if data.dtype != _numpy.float32:
                data = data.astype(_numpy.float32)
        else:
            data = _numpy.array(data, dtype=_numpy.float32)

        buffer = Registry.context.buffer(data)
        return OpenGLObject(buffer)

    def create_vbo(self, data):
        return self.create_buffer_object(data)

    def create_cbo(self, data):
        return self.create_buffer_object(data)

    def create_ibo(self, data):
        return self.create_buffer_object(data)

    def create_vao(
            self,
            program,
            data_or_vbo,
            attributes=None,
            index_buffer=None):

        if type(data_or_vbo) == _moderngl.Buffer:
            vbo = data_or_vbo
        elif type(data_or_vbo) == OpenGLObject:
            vbo = data_or_vbo.get()
        else:
            data = data_or_vbo
            vbo = self.create_vbo(data)

        if type(program) == _Shader:
            shader_program = program.get()

        if attributes is None:
            if type(program) == _Shader:
                attributes = program.get_in_attributes()
            else:
                attributes = []

        if type(index_buffer) == OpenGLObject:
            index_buffer = index_buffer.get()

        vao = Registry.context.simple_vertex_array(
            shader_program,
            vbo,
            *attributes,
            index_buffer=index_buffer)
        return OpenGLObject(vao)