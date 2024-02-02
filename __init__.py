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

pycache_prefix = base_path+sep+"temporary"

del up

def _init_(sep, path):
    print("__init__")
    root = base_path+sep+"src"
    path.append(base_path)
    path.append(root)
    path.append(root+sep+"core")

if __name__ == "pmma":
    _init_(sep, path)

    del sep, path, base_path, pycache_prefix

    from main import *

else:
    _init_(sep, path)

    del sep, path, base_path, pycache_prefix