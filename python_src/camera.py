from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Camera:
    def __init__(self):
        _initialize(self)

        if not _Constants.CAMERA_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CAMERA_MANAGER_OBJECT)
            from pmma.python_src.utility.camera_utils import CameraManager as _CameraManager
            _CameraManager()

        self._camera_manager = _Registry.pmma_module_spine[_Constants.CAMERA_MANAGER_OBJECT]
        self._camera_manager.add_camera(self)

    def __del__(self):
        if self._shut_down is False:
            self._camera_manager.remove_camera(self)

    def quit(self):
        self.__del__()
        self._shut_down = True

    def set_as_primary(self):
        self._camera_manager._primary_camera = self

    def is_primary(self):
        return self._camera_manager._primary_camera == self