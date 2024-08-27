import os as _os
import gc as _gc

import numpy as _numpy
import moderngl as _moderngl
import pygame as _pygame
import pyglet as _pyglet
from moderngl_window import geometry as _geometry
import moderngl_window as _moderngl_window

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.color import Color as _Color
from pmma.python_src.surface import Surface as _Surface
from pmma.python_src.opengl import OpenGL as _OpenGL

from pmma.python_src.utility.opengl_utils import OpenGLIntermediary as _OpenGLIntermediary

class Display:
    def __init__(self):
        initialize(self, unique_instance=Constants.DISPLAY_OBJECT, add_to_pmma_module_spine=True, requires_display_mode_set=True)

        if Registry.display_mode == Constants.PYGAME:
            self._clock = _pygame.time.Clock()

        self._fullscreen = None
        self._display_attributes = []
        self._vsync = True

        self._color_converter = _Color()

        self._display_creation_attributes = []

        self._display_quad = None

        self._opengl = _OpenGL()

        self._fill_color = None
        self._color_key = _numpy.array([0, 0, 0], dtype=_numpy.float32)

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
        self._pygame_surface = _Surface()
        self._pygame_surface.create(*size)
        self._pygame_surface_texture = self._opengl.create_texture(*size, color_format=Constants.RGB)
        self._two_dimension_texture = self._opengl.create_texture(*size)
        self._two_dimension_frame_buffer = self._opengl.create_fbo(*size, texture=self._two_dimension_texture)
        self._three_dimension_texture = self._opengl.create_texture(*size)
        self._three_dimension_frame_buffer = self._opengl.create_fbo(*size, texture=self._three_dimension_texture)

    def get_pygame_surface(self):
        if Registry.display_mode == Constants.PYGAME:
            return self._pygame_surface

    def get_2D_hardware_accelerated_surface(self, set_to_be_used=True):
        if Registry.display_mode == Constants.PYGAME:
            if set_to_be_used:
                self._two_dimension_frame_buffer.get().use()
            return self._two_dimension_frame_buffer
        else:
            raise NotImplementedError

    def get_3D_hardware_accelerated_surface(self, set_to_be_used=True):
        if Registry.display_mode == Constants.PYGAME:
            if set_to_be_used:
                self._three_dimension_frame_buffer.get().use()
            return self._three_dimension_frame_buffer
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

        self._vsync = vsync
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

            self._flags = flags

            size = width, height
            self._display_attributes = [size, flags, self._vsync]

            self._display = _pygame.display.set_mode(
                size,
                flags,
                vsync=self._vsync)

            size = _pygame.display.get_window_size()
            Registry.display_initialized = True
            Registry.window_context = _moderngl_window.get_local_window_cls("pygame2")

            _OpenGLIntermediary()

            self.__setup_layers(size)

            self._display_quad = _geometry.quad_fs()

            _pygame.display.set_caption(str(caption))
        else:
            raise NotImplementedError

    def set_caption(self, caption):
        _pygame.display.set_caption(str(caption))

    def display_resize(self):
        size = _pygame.display.get_window_size()

        self._pygame_surface.quit()

        self._pygame_surface_texture.quit()
        self._two_dimension_texture.quit()
        self._two_dimension_frame_buffer.quit()
        self._three_dimension_texture.quit()
        self._three_dimension_frame_buffer.quit()

        self.__setup_layers(size)

        Registry.context.viewport = (0, 0, *size)

    def toggle_fullscreen(self):
        self._fullscreen = not self._fullscreen
        if Registry.display_mode == Constants.PYGAME:
            if self._fullscreen:
                size = (0, 0)
            else:
                size = self._display_attributes[0]

            self._display = _pygame.display.set_mode(
                size,
                self._display_attributes[1],
                vsync=self._display_attributes[2])

        Registry.pmma_module_spine[Constants.EVENTS_OBJECT].set_display_needs_resize(True)

    def blit(self, content, position=[0, 0]):
        self._pygame_surface.blit(content, position)

    def get_size(self):
        if Registry.display_mode == Constants.PYGAME:
            return _pygame.display.get_window_size()
        else:
            raise NotImplementedError

    def get_height(self):
        if Registry.display_mode == Constants.PYGAME:
            return self._display.get_height()
        else:
            raise NotImplementedError

    def get_width(self):
        if Registry.display_mode == Constants.PYGAME:
            return self._display.get_width()
        else:
            raise NotImplementedError

    def clear(self, *args):
        Registry.in_game_loop = True

        if args == () or args == (None,):
            args = (0, 0, 0)
        if not (type(args[0]) == int or type(args[0]) == float):
            args = args[0]

        self._color_converter.input_color(args)

        if Registry.display_mode == Constants.PYGAME:
            self._two_dimension_frame_buffer.get().use()
            self._two_dimension_frame_buffer.get().clear(0, 0, 0, 0)
            self._three_dimension_frame_buffer.get().use()
            self._three_dimension_frame_buffer.get().clear(0, 0, 0, 0)
            self._fill_color = self._color_converter.output_color(format=Constants.RGB)
            self._color_key = _numpy.array([*self._color_converter.output_color(format=Constants.SMALL_RGB)], dtype=_numpy.float32)
            self._pygame_surface.clear(self._fill_color)
            Registry.context.screen.use()
            Registry.context.clear(*self._color_converter.output_color(format=Constants.SMALL_RGBA))
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

        Registry.context.screen.use()

        Registry.refresh_rate = refresh_rate
        if Registry.display_mode == Constants.PYGAME:
            byte_data = self._pygame_surface.to_string(flipped=True)
            self._opengl.blit_image_to_texture(
                byte_data,
                self._pygame_surface_texture)

            aggregation_program = self._opengl.get_texture_aggregation_program().get()
            aggregation_program["texture2d"].value = 0
            aggregation_program["texture3d"].value = 1
            aggregation_program["pygame_texture"].value = 2
            aggregation_program["color_key"].write(self._color_key)
            self._two_dimension_texture.get().use(location=0)
            self._three_dimension_texture.get().use(location=1)
            self._pygame_surface_texture.get().use(location=2)

            Registry.context.enable(_moderngl.BLEND)
            self._display_quad.render(aggregation_program)
            Registry.context.disable(_moderngl.BLEND)

            _pygame.display.flip()

            if Constants.EVENTS_OBJECT in Registry.pmma_module_spine.keys():
                if Registry.pmma_module_spine[Constants.EVENTS_OBJECT].get_display_needs_resize():
                    Registry.pmma_module_spine[Constants.EVENTS_OBJECT].set_display_needs_resize(False)
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
                self._clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Constants.PYGAME:
            _pygame.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if Registry.display_mode == Constants.PYGAME:
            return self._clock.get_fps()
        else:
            raise NotImplementedError

    def get_refresh_rate(self):
        return self.get_fps()

    def get_center(self, as_integer=True):
        if Registry.display_mode == Constants.PYGAME:
            if as_integer:
                return self._display.get_width() // 2, self._display.get_height() // 2
            return self._display.get_width() / 2, self._display.get_height() / 2
        else:
            raise NotImplementedError