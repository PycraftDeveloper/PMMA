Display (``pmma.Display``)
===============================

This class is responsible for managing the display window, including its creation, configuration, and properties. It provides methods to manipulate the window's state, such as minimizing, maximizing, and setting its position. Additionally, it offers functionality to retrieve information about the display, such as its size, aspect ratio, and frame rate.

Create
------

.. py:class:: pmma.Display() -> pmma.Display

    This creates a new Display object.

    .. note:: This does not create the actual window. You must call the :py:meth:`~pmma.Display.create` method to create the window.

Methods
-------

.. py:method:: Display.create(size: Union[npt.NDArray[np.int32], npt.NDArray[np.int8], npt.NDArray[np.int16], npt.NDArray[np.int64], Iterable[int]]=np.array([0, 0], dtype=np.uint32, order='C'), caption: str="PMMA Display", fullscreen: Union[None, bool]=None, resizable: bool=False, no_frame: bool=False, vsync: bool=False, icon: str="", centered: bool=True, maximized: bool=False, transparent: bool=False) -> None

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
    :param bool transparent: This is used to determine if the window should be clear when created. This allows you to break away from the classic box shaped window arrangement and is especially effective when used in conjunction with 'no-frame'. Please note however that this does not guarantee the window is going to be transparent - that depends on the operating system and graphics drivers so it cannot be considered as reliable at this stage. We are working to address this.

    .. note:: This method must be called before any rendering can occur.
    .. note:: Certain display settings can only be set at the time of window creation. If you need to change these settings, you will need to recreate the window. We are working on making this process easier.
    .. note:: Only one PMMA display can be created at a time. You can have multiple display instances but they will all share the same object behind the scenes. This is something we are looking to address in a future version of PMMA.

.. py:method:: Display.center_window() -> None

    This method is used to position the window centrally in the monitor the window was first created on.

.. py:method:: Display.clear() -> None

    🟩 **R** -

.. py:method:: Display.set_window_in_focus() -> None

    🟩 **R** -

.. py:method:: Display.set_window_minimized() -> None

    🟩 **R** -

.. py:method:: Display.set_window_maximized() -> None

    🟩 **R** -

.. py:method:: Display.set_icon() -> None

    🟩 **R** -

.. py:method:: Display.set_caption() -> None

    🟩 **R** -

.. py:method:: Display.set_relative_window_position() -> None

    🟩 **R** -

.. py:method:: Display.set_absolute_window_position() -> None

    🟩 **R** -

.. py:method:: Display.refresh() -> None

    🟩 **R** -

.. py:method:: Display.trigger_event_refresh() -> None

    🟩 **R** -

.. py:method:: Display.get_caption() -> str

    🟩 **R** -

.. py:method:: Display.get_center() -> Union[npt.NDArray[np.int32], npt.NDArray[np.int8],npt.NDArray[np.int16],npt.NDArray[np.int64],Iterable[int]]

    🟩 **R** -

.. py:method:: Display.get_aspect_ratio() -> float

    🟩 **R** -

.. py:method:: Display.get_frame_rate() -> int

    🟩 **R** -

.. py:method:: Display.get_frame_time() -> float

    🟩 **R** -

.. py:method:: Display.get_width() -> int

    🟩 **R** -

.. py:method:: Display.get_height() -> int

    🟩 **R** -

.. py:method:: Display.get_size() -> Union[npt.NDArray[np.int32], npt.NDArray[np.int8],npt.NDArray[np.int16],npt.NDArray[np.int64],Iterable[int]]

    🟩 **R** -

.. py:method:: Display.get_msaa_samples() -> int

    🟩 **R** -

.. py:method:: Display.get_current_monitor_refresh_rate() -> int

    🟩 **R** -

.. py:method:: Display.toggle_full_screen() -> None

    🟩 **R** -

.. py:method:: Display.is_window_in_focus() -> bool

    🟩 **R** -

.. py:method:: Display.is_window_minimized() -> bool

    🟩 **R** -

.. py:method:: Display.is_window_maximized() -> bool

    🟩 **R** -

.. py:method:: Display.is_window_resizable() -> bool

    🟩 **R** -

.. py:method:: Display.is_window_visible() -> bool

    🟩 **R** -

.. py:method:: Display.is_window_always_on_top() -> bool

    🟩 **R** -

.. py:method:: Display.is_window_using_vsync() -> bool

    🟩 **R** -

Attributes
----------

.. py:attribute:: Display.window_fill_color

    🟩 **R** -