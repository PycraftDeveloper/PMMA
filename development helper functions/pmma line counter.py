import os

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base = _up(_up(__file__))
files = []
for r, d, f in os.walk(base):
    for file in f:
        if file.endswith(".py") or file.endswith(".md") or file.endswith(".rst") or file.endswith(".glsl") or file.endswith(".txt") or file.endswith(".pyx") or file.endswith(".c") or file.endswith(".toml") or file.endswith(".yml") or file.endswith(".json"):
            files.append(os.path.join(r, file))

line_count = 0
variable_count = 0
comparison_count = 0
class_count = 0
function_count = 0
nothing_count = 0
chars = 0
for file in files:
    try:
        with open(file, 'r') as f:
            content = f.readlines()
    except:
        continue

    for line in content:
        line_count += 1
        chars += len(line)
        if "if" in line or "else" in line or "elif" in line:
            comparison_count += 1
        if "class" in line:
            class_count += 1
        if "def" in line:
            function_count += 1
        if "=" in line:
            variable_count += 1
        if line.strip() == "":
            nothing_count += 1

print(f"PMMA is: {line_count} lines long|")
print(f"PMMA has: {chars:_} characters!")
print(f"PMMA has: {variable_count} variables! {round((variable_count/line_count)*100, 2)} %")
print(f"PMMA has: {comparison_count} comparisons! {round((comparison_count/line_count)*100, 2)} %")
print(f"PMMA has: {nothing_count} blank lines! {round((nothing_count/line_count)*100, 2)} %")
print(f"PMMA has: {function_count} functions! {round((function_count/line_count)*100, 2)} %")
print(f"PMMA has: {class_count} classes! {round((class_count/line_count)*100, 2)} %")
print(f"PMMA has an estimated line size of {((chars*8)/1000)/1000} MB!")