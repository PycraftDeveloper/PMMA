========
PMMA
========

PMMA is targeted at helping you build applications of any size in Python and C++ by covering areas such as rendering, audio/video playback and much more!

Welcome
=======

Welcome to the Python Multi-Media API (or PMMA as it is more commonly known) documentation! PMMA is a powerful API designed to help make the development of applications using the programming language Python easier and faster. PMMA is, by design, built to work in a variety of different applications, but also includes a lot of the tools commonly used in the game development industry.

PMMA includes standard support for efficient 2D and 3D pipelines using OpenGL and hardware acceleration in a variety of components as standard. Where the raw speed of hardware acceleration isn’t available, we will automatically transfer some components of PMMA over from Python to Cython for an additional increase in speed, but everything is wrapped up through Python, so it is super easy to use and compatible with most IDEs.

By default, PMMA is designed to be as fast as possible, but it has massively improved the efficiency of your Python application, far outstripping the efficiency of competing graphics APIs like Pygame and Pyglet in some of environments*.

Hey! Did you spot something that doesn’t look right or could be better with the documentation? Let us know by raising it as an issue, or feel free to fork the project and improve the documentation yourself! If you spot a mistake or something we missed or should add to PMMA itself, please also feel free to raise it as an issue and we will work with you to pin down exactly what you're looking for so we can make PMMA better for you – or alternatively feel free to fork it and make the change yourself! PMMA is completely open source and any help is always appreciated!

*Currently things are a work in progress as we write the documentation, bear with us!*

Contents
========
.. toctree::
    :maxdepth: 2

    overview/index.rst
    python_api/index.rst
    cpp_api/index.rst