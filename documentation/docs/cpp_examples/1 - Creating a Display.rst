1 - Creating a Display
======================

This example shows how to create a simple responsive display using PMMA in C++.
This example has the same functionality as the Python version with the same name.

.. code-block:: cpp

    #include <PMMA_Core.hpp>

    using namespace std;

    int main() {
        // PMMA must be initialized with a parameter telling it where it exists on the drive.
        // This is needed for resource loading.
        string path = "W://Documents//GitHub//PMMA//pmma";
        PMMA_Initialize(path);

        // Create a display object.
        CPP_Display* display = new CPP_Display();
        unsigned int size[2] = { 1280, 720 };
        display->Create(size);

        // Start the main loop
        while (CPP_General::IsApplicationRunning()) {
            // Clear the display.
            display->Clear();

            // Refresh the display to show any updates and limit refresh rate.
            display->Refresh();
        }

        // Make sure to uninitialize PMMA so it cleans up properly when exiting.
        PMMA_Uninitialize();
        return 0;
    }

Detailed Breakdown
------------------

The above code block is one of the most fundamental building blocks of any graphical application using PMMA. The display is where we will render (or draw however we will be using rendering as the key work for all future examples) all of our 2D and 3D graphics. In addition to creating a display, this code also sets up a main loop (or game loop) that will keep the application running until the user decides to close it, which is handled by the :code:`pmma.General.is_application_running()` method.

In this code example the :code:`pmma.Display()` class is used to create a new display object. This object represents the window or screen where all graphical content will be rendered. The :code:`display.create` method is then use to create the actual window with any specific customization options we would like to use. In this case we are simply setting the window size to 1280x720 pixels, which is a common resolution for many applications. If you do not specify a size, PMMA will default to a full-screen window using the current display resolution. If you specify a size, by default PMMA will create a windowed display, but you can also specify that you would like a full-screen display by passing the :code:`fullscreen=True` key-word argument to the :code:`display.create()` method. There are many other customization options available when creating a display, for more information on these options please refer to the official PMMA documentation. Please note that some of the parameters available for the :code:`display.create()` method may not be adjusted after the display has been created, so it is important to set them correctly when creating the display.

The :code:`pmma.General.is_application_running()` method checks if the application is still running and returns :code:`True` if it is, and :code:`False` if it has been requested to close. This is typically done by the user clicking the close button on the window or in full-screen windows only, by pressing the 'Esc' key. This ensures that if you haven't yet implemented any event handling in your application, the user can still close the application gracefully. We appreciate that :code:`pmma.General.is_application_running()` may seem a bit verbose, but it is designed to be explicit and clear about its purpose. If you find yourself using contents from :code:`pmma.General` frequently, consider an approach where you associate this portion of the API with a name. In the case of the short example below, we renamed :code:`pmma.General` to :code:`general` for brevity.

.. code-block:: python
    # This needs to change as general is not a definable sub-component here for C++.
    import pmma

    general = pmma.General

    # Create a display object
    display = pmma.Display()

    # Set the title of the display window
    display.create([1280, 720])

    # Start the main loop
    while general.is_application_running():
        # Clear the display
        display.clear()

        # Perform any rendering here...

        # Refresh the display to show any updates and limit refresh rate
        display.refresh()

The :code:`display.clear()` method is used to clear the display at the beginning of each iteration of the main loop. This ensures that any previous drawings are removed before we draw new content. Whilst you may want to keep the contents of the previous frame, it is generally a bad idea to omit this step as it makes the display more vulnerable to graphical glitches and artifacts - like for example when resizing the window, maximizing or minimizing it or if you have any on-screen overlays like MSI Afterburner's On Screen Display (OSD), which PMMA's display supports you using.

You should ensure that any rendering you wish to do is performed between the :code:`display.clear()` and :code:`display.refresh()` calls. The :code:`display.refresh()` method is responsible for updating the display with any new graphical content. Any rendering that occurs before :code:`display.clear()` will not be visible on the display, as it will be cleared away at the start of the next loop iteration, and the same applies for any rendering that occurs after :code:`display.refresh()`, as the display will not be updated again until the next loop iteration. Its also important to note that in PMMA, it is recommended that any content is only rendered once per loop iteration (in this situation also known as a frame), as rendering multiple times per frame may cause previous render calls to the same object to be ignored or changed in unexpected ways.

