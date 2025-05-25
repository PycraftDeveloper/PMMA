from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class Display:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DISPLAY_OBJECT)
            from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
            _DisplayIntermediary()

        self._display_intermediary: "_DisplayIntermediary" = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT]

    def clear(self, color=None, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._display_intermediary.clear(color=color, format=format)

    def set_window_in_focus(self, value):
        """
        🟩 **R** -
        """
        self._display_intermediary.set_window_in_focus(value=value)

    def set_window_minimized(self, value):
        """
        🟩 **R** -
        """
        self._display_intermediary.set_window_minimized(value=value)

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def get_2D_hardware_accelerated_surface(self, set_to_be_used=True):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_2D_hardware_accelerated_surface(set_to_be_used=set_to_be_used)

    def get_3D_hardware_accelerated_surface(self, set_to_be_used=True):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_3D_hardware_accelerated_surface(set_to_be_used=set_to_be_used)

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

        self._display_intermediary.create(
            width=width,
            height=height,
            full_screen=full_screen,
            resizable=resizable,
            no_frame=no_frame,
            caption=caption,
            vsync=vsync,
            icon=icon,
            transparent_display=transparent_display,
            centered=centered)

    def set_caption(self, caption=None):
        """
        🟩 **R** -
        """
        self._display_intermediary.set_caption(caption=caption)

    def set_icon(self, icon=None):
        """
        🟩 **R** -
        """
        self._display_intermediary.set_icon(icon=icon)

    def toggle_full_screen(self):
        """
        🟩 **R** -
        """
        self._display_intermediary.toggle_full_screen()

    def get_size(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_size()

    def get_frame_time(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_frame_time()

    def get_height(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_height()

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_width()

    def get_aspect_ratio(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_aspect_ratio()

    def refresh(
            self,
            refresh_rate=None,
            lower_refresh_rate_when_minimized=True,
            lower_refresh_rate_when_unfocused=True,
            lower_refresh_rate_on_low_battery=True):
        """
        🟩 **R** -
        """

        self._display_intermediary.refresh(
            refresh_rate=refresh_rate,
            lower_refresh_rate_when_minimized=lower_refresh_rate_when_minimized,
            lower_refresh_rate_when_unfocused=lower_refresh_rate_when_unfocused,
            lower_refresh_rate_on_low_battery=lower_refresh_rate_on_low_battery)

    def close(self):
        """
        🟩 **R** -
        """
        self._display_intermediary.close()

    def get_fps(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_fps()

    def get_refresh_rate(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_refresh_rate()

    def get_center(self, as_integer=True):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_center(as_integer=as_integer)

    def get_display_projection(self):
        """
        🟩 **R** -
        """
        return self._display_intermediary.get_display_projection()