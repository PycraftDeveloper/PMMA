try:
    from os import sep
    from sys import path, pycache_prefix
except Exception as error:
    from tkinter import messagebox

    messagebox.showerror(
        "Unable to start PMMA",
        f"A problem occurred whilst trying to start PMMA.\nMore Details: {error}")

def up(file_path: str) -> str:
    return file_path[::-1].split(sep, 1)[-1][::-1]

base_path = up(__file__)
del up

pycache_prefix = base_path+sep+"temporary"

root = base_path+sep+"src"
path.append(base_path)
path.append(root)
path.append(root+sep+"core")
path.append(root+sep+"audio")
path.append(root+sep+"display")
path.append(root+sep+"events")
path.append(root+sep+"math")
path.append(root+sep+"noise")
path.append(root+sep+"text")
path.append(root+sep+"time")
path.append(root+sep+"graphics")

del sep, path, pycache_prefix, base_path