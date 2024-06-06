import pmma
import time

pmma.init()

fc = pmma.FileCore(project_directory="/home/thomas/wiggly")

n = 0
while True:
    time.sleep(1/30)
    n += 1
    if n < 30:
        print(n)
    if n == 30:
        fc.update_locations()