import json as _json
import gc as _gc
import threading as _threading

import wmi as _wmi
import pyadl as _pyadl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.gpu import GPU as _GPU

from pmma.python_src.executor import Executor as _Executor

class GPUsIntermediary:
    def uuid_cleaner(self, uuid):
        uuid = uuid.strip()
        uuid = uuid.replace("\\", "_")
        return uuid[:66]

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        initialize(self, unique_instance=Constants.GPUS_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        self._unique_gpus = {} # {"bus": n, "uuid": n}: {SMI: n, ADL: n, WMI, n}

        raw_GPUs = _pyadl.ADLManager.getInstance().getDevices()
        adl_index = 0
        for raw_gpu in raw_GPUs:
            adl_bus = raw_gpu.__dict__["busNumber"]
            adl_uuid = raw_gpu.__dict__["uuid"]
            adl_uuid = adl_uuid.decode("utf-8")
            adl_uuid = self.uuid_cleaner(adl_uuid)
            json_identifier = _json.dumps({"bus": adl_bus, "uuid": adl_uuid})
            self._unique_gpus[json_identifier] = {Constants.SMI: None, Constants.WMI: None, Constants.PYADL: adl_index}
            adl_index += 1

        nvidia_smi = find_executable_nvidia_smi()
        if nvidia_smi is not None:
            self._executor = _Executor()
            self._executor.run([
                f"{nvidia_smi}",
                "--query-gpu=index,pci.bus",
                "--format=csv,noheader"])

            for line in self._executor.get_result().splitlines():
                index, hex_bus = line.split(",")
                smi_index = int(index.strip())
                smi_bus = int(hex_bus.strip(), base=16)
                for key in self._unique_gpus:
                    unloaded_key = _json.loads(key)
                    if unloaded_key["bus"] == smi_bus:
                        self._unique_gpus[key][Constants.SMI] = smi_index

        computer = _wmi.WMI()
        wmi_index = 0
        for gpu in computer.Win32_VideoController():
            wmi_uuid = getattr(gpu, "PNPDeviceID")
            wmi_uuid = self.uuid_cleaner(wmi_uuid)
            for key in self._unique_gpus:
                unloaded_key = _json.loads(key)
                if unloaded_key["uuid"] == wmi_uuid:
                    self._unique_gpus[key][Constants.WMI] = wmi_index

            wmi_index += 1


        gpu_instances = []
        self._gpu_instances = []
        for key in self._unique_gpus:
            gpu_instances.append(_GPU(self._unique_gpus[key]))

        threads = []
        for gpu in gpu_instances:
            thread = _threading.Thread(target=gpu.update, kwargs={"everything": True, "wait_for_completion": True})
            thread.name = "GPUs:Get_Data_Thread"
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for gpu in gpu_instances:
            self._gpu_instances.append(gpu)

        if len(self._gpu_instances) == 0:
            log_warning("No GPU devices were detected.")
            log_development("PMMA was unable to detect any GPU devices. \
Whilst this doesn't mean that PMMA wont run, it does mean that some \
mechanics may run slower than expected.")

    def identify_gpus(self):
        for i in range(len(self._gpu_instances)):
            print(f"GPU: {i}, has name: {self._gpu_instances[i].get_name()}")

    def get_gpu(self, gpu_index):
        return self._gpu_instances[gpu_index]