The :code:`display.refresh()` method also dynamically limits the refresh rate of the display, which can be beneficial for performance and power consumption. In the above example we have allowed PMMA to automatically use a feature called 'V-Sync' (Vertical Synchronization), which synchronizes the display's refresh rate with the monitor's refresh rate. This helps to prevent screen tearing and provides a smoother visual experience. If you wish to control wether V-Sync is used it can be adjusted when creating the display as shown in the example below:

.. code-block:: python

    import pmma

    # Create a display object
    display = pmma.Display()

    # Set the title of the display window with V-Sync disabled
    display.create([1280, 720], vsync=False)

    # Start the main loop
    while pmma.General.is_application_running():
        # Clear the display
        display.clear()

        # Perform any rendering here...

        # Refresh the display to show any updates and limit refresh rate
        display.refresh()

In the above example now V-Sync is disabled. PMMA will now dynamically adjust the refresh rate of the application dynamically based on how the application is interacted with and when content changes on-screen. The default behaviour is to go as low as 5 frames per second and as high as 60 frames per second. If you wish to set a custom frame rate limit, you can do so by passing integer values to the :code:`min_refresh_rate` and :code:`max_refresh_rate` key-word arguments of the :code:`display.refresh()` method as shown in the example below:

.. code-block:: python

    import pmma

    # Create a display object
    display = pmma.Display()

    # Set the title of the display window with V-Sync disabled
    display.create([1280, 720], vsync=False)

    # Start the main loop
    while pmma.General.is_application_running():
        # Clear the display
        display.clear()

        # Perform any rendering here...

        # Refresh the display to show any updates dynamically.
        display.refresh(min_refresh_rate=30, max_refresh_rate=120)

In addition to a manually specified refresh rate minimum and maximum, PMMA will also automatically adjust the refresh rate based on the current application context. This means that if the display is minimized, not in focus or the device is in power saving mode, PMMA will automatically reduce the refresh rate to conserve system resources. This behavior can be disabled or customized by adjusting the key-word arguments of the :code:`display.refresh()` method. For more information on these options, please refer to the official PMMA documentation.

Extensions
----------

Below are some additional examples of how you can further customize and extend the display created in the above example!

Did you can use :code:`display.window_fill_color` to set a custom color for the window (instead of being black which is the default), here is an example of this in action:

.. code-block:: python

    import pmma

    # Create a display object
    display = pmma.Display()

    # Set the title of the display window
    display.create([1280, 720])

    # Set the window fill color to a randomly selected color
    display.window_fill_color.generate_from_random()

    # Start the main loop
    while pmma.General.is_application_running():
        # Clear the display
        display.clear()

        # Perform any rendering here...

        # Refresh the display to show any updates and limit refresh rate
        display.refresh()

Please note though that setting the window fill color randomly every frame (yes, we have all done it!) can cause discomfort for some users and is generally not recommended for production applications. If you do wish to change the window fill color dynamically, consider using a more subtle approach, such as gradually changing the color over time or in response to user actions - as demonstrated below with a more advanced color generation technique:

.. code-block:: python

    import pmma, time

    # Create a display object
    display = pmma.Display()

    # Set the title of the display window
    display.create([1280, 720])

    # Configure the window_fill_color component to allow for support for
    # Perlin and Fractal Brownian Motion (FBM) noise generation for a
    # smoother color transition effect
    display.window_fill_color.configure()

    # Start the main loop
    while pmma.General.is_application_running():
        # Use 1D Perlin noise to generate a smooth color transition over time
        display.window_fill_color.generate_from_1D_perlin_noise(time.perf_counter())

        # Clear the display
        display.clear()

        # Perform any rendering here...

        # Refresh the display to show any updates and limit refresh rate
        display.refresh()

You can also set and change the window title or icon at any time using the :code:`display.set_title()` and :code:`display.set_icon()` methods respectively. Here is an example of changing the window title dynamically based on the current frame count:

.. code-block:: python

    import pmma

    # Create a display object
    display = pmma.Display()

    # Set the title of the display window
    display.create([1280, 720])

    frame_count = 0

    # Start the main loop
    while pmma.General.is_application_running():
        frame_count += 1

        # Update the window title with the current frame count
        display.set_title(f"Frame no.: {frame_count}")

        # Clear the display
        display.clear()

        # Perform any rendering here...

        # Refresh the display to show any updates and limit refresh rate
        display.refresh()