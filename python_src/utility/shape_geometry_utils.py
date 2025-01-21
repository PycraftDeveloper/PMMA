from waiting import wait as _waiting__wait

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ShapeGeometryManager:
    def __init__(self):
        _initialize(self, unique_instance=_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self.line_geometry = {}
        self.radial_polygon_geometry = {}
        self.rectangle_geometry = {}
        self.arc_geometry = {}
        self.ellipse_geometry = {}
        self.polygon_geometry = {}
        self.pixel_geometry = {"vertices": None, "references": 0}

        self._display_size = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_size()

    def add_line(self, identifier, data):
        self.line_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_line_exists(self, identifier):
        return identifier in self.line_geometry

    def get_line(self, identifier):
        self.line_geometry[identifier]["references"] += 1
        return self.line_geometry[identifier]["vertices"]

    def remove_line(self, identifier):
        if self.check_if_line_exists(identifier):
            self.line_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None

    def add_radial_polygon(self, identifier, data):
        self.radial_polygon_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_radial_polygon_exists(self, identifier):
        return identifier in self.radial_polygon_geometry

    def get_radial_polygon(self, identifier):
        self.radial_polygon_geometry[identifier]["references"] += 1
        return self.radial_polygon_geometry[identifier]["vertices"]

    def remove_radial_polygon(self, identifier):
        if self.check_if_radial_polygon_exists(identifier):
            self.radial_polygon_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None

    def add_rectangle(self, identifier, data):
        self.rectangle_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_rectangle_exists(self, identifier):
        return identifier in self.rectangle_geometry

    def get_rectangle(self, identifier):
        self.rectangle_geometry[identifier]["references"] += 1
        return self.rectangle_geometry[identifier]["vertices"]

    def remove_rectangle(self, identifier):
        if self.check_if_rectangle_exists(identifier):
            self.rectangle_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None

    def add_arc(self, identifier, data):
        self.arc_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_arc_exists(self, identifier):
        return identifier in self.arc_geometry

    def get_arc(self, identifier):
        self.arc_geometry[identifier]["references"] += 1
        return self.arc_geometry[identifier]["vertices"]

    def remove_arc(self, identifier):
        if self.check_if_arc_exists(identifier):
            self.arc_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None

    def add_ellipse(self, identifier, data):
        self.ellipse_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_ellipse_exists(self, identifier):
        return identifier in self.ellipse_geometry

    def get_ellipse(self, identifier):
        self.ellipse_geometry[identifier]["references"] += 1
        return self.ellipse_geometry[identifier]["vertices"]

    def remove_ellipse(self, identifier):
        if self.check_if_ellipse_exists(identifier):
            self.ellipse_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None

    def add_polygon(self, identifier, data):
        self.polygon_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_polygon_exists(self, identifier):
        return identifier in self.polygon_geometry

    def get_polygon(self, identifier):
        self.polygon_geometry[identifier]["references"] += 1
        return self.polygon_geometry[identifier]["vertices"]

    def remove_polygon(self, identifier):
        if self.check_if_polygon_exists(identifier):
            self.polygon_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None

    def add_pixel(self, identifier, data):
        self.pixel_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_pixel_exists(self, identifier):
        return identifier in self.pixel_geometry

    def get_pixel(self, identifier):
        self.pixel_geometry[identifier]["references"] += 1
        return self.pixel_geometry[identifier]["vertices"]

    def remove_pixel(self, identifier):
        if self.check_if_pixel_exists(identifier):
            self.pixel_geometry[identifier]["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None