import pmma

import sys
import time

pmma.init(log_information=True, log_warning=True, log_error=True)

inst = pmma.MemoryManager()

addr = inst.add("a", custom_id="test", object_lifetime=15)
addr = inst.add("d", custom_id="shorty", object_lifetime=2)
time.sleep(3)
addr = inst.add("k", custom_id="theinter", object_lifetime=6)
time.sleep(50)