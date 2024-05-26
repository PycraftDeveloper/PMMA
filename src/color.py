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

    def __convert_rgb_to_hsv(self, red, green, blue):
        #get rgb percentage: range (0-1, 0-1, 0-1 )
        red_percentage= red / float(255)
        green_percentage= green/ float(255)
        blue_percentage=blue / float(255)


        #get hsv percentage: range (0-1, 0-1, 0-1)
        color_hsv_percentage=colorsys.rgb_to_hsv(red_percentage, green_percentage, blue_percentage)

        #get normal hsv: range (0-360, 0-255, 0-255)
        color_h=round(360*color_hsv_percentage[0])
        color_s=round(100*color_hsv_percentage[1])
        color_v=round(100*color_hsv_percentage[2])

        return color_h, color_s, color_v

    def out(self, out_type):
        if sorted(out_type) == sorted(Constants.RGBA):
            return swizzle(Constants.RGBA, self.color, out_type)
        elif sorted(out_type) == sorted(Constants.RGB):
            return swizzle(Constants.RGB, self.color[0:3], out_type)
        elif sorted(out_type) == sorted(Constants.HSL):
            color = list(self.__convert_rgb_to_hsv(*self.color[0:3]))
            return swizzle(Constants.HSL, color, out_type)
        elif sorted(out_type) == sorted(Constants.HSLA):
            color = list(self.__convert_rgb_to_hsv(*self.color[0:3])) + [round((100/255)*self.color[3])]
            return swizzle(Constants.HSLA, color, out_type)
        elif sorted(out_type) == sorted(Constants.SMALL_HSL):
            pass
        elif sorted(out_type) == sorted(Constants.SMALL_HSLA):
            pass
        elif sorted(out_type) == sorted(Constants.SMALL_RGB):
            pass
        elif sorted(out_type) == sorted(Constants.SMALL_RGBA):
            pass
        elif sorted(out_type) == sorted(Constants.HEX):
            pass
        elif sorted(out_type) == sorted(Constants.HEXA):
            pass

print(ColorIntermediary(Constants.RGBA, (250, 190, 170, 255)).out(Constants.LSHA))