import pmma.python_src.memory_manager as mm
import pmma.python_src.logging as log
from pmma import init

import sys
import time

init(log_information=True, log_warning=True, log_error=True)

inst = mm.MemoryManager()

addr = inst.add_object("a", custom_id="test", object_lifetime=15)
addr = inst.add_object("d", custom_id="shorty", object_lifetime=2)
time.sleep(3)
addr = inst.add_object("k", custom_id="theinter", object_lifetime=6)
time.sleep(50)