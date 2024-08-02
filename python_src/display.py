import os
import importlib
import io
import contextlib

import numpy
import moderngl

from pmma.python_src.surface import Surface
from pmma.python_src.opengl import OpenGL

import pmma.python_src.core as core
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Display:
    def __init__(self, display_mode=Constants.PYGAME):
        if Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            core.log_warning("Display object already exists")
            core.log_development("Some PMMA objects can only be initialized once. \
This is to avoid creating unexpected behavior.")
            raise Exception("Display object already exists")

        if display_mode == Constants.PYGAME:
            os.environ["SDL_VIDEO_CENTERED"] = "1"

            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                Registry.graphics_backend = importlib.import_module(display_mode)
            message = buffer.getvalue()
            if core.log_information(message) is False:
                print(message)

            Registry.graphics_backend.init()

        Registry.display_mode = display_mode
        if Registry.display_mode == Constants.PYGAME:
            self.clock = Registry.graphics_backend.time.Clock()

        self.fullscreen = None
        self.display_attributes = []
        self.vsync = True

        Registry.pmma_module_spine[Constants.DISPLAY_OBJECT] = self

    def destroy(self):
        Registry.pmma_module_spine[Constants.DISPLAY_OBJECT] = None

    def create(
            self,
            width,
            height,
            fullscreen=False,
            resizable=False,
            caption="PMMA Canvas",
            native_fullscreen=True,
            vsync=True,
            alpha=False):

        self.vsync = vsync
        if Registry.display_mode == Constants.PYGAME:
            flags = Registry.graphics_backend.OPENGL | Registry.graphics_backend.DOUBLEBUF
            if fullscreen:
                self.flags = flags | Registry.graphics_backend.FULLSCREEN | Registry.graphics_backend.NOFRAME
                if native_fullscreen:
                    width, height = 0, 0

            else:
                if resizable:
                    flags = flags | Registry.graphics_backend.RESIZABLE

            display_size = width, height
            self.display_attributes = [display_size, flags, self.vsync]
            self.display = Registry.graphics_backend.display.set_mode(
                display_size,
                flags,
                vsync=self.vsync)

            display_size = self.display.get_size()
            Registry.display_initialized = True
            OpenGL()
            self.pygame_surface = Surface()
            self.pygame_surface.create(*display_size, alpha=True)
            self.pygame_surface_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*display_size)
            self.two_dimension_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*display_size)
            self.two_dimension_frame_buffer = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_fbo(*display_size, texture=self.two_dimension_texture)
            self.three_dimension_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*display_size)
            self.three_dimension_frame_buffer = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_fbo(*display_size, texture=self.three_dimension_texture)
            combine_program = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_texture_aggregation_program()
            quad_vertices = numpy.array([
                # x, y, u, v
                -1.0, -1.0, 0.0, 0.0,
                1.0, -1.0, 1.0, 0.0,
                1.0,  1.0, 1.0, 1.0,
                -1.0,  1.0, 0.0, 1.0,
            ], dtype='f4')

            quad_indices = numpy.array([0, 1, 2, 0, 2, 3], dtype='i4')
            quad_vbo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vbo(quad_vertices)
            quad_ibo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_ibo(quad_indices)
            self.quad_vao = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vao(
                combine_program,
                quad_vbo,
                attributes=["in_vert", "in_uv"],
                index_buffer=quad_ibo)

            Registry.graphics_backend.display.set_caption(caption)
        else:
            raise NotImplementedError

    def set_caption(self, caption):
        Registry.graphics_backend.display.set_caption(caption)

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            if Registry.display_mode == Constants.PYGAME:
                self.surface = Registry.graphics_backend.display.set_mode(
                    (0, 0),
                    self.display_attributes[1],
                    vsync=self.display_attributes[2])
        else:
            if Registry.display_mode == Constants.PYGAME:
                self.surface = Registry.graphics_backend.display.set_mode(
                    self.display_attributes[0],
                    self.display_attributes[1],
                    vsync=self.display_attributes[2])


    def blit(self, content, position=[0, 0]):
        self.pygame_surface.blit(content, position)

    def get_size(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.display.get_size()
        else:
            raise NotImplementedError

    def get_height(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.display.get_height()
        else:
            raise NotImplementedError

    def get_width(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.display.get_width()
        else:
            raise NotImplementedError

    def clear(self, *args):
        if args == ():
            args = (0, 0, 0)
        if not (type(args[0]) == int or type(args[0]) == float):
            args = args[0]
        if Registry.display_mode == Constants.PYGAME:
            self.two_dimension_frame_buffer.use()
            self.two_dimension_frame_buffer.clear(*args[0:3], 0.0)
            self.three_dimension_frame_buffer.use()
            self.three_dimension_frame_buffer.clear(*args[0:3], 0.0)
            self.pygame_surface.clear(*args[0:3], 0.0)
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=None):
        if refresh_rate is None:
            if Registry.power_saving_mode:
                refresh_rate = 45
            else:
                refresh_rate = 60

        Registry.refresh_rate = refresh_rate
        if Registry.display_mode == Constants.PYGAME:
            byte_data = self.pygame_surface.to_string(flipped=True)
            Registry.pmma_module_spine[Constants.OPENGL_OBJECT].blit_image_to_texture(
                byte_data,
                self.pygame_surface_texture)

            Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_context().screen.use()
            Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_context().clear(
                0,
                0,
                0)

            self.two_dimension_texture.use(location=0)
            self.three_dimension_texture.use(location=1)
            self.pygame_surface_texture.use(location=2)
            aggregation_program = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_texture_aggregation_program().get()
            aggregation_program["texture2d"].value = 0
            aggregation_program["texture3d"].value = 1
            aggregation_program["pygame_texture"].value = 2
            self.quad_vao.render(moderngl.TRIANGLES)
            Registry.graphics_backend.display.flip()
            if refresh_rate > 0:
                self.clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.clock.get_fps()
        else:
            raise NotImplementedError

    def get_center(self, as_integer=True):
        if Registry.display_mode == Constants.PYGAME:
            if as_integer:
                return self.display.get_width() // 2, self.display.get_height() // 2
            return self.display.get_width() / 2, self.display.get_height() / 2
        else:
            raise NotImplementedError