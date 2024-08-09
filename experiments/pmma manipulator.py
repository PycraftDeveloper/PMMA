import glob
import os
import sys

print(sys.builtin_module_names)

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base = _up(_up(__file__))
files = []
for r, d, f in os.walk(base):
    for file in f:
        if file.endswith(".py"):
            files.append(os.path.join(r, file))

line_count = 0
for file in files:
    try:
        with open(file, 'r') as f:
            content = f.readlines()
    except:
        continue

    #print(file)

    for line in content:
        if "import " in line and ">>>" not in line and "pmma" not in line:
            print(line.strip())
        line_count += 1

print(line_count)