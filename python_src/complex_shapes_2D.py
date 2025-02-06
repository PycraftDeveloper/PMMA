from math import cos as _math__cos
from math import pi as _math__pi

from pmma.python_src.shapes_2D import RadialPolygon as _RadialPolygon
from pmma.python_src.shapes_2D import Rectangle as _Rectangle
from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Triangle:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._radial_polygon = _RadialPolygon()
        self._radial_polygon.set_point_count(3)

        angle = 60 * (_math__pi / 180)
        self._cos_sixty = _math__cos(angle)

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._radial_polygon.render()

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_rotation(rotation, format=format)

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_rotation(format=format)

    def set_radius(self, value, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_radius(value, format=format)

    def get_radius(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_radius(format=format)

    def get_point_count(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_point_count()

    def set_center(self, center, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_center(center, format=format)

    def get_center(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_center(format=format)

    def set_width(self, width=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_width(width=width)

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_width()

    def set_length(self, length, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        radius = length / self._cos_sixty
        self._radial_polygon.set_radius(radius, format=format)

    def get_length(self, format=_Constants.OPENGL_COORDINATES):
        """
        🟩 **R** -
        """
        radius = self._radial_polygon.get_radius(format=format)
        return self._cos_sixty * radius

class Square:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._rectangle = _Rectangle()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._rectangle.render()

    def set_width(self, width=1, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._rectangle.set_width(width, format=format)

    def get_width(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._rectangle.get_width(format=format)

    def set_corner_radius(self, corner_radius=1, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._rectangle.set_corner_radius(corner_radius, format=format)

    def get_corner_width(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._rectangle.get_corner_width(format=format)

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._rectangle.set_rotation(rotation, format=format)

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        return self._rectangle.get_rotation(format=format)

    def set_center(self, center, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._rectangle.set_center(center, format=format)

    def get_center(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._rectangle.get_center(format=format)

    def set_length(self, length, size_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._rectangle.set_size([length]*2, size_format=size_format)

    def get_length(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._rectangle.get_size(format=format)[0]

    def get_size(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._rectangle.get_size(format=format)