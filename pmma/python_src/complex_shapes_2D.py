from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Lines:
    """
    🟩 **R** - Draws a multi-point line.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._polygon = self._shapes_2D__module.Polygon()
        self._polygon._closed = False

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._polygon.render()

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._polygon.set_rotation(rotation, format=format)

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        return self._polygon.get_rotation(format=format)

    def set_curved(self, curved=False):
        """
        🟩 **R** -
        """
        self._polygon.set_curved(curved=curved)

    def get_curved(self):
        """
        🟩 **R** -
        """
        return self._polygon.get_curved()

    def get_closed(self):
        """
        🟩 **R** -
        """
        return self._polygon.get_closed()

    def set_points(self, points, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._polygon.set_points(points, format=format)

    def get_points(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._polygon.get_points(format=format)

    def set_width(self, width=None):
        """
        🟩 **R** -
        """
        self._polygon.set_width(width=width)

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._polygon.get_width()

class Circle:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Decagon:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(10)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Nonagon:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(9)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Octagon:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(8)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Heptagon:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(7)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Septagon(Heptagon):
    def __init__(self):
        super().__init__()

class Hexagon:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(6)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Pentagon:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(5)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

class Triangle:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._math__module = _ModuleManager.import_module("math")

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._radial_polygon = self._shapes_2D__module.RadialPolygon()
        self._radial_polygon.set_point_count(3)

        angle = 60 * (self._math__module.pi / 180)
        self._cos_sixty = self._math__module.cos(angle)

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._radial_polygon.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._radial_polygon.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._radial_polygon.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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

        self._shapes_2D__module = _ModuleManager.import_module("pmma.python_src.shapes_2D")

        self._rectangle = self._shapes_2D__module.Rectangle()

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

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        self._rectangle.set_color(color, format=format)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._rectangle.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        return self._rectangle.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._rectangle.generate_random_color(
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._rectangle.generate_color_from_perlin_noise(
            value=value,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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