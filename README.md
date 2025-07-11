<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# PMMA (Python Multi-Media API)
⚠️ This is the DEVELOPMENT version for PMMA 5.0.0 and is NOT meant for routine use yet. ⚠️


PMMA is a Python library aimed at improving application development in Python.
Typically, developing applications in Python necessitates familiarity with a variety of different libraries such as [Pygame](https://github.com/pygame/pygame), [ModernGL](https://github.com/moderngl/moderngl), [PIL](https://github.com/python-pillow/Pillow) and [Numpy](https://github.com/numpy/numpy). PMMA aims to simplify the application development process by creating a single interface that provides easy access to simple and advanced pre-written and highly optimised application development utilities, whilst still also allowing these utilities to be expanded upon by exposing their underlying APIs.

## Contents

* [Development Progress](https://github.com/PycraftDeveloper/PMMA?tab=readme-ov-file#development-progress)
* [Installation](https://github.com/PycraftDeveloper/PMMA/blob/main/README.md#installation)
* [Build Guide](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/BuildGuides/intro.md#pmma-build-guide)
* [Troubleshooting](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/Troubleshooting/into.md#pmma-troubleshooting)
* [Credits](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/Troubleshooting/into.md#pmma-credits)
* [About](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/Troubleshooting/into.md#pmma-about)

## Development Progress

![Progress on PMMA v5.0.0](https://geps.dev/progress/46)

We are currently working on the next major update to PMMA, version 5.x.x. This update features a complete API rework with a significant proportion being re-written in C++ for a significant performance and efficiency improvement. This major update will also introduce all the features lacking from previous iterations of PMMA, including text rendering, aggregated events for text input and improvements to the accuracy and variety of procedural noise generation. If you want to check out our current progress list, you can find it here: [Progress on PMMA 5](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/DevelopmentProgress.md#progress-on-pmma-5)

## Installation

You can install the latest version of PMMA from PyPi using the command: `pip install pmma' or you can head over to the website here: [PMMA on PyPi](https://pypi.org/project/pmma/) tio select a custom version to install.

### Requirements

In order to install PMMA 5 and newer, you must ensure you meet the following criteria:

| Category | Requirement |
| :-------- | :------: |
| Operating System | `Windows`, `ALT Linux 10+`, `RHEL 9+`, `Debian 11+`, `Fedora 34+`, `Mageia 8+`, `Photon OS 3.0 (with updates)`, `Ubuntu 21.04+` **Architecture**: `64-bit (x64)`<br><br>`MacOS` **Architecture**:  `arm-64` |
| Python Version | `3.8.x`, `3.9.x`, `3.10.x`, `3.11.x` |
| `pip` Version | `20.3 or newer` |

_Note: If your platform is not listed here then you can attempt to build your own version of PMMA using our [build guide](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/BuildGuides/intro.md)!_

<details><summary>Additional Technical Requirements</summary>

_Please note, these requirements are only needed by users installing PMMA onto Linux machines and in most cases the operating systems listed above should be compatible._

* In order for PMMA to work as expected, you must be using either X-Lib, or Wayland. This means that Ubuntu 21.04 DESKTOP will work, but Ubuntu 21.04 SERVER is unlikely to.
* Additionally, you will need `glibc 2.28` or newer, this can be checked on linux using the command `ldd --version` (root not required). The result should be on the first line as shown in the image below:

![Example output](https://github.com/user-attachments/assets/bcd09e5a-8f2e-4a39-b323-dd15f94efe8b)

</details>
</br>

> For older versions of PMMA, there are no hardware requirements.

_If you encounter any issues or problems then check out our [troubleshooting page](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/Troubleshooting/into.md#pmma-troubleshooting)._

## Credits

PMMA is made possible thanks to the following:

C/C++ projects (used in PMMA 5 and newer)
* LIBZ - 1.3.1 - https://github.com/madler/zlib
* Libpng - 1.6.49 - https://github.com/glennrp/libpng
* GLFW - 3.4 - https://github.com/glfw/glfw
* FreeType - 2-13-3 - https://gitlab.freedesktop.org/freetype/freetype
* GLM - 0.9.3.2 - https://github.com/icaven/glm
* GLAD - 2.0.8 - https://github.com/Dav1dde/glad
* HarfBuzz - 11.2.1 - https://github.com/harfbuzz/harfbuzz

Python projects (used in PMMA 1 and newer)
* PyAV - latest - https://github.com/PyAV-Org/PyAV
* Cython - latest - https://github.com/cython/cython
* GetOSTheme - latest - https://github.com/FHPythonUtils/GetOSTheme
* MoviePy - latest - https://github.com/Zulko/moviepy
* Num2Words - latest - https://github.com/savoirfairelinux/num2words
* Pedalboard - latest - https://github.com/spotify/pedalboard
* Pillow - latest - https://github.com/python-pillow/Pillow
* Pprofile - latest - https://github.com/vpelletier/pprofile
* Psutil - latest - https://github.com/giampaolo/psutil
* PyADL - latest - https://github.com/nicolargo/pyadl
* Pyrr - latest - https://github.com/adamlwgriffiths/Pyrr
* Requests - latest - https://github.com/psf/requests
* Send2Trash - latest - https://github.com/arsenetar/send2trash
* SoundDevice - latest - https://github.com/spatialaudio/python-sounddevice/
* SoundFile - latest - https://github.com/bastibe/python-soundfile
* Waiting - latest - https://github.com/vmalloc/waiting
* Watchdog - latest - https://github.com/gorakhargosh/watchdog/
* PyWin32 - latest - https://github.com/mhammond/pywin32
* WMI - latest - https://timgolden.me.uk/python/wmi/

NONE of the projects mentioned above are owned or maintained by PycraftDeveloper the maker of this repository, who would also like to say a big thank you to all the teams working on these projects!

You can check out our licenses and the licenses of all the C/C++ projects PMMA uses as standard [here](https://github.com/PycraftDeveloper/PMMA/tree/main/pmma/licenses) or on your installed version of PMMA (version 5 or later) under `pmma/licenses`.

_Note: If you spot a problem in our licensing or distribution of third party dependencies please raise the problem as [an issue here](https://github.com/PycraftDeveloper/PMMA/issues) with the title-prefix: 'LICENSING: ' and we will respond to these problems as soon as possible. Thanks!_

## About

We have worked on numerous large applications using the Python programming language. Most notably [Pycraft](https://github.com/PycraftDeveloper/Pycraft) which is our flagship project, an OpenGL based game using Python. Every time we write these large projects, we often find ourselves writing the same utility programs - which are small programs that help to eliminate complexity in our larger program files. So we decided to combine all of these utility programs into this project, PMMA which is intended then to make writing these larger applications easier as we don't need to keep re-using the same utility programs. The benefits don't stop there though as we are also ensuring this API is as fast and efficient as possible.