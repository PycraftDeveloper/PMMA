from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ShapeGeometryManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self._threading__module = _ModuleManager.import_module("threading")
        self._time__module = _ModuleManager.import_module("time")
        self._waiting__module = _ModuleManager.import_module("waiting")
        self._psutil__module = _ModuleManager.import_module("psutil")

        self.geometry_cache = {
            _InternalConstants.LINE: {},
            _InternalConstants.RADIAL_POLYGON: {},
            _InternalConstants.RECTANGLE: {},
            _InternalConstants.ARC: {},
            _InternalConstants.ELLIPSE: {},
            _InternalConstants.POLYGON: {}}

        self.current_cache_size = 0

        self.pixel_geometry = {"vertices": None, "references": 0}

        self.lock = self._threading__module.RLock()

        try:
            free_memory = self._psutil__module.virtual_memory().free

            self.max_size = free_memory / 10
        except:
            self.max_size = 1_000_000_000 # default 1GB max size

        self.manager_thread = self._threading__module.Thread() # load empty thread
        self.running_clean_up = False

    def initiate_garbage_collection(self):
        if self.manager_thread.is_alive() is False:
            self.manager_thread = self._threading__module.Thread(target=self.shape_geometry_manager)
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
            self._waiting__module.wait(self.shape_manager_thread_wait_for_data)

            if self.current_cache_size > self.max_size * 0.9:
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

            self._time__module.sleep(1)

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
            if self.current_cache_size > self.max_size * 0.9:
                self.initiate_garbage_collection()

    def line_cache(self, old_id, new_id):
        line_geometry_cache = self.geometry_cache[_InternalConstants.LINE]
        if old_id is not None:
            if self.running_clean_up:
                with self.lock:
                    line_geometry = line_geometry_cache.get(old_id, None)
                    if line_geometry:
                        line_geometry["references"] -= 1
                        if line_geometry["references"] <= 0:
                            self.current_cache_size -= line_geometry["vertices"].nbytes
                            del self.geometry_cache[_InternalConstants.LINE][old_id]
            else:
                line_geometry = line_geometry_cache.get(old_id, None)
                if line_geometry:
                    line_geometry["references"] -= 1
                    if line_geometry["references"] <= 0:
                        self.current_cache_size -= line_geometry["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.LINE][old_id]

        if self.running_clean_up:
            with self.lock:
                line_geometry = line_geometry_cache.get(new_id, None)
                if line_geometry:
                    line_geometry["references"] += 1
                    return line_geometry["vertices"]
        else:
            line_geometry = line_geometry_cache.get(new_id, None)
            if line_geometry:
                line_geometry["references"] += 1
                return line_geometry["vertices"]

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
            if self.current_cache_size > self.max_size * 0.9:
                self.initiate_garbage_collection()

    def radial_polygon_cache(self, old_id, new_id):
        radial_polygon_geometry_cache = self.geometry_cache[_InternalConstants.RADIAL_POLYGON]
        if old_id is not None:
            if self.running_clean_up:
                with self.lock:
                    radial_polygon_geometry = radial_polygon_geometry_cache.get(old_id, None)
                    if radial_polygon_geometry:
                        radial_polygon_geometry["references"] -= 1
                        if radial_polygon_geometry["references"] <= 0:
                            self.current_cache_size -= radial_polygon_geometry["vertices"].nbytes
                            del self.geometry_cache[_InternalConstants.RADIAL_POLYGON][old_id]
            else:
                radial_polygon_geometry = radial_polygon_geometry_cache.get(old_id, None)
                if radial_polygon_geometry:
                    radial_polygon_geometry["references"] -= 1
                    if radial_polygon_geometry["references"] <= 0:
                        self.current_cache_size -= radial_polygon_geometry["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.RADIAL_POLYGON][old_id]

        if self.running_clean_up:
            with self.lock:
                radial_polygon_geometry = radial_polygon_geometry_cache.get(new_id, None)
                if radial_polygon_geometry:
                    radial_polygon_geometry["references"] += 1
                    return radial_polygon_geometry["vertices"]
        else:
            radial_polygon_geometry = radial_polygon_geometry_cache.get(new_id, None)
            if radial_polygon_geometry:
                radial_polygon_geometry["references"] += 1
                return radial_polygon_geometry["vertices"]

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
            if self.current_cache_size > self.max_size * 0.9:
                self.initiate_garbage_collection()

    def rectangle_cache(self, old_id, new_id):
        rectangle_geometry_cache = self.geometry_cache[_InternalConstants.RECTANGLE]
        if old_id is not None:
            if self.running_clean_up:
                with self.lock:
                    rectangle_geometry = rectangle_geometry_cache.get(old_id, None)
                    if rectangle_geometry:
                        rectangle_geometry["references"] -= 1
                        if rectangle_geometry["references"] <= 0:
                            self.current_cache_size -= rectangle_geometry["vertices"].nbytes
                            del self.geometry_cache[_InternalConstants.RECTANGLE][old_id]
            else:
                rectangle_geometry = rectangle_geometry_cache.get(old_id, None)
                if rectangle_geometry:
                    rectangle_geometry["references"] -= 1
                    if rectangle_geometry["references"] <= 0:
                        self.current_cache_size -= rectangle_geometry["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.RECTANGLE][old_id]

        if self.running_clean_up:
            with self.lock:
                rectangle_geometry = rectangle_geometry_cache.get(new_id, None)
                if rectangle_geometry:
                    rectangle_geometry["references"] += 1
                    return rectangle_geometry["vertices"]
        else:
            rectangle_geometry = rectangle_geometry_cache.get(new_id, None)
            if rectangle_geometry:
                rectangle_geometry["references"] += 1
                return rectangle_geometry["vertices"]

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
            if self.current_cache_size > self.max_size * 0.9:
                self.initiate_garbage_collection()

    def arc_cache(self, old_id, new_id):
        arc_geometry_cache = self.geometry_cache[_InternalConstants.ARC]
        if old_id is not None:
            if self.running_clean_up:
                with self.lock:
                    arc_geometry = arc_geometry_cache.get(old_id, None)
                    if arc_geometry:
                        arc_geometry["references"] -= 1
                        if arc_geometry["references"] <= 0:
                            self.current_cache_size -= arc_geometry["vertices"].nbytes
                            del self.geometry_cache[_InternalConstants.ARC][old_id]
            else:
                arc_geometry = arc_geometry_cache.get(old_id, None)
                if arc_geometry:
                    arc_geometry["references"] -= 1
                    if arc_geometry["references"] <= 0:
                        self.current_cache_size -= arc_geometry["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.ARC][old_id]

        if self.running_clean_up:
            with self.lock:
                arc_geometry = arc_geometry_cache.get(new_id, None)
                if arc_geometry:
                    arc_geometry["references"] += 1
                    return arc_geometry["vertices"]
        else:
            arc_geometry = arc_geometry_cache.get(new_id, None)
            if arc_geometry:
                arc_geometry["references"] += 1
                return arc_geometry["vertices"]

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
            if self.current_cache_size > self.max_size * 0.9:
                self.initiate_garbage_collection()

    def ellipse_cache(self, old_id, new_id):
        ellipse_geometry_cache = self.geometry_cache[_InternalConstants.ELLIPSE]
        if old_id is not None:
            if self.running_clean_up:
                with self.lock:
                    ellipse_geometry = ellipse_geometry_cache[old_id]
                    if ellipse_geometry:
                        ellipse_geometry["references"] -= 1
                        if ellipse_geometry["references"] <= 0:
                            self.current_cache_size -= ellipse_geometry["vertices"].nbytes
                            del self.geometry_cache[_InternalConstants.ELLIPSE][old_id]
            else:
                ellipse_geometry = ellipse_geometry_cache[old_id]
                if ellipse_geometry:
                    ellipse_geometry["references"] -= 1
                    if ellipse_geometry["references"] <= 0:
                        self.current_cache_size -= ellipse_geometry["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.ELLIPSE][old_id]

        if self.running_clean_up:
            with self.lock:
                ellipse_geometry = ellipse_geometry_cache.get(new_id, None)
                if ellipse_geometry:
                    ellipse_geometry["references"] += 1
                    return ellipse_geometry["vertices"]
        else:
            ellipse_geometry = ellipse_geometry_cache.get(new_id, None)
            if ellipse_geometry:
                ellipse_geometry["references"] += 1
                return ellipse_geometry["vertices"]

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
            if self.current_cache_size > self.max_size * 0.9:
                self.initiate_garbage_collection()

    def polygon_cache(self, old_id, new_id):
        polygon_geometry_cache = self.geometry_cache[_InternalConstants.POLYGON]
        if old_id is not None:
            if self.running_clean_up:
                with self.lock:
                    polygon_geometry = polygon_geometry_cache[old_id]
                    if polygon_geometry:
                        polygon_geometry["references"] -= 1
                        if polygon_geometry["references"] <= 0:
                            self.current_cache_size -= polygon_geometry["vertices"].nbytes
                            del self.geometry_cache[_InternalConstants.POLYGON][old_id]
            else:
                polygon_geometry = polygon_geometry_cache[old_id]
                if polygon_geometry:
                    polygon_geometry["references"] -= 1
                    if polygon_geometry["references"] <= 0:
                        self.current_cache_size -= polygon_geometry["vertices"].nbytes
                        del self.geometry_cache[_InternalConstants.POLYGON][old_id]

        if self.running_clean_up:
            with self.lock:
                polygon_geometry = polygon_geometry_cache.get(new_id, None)
                if polygon_geometry:
                    polygon_geometry["references"] += 1
                    return polygon_geometry["vertices"]
        else:
            polygon_geometry = polygon_geometry_cache.get(new_id, None)
            if polygon_geometry:
                polygon_geometry["references"] += 1
                return polygon_geometry["vertices"]

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