from gc import collect as _gc__collect
import os as _os
from platform import system as _platform__system

from numpy import float32 as _numpy__float32
from numpy import array as _numpy__array
from moderngl import BLEND as _moderngl__BLEND
from moderngl import create_context as _moderngl__create_context
from pygame import init as _pygame__init
from pygame import quit as _pygame__quit
from pygame import time as _pygame__time
from pygame import display as _pygame__display
from pygame import OPENGL as _pygame__OPENGL
from pygame import RESIZABLE as _pygame__RESIZABLE
from pygame import FULLSCREEN as _pygame__FULLSCREEN
from pygame import NOFRAME as _pygame__NOFRAME
from pygame import DOUBLEBUF as _pygame__DOUBLEBUF
from pygame import image as _pygame__image
from moderngl_window import geometry as _geometry
from moderngl_window import get_local_window_cls as _moderngl_window__get_local_window_cls
from moderngl_window import activate_context as _moderngl_window__activate_context

from pmma.python_src.general import get_operating_system as _get_operating_system
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.opengl import OpenGL as _OpenGL
from pmma.python_src.utility.opengl_utils import Texture as _Texture
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.opengl import FrameBufferObject as _FrameBufferObject
from pmma.python_src.events import WindowResized_EVENT as _WindowResized_EVENT
from pmma.python_src.events import WindowRestored_EVENT as _WindowRestored_EVENT
from pmma.python_src.events import WindowMinimized_EVENT as _WindowMinimized_EVENT
from pmma.python_src.events import WindowFocusGained_EVENT as _WindowFocusGained_EVENT
from pmma.python_src.events import WindowFocusLost_EVENT as _WindowFocusLost_EVENT
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.projection import OrthographicProjection as _OrthographicProjection
from pmma.python_src.projection import PerspectiveProjection as _PerspectiveProjection
from pmma.python_src.advtkinter import Tkinter as _Tkinter

from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

if _platform__system() == "Windows":
    from ctypes import windll as _ctypes__windll

