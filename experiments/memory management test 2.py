import pmma.python_src.memory_manager as mm
import pmma.python_src.logging as log
from pmma import init

import sys
import time

init()

inst = mm.MemoryManager()

addr = inst.add_object("a", custom_id="test")
time.sleep(5)