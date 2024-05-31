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

from pmma.py_src.registry import *
Registry.temporary_files_path = temporary_files_path
Registry.base_path = base_path
from pmma.py_src.core import *

environ_to_registry()

from pmma.py_src.constants import *
from pmma.py_src.optimizer import *
from pmma.py_src.recorder import *
from pmma.py_src.display import *
from pmma.py_src.events import *
from pmma.py_src.noise import *
from pmma.py_src.color import *
from pmma.py_src.draw import *
from pmma.py_src.advmath import *

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

benchmark = Benchmark() # cache this unique to device
benchmark.test_all()