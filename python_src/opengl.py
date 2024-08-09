import gc

import moderngl
import numpy

from pmma.python_src.shader import Shader
from pmma.python_src.file import path_builder

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class OpenGLObject:
    def __init__(self, _object):
        self.object = _object

    def get(self):
        return self.object

    def __del__(self, do_garbage_collection=True):
        self.object.release()
        del self.object
        if do_garbage_collection:
            gc.collect()

class OpenGL:
    def __init__(self):
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
                Registry.context = moderngl.create_context()
        except Exception as error:
            log_error("Failed to create OpenGL context.")
            log_development("Failed to create OpenGL context. The most \
likely cause for this error is that there is no available display with OpenGL \
support initiated; make sure to also call the 'create' function in the 'Display' \
class to create it. Should that also not work, make sure that you have the \
appropriate graphics drivers installed and make sure that your GPU supports OpenGL. \
If this fails, try to run another OpenGL application first to attempt to isolate the problem.")

            raise error

        self.simple_texture_rendering_program = Shader()
        self.simple_texture_rendering_program.create_from_location(
            path_builder(
                Registry.base_path,
                "shaders",
                "simple_texture_rendering"))

        self.texture_aggregation_program = Shader()
        self.texture_aggregation_program.create_from_location(
            path_builder(
                Registry.base_path,
                "shaders",
                "texture_aggregation"))

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

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
            fbo_texture = texture
        fbo = Registry.context.framebuffer(
            color_attachments=[fbo_texture])

        return fbo

    def create_texture(
            self,
            width,
            height,
            color_format=Constants.RGBA,
            x_scaling_method=moderngl.LINEAR,
            y_scaling_method=moderngl.LINEAR):

        color_component = len(color_format)

        texture = Registry.context.texture(
            (width, height),
            color_component)

        texture.filter = (x_scaling_method, y_scaling_method)
        return texture

    def blit_image_to_texture(self, image, texture):
        texture.write(image)

    def create_vbo(self, data):
        if type(data) == numpy.ndarray:
            if data.dtype != numpy.float32:
                data = data.astype(numpy.float32)
        else:
            data = numpy.array(data, dtype=numpy.float32)

        return Registry.context.buffer(data)

    def create_ibo(self, data):
        if type(data) == numpy.ndarray:
            if data.dtype != numpy.int32:
                data = data.astype(numpy.int32)
        else:
            data = numpy.array(data, dtype=numpy.int32)

        return Registry.context.buffer(data)

    def create_vao(
            self,
            program,
            data_or_vbo,
            attributes=None,
            index_buffer=None):

        if type(data_or_vbo) != moderngl.Buffer:
            data = data_or_vbo
            vbo = self.create_vbo(data)
        else:
            vbo = data_or_vbo
        if attributes is None:
            if type(program) == Shader:
                attributes = program.get_in_attributes()
                program = program.get()
            else:
                attributes = []

        if type(program) == Shader:
            program = program.get()

        return Registry.context.simple_vertex_array(
            program,
            vbo,
            *attributes,
            index_buffer=index_buffer)