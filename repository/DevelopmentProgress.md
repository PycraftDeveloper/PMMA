<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/blob/main/repository/SmallLogo.png)
</div>


# PMMA (Python Multi-Media API)

## Progress on the next version of PMMA

We are currently working on the next minor update to PMMA, version 5.1.x. This update is generally targeted at transitioning away from the OpenGL graphics API and into BGFX to better secure the future of the API with the gradual deprecation of the OpenGL API. This update will also bring numerous bug fixes, a major overhaul to the build system for the C++ side of PMMA, and an expansion ans general refinement of the Text and Animation portions of the API.

### ![Progress on PMMA 5.1](https://geps.dev/progress/55)

* ✅ - Remove all MacOS support from the API directly (as it cant be tested and fails to build - any CMAKE work will be kept).
* ✅ - Update repository for the beginning of work on PMMA 5.1.
* ✅ - Setup and test the new build system for PMMA (C++ component).
* ✅ - Introduce BGFX as the replacement for OpenGL.
* ✅ - Fix any bugs that are identified from the launch of PMMA 5.
* ⏳ - Make major refinements to the text rendering API.
* 🛑 - Introduce the 'Raw2DRendering' portion of the API which will replace the recently removed OpenGL portion.
* 🛑 - Extend the existing Animations API and rename it to Transitions2D in preparation for a 3D counterpart in the near future.
* 🛑 - Overhaul and work on the documentation and docstring usage within PMMA (C++ and Python components).
* 🛑 - Re-introduce an automated testing system for the new API.

* ⛔ - Temporarily halted progress on Video (Will be added in PMMA 5.2).
* 🚫 - Camera serves no purpose until PMMA 6 - temporarily halted development on this.

## Emoji Guide

* ✅ - Completed tasks.
* ⏳ - Tasks currently being worked on (with optional percentage of rough progress towards completion).
* 🛑 - Tasks that are yet to be started.
* ⛔ - Tasks that are to be done but will not be featured in the current developmental version of the API.
* 🚫 - Tasks that have been temporarily shelved and may or may not return in a future version of the API.