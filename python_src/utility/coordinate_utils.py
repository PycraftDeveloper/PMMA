from pmma.python_src.constants import Constants
from pmma.python_src.utils.registry import Registry as _Registry

from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.error_utils import DisplayNotYetCreatedError as _DisplayNotYetCreatedError

class CoordinateIntermediary:
    def __init__(self):
        self._coordinate = None
        self._logger = _InternalLogger()

    def set_coordinate(self, coordinate, in_type=Constants.CONVENTIONAL_COORDINATES):
        if Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        if Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._coordinate
        elif out_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            x = -(2 * self._coordinate[0]) / display_size[0] - 1
            x *= display.get_aspect_ratio()
            y = 1-(2 * self._coordinate[1]) / display_size[1]
            return [x, y]