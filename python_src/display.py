import os as _os
import gc as _gc
import time as _time

import numpy as _numpy
import moderngl as _moderngl
import pygame as _pygame
import pyglet as _pyglet

from pmma.python_src.surface import Surface as _Surface
from pmma.python_src.opengl import OpenGL as _OpenGL

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.color import Color as _Color

class Display:
    def __init__(self, display_mode=Constants.PYGAME):
        initialize(self, unique_instance=Constants.DISPLAY_OBJECT, add_to_pmma_module_spine=True)

        if display_mode == Constants.PYGAME:
            _os.environ["SDL_VIDEO_CENTERED"] = "1"

            if log_information(Registry.pygame_launch_message) is False:
                print(Registry.pygame_launch_message)

            _pygame.init()

        Registry.display_mode = display_mode
        if Registry.display_mode == Constants.PYGAME:
            self.clock = _pygame.time.Clock()

        self.fullscreen = None
        self.display_attributes = []
        self.vsync = True

        self.color_converter = _Color()

        self.display_creation_attributes = []

        self.quad_vertices = _numpy.array([
                # x, y, u, v
                -1.0, -1.0, 0.0, 0.0,
                1.0, -1.0, 1.0, 0.0,
                1.0,  1.0, 1.0, 1.0,
                -1.0,  1.0, 0.0, 1.0,
            ], dtype='f4')

        self.quad_indices = _numpy.array([0, 1, 2, 0, 2, 3], dtype='i4')

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if Registry.display_mode == Constants.PYGAME:
                _pygame.display.quit()
            del self
            del Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def destroy(self):
        Registry.pmma_module_spine[Constants.DISPLAY_OBJECT] = None

    def __setup_layers(self, size):
        self.pygame_surface = _Surface()
        self.pygame_surface.create(*size, alpha=True)
        self.pygame_surface_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*size)
        self.two_dimension_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*size)
        self.two_dimension_frame_buffer = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_fbo(*size, texture=self.two_dimension_texture)
        self.three_dimension_texture = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_texture(*size)
        self.three_dimension_frame_buffer = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_fbo(*size, texture=self.three_dimension_texture)

    def get_pygame_surface(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.pygame_surface

    def get_2D_hardware_accelerated_surface(self, set_to_be_used=True):
        if Registry.display_mode == Constants.PYGAME:
            if set_to_be_used:
                self.two_dimension_frame_buffer.get().use()
            return self.two_dimension_texture
        else:
            raise NotImplementedError

    def get_3D_hardware_accelerated_surface(self, set_to_be_used=True):
        if Registry.display_mode == Constants.PYGAME:
            if set_to_be_used:
                self.three_dimension_frame_buffer.get().use()
            return self.three_dimension_texture
        else:
            raise NotImplementedError

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
            flags = _pygame.OPENGL | _pygame.DOUBLEBUF
            if fullscreen:
                if width is None:
                    width = 0
                if height is None:
                    height = 0
                flags = flags | _pygame.FULLSCREEN | _pygame.NOFRAME
            else:
                if width is None:
                    width = 1280
                if height is None:
                    height = 720

            if resizable:
                flags = flags | _pygame.RESIZABLE

            self.flags = flags

            size = width, height
            self.display_attributes = [size, flags, self.vsync]

            self.display = _pygame.display.set_mode(
                size,
                flags,
                vsync=self.vsync)

            size = _pygame.display.get_window_size()
            Registry.display_initialized = True
            _OpenGL()

            self.__setup_layers(size)

            combine_program = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_texture_aggregation_program()

            quad_vbo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vbo(self.quad_vertices)
            quad_ibo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_ibo(self.quad_indices)
            self.quad_vao = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vao(
                combine_program,
                quad_vbo,
                attributes=["in_vert", "in_uv"],
                index_buffer=quad_ibo)

            _pygame.display.set_caption(str(caption))
        else:
            raise NotImplementedError

    def set_caption(self, caption):
        _pygame.display.set_caption(str(caption))

    def display_resize(self):
        size = _pygame.display.get_window_size()

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

            self.display = _pygame.display.set_mode(
                size,
                self.display_attributes[1],
                vsync=self.display_attributes[2])

        Registry.pmma_module_spine[Constants.EVENTS_OBJECT].display_needs_resize = True

    def blit(self, content, position=[0, 0]):
        self.pygame_surface.blit(content, position)

    def get_size(self):
        if Registry.display_mode == Constants.PYGAME:
            return _pygame.display.get_window_size()
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
        Registry.in_game_loop = True

        if args == () or args == (None,):
            args = (0, 0, 0)
        if not (type(args[0]) == int or type(args[0]) == float):
            args = args[0]

        self.color_converter.input_color(args)

        if Registry.display_mode == Constants.PYGAME:
            self.two_dimension_frame_buffer.get().use()
            self.two_dimension_frame_buffer.get().clear(*self.color_converter.output_color(format=Constants.SMALL_RGBA))
            self.three_dimension_frame_buffer.get().use()
            self.three_dimension_frame_buffer.get().clear(*self.color_converter.output_color(format=Constants.SMALL_RGBA))
            self.pygame_surface.clear(self.color_converter.output_color(format=Constants.RGBA))
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=None):
        Registry.in_game_loop = True

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
            Registry.context.clear(1, 0, 1)

            self.two_dimension_texture.get().use(location=0)
            self.three_dimension_texture.get().use(location=1)
            self.pygame_surface_texture.get().use(location=2)
            aggregation_program = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].get_texture_aggregation_program().get()
            aggregation_program["texture2d"].value = 0
            aggregation_program["texture3d"].value = 1
            aggregation_program["pygame_texture"].value = 2

            self.quad_vao.get().render(_moderngl.TRIANGLES)

            _pygame.display.flip()

            if Constants.EVENTS_OBJECT in Registry.pmma_module_spine.keys():
                if Registry.pmma_module_spine[Constants.EVENTS_OBJECT].display_needs_resize:
                    Registry.pmma_module_spine[Constants.EVENTS_OBJECT].display_needs_resize = False
                    self.display_resize()

            frame_rate = self.get_fps()
            if Registry.application_average_frame_rate["Samples"] == 0:
                Registry.application_average_frame_rate["Mean"] = frame_rate
                Registry.application_average_frame_rate["Samples"] = 1
            else:
                mean = Registry.application_average_frame_rate["Mean"] * Registry.application_average_frame_rate["Samples"]
                mean += frame_rate
                Registry.application_average_frame_rate["Samples"] += 1
                Registry.application_average_frame_rate["Mean"] = mean / Registry.application_average_frame_rate["Samples"]

            if refresh_rate > 0:
                self.clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Constants.PYGAME:
            _pygame.quit()
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