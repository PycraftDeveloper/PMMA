import gc as _gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.utility.color_utils import ColorIntermediary as _ColorIntermediary

class Color:
    def __init__(self, color, in_type=Constants.AUTODETECT):
        initialize(self)

        self.__color_backend = _ColorIntermediary(in_type, color)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def convert_format(self, out_type):
        return self.__color_backend.out(out_type)

    def generate_perlin_color(self, generate_alpha=False):
        color = [None, None, None]
        if generate_alpha:
            color += None
            self.__init__(color, in_type=Constants.RGBA)
        else:
            self.__init__(color, in_type=Constants.RGB)