from threading import Lock as _threading__Lock
from threading import Thread as _threading__Thread
from time import sleep as _time__sleep

from waiting import wait as _waiting__wait
from psutil import virtual_memory as _psutil__virtual_memory

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

        self.line_lock = _threading__Lock()
        self.radial_polygon_lock = _threading__Lock()
        self.rectangle_lock = _threading__Lock()
        self.arc_lock = _threading__Lock()
        self.ellipse_lock = _threading__Lock()
        self.polygon_lock = _threading__Lock()

        try:
            free_memory = _psutil__virtual_memory().free

            self.max_size = free_memory / 10
        except:
            self.max_size = 1_000_000_000 # default 1GB max size

        self.manager_thread = _threading__Thread(target=self.shape_geometry_manager)
        self.manager_thread.daemon = True
        self.manager_thread.name = "ShapeGeometryManager: Shape_Geometry_Manager_Thread"
        self.manager_thread.start()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def reset(self):
        with self.line_lock:
            self.line_geometry = {}
        with self.radial_polygon_lock:
            self.radial_polygon_geometry = {}
        with self.rectangle_lock:
            self.rectangle_geometry = {}
        with self.arc_lock:
            self.arc_geometry = {}
        with self.ellipse_lock:
            self.ellipse_geometry = {}
        with self.polygon_lock:
            self.polygon_geometry = {}

    def get_size_of_dictionary(self, dictionary):
        size = 0
        for key in dictionary:
            size += dictionary[key]["vertices"].nbytes
        return size

    def get_total_size(self):
        with self.line_lock:
            line_geometry_size = self.get_size_of_dictionary(self.line_geometry)
        with self.radial_polygon_lock:
            radial_polygon_geometry_size = self.get_size_of_dictionary(self.radial_polygon_geometry)
        with self.rectangle_lock:
            rectangle_geometry_size = self.get_size_of_dictionary(self.rectangle_geometry)
        with self.arc_lock:
            arc_geometry_size = self.get_size_of_dictionary(self.arc_geometry)
        with self.ellipse_lock:
            ellipse_geometry_size = self.get_size_of_dictionary(self.ellipse_geometry)
        with self.polygon_lock:
            polygon_geometry_size = self.get_size_of_dictionary(self.polygon_geometry)

        return line_geometry_size+radial_polygon_geometry_size+rectangle_geometry_size+arc_geometry_size+ellipse_geometry_size+polygon_geometry_size

    def shape_manager_thread_wait_for_data(self):
        return self.line_geometry != {} or self.radial_polygon_geometry != {} or self.rectangle_geometry != {} or self.arc_geometry != {} or self.ellipse_geometry != {} or self.polygon_geometry != {}

    def clean_single_references(self, lock, dictionary):
        with lock:
            garbage_keys = []
            for key in dictionary:
                if dictionary[key]["references"] <= 1:
                    garbage_keys.append(key)

            for key in garbage_keys:
                del dictionary[key]

    def stricter_clean(self, lock, dictionary):
        with lock:
            data_efficiency_array = []
            for key in dictionary:
                data_efficiency_array.append([key, dictionary[key]["references"]])

            data_length = len(data_efficiency_array)
            trim_size = int(data_length/10)
            data_efficiency_array.sort(key=lambda x: x[1])
            for i in range(trim_size):
                del dictionary[data_efficiency_array[i][0]]

    def shape_geometry_manager(self):
        while True:
            _waiting__wait(self.shape_manager_thread_wait_for_data)

            total_size = self.get_total_size()
            if total_size > self.max_size:
                self.clean_single_references(self.line_lock, self.line_geometry)
                self.clean_single_references(self.radial_polygon_lock, self.radial_polygon_geometry)
                self.clean_single_references(self.rectangle_lock, self.rectangle_geometry)
                self.clean_single_references(self.arc_lock, self.arc_geometry)
                self.clean_single_references(self.ellipse_lock, self.ellipse_geometry)
                self.clean_single_references(self.polygon_lock, self.polygon_geometry)

                # clean larger components if necessary
                while True:
                    total_size = self.get_total_size()
                    if total_size < self.max_size:
                        break

                    self.stricter_clean(self.line_lock, self.line_geometry)
                    self.stricter_clean(self.radial_polygon_lock, self.radial_polygon_geometry)
                    self.stricter_clean(self.rectangle_lock, self.rectangle_geometry)
                    self.stricter_clean(self.arc_lock, self.arc_geometry)
                    self.stricter_clean(self.ellipse_lock, self.ellipse_geometry)
                    self.stricter_clean(self.polygon_lock, self.polygon_geometry)

            _time__sleep(1)

    def add_line(self, identifier, data):
        with self.line_lock:
            self.line_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_line_exists(self, identifier):
        return self.line_geometry.get(identifier) != None

    def get_line(self, identifier):
        with self.line_lock:
            self.line_geometry[identifier]["references"] += 1
            return self.line_geometry[identifier]["vertices"]

    def remove_line(self, identifier):
        with self.line_lock:
            if self.line_geometry.get(identifier):
                self.line_geometry[identifier]["references"] -= 1
                if self.line_geometry[identifier]["references"] <= 0:
                    del self.line_geometry[identifier]

    def add_radial_polygon(self, identifier, data):
        with self.radial_polygon_lock:
            self.radial_polygon_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_radial_polygon_exists(self, identifier):
        return self.radial_polygon_geometry.get(identifier) != None

    def get_radial_polygon(self, identifier):
        with self.radial_polygon_lock:
            self.radial_polygon_geometry[identifier]["references"] += 1
            return self.radial_polygon_geometry[identifier]["vertices"]

    def remove_radial_polygon(self, identifier):
        with self.radial_polygon_lock:
            if self.radial_polygon_geometry.get(identifier):
                self.radial_polygon_geometry[identifier]["references"] -= 1
                if self.radial_polygon_geometry[identifier]["references"] <= 0:
                    del self.radial_polygon_geometry[identifier]

    def add_rectangle(self, identifier, data):
        with self.rectangle_lock:
            self.rectangle_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_rectangle_exists(self, identifier):
        return self.rectangle_geometry.get(identifier) != None

    def get_rectangle(self, identifier):
        with self.rectangle_lock:
            self.rectangle_geometry[identifier]["references"] += 1
            return self.rectangle_geometry[identifier]["vertices"]

    def remove_rectangle(self, identifier):
        with self.rectangle_lock:
            if self.rectangle_geometry.get(identifier):
                self.rectangle_geometry[identifier]["references"] -= 1
                if self.rectangle_geometry[identifier]["references"] <= 0:
                    del self.rectangle_geometry[identifier]

    def add_arc(self, identifier, data):
        with self.arc_lock:
            self.arc_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_arc_exists(self, identifier):
        return self.arc_geometry.get(identifier) != None

    def get_arc(self, identifier):
        with self.arc_lock:
            self.arc_geometry[identifier]["references"] += 1
            return self.arc_geometry[identifier]["vertices"]

    def remove_arc(self, identifier):
        with self.arc_lock:
            if self.arc_geometry.get(identifier):
                self.arc_geometry[identifier]["references"] -= 1
                if self.arc_geometry[identifier]["references"] <= 0:
                    del self.arc_geometry[identifier]

    def add_ellipse(self, identifier, data):
        with self.ellipse_lock:
            self.ellipse_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_ellipse_exists(self, identifier):
        return self.ellipse_geometry.get(identifier) != None

    def get_ellipse(self, identifier):
        with self.ellipse_lock:
            self.ellipse_geometry[identifier]["references"] += 1
            return self.ellipse_geometry[identifier]["vertices"]

    def remove_ellipse(self, identifier):
        with self.ellipse_lock:
            if self.ellipse_geometry.get(identifier):
                self.ellipse_geometry[identifier]["references"] -= 1
                if self.ellipse_geometry[identifier]["references"] <= 0:
                    del self.ellipse_geometry[identifier]

    def add_polygon(self, identifier, data):
        with self.polygon_lock:
            self.polygon_geometry[identifier] = {"vertices": data, "references": 1}

    def check_if_polygon_exists(self, identifier):
        return self.polygon_geometry.get(identifier) != None

    def get_polygon(self, identifier):
        with self.polygon_lock:
            self.polygon_geometry[identifier]["references"] += 1
            return self.polygon_geometry[identifier]["vertices"]

    def remove_polygon(self, identifier):
        with self.polygon_lock:
            if self.polygon_geometry.get(identifier):
                self.polygon_geometry[identifier]["references"] -= 1
                if self.polygon_geometry[identifier]["references"] <= 0:
                    del self.polygon_geometry[identifier]

    def add_pixel(self, data):
        self.pixel_geometry = {"vertices": data, "references": 1}

    def check_if_pixel_exists(self):
        return self.pixel_geometry["vertices"] is not None

    def get_pixel(self):
        self.pixel_geometry["references"] += 1
        return self.pixel_geometry["vertices"]

    def remove_pixel(self):
        if self.check_if_pixel_exists():
            self.pixel_geometry["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None