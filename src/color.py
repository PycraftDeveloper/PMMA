from functools import reduce
import colorsys

from pmma.src.registry import Registry
from pmma.src.constants import Constants

from pmma.src.general import swizzle, can_swizzle

class ColorIntermediary(Registry, Constants):
    def __init__(self, in_type, color):
        color = list(color)
        if sorted(in_type) == sorted(Constants.RGBA):
            self.color = color
        elif sorted(in_type) == sorted(Constants.RGB):
            self.color = color + [255]
        elif sorted(in_type) == sorted(Constants.HSL):
            self.color = list(colorsys.hsv_to_rgb(color[0]/360, color[1]/100, color[2]/100)) + [255]
        elif sorted(in_type) == sorted(Constants.HSLA):
            self.color = list(colorsys.hsv_to_rgb(color[0]/360, color[1]/100, color[2]/100)) + [(color[3]/100)*255]
        elif sorted(in_type) == sorted(Constants.SMALL_HSL):
            self.color = list(colorsys.hsv_to_rgb(*color[0:3])) + [255]
        elif sorted(in_type) == sorted(Constants.SMALL_HSLA):
            self.color = list(colorsys.hsv_to_rgb(*color[0:3])) + [255*color[3]]
        elif sorted(in_type) == sorted(Constants.SMALL_RGB):
            self.color = [color[0]*255, color[1]*255, color[2]*255, 255]
        elif sorted(in_type) == sorted(Constants.SMALL_RGBA):
            self.color = [color[0]*255, color[1]*255, color[2]*255, color[3]*255]
        elif sorted(in_type) == sorted(Constants.HEX):
            color = "".join(color)
            self.color = list(int(color[i:i+2], 16) for i in (0, 2, 4)) + [255]
        elif sorted(in_type) == sorted(Constants.HEXA):
            color = "".join(color)
            self.color = list(int(str(color[i:i+2]), 16) for i in (0, 2, 4, 6))

    def out(self, out_type):
        if sorted(out_type) == sorted(Constants.RGBA):
            return swizzle(Constants.RGBA, self.color, out_type)
        elif sorted(out_type) == sorted(Constants.RGB):
            return swizzle(Constants.RGB, self.color[0:3], out_type)

print(ColorIntermediary(Constants.RGBA, (250, 190, 170, 5)).out(Constants.BRG))