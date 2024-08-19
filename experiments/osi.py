import pmma
import time

pmma.init()

for key in pmma.__dict__:
    print(key, pmma.__dict__[key])

print("Done")

pmma.quit()