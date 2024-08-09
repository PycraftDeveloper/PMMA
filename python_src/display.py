import os
import io
import contextlib

import numpy
import moderngl

buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    import pygame
pygame_initialization_message = buffer.getvalue()

import pyglet

from pmma.python_src.surface import Surface
from pmma.python_src.opengl import OpenGL

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Display:
    def __init__(self, display_mode=Constants.PYGAME):
        if Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            log_warning("Display object already exists")
            log_development("Some PMMA objects can only be initialized once. \
This is to avoid creating unexpected behavior.")
            raise Exception("Display object already exists")

        if display_mode == Constants.PYGAME:
            os.environ["SDL_VIDEO_CENTERED"] = "1"

            if log_information(pygame_initialization_message) is False:
                print(pygame_initialization_message)

            pygame.init()

        Registry.display_mode = display_mode
        if Registry.display_mode == Constants.PYGAME:
            self.clock = pygame.time.Clock()

        self.fullscreen = None
        self.display_attributes = []
        self.vsync = True

        self.display_creation_attributes = []

        self.quad_vertices = numpy.array([
                # x, y, u, v
                -1.0, -1.0, 0.0, 0.0,
                1.0, -1.0, 1.0, 0.0,
                1.0,  1.0, 1.0, 1.0,
                -1.0,  1.0, 0.0, 1.0,
            ], dtype='f4')

        self.quad_indices = numpy.array([0, 1, 2, 0, 2, 3], dtype='i4')

        Registry.pmma_module_spine[Constants.DISPLAY_OBJECT] = self

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def destroy(self):
        Registry.pmma_module_spine[Constants.DISPLAY_OBJECT] = None

    def __setup_layers(self, size):
        self.pygame_surface = Surface()
        self.pygame_surface.create(*size, alpha=True)
        self.pygame_surface_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*size)
        self.two_dimension_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*size)
        self.two_dimension_frame_buffer = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_fbo(*size, texture=self.two_dimension_texture)
        self.three_dimension_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*size)
        self.three_dimension_frame_buffer = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_fbo(*size, texture=self.three_dimension_texture)

    def create(
            self,
            width=None,
            height=None,
            fullscreen=True,
            resizable=False,
            caption="PMMA Display",
            vsync=True,
            alpha=False):

        self.vsync = vsync
        if Registry.display_mode == Constants.PYGAME:
            flags = pygame.OPENGL | pygame.DOUBLEBUF
            if fullscreen:
                if width is None:
                    width = 0
                if height is None:
                    height = 0
                flags = flags | pygame.FULLSCREEN | pygame.NOFRAME
            else:
                if width is None:
                    width = 1280
                if height is None:
                    height = 720

            if resizable:
                flags = flags | pygame.RESIZABLE

            self.flags = flags

            size = width, height
            self.display_attributes = [size, flags, self.vsync]

            self.display = pygame.display.set_mode(
                size,
                flags,
                vsync=self.vsync)

            size = pygame.display.get_window_size()
            Registry.display_initialized = True
            OpenGL()

            self.__setup_layers(size)

            combine_program = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_texture_aggregation_program()

            quad_vbo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vbo(self.quad_vertices)
            quad_ibo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_ibo(self.quad_indices)
            self.quad_vao = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vao(
                combine_program,
                quad_vbo,
                attributes=["in_vert", "in_uv"],
                index_buffer=quad_ibo)

            pygame.display.set_caption(str(caption))
        else:
            raise NotImplementedError

    def set_caption(self, caption):
        pygame.display.set_caption(str(caption))

    def display_resize(self):
        size = pygame.display.get_window_size()

        self.pygame_surface.quit()

        self.pygame_surface_texture.quit()
        self.two_dimension_texture.quit()
        self.two_dimension_frame_buffer.quit()
        self.three_dimension_texture.quit()
        self.three_dimension_frame_buffer.quit()

        self.__setup_layers(size)

        Registry.context.viewport = (0, 0, *size)

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if Registry.display_mode == Constants.PYGAME:
            if self.fullscreen:
                size = (0, 0)
            else:
                size = self.display_attributes[0]

            self.display = pygame.display.set_mode(
                size,
                self.display_attributes[1],
                vsync=self.display_attributes[2])

        Registry.pmma_module_spine[Constants.EVENTS_OBJECT].display_needs_resize = True

    def blit(self, content, position=[0, 0]):
        self.pygame_surface.blit(content, position)

    def get_size(self):
        if Registry.display_mode == Constants.PYGAME:
            return pygame.display.get_window_size()
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
            self.two_dimension_frame_buffer.get().use()
            self.two_dimension_frame_buffer.get().clear(*args[0:3], 0.0)
            self.three_dimension_frame_buffer.get().use()
            self.three_dimension_frame_buffer.get().clear(*args[0:3], 0.0)
            self.pygame_surface.clear(*args[0:3], 0.0)
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=None):
        if Registry.number_of_draw_calls != 0:
            log_warning("PMMA compute operation not called! Please call \
this function before ending the game loop with this!")
            log_development("PMMA compute operation not called! Calling \
this allows PMMA to perform more self-optimization and improve development \
messages. Please place this compute function 'pmma.compute()' just before \
this method call to ensure optimal performance and support!")

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

            Registry.context.screen.use()
            Registry.context.clear(0, 0, 0)

            self.two_dimension_texture.get().use(location=0)
            self.three_dimension_texture.get().use(location=1)
            self.pygame_surface_texture.get().use(location=2)
            aggregation_program = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_texture_aggregation_program().get()
            aggregation_program["texture2d"].value = 0
            aggregation_program["texture3d"].value = 1
            aggregation_program["pygame_texture"].value = 2
            self.quad_vao.get().render(moderngl.TRIANGLES)

            pygame.display.flip()

            if Constants.EVENTS_OBJECT in Registry.pmma_module_spine.keys():
                if Registry.pmma_module_spine[Constants.EVENTS_OBJECT].display_needs_resize:
                    Registry.pmma_module_spine[Constants.EVENTS_OBJECT].display_needs_resize = False
                    self.display_resize()

            if refresh_rate > 0:
                self.clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Constants.PYGAME:
            pygame.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.clock.get_fps()
        else:
            raise NotImplementedError

    def get_refresh_rate(self):
        return self.get_fps()

    def get_center(self, as_integer=True):
        if Registry.display_mode == Constants.PYGAME:
            if as_integer:
                return self.display.get_width() // 2, self.display.get_height() // 2
            return self.display.get_width() / 2, self.display.get_height() / 2
        else:
            raise NotImplementedError