
from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.constants import Constants

from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

from pmma.python_src.utility.registry_utils import Registry as _Registry

class Color:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        self._coloysys__module = _ModuleManager.import_module("colorsys")

        self._numpy__module = _ModuleManager.import_module("numpy")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._GeneralIntermediary = self._general_utils__module.GeneralIntermediary()
        self.in_type = None
        self.color = None

    def set_color(self, color, in_type=Constants.RGB):
        """
        🟩 **R** -
        """
        if isinstance(color, str):
            color = color.lower()

        self.in_type = in_type

        color_list = list(color)
        sorted_in_type = sorted(in_type)

        if sorted_in_type == Constants.SORTED_RGBA:
            self.color = color_list
        elif sorted_in_type == Constants.SORTED_RGB:
            self.color = color_list + [255]
        elif sorted_in_type == Constants.SORTED_HSL:
            self.color = list(self._coloysys__module.hsv_to_rgb(
                color_list[0] / 360,
                color_list[1] / 100,
                color_list[2] / 100)) + [255]
        elif sorted_in_type == Constants.SORTED_HSLA:
            self.color = list(self._coloysys__module.hsv_to_rgb(
                color_list[0] / 360,
                color_list[1] / 100,
                color_list[2] / 100)) + [(color_list[3] / 100) * 255]
        elif sorted_in_type == Constants.SORTED_SMALL_HSL:
            self.color = list(self._coloysys__module.hsv_to_rgb(color_list[0], color_list[1], color_list[2])) + [255]
        elif sorted_in_type == Constants.SORTED_SMALL_HSLA:
            self.color = list(self._coloysys__module.hsv_to_rgb(color_list[0], color_list[1], color_list[2])) + [255 * color_list[3]]
        elif sorted_in_type == Constants.SORTED_SMALL_RGB:
            self.color = [color_list[0] * 255, color_list[1] * 255, color_list[2] * 255, 255]
        elif sorted_in_type == Constants.SORTED_SMALL_RGBA:
            self.color = [color_list[0] * 255, color_list[1] * 255, color_list[2] * 255, color_list[3] * 255]
        elif in_type == Constants.HEX:
            self.color = [int(color[i:i + 2], 16) for i in (0, 2, 4)] + [255]
        elif in_type == Constants.HEXA:
            self.color = [int(color[i:i + 2], 16) for i in (0, 2, 4, 6)]
        elif in_type == Constants.TEXT:
            self.color = Constants.TEXT_BASED_COLORS[color.upper()] + [255]

    def __convert_rgb_to_hsv(self, red, green, blue, per_maximum=100, do_round=True):
        """
        🟩 **R** -
        """
        red_percentage = red / 255
        green_percentage = green / 255
        blue_percentage = blue / 255
        color_hsv_percentage = self._coloysys__module.rgb_to_hsv(
            red_percentage, green_percentage, blue_percentage)
        color_h = 360 * color_hsv_percentage[0]

        if do_round:
            color_s = round(per_maximum * color_hsv_percentage[1])
            color_v = round(per_maximum * color_hsv_percentage[2])
        else:
            color_s = per_maximum * color_hsv_percentage[1]
            color_v = per_maximum * color_hsv_percentage[2]
        return (color_h, color_s, color_v)

    def get_color(self, out_type):
        """
        🟩 **R** -
        """
        if self.color is None:
            return None
        sorted_out_type = sorted(out_type)
        if sorted_out_type == Constants.SORTED_RGBA:
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.RGBA, self.color, out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_RGB:
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.RGB, self.color[0:3], out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_HSL:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2]))
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.HSL, color, out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_HSLA:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2])) + [round((100 / 255) * self.color[3])]
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.HSLA, color, out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_HSL:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2], per_maximum=1, do_round=False))
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.SMALL_HSL, color, out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_HSLA:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2], per_maximum=1, do_round=False)) + \
                    [round((1 / 255) * self.color[3])]
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.SMALL_HSLA, color, out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_RGB:
            color = [self.color[0] / 255, self.color[1] / 255, self.color[2] / 255]
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.SMALL_RGB, color, out_type), dtype=self._numpy__module.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_RGBA:
            color = [self.color[0] / 255, self.color[1] / 255, self.color[2] / 255, self.color[3] / 255]
            return self._numpy__module.array(self._GeneralIntermediary.swizzle(Constants.SMALL_RGBA, color, out_type), dtype=self._numpy__module.float32)
        elif out_type == Constants.HEX:
            return '#%02x%02x%02x' % tuple(self.color[0:3])
        elif out_type == Constants.HEXA:
            return '#%02x%02x%02x%02x' % tuple(self.color)
        elif out_type == Constants.TEXT:
            return [value for value, key in Constants.TEXT_BASED_COLORS.items() if key == self.color]

class DisplayScalar:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._point = 0.0
        self._logger = self._logging_utils__module.InternalLogger()
        self.display_height = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_height()

    def update_display_height(self):
        self.display_height = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_height()

    def set_point(self, value, in_type=Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if in_type == Constants.CONVENTIONAL_COORDINATES:
            self._point = value
        elif in_type == Constants.OPENGL_COORDINATES:
            half_display_height = self.display_height / 2.0
            self._point = value * half_display_height

    def get_point(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._point
        elif out_type == Constants.OPENGL_COORDINATES:
            return self._point / (self.display_height / 2.0)

class DisplayCoordinates:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._coordinate = [0.0, 0.0]
        self._logger = self._logging_utils__module.InternalLogger()

        self.display_size = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_size()

    def update_display_size(self):
        self.display_size = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_size()

    def set_coordinate(self, coordinate, in_type=Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if isinstance(coordinate, (list, tuple, self._numpy__module.ndarray)):
            converted_coordinate = list(coordinate)
        else:
            converted_coordinate = [float(coordinate)]

        if len(converted_coordinate) == 0:
            converted_coordinate = [0.0, 0.0]
        elif len(converted_coordinate) == 1:
            converted_coordinate.append(0.0)
        elif len(converted_coordinate) > 2:
            self._logger.log_development("This process is only required for 2D coordinates.")
            converted_coordinate = converted_coordinate[:2]

        if in_type == Constants.CONVENTIONAL_COORDINATES:
            self._coordinate = converted_coordinate
        elif in_type == Constants.OPENGL_COORDINATES:
            half_display_width = self.display_size[0] / 2.0
            half_display_height = self.display_size[1] / 2.0
            x = half_display_width * (converted_coordinate[0] + 1)
            y = -half_display_height * (converted_coordinate[1] - 1)
            self._coordinate = [x, y]

    def get_coordinate(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._numpy__module.array(self._coordinate, dtype=self._numpy__module.float32)

        elif out_type == Constants.OPENGL_COORDINATES:
            display_width = self.display_size[0]
            display_height = self.display_size[1]
            x = (2.0 * self._coordinate[0]) / display_width - 1.0
            y = 1.0 - (2.0 * self._coordinate[1]) / display_height
            return self._numpy__module.array([x, y], dtype=self._numpy__module.float32)