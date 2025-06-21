<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# PMMA (Python Multi-Media API)

## Contents
* [Back to the README](https://github.com/PycraftDeveloper/PMMA/blob/main/README.md#contents)

## Linux Build Guide

Welcome to the Linux build guide! Before we begin, you will need admin privileges to do this. Lets begin:

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