from moderngl import TRIANGLES as _moderngl__TRIANGLES
from moderngl import LINEAR as _moderngl__LINEAR

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class OpenGL:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._error_utils__module = _ModuleManager.import_module("pmma.python_src.utility.error_utils")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._logger = self._logging_utils__module.InternalLogger()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def _check_if_opengl_backend_initialized(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("OpenGL backend has not been initialized yet. This is \
most likely due to not having created a Display through PMMA. You must do this \
first if you want to be able to use these OpenGL functions.")

            raise self._error_utils__module.OpenGLNotYetInitializedError()

    def get_context(self):
        """
        🟩 **R** -
        """
        self._check_if_opengl_backend_initialized()
        return _Registry.context

    def blit_image_to_texture(self, image, texture):
        """
        🟩 **R** -
        """
        self._check_if_opengl_backend_initialized()
        texture.write(image)

class BufferObject:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._gc__module = _ModuleManager.import_module("gc")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._data_size = 0
        self._buffer_object = None

        self._logger = self._logging_utils__module.InternalLogger()

        self._reserve = 0
        self._dynamic = False

        self._reassign_to_vertex_array_object = False

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._data_size = 0

            if self._buffer_object is not None:
                self._buffer_object.release()

            del _Registry.opengl_objects[self._unique_identifier]

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def _update_buffer_object(self, data=None):
        """
        🟩 **R** -
        """
        if data is None:
            if self._buffer_object is not None:
                data = self._buffer_object.read()

        old_reserve = self._reserve

        self._reserve = max(self._reserve, self._data_size)

        if data is not None:
            reserve = 0
        else:
            reserve = self._reserve

        if self._buffer_object is None:
            self._buffer_object = _Registry.context.buffer(data, dynamic=self._dynamic, reserve=reserve)
            self._reassign_to_vertex_array_object = True
        else:
            if old_reserve != self._reserve:
                self._buffer_object.release()
                self._gc__module.collect()
                self._buffer_object = _Registry.context.buffer(data, dynamic=self._dynamic, reserve=reserve)
                self._reassign_to_vertex_array_object = True
            else:
                self._buffer_object.clear()
                self._buffer_object.write(data)

    def get_buffer_object(self):
        """
        🟩 **R** -
        """
        return self._buffer_object

    def has_data(self):
        """
        🟩 **R** -
        """
        return self._data_size > 0

    def set_data(self, data):
        """
        🟩 **R** -
        """
        self._data_size = data.nbytes
        self._update_buffer_object(data=data)

    def get_data(self):
        """
        🟩 **R** -
        """
        if self._buffer_object is not None:
            return self._buffer_object.read()

    def set_dynamic(self, dynamic):
        """
        🟩 **R** -
        """
        self._dynamic = dynamic

        if self._buffer_object is not None:
            self._update_buffer_object()

    def get_dynamic(self):
        """
        🟩 **R** -
        """
        return self._dynamic

    def set_reserve(self, reserve):
        """
        🟩 **R** -
        """
        self._reserve = reserve

        self._reserve = max(self._reserve, self._data_size)
        self._update_buffer_object()

    def get_reserve(self):
        """
        🟩 **R** -
        """
        return self._reserve

    def get_data(self):
        """
        🟩 **R** -
        """
        return self._data

    def clear(self):
        """
        🟩 **R** -
        """
        self._data_size = 0
        if self._buffer_object is not None:
            self._buffer_object.clear()

    def bind_to_uniform_block(self, binding):
        """
        🟩 **R** -
        """
        if self._buffer_object is not None:
            self._buffer_object.bind_to_uniform_block(binding)

    def bind_to_shader_storage_buffer(self, binding):
        """
        🟩 **R** -
        """
        if self._buffer_object is not None:
            self._buffer_object.bind_to_storage_buffer(binding)

class GenericBufferObject(BufferObject):
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

class VertexBufferObject(BufferObject):
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

class IndexBufferObject(BufferObject):
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

class ColorBufferObject(BufferObject):
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

class VertexArrayObject:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._gc__module = _ModuleManager.import_module("gc")

        self._moderngl__module = _ModuleManager.import_module("moderngl")

        self._error_utils__module = _ModuleManager.import_module("pmma.python_src.utility.error_utils")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

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

        self._logger = self._logging_utils__module.InternalLogger()

    def _analyse_and_filter_buffer_attributes(self, attributes):
        """
        🟩 **R** -
        """
        if not (type(attributes) is list or type(attributes) is tuple):
            self._logger.log_development("Your buffer shader attributes must always be \
an array of 2 or more components, specifying the data type and shader value that each element in the \
vertex buffer object the GLSL shader will use. For example: [data_type, variable_name] or ['3f', 'in_position']")
            raise self._error_utils__module.UnexpectedBufferAttributeFormatError()

        filtered_data_types = ""
        filtered_variable_names = []
        program_buffer_inputs = self._program.get_buffer_input_variable_names()

        if " " in attributes[0]: # ModernGL style [all data types, variable name 1, variable name 2 ...]
            split_data_type_attributes = attributes[0].split(" ") # gets data types
            for data_type in split_data_type_attributes:
                if data_type.lower() in _Constants.DATA_INTERPRETATIONS:
                    filtered_data_types += data_type.lower() + " "
                else:
                    self._logger.log_development(f"Unexpected data type found in buffer attribute analysis. \
It must be one of the following formats: {','.join(_Constants.DATA_COLLECTION_METHODS)}.") # fine to use f string here, as constant
                    raise self._error_utils__module.UnknownDataTypeError
            filtered_data_types = filtered_data_types.strip()
        else: # PMMA style [data type 1, variable name 1, data type 2, variable name 2 ...]
            if attributes[0].lower() in _Constants.DATA_INTERPRETATIONS:
                variable_position = 0
            else:
                variable_position = 1
            for attribute_index in range(len(attributes)):
                if attribute_index % 2 == variable_position:
                    if attributes[attribute_index].lower() in _Constants.DATA_INTERPRETATIONS:
                        filtered_data_types += attributes[attribute_index].lower() + " "
                    else:
                        self._logger.log_development(f"Unexpected data type found in buffer attribute analysis. \
It must be one of the following formats: {','.join(_Constants.DATA_COLLECTION_METHODS)}.") # fine to use f string here, as constant
                        raise self._error_utils__module.UnknownDataTypeError()
                else:
                    if attributes[attribute_index] in program_buffer_inputs:
                        filtered_variable_names.append(attributes[attribute_index]) # check this against shader inputs l8r
                    else:
                        self._logger.log_development("You attempted to assign a buffer object to a variable in \
your shader that doesn't exist. The available shader buffer inputs that you can write to are: {}", variables=[program_buffer_inputs])
                        raise self._error_utils__module.UnexpectedBufferAttributeError()

            filtered_data_types = filtered_data_types.strip()

        if len(filtered_data_types.split(" ")) != len(filtered_variable_names):
            self._logger.log_development("It appears you are missing either a data type, or a variable \
name in your buffer attributes. Remember, each buffer attribute must have its own data type and variable name.")

        return [filtered_data_types, *filtered_variable_names]

    def create(
            self,
            program,
            vertex_buffer_object,
            vertex_buffer_shader_attributes,
            color_buffer_object=None,
            color_buffer_shader_attributes=[],
            index_buffer_object=None,
            index_element_size=4,
            additional_buffers=[],
            additional_buffer_attributes=[]):
        """
        🟩 **R** -
        """

        if program is None:
            raise ValueError("Program cannot be None")
        if program.get_created() is False:
            program.create()

        self._program = program

        if vertex_buffer_object is None:
            raise ValueError("Vertex buffer object cannot be None")
        if vertex_buffer_object.has_data() is False:
            raise ValueError("Vertex buffer object has no data")

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

    def _reassociate_buffers(self):
        """
        🟩 **R** -
        """
        if self._vao is not None:
            self._vao.release()

            self._gc__module.collect()

            program = self._program.use_program()

            if self._index_buffer_object is not None:
                ibo = self._index_buffer_object.get_buffer_object()
            else:
                ibo = None

            buffer_passthrough = [
                (self._vertex_buffer_object.get_buffer_object(), *self._vertex_buffer_shader_attributes)]

            for buffer_count in range(len(self._additional_buffers)):
                buffer_passthrough.append((self._additional_buffers[buffer_count].get_buffer_object(), *self._additional_buffer_attributes[buffer_count]))

            self._vao = _Registry.context.vertex_array(
                program,
                buffer_passthrough,
                index_buffer=ibo,
                index_element_size=self._index_element_size)

    def render_wire_frame(self):
        """
        🟩 **R** -
        """
        if self._vao is not None:
            self._vao.render(mode=self._moderngl__module.LINE_LOOP)

    def render(self, mode=_moderngl__TRIANGLES, allow_shaders_to_adjust_point_size=True):
        """
        🟩 **R** -
        """
        if self._vao is not None:
            if self._vertex_buffer_object._reassign_to_vertex_array_object:
                self._reassociate_buffers()
                self._vertex_buffer_object._reassign_to_vertex_array_object = False
            if self._index_buffer_object is not None:
                if self._index_buffer_object._reassign_to_vertex_array_object:
                    self._reassociate_buffers()
                    self._index_buffer_object._reassign_to_vertex_array_object = False

            self._program.use_program()
            if allow_shaders_to_adjust_point_size and mode == self._moderngl__module.POINTS:
                if self._program.get_using_gl_point_size_syntax():
                    _Registry.context.enable(self._moderngl__module.PROGRAM_POINT_SIZE)
                    self._logger.log_development("We have automatically detected that you want to \
render points with their size individually specified in your shader. By default this isn't enabled \
in OpenGL, but we have enabled it here so you don't have to. This behavior can be controlled \
using the `allow_shaders_to_adjust_point_size` keyword argument.")

            self._vao.render(mode=mode)
            if allow_shaders_to_adjust_point_size and mode == self._moderngl__module.POINTS:
                if self._program.get_using_gl_point_size_syntax():
                    _Registry.context.disable(self._moderngl__module.PROGRAM_POINT_SIZE)

    def get_vertex_array_object(self):
        """
        🟩 **R** -
        """
        return self._vao

    def get_program(self):
        """
        🟩 **R** -
        """
        return self._program

    def get_vertex_buffer_object(self):
        """
        🟩 **R** -
        """
        return self._vertex_buffer_object

    def get_vertex_buffer_shader_attributes(self):
        """
        🟩 **R** -
        """
        return self._vertex_buffer_shader_attributes

    def get_additional_buffers(self):
        """
        🟩 **R** -
        """
        return self._additional_buffers

    def get_additional_buffer_attributes(self):
        """
        🟩 **R** -
        """
        return self._additional_buffer_attributes

    def get_index_buffer_object(self):
        """
        🟩 **R** -
        """
        return self._index_buffer_object

    def get_element_size(self):
        """
        🟩 **R** -
        """
        return self._index_element_size

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._created = False
            if self._vao is not None:
                self._vao.release()
            del _Registry.opengl_objects[self._unique_identifier]

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def get_created(self):
        """
        🟩 **R** -
        """
        return self._created

class Shader:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._numpy__module = _ModuleManager.import_module("numpy")
        self._os__module = _ModuleManager.import_module("os")

        self._file__module = _ModuleManager.import_module("pmma.python_src.file")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._shader_utils__module = _ModuleManager.import_module("pmma.python_src.utility.shader_utils")

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._program = None
        self._program_data = {"vertex": None, "fragment": None}

        self._created = False

        self._logger = self._logging_utils__module.InternalLogger()

        self._uniform_values = {}
        self._buffer_input_variable_names = []
        self._using_gl_point_size_syntax = False
        self._shader_manager = self._shader_utils__module.ShaderManager()
        self._shader_loaded_from_directory = None

    def get_buffer_input_variable_names(self):
        """
        🟩 **R** -
        """
        return self._buffer_input_variable_names

    def _analyze_shader_component(self, file_data):
        """
        🟩 **R** -
        """
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
            self._uniform_values[name] = {"value": None, "updated": False}

    def get_using_gl_point_size_syntax(self):
        """
        🟩 **R** -
        """
        return self._using_gl_point_size_syntax

    def set_shader_variable(self, name, value):
        """
        🟩 **R** -
        """
        if name in self._uniform_values:
            if self._uniform_values[name]["value"] is None:
                self._uniform_values[name] = {"value": value, "updated": True}
                return

            if type(value) == self._numpy__module.ndarray and type(self._uniform_values[name]["value"]) == self._numpy__module.ndarray:
                if self._numpy__module.array_equal(value, self._uniform_values[name]["value"]) is False:
                    self._uniform_values[name] = {"value": value, "updated": True}
                return

            if self._uniform_values[name]["value"] != value:
                self._uniform_values[name] = {"value": value, "updated": True}
                return
        else:
            raise ValueError(f"Uniform '{name}' not found in the shader")

    def get_shader_variable(self, name):
        """
        🟩 **R** -
        """
        if name in self._uniform_values:
            return self._uniform_values[name]["value"]
        else:
            raise ValueError(f"Uniform '{name}' not found in the shader")

    def analyze(self):
        """
        🟩 **R** -
        """
        if self._program_data["vertex"] is not None:
            self._analyze_shader_component(self._program_data["vertex"].split("\n"))
        if self._program_data["fragment"] is not None:
            self._analyze_shader_component(self._program_data["fragment"].split("\n"))

    def load_vertex_shader_from_file(self, file_path):
        """
        🟩 **R** -
        """
        with open(file_path, "r") as file:
            self._program_data["vertex"] = file.read()
        self.analyze()

    def load_fragment_shader_from_file(self, file_path):
        """
        🟩 **R** -
        """
        with open(file_path, "r") as file:
            self._program_data["fragment"] = file.read()
        self.analyze()

    def load_vertex_shader_from_string(self, string):
        """
        🟩 **R** -
        """
        self._program_data["vertex"] = string
        self.analyze()

    def load_fragment_shader_from_string(self, string):
        """
        🟩 **R** -
        """
        self._program_data["fragment"] = string
        self.analyze()

    def load_shader_from_string(self, vertex_string, fragment_shader):
        """
        🟩 **R** -
        """
        self._program_data["vertex"] = vertex_string
        self._program_data["fragment"] = fragment_shader
        self.analyze()

    def load_shader_from_folder(self, directory):
        """
        🟩 **R** -
        """
        vertex_aliases = ["vertex", "vert", "vertex_shader", "vert_shader", "vertex shader", "vert shader"]
        vertex_shader = None
        fragment_aliases = ["fragment", "frag", "fragment_shader", "frag_shader", "fragment shader", "frag shader"]
        fragment_shader = None
        self._uniform_values = {}
        self._using_gl_point_size_syntax = False
        self._buffer_input_variable_names = []

        if self._shader_loaded_from_directory is not None:
            self._shader_manager.remove_shader_from_memory(self._shader_loaded_from_directory)

        if self._shader_manager.check_if_shader_exists(directory):
            self._program_data["vertex"], self._program_data["fragment"], self._using_gl_point_size_syntax, self._uniform_values, self._buffer_input_variable_names = self._shader_manager.get_shader(directory)

        else:
            loaded_from_file = False
            for name in vertex_aliases:
                path = self._file__module.path_builder(directory, f"{name}.glsl")
                shader_exists = self._shader_manager.check_if_shader_exists(directory, shader_type=_Constants.VERTEX_ONLY)
                if shader_exists or self._os__module.path.exists(path):
                    if shader_exists:
                        vertex_shader, using_gl_point_size_syntax, uniform_values, buffer_names = self._shader_manager.get_shader(directory, shader_type=_Constants.VERTEX_ONLY)
                        self._using_gl_point_size_syntax = self._using_gl_point_size_syntax or using_gl_point_size_syntax
                        self._buffer_input_variable_names.extend(buffer_names)
                        for key in uniform_values:
                            if key not in self._uniform_values:
                                self._uniform_values[key] = uniform_values[key]
                    else:
                        with open(path, "r") as file:
                            vertex_shader = file.read()
                        loaded_from_file = True
                    break

            for name in fragment_aliases:
                path = self._file__module.path_builder(directory, f"{name}.glsl")
                shader_exists = self._shader_manager.check_if_shader_exists(directory, shader_type=_Constants.FRAGMENT_ONLY)
                if shader_exists or self._os__module.path.exists(path):
                    if shader_exists:
                        fragment_shader, using_gl_point_size_syntax, uniform_values, buffer_names = self._shader_manager.get_shader(directory, shader_type=_Constants.FRAGMENT_ONLY)
                        self._using_gl_point_size_syntax = self._using_gl_point_size_syntax or using_gl_point_size_syntax
                        self._buffer_input_variable_names.extend(buffer_names)
                        for key in uniform_values:
                            if key not in self._uniform_values:
                                self._uniform_values[key] = uniform_values[key]
                    else:
                        with open(path, "r") as file:
                            fragment_shader = file.read()
                        loaded_from_file = True
                    break

            if vertex_shader is None:
                self._logger.log_warning("Vertex shader not found.")
                raise Exception("Vertex shader not found.")
            if fragment_shader is None:
                self._logger.log_warning("Fragment shader not found.")
                raise Exception("Fragment shader not found.")

            self._program_data["vertex"] = vertex_shader
            self._program_data["fragment"] = fragment_shader
            if loaded_from_file:
                self.analyze()

            self._shader_manager.add_shader_from_file(directory, vertex=vertex_shader, fragment=fragment_shader, using_gl_point_size_syntax=self._using_gl_point_size_syntax, uniform_values=self._uniform_values, buffer_names=self._buffer_input_variable_names)

        self._shader_loaded_from_directory = directory

    def create(self):
        """
        🟩 **R** -
        """
        self._program = _Registry.context.program(
            vertex_shader=self._program_data["vertex"],
            fragment_shader=self._program_data["fragment"])
        self._created = True

    def get_program(self):
        """
        🟩 **R** -
        """
        return self._program

    def use_program(self):
        """
        🟩 **R** -
        """
        for key in self._uniform_values:
            if self._uniform_values[key]["value"] is not None:
                data = self._uniform_values[key]
                if data["updated"]:
                    if isinstance(data["value"], (float, int, tuple, list)):
                        self._program[key].value = data["value"]
                    elif isinstance(data["value"], (bytes, bytearray, self._numpy__module.ndarray)):
                        self._program[key].write(data["value"])
                    else:
                        raise TypeError("Invalid data type for uniform variable")
                    self._uniform_values[key]["updated"] = False
        return self._program

    def get_vertex_shader(self):
        """
        🟩 **R** -
        """
        return self._program_data["vertex"]

    def get_fragment_shader(self):
        """
        🟩 **R** -
        """
        return self._program_data["fragment"]

    def get_program(self):
        """
        🟩 **R** -
        """
        return self._program

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._created = False
            if self._shader_loaded_from_directory is not None:
                self._shader_manager.remove_shader_from_memory(self._shader_loaded_from_directory)
            if self._program is not None:
                self._program.release()
            del _Registry.opengl_objects[self._unique_identifier]

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def get_created(self):
        """
        🟩 **R** -
        """
        return self._created

class Texture:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._opengl_utils__module = _ModuleManager.import_module("pmma.python_src.utility.opengl_utils")

        self._internal_texture = self._opengl_utils__module.Texture()

    def create(
            self,
            size,
            data=None,
            components=_Constants.RGB,
            scaling=_moderngl__LINEAR,
            x_scaling=None,
            y_scaling=None,
            samples=None):
        """
        🟩 **R** -
        """
        self._internal_texture.create(
            size,
            data=data,
            components=components,
            scaling=scaling,
            x_scaling=x_scaling,
            y_scaling=y_scaling,
            samples=samples,
            internal=False)

    def write(self, data):
        """
        🟩 **R** -
        """
        self._internal_texture.write(data)

    def load_texture(self, file_path, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None):
        """
        🟩 **R** -
        """
        self._internal_texture.load_from_file(file_path, scaling=scaling, x_scaling=x_scaling, y_scaling=y_scaling)

    def set_scaling(self, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None):
        """
        🟩 **R** -
        """
        self._internal_texture.set_scaling(scaling=scaling, x_scaling=x_scaling, y_scaling=y_scaling)

    def get_samples(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_samples()

    def get_intended_samples(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_intended_samples()

    def texture_to_PIL_image(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.texture_to_PIL_image()

    def get_texture(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_texture()

    def use(self, location=0):
        """
        🟩 **R** -
        """
        self._internal_texture.use(location=location)

    def get_size(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_size()

    def get_components(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_components()

    def get_data(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_data()

    def build_mipmaps(self, base=0, max_level=1000):
        """
        🟩 **R** -
        """
        self._internal_texture.build_mipmaps(base=base, max_level=max_level)

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._internal_texture.quit()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def get_created(self):
        """
        🟩 **R** -
        """
        return self._internal_texture.get_created()

class FrameBufferObject:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._fbo = None
        self._created = False
        self._color_attachments = None
        self._depth_attachment = None

    def create(self, color_attachments=None, depth_attachment=None):
        """
        🟩 **R** -
        """
        self._color_attachments = color_attachments
        self._depth_attachment = depth_attachment

        color_attachments = []
        for color_attachment in self._color_attachments:
            color_attachments.append(color_attachment.get_texture())

        self._fbo = _Registry.context.framebuffer(
            color_attachments=color_attachments,
            depth_attachment=self._depth_attachment)
        self._created = True

    def clear(self, color=None, depth=1.0, viewport=None):
        """
        🟩 **R** -
        """
        if color is None:
            color = (0.0, 0.0, 0.0, 0.0)
        elif type(color) == self._number_converter__module.ColorConverter:
            color = color.get_color(_Constants.SMALL_RGBA)
        elif len(color) == 3:
            color = (*color, 0.0)
        if self._fbo is not None:
            self._fbo.clear(color=color, depth=depth, viewport=viewport)

    def use(self):
        """
        🟩 **R** -
        """
        if self._fbo is not None:
            self._fbo.use()

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._created = False
            if self._fbo is not None:
                self._fbo.release()
            del _Registry.opengl_objects[self._unique_identifier]

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def get_created(self):
        """
        🟩 **R** -
        """
        return self._created