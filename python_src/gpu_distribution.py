from gc import collect as _gc__collect

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class GPUDistribution:
    def __init__(self):
        _initialize(self)

        if not _Constants.GPU_DISTRIBUTION_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.GPU_DISTRIBUTION_MANAGER_OBJECT)
            from pmma.python_src.utility.gpu_distribution_utils import GPUDistributionManager as _GPUDistributionManager
            _GPUDistributionManager()

        self._gpu_distribution_manager = _Registry.pmma_module_spine[_Constants.GPU_DISTRIBUTION_MANAGER_OBJECT]

    def get_render_gpu(self):
        return self._gpu_distribution_manager.get_render_gpu()

    def get_video_gpu(self, index=0):
        return self._gpu_distribution_manager.get_video_gpu(index=index)

    def get_all_video_gpus(self):
        return self._gpu_distribution_manager.get_all_video_gpus()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True