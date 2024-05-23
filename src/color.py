from functools import reduce
import colorsys

from pmma.src.registry import Registry
from pmma.src.constants import Constants

from pmma.src.general import swizzle, can_swizzle

class ColorIntermediary(Registry, Constants):
    def __init__(self, type, color):
        self.in_type = type
        if self.in_type == Constants.RGB:
            self.data = list(color) + [255]
        elif self.in_type == Constants.RGBA:
            self.data = list(color)
        elif self.in_type == Constants.HEX:
            self.data = list(int(color[i:i+2], 16) for i in (0, 2, 4)) + [255]
        elif self.in_type == Constants.HEXA:
            self.data = list(int(color[i:i+2], 16) for i in (0, 2, 4, 6))
        elif self.in_type == Constants.HSL:
            self.data = list(colorsys.hsv_to_rgb(*color)) + [255]
        elif self.in_type == Constants.HSLA:
            self.data = list(round(i * 255) for i in colorsys.hsv_to_rgb(*color[0:3])) + [int((255/1)*color[3])]

        self.original = color

    def out(self, out_type):
        if sorted(self.in_type) == sorted(out_type):
            return swizzle(self.in_type, self.original, out_type)
        elif sorted(out_type) == sorted(Constants.RGB):
            return swizzle(Constants.RGBA, self.data, out_type)
        elif sorted(out_type) == sorted(Constants.HEX):
            return '#%02x%02x%02x' % tuple(self.data[0:3])
        elif sorted(out_type) == sorted(Constants.HEXA):
            return '#%02x%02x%02x%02x' % tuple(self.data)
        elif sorted(out_type) == sorted(Constants.HSL):
            data = list(colorsys.rgb_to_hsv(*self.data[0:3]))
            return swizzle(Constants.HSL, data, out_type)
        elif sorted(out_type) == sorted(Constants.HSLA):
            data = list(colorsys.rgb_to_hsv(*self.data[0:3])) + [self.data[3]/255]
            return swizzle(Constants.HSLA, data, out_type)