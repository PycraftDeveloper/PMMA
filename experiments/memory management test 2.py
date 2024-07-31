import pmma.python_src.memory_manager as mm
import pmma.python_src.logging as log

import tracemalloc
import linecache
import os
import gc

tracemalloc.start()

import cv2

import sys
import time

def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

log.Logger()

inst = mm.MemoryManager()

#with open(r"H:\Videos\2024-07-03 18-21-06.mp4", "rb") as file:
    #data = file.read()

data = "hellomynameisjeff"
for i in range(28):
    data += data

addr = inst.add_object(data, custom_id="test")
print((sys.getsizeof(inst.get_object(addr))/1000)/1000)
del data
gc.collect()
time.sleep(15)
snapshot = tracemalloc.take_snapshot()
display_top(snapshot)
time.sleep(15)
inst.get_object(addr)
time.sleep(200000)