Display (``pmma.CPP_Display``)
===============================

This class is responsible for managing the display window, including its creation, configuration, and properties. It provides methods to manipulate the window's state, such as minimizing, maximizing, and setting its position. Additionally, it offers functionality to retrieve information about the display, such as its size, aspect ratio, and frame rate.

Create
------

.. cpp:class:: CPP_Display

    This creates a new Display object.

    .. note:: This does not create the actual window. You must call the :py:meth:`~pmma.Display.create` method to create the window.

Structs
-------

.. cpp:class:: CPP_Display_Create_Kwargs

    A struct used to more easily customize the default arguments when creating a display.

    .. cpp:member:: std::string Caption = "PMMA Display"

        The window title name.

    .. cpp:member:: std::string IconPath = ""

        This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.

    .. cpp:member:: std::optional<bool> OptionalFullScreen = std::nullopt

        This is used to control if the window should be full screen or not. If the value is left as the default :code:`std::nullopt` PMMA will set the window to be automatically full screened when the window size is (0, 0).

    .. cpp:member:: bool Resizable = false

        This is used to control whether the window can be resized by the user. By default the end user cannot resize the window.

    .. cpp:member:: bool NoFrame = false

        This is used to control whether the window has a border and title bar visible. Please note that when no title bar is visible it can be harder for the user to re-position the window. By default the window is set to have a frame.

    .. cpp:member:: bool Vsync = true

        This is used to determine if the window refresh rate will be synchronized with the current monitor refresh rate. This is by default set to :code:`true` as this can improve application efficiency and reduce visual tearing.

    .. cpp:member:: bool Centered = true

        This is used to set the window to be centered in the currently active window when created. The currently active window is typically the one the mouse cursor is in when the window is created. This defaults to :code:`true` ensuring the window is centered on screen. This does not prevent the window from being moved later on.

    .. cpp:member:: bool Maximized = false

        This is used to determine if the window should be considered as being in a maximized state. The default value here is :code:`true`.

.. cpp:class:: CPP_Display_Refresh_Kwargs

    A struct used to more easily customize the default arguments when refreshing a display.

    .. cpp:member:: unsigned int MinRefreshRate = 5

        The minimum refresh rate to dynamically adjust down to. If this value is 0, then the display will be updated only when nessasary (most efficient), this will **not** break window functionality.

    .. cpp:member:: std::optional<unsigned int> MaxRefreshRate = std::nullopt

        The maximum refresh rate to dynamically adjust up to. There is no guarantee this value will be achieved - but the window should not refresh at a faster rate for extended period of times. If set to :code:`std::nullopt` the window will not have a capped refresh rate (generally not advised).

    .. cpp:member:: bool LimitRefreshRate = true

        This is used to completely disable any dynamic refresh rate behaviour and force the window to refresh as fast as possible. **This is not recommended for most use-cases, but could be useful for performance testing.**

    .. cpp:member:: bool LowerRefreshRate_OnMinimize = true

        This is used to customize the dynamic refresh rate behaviour. If :code:`true` then when the window is minimized the refresh rate of the window will drop. If :code:`false` the refresh rate of the window will not change when the window is minimized.

    .. cpp:member:: bool LowerRefreshRate_OnFocusLoss = true

        This is used to customize the dynamic refresh rate behaviour. If :code:`true` then when the window is not in focus the refresh rate of the window will drop. If :code:`false` the refresh rate of the window will not change when the window is not in focus.

    .. cpp:member:: bool LowerRefreshRate_OnLowBattery = true

        This is used to customize the dynamic refresh rate behaviour. If :code:`true` then when the device is in a ‘low power state’ the refresh rate of the window will drop. If :code:`false` the refresh rate of the window will not change when the device is in a ‘low power state’.

Methods
-------

.. cpp:function:: void CPP_Display::Create(unsigned int* NewSize, CPP_Display_Create_Kwargs kwargs = {})

    This method is used to create a window which will be the rendering target for PMMA. All 2D and 3D content will end up being rendered to this window.

    :param unsigned int NewSize: The size of the window in pixels. If set to (0, 0) the window will be created at the current monitor's resolution and be automatically full-screen. For this method you can input either an iterable Python sequence (list or tuple for example) or a numpy array. All inputs are converted automatically to be a continuous uint32 (or unsigned int 32) numpy array - its unlikely this conversion will be slow in this scenario.
    :param CPP_Display_Create_Kwargs kwargs: Used to customize the default window parameters.

    .. note:: This method must be called before any rendering can occur.
    .. note:: Certain display settings can only be set at the time of window creation. If you need to change these settings, you will need to recreate the window. We are working on making this process easier.
    .. note:: Only one PMMA display can be created at a time. You can have multiple display instances but they will all share the same object behind the scenes. This is something we are looking to address in a future version of PMMA.

