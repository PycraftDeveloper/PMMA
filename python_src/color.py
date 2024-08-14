import colorsys
import gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.general import swizzle

class ColorIntermediary:
    def detect_color_type(self, color):
        in_type = None
        if type(color) == str:
            if ("#" in color or
                    "a" in color or
                    "b" in color or
                    "c" in color or
                    "d" in color or
                    "e" in color or
                    "f" in color):

                if len(color) == 8:
                    in_type = Constants.HEXA
                elif len(color) == 6:
                    in_type = Constants.HEX
                else:
                    in_type = Constants.TEXT
            else:
                in_type = Constants.TEXT

        elif color[0] > 1:
            if color[0] <= 255:
                if len(color) == 4:
                    in_type = Constants.RGBA
                else:
                    in_type = Constants.RGB
            else:
                if color[0] < 360:
                    if color[1] > 1:
                        if len(color) == 4:
                            in_type = Constants.HSLA
                        else:
                            in_type = Constants.HSL
                    else:
                        if len(color) == 4:
                            in_type = Constants.SMALL_HSLA
                        else:
                            in_type = Constants.SMALL_HSL

        else:
            if len(color) == 4:
                in_type = Constants.SMALL_RGBA
            else:
                in_type = Constants.SMALL_RGB

        return in_type

    def __init__(self, color, in_type=Constants.AUTODETECT):
        initialize(self)

        self.attributes = []

        if type(color) == str:
            color = color.lower()
        if in_type == Constants.AUTODETECT:
            in_type = self.detect_color_type(color)
        self.in_type = in_type

        color = color
        color_list = list(color)

        sorted_in_type = sorted(in_type)

        if sorted_in_type == Constants.SORTED_RGBA:
            self.color = color_list
        elif sorted_in_type == Constants.SORTED_RGB:
            self.color = color_list + [255]
        elif sorted_in_type == Constants.SORTED_HSL:
            self.color = list(colorsys.hsv_to_rgb(
                color_list[0]/360,
                color_list[1]/100,
                color_list[2]/100)) + [255]

        elif sorted_in_type == Constants.SORTED_HSLA:
            self.color = list(colorsys.hsv_to_rgb(
                color_list[0]/360,
                color_list[1]/100,
                color_list[2]/100)) + [(color_list[3]/100)*255]

        elif sorted_in_type == Constants.SORTED_SMALL_HSL:
            self.color = list(colorsys.hsv_to_rgb(*color_list[0:3])) + [255]
        elif sorted_in_type == Constants.SORTED_SMALL_HSLA:
            self.color = list(colorsys.hsv_to_rgb(*color_list[0:3])) + [255*color_list[3]]
        elif sorted_in_type == Constants.SORTED_SMALL_RGB:
            self.color = [
                color_list[0]*255,
                color_list[1]*255,
                color_list[2]*255,
                255]

        elif sorted_in_type == Constants.SORTED_SMALL_RGBA:
            self.color = [
                color_list[0]*255,
                color_list[1]*255,
                color_list[2]*255,
                color_list[3]*255]

        elif in_type == Constants.HEX:
            self.color = list(int(color[i:i+2], 16) for i in (0, 2, 4)) + [255]
        elif in_type == Constants.HEXA:
            self.color = list(int(str(color[i:i+2]), 16) for i in (0, 2, 4, 6))
        elif in_type == Constants.TEXT:
            self.color = Constants.TEXT_BASED_COLORS[color.upper()] + [255]

        self._shut_down = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __convert_rgb_to_hsv(self, red, green, blue, per_maximum=100, do_round=True):
        #get rgb percentage: range (0-1, 0-1, 0-1 )
        red_percentage = red / float(255)
        green_percentage = green/ float(255)
        blue_percentage = blue / float(255)

        #get hsv percentage: range (0-1, 0-1, 0-1)
        color_hsv_percentage = colorsys.rgb_to_hsv(
            red_percentage,
            green_percentage,
            blue_percentage)

        #get normal hsv: range (0-360, 0-255, 0-255)
        color_h = round(360*  color_hsv_percentage[0])

        if do_round:
            color_s = round(per_maximum * color_hsv_percentage[1])
            color_v = round(per_maximum * color_hsv_percentage[2])
        else:
            color_s = per_maximum * color_hsv_percentage[1]
            color_v = per_maximum * color_hsv_percentage[2]

        return color_h, color_s, color_v

    def out(self, out_type):
        sorted_out_type = sorted(out_type)

        if sorted_out_type == Constants.SORTED_RGBA:
            return swizzle(Constants.RGBA, self.color, out_type)
        elif sorted_out_type == Constants.SORTED_RGB:
            return swizzle(Constants.RGB, self.color[0:3], out_type)
        elif sorted_out_type == Constants.SORTED_HSL:
            color = list(self.__convert_rgb_to_hsv(*self.color[0:3]))
            return swizzle(Constants.HSL, color, out_type)
        elif sorted_out_type == Constants.SORTED_HSLA:
            color = list(self.__convert_rgb_to_hsv(*self.color[0:3])) + [round((100/255)*self.color[3])]
            return swizzle(Constants.HSLA, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_HSL:
            color = list(self.__convert_rgb_to_hsv(
                *self.color[0:3],
                per_maximum=1,
                do_round=False))

            return swizzle(Constants.SMALL_HSL, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_HSLA:
            color = list(self.__convert_rgb_to_hsv(
                *self.color[0:3],
                per_maximum=1,
                do_round=False)) + [round((1/255)*self.color[3])]

            return swizzle(Constants.SMALL_HSLA, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_RGB:
            color = self.color[0]/255, self.color[1]/255, self.color[2]/255
            return swizzle(Constants.SMALL_RGB, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_RGBA:
            color = (
                self.color[0]/255,
                self.color[1]/255,
                self.color[2]/255,
                self.color[3]/255)

            return swizzle(Constants.SMALL_RGBA, color, out_type)
        elif out_type == Constants.HEX:
            return '#%02x%02x%02x' % tuple(self.color[0:3])
        elif out_type == Constants.HEXA:
            return '#%02x%02x%02x%02x' % tuple(self.color)
        elif out_type == Constants.TEXT:
            return [value for value, key in Constants.TEXT_BASED_COLORS.items() if key == self.color]

class Color:
    def __init__(self, color, in_type=Constants.AUTODETECT):
        initialize(self)

        self.__color_backend = ColorIntermediary(in_type, color)

        self.attributes = []

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

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