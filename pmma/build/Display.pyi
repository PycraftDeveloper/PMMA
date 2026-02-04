from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

import pmma.core.py_src.Utility as Utility
from pmma.build.CoreTypes import Color

Integer1D = Union[
    npt.NDArray[np.int32], # preferred
    npt.NDArray[np.int8],
    npt.NDArray[np.int16],
    npt.NDArray[np.int64],
    Iterable[int],
]

OptionalInteger = Union[
    int,
    None,
]

OptionalColor = Union[
    Color,
    None
]

OptionalBool = Union[
    bool,
    None
]

Float1D = Union[
    npt.NDArray[np.float32], # preferred
    npt.NDArray[np.float16],
    npt.NDArray[np.float64],
    Iterable[float]]

Numerical = Union[float, int]

NoneInt = Union[int, None]

class Display:
    def __init__(self) -> None:
        """This creates a new Display object."""
        ...

    window_fill_color: Color

    def create(
            self, size: Integer1D=..., caption: str="PMMA Display",
            fullscreen: OptionalBool=True, resizable: bool=False,
            no_frame: bool=False, vsync: bool=True, icon: str="",
            centered: bool=True, maximized: bool=False) -> None:
        """
        This method is used to create a window which will be the rendering target for PMMA. All 2D and 3D content will end up being rendered to this window.

        :param Union[npt.NDArray[np.int32], npt.NDArray[np.int8], npt.NDArray[np.int16], npt.NDArray[np.int64], Iterable[int]] size: The size of the window in pixels. If set to (0, 0) the window will be created at the current monitor's resolution and be automatically full-screen. For this method you can input either an iterable Python sequence (list or tuple for example) or a numpy array. All inputs are converted automatically to be a continuous uint32 (or unsigned int 32) numpy array - its unlikely this conversion will be slow in this scenario.
        :param str caption: The window title name.
        :param Union[None, bool] fullscreen: This is used to control if the window should be full screen or not. If the value is left as the default :code:`None` PMMA will set the window to be automatically full screened when the window size is (0, 0).
        :param bool resizable: This is used to control whether the window can be resized by the user. By default the end user cannot resize the window.
        :param bool no_frame: This is used to control whether the window has a border and title bar visible. Please note that when no title bar is visible it can be harder for the user to re-position the window. By default the window is set to have a frame.
        :param bool vsync: This is used to determine if the window refresh rate will be synchronized with the current monitor refresh rate. This is by default set to :code:`True` as this can improve application efficiency and reduce visual tearing.
        :param str icon: This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.
        :param bool centered: This is used to set the window to be centered in the currently active window when created. The currently active window is typically the one the mouse cursor is in when the window is created. This defaults to :code:`True` ensuring the window is centered on screen. This does not prevent the window from being moved later on.
        :param bool maximized: This is used to determine if the window should be considered as being in a maximized state. The default value here is :code:`True`.

        .. note:: This method must be called before any rendering can occur.
        .. note:: Certain display settings can only be set at the time of window creation. If you need to change these settings, you will need to recreate the window. We are working on making this process easier.
        .. note:: Only one PMMA display can be created at a time. You can have multiple display instances but they will all share the same object behind the scenes. This is something we are looking to address in a future version of PMMA.
        """
        ...

    def center_window(self) -> None:
        """
        This method is used to position the window centrally in the monitor the window was first created on.

        .. note:: We are working on a way to have this center the window to whichever monitor it is currently on.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    @Utility.require_render_thread
    def clear(self) -> None:
        """
        This method is used to clear all rendered graphics from the previous frame, and also used to apply the specified background color defined in :code:`Display.window_fill_color`.

        .. note:: This method must be called from the same thread that the window was created in.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_window_in_focus(self) -> None:
        """
        This method is used to force the created window to be put into focus.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_window_minimized(self, value: bool) -> None:
        """
        This method is used to minimize the created window (to the taskbar or equivalent on your operating system).

        :param bool value: When :code:`True` the display will be minimized. When :code:`False` the display will be returned to its original state (not maximized).

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_window_maximized(self, value: bool) -> None:
        """
        This method is used to maximize the created window to fill the current monitor, showing the title bar.

        :param bool value: When :code:`True` the display will be maximized. When :code:`False` the display will be returned to its original state (not minimized).

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_icon(self, icon_path: str) -> None:
        """
        This method is used to pass an image file path to the display to be used as an icon, which replaces the default icon.

        :param str caption: This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_caption(self, caption: str) -> None:
        """
        This method is used to pass a string to use as the display caption.

        :param str caption: The window title name.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_relative_window_position(self, position: Integer1D) -> None:
        """
        This method is used to set the window to be positioned on-screen relative to the origin of the current monitor (the top left corner).

        :param Union[npt.NDArray[np.int32], npt.NDArray[np.int8], npt.NDArray[np.int16], npt.NDArray[np.int64], Iterable[int]] position: The number of pixels to move the window to. This takes two values (x, y).

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def set_absolute_window_position(self, position: Integer1D) -> None:
        """
        This method is used to set the window to be positioned on-screen relative to the windowing system's origin (typically the top left corner of the left-most monitor as arranged on your desktop).

        :param Union[npt.NDArray[np.int32], npt.NDArray[np.int8], npt.NDArray[np.int16], npt.NDArray[np.int64], Iterable[int]] position: The number of pixels to move the window to. This takes two values (x, y).

        .. note:: Please be aware that some monitor layouts will have 'gaps' between each monitor due to their arrangement or resolution. Care should be taken to not place the window in this area as it will not be seen.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    @Utility.require_render_thread
    def refresh(self, min_refresh_rate: int=5,
            max_refresh_rate: NoneInt=None,
            limit_refresh_rate: bool=True,
            lower_refresh_rate_on_minimize: bool=True,
            lower_refresh_rate_on_focus_loss: bool=True,
            lower_refresh_rate_on_low_battery: bool=True) -> None:
        """
        This method is used to update the window to show all the content rendered since :code:`Display.clear`. Additionally, it is used to limit the refresh rate of the window to avoid excessive resource usage.

        When the window is created with :code:`vsync=True` the refresh rate of the window will be forced to the monitor refresh rate. Otherwise, the refresh rate will be dynamically adjusted to save resources. This behaviour is customizable using the parameters below.

        :param int min_refresh_rate: The minimum refresh rate to dynamically adjust down to. If this value is 0, then the display will be updated only when nessasary (most efficient), this will **not** break window functionality.
        :param Union[int, None] max_refresh_rate: The maximum refresh rate to dynamically adjust up to. There is no guarantee this value will be achieved - but the window should not refresh at a faster rate for extended period of times. If set to :code:`None` the window will not have a capped refresh rate (generally not advised).
        :param bool limit_refresh_rate: This is used to completely disable any dynamic refresh rate behaviour and force the window to refresh as fast as possible. **This is not recommended for most use-cases, but could be useful for performance testing.**
        :param bool lower_refresh_rate_on_minimize: This is used to customize the dynamic refresh rate behaviour. If :code:`True` then when the window is minimized the refresh rate of the window will drop. If :code:`False` the refresh rate of the window will not change when the window is minimized.
        :param bool lower_refresh_rate_on_focus_loss: This is used to customize the dynamic refresh rate behaviour. If :code:`True` then when the window is not in focus the refresh rate of the window will drop. If :code:`False` the refresh rate of the window will not change when the window is not in focus.
        :param bool lower_refresh_rate_on_low_battery: This is used to customize the dynamic refresh rate behaviour. If :code:`True` then when the device is in a 'low power state' the refresh rate of the window will drop. If :code:`False` the refresh rate of the window will not change when the device is in a 'low power state'.

        .. note:: If you set :code:`min_refresh_rate` to 0, the display will be refreshed when the user interacts with it or when the rendered content on-screen changes. This created a highly-efficient behaviour seen in most desktop applications and is generally recommended.
        .. note:: This method must be called from the same thread that the window was created in.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def trigger_event_refresh(self) -> None:
        """
        This method is used to force the window to refresh. This works even when :code:`min_refresh_rate` is 0.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_caption(self) -> str:
        """
        This method is used to get the window caption.

        :returns str: The window caption as a string.
        """
        ...

    def get_center(self, object_size: Union[None, Integer1D]=None) -> Integer1D:
        """
        This method is used to get the center point of the window.

        :returns Union[npt.NDArray[np.int32], npt.NDArray[np.int8],npt.NDArray[np.int16],npt.NDArray[np.int64],Iterable[int]]: The center point as a coordinate (x, y).

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_aspect_ratio(self) -> float:
        """
        This method is used to get the aspect ratio of the window.

        :returns float: The window aspect ratio. For example: 2.667 would be returned for a window with aspect ration 16:9.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_frame_rate(self) -> int:
        """
        This method is used to get the current frame rate of the window.

        :returns int: The refresh rate of the window.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_frame_time(self) -> float:
        """
        This method is used to get the current frame time of the window.

        :returns float: The time in seconds between the current and previous frame.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_width(self) -> int:
        """
        This method gets the current window width in pixels.

        :returns int: The window width in pixels.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_height(self) -> int:
        """
        This method gets the current window height in pixels.

        :returns int: The window height in pixels.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_size(self) -> Integer1D:
        """
        This method gets the current size of the window in pixels (width, height)

        :returns Union[npt.NDArray[np.int32], npt.NDArray[np.int8],npt.NDArray[np.int16],npt.NDArray[np.int64],Iterable[int]]: The size of the window in pixels.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_msaa_samples(self) -> int:
        """
        This method is used to get the number of Multi-Sample Anti-Aliasing samples.

        :returns int: The number of samples.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def get_current_monitor_refresh_rate(self) -> int:
        """
        This method gets the refresh rate of the current monitor video mode.

        :returns int: The current monitor video mode refresh rate.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def toggle_full_screen(self) -> None:
        """
        This method is used to switch the window between full screen and windowed modes.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_in_focus(self) -> bool:
        """
        This method is used to get if the window is currently in focus.

        :returns bool: Returns :code:`True` when in focus. Returns :code:`False` when not in focus.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_minimized(self) -> bool:
        """
        This method is used to get if the window is currently minimized.

        :returns bool: Returns :code:`True` when the window is minimized. Returns :code:`False` when the window is not minimized.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_resizable(self) -> bool:
        """
        This method is used to get if the window is resizable.

        :returns bool: Returns :code:`True` when the window is able to be resized by the end user. Returns :code:`False` when the window is not resizable by the end user.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_visible(self) -> bool:
        """
        This method is used to get if the window is currently visible on-screen.

        :returns bool: Returns :code:`True` when the window is visible. Returns :code:`False` when the window is not visible.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_always_on_top(self) -> bool:
        """
        This method is used to get if the window is set to be always on top.

        :returns bool: Returns :code:`True` when the window is always on top. Returns :code:`False` when the window is not always on top.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_auto_minimized(self) -> bool:
        """
        This method is used get if the window is set to automatically minimize when it is no longer in focus. This is typically seen in game applications.

        :returns bool: Returns :code:`True` when the window is configured to automatically minimize when focus is lost. Returns :code:`False` when the window is not configured to automatically minimize when focus is lost.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_maximized(self) -> bool:
        """
        This method is used to get if the window is currently maximized.

        :returns bool: Returns :code:`True` when the window is maximized. Returns :code:`False` when the window is not maximized.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...

    def is_window_using_vsync(self) -> bool:
        """
        This method is used to get if the window is set to use vsync. Note that this does not check if vsync is supported in your setup, as this varies based on third party factors that we cannot check.

        :returns bool: Returns :code:`True` when vsync is used. Returns :code:`False` when the window is not using vsync.

        .. warning:: A valid window must be created using :code:`Display.Create` before calling this method.
        """
        ...