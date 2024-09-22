import gc as _gc
import time as _time

from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class GPUDistribution:
    def __init__(self):
        _initialize(self)

        self._gpu_distribution_manager = _Registry.pmma_module_spine[Constants.GPU_DISTRIBUTION_MANAGER_OBJECT]

    def get_render_gpu(self):
        return self._gpu_distribution_manager.get_render_gpu()

    def get_video_gpu(self, index=0):
        return self._gpu_distribution_manager.get_video_gpu(index=index)

    def get_all_video_gpus(self):
        return self._gpu_distribution_manager.get_all_video_gpus()