from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class Camera:
    def __init__(self):
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CAMERA_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.components_used.append(_InternalConstants.CAMERA_MANAGER_OBJECT)
            from pmma.python_src.utility.camera_utils import CameraManager as _CameraManager
            _CameraManager()

        self._camera_manager = _Registry.pmma_module_spine[_InternalConstants.CAMERA_MANAGER_OBJECT]
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