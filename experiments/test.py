import pmma
import time

pmma.init()

fc = pmma.FileCore()

while True:
    time.sleep(1/15)
    print(len(fc.file_matrix.keys()))