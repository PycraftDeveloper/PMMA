import colorsys

from pmma.python_src.constants import Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.error_utils import DisplayNotYetCreatedError as _DisplayNotYetCreatedError
from pmma.python_src.utility.general_utils import swizzle as _swizzle

class Color:
    def set_color(self, color, in_type=Constants.RGB): # converts to RGBA
        if type(color) == str:
            color = color.lower()
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

    def __init__(self):
        self.in_type = None
        self.color = None

    def get_color_format(self):
        return self.in_type

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

    def get_color(self, out_type): # Converts from RGBA
        if self.color is None:
            return None
        sorted_out_type = sorted(out_type)

        if sorted_out_type == Constants.SORTED_RGBA:
            return _swizzle(Constants.RGBA, self.color, out_type)
        elif sorted_out_type == Constants.SORTED_RGB:
            return _swizzle(Constants.RGB, self.color[0:3], out_type)
        elif sorted_out_type == Constants.SORTED_HSL:
            color = list(self.__convert_rgb_to_hsv(*self.color[0:3]))
            return _swizzle(Constants.HSL, color, out_type)
        elif sorted_out_type == Constants.SORTED_HSLA:
            color = list(self.__convert_rgb_to_hsv(*self.color[0:3])) + [round((100/255)*self.color[3])]
            return _swizzle(Constants.HSLA, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_HSL:
            color = list(self.__convert_rgb_to_hsv(
                *self.color[0:3],
                per_maximum=1,
                do_round=False))

            return _swizzle(Constants.SMALL_HSL, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_HSLA:
            color = list(self.__convert_rgb_to_hsv(
                *self.color[0:3],
                per_maximum=1,
                do_round=False)) + [round((1/255)*self.color[3])]

            return _swizzle(Constants.SMALL_HSLA, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_RGB:
            color = self.color[0]/255, self.color[1]/255, self.color[2]/255
            return _swizzle(Constants.SMALL_RGB, color, out_type)
        elif sorted_out_type == Constants.SORTED_SMALL_RGBA:
            color = (
                self.color[0]/255,
                self.color[1]/255,
                self.color[2]/255,
                self.color[3]/255)

            return _swizzle(Constants.SMALL_RGBA, color, out_type)
        elif out_type == Constants.HEX:
            return '#%02x%02x%02x' % tuple(self.color[0:3])
        elif out_type == Constants.HEXA:
            return '#%02x%02x%02x%02x' % tuple(self.color)
        elif out_type == Constants.TEXT:
            return [value for value, key in Constants.TEXT_BASED_COLORS.items() if key == self.color]

class Point:
    def __init__(self):
        self._point = None
        self._logger = _InternalLogger()

    def set_point(self, value, in_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL values vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if in_type == Constants.CONVENTIONAL_COORDINATES:
            self._point = value
        elif in_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            half_display_height = display_size[1] / 2
            self._point = (value * half_display_height)

    def get_point(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._point
        elif out_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            return self._point / (display_size[1] / 2)

class Coordinate:
    def __init__(self):
        self._coordinate = None
        self._logger = _InternalLogger()

    def set_coordinate(self, coordinate, in_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(coordinate) == list or type(coordinate) == tuple:
            coordinate = list(coordinate)
        else:
            coordinate = [float(coordinate)]

        if len(coordinate) == 0:
            coordinate = [0, 0]
            in_type == Constants.CONVENTIONAL_COORDINATES
        elif len(coordinate) == 1:
            coordinate = [coordinate[0], 0]
        elif len(coordinate) > 2:
            self._logger.log_development("This process is only required for coordinates in 2D or 1D space.")
            coordinate = coordinate[:2]


        if in_type == Constants.CONVENTIONAL_COORDINATES:
            self._coordinate = coordinate
        elif in_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            half_display_size = [display_size[0] / 2, display_size[1] / 2]
            x = half_display_size[0] * (coordinate[0] + 1)
            y = -half_display_size[1] * (coordinate[1] - 1)
            self._coordinate = [x, y]

    def get_coordinate(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._coordinate
        elif out_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            x = (2 * self._coordinate[0]) / display_size[0] - 1  # Removed the extra negative
            y = 1 - (2 * self._coordinate[1]) / display_size[1]  # This is correct
            return [x, y]