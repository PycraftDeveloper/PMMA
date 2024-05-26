from pmma.src.registry import Registry
from pmma.src.constants import Constants

class CoordinateIntermediary:
    def __init__(self, type, coordinate):
        self.type = type
        self.data = coordinate

    def out(self, type):
        return self.data