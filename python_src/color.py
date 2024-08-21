import gc as _gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.noise import Perlin as _Perlin

from pmma.python_src.utility.color_utils import ColorIntermediary as _ColorIntermediary

class Color:
    def __init__(self, seed=None):
        initialize(self)

        self._color_intermediary = _ColorIntermediary()

        self._red_noise = _Perlin(seed=seed)
        self._green_noise = _Perlin(seed=seed)
        self._blue_noise = _Perlin(seed=seed)
        self._alpha_noise = _Perlin(seed=seed)

    def input_color(self, color, format=Constants.AUTODETECT):
        self._color_intermediary.set_color(color, format)

    def output_color(self, format):
        return self._color_intermediary.get_color(format)

    def output_color_format(self):
        return self._color_intermediary.get_color_format()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def generate_color(self, value, format=Constants.RGBA, color_range=[0, 255], red_color_range=[0, 255], green_color_range=[0, 255], blue_color_range=[0, 255], alpha_color_range=[0, 255]):
        if color_range != [0, 255]:
            if red_color_range == [0, 255]:
                red_color_range = color_range
            elif green_color_range == [0, 255]:
                green_color_range = color_range
            elif blue_color_range == [0, 255]:
                blue_color_range = color_range
            elif alpha_color_range == [0, 255]:
                alpha_color_range = color_range

        color = [
            self._red_noise.generate_1D_perlin_noise(value, new_range=red_color_range),
            self._green_noise.generate_1D_perlin_noise(value, new_range=green_color_range),
            self._blue_noise.generate_1D_perlin_noise(value, new_range=blue_color_range),
            self._alpha_noise.generate_1D_perlin_noise(value, new_range=alpha_color_range)]

        self._color_intermediary.set_color(color, Constants.RGBA)
        return self.output_color(format)