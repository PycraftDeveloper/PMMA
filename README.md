<div align="center">
  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# Python Multi-Media API (PMMA)
PMMA is a Python library designed to make the development of applications using the programming language Python easier and faster. Typically, application development in Python would require the developer to be familiar with a wide range of different libraries: (Pygame)[https://github.com/pygame/pygame], (ModernGL)[https://github.com/moderngl/moderngl], (PIL)[https://github.com/python-pillow/Pillow] and (Numpy)[https://github.com/numpy/numpy] for example. PMMA aims to change this idea of application development by combining all of those libraries - and more - together, along with optimized implementations of basic and advanced concepts, like window management, events management right through to shadow-mapping and advanced OpenGL.

## Contents

To Do

## Backstory
I (PycraftDev)[https://github.com/PycraftDeveloper] joined GitHub to make the video game (Pycraft)[https://github.com/PycraftDeveloper/Pycraft] in public, using the programming language Python. Whilst my initial progress wasn't very methodical, pretty much the first thing I would do, is start with the basic game loop, and work out how different Python libraries interacted with each other. Then, upon finding that my design was slow, I'd go back and optimize it.

After many years of going through this cycle of development and optimization, I ended up with a large bank of knowledge of how to make some aspects of application development in Python really fast, and performant. With that in mind, I started writing utility programs for Pycraft, which would handle all of this behind the scenes, leaving the main programs much cleaner for their aggregation into my project - a video game.

Then, as I started work on other projects (of which there are a fair few!) I found myself copying over these utility programs, revising them and gradually evolving my implementation of specific functions or classes. Eventually however, this set of utility programs grew to be longer typically than the applications using them, and I decided it was time to separate my applications into two: the application its' self, and PMMA.

## Features
Bear with me, there are a fair few!

* Object Oriented Programming - Most of PMMA exists as specific objects, making it super easy to customize what you want.
  * (Cython)[https://github.com/cython/cython] and JIT ((Numba)[https://github.com/numba/numba]) acceleration - Where native Python is "too slow" we switch it out for these alternatives, dynamically choosing at runtime which one is fastest.
* Machine Learning (ML) - Machine Learning is used to further optimize some areas of PMMA, by learning how you use it in your applications.
* GPU accelerated - PMMA can use GPU acceleration for 2D and 3D rendering.
* Advanced mathematics - PMMA includes highly-optimized commonly used mathematical functions.
* Advanced threading - PMMA includes an advanced form of the Threading library, which extends its existing functionality to include the ability to kill threads on the fly.
* Advanced Tkinter - PMMA includes some advanced Tkinter functions, like getting window size, and default operating system fonts.
* Simple shared memory - PMMA allows you to have a shared memory space for variables, as a replacement for global variables, which can be accessed easily through threads.
* Dynamic color and coordinates - PMMA can easily convert between different color and coordinate formats.
* Pipelines - PMMA uses these to allow for the bulk execution of functions, typically for compute or rendering purposes.
* Easy display management - PMMA allows you to easily manage your application window, including size, captions, display modes and vsync.
* Efficient shape rendering - PMMA includes support for a wide range of shapes, and can render these using GPU acceleration.
* Advanced memory management - PMMA will automatically manage large objects stored in memory.
* Image manipulation - PMMA will automatically convert image formats as needed for your application, and cache them for improved performance.
* Fast noise generation - PMMA can very efficiently create noise patterns in 1D, 2D or 3D.
* Application customization - PMMA can be told details about your application, and dynamically change its behavior.
* Efficient text rendering - PMMA can render and format text easily, with its own formatting language and powerful appearance controls.
* Video playback - PMMA can play back videos from a file, in your application.

_Note: GPU acceleration is only available with OpenGL applications, or in the render pipeline with the Pyglet graphics backend_
_Note: PMMA is still undergoing active development, and some features will be changed, added or extended in the near future - we will attempt to include backwards compatibility where possible_

## Optional Dependancies

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

### scikit-learn-intelex

PMMA uses Scikit-learn for Machine Learning, and can make use of the Python library `scikit-learn-intelex` for improved performance in these tasks. Installing this on a non-intel CPU or GPU system will not result in any degradation in performance. **This is not a required dependency**. To read more and to learn how to install go here: https://pypi.org/project/scikit-learn-intelex/

## Final Notes

We are currently working on improving the design of PMMA, bear with us as we continue to make changes over the next few days!