from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class GPUDistributionManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.GPU_DISTRIBUTION_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self._time__module = _ModuleManager.import_module("time")

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.GPUS_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.GPUS_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.gpu_utils import GPUsIntermediary as _GPUsIntermediary
            _GPUsIntermediary()

        self._gpus = _Registry.pmma_module_spine[_InternalConstants.GPUS_INTERMEDIARY_OBJECT]

        self._render_gpu = None
        self._video_gpu = []
        self._last_updated = self._time__module.perf_counter()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def update_gpu_roles(self, initialization_override=False):
        """
        🟩 **R** -
        """
        if initialization_override or self._last_updated - self._time__module.perf_counter() > 30:
            if _Registry.display_initialized:
                self._render_gpu = []
                self._video_gpu = []

                render_gpu = _Registry.context.info["GL_RENDERER"]
                raw_render_gpu_manufacturer = str(_Registry.context.info["GL_VENDOR"]).lower().split()

                if "nvidia" in raw_render_gpu_manufacturer:
                    render_gpu_manufacturer = "nvidia"
                elif "amd" in raw_render_gpu_manufacturer or "ati" in raw_render_gpu_manufacturer:
                    render_gpu_manufacturer = "amd"
                elif "intel" in raw_render_gpu_manufacturer:
                    render_gpu_manufacturer = "intel"
                else:
                    render_gpu_manufacturer = raw_render_gpu_manufacturer[0] # assume manufacture name is first.

                identified_gpus = self._gpus.get_all_gpus()
                all_gpus_are_unique = self._gpus.all_gpus_are_unique()
                self._video_gpu: list = identified_gpus
                if all_gpus_are_unique:
                    for gpu in identified_gpus:
                        if gpu.get_name() == render_gpu:
                            self._render_gpu = gpu
                            self._video_gpu.remove(gpu)
                            break
                else:
                    for gpu in identified_gpus:
                        if render_gpu_manufacturer in gpu.get_name().lower():
                            self._render_gpu = gpu
                            self._video_gpu.remove(gpu)
                            break

                self._video_gpu.append(self._render_gpu)

    def get_render_gpu(self):
        """
        🟩 **R** -
        """
        return self._render_gpu

    def get_video_gpu(self, index=0):
        """
        🟩 **R** -
        """
        if len(self._video_gpu) > 0:
            return self._video_gpu[index]

    def get_all_video_gpus(self):
        """
        🟩 **R** -
        """
        return self._video_gpu