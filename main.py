print("Thank you for using Python Multi-Media API (PMMA)!")

if __name__ == "__main__":
    import __init__
    del __init__

class Src:
    registry = None
    Perlin_utils = None

src = Src()
del Src

import registry_utils
src.registry = registry_utils.Registry()
del registry_utils

def init_all():
    import Perlin_utils
    src.Perlin_utils = Perlin_utils
    del Perlin_utils

def init_audio():
    pass

def init_display():
    pass

def init_events():
    pass

def init_graphics():
    pass

def init_math():
    pass

def init_noise():
    import Perlin_utils
    src.Perlin_utils = Perlin_utils
    del Perlin_utils

def init_text():
    pass

def init_time():
    pass

print("API here")