.. cpp:function:: void CPP_Display::CenterWindow()

    This method is used to position the window centrally in the monitor the window was first created on.

    .. note:: We are working on a way to have this center the window to whichever monitor it is currently on.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::Clear()

    This method is used to clear all rendered graphics from the previous frame, and also used to apply the specified background color defined in :code:`Display.window_fill_color`.

    .. note:: This method must be called from the same thread that the window was created in.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::SetWindowInFocus()

    This method is used to force the created window to be put into focus.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::GetIsWindowMinimized(bool value)

    This method is used to minimize the created window (to the taskbar or equivalent on your operating system).

    :param bool value: When :code:`true` the display will be minimized. When :code:`false` the display will be returned to its original state (not maximized).

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::SetWindowMaximized(bool value)

    This method is used to maximize the created window to fill the current monitor, showing the title bar.

    :param bool value: When :code:`true` the display will be maximized. When :code:`false` the display will be returned to its original state (not minimized).

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::SetIcon(std::string icon_path)

    This method is used to pass an image file path to the display to be used as an icon, which replaces the default icon.

    :param std::string icon_path: This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::SetCaption(std::string caption)

    This method is used to pass a string to use as the display caption.

    :param std::string caption: The window title name.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::SetRelativeWindowPosition(unsigned int* position)

    This method is used to set the window to be positioned on-screen relative to the origin of the current monitor (the top left corner).

    :param unsigned int* position: The number of pixels to move the window to. This takes two values (x, y).

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::SetAbsoluteWindowPosition(unsigned int* position)

    This method is used to set the window to be positioned on-screen relative to the windowing system's origin (typically the top left corner of the left-most monitor as arranged on your desktop).

    :param unsigned int* position: The number of pixels to move the window to. This takes two values (x, y).

    .. note:: Please be aware that some monitor layouts will have 'gaps' between each monitor due to their arrangement or resolution. Care should be taken to not place the window in this area as it will not be seen.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::Refresh(CPP_Display_Refresh_Kwargs kwargs = {})

    This method is used to update the window to show all the content rendered since :code:`Display.clear`. Additionally, it is used to limit the refresh rate of the window to avoid excessive resource usage.

    When the window is created with :code:`vsync=True` the refresh rate of the window will be forced to the monitor refresh rate. Otherwise, the refresh rate will be dynamically adjusted to save resources. This behaviour is customizable using the parameters below.

    :param CPP_Display_Refresh_Kwargs kwargs: Used to customize the default refresh parameters.

    .. note:: If you set :code:`min_refresh_rate` to 0, the display will be refreshed when the user interacts with it or when the rendered content on-screen changes. This created a highly-efficient behaviour seen in most desktop applications and is generally recommended.
    .. note:: This method must be called from the same thread that the window was created in.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::TriggerEventRefresh()

    This method is used to force the window to refresh. This works even when :code:`min_refresh_rate` is 0.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: std::string CPP_Display::GetCaption()

    This method is used to get the window caption.

    :returns std::string: The window caption as a string.

.. cpp:function:: void CPP_Display::GetCenterPosition(unsigned int* out)

    This method is used to get the center point of the window.

    :param unsigned int* out: The center point as a coordinate (x, y).

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::GetCenterPosition(unsigned int* ObjectSize, unsigned int* out)

    This method is used to get the center point of the window.

    :param unsigned int* ObjectSize: The size in the format (x, y) to offset the center position.
    :param unsigned int* out: The output center point as a coordinate (x, y).

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: float CPP_Display::GetAspectRatio()

    This method is used to get the aspect ratio of the window.

    :returns float: The window aspect ratio. For example: 2.667 would be returned for a window with aspect ration 16:9.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: unsigned int CPP_Display::GetFrameRate()

    This method is used to get the current frame rate of the window.

    :returns unsigned int: The refresh rate of the window.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: float CPP_Display::GetFrameTime()

    This method is used to get the current frame time of the window.

    :returns float: The time in seconds between the current and previous frame.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: unsigned int CPP_Display::GetWidth()

    This method gets the current window width in pixels.

    :returns unsigned int: The window width in pixels.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: unsigned int CPP_Display::GetHeight()

    This method gets the current window height in pixels.

    :returns unsigned int: The window height in pixels.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::GetSize(int* out)

    This method gets the current size of the window in pixels (width, height)

    :param int* out: The output size of the window in pixels.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: unsigned int CPP_Display::GetWindow_MSAA_Samples()

    This method is used to get the number of Multi-Sample Anti-Aliasing samples.

    :returns unsigned int: The number of samples.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: unsigned int CPP_Display::GetCurrentMonitorRefreshRate()

    This method gets the refresh rate of the current monitor video mode.

    :returns unsigned int: The current monitor video mode refresh rate.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::ToggleFullScreen()

    This method is used to switch the window between full screen and windowed modes.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowInFocus()

    This method is used to get if the window is currently in focus.

    :returns bool: Returns :code:`true` when in focus. Returns :code:`false` when not in focus.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowMinimized()

    This method is used to get if the window is currently minimized.

    :returns bool: Returns :code:`true` when the window is minimized. Returns :code:`false` when the window is not minimized.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowMaximized()

    This method is used to get if the window is currently maximized.

    :returns bool: Returns :code:`true` when the window is maximized. Returns :code:`false` when the window is not maximized.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowResizable()

    This method is used to get if the window is resizable.

    :returns bool: Returns :code:`true` when the window is able to be resized by the end user. Returns :code:`false` when the window is not resizable by the end user.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowVisible()

    This method is used to get if the window is currently visible on-screen.

    :returns bool: Returns :code:`true` when the window is visible. Returns :code:`false` when the window is not visible.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowAlwaysOnTop()

    This method is used to get if the window is set to be always on top.

    :returns bool: Returns :code:`true` when the window is always on top. Returns :code:`false` when the window is not always on top.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowUsingVsync()

    This method is used to get if the window is set to use vsync. Note that this does not check if vsync is supported in your setup, as this varies based on third party factors that we cannot check.

    :returns bool: Returns :code:`true` when vsync is used. Returns :code:`false` when the window is not using vsync.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: bool CPP_Display::GetIsWindowAutoMinimize()

    This method is used get if the window is set to automatically minimize when it is no longer in focus. This is typically seen in game applications.

    :returns bool: Returns :code:`true` when the window is configured to automatically minimize when focus is lost. Returns :code:`false` when the window is not configured to automatically minimize when focus is lost.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

.. cpp:function:: void CPP_Display::GetOrthographicProjection(float* out)

    This method is used to get the display's orthographic projection.

    :param float* out: The output projection matrix.

    .. warning:: A valid window must be created using :code:`CPP_Display::Create` before calling this method.

Attributes
----------