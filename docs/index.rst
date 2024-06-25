========
PMMA
========

Python Multi-Media API (PMMA) is a multi-purpose API designed to make working on multi-media projects easier and faster!

Contents
========
.. toctree::
    :maxdepth: 2

    advmath/index.rst
    advthreading/index.rst
    advtkinter/index.rst
    audio/index.rst
    color/index.rst
    constants/index.rst
    coordinate/index.rst
    core/index.rst
    display/index.rst
    draw/index.rst
    events/index.rst
    file/index.rst
    general/index.rst
    noise/index.rst
    opengl/index.rst
    optimizer/index.rst
    passport/index.rst
    recorder/index.rst
    registry/index.rst
    surface/index.rst
    text/index.rst
    video/index.rst

Welcome
=======

Welcome to PMMA's documentation! PMMA (or Python Multi-Media API) is a powerful library designed to help you make complex applications in Python, by handling the more complex behind-the-scenes content. PMMA is largely focused on game development applications including powerful 2D and 3D rendering pipelines, support for multiple graphics APIs (SDL2 and OpenGL for now), hardware accelerated graphics, C and JIT compilation (through Cython and Numba respectively) and even simplifies text rendering, audio and visual media manipulation and advanced mathematical operations. PMMA is also built with performance in mind, enabling powerful and performant code.

This documentation then, provides insight into how you can take advantage of PMMA in your applications by providing detailed and clear information into what each namespace (the names you will use to call PMMA's library) does. All of this is aided by a set of new at-a-glance syntax designed to help you spend less time reading documentation and more time developing!

Let's walk you through PMMA's additional syntax now:

    1. Firstly, lets walk you through our deployment indicators. These are the colored squares found with each namespace description.
        * The green square - 🟩 - indicates that this code **is safe** to use in your projects, as it's unlikely to be modified in any-way in future updates to PMMA.
        * The yellow square - 🟨 - indicates that this code **is safe** to use in your projects, as it's likely to have its name changed, but won't change in functionality or in its inputs and outputs (I/O).
        * The orange square - 🟧 - indicates that this code **isn't safe** for deployment yet, as its likely to have its name and/or its inputs and outputs (I/O) changed - its functionality won't change.
        * The red square - 🟥 - indicates that this code **isn't safe** for deployment yet, as its likely to have its name and/or its inputs and outputs (I/O) changed and/or its functionality may also be changed.

    2. Secondly, the icon after the deployment indicator (in bold) indicates if the namespace uses any additional optimization.
        * The **R** symbol - indicates that this namespace has no additional optimization (meaning  :raw-html:`<strong>R</strong>` aw Python) - *no speed up*
        * The **N** symbol - indicates that this namespace *can* use Numba (JIT) compilation (meaning :raw-html:`<strong>N</strong>` umba) - *minor speed up*
        * The **C** symbol - indicates that this namespace *can* use Cython compilation (meaning :raw-html:`<strong>C</strong>` ython) - *major speed up*
        * The use of a **/** indicates that multiple options are available - with **R** being the only option that's **always** required.
Now lets discuss some important points about PMMA:
    1. Secondly, PMMA uses an object called the ``Registry`` behind the scenes. This is used to behind the scenes to configure PMMA for optimal performance and compatibility. This object can be accessed from outside PMMA (ie. in your own applications) however we strongly recommend that if you need to access it, you do so without changing any of its attributes *unless you know what your doing*.

*Currently things are a bit of a work in progress as we write the documentation, bear with us!*