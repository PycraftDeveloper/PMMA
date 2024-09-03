import gc as _gc
import os as _os

import moderngl as _moderngl
from PIL import Image as _Image

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.error_utils import *
from pmma.python_src.utility.general_utils import initialize as _initialize

class OpenGL:
    def __init__(self):
        _initialize(self)

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

    def get_context(self):
        self._check_if_opengl_backend_initialized()
        return Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].get_context()

    def blit_image_to_texture(self, image, texture):
        self._check_if_opengl_backend_initialized()
        Registry.pmma_module_spine[Constants.OPENGL_INTERMEDIARY_OBJECT].blit_image_to_texture(image, texture)

class VertexBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._vbo = None

    def create(self, data, dynamic=False, reserve=0):
        self._data = data
        self._vbo = Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)

    def recreate(self):
        if self._vbo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._vbo.release()

            if self._data is None:
                self._vbo = Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._vbo = Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._vbo is None:
            self.create(data)
            return

        self._data = data
        self._vbo.write(self._data)

    def read(self, from_vbo=False):
        if from_vbo:
            return self._data
        else:
            if self._vbo is not None:
                return self._vbo.read()

    def get_vertex_buffer_object(self):
        return self._vbo

    def clear(self):
        self._data = None
        if self._vbo is not None:
            self._vbo.clear()

    def bind_to_uniform_block(self, binding):
        if self._vbo is not None:
            self._vbo.bind_to_uniform_block(binding)

    def bind_to_shader_storage_buffer(self, binding):
        if self._vbo is not None:
            self._vbo.bind_to_storage_buffer(binding)

    def _size(self):
        if self._vbo is not None:
            return self._vbo.size

    def get_size(self):
        log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_vertex_buffer_object(self):
        return self._vbo

    def get_dynamic(self):
        if self._vbo is not None:
            return self._vbo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._vbo is not None:
                self._vbo.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class ColorBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._cbo = None

    def create(self, data, dynamic=False, reserve=0):
        self._data = data
        self._cbo = Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)

    def recreate(self):
        if self._cbo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._cbo.release()

            if self._data is None:
                self._cbo = Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._cbo = Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._cbo is None:
            self.create(data)
            return

        self._data = data
        self._cbo.write(self._data)

    def read(self, from_vbo=False):
        if from_vbo:
            return self._data
        else:
            if self._cbo is not None:
                return self._cbo.read()

    def get_vertex_buffer_object(self):
        return self._cbo

    def clear(self):
        self._data = None
        if self._cbo is not None:
            self._cbo.clear()

    def bind_to_uniform_block(self, binding):
        if self._cbo is not None:
            self._cbo.bind_to_uniform_block(binding)

    def bind_to_shader_storage_buffer(self, binding):
        if self._cbo is not None:
            self._cbo.bind_to_storage_buffer(binding)

    def _size(self):
        if self._cbo is not None:
            return self._cbo.size

    def get_size(self):
        log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_color_buffer_object(self):
        return self._cbo

    def get_dynamic(self):
        if self._cbo is not None:
            return self._cbo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._cbo is not None:
                self._cbo.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class IndexBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._ibo = None

    def create(self, data, dynamic=False, reserve=0):
        self._data = data
        self._ibo = Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)

    def recreate(self):
        if self._ibo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._ibo.release()

            if self._data is None:
                self._ibo = Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._ibo = Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._ibo is None:
            self.create(data)
            return

        self._data = data
        self._ibo.write(self._data)

    def read(self, from_vbo=False):
        if from_vbo:
            return self._data
        else:
            if self._ibo is not None:
                return self._ibo.read()

    def get_index_buffer_object(self):
        return self._ibo

    def get_vertex_buffer_object(self):
        return self._ibo

    def clear(self):
        self._data = None
        if self._ibo is not None:
            self._ibo.clear()

    def bind_to_uniform_block(self, binding):
        if self._ibo is not None:
            self._ibo.bind_to_uniform_block(binding)

    def bind_to_shader_storage_buffer(self, binding):
        if self._ibo is not None:
            self._ibo.bind_to_storage_buffer(binding)

    def _size(self):
        if self._ibo is not None:
            return self._ibo.size

    def get_size(self):
        log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_dynamic(self):
        if self._ibo is not None:
            return self._ibo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._ibo is not None:
                self._ibo.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class VertexArrayObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._vao = None
        self._program = None
        self._vertex_buffer_object = None
        self._vertex_buffer_shader_attributes = None
        self._color_buffer_object = None
        self._color_buffer_shader_attributes = None
        self._index_buffer_object = None
        self._index_element_size = None

    def create(self, program, vertex_buffer_object, vertex_buffer_shader_attributes, color_buffer_object=None, color_buffer_shader_attributes=None, index_buffer_object=None, index_element_size=4):
        self._program = program
        self._vertex_buffer_object = vertex_buffer_object
        self._vertex_buffer_shader_attributes = vertex_buffer_shader_attributes
        self._color_buffer_object = color_buffer_object
        self._color_buffer_shader_attributes = color_buffer_shader_attributes
        self._index_buffer_object = index_buffer_object
        self._index_element_size = index_element_size

        program = self._program.get_program()
        vbo = self._vertex_buffer_object.get_vertex_buffer_object()
        if self._color_buffer_object is not None:
            cbo = self._color_buffer_object.get_color_buffer_object()
        else:
            cbo = None
        if self._index_buffer_object is not None:
            ibo = self._index_buffer_object.get_index_buffer_object()
        else:
            ibo = None

        self._vao = Registry.context.vertex_array(
            program,
            [
                (vbo, *self._vertex_buffer_shader_attributes),
                (cbo, *self._color_buffer_shader_attributes)],
            index_buffer=ibo,
            index_element_size=self._index_element_size)

    def recreate(self):
        if self._vao is not None:
            self._vao.release()

            program = self._program.get_program()
            vbo = self._vertex_buffer_object.get_vertex_buffer_object()
            if self._color_buffer_object is not None:
                cbo = self._color_buffer_object.get_color_buffer_object()
            else:
                cbo = None
            if self._index_buffer_object is not None:
                ibo = self._index_buffer_object.get_index_buffer_object()
            else:
                ibo = None

            self._vao = Registry.context.vertex_array(
            program,
            [
                (vbo, *self._vertex_buffer_shader_attributes),
                (cbo, *self._color_buffer_shader_attributes)],
            index_buffer=ibo,
            index_element_size=self._index_element_size)

    def render(self, mode=_moderngl.TRIANGLES, allow_shaders_to_adjust_point_size=True):
        if self._vao is not None:
            if allow_shaders_to_adjust_point_size:
                Registry.context.enable(_moderngl.PROGRAM_POINT_SIZE)
            self._vao.render(mode=mode)
            if allow_shaders_to_adjust_point_size:
                Registry.context.disable(_moderngl.PROGRAM_POINT_SIZE)

    def get_vertex_array_object(self):
        return self._vao

    def get_program(self):
        return self._program

    def get_vertex_buffer_object(self):
        return self._vertex_buffer_object

    def get_vertex_buffer_shader_attributes(self):
        return self._vertex_buffer_shader_attributes

    def get_color_buffer_object(self):
        return self._color_buffer_object

    def get_color_buffer_shader_attributes(self):
        return self._color_buffer_shader_attributes

    def get_index_buffer_object(self):
        return self._index_buffer_object

    def get_element_size(self):
        return self._index_element_size

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._vao is not None:
                self._vao.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Shader:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._program = None
        self._program_data = {"vertex": None, "fragment": None}

    def load_vertex_shader_from_file(self, file_path):
        with open(file_path, "r") as file:
            self._program_data["vertex"] = file.read()

    def load_fragment_shader_from_file(self, file_path):
        with open(file_path, "r") as file:
            self._program_data["fragment"] = file.read()

    def load_vertex_shader_from_string(self, string):
        self._program_data["vertex"] = string

    def load_fragment_shader_from_string(self, string):
        self._program_data["fragment"] = string

    def load_shader_from_string(self, vertex_string, fragment_shader):
        self._program_data["vertex"] = vertex_string
        self._program_data["fragment"] = fragment_shader

    def load_shader_from_folder(self, directory):
        if _os.path.exists(_path_builder(directory, "vertex.glsl")):
            with open(_path_builder(directory, "vertex.glsl"), "r") as file:
                vertex_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "vert.glsl")):
            with open(_path_builder(directory, "vert.glsl"), "r") as file:
                vertex_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "vertex_shader.glsl")):
            with open(_path_builder(directory, "vertex_shader.glsl"), "r") as file:
                vertex_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "vert_shader.glsl")):
            with open(_path_builder(directory, "vert_shader.glsl"), "r") as file:
                vertex_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "vertex shader.glsl")):
            with open(_path_builder(directory, "vertex shader.glsl"), "r") as file:
                vertex_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "vert shader.glsl")):
            with open(_path_builder(directory, "vert shader.glsl"), "r") as file:
                vertex_shader = file.read()

        if _os.path.exists(_path_builder(directory, "fragment.glsl")):
            with open(_path_builder(directory, "fragment.glsl"), "r") as file:
                fragment_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "frag.glsl")):
            with open(_path_builder(directory, "frag.glsl"), "r") as file:
                fragment_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "fragment_shader.glsl")):
            with open(_path_builder(directory, "fragment_shader.glsl"), "r") as file:
                fragment_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "frag_shader.glsl")):
            with open(_path_builder(directory, "frag_shader.glsl"), "r") as file:
                fragment_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "fragment shader.glsl")):
            with open(_path_builder(directory, "fragment shader.glsl"), "r") as file:
                fragment_shader = file.read()
        elif _os.path.exists(_path_builder(directory, "frag shader.glsl")):
            with open(_path_builder(directory, "frag shader.glsl"), "r") as file:
                fragment_shader = file.read()

        if vertex_shader is None or fragment_shader is None:
            log_warning("Vertex shader or fragment shader not found.")
            raise Exception("Vertex shader or fragment shader not found.")

        self._program_data["vertex"] = vertex_shader
        self._program_data["fragment"] = fragment_shader

    def create(self):
        self._program = Registry.context.program(
            vertex_shader=self._program_data["vertex"],
            fragment_shader=self._program_data["fragment"])

    def recreate(self):
        if self._program is not None:
            self._program.release()

            self._program = Registry.context.program(
                vertex_shader=self._program_data["vertex"],
                fragment_shader=self._program_data["fragment"])

    def get_program(self):
        return self._program

    def get_vertex_shader(self):
        return self._program_data["vertex"]

    def get_fragment_shader(self):
        return self._program_data["fragment"]

    def get_program(self):
        return self._program

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._program is not None:
                self._program.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Texture:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._texture = None
        self._size = (None, None)
        self._components = None
        self._data = None
        self._scaling = None

    def create(self, size, data=None, components=Constants.RGB, scaling=_moderngl.LINEAR, x_scaling=None, y_scaling=None):
        self._size = size
        self._components = len(components)
        self._data = data
        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

        self._texture = Registry.context.texture(self._size, self._components, self._data)
        self._texture.filter = (self._scaling[0], self._scaling[1])

    def write(self, data):
        self._texture.write(data)

    def load_from_file(self, file_path, scaling=_moderngl.LINEAR, x_scaling=None, y_scaling=None):
        image = _Image.open(file_path)
        self._size = image.size
        self._components = len(image.mode)
        self._data = image.tobytes()
        image.close()

        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

        self._texture = Registry.context.texture(self._size, self._components, self._data)
        self._texture.filter = (self._scaling[0], self._scaling[1])

    def set_scaling(self, scaling=_moderngl.LINEAR, x_scaling=None, y_scaling=None):
        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

    def get_texture(self):
        return self._texture

    def use(self, location=0):
        if self._texture is not None:
            self._texture.use(location=location)

    def get_size(self):
        return self._size

    def get_components(self):
        return self._components

    def get_data(self):
        return self._data

    def build_mipmaps(self, base=0, max_level=1000):
        if self._texture is not None:
            self._texture.build_mipmaps(base=base, max_level=max_level)

    def recreate(self):
        if self._texture is not None:
            self._texture.release()

            self._texture = Registry.context.texture(self._size, self._components, self._data)
            self._texture.filter = (self._scaling[0], self._scaling[1])

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._texture is not None:
                self._texture.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class FrameBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        Registry.opengl_objects[self._unique_identifier] = self

        self._fbo = None
        self._color_attachments = None
        self._depth_attachment = None

    def create(self, color_attachments=None, depth_attachment=None):
        self._color_attachments = color_attachments
        self._depth_attachment = depth_attachment

        color_attachments = []
        for color_attachment in self._color_attachments:
            color_attachments.append(color_attachment.get_texture())

        self._fbo = Registry.context.framebuffer(
            color_attachments=color_attachments,
            depth_attachment=self._depth_attachment)

    def recreate(self):
        if self._fbo is not None:
            self._fbo.release()

            color_attachments = []
            for color_attachment in self._color_attachments:
                color_attachments.append(color_attachment.get_texture())

            self._fbo = Registry.context.framebuffer(
                color_attachments=color_attachments,
                depth_attachment=self._depth_attachment)

    def clear(self, color=None, depth=1.0, viewport=None):
        if color is None:
            color = (0.0, 0.0, 0.0, 0.0)
        elif len(color) == 3:
            color = (*color, 0.0)
        if self._fbo is not None:
            self._fbo.clear(color=color, depth=depth, viewport=viewport)

    def use(self):
        if self._fbo is not None:
            self._fbo.use()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._fbo is not None:
                self._fbo.release()
            del Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True