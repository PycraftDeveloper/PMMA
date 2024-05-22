from pmma.src.registry import Registry
from pmma.src.constants import Constants

class ColorIntermediary(Registry, Constants):
    def __init__(self, type, color):
        self.type = type
        self.data = color

    def out(self, type):
        return self.data