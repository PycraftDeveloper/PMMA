<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# PMMA (Python Multi-Media API)
⚠️ This is the DEVELOPMENT version for PMMA 5.0.0 and is NOT meant for routine use yet. ⚠️


PMMA is a Python library aimed at improving application development in Python.
Typically, developing applications in Python necessitates familiarity with a variety of different libraries such as [Pygame](https://github.com/pygame/pygame), [ModernGL](https://github.com/moderngl/moderngl), [PIL](https://github.com/python-pillow/Pillow) and [Numpy](https://github.com/numpy/numpy). PMMA aims to simplify the application development process by creating a single interface that provides easy access to simple and advanced pre-written and highly optimised application development utilities, whilst still also allowing these utilities to be expanded upon by exposing their underlying APIs.

## Progress on PMMA v5.0.0

![Progress on PMMA v5.0.0](https://geps.dev/progress/40)

Each entry is worth: (20/7) %

* ✅ - Setup new repository structure
* ✅ - Setup new repository automation
* ✅ - Finished Advanced Mathematics component
* ✅ - Finished Perlin Noise component
* ✅ - Finished Fractal Brownian Motion
* ✅ - Finished Backpack
* ✅ - Finished Number Converter
* ✅ - Finished Audio
* ✅ - Finished GPU
* ✅ - Finished Executor
* ✅ - Finished Advanced Tkinter
* ⏳ - Working on Video
* ⏳ - Working on Display
* ⏳ - Working on Events
* ⏳ - Working on OpenGL
* ⏳ - Working on Logging
* ⏳ - Working on General
* 🛑 - Not started Advanced Threading
* 🛑 - Not started Camera
* 🛑 - Not started Complex 2D shapes
* 🛑 - Not started Constants
* 🛑 - Not started Registry
* 🛑 - Not started Controller
* 🛑 - Not started Data Structures
* 🛑 - Not started Error
* 🛑 - Not started File
* 🛑 - Not started Formatters
* 🛑 - Not started Memory Manager
* 🛑 - Not started Quick Start
* 🛑 - Not started Recorder
* 🛑 - Not started Sampler
* 🛑 - Not started Settings
* 🛑 - Not started Shapes 2D
* 🛑 - Not started Transitions

## Contents

* [History](https://github.com/PycraftDeveloper/PMMA?tab=readme-ov-file#history)
* [Features](https://github.com/PycraftDeveloper/PMMA?tab=readme-ov-file#features)
* [Optional Dependencies](https://github.com/PycraftDeveloper/PMMA?tab=readme-ov-file#optional-dependencies)
* * [Cython](https://github.com/PycraftDeveloper/PMMA?tab=readme-ov-file#cython)
* [Final Notes](https://github.com/PycraftDeveloper/PMMA?tab=readme-ov-file#final-notes)

## History
I, ([PycraftDev](https://github.com/PycraftDeveloper)), joined GitHub to make the video game [Pycraft](https://github.com/PycraftDeveloper/Pycraft) in public using the programming language Python. Initially, my progress wasn't very methodical. I started with the basic game loop and worked out how different Python libraries interacted with each other. When I found that my design was slow, I went back and optimized it.

After many years of development and optimization, I gained extensive knowledge of making certain aspects of application development in Python really fast and performant. With that in mind, I started writing utility programs for Pycraft, which handled all of this behind the scenes, leaving the main programs much cleaner for their aggregation into my project - a video game.

As I worked on other projects, I found myself copying over these utility programs, revising them and gradually evolving my implementation of specific functions or classes. Eventually, this set of utility programs grew to be longer typically than the applications using them, and I decided it was time to separate my applications into two: the application itself, and PMMA.

## Features
* Object-Oriented Programming—Most of PMMA exists as specific objects, making it super easy to customize what you want.
* [Cython](https://github.com/cython/cython) acceleration - Where native Python is "too slow" we switch it out for this alternative whenever possible.
* GPU accelerated - PMMA can use GPU acceleration for 2D and 3D rendering.
* Advanced mathematics - PMMA includes highly optimised commonly used mathematical functions.
* Advanced threading - PMMA includes an advanced form of the Threading library, which extends its existing functionality to include the ability to kill threads on the fly.
* Advanced Tkinter - PMMA includes some advanced Tkinter functions, like getting window size and default operating system fonts.
* Simple shared memory - PMMA allows you to have a shared memory space for variables as a replacement for global variables, which can be accessed easily through threads.
* Dynamic colour, coordinate, time, angle, and scalars—PMMA easily converts between different formats, so you can work with whatever is easiest for you!
* Easy display management - PMMA allows you to easily manage your application window, including size, captions, display modes and v-sync.
* Efficient shape rendering—PMMA supports a wide range of shapes and can render them using GPU acceleration.
* Advanced memory management - PMMA will automatically manage large objects stored in memory.
* Fast noise generation - PMMA can very efficiently create noise patterns in 1D, 2D or 3D.
* Application customization—PMMA can be told details about your application and dynamically change its behaviour or how it appears to the operating system!
* Video playback - PMMA can play back videos from a file, in your application. This is done by streaming the data from the disk, so wave goodbye to long video loading times and high memory usage.
* Simplified Audio playback - PMMA includes support for very efficient audio playback, including steaming music directly from a file instead of reading the whole file at once. This is additionally supplemented with a range of additional controls like the ability to loop or pan audio and change its volume back.
* Realtime Effects - PMMA can be used to apply effects to audio in real-time.
* Transitions—PMMA can automatically manage the animation of values and coordinates for you in a variety of different styles. This is useful for moving objects about onscreen.
* Advanced GPU information collection - PMMA can gather extremely detailed information about all installed GPUs.
* Easy multi-device input—PMMA will automatically handle any additional controllers connected to your system, allowing you to interface easily with these devices. It even includes support for effects like Rumble!
* Event management—PMMA will automatically update event objects in the background, allowing you to easily choose which events you need in your application. This idea has also been extended to detect when some events have been triggered in quick succession, like a double-tapped key (with per-key timings if needed).
* Simple file systems – PMMA will automatically resolve file paths for you and can even scan project directories and produce unique user-friendly names for your files, which you can use instead!
* Advanced data structures – PMMA includes access to fast implementations for advanced data structures like stacks, queues, circular queues, priority queues, priority stacks, inverted priority queues, inverted priority stacks, priority lists and inverted priority lists.
* Command Execution—PMMA includes a super simple way for you to run command-line-level commands for your application, including the ability to get the result from the command in real time!
* Projections—PMMA can automatically create and easily create projections that match your PMMA display for use in your 3D scenes.
* OpenGL objects—PMMA includes its own wrapper for OpenGL through ModernGL, with a much simpler interface and the usual performance improvements thrown in.
* Dynamic GPU allocation - PMMA can automatically try to distribute some graphics tasks to multiple installed GPUs to spread the load across all the available hardware.
* Pipelines—PMMA combines complex 2D and 3D objects and renders them simultaneously, significantly improving performance.

_Note: PMMA is still undergoing active development, and some features will be changed, added or extended in the near future - we will attempt to include backwards compatibility where possible._

## Optional Dependencies

### Cython

PMMA can take advantage of Cython compilation. This converts PYX files into C or C++. To do this, we would recommend GCC or MSVC, as they have written support in PMMA - you can use another compiler, or potentially even use pre-compiled binaries, but note you might get very slightly reduced performance in some applications.

To install GCC:
* On Windows: https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/ or https://www.supportyourtech.com/tech/how-to-install-gcc-on-windows-11-a-step-by-step-guide-for-beginners/
* On Linux: https://linuxcapable.com/how-to-install-gcc-compiler-on-ubuntu-linux/ or https://linuxconfig.org/how-to-install-gcc-compiler-in-redhat-linux-8
* On MacOS: https://macreports.com/how-to-install-gcc-on-your-mac/

To install MSVC:
* On Windows: https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170
* On Linux: MSVC isn't supported directly, although possible to use through WINE, I'd recommend GCC here.
* On MacOS: I'd recommend GCC here but otherwise: https://learn.microsoft.com/en-us/visualstudio/mac/installation?view=vsmac-2022

_Note: I am working on supporting additional compilers directly, however they should already work - they just haven't been tested yet_

## Final Notes

PMMA is still in active development. PLease bear with us as we continue to make changes, and consult the documentation for advise on what features are 'safe to use'!
