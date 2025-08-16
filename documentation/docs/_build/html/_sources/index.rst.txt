========
PMMA
========

Python Multi-Media API (PMMA) is a multi-purpose API designed to make working on multi-media projects easier and faster!

Welcome
=======

Welcome to the Python Multi-Media API (or PMMA as it is more commonly known) documentation! PMMA is a powerful API designed to help make the development of applications using the programming language Python easier and faster. PMMA is, by design, built to work in a variety of different applications, but also includes a lot of the tools commonly used in the game development industry.

PMMA includes standard support for efficient 2D and 3D pipelines using OpenGL and hardware acceleration in a variety of components as standard. Where the raw speed of hardware acceleration isn’t available, we will automatically transfer some components of PMMA over from Python to Cython for an additional increase in speed, but everything is wrapped up through Python, so it is super easy to use and compatible with most IDEs.

By default, PMMA is designed to be as fast as possible, but it has massively improved the efficiency of your Python application, far outstripping the efficiency of competing graphics APIs like Pygame and Pyglet in some of environments*.

The purpose of this documentation, then, is to provide an insight into how you can use PMMA in your application by providing a detailed and clear insight into what each namespace (the names you use to interact with PMMA’s API) does. All of this has been aided by our own at-a-glance syntax designed to help you quickly understand if this is the right component for you to use so you can spend less time reading the documentation and more time developing!

Let's walk you through PMMA's additional syntax now:

1. Lets walk you through our deployment indicators. These are the colored squares found with each namespace description.
    * The green square - 🟩 - indicates that this code **is safe** to use in your projects, as it's unlikely to be modified in any-way in future updates to PMMA.
    * The yellow square - 🟨 - indicates that this code **is safe** to use in your projects, as it's likely to get optimizations or algorithm changes, but its name and inputs and outputs (I/O) will not change.
    * The orange square - 🟧 - indicates that this code **isn't safe** for deployment yet, as its likely to have its name and/or its inputs and outputs (I/O) changed - its functionality won't change.
    * The red square - 🟥 - indicates that this code **isn't safe** for deployment yet, as its likely to have its name and/or its inputs and outputs (I/O) changed and/or its functionality may also be changed.

2. The icon after the deployment indicator (in bold) indicates if the namespace uses any additional optimization.
    * The **R** symbol - indicates that this namespace has no additional optimization (meaning  Raw Python) - *no speed up*
    * The **C** symbol - indicates that this namespace *can* use Cython compilation (meaning Cython) - *major speed up*
    * The use of a **/** indicates that multiple options are available - with **R** being the only option that's **always** required.


Hey! Did you spot something that doesn’t look right or could be better with the documentation? Let us know by raising it as an issue, or feel free to fork the project and improve the documentation yourself! If you spot a mistake or something we missed or should add to PMMA itself, please also feel free to raise it as an issue and we will work with you to pin down exactly what you're looking for so we can make PMMA better for you – or alternatively feel free to fork it and make the change yourself! PMMA is completely open source and any help is always appreciated!

*It’s important though, in mentioning PyGame that PMMA would not be possible without Pygame and the large community surrounding it, as Pygame first inspired me to make this project, and also provides a lot of the low-level references used in PMMA for things like window creation and event handling – so make sure to go and check out PyGame here: https://www.pygame.org/

*Currently things are a work in progress as we write the documentation, bear with us!*

Contents
========
.. toctree::
    :maxdepth: 2

    library_breakdown/index.rst