import gc as _gc
import ctypes as _ctypes

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
from pmma.python_src.events import WindowResized_EVENT as _WindowResized_EVENT

class Display:
    def __init__(self):
        initialize(self, unique_instance=Constants.DISPLAY_OBJECT, add_to_pmma_module_spine=True, requires_display_mode_set=True)

        if Registry.display_mode == Constants.PYGAME:
            self._clock = _pygame.time.Clock()

        self._color_converter = _Color()

        self._display_creation_attributes = []

        self._display_quad = None

        self._opengl = _OpenGL()

        self._fill_color = None
        self._color_key = _numpy.array([0, 0, 0], dtype=_numpy.float32)

        self.resized_event = _WindowResized_EVENT()

        self._display_attribute_resizable = False
        self._display_attribute_full_screen = True
        self._display_attribute_no_frame = True
        self._display_attribute_vsync = True
        self._display_attribute_size = (0, 0)
        self._display_attribute_caption = "PMMA Display"
        self._display_attribute_hwnd = None
        self._display_attribute_transparent_display = False

        self._clear_color = (0, 0, 0)

        self._window_in_focus = True
        self._window_minimized = False

    def set_window_in_focus(self, value):
        self._window_in_focus = value

    def set_window_minimized(self, value):
        self._window_minimized = value

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

    def _generate_pygame_flags(self):
        flags = _pygame.OPENGL | _pygame.DOUBLEBUF

        if self._display_attribute_no_frame:
            flags |= _pygame.NOFRAME
        if self._display_attribute_resizable:
            flags |= _pygame.RESIZABLE
        if self._display_attribute_full_screen:
            flags |= _pygame.FULLSCREEN

        return flags

    def create(
            self,
            width=None,
            height=None,
            full_screen=True,
            resizable=False,
            no_frame=False,
            caption=None,
            vsync=True,
            transparent_display=False):

        self._display_attribute_resizable = resizable
        self._display_attribute_full_screen = full_screen
        self._display_attribute_no_frame = no_frame
        self._display_attribute_vsync = vsync
        self._display_attribute_transparent_display = transparent_display

        if self._display_attribute_transparent_display:
            if get_operating_system() == Constants.WINDOWS:
                log_development("You are using PMMA's transparent display technology. \
This means that the window you create is going to be completely transparent - including \
its borders and captions. It might seem like the display 'pops-in' before disappearing, \
this is message is really here to reassure you that this is expected behavior and that \
the window is still there, but transparent.")

            else:
                log_development("You are attempting to use PMMA's transparent display \
technology - however this isn't currently available on your operating system. We are \
actively working to address this operating system limitation.")

        if caption is not None:
            self._display_attribute_caption = caption

        if self._display_attribute_full_screen:
            if width is None:
                width = 0
            if height is None:
                height = 0
        else:
            if width is None:
                width = 800
            if height is None:
                height = 600

        self._display_attribute_size = (width, height)

        if Registry.display_mode == Constants.PYGAME:
            flags = self._generate_pygame_flags()

            self.set_caption()

            self._display = _pygame.display.set_mode(
                self._display_attribute_size,
                flags,
                vsync=self._display_attribute_vsync)

            size = _pygame.display.get_window_size()
            Registry.window_context = _moderngl_window.get_local_window_cls("pygame2")

            if self._display_attribute_transparent_display:
                if get_operating_system() == Constants.WINDOWS:
                    self._display_attribute_hwnd = _pygame.display.get_wm_info()["window"]

                    # Make the window transparent and allow click-through
                    # Set the window to be layered
                    _ctypes.windll.user32.SetWindowLongW(self._display_attribute_hwnd, -20, _ctypes.windll.user32.GetWindowLongW(self._display_attribute_hwnd, -20) | 0x80000)

                    # Set transparency color key
                    color_key = self.hex_color_to_windows_raw_color("#000000")
                    _ctypes.windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)
        else:
            raise NotImplementedError

        Registry.display_initialized = True

        _OpenGLIntermediary()

        self.__setup_layers(size)

        self._display_quad = _geometry.quad_fs()

    def set_caption(self, caption=None):
        if caption is None:
            caption = self._display_attribute_caption
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

    def hex_color_to_windows_raw_color(self, value):
        color_key = int(value[1:], 16)
        color_key = ((color_key & 0xFF0000) >> 16) | (color_key & 0x00FF00) | ((color_key & 0x0000FF) << 16)
        return color_key

    def toggle_full_screen(self):
        self._display_attribute_full_screen = not self._display_attribute_full_screen

        if Registry.display_mode == Constants.PYGAME:
            if self._display_attribute_full_screen:
                size = (0, 0)
                self._display_attribute_size = self.get_size()
            else:
                size = self._display_attribute_size
                if size == (0, 0):
                    size = (800, 600)

            flags = self._generate_pygame_flags()

            _pygame.display.quit()
            _pygame.display.init()

            self.set_caption()

            self._display = _pygame.display.set_mode(
                size,
                flags,
                vsync=self._display_attribute_vsync)

            if self._display_attribute_transparent_display:
                if get_operating_system() == Constants.WINDOWS:
                    self._display_attribute_hwnd = _pygame.display.get_wm_info()["window"]

                    # Make the window transparent and allow click-through
                    # Set the window to be layered
                    _ctypes.windll.user32.SetWindowLongW(self._display_attribute_hwnd, -20, _ctypes.windll.user32.GetWindowLongW(self._display_attribute_hwnd, -20) | 0x80000)

                    # Set transparency color key
                    self._color_converter.input_color(self._clear_color, format=Constants.RGB)
                    hex_color = self._color_converter.output_color(format=Constants.HEX)
                    color_key = self.hex_color_to_windows_raw_color(hex_color)
                    _ctypes.windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)

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

        # Set transparency color key
        hex_color = self._color_converter.output_color(format=Constants.HEX)
        color_key = self.hex_color_to_windows_raw_color(hex_color)

        _ctypes.windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)

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
            self._clear_color = self._color_converter.output_color(format=Constants.RGB)
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=None):
        print(self._window_in_focus, self._window_minimized) # tmp

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

            if self.resized_event.get_value():
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