class DisplayIntermediary:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_Constants.DISPLAY_OBJECT, add_to_pmma_module_spine=True)

        self._logger = _InternalLogger()

        self._clock = None

        self._color_converter = _ColorConverter()

        self._display_creation_attributes = []

        self._display_quad = None

        self._opengl = _OpenGL()

        self._fill_color = None
        self._color_key = _numpy__array([0, 0, 0], dtype=_numpy__float32)

        self.resized_event = _WindowResized_EVENT()
        _WindowRestored_EVENT() # for passports
        _WindowMinimized_EVENT() # for passports
        _WindowFocusGained_EVENT() # for passports
        _WindowFocusLost_EVENT() # for passports

        self._currently_active_frame_buffer = _Constants.DISPLAY_FRAME_BUFFER

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

        self._clear_called_but_skipped = False
        self._render_calls = 0
        self._attempted_render_calls = 0 # interface my interface!
        self._refresh_optimization_override = False
        self._previous_frame_color = None
        self._current_display_size = [None, None]

        self._object_updated = False

        self._two_dimension_texture = _Texture()
        self._two_dimension_frame_buffer = _FrameBufferObject()
        self._three_dimension_texture = _Texture()
        self._three_dimension_frame_buffer = _FrameBufferObject()

        self._orthographic_projection = None

        self._tkinter_backend = _Tkinter()

        self._clock = _pygame__time.Clock()

        if not _Constants.GPU_DISTRIBUTION_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.GPU_DISTRIBUTION_MANAGER_OBJECT)
            from pmma.python_src.utility.gpu_distribution_utils import GPUDistributionManager as _GPUDistributionManager
            _GPUDistributionManager()

        self._gpu_distribution_manager = _Registry.pmma_module_spine[_Constants.GPU_DISTRIBUTION_MANAGER_OBJECT]

        if not _Constants.PROJECTION_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PROJECTION_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.projection_utils import ProjectionIntermediary as _ProjectionIntermediary
            _ProjectionIntermediary()

        self._projection_intermediary = _Registry.pmma_module_spine[_Constants.PROJECTION_INTERMEDIARY_OBJECT]

    def get_clear_called_but_skipped(self):
        """
        🟩 **R** -
        """
        return self._clear_called_but_skipped

    def set_clear_called_but_skipped(self, value):
        """
        🟩 **R** -
        """
        self._clear_called_but_skipped = value

    def get_render_calls(self):
        """
        🟩 **R** -
        """
        return self._render_calls

    def set_render_calls(self, value):
        """
        🟩 **R** -
        """
        self._render_calls = value

    def update_render_calls(self, value):
        """
        🟩 **R** -
        """
        self._attempted_render_calls += value

    def get_attempted_render_calls(self):
        """
        🟩 **R** -
        """
        return self._render_calls

    def set_attempted_render_calls(self, value):
        """
        🟩 **R** -
        """
        self._render_calls = value

    def update_attempted_render_calls(self, value):
        """
        🟩 **R** -
        """
        self._attempted_render_calls += value

    def get_refresh_optimization_override(self):
        """
        🟩 **R** -
        """
        return self._refresh_optimization_override

    def set_refresh_optimization_override(self, value):
        """
        🟩 **R** -
        """
        self._refresh_optimization_override = value

    def clear(self, color=None, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return

        if color is None or color == [] or color == ():
            self._color_converter.set_color((0, 0, 0), format=_Constants.RGB)

        elif type(color) == _ColorConverter:
            raw_color = color.get_color(_Constants.RGBA)
            self._color_converter.set_color(raw_color, format=_Constants.RGBA)
        else:
            self._color_converter.set_color(color, format=format)

        if self._previous_frame_color is not None:
            background_color_comparison = self._color_converter.get_color(format=_Constants.RGBA) == self._previous_frame_color.get_color(format=_Constants.RGBA)
            if background_color_comparison.all():
                if self._refresh_optimization_override is False:
                    if self._render_calls == self._attempted_render_calls:
                        self._render_calls = self._attempted_render_calls
                        self._attempted_render_calls = 0
                        self._clear_called_but_skipped = True
                        return

        self._previous_frame_color = _ColorConverter()
        self._previous_frame_color.set_color(self._color_converter.get_color(format=_Constants.RGBA), format=_Constants.RGBA)

        self._clear_called_but_skipped = False
        self._refresh_optimization_override = False
        self._render_calls = self._attempted_render_calls
        self._attempted_render_calls = 0

        if self._display_attribute_transparent_display:
            # Set transparency color key
            hex_color = self._color_converter.get_color(format=_Constants.HEX)
            color_key = self.hex_color_to_windows_raw_color(hex_color)

            _ctypes__windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)

        self._color_key = _numpy__array([*self._color_converter.get_color(format=_Constants.SMALL_RGB)], dtype=_numpy__float32)

        #self._two_dimension_frame_buffer.use()
        self._two_dimension_frame_buffer.clear(self._color_converter)
        #self._three_dimension_frame_buffer.use()
        self._three_dimension_frame_buffer.clear(self._color_converter)
        _Registry.context.screen.use()
        _Registry.context.clear(*self._color_converter.get_color(format=_Constants.SMALL_RGB))

    def set_window_in_focus(self, value):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        self._window_in_focus = value

    def set_window_minimized(self, value):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        self._window_minimized = value

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            _pygame__display.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _setup_layers(self, size):
        """
        🟩 **R** -
        """
        if _Registry.do_anti_aliasing is False:
            samples = 0
        else:
            samples = _Registry.anti_aliasing_level

        self._two_dimension_texture.create(size, components=_Constants.RGB, samples=samples)
        self._two_dimension_frame_buffer.create(color_attachments=[self._two_dimension_texture])
        self._three_dimension_texture.create(size, components=_Constants.RGB, samples=samples)
        self._three_dimension_frame_buffer.create(color_attachments=[self._three_dimension_texture])

    def get_2D_hardware_accelerated_surface(self, set_to_be_used=True):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        if set_to_be_used:
            if self._currently_active_frame_buffer != _Constants.TWO_DIMENSION_FRAME_BUFFER:
                self._currently_active_frame_buffer = _Constants.TWO_DIMENSION_FRAME_BUFFER
                self._two_dimension_frame_buffer.use()
        return self._two_dimension_frame_buffer

    def get_3D_hardware_accelerated_surface(self, set_to_be_used=True):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        if set_to_be_used:
            if self._currently_active_frame_buffer != _Constants.THREE_DIMENSION_FRAME_BUFFER:
                self._currently_active_frame_buffer = _Constants.THREE_DIMENSION_FRAME_BUFFER
                self._three_dimension_frame_buffer.use()
        return self._three_dimension_frame_buffer

    def _generate_pygame_flags(self, care_about_full_screen=True):
        """
        🟩 **R** -
        """
        flags = _pygame__OPENGL | _pygame__DOUBLEBUF

        if self._display_attribute_no_frame:
            flags |= _pygame__NOFRAME
        if self._display_attribute_resizable:
            flags |= _pygame__RESIZABLE
        if self._display_attribute_full_screen and care_about_full_screen:
            flags |= _pygame__FULLSCREEN

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
        """
        🟩 **R** -
        """

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame__init()

        if vsync:
            self._logger.log_development("Your display is using vsync. Therefore the \
maximum refresh rate of the display is limited by either the refresh rate, app performance \
or the refresh rate of the monitor - WHICHEVER IS SMALLEST. If you are testing the performance \
of your application make sure to disable this, but otherwise its best left enabled as it can \
reduce graphical tearing and other rendering anomalies.")

        self._display_attribute_resizable = resizable
        self._display_attribute_full_screen = full_screen
        self._display_attribute_no_frame = no_frame
        self._display_attribute_vsync = vsync
        self._display_attribute_transparent_display = transparent_display
        self._display_attribute_centered = centered

        if self._display_attribute_transparent_display:
            if _get_operating_system() == _Constants.WINDOWS:
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

        if width is None:
            width = 800
        if height is None:
            height = 600

        self._display_attribute_size = (width, height)

        flags = self._generate_pygame_flags()

        self.set_caption()

        self.set_icon()

        if self._display_attribute_centered:
            _os.environ["SDL_VIDEO_CENTERED"] = "1"

        if self._display_attribute_full_screen:
            size = (0, 0)
        else:
            size = self._display_attribute_size

        self._display = _pygame__display.set_mode(
            size,
            flags,
            vsync=self._display_attribute_vsync)

        _Registry.window_context = _moderngl_window__get_local_window_cls("pygame2")

        if self._display_attribute_transparent_display:
            if _get_operating_system() == _Constants.WINDOWS:
                self._display_attribute_hwnd = _pygame__display.get_wm_info()["window"]

                # Make the window transparent and allow click-through
                # Set the window to be layered
                _ctypes__windll.user32.SetWindowLongW(self._display_attribute_hwnd, -20, _ctypes__windll.user32.GetWindowLongW(self._display_attribute_hwnd, -20) | 0x80000)

                # Set transparency color key
                color_key = self.hex_color_to_windows_raw_color("#000000")
                _ctypes__windll.user32.SetLayeredWindowAttributes(self._display_attribute_hwnd, color_key, 0, 0x2)

        _Registry.display_initialized = True

        try:
            _Registry.context = _moderngl__create_context()
            _moderngl_window__activate_context(_Registry.window_context, _Registry.context)
        except Exception as error:
            self._logger.log_error("Failed to create OpenGL context.")
            self._logger.log_development("Failed to create OpenGL context. Make sure that \
you have the appropriate graphics drivers installed and make sure that your GPU supports OpenGL. \
If this fails, try to run another OpenGL application first to attempt to isolate the problem.")

            raise error

        self._texture_aggregation_program = _Shader()
        self._texture_aggregation_program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "texture_aggregation"))
        self._texture_aggregation_program.create()

        self.on_window_size_changed()

        self._display_quad = _geometry.quad_fs()

        self._gpu_distribution_manager.update_gpu_roles(initialization_override=True)

    def set_caption(self, caption=None):
        """
        🟩 **R** -
        """
        if caption is None:
            caption = self._display_attribute_caption
        _pygame__display.set_caption(str(caption))

    def set_icon(self, icon=None):
        """
        🟩 **R** -
        """
        if icon is None:
            icon = self._display_attribute_icon
        icon_img = _pygame__image.load(icon)
        _pygame__display.set_icon(icon_img)
        del icon_img

    def get_display_projection(self): # should be public
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self._orthographic_projection

    def on_window_size_changed(self):
        """
        🟩 **R** -
        """
        size = _pygame__display.get_window_size()

        self._current_display_size = size

        self._projection_intermediary.orthographic_projection = _OrthographicProjection(0, size[0], size[1], 0, 1, -1)
        self._projection_intermediary.perspective_projection = _PerspectiveProjection(60, self.get_aspect_ratio(), 0.1, 1000) # determine these later

        self._setup_layers(size)

        _Registry.context.viewport = (0, 0, *size)

        self._refresh_optimization_override = True
        self._currently_active_frame_buffer = _Constants.DISPLAY_FRAME_BUFFER

        if _Constants.SHAPE_GEOMETRY_MANAGER_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].reset()

    def hex_color_to_windows_raw_color(self, value):
        """
        🟩 **R** -
        """
        color_key = int(value[1:], 16)
        color_key = ((color_key & 0xFF0000) >> 16) | (color_key & 0x00FF00) | ((color_key & 0x0000FF) << 16)
        return color_key

    def toggle_full_screen(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        flags = self._generate_pygame_flags(care_about_full_screen=False)

        if self._display_attribute_full_screen is False:
            self._display_attribute_size = _pygame__display.get_window_size()

        self._display_attribute_full_screen = not self._display_attribute_full_screen

        if self._display_attribute_full_screen:
            _pygame__display.set_mode((0, 0), flags, vsync=self._display_attribute_vsync)
            self._display = _pygame__display.set_mode((0, 0), flags | _pygame__FULLSCREEN, vsync=self._display_attribute_vsync)

        else:
            _pygame__display.set_mode((0, 0), flags, vsync=self._display_attribute_vsync)

            if self._display_attribute_size[0] < 800:
                self._display_attribute_size = (800, self._display_attribute_size[1])

            if self._display_attribute_size[1] < 600:
                self._display_attribute_size = (self._display_attribute_size[0], 600)

            self._display = _pygame__display.set_mode(self._display_attribute_size, flags, vsync=self._display_attribute_vsync)

        self.on_window_size_changed()

    def get_size(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self._current_display_size

    def get_frame_time(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return 1/self.get_fps()

    def get_height(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self._current_display_size[1]

    def get_width(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self._current_display_size[0]

    def get_aspect_ratio(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self._current_display_size[0] / self._current_display_size[1]

    def refresh(
            self,
            refresh_rate=None,
            lower_refresh_rate_when_minimized=True,
            lower_refresh_rate_when_unfocused=True,
            lower_refresh_rate_on_low_battery=True):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
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
        if self._clear_called_but_skipped is False:
            if _Registry.render_pipeline_acceleration_available:
                self.get_2D_hardware_accelerated_surface()
                _Registry.pmma_module_spine[_Constants.RENDER_PIPELINE_MANAGER_OBJECT].render()

            _Registry.context.screen.use()
            self._currently_active_frame_buffer = _Constants.DISPLAY_FRAME_BUFFER

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

            _Registry.context.enable(_moderngl__BLEND)
            self._display_quad.render(self._texture_aggregation_program.use_program())
            _Registry.context.disable(_moderngl__BLEND)

            _pygame__display.flip()

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

    def get_clock(self):
        """
        🟩 **R** -
        """
        return self._clock

    def close(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        _pygame__quit()

    def get_fps(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self._clock.get_fps()

    def get_refresh_rate(self):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        return self.get_fps()

    def get_center(self, as_integer=True):
        """
        🟩 **R** -
        """
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to create a display with the `create` before you can use this function.")
            return
        if as_integer:
            return self._display.get_width() // 2, self._display.get_height() // 2
        return self._display.get_width() / 2, self._display.get_height() / 2