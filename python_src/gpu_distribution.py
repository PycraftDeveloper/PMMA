from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class GPUDistribution:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if not _InternalConstants.GPU_DISTRIBUTION_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_InternalConstants.GPU_DISTRIBUTION_MANAGER_OBJECT)
            from pmma.python_src.utility.gpu_distribution_utils import GPUDistributionManager as _GPUDistributionManager
            _GPUDistributionManager()

        self._gpu_distribution_manager = _Registry.pmma_module_spine[_InternalConstants.GPU_DISTRIBUTION_MANAGER_OBJECT]

    def get_render_gpu(self):
        """
        🟩 **R** -
        """
        return self._gpu_distribution_manager.get_render_gpu()

    def get_video_gpu(self, index=0):
        """
        🟩 **R** -
        """
        return self._gpu_distribution_manager.get_video_gpu(index=index)

    def get_all_video_gpus(self):
        """
        🟩 **R** -
        """
        return self._gpu_distribution_manager.get_all_video_gpus()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True