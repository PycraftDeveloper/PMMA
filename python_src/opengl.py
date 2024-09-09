import gc as _gc
import os as _os

import moderngl as _moderngl
from PIL import Image as _Image
import numpy as _numpy

from pmma.python_src.constants import Constants
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.number_converter import ColorConverter as _ColorConverter

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.error_utils import *
from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.shader_utils import ShaderIntermediary as _ShaderIntermediary

class OpenGL:
    def __init__(self):
        _initialize(self)

        self._logger = _InternalLogger()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _check_if_opengl_backend_initialized(self):
        if _Registry.display_initialized is False:
            self._logger.log_development("OpenGL backend has not been initialized yet. This is \
most likely due to not having created a Display through PMMA. You must do this \
first if you want to be able to use these OpenGL functions.")

            raise OpenGLNotYetInitializedError()

    def get_context(self):
        self._check_if_opengl_backend_initialized()
        return _Registry.context

    def blit_image_to_texture(self, image, texture):
        self._check_if_opengl_backend_initialized()
        texture.write(image)

class VertexBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._vbo = None

        self._created = False

        self._logger = _InternalLogger()

    def create(self, data, dynamic=False, reserve=0):
        if type(data) == list or type(data) == tuple:
            data = _numpy.array(data, dtype=_numpy.float32)
            self._logger.log_development("Converting list or tuple to numpy array for compatibility \
with OpenGL. The data you submit to this 'create' method should be in a 'C-Like' format. A great \
example of a 'C-Like' format would be a numpy array. Theoretically this conversion process should \
work fine, however can be an 'inefficient' representation of the data it contains as we air on the \
side of caution when it is created, effectively meaning it might use up more memory than absolutely \
required. If however you see this message and encounter strange rendering behavior, this should always \
be the first issue you address - it might not fix the problem, but there is a good chance it might.")

        self._data = data
        self._vbo = _Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)
        self._created = True

    def recreate(self):
        if self._vbo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._vbo.release()

            if self._data is None:
                self._vbo = _Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._vbo = _Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._vbo is None:
            self.create(data)
            return

        self._data = data
        self._vbo.clear()
        self._vbo.write(self._data)

    def read(self, from_vbo=False):
        if from_vbo:
            return self._data
        else:
            if self._vbo is not None:
                return self._vbo.read()

    def get_buffer_object(self):
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
        self._logger.log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_dynamic(self):
        if self._vbo is not None:
            return self._vbo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._vbo is not None:
                self._vbo.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class GenericBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._gbo = None

        self._created = False

        self._logger = _InternalLogger()

    def create(self, data, dynamic=False, reserve=0):
        self._data = data
        self._gbo = _Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)
        self._created = True

    def recreate(self):
        if self._gbo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._gbo.release()

            if self._data is None:
                self._gbo = _Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._gbo = _Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._gbo is None:
            self.create(data)
            return

        self._data = data
        self._gbo.clear()
        self._gbo.write(self._data)

    def read(self, from_gbo=False):
        if from_gbo:
            return self._data
        else:
            if self._gbo is not None:
                return self._gbo.read()

    def get_buffer_object(self):
        return self._gbo

    def clear(self):
        self._data = None
        if self._gbo is not None:
            self._gbo.clear()

    def bind_to_uniform_block(self, binding):
        if self._gbo is not None:
            self._gbo.bind_to_uniform_block(binding)

    def bind_to_shader_storage_buffer(self, binding):
        if self._gbo is not None:
            self._gbo.bind_to_storage_buffer(binding)

    def _size(self):
        if self._gbo is not None:
            return self._gbo.size

    def get_size(self):
        self._logger.log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_dynamic(self):
        if self._gbo is not None:
            return self._gbo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._gbo is not None:
                self._gbo.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class ColorBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._cbo = None

        self._created = False

        self._logger = _InternalLogger()

    def create(self, data, dynamic=False, reserve=0):
        self._data = data
        self._cbo = _Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)
        self._created = True

    def recreate(self):
        if self._cbo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._cbo.release()

            if self._data is None:
                self._cbo = _Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._cbo = _Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._cbo is None:
            self.create(data)
            return

        self._data = data
        self._cbo.clear()
        self._cbo.write(self._data)

    def read(self, from_vbo=False):
        if from_vbo:
            return self._data
        else:
            if self._cbo is not None:
                return self._cbo.read()

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
        self._logger.log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_buffer_object(self):
        return self._cbo

    def get_dynamic(self):
        if self._cbo is not None:
            return self._cbo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._cbo is not None:
                self._cbo.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class IndexBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._data = None
        self._ibo = None

        self._created = False

        self._logger = _InternalLogger()

    def create(self, data, dynamic=False, reserve=0):
        self._data = data
        self._ibo = _Registry.context.buffer(self._data, dynamic=dynamic, reserve=reserve)
        self._created = True

    def recreate(self):
        if self._ibo is not None:
            dynamic = self.get_dynamic()
            reserve = self._size()

            self._ibo.release()

            if self._data is None:
                self._ibo = _Registry.context.buffer(dynamic=dynamic, reserve=reserve)
            else:
                self._ibo = _Registry.context.buffer(self._data, dynamic=dynamic)

    def update(self, data):
        if self._ibo is None:
            self.create(data)
            return

        self._data = data
        self._ibo.clear()
        self._ibo.write(self._data)

    def read(self, from_vbo=False):
        if from_vbo:
            return self._data
        else:
            if self._ibo is not None:
                return self._ibo.read()

    def get_buffer_object(self):
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
        self._logger.log_development("Just as a point of clarification, this gets the size of the \
buffer, not the memory used to store it (either system memory or video memory)")
        return self._size()

    def get_dynamic(self):
        if self._ibo is not None:
            return self._ibo.dynamic

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._ibo is not None:
                self._ibo.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class VertexArrayObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._created = False

        self._vao = None
        self._program = None
        self._vertex_buffer_object = None
        self._vertex_buffer_shader_attributes = None
        self._index_buffer_object = None
        self._index_element_size = None
        self._additional_buffers = None
        self._additional_buffer_attributes = None

        self._logger = _InternalLogger()

    def _analyse_and_filter_buffer_attributes(self, attributes):
        if not (type(attributes) is list or type(attributes) is tuple):
            self._logger.log_development("Your buffer shader attributes must always be \
an array of 2 or more components, specifying the data type and shader value that each element in the \
vertex buffer object the GLSL shader will use. For example: [data_type, variable_name] or ['3f', 'in_position']")
            raise UnexpectedBufferAttributeFormatError()

        filtered_data_types = ""
        filtered_variable_names = []
        program_buffer_inputs = self._program.get_buffer_input_variable_names()

        if " " in attributes[0]: # ModernGL style [all data types, variable name 1, variable name 2 ...]
            split_data_type_attributes = attributes[0].split(" ") # gets data types
            for data_type in split_data_type_attributes:
                if data_type.lower() in Constants.DATA_INTERPRETATIONS:
                    filtered_data_types += data_type.lower() + " "
                else:
                    self._logger.log_development(f"Unexpected data type found in buffer attribute analysis. \
It must be one of the following formats: {','.join(Constants.DATA_COLLECTION_METHODS)}.") # fine to use f string here, as constant
                    raise UnknownDataTypeError
            filtered_data_types = filtered_data_types.strip()
        else: # PMMA style [data type 1, variable name 1, data type 2, variable name 2 ...]
            if attributes[0].lower() in Constants.DATA_INTERPRETATIONS:
                variable_position = 0
            else:
                variable_position = 1
            for attribute_index in range(len(attributes)):
                if attribute_index % 2 == variable_position:
                    if attributes[attribute_index].lower() in Constants.DATA_INTERPRETATIONS:
                        filtered_data_types += attributes[attribute_index].lower() + " "
                    else:
                        self._logger.log_development(f"Unexpected data type found in buffer attribute analysis. \
It must be one of the following formats: {','.join(Constants.DATA_COLLECTION_METHODS)}.") # fine to use f string here, as constant
                        raise UnknownDataTypeError()
                else:
                    if attributes[attribute_index] in program_buffer_inputs:
                        filtered_variable_names.append(attributes[attribute_index]) # check this against shader inputs l8r
                    else:
                        self._logger.log_development("You attempted to assign a buffer object to a variable in \
your shader that doesn't exist. The available shader buffer inputs that you can write to are: {}", variables=program_buffer_inputs)
                        raise UnexpectedBufferAttributeError()

            filtered_data_types = filtered_data_types.strip()

        if len(filtered_data_types.split(" ")) != len(filtered_variable_names):
            self._logger.log_development("It appears you are missing either a data type, or a variable \
name in your buffer attributes. Remember, each buffer attribute must have its own data type and variable name.")

        return [filtered_data_types, *filtered_variable_names]

    def create(self, program, vertex_buffer_object, vertex_buffer_shader_attributes, color_buffer_object=None, color_buffer_shader_attributes=[], index_buffer_object=None, index_element_size=4, additional_buffers=[], additional_buffer_attributes=[]):
        if program is None:
            raise ValueError("Program cannot be None")
        if program.get_created() is False:
            program.create()

        self._program = program

        if vertex_buffer_object is None:
            raise ValueError("Vertex buffer object cannot be None")
        if vertex_buffer_object.get_created() is False:
            raise ValueError("Vertex buffer object has not been created yet")

        self._vertex_buffer_object = vertex_buffer_object

        self._vertex_buffer_shader_attributes = self._analyse_and_filter_buffer_attributes(vertex_buffer_shader_attributes)
        self._index_buffer_object = index_buffer_object
        self._index_element_size = index_element_size

        if color_buffer_object is not None:
            additional_buffers = [color_buffer_object] + additional_buffers
            additional_buffer_attributes = [color_buffer_shader_attributes] + additional_buffer_attributes

        filtered_buffer_attributes = []
        for buffer_attribute in additional_buffer_attributes:
            filtered_buffer_attributes.append(self._analyse_and_filter_buffer_attributes(buffer_attribute))

        self._additional_buffers = additional_buffers
        self._additional_buffer_attributes = filtered_buffer_attributes

        if self._index_buffer_object is not None:
            ibo = self._index_buffer_object.get_buffer_object()
        else:
            ibo = None

        buffer_passthrough = [
                (vertex_buffer_object.get_buffer_object(), *self._vertex_buffer_shader_attributes)]

        for buffer_count in range(len(additional_buffers)):
            buffer_passthrough.append((additional_buffers[buffer_count].get_buffer_object(), *additional_buffer_attributes[buffer_count]))

        program = self._program.use_program()

        self._vao = _Registry.context.vertex_array(
            program,
            buffer_passthrough,
            index_buffer=ibo,
            index_element_size=self._index_element_size)
        self._created = True

    def recreate(self):
        if self._vao is not None:
            self._vao.release()

            self._program.recreate()
            self._vertex_buffer_object.recreate()

            if self._index_buffer_object is not None:
                self._index_buffer_object.recreate()
                ibo = self._index_buffer_object.get_buffer_object()
            else:
                ibo = None

            for buffer in self._additional_buffers:
                buffer.recreate()

            buffer_passthrough = [
                (self._vertex_buffer_object.get_buffer_object(), *self._vertex_buffer_shader_attributes)]

            for buffer_count in range(len(self._additional_buffers)):
                buffer_passthrough.append((self._additional_buffers[buffer_count].get_buffer_object(), *self._additional_buffer_attributes[buffer_count]))

            program = self._program.use_program()

            self._vao = _Registry.context.vertex_array(
            program,
            buffer_passthrough,
            index_buffer=ibo,
            index_element_size=self._index_element_size)

    def render_wire_frame(self):
        if self._vao is not None:
            self._vao.render(mode=_moderngl.LINE_LOOP)

    def render(self, mode=_moderngl.TRIANGLES, allow_shaders_to_adjust_point_size=True):
        if self._vao is not None:
            if allow_shaders_to_adjust_point_size and mode == _moderngl.POINTS:
                if self._program.get_using_gl_point_size_syntax():
                    _Registry.context.enable(_moderngl.PROGRAM_POINT_SIZE)
                    self._logger.log_development("We have automatically detected that you want to \
render points with their size individually specified in your shader. By default this isn't enabled \
in OpenGL, but we have enabled it here so you don't have to. This behavior can be controlled \
using the `allow_shaders_to_adjust_point_size` keyword argument.")

            self._vao.render(mode=mode)
            if allow_shaders_to_adjust_point_size and mode == _moderngl.POINTS:
                if self._program.get_using_gl_point_size_syntax():
                    _Registry.context.disable(_moderngl.PROGRAM_POINT_SIZE)

    def get_vertex_array_object(self):
        return self._vao

    def get_program(self):
        return self._program

    def get_vertex_buffer_object(self):
        return self._vertex_buffer_object

    def get_vertex_buffer_shader_attributes(self):
        return self._vertex_buffer_shader_attributes

    def get_additional_buffers(self):
        return self._additional_buffers

    def get_additional_buffer_attributes(self):
        return self._additional_buffer_attributes

    def get_index_buffer_object(self):
        return self._index_buffer_object

    def get_element_size(self):
        return self._index_element_size

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._vao is not None:
                self._vao.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class Shader:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._program = None
        self._program_data = {"vertex": None, "fragment": None}

        self._created = False

        self._logger = _InternalLogger()

        self._uniform_values = {}
        self._buffer_input_variable_names = []
        self._using_gl_point_size_syntax = False

    def get_buffer_input_variable_names(self):
        return self._buffer_input_variable_names

    def _analyze_shader_component(self, file_data):
        uniform_names = []
        self._using_gl_point_size_syntax = False

        # Parse file data for uniform declarations
        for line in file_data:
            if "uniform" in line:
                uniform_name = line.split(" ")[-1].strip().replace(";", "")
                uniform_names.append(uniform_name)
            elif "in " in line:
                buffer_input_variable_name = line.split(" ")[-1].strip().replace(";", "")
                self._buffer_input_variable_names.append(buffer_input_variable_name)

            if "gl_PointSize" in line:
                self._using_gl_point_size_syntax = True

        # Dynamically create getter and setter functions for each uniform
        for name in uniform_names:
            self._uniform_values[name] = None

    def get_using_gl_point_size_syntax(self):
        return self._using_gl_point_size_syntax

    def set_shader_variable(self, name, value):
        if name in self._uniform_values:
            self._uniform_values[name] = value
        else:
            raise ValueError(f"Uniform '{name}' not found in the shader")

    def get_shader_variable(self, name):
        if name in self._uniform_values:
            return self._uniform_values[name]
        else:
            raise ValueError(f"Uniform '{name}' not found in the shader")

    def analyze(self):
        if self._program_data["vertex"] is not None:
            self._analyze_shader_component(self._program_data["vertex"].split("\n"))
        if self._program_data["fragment"] is not None:
            self._analyze_shader_component(self._program_data["fragment"].split("\n"))

    def load_vertex_shader_from_file(self, file_path):
        if file_path in _ShaderIntermediary.loaded_shaders:
            if "vertex" in _ShaderIntermediary.loaded_shaders[file_path]:
                self._program_data["vertex"] = _ShaderIntermediary.loaded_shaders[file_path]["vertex"]
            else:
                with open(file_path, "r") as file:
                    self._program_data["vertex"] = file.read()
                _ShaderIntermediary.loaded_shaders[file_path]["vertex"] = self._program_data["vertex"]
        else:
            with open(file_path, "r") as file:
                self._program_data["vertex"] = file.read()
            _ShaderIntermediary.loaded_shaders[file_path] = {"vertex": self._program_data["vertex"]}
        self.analyze()

    def load_fragment_shader_from_file(self, file_path):
        if file_path in _ShaderIntermediary.loaded_shaders:
            if "fragment" in _ShaderIntermediary.loaded_shaders[file_path]:
                self._program_data["fragment"] = _ShaderIntermediary.loaded_shaders[file_path]["fragment"]
            else:
                with open(file_path, "r") as file:
                    self._program_data["fragment"] = file.read()
                _ShaderIntermediary.loaded_shaders[file_path]["fragment"] = self._program_data["fragment"]
        else:
            with open(file_path, "r") as file:
                self._program_data["fragment"] = file.read()
            _ShaderIntermediary.loaded_shaders[file_path] = {"fragment": self._program_data["fragment"]}
        self.analyze()

    def load_vertex_shader_from_string(self, string):
        self._program_data["vertex"] = string
        self.analyze()

    def load_fragment_shader_from_string(self, string):
        self._program_data["fragment"] = string
        self.analyze()

    def load_shader_from_string(self, vertex_string, fragment_shader):
        self._program_data["vertex"] = vertex_string
        self._program_data["fragment"] = fragment_shader
        self.analyze()

    def load_shader_from_folder(self, directory):
        vertex_aliases = ["vertex", "vert", "vertex_shader", "vert_shader", "vertex shader", "vert shader"]
        vertex_shader = None
        for name in vertex_aliases:
            path = _path_builder(directory, f"{name}.glsl")
            if path in _ShaderIntermediary.loaded_shaders or _os.path.exists(path):
                if path in _ShaderIntermediary.loaded_shaders:
                    if "vertex" in _ShaderIntermediary.loaded_shaders[path]:
                        vertex_shader = _ShaderIntermediary.loaded_shaders[path]["vertex"]
                    else:
                        with open(path, "r") as file:
                            vertex_shader = file.read()
                        _ShaderIntermediary.loaded_shaders[path]["vertex"] = vertex_shader
                else:
                    with open(path, "r") as file:
                        vertex_shader = file.read()
                    _ShaderIntermediary.loaded_shaders[path] = {"vertex": vertex_shader}

                break

        fragment_aliases = ["fragment", "frag", "fragment_shader", "frag_shader", "fragment shader", "frag shader"]
        fragment_shader = None
        for name in fragment_aliases:
            path = _path_builder(directory, f"{name}.glsl")
            if path in _ShaderIntermediary.loaded_shaders or _os.path.exists(path):
                if path in _ShaderIntermediary.loaded_shaders:
                    if "fragment" in _ShaderIntermediary.loaded_shaders[path]:
                        fragment_shader = _ShaderIntermediary.loaded_shaders[path]["fragment"]
                    else:
                        with open(path, "r") as file:
                            fragment_shader = file.read()
                        _ShaderIntermediary.loaded_shaders[path]["fragment"] = vertex_shader
                else:
                    with open(path, "r") as file:
                        fragment_shader = file.read()
                    _ShaderIntermediary.loaded_shaders[path] = {"fragment": fragment_shader}

                break

        if vertex_shader is None or fragment_shader is None:
            self._logger.log_warning("Vertex shader or fragment shader not found.")
            raise Exception("Vertex shader or fragment shader not found.")

        self._program_data["vertex"] = vertex_shader
        self._program_data["fragment"] = fragment_shader
        self.analyze()

    def create(self):
        self._program = _Registry.context.program(
            vertex_shader=self._program_data["vertex"],
            fragment_shader=self._program_data["fragment"])
        self._created = True

    def recreate(self):
        if self._program is not None:
            self._program.release()

            self._program = _Registry.context.program(
                vertex_shader=self._program_data["vertex"],
                fragment_shader=self._program_data["fragment"])

    def get_program(self):
        return self._program

    def use_program(self):
        for key in self._uniform_values:
            if self._uniform_values[key] is not None:
                self._program[key].value = self._uniform_values[key]
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
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class Texture:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._texture = None
        self._size = (None, None)
        self._components = None
        self._data = None
        self._scaling = None
        self._samples = None
        self._intended_samples = None

        self._created = False

        self._logger = _InternalLogger()

    def create(self, size, data=None, components=Constants.RGB, scaling=_moderngl.LINEAR, x_scaling=None, y_scaling=None, samples=None):
        self._size = size
        self._components = len(components)
        self._data = data

        if samples is None:
            samples = 0

        self._intended_samples = samples

        if samples != 0:
            self._logger.log_development("You are using an anti-aliased texture. Therefore, please \
make sure that you update your shader that uses this texture accordingly, otherwise you will \
encounter visual issues with that texture when you go to render something using it.")

        if samples > _Registry.context.max_samples:
            self._logger.log_development("The requested number of samples is greater than the maximum \
number of samples supported by your system. The maximum number of samples will be used instead. The \
maximum number of samples supported by your system is: {}", variables=[_Registry.context.max_samples])
            samples = _Registry.context.max_samples

        self._samples = samples

        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

        self._texture = _Registry.context.texture(self._size, self._components, self._data, samples=self._samples)
        self._texture.filter = (self._scaling[0], self._scaling[1])
        self._created = True

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

        self._texture = _Registry.context.texture(self._size, self._components, self._data)
        self._texture.filter = (self._scaling[0], self._scaling[1])

    def set_scaling(self, scaling=_moderngl.LINEAR, x_scaling=None, y_scaling=None):
        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

    def get_samples(self):
        return self._samples

    def get_intended_samples(self):
        return self._intended_samples

    def texture_to_PIL_image(self):
        if self._texture is not None:
            return _Image.frombytes("RGB", self._size, self._texture.read())

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

            self._texture = _Registry.context.texture(self._size, self._components, self._data, samples=self._samples)
            self._texture.filter = (self._scaling[0], self._scaling[1])

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._texture is not None:
                self._texture.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created

class FrameBufferObject:
    def __init__(self):
        _initialize(self)

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._fbo = None
        self._created = False
        self._color_attachments = None
        self._depth_attachment = None

    def create(self, color_attachments=None, depth_attachment=None):
        self._color_attachments = color_attachments
        self._depth_attachment = depth_attachment

        color_attachments = []
        for color_attachment in self._color_attachments:
            color_attachments.append(color_attachment.get_texture())

        self._fbo = _Registry.context.framebuffer(
            color_attachments=color_attachments,
            depth_attachment=self._depth_attachment)
        self._created = True

    def recreate(self):
        if self._fbo is not None:
            self._fbo.release()

            color_attachments = []
            for color_attachment in self._color_attachments:
                color_attachment.recreate()
                color_attachments.append(color_attachment.get_texture())

            self._fbo = _Registry.context.framebuffer(
                color_attachments=color_attachments,
                depth_attachment=self._depth_attachment)

    def clear(self, color=None, depth=1.0, viewport=None):
        if color is None:
            color = (0.0, 0.0, 0.0, 0.0)
        elif type(color) == _ColorConverter:
            color = color.get_color(Constants.SMALL_RGBA)
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
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created