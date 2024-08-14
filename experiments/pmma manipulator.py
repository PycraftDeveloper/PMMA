import os

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base = _up(_up(__file__))
files = []
for r, d, f in os.walk(base):
    for file in f:
        if file.endswith(".py") or file.endswith(".md") or file.endswith(".rst") or file.endswith(".glsl") or file.endswith(".txt") or file.endswith(".pyx") or file.endswith(".c"):
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
        line_count += 1

print(line_count)