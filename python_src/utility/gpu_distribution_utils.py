from gc import collect as _gc__collect
from time import perf_counter as _time__perf_counter

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class GPUDistributionManager:
    def __init__(self):
        _initialize(self, unique_instance=_Constants.GPU_DISTRIBUTION_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        if not _Constants.GPUS_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.GPUS_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.gpu_utils import GPUsIntermediary as _GPUsIntermediary
            _GPUsIntermediary()

        self._gpus = _Registry.pmma_module_spine[_Constants.GPUS_INTERMEDIARY_OBJECT]

        self._render_gpu = None
        self._video_gpu = []
        self._last_updated = _time__perf_counter()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def update_gpu_roles(self, initialization_override=False):
        if initialization_override or self._last_updated - _time__perf_counter() > 30:
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
        return self._render_gpu

    def get_video_gpu(self, index=0):
        if len(self._video_gpu) > 0:
            return self._video_gpu[index]

    def get_all_video_gpus(self):
        return self._video_gpu