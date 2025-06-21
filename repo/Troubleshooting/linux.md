<div align="center">

  ![PMMA logo](https://github.com/PycraftDeveloper/PMMA/assets/81379254/2c4858b8-b50c-4f3b-95f3-d93fd1f0f19b)
</div>


# PMMA (Python Multi-Media API)

## Contents
* [Back to the README](https://github.com/PycraftDeveloper/PMMA/blob/main/README.md#contents)
* [`OSError: PortAudio library not found`](https://github.com/PycraftDeveloper/PMMA/blob/main/repo/Troubleshooting/linux.md#oserror-portaudio-library-not-found)

## Linux Troubleshooting

### `OSError: PortAudio library not found`

This error occurs because the `sounddevice` module uses the PortAudio library. We would love to include the PortAudio library for you, however we can't because it uses the ASIO SDK from Steinberg which beings with it some licensing complexities at this time unfortunately.

Notes:
* This error will prevent the use of PMMA's Audio component only.
* Fixing this error will likely require admin privileges eg; `sudo`.

To fix:
* On Ubuntu/Debian do: `sudo apt install portaudio19-dev`
* On Fedora/RHEL do: `sudo dnf install portaudio-devel` or `sudo yum install portaudio-devel`
* On Arch/Manjaro do: `sudo pacman -S portaudio`

Then reinstall `sounddevice` with: `pip install --force-reinstall sounddevice`. Please note that this command may change your version of `sounddevice` to one that may be incompatible with PMMA, to check head to: `requirements.txt` or our [Dependency Graph](https://github.com/PycraftDeveloper/PMMA/network/dependencies).