<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# Python Multi-Media API (PMMA)

## Performance Testing Report

Welcome to PMMA's performance testing report. PMMA is dedicated to enhancing the in-app performance of your applications. In this report, we will be evaluating the raw performance of PMMA and presenting a comprehensive analysis of each test. While our tests may not be entirely scientific, we strive to maintain a scientific and transparent approach to minimize any potential bias. When PMMA's performance falls short of our expectations, we may make revisions to improve it, and those changes will be documented here. Additionally, PMMA leverages various performance optimization methods, some of which may be influenced by hardware choices (such as GPU power for hardware accelerated rendering or Intel CPUs for `scikit-learn-intelex` optimized Machine Learning) or by software choices (support for GCC and MSVC as optimized C compilers, and the impact of not having either installed or using a different C compiler). Let's begin!

_Note: In PMMA we target a minimum of 2,000 (two thousand) runs of any operation in the game loop. This is because, the maximum achievable refresh rate of PMMA is 2,000. This value is calculated by using the formulae: $`\frac{1}{\left( \frac{T}{n} \right)}`$ where: `T` is the total execution time of `n` runs (greater than 10)_

### PMMA Draw Based Rendering

#### Overview

PMMA has 2 main approaches to rendering. It can either draw content directly to a canvas, or it can generate a canvas and render that to another canvas (or the main window). This performance test is to compare the performance of PMMA in drawing content directly to a canvas (the former).

#### Existing Performance

PMMA can use three different approaches to draw content directly to a canvas, depending on which display mode you are using.
* For the Pygame display mode: `SDL`, `OpenGL (PMMA)`
* For the Pyglet display mode: `OpenGL (Pyglet)`

_Note: It's important to identify here that `OpenGL (PMMA)` and `OpenGL (Pyglet)` use the same API (OpenGL) for their rendering, but the interface between OpenGL and the relevant draw functionality is NOT the same. As such they are identified separately_

