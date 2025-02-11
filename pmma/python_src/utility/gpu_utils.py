from json import dumps as _json__dumps
from json import loads as _json__loads
from threading import Thread as _threading__Thread
from typing import List as _List

try:
    from pyadl import ADLManager as _pyadl__ADLManager
    pyadl_available = True
except Exception as error:
    if type(error) != ModuleNotFoundError:
        pyadl_available = False
    else:
        raise error

from pmma.python_src.general import get_operating_system as _get_operating_system
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.gpu import GPU as _GPU
from pmma.python_src.executor import Executor as _Executor

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.general_utils import find_executable_nvidia_smi as _find_executable_nvidia_smi
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

if _get_operating_system() == _Constants.WINDOWS:
    from wmi import WMI as _wmi__WMI

class GPUsIntermediary:
    """
    🟩 **R** -
    """
    def uuid_cleaner(self, uuid):
        """
        🟩 **R** -
        """
        uuid = uuid.strip()
        uuid = uuid.replace("\\", "_")
        return uuid[:66]

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.GPUS_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        self._logger = _InternalLogger()

        self._unique_gpus = {} # {"bus": n, "uuid": n}: {SMI: n, ADL: n, WMI, n}

        if pyadl_available:
            raw_GPUs = _pyadl__ADLManager.getInstance().getDevices()
            adl_index = 0
            for raw_gpu in raw_GPUs:
                adl_bus = raw_gpu.__dict__["busNumber"]
                adl_uuid: bytes = raw_gpu.__dict__["uuid"]
                adl_uuid = adl_uuid.decode("utf-8")
                adl_uuid = self.uuid_cleaner(adl_uuid)
                json_identifier = _json__dumps({"bus": adl_bus, "uuid": adl_uuid})
                self._unique_gpus[json_identifier] = {_Constants.SMI: None, _Constants.WMI: None, _Constants.PYADL: adl_index}
                adl_index += 1

        nvidia_smi = _find_executable_nvidia_smi()
        if nvidia_smi is not None:
            self._executor = _Executor()
            self._executor.run([
                f"{nvidia_smi}",
                "--query-gpu=index,pci.bus,gpu_name",
                "--format=csv,noheader"])

            executor_result = self._executor.get_result()

            if executor_result is not None:
                for line in executor_result.splitlines():
                    index, hex_bus, name = line.split(",")
                    smi_index = int(index.strip())
                    smi_bus = int(hex_bus.strip(), base=16)
                    for key in self._unique_gpus:
                        unloaded_key = _json__loads(key)
                        if unloaded_key["bus"] == smi_bus:
                            self._unique_gpus[key][_Constants.SMI] = smi_index

        if _get_operating_system() == _Constants.WINDOWS:
            computer = _wmi__WMI()
            wmi_index = 0
            for gpu in computer.Win32_VideoController():
                wmi_uuid = getattr(gpu, "PNPDeviceID")
                wmi_uuid = self.uuid_cleaner(wmi_uuid)
                for key in self._unique_gpus:
                    unloaded_key = _json__loads(key)
                    if unloaded_key["uuid"] == wmi_uuid:
                        self._unique_gpus[key][_Constants.WMI] = wmi_index

                wmi_index += 1

        gpu_instances: _List[_GPU] = []
        self._gpu_instances: _List[_GPU] = []
        for key in self._unique_gpus:
            gpu_instances.append(_GPU(self._unique_gpus[key]))

        threads: _List[_threading__Thread] = []
        for gpu in gpu_instances:
            thread = _threading__Thread(target=gpu.update, kwargs={"everything": True, "wait_for_completion": True})
            thread.name = "GPUs:Get_Data_Thread"
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        all_gpus_are_unique = True
        gpu_names = []
        for gpu in gpu_instances:
            if all_gpus_are_unique:
                if gpu.get_name() in gpu_names:
                    all_gpus_are_unique = False
                    break

        self._all_gpus_are_unique = all_gpus_are_unique

        for gpu in gpu_instances:
            self._gpu_instances.append(gpu)

        if len(self._gpu_instances) == 0:
            self._logger.log_warning("No GPU devices were detected.")
            self._logger.log_development("PMMA was unable to detect any GPU devices. \
Whilst this doesn't mean that PMMA wont run, it does mean that some \
mechanics may run slower than expected.")

    def identify_gpus(self):
        """
        🟩 **R** -
        """
        for i in range(len(self._gpu_instances)):
            print(f"GPU: {i}, has name: {self._gpu_instances[i].get_name()}")

    def get_gpu(self, gpu_index):
        """
        🟩 **R** -
        """
        return self._gpu_instances[gpu_index]

    def all_gpus_are_unique(self):
        """
        🟩 **R** -
        """
        return self._all_gpus_are_unique

    def get_gpu_count(self):
        """
        🟩 **R** -
        """
        return len(self._gpu_instances)

    def get_all_gpus(self):
        """
        🟩 **R** -
        """
        return self._gpu_instances