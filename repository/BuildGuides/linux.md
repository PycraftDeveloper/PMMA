<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# PMMA (Python Multi-Media API)

## Contents
* [Back to the README](https://github.com/PycraftDeveloper/PMMA/blob/main/README.md#contents)

## Linux Build Guide

Welcome to the Linux build guide! This build guide is intended for users of PMMA 5 or later, but for users of PMMA 4 or older only do steps 2 and 7.

Before we begin, you will need admin privileges to do this.

### Step 1: Pre-requisites

Before we can begin to build PMMA for your system, we need to make sure you have a few packages set-up first:

You will need:
`cmake`, `make`, `gcc`, `gcc-c++`, `mesa-libGL-dev`, `libXrandr-dev`, `libXinerama-dev`, `libXcursor-dev`, `libXi-dev`, `wayland-dev`, `libxkbcommon-dev`, `git` and a python version of your choosing.

To install all these packages you can do:
* On Ubuntu/Debian do: `sudo apt install cmake make gcc g++ libgl1-mesa-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev libwayland-dev libxkbcommon-dev git python3 python3-pip curl unzip grep`
* On Fedora/RHEL do: `sudo dnf install cmake make gcc gcc-c++ mesa-libGL-devel libXrandr-devel libXinerama-devel libXcursor-devel libXi-devel wayland-devel libxkbcommon-devel git python3 python3-pip curl unzip grep`
* On Arch/Manjaro do: `sudo pacman -Syu cmake make gcc mesa libxrandr libxinerama libxcursor libxi wayland libxkbcommon git python python-pip curl unzip grep`

### Step 2: Grab a copy of PMMA

Now we have installed all the packages we will need later, lets grab the latest copy of PMMA!

To do this, we will use this handy install script:
```
latest=$(curl -s https://api.github.com/repos/PycraftDeveloper/PMMA/releases/latest | grep tag_name | cut -d '"' -f 4)
curl -L -o PMMA.zip "https://github.com/PycraftDeveloper/PMMA/archive/refs/tags/$latest.zip"
unzip PMMA.zip
rm PMMA.zip
```

This command will:
1. Get the tag (the version number) for the latest release of PMMA on GitHub.
2. Then it downloads the latest zip (source code) release of PMMA and stores it in "PMMA.zip"
3. Then it extracts this zip file.
4. Before cleaning up the zip file we downloaded in step 2.

Alternatively you can use the command listed below to grab a specific version of PMMA - you can find the tag codes here: [here](https://github.com/PycraftDeveloper/PMMA/tags). The substitute in the command `< tag code here >` for your preference:
```
tagcode=< tag code here >
curl -L -o PMMA.zip "https://github.com/PycraftDeveloper/PMMA/archive/refs/tags/$tagcode.zip"
unzip PMMA.zip
rm PMMA.zip
```

Alternatively you can head over to the [releases section](https://github.com/PycraftDeveloper/PMMA/releases) and manually download and extract either of the "Source code" releases.

### Step 3: Setup PMMA for the build

Now we have grabbed a copy of PMMA, we need to head into the folder and move some stuff around.

To begin, enter the command `ls` to get the name of the folder we extracted in the previous step. Due to the way that GitHub packages the releases, we should see a folder called: `PMMA-< tag code >` where `< tag code >` reflects the version of PMMA we downloaded.

Make a note of the name, and head into this directory with: `cd PMMA-< tag code >`. From now on, we will refer to this base directory as ROOT, but this shouldn't effect any of our commands.

In this ROOT directory we need to make a new sub-directory called temporary. This is where we will be putting all the stuff we don't need once we have built PMMA. To do this we can to `mkdir temporary`

### Step 4: Install PMMA's PIP dependencies

I'm sure you probably thought we where done with installing dependencies, however whilst we have installed some system packages that are required for the next step - we haven't installed the packages that PMMA needs directly.

Unlike the previous dependency installation step, this is much easier as you just need to run `pip3 install -r requirements.txt`.

### Step 5: Building PMMA Core

PMMA is composed of two overlapping sections. There is the Python facing side which you use to interact with the API, then there is the C++ side that does a lot of the API's heavy lifting. Where we can use PIP to install the python packages for PMMA, there isn't a similar command to install the C++ dependencies for the API. Because of this, we need to compile PMMA Core, and all these dependencies in this step - this will enable the API to be completely stand-alone from any system packages, meaning you can much more easily move it around on your system - or deploy to multiple identical machines.

Of course though, there are risks to doing this - compiled code on one machine may not work on another - particularly if they have different architectures (for example building on 64-bit for a 32-bit machine) or platforms (this Linux build will not work on Windows). Similarly, we compile PMMA for a 'generic architecture' meaning we don't enable support for features like AVX-512, however if you are building PMMA for this exact CPU architecture, you can mess around with the compiler flags for PMMA [more on this later](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/BuildGuides/linux.md#final-considerations) to get even faster performance!

With that small novel out the way - we can build PMMA Core and its dependencies using the following commands:

1. `cmake -S build_tools/cmake -B temporary -DCMAKE_POSITION_INDEPENDENT_CODE=ON` - Here we are configuring CMake (not performing the actual build, thats step 2) and telling it to build into the temporary directory. Don't worry though, everything we need will be installed into the correct directories, this is for easier cleaning up later.

2. `cmake --build temporary --config Release` - Here we are telling CMake to compile our project using the configuration we made in the temporary directory earlier. The additional configuration step here also tells CMake that this build is ready for prime-time so optimize more aggressively.

Now these commands will take a while to complete - I should have made you read the first two paragraphs of this step now!

Once complete, it's up to you if you plan to re-build PMMA later or not.
* If you plan to re-build PMMA later then we recommend you keep the temporary directory
* If you don't plan to re-build PMMA again, or encountered any errors in the build process, we recommend deleting the contents using the command `rm -rf /temporary/*`.

### Step 6: Building the PMMA Core -> Python interface

Now that the C++ API is built, we need a way of accessing it from Python. To do this, we are now going to compile the Cython API that will hook into PMMA Core for us.

This is nice and simple - just run: `python3 setup.py build_ext --build-lib pmma/build --build-temp temporary`

### Step 7: Finishing up

Congratulations, you now have a ready-to-go version of PMMA on your computer! However we have just one more step to make - we need to copy the entire `ROOT/pmma directory` into your python versions `dist-packages` folder, so you can import it and use it like any other Python module.

This step will depend on where Python3 was installed to, but you can do: `sudo cp -r pmma '/usr/lib/python3/dist-packages/pmma'`

Alternatively, you can find the dist-folder by running the command: `python3 -c "import site, os; [print(p) or exit() for p in site.getsitepackages() if os.path.exists(os.path.join(p, 'numpy'))]"` then run: `cp -r pmma '/usr/lib/python3/dist-packages/pmma'`. Please note you may need to run that last command as an admin.

Once this is done and you have checked you can import pmma in Python (note that if you had a python window open before starting this step, you may need to close and reopen it) then you are free to now delete the `PMMA-< tag code >` directory with the command: `rm -rf PMMA-< tag code >` replacing `< tag code >` with the version of PMMA you downloaded initially.

## Final Considerations

Don't worry, there isn't another step! However, there are some things you can consider now.

If you want to adjust PMMA's compile arguments to build a more hardware optimized version for your CPU's architecture you can do so by modifying the compile args in the file: `build_tools/cmake/4_build_core/CMakeLists.txt` on line 67. You can then do the same by modifying `setup.py` line 38. Here are some pointers to some compiler arguments that might improve the performance of PMMA further: `-march=native -mtune=native -flto -fno-exceptions -fno-rtti -falign-functions=32`. **Please note; adding or removing compiler args can cause either build process to fail or unexpected things to happen, please modify PMMA's compile args at your own risk.**