import os

from pmma.python_src.file import path_builder

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Shader:
    def __init__(self):
        if not Constants.OPENGL_OBJECT in Registry.pmma_module_spine.keys():
            log_warning("OpenGL object does not exist.")
            log_development("In rare cases PMMA objects can only be \
initialized after others. In this case you need to already have instantiated \
the 'OpenGL' class before instantiating this.")
            raise Exception("OpenGL object does not exist.")

        self.vertex_shader = None
        self.fragment_shader = None
        self.program = None

        self.attributes = []

        self.in_attributes = []
        self.out_attributes = []
        self.uniform_attributes = []

        Registry.pmma_object_instances[id(self)] = self
        self._shut_down = False

    def analyze(self):
        self.in_attributes = []
        self.out_attributes = []
        self.uniform_attributes = []

        vertex_shader = self.vertex_shader.replace(";", " ")
        for line in vertex_shader.split("\n"):
            if "in " in line:
                self.in_attributes.append(line.split(" ")[2])

    def get_out_attributes(self):
        return self.out_attributes

    def get_in_attributes(self):
        return self.in_attributes

    def get_uniform_attributes(self):
        return self.uniform_attributes

    def __del__(self):
        if self._shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self._shut_down = True

    def get(self):
        return self.program.get()

    def create_from_string(
            self,
            vertex_shader,
            fragment_shader):

        self.vertex_shader = vertex_shader
        self.fragment_shader = fragment_shader

        program = Registry.context.program(
            vertex_shader=self.vertex_shader,
            fragment_shader=self.fragment_shader)

        self.program = OpenGLObject(program)

        self.analyze()

    def create_from_file(
            self,
            vertex_shader_file,
            fragment_shader_file):

        with open(vertex_shader_file, "r") as file:
            vertex_shader = file.read()

        with open(fragment_shader_file, "r") as file:
            fragment_shader = file.read()

        self.create_from_string(vertex_shader, fragment_shader)

    def create_from_location(self, directory):
        vertex_shader = None
        fragment_shader = None
        if os.path.exists(path_builder(directory, "vertex.glsl")):
            with open(path_builder(directory, "vertex.glsl"), "r") as file:
                vertex_shader = file.read()
        elif os.path.exists(path_builder(directory, "vert.glsl")):
            with open(path_builder(directory, "vert.glsl"), "r") as file:
                vertex_shader = file.read()
        elif os.path.exists(path_builder(directory, "vertex_shader.glsl")):
            with open(path_builder(directory, "vertex_shader.glsl"), "r") as file:
                vertex_shader = file.read()
        elif os.path.exists(path_builder(directory, "vert_shader.glsl")):
            with open(path_builder(directory, "vert_shader.glsl"), "r") as file:
                vertex_shader = file.read()
        elif os.path.exists(path_builder(directory, "vertex shader.glsl")):
            with open(path_builder(directory, "vertex shader.glsl"), "r") as file:
                vertex_shader = file.read()
        elif os.path.exists(path_builder(directory, "vert shader.glsl")):
            with open(path_builder(directory, "vert shader.glsl"), "r") as file:
                vertex_shader = file.read()

        if os.path.exists(path_builder(directory, "fragment.glsl")):
            with open(path_builder(directory, "fragment.glsl"), "r") as file:
                fragment_shader = file.read()
        elif os.path.exists(path_builder(directory, "frag.glsl")):
            with open(path_builder(directory, "frag.glsl"), "r") as file:
                fragment_shader = file.read()
        elif os.path.exists(path_builder(directory, "fragment_shader.glsl")):
            with open(path_builder(directory, "fragment_shader.glsl"), "r") as file:
                fragment_shader = file.read()
        elif os.path.exists(path_builder(directory, "frag_shader.glsl")):
            with open(path_builder(directory, "frag_shader.glsl"), "r") as file:
                fragment_shader = file.read()
        elif os.path.exists(path_builder(directory, "fragment shader.glsl")):
            with open(path_builder(directory, "fragment shader.glsl"), "r") as file:
                fragment_shader = file.read()
        elif os.path.exists(path_builder(directory, "frag shader.glsl")):
            with open(path_builder(directory, "frag shader.glsl"), "r") as file:
                fragment_shader = file.read()

        if vertex_shader is None or fragment_shader is None:
            log_warning("Vertex shader or fragment shader not found.")
            raise Exception("Vertex shader or fragment shader not found.")

        else:
            self.create_from_string(vertex_shader, fragment_shader)