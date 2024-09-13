import gc as _gc

from pmma.python_src.constants import Constants

from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Display:
    def __init__(self):
        _initialize(self)

        self._display_intermediary: "_DisplayIntermediary" = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

    def clear(self, color=None, format=Constants.RGB):
        self._display_intermediary.clear(color=color, format=format)

    def set_window_in_focus(self, value):
        self._display_intermediary.set_window_in_focus(value=value)

    def set_window_minimized(self, value):
        self._display_intermediary.set_window_minimized(value=value)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_2D_hardware_accelerated_surface(self, set_to_be_used=True):
        return self._display_intermediary.get_2D_hardware_accelerated_surface(set_to_be_used=set_to_be_used)

    def get_3D_hardware_accelerated_surface(self, set_to_be_used=True):
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
        self._display_intermediary.set_caption(caption=caption)

    def set_icon(self, icon=None):
        self._display_intermediary.set_icon(icon=icon)

    def toggle_full_screen(self):
        self._display_intermediary.toggle_full_screen()

    def get_size(self):
        return self._display_intermediary.get_size()

    def get_frame_time(self):
        return self._display_intermediary.get_frame_time()

    def get_height(self):
        return self._display_intermediary.get_height()

    def get_width(self):
        return self._display_intermediary.get_width()

    def get_aspect_ratio(self):
        return self._display_intermediary.get_aspect_ratio()

    def refresh(
            self,
            refresh_rate=None,
            lower_refresh_rate_when_minimized=True,
            lower_refresh_rate_when_unfocused=True,
            lower_refresh_rate_on_low_battery=True):

        self._display_intermediary.refresh(
            refresh_rate=refresh_rate,
            lower_refresh_rate_when_minimized=lower_refresh_rate_when_minimized,
            lower_refresh_rate_when_unfocused=lower_refresh_rate_when_unfocused,
            lower_refresh_rate_on_low_battery=lower_refresh_rate_on_low_battery)

    def close(self):
        self._display_intermediary.close()

    def get_fps(self):
        return self._display_intermediary.get_fps()

    def get_refresh_rate(self):
        return self._display_intermediary.get_refresh_rate()

    def get_center(self, as_integer=True):
        return self._display_intermediary.get_center(as_integer=as_integer)