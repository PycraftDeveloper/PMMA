from threading import RLock as _threading__RLock
from threading import Thread as _threading__Thread
from time import sleep as _time__sleep

from waiting import wait as _waiting__wait
from psutil import virtual_memory as _psutil__virtual_memory

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class ShapeGeometryManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self.geometry_cache = {
            _InternalConstants.LINE: {},
            _InternalConstants.RADIAL_POLYGON: {},
            _InternalConstants.RECTANGLE: {},
            _InternalConstants.ARC: {},
            _InternalConstants.ELLIPSE: {},
            _InternalConstants.POLYGON: {}}

        self.current_cache_size = 0

        self.pixel_geometry = {"vertices": None, "references": 0}

        self.lock = _threading__RLock()

        try:
            free_memory = _psutil__virtual_memory().free

            self.max_size = free_memory / 10
        except:
            self.max_size = 1_000_000_000 # default 1GB max size

        self.manager_thread = _threading__Thread() # load empty thread
        self.running_clean_up = False

    def initiate_garbage_collection(self):
        if self.manager_thread.is_alive() is False:
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
        """
        🟩 **R** -
        """
        with self.lock:
            self.geometry_cache = {
                _InternalConstants.LINE: {},
                _InternalConstants.RADIAL_POLYGON: {},
                _InternalConstants.RECTANGLE: {},
                _InternalConstants.ARC: {},
                _InternalConstants.ELLIPSE: {},
                _InternalConstants.POLYGON: {}}
            self.current_cache_size = 0

    def shape_manager_thread_wait_for_data(self):
        """
        🟩 **R** -
        """
        return (self.geometry_cache[_InternalConstants.LINE] or
                    self.geometry_cache[_InternalConstants.RADIAL_POLYGON] or
                    self.geometry_cache[_InternalConstants.RECTANGLE] or
                    self.geometry_cache[_InternalConstants.ARC] or
                    self.geometry_cache[_InternalConstants.ELLIPSE] or
                    self.geometry_cache[_InternalConstants.POLYGON])

    def clean_single_references(self, shape_type):
        """
        🟩 **R** -
        """
        with self.lock:
            for key in list(self.geometry_cache[shape_type]):
                if self.geometry_cache[shape_type][key]["references"] <= 1:
                    self.current_cache_size -= self.geometry_cache[shape_type][key]["vertices"].nbytes
                    del self.geometry_cache[shape_type][key]

    def stricter_clean(self, shape_type):
        """
        🟩 **R** -
        """
        with self.lock:
            data_efficiency_array = []
            for key in self.geometry_cache:
                data_efficiency_array.append([key, self.geometry_cache[shape_type][key]["references"]])

            data_length = len(data_efficiency_array)
            trim_size = int(data_length/10)
            data_efficiency_array.sort(key=lambda x: x[1])
            for i in range(trim_size):
                del self.geometry_cache[shape_type][data_efficiency_array[i][0]]

    def shape_geometry_manager(self):
        """
        🟩 **R** -
        """
        self.running_clean_up = True
        while True:
            _waiting__wait(self.shape_manager_thread_wait_for_data)

            if self.current_cache_size > self.max_size:
                self.clean_single_references(_InternalConstants.LINE)
                self.clean_single_references(_InternalConstants.RADIAL_POLYGON)
                self.clean_single_references(_InternalConstants.RECTANGLE)
                self.clean_single_references(_InternalConstants.ARC)
                self.clean_single_references(_InternalConstants.ELLIPSE)
                self.clean_single_references(_InternalConstants.POLYGON)

                # clean larger components if necessary
                while True:
                    if self.current_cache_size < self.max_size:
                        self.running_clean_up = False
                        break

                    self.stricter_clean(_InternalConstants.LINE)
                    self.stricter_clean(_InternalConstants.RADIAL_POLYGON)
                    self.stricter_clean(_InternalConstants.RECTANGLE)
                    self.stricter_clean(_InternalConstants.ARC)
                    self.stricter_clean(_InternalConstants.ELLIPSE)
                    self.stricter_clean(_InternalConstants.POLYGON)

            _time__sleep(1)

    def add_line(self, identifier, data):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.LINE][identifier] = {"vertices": data, "references": 1}
                self.current_cache_size += data.nbytes
        else:
            self.geometry_cache[_InternalConstants.LINE][identifier] = {"vertices": data, "references": 1}
            self.current_cache_size += data.nbytes
            if self.current_cache_size > self.max_size:
                self.initiate_garbage_collection()

    def check_if_line_exists(self, identifier):
        """
        🟩 **R** -
        """
        return identifier in self.geometry_cache[_InternalConstants.LINE]

    def get_line(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.LINE][identifier]["references"] += 1
                return self.geometry_cache[_InternalConstants.LINE][identifier]["vertices"]
        else:
            self.geometry_cache[_InternalConstants.LINE][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.LINE][identifier]["vertices"]

    def remove_line(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                if identifier in self.geometry_cache[_InternalConstants.LINE]:
                    self.geometry_cache[_InternalConstants.LINE][identifier]["references"] -= 1
                    if self.geometry_cache[_InternalConstants.LINE][identifier]["references"] <= 0:
                        self.current_cache_size -= self.geometry_cache[_InternalConstants.LINE][identifier]["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.LINE][identifier]
        else:
            if identifier in self.geometry_cache[_InternalConstants.LINE]:
                self.geometry_cache[_InternalConstants.LINE][identifier]["references"] -= 1
                if self.geometry_cache[_InternalConstants.LINE][identifier]["references"] <= 0:
                    self.current_cache_size -= self.geometry_cache[_InternalConstants.LINE][identifier]["vertices"].nbytes
                    del self.geometry_cache[_InternalConstants.LINE][identifier]

    def add_radial_polygon(self, identifier, data):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier] = {"vertices": data, "references": 1}
                self.current_cache_size += data.nbytes
        else:
            self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier] = {"vertices": data, "references": 1}
            self.current_cache_size += data.nbytes
            if self.current_cache_size > self.max_size:
                self.initiate_garbage_collection()

    def check_if_radial_polygon_exists(self, identifier):
        """
        🟩 **R** -
        """
        return identifier in self.geometry_cache[_InternalConstants.RADIAL_POLYGON]

    def get_radial_polygon(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["vertices"]
        with self.lock:
            self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["vertices"]

    def remove_radial_polygon(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                if identifier in self.geometry_cache[_InternalConstants.RADIAL_POLYGON]:
                    self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["references"] -= 1
                    if self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["references"] <= 0:
                        self.current_cache_size -= self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]
        else:
            #radial_polygon_geometry = self.geometry_cache[_InternalConstants.RADIAL_POLYGON].get(identifier, None)
            #if
            if identifier in self.geometry_cache[_InternalConstants.RADIAL_POLYGON]:
                self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["references"] -= 1
                if self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["references"] <= 0:
                    self.current_cache_size -= self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]["vertices"].nbytes
                    del self.geometry_cache[_InternalConstants.RADIAL_POLYGON][identifier]

    def add_rectangle(self, identifier, data):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.RECTANGLE][identifier] = {"vertices": data, "references": 1}
                self.current_cache_size += data.nbytes
        else:
            self.geometry_cache[_InternalConstants.RECTANGLE][identifier] = {"vertices": data, "references": 1}
            self.current_cache_size += data.nbytes
            if self.current_cache_size > self.max_size:
                self.initiate_garbage_collection()

    def check_if_rectangle_exists(self, identifier):
        """
        🟩 **R** -
        """
        return identifier in self.geometry_cache[_InternalConstants.RECTANGLE]

    def get_rectangle(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["references"] += 1
                return self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["vertices"]
        else:
            self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["vertices"]

    def remove_rectangle(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                if identifier in self.geometry_cache[_InternalConstants.RECTANGLE]:
                    self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["references"] -= 1
                    if self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["references"] <= 0:
                        self.current_cache_size -= self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.RECTANGLE][identifier]
        else:
            if identifier in self.geometry_cache[_InternalConstants.RECTANGLE]:
                self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["references"] -= 1
                if self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["references"] <= 0:
                    self.current_cache_size -= self.geometry_cache[_InternalConstants.RECTANGLE][identifier]["vertices"].nbytes
                    del self.geometry_cache[_InternalConstants.RECTANGLE][identifier]

    def add_arc(self, identifier, data):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.ARC][identifier] = {"vertices": data, "references": 1}
                self.current_cache_size += data.nbytes
        else:
            self.geometry_cache[_InternalConstants.ARC][identifier] = {"vertices": data, "references": 1}
            self.current_cache_size += data.nbytes
            if self.current_cache_size > self.max_size:
                self.initiate_garbage_collection()

    def check_if_arc_exists(self, identifier):
        """
        🟩 **R** -
        """
        return identifier in self.geometry_cache[_InternalConstants.ARC]

    def get_arc(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.ARC][identifier]["references"] += 1
                return self.geometry_cache[_InternalConstants.ARC][identifier]["vertices"]
        else:
            self.geometry_cache[_InternalConstants.ARC][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.ARC][identifier]["vertices"]

    def remove_arc(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                if identifier in self.geometry_cache[_InternalConstants.ARC]:
                    self.geometry_cache[_InternalConstants.ARC][identifier]["references"] -= 1
                    if self.geometry_cache[_InternalConstants.ARC][identifier]["references"] <= 0:
                        self.current_cache_size -= self.geometry_cache[_InternalConstants.ARC][identifier]["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.ARC][identifier]
        else:
            if identifier in self.geometry_cache[_InternalConstants.ARC]:
                self.geometry_cache[_InternalConstants.ARC][identifier]["references"] -= 1
                if self.geometry_cache[_InternalConstants.ARC][identifier]["references"] <= 0:
                    self.current_cache_size -= self.geometry_cache[_InternalConstants.ARC][identifier]["vertices"].nbytes
                    del self.geometry_cache[_InternalConstants.ARC][identifier]

    def add_ellipse(self, identifier, data):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.ELLIPSE][identifier] = {"vertices": data, "references": 1}
                self.current_cache_size += data.nbytes
        else:
            self.geometry_cache[_InternalConstants.ELLIPSE][identifier] = {"vertices": data, "references": 1}
            self.current_cache_size += data.nbytes
            if self.current_cache_size > self.max_size:
                self.initiate_garbage_collection()

    def check_if_ellipse_exists(self, identifier):
        """
        🟩 **R** -
        """
        return identifier in self.geometry_cache[_InternalConstants.ELLIPSE]

    def get_ellipse(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.ellipse_lock:
                self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["references"] += 1
                return self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["vertices"]
        else:
            self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["vertices"]

    def remove_ellipse(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                if identifier in self.geometry_cache[_InternalConstants.ELLIPSE]:
                    self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["references"] -= 1
                    if self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["references"] <= 0:
                        self.current_cache_size -= self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.ELLIPSE][identifier]
        else:
            if identifier in self.geometry_cache[_InternalConstants.ELLIPSE]:
                self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["references"] -= 1
                if self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["references"] <= 0:
                    self.current_cache_size -= self.geometry_cache[_InternalConstants.ELLIPSE][identifier]["vertices"].nbytes
                    del self.geometry_cache[_InternalConstants.ELLIPSE][identifier]

    def add_polygon(self, identifier, data):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.POLYGON][identifier] = {"vertices": data, "references": 1}
                self.current_cache_size += data.nbytes
        else:
            self.geometry_cache[_InternalConstants.POLYGON][identifier] = {"vertices": data, "references": 1}
            self.current_cache_size += data.nbytes
            if self.current_cache_size > self.max_size:
                self.initiate_garbage_collection()

    def check_if_polygon_exists(self, identifier):
        """
        🟩 **R** -
        """
        return identifier in self.geometry_cache[_InternalConstants.POLYGON]

    def get_polygon(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                self.geometry_cache[_InternalConstants.POLYGON][identifier]["references"] += 1
                return self.geometry_cache[_InternalConstants.POLYGON][identifier]["vertices"]
        else:
            self.geometry_cache[_InternalConstants.POLYGON][identifier]["references"] += 1
            return self.geometry_cache[_InternalConstants.POLYGON][identifier]["vertices"]

    def remove_polygon(self, identifier):
        """
        🟩 **R** -
        """
        if self.running_clean_up:
            with self.lock:
                if identifier in self.geometry_cache[_InternalConstants.POLYGON]:
                    self.geometry_cache[_InternalConstants.POLYGON][identifier]["references"] -= 1
                    if self.geometry_cache[_InternalConstants.POLYGON][identifier]["references"] <= 0:
                        self.current_cache_size -= self.geometry_cache[_InternalConstants.POLYGON][identifier]["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.POLYGON][identifier]
        else:
            if identifier in self.geometry_cache[_InternalConstants.POLYGON]:
                self.geometry_cache[_InternalConstants.POLYGON][identifier]["references"] -= 1
                if self.geometry_cache[_InternalConstants.POLYGON][identifier]["references"] <= 0:
                    self.current_cache_size -= self.geometry_cache[_InternalConstants.POLYGON][identifier]["vertices"].nbytes
                    del self.geometry_cache[_InternalConstants.POLYGON][identifier]

    def add_pixel(self, data):
        """
        🟩 **R** -
        """
        self.pixel_geometry = {"vertices": data, "references": 1}

    def check_if_pixel_exists(self):
        """
        🟩 **R** -
        """
        return self.pixel_geometry["vertices"] is not None

    def get_pixel(self):
        """
        🟩 **R** -
        """
        self.pixel_geometry["references"] += 1
        return self.pixel_geometry["vertices"]

    def remove_pixel(self):
        """
        🟩 **R** -
        """
        if self.check_if_pixel_exists():
            self.pixel_geometry["references"] -= 1
            if self.pixel_geometry["references"] <= 0:
                self.pixel_geometry["references"] = 0
                self.pixel_geometry["vertices"] = None