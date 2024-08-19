import json

import wmi
import pyadl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.executor import Executor

from pmma.python_src.utility.gpu_utils import GPU

class GPUs:
    def _uuid_cleaner(self, uuid):
        uuid = uuid.strip()
        uuid = uuid.replace("\\", "_")
        return uuid[:66]

    def __init__(self):
        initialize(self, unique_instance=Constants.GPUS_OBJECT, add_to_pmma_module_spine=True)

        self.unique_gpus = {} # {"bus": n, "uuid": n}: {SMI: n, ADL: n, WMI, n}

        raw_GPUs = pyadl.ADLManager.getInstance().getDevices()
        adl_index = 0
        for raw_gpu in raw_GPUs:
            adl_bus = raw_gpu.__dict__["busNumber"]
            adl_uuid = raw_gpu.__dict__["uuid"]
            adl_uuid = adl_uuid.decode("utf-8")
            adl_uuid = self._uuid_cleaner(adl_uuid)
            json_identifier = json.dumps({"bus": adl_bus, "uuid": adl_uuid})
            self.unique_gpus[json_identifier] = {Constants.SMI: None, Constants.WMI: None, Constants.PYADL: adl_index}
            adl_index += 1

        nvidia_smi = find_executable_nvidia_smi()
        if nvidia_smi is not None:
            self.executor = Executor()
            self.executor.run(f"{nvidia_smi} --query-gpu=index,pci.bus, --format=csv,noheader")

            for line in self.executor.result.splitlines():
                index, hex_bus = line.split(",")
                smi_index = int(index.strip())
                smi_bus = int(hex_bus.strip(), base=16)
                for key in self.unique_gpus:
                    unloaded_key = json.loads(key)
                    if unloaded_key["bus"] == smi_bus:
                        self.unique_gpus[key][Constants.SMI] = smi_index

        computer = wmi.WMI()
        wmi_index = 0
        for gpu in computer.Win32_VideoController():
            wmi_uuid = getattr(gpu, "PNPDeviceID")
            wmi_uuid = self._uuid_cleaner(wmi_uuid)
            for key in self.unique_gpus:
                unloaded_key = json.loads(key)
                if unloaded_key["uuid"] == wmi_uuid:
                    self.unique_gpus[key][Constants.WMI] = wmi_index

            wmi_index += 1

        self.gpu_instances = []
        for key in self.unique_gpus:
            self.gpu_instances.append(GPU(self.unique_gpus[key]))