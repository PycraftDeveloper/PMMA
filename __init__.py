def _init_():
    print("__init__")

if __name__ == "pmma":
    _init_()

    from . import main

else:
    _init_()