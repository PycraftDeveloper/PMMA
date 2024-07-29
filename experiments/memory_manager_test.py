import pmma.python_src.memory_manager as mm

import numpy as np

import sys
import time

inst = mm.MemoryManager()

#with open(r"H:\Videos\2024-07-03 18-21-06.mp4", "rb") as file:
    #data = file.read()

data = "hello"
data2 = "hello2"

addr = inst.add_object(data, custom_id="test")
addr = inst.add_object(data2, custom_id="test")
print((sys.getsizeof(inst.get_object(addr))/1000)/1000)
del data
print(inst.objects)
print(inst.linker)
time.sleep(2)
print(inst.get_object(addr))
time.sleep(2)
print(inst.get_object(addr))
time.sleep(2)
print(inst.get_object(addr))
time.sleep(2)
print(inst.get_object(addr))
time.sleep(3)
print(inst.get_object(addr))