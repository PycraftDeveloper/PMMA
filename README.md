<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# PMMA (Python Multi-Media API)
PMMA is a Python library aimed at improving application development in Python.
Typically, developing applications in Python necessitates familiarity with a variety of different libraries such as [Pygame](https://github.com/pygame/pygame), [ModernGL](https://github.com/moderngl/moderngl), [PIL](https://github.com/python-pillow/Pillow) and [Numpy](https://github.com/numpy/numpy). PMMA aims to simplify the application development process by creating a single interface that provides easy access to simple and advanced pre-written and highly optimised application development utilities, whilst still also allowing these utilities to be expanded upon by exposing their underlying APIs.

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
Bear with me, there are a fair few!

* Object Oriented Programming - Most of PMMA exists as specific objects, making it super easy to customize what you want.
  * [Cython](https://github.com/cython/cython) and JIT ([Numba](https://github.com/numba/numba)) acceleration - Where native Python is "too slow" we switch it out for these alternatives, dynamically choosing at runtime which one is fastest.
* GPU accelerated - PMMA can use GPU acceleration for 2D and 3D rendering.
* Advanced mathematics - PMMA includes highly-optimized commonly used mathematical functions.
* Advanced threading - PMMA includes an advanced form of the Threading library, which extends its existing functionality to include the ability to kill threads on the fly.
* Advanced Tkinter - PMMA includes some advanced Tkinter functions, like getting window size, and default operating system fonts.
* Simple shared memory - PMMA allows you to have a shared memory space for variables, as a replacement for global variables, which can be accessed easily through threads.
* Dynamic color and coordinates - PMMA can easily convert between different color and coordinate formats.
* Pipelines - PMMA uses these to allow for the bulk execution of functions, typically for rendering purposes.
* Easy display management - PMMA allows you to easily manage your application window, including size, captions, display modes and v-sync.
* Efficient shape rendering - PMMA includes support for a wide range of shapes, and can render these using GPU acceleration.
* Advanced memory management - PMMA will automatically manage large objects stored in memory.
* Image manipulation - PMMA will automatically convert image formats as needed for your application, and cache them for improved performance.
* Fast noise generation - PMMA can very efficiently create noise patterns in 1D, 2D or 3D.
* Application customization - PMMA can be told details about your application, and dynamically change its behavior.
* Efficient text rendering - PMMA can render and format text easily, with its own formatting language and powerful appearance controls.
* Video playback - PMMA can play back videos from a file, in your application.

_Note: GPU acceleration is only available when using the rendering pipeline with either the default (Pygame) or Pyglet graphics API._
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

We are currently working on improving the design of PMMA, bear with us as we continue to make changes over the next few days!