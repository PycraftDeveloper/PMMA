import sys
import os
import json

import numba

#import path

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base_path = _up(__file__)
temporary_files_path = base_path + os.sep + "temporary"
sys.pycache_prefix = temporary_files_path
numba.config.CACHE_DIR = temporary_files_path

from pmma.src.registry import *
Registry.temporary_files_path = temporary_files_path
Registry.base_path = base_path
from pmma.src.core import *

environ_to_registry()

from pmma.src.constants import *
from pmma.src.recorder import *
from pmma.src.display import *
from pmma.src.events import *
from pmma.src.noise import *
from pmma.src.draw import *
from pmma.src.utility.math_utils import *
from pmma.src.utility.noise_utils import *

Registry.base_path

# use json to load events.json
# add these events to constants module
# use these constants to key against events
# to generate a list of events that are constant
# regardless of graphics API.

# also add path module when legal issues resolved!

del base_path
del temporary_files_path
del sys
del os
del numba
del environ_to_registry