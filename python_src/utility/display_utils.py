import gc as _gc
import ctypes as _ctypes
import os as _os

import numpy as _numpy
import moderngl as _moderngl
import pygame as _pygame
import pyglet as _pyglet
from moderngl_window import geometry as _geometry
import moderngl_window as _moderngl_window

from pmma.python_src.general import *
from pmma.python_src.constants import Constants
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.opengl import OpenGL as _OpenGL
from pmma.python_src.utility.opengl_utils import Texture as _Texture
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.opengl import FrameBufferObject as _FrameBufferObject
from pmma.python_src.events import WindowResized_EVENT as _WindowResized_EVENT
from pmma.python_src.events import WindowFullScreenStatusChanged_EVENT as _WindowFullScreenStatusChanged_EVENT
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

class DisplayIntermediary:
    def __init__(self):
        _initialize(self, unique_instance=Constants.DISPLAY_OBJECT, add_to_pmma_module_spine=True)

        self._logger = _InternalLogger()

        self._clock = None

        self._color_converter = _ColorConverter()

        self._display_creation_attributes = []

        self._display_quad = None

        self._opengl = _OpenGL()

        self._fill_color = None
        self._color_key = _numpy.array([0, 0, 0], dtype=_numpy.float32)

        self.resized_event = _WindowResized_EVENT()

        self._currently_active_frame_buffer = Constants.DISPLAY_FRAME_BUFFER

        self._display_attribute_resizable = False
        self._display_attribute_full_screen = True
        self._display_attribute_no_frame = True
        self._display_attribute_vsync = True
        self._display_attribute_size = (0, 0)
        self._display_attribute_caption = "PMMA Display"
        self._display_attribute_hwnd = None
        self._display_attribute_transparent_display = False
        self._display_attribute_icon = _path_builder(_Registry.base_path, "resources", "images", "PMMA icon.ico")
        self._display_attribute_centered = True

        self._window_in_focus = True
        self._window_minimized = False

        self.window_full_screen_state_changed_event = _WindowFullScreenStatusChanged_EVENT()

        self._clear_called_but_skipped = False
        self._render_calls = 0
        self._attempted_render_calls = 0 # interface my interface!
        self._refresh_optimization_override = False
        self._previous_frame_color = None
        self._current_display_size = [None, None]

        self._object_updated = False

    def update_class(self):
        if self._object_updated is False:
            self._object_updated = True

            if _Registry.display_mode_set is False:
                _Registry.display_mode_set = True
                _Registry.display_mode = Constants.PYGAME
                self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

            if _Registry.displayed_pygame_start_message is False:
                _Registry.displayed_pygame_start_message = True
                if _Registry.display_mode == Constants.PYGAME:
                    self._logger.log_information(_Registry.pygame_launch_message)
                    _pygame.init()

            if _Registry.display_mode == Constants.PYGAME:
                self._clock = _pygame.time.Clock()

    def get_clear_called_but_skipped(self):
        if self._object_updated is False:
            self.update_class()
        return self._clear_called_but_skipped

    def set_clear_called_but_skipped(self, value):
        if self._object_updated is False:
            self.update_class()
        self._clear_called_but_skipped = value

    def get_render_calls(self):
        if self._object_updated is False:
            self.update_class()
        return self._render_calls

    def set_render_calls(self, value):
        if self._object_updated is False:
            self.update_class()
        self._render_calls = value

    def update_render_calls(self, value):
        if self._object_updated is False:
            self.update_class()
        self._attempted_render_calls += value

    def get_attempted_render_calls(self):
        if self._object_updated is False:
            self.update_class()
        return self._render_calls

    def set_attempted_render_calls(self, value):
        if self._object_updated is False:
            self.update_class()
        self._render_calls = value

    def update_attempted_render_calls(self, value):
        if self._object_updated is False:
            self.update_class()
        self._attempted_render_calls += value

    def get_refresh_optimization_override(self):
        if self._object_updated is False:
            self.update_class()
        return self._refresh_optimization_override

    def set_refresh_optimization_override(self, value):
        if self._object_updated is False:
            self.update_class()
        self._refresh_optimization_override = value

    def clear(self, color=None, format=Constants.RGB):
        if self._object_updated is False:
            self.update_class()
        if color is None or color == [] or color == ():
            self._color_converter.set_color((0, 0, 0), format=Constants.RGB)

        elif type(color) == _ColorConverter:
            raw_color = color.get_color(Constants.RGBA)
            self._color_converter.set_color(raw_color, format=Constants.RGBA)
        else:
            self._color_converter.set_color(color, format=format)

        if self._previous_frame_color is not None:
            if self._color_converter.get_color(format=Constants.RGBA) == self._previous_frame_color.get_color(format=Constants.RGBA):
                if self._refresh_optimization_override is False:
                    if self._render_calls == self._attempted_render_calls:
                        self._render_calls = self._attempted_render_calls
                        self._attempted_render_calls = 0
                        self._clear_called_but_skipped = True
                        return

        self._previous_frame_color = _ColorConverter()
        self._previous_frame_color.set_color(self._color_converter.get_color(format=Constants.RGBA), format=Constants.RGBA)

        self._clear_called_but_skipped = False
        self._refresh_optimization_override = False
        self._render_calls = self._attempted_render_calls
        self._attempted_render_calls = 0

        if self._display_attribute_transparent_display:
            # Set transparency color key
            hex_color = self._color_converter.get_color(format=Constants.HEX)
            color_key = self.hex_color_to_windows_raw_color(hex_color)

            _ctypes.windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)

        self._color_key = _numpy.array([*self._color_converter.get_color(format=Constants.SMALL_RGB)], dtype=_numpy.float32)

        if _Registry.display_mode == Constants.PYGAME:
            #self._two_dimension_frame_buffer.use()
            self._two_dimension_frame_buffer.clear(self._color_converter)
            #self._three_dimension_frame_buffer.use()
            self._three_dimension_frame_buffer.clear(self._color_converter)
            _Registry.context.screen.use()
            _Registry.context.clear(*self._color_converter.get_color(format=Constants.SMALL_RGB))
        else:
            raise NotImplementedError

    def set_window_in_focus(self, value):
        if self._object_updated is False:
            self.update_class()
        self._window_in_focus = value

    def set_window_minimized(self, value):
        if self._object_updated is False:
            self.update_class()
        self._window_minimized = value

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if _Registry.display_mode == Constants.PYGAME:
                _pygame.display.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _setup_layers(self, size):
        if self._object_updated is False:
            self.update_class()
        if _Registry.do_anti_aliasing is False:
            samples = 0
        else:
            samples = _Registry.anti_aliasing_level

        self._current_display_size = _pygame.display.get_window_size()

        self._two_dimension_texture = _Texture()
        self._two_dimension_texture.create(size, components=Constants.RGB, samples=samples)
        self._two_dimension_frame_buffer = _FrameBufferObject()
        self._two_dimension_frame_buffer.create(color_attachments=[self._two_dimension_texture])
        self._three_dimension_texture = _Texture()
        self._three_dimension_texture.create(size, components=Constants.RGB, samples=samples)
        self._three_dimension_frame_buffer = _FrameBufferObject()
        self._three_dimension_frame_buffer.create(color_attachments=[self._three_dimension_texture])

        self._refresh_optimization_override = True
        self._currently_active_frame_buffer = Constants.DISPLAY_FRAME_BUFFER

    def get_2D_hardware_accelerated_surface(self, set_to_be_used=True):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            if set_to_be_used:
                if self._currently_active_frame_buffer != Constants.TWO_DIMENSION_FRAME_BUFFER:
                    self._currently_active_frame_buffer = Constants.TWO_DIMENSION_FRAME_BUFFER
                    self._two_dimension_frame_buffer.use()
            return self._two_dimension_frame_buffer
        else:
            raise NotImplementedError

    def get_3D_hardware_accelerated_surface(self, set_to_be_used=True):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            if set_to_be_used:
                if self._currently_active_frame_buffer != Constants.THREE_DIMENSION_FRAME_BUFFER:
                    self._currently_active_frame_buffer = Constants.THREE_DIMENSION_FRAME_BUFFER
                    self._three_dimension_frame_buffer.use()
            return self._three_dimension_frame_buffer
        else:
            raise NotImplementedError

    def _generate_pygame_flags(self):
        if self._object_updated is False:
            self.update_class()
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
            icon=None,
            transparent_display=False,
            centered=True):

        if self._object_updated is False:
            self.update_class()

        if vsync:
            self._logger.log_development("Your display is using vsync. Therefore the \
maximum refresh rate of the display is limited by either the refresh rate, app performance \
or the refresh rate vof the monitor - WHICHEVER IS SMALLEST. If you are testing the performance \
of your application make sure to disable this, but otherwise its best left enabled as it can \
reduce graphical tearing and other rendering anomalies.")

        self._display_attribute_resizable = resizable
        self._display_attribute_full_screen = full_screen
        self._display_attribute_no_frame = no_frame
        self._display_attribute_vsync = vsync
        self._display_attribute_transparent_display = transparent_display
        self._display_attribute_centered = centered

        if self._display_attribute_transparent_display:
            if get_operating_system() == Constants.WINDOWS:
                self._logger.log_development("You are using PMMA's transparent display technology. \
This means that the window you create is going to be completely transparent - including \
its borders and captions. It might seem like the display 'pops-in' before disappearing, \
this is message is really here to reassure you that this is expected behavior and that \
the window is still there, but transparent.")

            else:
                self._logger.log_development("You are attempting to use PMMA's transparent display \
technology - however this isn't currently available on your operating system. We are \
actively working to address this operating system limitation.")

        if caption is not None:
            self._display_attribute_caption = caption

        if icon is not None:
            self._display_attribute_icon = icon

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

        if _Registry.display_mode == Constants.PYGAME:
            flags = self._generate_pygame_flags()

            self.set_caption()

            self.set_icon()

            if self._display_attribute_centered:
                _os.environ["SDL_VIDEO_CENTERED"] = "1"

            self._display = _pygame.display.set_mode(
                self._display_attribute_size,
                flags,
                vsync=self._display_attribute_vsync)

            size = _pygame.display.get_window_size()
            _Registry.window_context = _moderngl_window.get_local_window_cls("pygame2")

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

        _Registry.display_initialized = True

        try:
            _Registry.context = _moderngl.create_context()
            _moderngl_window.activate_context(_Registry.window_context, _Registry.context)
        except Exception as error:
            self._logger.log_error("Failed to create OpenGL context.")
            self._logger.log_development("Failed to create OpenGL context. The most \
likely cause for this error is that there is no available display with OpenGL \
support initiated; make sure to also call the 'create' function in the 'Display' \
class to create it. Should that also not work, make sure that you have the \
appropriate graphics drivers installed and make sure that your GPU supports OpenGL. \
If this fails, try to run another OpenGL application first to attempt to isolate the problem.")

            raise error

        self._texture_aggregation_program = _Shader()
        self._texture_aggregation_program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "texture_aggregation"))
        self._texture_aggregation_program.create()

        self._setup_layers(size)

        self._display_quad = _geometry.quad_fs()

    def set_caption(self, caption=None):
        if self._object_updated is False:
            self.update_class()
        if caption is None:
            caption = self._display_attribute_caption
        if _Registry.display_mode == Constants.PYGAME:
            _pygame.display.set_caption(str(caption))

    def set_icon(self, icon=None):
        if self._object_updated is False:
            self.update_class()
        if icon is None:
            icon = self._display_attribute_icon
        if _Registry.display_mode == Constants.PYGAME:
            icon_img = _pygame.image.load(icon)
            _pygame.display.set_icon(icon_img)
            del icon_img

    def display_resize(self):
        if self._object_updated is False:
            self.update_class()
        size = _pygame.display.get_window_size()

        self._two_dimension_texture.quit()
        self._two_dimension_frame_buffer.quit()
        self._three_dimension_texture.quit()
        self._three_dimension_frame_buffer.quit()

        self._setup_layers(size)

        _Registry.context.viewport = (0, 0, *size)

    def hex_color_to_windows_raw_color(self, value):
        if self._object_updated is False:
            self.update_class()
        color_key = int(value[1:], 16)
        color_key = ((color_key & 0xFF0000) >> 16) | (color_key & 0x00FF00) | ((color_key & 0x0000FF) << 16)
        return color_key

    def toggle_full_screen(self):
        if self._object_updated is False:
            self.update_class()
        self.window_full_screen_state_changed_event.set_value(True)

        self._display_attribute_full_screen = not self._display_attribute_full_screen

        if _Registry.display_mode == Constants.PYGAME:
            if self._display_attribute_full_screen:
                size = (0, 0)
                self._display_attribute_size = self.get_size()
            else:
                size = self._display_attribute_size
                if size == (0, 0):
                    size = (800, 600)

            flags = self._generate_pygame_flags()

            _pygame.display.quit() # issues here with moderngl likely - but without more major windowing issues.

            _Registry.context.release()

            _pygame.display.init()

            self.set_caption()

            self.set_icon()

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
                    self._color_converter.set_color((0, 0, 0), format=Constants.RGB)
                    hex_color = self._color_converter.get_color(format=Constants.HEX)
                    color_key = self.hex_color_to_windows_raw_color(hex_color)
                    _ctypes.windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)

        _Registry.context = _moderngl.create_context()
        _moderngl_window.activate_context(_Registry.window_context, _Registry.context)

        self.display_resize()

        for opengl_object in list(_Registry.opengl_objects.keys()):
            _Registry.opengl_objects[opengl_object].recreate()

        self._display_quad = _geometry.quad_fs()

    def get_size(self):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            return self._current_display_size
        else:
            raise NotImplementedError

    def get_frame_time(self):
        if self._object_updated is False:
            self.update_class()
        return 1/self.get_fps()

    def get_height(self):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            return self._current_display_size[1]
        else:
            raise NotImplementedError

    def get_width(self):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            return self._current_display_size[0]
        else:
            raise NotImplementedError

    def get_aspect_ratio(self):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            return self._current_display_size[0] / self._current_display_size[1]
        else:
            raise NotImplementedError

    def refresh(
            self,
            refresh_rate=None,
            lower_refresh_rate_when_minimized=True,
            lower_refresh_rate_when_unfocused=True,
            lower_refresh_rate_on_low_battery=True):

        if self._object_updated is False:
            self.update_class()

        if _Registry.handled_events is False:
            self._logger.log_development("You are not using PMMA's event manager. This is \
important as it tells the operating system that the window is responding and \
working correctly. It is strongly advised that when running a display, you \
handle events too.")

        _Registry.handled_events = False

        if _Registry.compute_component_called is False:
            self._logger.log_warning("PMMA compute operation not called! Please call \
this function before ending the game loop with this!")
            self._logger.log_development("PMMA compute operation not called! Calling \
this allows PMMA to perform more self-optimization and improve development \
messages. Please place this compute function 'pmma.compute()' just before \
you refresh the display to ensure optimal performance and support!")
        else:
            _Registry.compute_component_called = False

        if refresh_rate is None:
            refresh_rate = 60

        if _Registry.power_saving_mode and lower_refresh_rate_on_low_battery:
            refresh_rate = int(refresh_rate * 0.75)

        if lower_refresh_rate_when_unfocused and not self._window_in_focus:
            refresh_rate = int(refresh_rate * 0.5)

        if lower_refresh_rate_when_minimized and self._window_minimized:
            refresh_rate = 5

        if refresh_rate < 5:
            refresh_rate = 5

        _Registry.refresh_rate = refresh_rate
        if _Registry.display_mode == Constants.PYGAME:
            if self._clear_called_but_skipped is False:
                _Registry.context.screen.use()
                self._currently_active_frame_buffer = Constants.DISPLAY_FRAME_BUFFER

                if self._two_dimension_texture.get_samples() == 0:
                    self._texture_aggregation_program.set_shader_variable("texture2d", 0)
                    self._two_dimension_texture.use(location=0)
                else:
                    self._texture_aggregation_program.set_shader_variable("texture2d_ms", 0)
                    self._two_dimension_texture.use(location=0)
                self._texture_aggregation_program.set_shader_variable("texture2d_samples", self._two_dimension_texture.get_samples())
                self._texture_aggregation_program.set_shader_variable("texture2d_resolution", self._two_dimension_texture.get_size())

                if self._three_dimension_texture.get_samples() == 0:
                    self._texture_aggregation_program.set_shader_variable("texture3d", 1)
                    self._three_dimension_texture.use(location=1)
                else:
                    self._texture_aggregation_program.set_shader_variable("texture3d_ms", 1)
                    self._three_dimension_texture.use(location=1)
                self._texture_aggregation_program.set_shader_variable("texture3d_samples", self._three_dimension_texture.get_samples())
                self._texture_aggregation_program.set_shader_variable("texture3d_resolution", self._three_dimension_texture.get_size())

                self._texture_aggregation_program.set_shader_variable("color_key", self._color_key)

                _Registry.context.enable(_moderngl.BLEND)
                self._display_quad.render(self._texture_aggregation_program.use_program())
                _Registry.context.disable(_moderngl.BLEND)

                _pygame.display.flip()

            if self.resized_event.get_value():
                self.display_resize()

            frame_rate = self.get_fps()
            if _Registry.application_average_frame_rate["Samples"] == 0:
                _Registry.application_average_frame_rate["Mean"] = frame_rate
                _Registry.application_average_frame_rate["Samples"] = 1
            else:
                mean = _Registry.application_average_frame_rate["Mean"] * _Registry.application_average_frame_rate["Samples"]
                mean += frame_rate
                _Registry.application_average_frame_rate["Samples"] += 1
                _Registry.application_average_frame_rate["Mean"] = mean / _Registry.application_average_frame_rate["Samples"]

            if refresh_rate > 0:
                self._clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            _pygame.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            return self._clock.get_fps()
        else:
            raise NotImplementedError

    def get_refresh_rate(self):
        if self._object_updated is False:
            self.update_class()
        return self.get_fps()

    def get_center(self, as_integer=True):
        if self._object_updated is False:
            self.update_class()
        if _Registry.display_mode == Constants.PYGAME:
            if as_integer:
                return self._display.get_width() // 2, self._display.get_height() // 2
            return self._display.get_width() / 2, self._display.get_height() / 2
        else:
            raise NotImplementedError