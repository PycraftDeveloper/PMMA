from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class CameraManager:
    def __init__(self):
        _initialize(self, unique_instance=_InternalConstants.CAMERA_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self._cameras = {}
        self._primary_camera = None

    def add_camera(self, camera):
        self._cameras[id(camera)] = camera
        if self._primary_camera is None:
            self._primary_camera = camera

    def remove_camera(self, camera):
        del self._cameras[id(camera)]

        if self._primary_camera == camera:
            if self._cameras == {}:
                self._primary_camera = None
            else:
                self._primary_camera = list(self._cameras.values())[0]