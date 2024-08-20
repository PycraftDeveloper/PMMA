import json as _json
import gc as _gc
import threading as _threading

import wmi as _wmi
import pyadl as _pyadl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.executor import Executor as _Executor

if get_operating_system() == Constants.WINDOWS:
    import pythoncom as _pythoncom

class GPUs:
    def _uuid_cleaner(self, uuid):
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
        initialize(self, unique_instance=Constants.GPUS_OBJECT, add_to_pmma_module_spine=True)

        self.unique_gpus = {} # {"bus": n, "uuid": n}: {SMI: n, ADL: n, WMI, n}

        raw_GPUs = _pyadl.ADLManager.getInstance().getDevices()
        adl_index = 0
        for raw_gpu in raw_GPUs:
            adl_bus = raw_gpu.__dict__["busNumber"]
            adl_uuid = raw_gpu.__dict__["uuid"]
            adl_uuid = adl_uuid.decode("utf-8")
            adl_uuid = self._uuid_cleaner(adl_uuid)
            json_identifier = _json.dumps({"bus": adl_bus, "uuid": adl_uuid})
            self.unique_gpus[json_identifier] = {Constants.SMI: None, Constants.WMI: None, Constants.PYADL: adl_index}
            adl_index += 1

        nvidia_smi = find_executable_nvidia_smi()
        if nvidia_smi is not None:
            self.executor = _Executor()
            self.executor.run([
                f"{nvidia_smi}",
                "--query-gpu=index,pci.bus",
                "--format=csv,noheader"])

            for line in self.executor.result.splitlines():
                index, hex_bus = line.split(",")
                smi_index = int(index.strip())
                smi_bus = int(hex_bus.strip(), base=16)
                for key in self.unique_gpus:
                    unloaded_key = _json.loads(key)
                    if unloaded_key["bus"] == smi_bus:
                        self.unique_gpus[key][Constants.SMI] = smi_index

        computer = _wmi.WMI()
        wmi_index = 0
        for gpu in computer.Win32_VideoController():
            wmi_uuid = getattr(gpu, "PNPDeviceID")
            wmi_uuid = self._uuid_cleaner(wmi_uuid)
            for key in self.unique_gpus:
                unloaded_key = _json.loads(key)
                if unloaded_key["uuid"] == wmi_uuid:
                    self.unique_gpus[key][Constants.WMI] = wmi_index

            wmi_index += 1


        gpu_instances = []
        self.gpu_instances = []
        for key in self.unique_gpus:
            gpu_instances.append(_GPU(self.unique_gpus[key]))

        threads = []
        for gpu in gpu_instances:
            thread = _threading.Thread(target=gpu.update, kwargs={"everything": True, "wait_for_completion": True})
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for gpu in gpu_instances:
            self.gpu_instances.append(gpu)

        if len(self.gpu_instances) == 0:
            log_warning("No GPU devices were detected.")
            log_development("PMMA was unable to detect any GPU devices. \
Whilst this doesn't mean that PMMA wont run, it does mean that some \
mechanics may run slower than expected.")

    def identify_gpus(self):
        for i in range(len(self.gpu_instances)):
            print(f"GPU: {i}, has name: {self.gpu_instances[i].get_name()}")

    def get_gpu(self, gpu_index):
        return self.gpu_instances[gpu_index]

class _GPU:
    def __init__(self, module_identification_indices):
        initialize(self)

        self.module_identification_indices = module_identification_indices
        self.executor = _Executor()

        self.accelerator_capabilities = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['AcceleratorCapabilities'], Constants.PYADL: []}}
        self.accounting_mode_enabled = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['accounting.mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.accounting_mode_buffer_size = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['accounting.buffer_size'], Constants.WMI: [], Constants.PYADL: []}}
        self.adapter_compatibility = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['AdapterCompatibility'], Constants.PYADL: []}}
        self.adapter_DAC_type = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['AdapterDACType'], Constants.PYADL: []}}
        self.adapter_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['adapterID']}}
        self.adapter_index = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['adapterIndex']}}
        self.addressing_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['addressing_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.availability = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['Availability'], Constants.PYADL: []}}
        self.capability_descriptions = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CapabilityDescriptions'], Constants.PYADL: []}}
        self.caption = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['Caption'], Constants.PYADL: []}}
        self.chip_to_chip_interconnect_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['c2c.mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_as_bitmap = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.active', 'clocks_throttle_reasons.active'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_application_setting = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.applications_clocks_setting', 'clocks_throttle_reasons.applications_clocks_setting'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_is_hardware_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.hw_slowdown', 'clocks_throttle_reasons.hw_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_gpu_idle_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.gpu_idle', 'clocks_throttle_reasons.gpu_idle'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_software_power_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.sw_power_cap', 'clocks_throttle_reasons.sw_power_cap'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_software_thermal_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.sw_thermal_slowdown', 'clocks_throttle_reasons.sw_thermal_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_power_break_slowdown_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.hw_power_brake_slowdown', 'clocks_throttle_reasons.hw_power_brake_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.supported', 'clocks_throttle_reasons.supported'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_sync_boost = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.sync_boost', 'clocks_throttle_reasons.sync_boost'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_thermal_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks_event_reasons.hw_thermal_slowdown', 'clocks_throttle_reasons.hw_thermal_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.color_table_entries = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ColorTableEntries'], Constants.PYADL: []}}
        self.compute_cap = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['compute_cap'], Constants.WMI: [], Constants.PYADL: []}}
        self.compute_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['compute_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.config_manager_error_code = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ConfigManagerErrorCode'], Constants.PYADL: []}}
        self.config_manager_user_config = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ConfigManagerUserConfig'], Constants.PYADL: []}}
        self.core_voltage = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getCurrentCoreVoltage']}}
        self.core_voltage_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['coreVoltageRange']}}
        self.creation_class_name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CreationClassName'], Constants.PYADL: []}}
        self.current_bits_per_pixel = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentBitsPerPixel'], Constants.PYADL: []}}
        self.current_horizontal_resolution = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentHorizontalResolution'], Constants.PYADL: []}}
        self.current_number_of_colors = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentNumberOfColors'], Constants.PYADL: []}}
        self.current_number_of_columns = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentNumberOfColumns'], Constants.PYADL: []}}
        self.current_number_of_rows = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentNumberOfRows'], Constants.PYADL: []}}
        self.current_refresh_rate = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentRefreshRate'], Constants.PYADL: []}}
        self.current_scan_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentScanMode'], Constants.PYADL: []}}
        self.current_vertical_resolution = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['CurrentVerticalResolution'], Constants.PYADL: []}}
        self.description = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['Description'], Constants.PYADL: []}}
        self.device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['DeviceID'], Constants.PYADL: []}}
        self.device_specific_pens = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['DeviceSpecificPens'], Constants.PYADL: []}}
        self.display_active = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['display_active'], Constants.WMI: [], Constants.PYADL: []}}
        self.display_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['display_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.dither_type = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['DitherType'], Constants.PYADL: []}}
        self.driver_date = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['DriverDate'], Constants.PYADL: []}}
        self.driver_model_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['driver_model.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.driver_model_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['driver_model.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.driver_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['driver_version'], Constants.WMI: ['DriverVersion'], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.aggregate.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.corrected.volatile.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.aggregate.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.errors.uncorrected.volatile.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_mode_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['ecc.mode.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.encoder_average_FPS = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['encoder.stats.averageFps'], Constants.WMI: [], Constants.PYADL: []}}
        self.encoder_average_latency = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['encoder.stats.averageLatency'], Constants.WMI: [], Constants.PYADL: []}}
        self.encoder_session_count = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['encoder.stats.sessionCount'], Constants.WMI: [], Constants.PYADL: []}}
        self.engine_clock_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['engineClockRange']}}
        self.error_cleared = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ErrorCleared'], Constants.PYADL: []}}
        self.error_description = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ErrorDescription'], Constants.PYADL: []}}
        self.fabric_state = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['fabric.state'], Constants.WMI: [], Constants.PYADL: []}}
        self.fabric_status = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['fabric.status'], Constants.WMI: [], Constants.PYADL: []}}
        self.fan_speed_percentage = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['fan.speed'], Constants.WMI: [], Constants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self.fan_speed_percentage_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self.fan_speed_RPM = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self.fan_speed_RPM_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self.fractional_multi_vGPU = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['vgpu_device_capability.fractional_multiVgpu'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_default_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.default_applications.graphics', 'clocks.default_applications.gr'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_default_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.default_applications.memory', 'clocks.default_applications.mem'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.applications.memory', 'clocks.applications.mem'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.applications.graphics', 'clocks.applications.gr'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_maximum_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.max.memory', 'clocks.max.mem'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_maximum_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.max.graphics', 'clocks.max.gr'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_maximum_streaming_multiprocessor_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.max.sm', 'clocks.max.sm'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.current.memory', 'clocks.mem'], Constants.WMI: [], Constants.PYADL: ['getCurrentMemoryClock']}}
        self.frequency_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.current.graphics', 'clocks.gr'], Constants.WMI: [], Constants.PYADL: ['getCurrentEngineClock']}}
        self.frequency_streaming_multiprocessor_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.current.sm', 'clocks.sm'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_video_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['clocks.current.video', 'clocks.video'], Constants.WMI: [], Constants.PYADL: []}}
        self.heterogenous_multi_vGPU = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['vgpu_driver_capability.heterogenous_multivGPU'], Constants.WMI: [], Constants.PYADL: []}}
        self.heterogenous_time_slice_profile = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_profile'], Constants.WMI: [], Constants.PYADL: []}}
        self.heterogenous_time_slice_sizes = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_sizes'], Constants.WMI: [], Constants.PYADL: []}}
        self.ICM_indent = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ICMIntent'], Constants.PYADL: []}}
        self.ICM_method = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ICMMethod'], Constants.PYADL: []}}
        self.inf_filename = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['InfFilename'], Constants.PYADL: []}}
        self.inf_section = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['InfSection'], Constants.PYADL: []}}
        self.info_ROM_ecc = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['inforom.ecc'], Constants.WMI: [], Constants.PYADL: []}}
        self.info_ROM_oem = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['inforom.oem'], Constants.WMI: [], Constants.PYADL: []}}
        self.info_ROM_power = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['inforom.pwr', 'inforom.power'], Constants.WMI: [], Constants.PYADL: []}}
        self.info_ROM_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['inforom.img', 'inforom.image'], Constants.WMI: [], Constants.PYADL: []}}
        self.install_date = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['InstallDate'], Constants.PYADL: []}}
        self.installed_display_drivers = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['InstalledDisplayDrivers'], Constants.PYADL: []}}
        self.last_error_code = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['LastErrorCode'], Constants.PYADL: []}}
        self.max_memory_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['MaxMemorySupported'], Constants.PYADL: []}}
        self.max_number_controlled = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['MaxNumberControlled'], Constants.PYADL: []}}
        self.max_refresh_rate = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['MaxRefreshRate'], Constants.PYADL: []}}
        self.memory_clock_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getMemoryClockRange']}}
        self.memory_free = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['memory.free'], Constants.WMI: [], Constants.PYADL: []}}
        self.memory_reserved = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['memory.reserved'], Constants.WMI: [], Constants.PYADL: []}}
        self.memory_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['memory.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.memory_used = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['memory.used'], Constants.WMI: [], Constants.PYADL: []}}
        self.min_refresh_rate = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['MinRefreshRate'], Constants.PYADL: []}}
        self.monochrome = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['Monochrome'], Constants.PYADL: []}}
        self.multi_instance_GPU_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['mig.mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.multi_instance_GPU_mode_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['mig.mode.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['name', 'gpu_name'], Constants.WMI: ['Name'], Constants.PYADL: ['adapterName']}}
        self.number_of_color_planes = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['NumberOfColorPlanes'], Constants.PYADL: []}}
        self.number_of_video_pages = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['NumberOfVideoPages'], Constants.PYADL: []}}
        self.operating_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['gom.current', 'gpu_operation_mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.operating_mode_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['gom.pending', 'gpu_operation_mode.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_bus = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pci.bus'], Constants.WMI: [], Constants.PYADL: ['busNumber']}}
        self.pci_bus_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pci.bus_id', 'gpu_bus_id'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_device = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pci.device'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pci.device_id'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_domain = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pci.domain'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pcie.link.gen.gpucurrent'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_device_host_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pcie.link.gen.max'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_gpu_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pcie.link.gen.gpumax'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pcie.link.gen.hostmax'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_width_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pcie.link.width.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_width_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pcie.link.width.max'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_sub_device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pci.sub_device_id'], Constants.WMI: [], Constants.PYADL: []}}
        self.persistence_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['persistence_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.PNP_device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['PNPDeviceID'], Constants.PYADL: []}}
        self.power_draw = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.draw'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_average = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.draw.average'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_default_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.default_limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_enforced_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['enforced.power.limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_instant = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.draw.instant'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.max_limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_minimum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.min_limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_management_capabilities = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['PowerManagementCapabilities'], Constants.PYADL: []}}
        self.power_management_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['power.management'], Constants.WMI: ['PowerManagementSupported'], Constants.PYADL: []}}
        self.protected_memory_free = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['protected_memory.free'], Constants.WMI: [], Constants.PYADL: []}}
        self.protected_memory_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['protected_memory.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.protected_memory_used = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['protected_memory.used'], Constants.WMI: [], Constants.PYADL: []}}
        self.protocol_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ProtocolSupported'], Constants.PYADL: []}}
        self.performance_state = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['pstate'], Constants.WMI: [], Constants.PYADL: []}}
        self.retired_pages_double_bit_ecc_errors_count = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['retired_pages.double_bit.count', 'retired_pages.dbe'], Constants.WMI: [], Constants.PYADL: []}}
        self.retired_pages_single_bit_ecc_errors_count = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['retired_pages.single_bit_ecc.count', 'retired_pages.sbe'], Constants.WMI: [], Constants.PYADL: []}}
        self.retired_pages_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['retired_pages.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.reserved_system_palette_entries = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['ReservedSystemPaletteEntries'], Constants.PYADL: []}}
        self.reset_required = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['reset_status.reset_required'], Constants.WMI: [], Constants.PYADL: []}}
        self.reset_and_drain_recommended = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['reset_status.drain_and_reset_recommended'], Constants.WMI: [], Constants.PYADL: []}}
        self.serial = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['serial', 'gpu_serial'], Constants.WMI: [], Constants.PYADL: []}}
        self.specification_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['SpecificationVersion'], Constants.PYADL: []}}
        self.status = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['Status'], Constants.PYADL: []}}
        self.status_info = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['StatusInfo'], Constants.PYADL: []}}
        self.system_creation_class_name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['SystemCreationClassName'], Constants.PYADL: []}}
        self.system_name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['SystemName'], Constants.PYADL: []}}
        self.system_palette_entries = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['SystemPaletteEntries'], Constants.PYADL: []}}
        self.GPU_system_processor_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['gsp.mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.GPU_system_processor_mode_default = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['gsp.mode.default'], Constants.WMI: [], Constants.PYADL: []}}
        self.temperature_core = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['temperature.gpu'], Constants.WMI: [], Constants.PYADL: ['getCurrentTemperature']}}
        self.temperature_core_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['temperature.gpu.tlimit'], Constants.WMI: [], Constants.PYADL: []}}
        self.temperature_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['temperature.memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.time_of_last_reset = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['TimeOfLastReset'], Constants.PYADL: []}}
        self.utilization_decoder = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['utilization.decoder'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_encoder = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['utilization.encoder'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_gpu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['utilization.gpu'], Constants.WMI: [], Constants.PYADL: ['getCurrentUsage']}}
        self.utilization_jpeg = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['utilization.jpeg'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['utilization.memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_optical_flow = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['utilization.ofa'], Constants.WMI: [], Constants.PYADL: []}}
        self.uuid = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['uuid', 'gpu_uuid'], Constants.WMI: [], Constants.PYADL: ['uuid']}}
        self.vbios_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: ['vbios_version'], Constants.WMI: [], Constants.PYADL: []}}
        self.video_architecture = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['VideoArchitecture'], Constants.PYADL: []}}
        self.video_memory_type = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['VideoMemoryType'], Constants.PYADL: []}}
        self.video_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['VideoMode'], Constants.PYADL: []}}
        self.video_mode_description = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['VideoModeDescription'], Constants.PYADL: []}}
        self.video_processor = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, Constants.DATA_COLLECTION_METHODS: {Constants.SMI: [], Constants.WMI: ['VideoProcessor'], Constants.PYADL: []}}

        self.gpu_data_points = [
            "accelerator_capabilities",
            "accounting_mode_enabled",
            "accounting_mode_buffer_size",
            "adapter_compatibility",
            "adapter_DAC_type",
            "adapter_id",
            "adapter_index",
            "addressing_mode",
            "availability",
            "capability_descriptions",
            "caption",
            "chip_to_chip_interconnect_mode",
            "clock_event_reasons_as_bitmap",
            "clock_event_reasons_application_setting",
            "clock_event_reasons_is_hardware_limited",
            "clock_event_reasons_gpu_idle_limited",
            "clock_event_reasons_software_power_limited",
            "clock_event_reasons_software_thermal_limited",
            "clock_event_reasons_power_break_slowdown_limited",
            "clock_event_reasons_supported",
            "clock_event_reasons_sync_boost",
            "clock_event_reasons_thermal_limited",
            "color_table_entries",
            "compute_cap",
            "compute_mode",
            "config_manager_error_code",
            "config_manager_user_config",
            "core_voltage",
            "core_voltage_range",
            "creation_class_name",
            "current_bits_per_pixel",
            "current_horizontal_resolution",
            "current_number_of_colors",
            "current_number_of_columns",
            "current_number_of_rows",
            "current_refresh_rate",
            "current_scan_mode",
            "current_vertical_resolution",
            "description",
            "device_id",
            "device_specific_pens",
            "display_active",
            "display_mode",
            "dither_type",
            "driver_date",
            "driver_model_current",
            "driver_model_pending",
            "driver_version",
            "ecc_errors_corrected_all_time_in_cbu",
            "ecc_errors_corrected_all_time_in_primary_cache",
            "ecc_errors_corrected_all_time_in_register_file",
            "ecc_errors_corrected_all_time_in_secondary_cache",
            "ecc_errors_corrected_all_time_in_shared_memory",
            "ecc_errors_corrected_all_time_in_sram",
            "ecc_errors_corrected_all_time_in_texture_memory",
            "ecc_errors_corrected_all_time_in_total",
            "ecc_errors_corrected_all_time_in_video_memory",
            "ecc_errors_corrected_since_reboot_in_cbu",
            "ecc_errors_corrected_since_reboot_in_primary_cache",
            "ecc_errors_corrected_since_reboot_in_register_file",
            "ecc_errors_corrected_since_reboot_in_secondary_cache",
            "ecc_errors_corrected_since_reboot_in_shared_memory",
            "ecc_errors_corrected_since_reboot_in_sram",
            "ecc_errors_corrected_since_reboot_in_texture_memory",
            "ecc_errors_corrected_since_reboot_in_total",
            "ecc_errors_corrected_since_reboot_in_video_memory",
            "ecc_errors_uncorrected_all_time_in_cbu",
            "ecc_errors_uncorrected_all_time_in_primary_cache",
            "ecc_errors_uncorrected_all_time_in_register_file",
            "ecc_errors_uncorrected_all_time_in_secondary_cache",
            "ecc_errors_uncorrected_all_time_in_shared_memory",
            "ecc_errors_uncorrected_all_time_in_sram",
            "ecc_errors_uncorrected_all_time_in_texture_memory",
            "ecc_errors_uncorrected_all_time_in_total",
            "ecc_errors_uncorrected_all_time_in_video_memory",
            "ecc_errors_uncorrected_since_reboot_in_cbu",
            "ecc_errors_uncorrected_since_reboot_in_primary_cache",
            "ecc_errors_uncorrected_since_reboot_in_register_file",
            "ecc_errors_uncorrected_since_reboot_in_secondary_cache",
            "ecc_errors_uncorrected_since_reboot_in_shared_memory",
            "ecc_errors_uncorrected_since_reboot_in_sram",
            "ecc_errors_uncorrected_since_reboot_in_texture_memory",
            "ecc_errors_uncorrected_since_reboot_in_total",
            "ecc_errors_uncorrected_since_reboot_in_video_memory",
            "ecc_mode_current",
            "ecc_mode_pending",
            "encoder_average_FPS",
            "encoder_average_latency",
            "encoder_session_count",
            "engine_clock_range",
            "error_cleared",
            "error_description",
            "fabric_state",
            "fabric_status",
            "fan_speed_percentage",
            "fan_speed_percentage_range",
            "fan_speed_RPM",
            "fan_speed_RPM_range",
            "fractional_multi_vGPU",
            "frequency_application_default_shader_clock",
            "frequency_application_default_memory_clock",
            "frequency_application_memory_clock",
            "frequency_application_shader_clock",
            "frequency_maximum_memory_clock",
            "frequency_maximum_shader_clock",
            "frequency_maximum_streaming_multiprocessor_clock",
            "frequency_memory_clock",
            "frequency_shader_clock",
            "frequency_streaming_multiprocessor_clock",
            "frequency_video_clock",
            "heterogenous_multi_vGPU",
            "heterogenous_time_slice_profile",
            "heterogenous_time_slice_sizes",
            "ICM_indent",
            "ICM_method",
            "inf_filename",
            "inf_section",
            "info_ROM_ecc",
            "info_ROM_oem",
            "info_ROM_power",
            "info_ROM_version",
            "install_date",
            "installed_display_drivers",
            "last_error_code",
            "max_memory_supported",
            "max_number_controlled",
            "max_refresh_rate",
            "memory_clock_range",
            "memory_free",
            "memory_reserved",
            "memory_total",
            "memory_used",
            "min_refresh_rate",
            "monochrome",
            "multi_instance_GPU_mode_current",
            "multi_instance_GPU_mode_pending",
            "name",
            "number_of_color_planes",
            "number_of_video_pages",
            "operating_mode_current",
            "operating_mode_pending",
            "pci_bus",
            "pci_bus_id",
            "pci_device",
            "pci_device_id",
            "pci_domain",
            "pci_link_generation_current",
            "pci_link_generation_device_host_maximum",
            "pci_link_generation_gpu_maximum",
            "pci_link_generation_maximum",
            "pci_link_width_current",
            "pci_link_width_maximum",
            "pci_sub_device_id",
            "persistence_mode",
            "PNP_device_id",
            "power_draw",
            "power_draw_average",
            "power_draw_default_limit",
            "power_draw_enforced_limit",
            "power_draw_instant",
            "power_draw_limit",
            "power_draw_maximum",
            "power_draw_minimum",
            "power_management_capabilities",
            "power_management_supported",
            "protected_memory_free",
            "protected_memory_total",
            "protected_memory_used",
            "protocol_supported",
            "performance_state",
            "retired_pages_double_bit_ecc_errors_count",
            "retired_pages_single_bit_ecc_errors_count",
            "retired_pages_pending",
            "reserved_system_palette_entries",
            "reset_required",
            "reset_and_drain_recommended",
            "serial",
            "specification_version",
            "status",
            "status_info",
            "system_creation_class_name",
            "system_name",
            "system_palette_entries",
            "GPU_system_processor_mode_current",
            "GPU_system_processor_mode_default",
            "temperature_core",
            "temperature_core_limit",
            "temperature_memory",
            "time_of_last_reset",
            "utilization_decoder",
            "utilization_encoder",
            "utilization_gpu",
            "utilization_jpeg",
            "utilization_memory",
            "utilization_optical_flow",
            "uuid",
            "vbios_version",
            "video_architecture",
            "video_memory_type",
            "video_mode",
            "video_mode_description",
            "video_processor"
        ]

        self.priorities = [Constants.SMI, Constants.PYADL, Constants.WMI]

    def update(self, everything=False, data_points=None, wait_for_completion=False):
        if get_operating_system() == Constants.WINDOWS:
            _pythoncom.CoInitialize()
        if wait_for_completion:
            self._update(everything=everything, data_points=data_points)
        else:
            thread = _threading.Thread(target=self._update, args=(everything, data_points))
            thread.daemon = True
            thread.name = "GPU:Update_Data_Thread"
            thread.start()

    def _update(self, everything, data_points):
        if data_points is None:
            data_points = self.gpu_data_points
        smi_data = ""
        smi_data_points = []
        adl_data = []
        adl_data_points = []
        wmi_data = []
        wmi_data_points = []
        for data_point in data_points:
            if self.__dict__[data_point][Constants.MANUALLY_SET] is False or everything:
                data_collection_strategies = self.__dict__[data_point][Constants.DATA_COLLECTION_METHODS]
                for query_command in data_collection_strategies[Constants.SMI]:
                    if self.module_identification_indices[Constants.SMI] is not None:
                        smi_data += f"{query_command},"
                        smi_data_points.append(data_point)
                for query_command in data_collection_strategies[Constants.PYADL]:
                    if self.module_identification_indices[Constants.PYADL] is not None:
                        adl_data.append(query_command)
                        adl_data_points.append(data_point)
                for query_command in data_collection_strategies[Constants.WMI]:
                    if self.module_identification_indices[Constants.WMI] is not None:
                        wmi_data.append(query_command)
                        wmi_data_points.append(data_point)

        smi_data = smi_data[:-1]

        set_attributes = []

        for priority in self.priorities:
            if priority == Constants.SMI and smi_data != "":
                self.executor.run([
                    find_executable_nvidia_smi(),
                    f"--query-gpu={smi_data}",
                    "--format=csv,noheader,nounits",
                    f"-i={self.module_identification_indices[Constants.SMI]}"])

                result = self.executor.get_result()
                split_result = result.split(", ")

                for data_point, data in zip(smi_data_points, split_result):
                    if "N/A" in data:
                        data = None
                    elif "Not Active" in data or "Disabled" in data:
                        data = False
                    elif "Active" in data or "Enabled" in data:
                        data = True
                    if data_point not in set_attributes:
                        self.__dict__[data_point][Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

            elif priority == Constants.PYADL and adl_data != []:
                gpu_data = _pyadl.ADLManager.getInstance().getDevices()[self.module_identification_indices[Constants.PYADL]]
                result = []
                for data_point in adl_data:
                    if ":" in data_point:
                        split_data_point = data_point.split(":")
                        name = split_data_point[0]
                        args = getattr(_pyadl, split_data_point[1])
                    else:
                        name = data_point
                    attr = getattr(gpu_data, name)
                    if callable(attr):
                        if ":" in data_point:
                            try:
                                result.append(attr(args, reload=everything))
                            except:
                                try:
                                    result.append(attr(args))
                                except:
                                    result.append(None)
                        else:
                            try:
                                result.append(attr())
                            except:
                                try:
                                    result.append(attr(reload=everything))
                                except:
                                    result.append(None)
                    else:
                        result.append(attr)

                for data_point, data in zip(adl_data_points, result):
                    try:
                        if type(data) == bytes:
                            data = data.decode("utf-8")
                    except:
                        pass

                    if data_point not in set_attributes:
                        self.__dict__[data_point][Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

            elif priority == Constants.WMI and wmi_data != [] and get_operating_system() == Constants.WINDOWS:
                computer = _wmi.WMI()
                gpu_data = computer.Win32_VideoController()[self.module_identification_indices[Constants.WMI]]
                result = []
                for data_point in wmi_data:
                    result.append(getattr(gpu_data, data_point))

                for data_point, data in zip(wmi_data_points, result):
                    try:
                        if type(data) == bytes:
                            data = data.decode("utf-8")
                    except:
                        pass

                    if data_point not in set_attributes:
                        self.__dict__[data_point][Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

        for data_point in data_points:
            self.__dict__[data_point][Constants.UPDATING] = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_accelerator_capabilities(self, update=False, wait_for_completion=False):
        value = self.accelerator_capabilities[Constants.VALUE]
        if update and self.accelerator_capabilities[Constants.UPDATING] is False:
            self.update(data_points=["accelerator_capabilities"], wait_for_completion=wait_for_completion)
        return value

    def get_accounting_mode_enabled(self, update=False, wait_for_completion=False):
        value = self.accounting_mode_enabled[Constants.VALUE]
        if update and self.accounting_mode_enabled[Constants.UPDATING] is False:
            self.update(data_points=["accounting_mode_enabled"], wait_for_completion=wait_for_completion)
        return value

    def get_accounting_mode_buffer_size(self, update=False, wait_for_completion=False):
        value = self.accounting_mode_buffer_size[Constants.VALUE]
        if update and self.accounting_mode_buffer_size[Constants.UPDATING] is False:
            self.update(data_points=["accounting_mode_buffer_size"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_compatibility(self, update=False, wait_for_completion=False):
        value = self.adapter_compatibility[Constants.VALUE]
        if update and self.adapter_compatibility[Constants.UPDATING] is False:
            self.update(data_points=["adapter_compatibility"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_DAC_type(self, update=False, wait_for_completion=False):
        value = self.adapter_DAC_type[Constants.VALUE]
        if update and self.adapter_DAC_type[Constants.UPDATING] is False:
            self.update(data_points=["adapter_DAC_type"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_id(self, update=False, wait_for_completion=False):
        value = self.adapter_id[Constants.VALUE]
        if update and self.adapter_id[Constants.UPDATING] is False:
            self.update(data_points=["adapter_id"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_index(self, update=False, wait_for_completion=False):
        value = self.adapter_index[Constants.VALUE]
        if update and self.adapter_index[Constants.UPDATING] is False:
            self.update(data_points=["adapter_index"], wait_for_completion=wait_for_completion)
        return value

    def get_addressing_mode(self, update=False, wait_for_completion=False):
        value = self.addressing_mode[Constants.VALUE]
        if update and self.addressing_mode[Constants.UPDATING] is False:
            self.update(data_points=["addressing_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_availability(self, update=False, wait_for_completion=False):
        value = self.availability[Constants.VALUE]
        if update and self.availability[Constants.UPDATING] is False:
            self.update(data_points=["availability"], wait_for_completion=wait_for_completion)
        return value

    def get_capability_descriptions(self, update=False, wait_for_completion=False):
        value = self.capability_descriptions[Constants.VALUE]
        if update and self.capability_descriptions[Constants.UPDATING] is False:
            self.update(data_points=["capability_descriptions"], wait_for_completion=wait_for_completion)
        return value

    def get_caption(self, update=False, wait_for_completion=False):
        value = self.caption[Constants.VALUE]
        if update and self.caption[Constants.UPDATING] is False:
            self.update(data_points=["caption"], wait_for_completion=wait_for_completion)
        return value

    def get_chip_to_chip_interconnect_mode(self, update=False, wait_for_completion=False):
        value = self.chip_to_chip_interconnect_mode[Constants.VALUE]
        if update and self.chip_to_chip_interconnect_mode[Constants.UPDATING] is False:
            self.update(data_points=["chip_to_chip_interconnect_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_as_bitmap(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_as_bitmap[Constants.VALUE]
        if update and self.clock_event_reasons_as_bitmap[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_as_bitmap"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_application_setting(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_application_setting[Constants.VALUE]
        if update and self.clock_event_reasons_application_setting[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_application_setting"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_is_hardware_limited(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_is_hardware_limited[Constants.VALUE]
        if update and self.clock_event_reasons_is_hardware_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_is_hardware_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_gpu_idle_limited(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_gpu_idle_limited[Constants.VALUE]
        if update and self.clock_event_reasons_gpu_idle_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_gpu_idle_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_software_power_limited(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_software_power_limited[Constants.VALUE]
        if update and self.clock_event_reasons_software_power_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_software_power_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_software_thermal_limited(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_software_thermal_limited[Constants.VALUE]
        if update and self.clock_event_reasons_software_thermal_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_software_thermal_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_power_break_slowdown_limited(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_power_break_slowdown_limited[Constants.VALUE]
        if update and self.clock_event_reasons_power_break_slowdown_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_power_break_slowdown_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_supported(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_supported[Constants.VALUE]
        if update and self.clock_event_reasons_supported[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_sync_boost(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_sync_boost[Constants.VALUE]
        if update and self.clock_event_reasons_sync_boost[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_sync_boost"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_thermal_limited(self, update=False, wait_for_completion=False):
        value = self.clock_event_reasons_thermal_limited[Constants.VALUE]
        if update and self.clock_event_reasons_thermal_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_thermal_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_color_table_entries(self, update=False, wait_for_completion=False):
        value = self.color_table_entries[Constants.VALUE]
        if update and self.color_table_entries[Constants.UPDATING] is False:
            self.update(data_points=["color_table_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_compute_cap(self, update=False, wait_for_completion=False):
        value = self.compute_cap[Constants.VALUE]
        if update and self.compute_cap[Constants.UPDATING] is False:
            self.update(data_points=["compute_cap"], wait_for_completion=wait_for_completion)
        return value

    def get_compute_mode(self, update=False, wait_for_completion=False):
        value = self.compute_mode[Constants.VALUE]
        if update and self.compute_mode[Constants.UPDATING] is False:
            self.update(data_points=["compute_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_config_manager_error_code(self, update=False, wait_for_completion=False):
        value = self.config_manager_error_code[Constants.VALUE]
        if update and self.config_manager_error_code[Constants.UPDATING] is False:
            self.update(data_points=["config_manager_error_code"], wait_for_completion=wait_for_completion)
        return value

    def get_config_manager_user_config(self, update=False, wait_for_completion=False):
        value = self.config_manager_user_config[Constants.VALUE]
        if update and self.config_manager_user_config[Constants.UPDATING] is False:
            self.update(data_points=["config_manager_user_config"], wait_for_completion=wait_for_completion)
        return value

    def get_core_voltage(self, update=False, wait_for_completion=False):
        value = self.core_voltage[Constants.VALUE]
        if update and self.core_voltage[Constants.UPDATING] is False:
            self.update(data_points=["core_voltage"], wait_for_completion=wait_for_completion)
        return value

    def get_core_voltage_range(self, update=False, wait_for_completion=False):
        value = self.core_voltage_range[Constants.VALUE]
        if update and self.core_voltage_range[Constants.UPDATING] is False:
            self.update(data_points=["core_voltage_range"], wait_for_completion=wait_for_completion)
        return value

    def get_creation_class_name(self, update=False, wait_for_completion=False):
        value = self.creation_class_name[Constants.VALUE]
        if update and self.creation_class_name[Constants.UPDATING] is False:
            self.update(data_points=["creation_class_name"], wait_for_completion=wait_for_completion)
        return value

    def get_current_bits_per_pixel(self, update=False, wait_for_completion=False):
        value = self.current_bits_per_pixel[Constants.VALUE]
        if update and self.current_bits_per_pixel[Constants.UPDATING] is False:
            self.update(data_points=["current_bits_per_pixel"], wait_for_completion=wait_for_completion)
        return value

    def get_current_horizontal_resolution(self, update=False, wait_for_completion=False):
        value = self.current_horizontal_resolution[Constants.VALUE]
        if update and self.current_horizontal_resolution[Constants.UPDATING] is False:
            self.update(data_points=["current_horizontal_resolution"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_colors(self, update=False, wait_for_completion=False):
        value = self.current_number_of_colors[Constants.VALUE]
        if update and self.current_number_of_colors[Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_colors"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_columns(self, update=False, wait_for_completion=False):
        value = self.current_number_of_columns[Constants.VALUE]
        if update and self.current_number_of_columns[Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_columns"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_rows(self, update=False, wait_for_completion=False):
        value = self.current_number_of_rows[Constants.VALUE]
        if update and self.current_number_of_rows[Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_rows"], wait_for_completion=wait_for_completion)
        return value

    def get_current_refresh_rate(self, update=False, wait_for_completion=False):
        value = self.current_refresh_rate[Constants.VALUE]
        if update and self.current_refresh_rate[Constants.UPDATING] is False:
            self.update(data_points=["current_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_current_scan_mode(self, update=False, wait_for_completion=False):
        value = self.current_scan_mode[Constants.VALUE]
        if update and self.current_scan_mode[Constants.UPDATING] is False:
            self.update(data_points=["current_scan_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_current_vertical_resolution(self, update=False, wait_for_completion=False):
        value = self.current_vertical_resolution[Constants.VALUE]
        if update and self.current_vertical_resolution[Constants.UPDATING] is False:
            self.update(data_points=["current_vertical_resolution"], wait_for_completion=wait_for_completion)
        return value

    def get_description(self, update=False, wait_for_completion=False):
        value = self.description[Constants.VALUE]
        if update and self.description[Constants.UPDATING] is False:
            self.update(data_points=["description"], wait_for_completion=wait_for_completion)
        return value

    def get_device_id(self, update=False, wait_for_completion=False):
        value = self.device_id[Constants.VALUE]
        if update and self.device_id[Constants.UPDATING] is False:
            self.update(data_points=["device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_device_specific_pens(self, update=False, wait_for_completion=False):
        value = self.device_specific_pens[Constants.VALUE]
        if update and self.device_specific_pens[Constants.UPDATING] is False:
            self.update(data_points=["device_specific_pens"], wait_for_completion=wait_for_completion)
        return value

    def get_display_active(self, update=False, wait_for_completion=False):
        value = self.display_active[Constants.VALUE]
        if update and self.display_active[Constants.UPDATING] is False:
            self.update(data_points=["display_active"], wait_for_completion=wait_for_completion)
        return value

    def get_display_mode(self, update=False, wait_for_completion=False):
        value = self.display_mode[Constants.VALUE]
        if update and self.display_mode[Constants.UPDATING] is False:
            self.update(data_points=["display_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_dither_type(self, update=False, wait_for_completion=False):
        value = self.dither_type[Constants.VALUE]
        if update and self.dither_type[Constants.UPDATING] is False:
            self.update(data_points=["dither_type"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_date(self, update=False, wait_for_completion=False):
        value = self.driver_date[Constants.VALUE]
        if update and self.driver_date[Constants.UPDATING] is False:
            self.update(data_points=["driver_date"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_model_current(self, update=False, wait_for_completion=False):
        value = self.driver_model_current[Constants.VALUE]
        if update and self.driver_model_current[Constants.UPDATING] is False:
            self.update(data_points=["driver_model_current"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_model_pending(self, update=False, wait_for_completion=False):
        value = self.driver_model_pending[Constants.VALUE]
        if update and self.driver_model_pending[Constants.UPDATING] is False:
            self.update(data_points=["driver_model_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_version(self, update=False, wait_for_completion=False):
        value = self.driver_version[Constants.VALUE]
        if update and self.driver_version[Constants.UPDATING] is False:
            self.update(data_points=["driver_version"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_cbu(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_cbu[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_primary_cache[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_register_file(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_register_file[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_secondary_cache[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_shared_memory[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_sram(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_sram[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_texture_memory[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_total(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_total[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_video_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_all_time_in_video_memory[Constants.VALUE]
        if update and self.ecc_errors_corrected_all_time_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_cbu(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_cbu[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_primary_cache[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_register_file(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_register_file[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_shared_memory[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_sram(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_sram[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_texture_memory[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_total(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_total[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_video_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_corrected_since_reboot_in_video_memory[Constants.VALUE]
        if update and self.ecc_errors_corrected_since_reboot_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_cbu(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_cbu[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_primary_cache[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_register_file(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_register_file[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_shared_memory[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_sram(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_sram[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_texture_memory[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_total(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_total[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_video_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_all_time_in_video_memory[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_all_time_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_cbu(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_cbu[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_register_file(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_register_file[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_sram(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_sram[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_total(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_total[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_video_memory(self, update=False, wait_for_completion=False):
        value = self.ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.VALUE]
        if update and self.ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_mode_current(self, update=False, wait_for_completion=False):
        value = self.ecc_mode_current[Constants.VALUE]
        if update and self.ecc_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["ecc_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_mode_pending(self, update=False, wait_for_completion=False):
        value = self.ecc_mode_pending[Constants.VALUE]
        if update and self.ecc_mode_pending[Constants.UPDATING] is False:
            self.update(data_points=["ecc_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_average_FPS(self, update=False, wait_for_completion=False):
        value = self.encoder_average_FPS[Constants.VALUE]
        if update and self.encoder_average_FPS[Constants.UPDATING] is False:
            self.update(data_points=["encoder_average_FPS"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_average_latency(self, update=False, wait_for_completion=False):
        value = self.encoder_average_latency[Constants.VALUE]
        if update and self.encoder_average_latency[Constants.UPDATING] is False:
            self.update(data_points=["encoder_average_latency"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_session_count(self, update=False, wait_for_completion=False):
        value = self.encoder_session_count[Constants.VALUE]
        if update and self.encoder_session_count[Constants.UPDATING] is False:
            self.update(data_points=["encoder_session_count"], wait_for_completion=wait_for_completion)
        return value

    def get_engine_clock_range(self, update=False, wait_for_completion=False):
        value = self.engine_clock_range[Constants.VALUE]
        if update and self.engine_clock_range[Constants.UPDATING] is False:
            self.update(data_points=["engine_clock_range"], wait_for_completion=wait_for_completion)
        return value

    def get_error_cleared(self, update=False, wait_for_completion=False):
        value = self.error_cleared[Constants.VALUE]
        if update and self.error_cleared[Constants.UPDATING] is False:
            self.update(data_points=["error_cleared"], wait_for_completion=wait_for_completion)
        return value

    def get_error_description(self, update=False, wait_for_completion=False):
        value = self.error_description[Constants.VALUE]
        if update and self.error_description[Constants.UPDATING] is False:
            self.update(data_points=["error_description"], wait_for_completion=wait_for_completion)
        return value

    def get_fabric_state(self, update=False, wait_for_completion=False):
        value = self.fabric_state[Constants.VALUE]
        if update and self.fabric_state[Constants.UPDATING] is False:
            self.update(data_points=["fabric_state"], wait_for_completion=wait_for_completion)
        return value

    def get_fabric_status(self, update=False, wait_for_completion=False):
        value = self.fabric_status[Constants.VALUE]
        if update and self.fabric_status[Constants.UPDATING] is False:
            self.update(data_points=["fabric_status"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_percentage(self, update=False, wait_for_completion=False):
        value = self.fan_speed_percentage[Constants.VALUE]
        if update and self.fan_speed_percentage[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_percentage"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_percentage_range(self, update=False, wait_for_completion=False):
        value = self.fan_speed_percentage_range[Constants.VALUE]
        if update and self.fan_speed_percentage_range[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_percentage_range"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_RPM(self, update=False, wait_for_completion=False):
        value = self.fan_speed_RPM[Constants.VALUE]
        if update and self.fan_speed_RPM[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_RPM"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_RPM_range(self, update=False, wait_for_completion=False):
        value = self.fan_speed_RPM_range[Constants.VALUE]
        if update and self.fan_speed_RPM_range[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_RPM_range"], wait_for_completion=wait_for_completion)
        return value

    def get_fractional_multi_vGPU(self, update=False, wait_for_completion=False):
        value = self.fractional_multi_vGPU[Constants.VALUE]
        if update and self.fractional_multi_vGPU[Constants.UPDATING] is False:
            self.update(data_points=["fractional_multi_vGPU"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_default_shader_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_application_default_shader_clock[Constants.VALUE]
        if update and self.frequency_application_default_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_default_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_default_memory_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_application_default_memory_clock[Constants.VALUE]
        if update and self.frequency_application_default_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_default_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_memory_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_application_memory_clock[Constants.VALUE]
        if update and self.frequency_application_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_shader_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_application_shader_clock[Constants.VALUE]
        if update and self.frequency_application_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_memory_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_maximum_memory_clock[Constants.VALUE]
        if update and self.frequency_maximum_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_shader_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_maximum_shader_clock[Constants.VALUE]
        if update and self.frequency_maximum_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_streaming_multiprocessor_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_maximum_streaming_multiprocessor_clock[Constants.VALUE]
        if update and self.frequency_maximum_streaming_multiprocessor_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_memory_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_memory_clock[Constants.VALUE]
        if update and self.frequency_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_shader_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_shader_clock[Constants.VALUE]
        if update and self.frequency_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_streaming_multiprocessor_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_streaming_multiprocessor_clock[Constants.VALUE]
        if update and self.frequency_streaming_multiprocessor_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_video_clock(self, update=False, wait_for_completion=False):
        value = self.frequency_video_clock[Constants.VALUE]
        if update and self.frequency_video_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_video_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_multi_vGPU(self, update=False, wait_for_completion=False):
        value = self.heterogenous_multi_vGPU[Constants.VALUE]
        if update and self.heterogenous_multi_vGPU[Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_multi_vGPU"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_time_slice_profile(self, update=False, wait_for_completion=False):
        value = self.heterogenous_time_slice_profile[Constants.VALUE]
        if update and self.heterogenous_time_slice_profile[Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_time_slice_profile"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_time_slice_sizes(self, update=False, wait_for_completion=False):
        value = self.heterogenous_time_slice_sizes[Constants.VALUE]
        if update and self.heterogenous_time_slice_sizes[Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_time_slice_sizes"], wait_for_completion=wait_for_completion)
        return value

    def get_ICM_indent(self, update=False, wait_for_completion=False):
        value = self.ICM_indent[Constants.VALUE]
        if update and self.ICM_indent[Constants.UPDATING] is False:
            self.update(data_points=["ICM_indent"], wait_for_completion=wait_for_completion)
        return value

    def get_ICM_method(self, update=False, wait_for_completion=False):
        value = self.ICM_method[Constants.VALUE]
        if update and self.ICM_method[Constants.UPDATING] is False:
            self.update(data_points=["ICM_method"], wait_for_completion=wait_for_completion)
        return value

    def get_inf_filename(self, update=False, wait_for_completion=False):
        value = self.inf_filename[Constants.VALUE]
        if update and self.inf_filename[Constants.UPDATING] is False:
            self.update(data_points=["inf_filename"], wait_for_completion=wait_for_completion)
        return value

    def get_inf_section(self, update=False, wait_for_completion=False):
        value = self.inf_section[Constants.VALUE]
        if update and self.inf_section[Constants.UPDATING] is False:
            self.update(data_points=["inf_section"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_ecc(self, update=False, wait_for_completion=False):
        value = self.info_ROM_ecc[Constants.VALUE]
        if update and self.info_ROM_ecc[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_ecc"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_oem(self, update=False, wait_for_completion=False):
        value = self.info_ROM_oem[Constants.VALUE]
        if update and self.info_ROM_oem[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_oem"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_power(self, update=False, wait_for_completion=False):
        value = self.info_ROM_power[Constants.VALUE]
        if update and self.info_ROM_power[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_power"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_version(self, update=False, wait_for_completion=False):
        value = self.info_ROM_version[Constants.VALUE]
        if update and self.info_ROM_version[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_version"], wait_for_completion=wait_for_completion)
        return value

    def get_install_date(self, update=False, wait_for_completion=False):
        value = self.install_date[Constants.VALUE]
        if update and self.install_date[Constants.UPDATING] is False:
            self.update(data_points=["install_date"], wait_for_completion=wait_for_completion)
        return value

    def get_installed_display_drivers(self, update=False, wait_for_completion=False):
        value = self.installed_display_drivers[Constants.VALUE]
        if update and self.installed_display_drivers[Constants.UPDATING] is False:
            self.update(data_points=["installed_display_drivers"], wait_for_completion=wait_for_completion)
        return value

    def get_last_error_code(self, update=False, wait_for_completion=False):
        value = self.last_error_code[Constants.VALUE]
        if update and self.last_error_code[Constants.UPDATING] is False:
            self.update(data_points=["last_error_code"], wait_for_completion=wait_for_completion)
        return value

    def get_max_memory_supported(self, update=False, wait_for_completion=False):
        value = self.max_memory_supported[Constants.VALUE]
        if update and self.max_memory_supported[Constants.UPDATING] is False:
            self.update(data_points=["max_memory_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_max_number_controlled(self, update=False, wait_for_completion=False):
        value = self.max_number_controlled[Constants.VALUE]
        if update and self.max_number_controlled[Constants.UPDATING] is False:
            self.update(data_points=["max_number_controlled"], wait_for_completion=wait_for_completion)
        return value

    def get_max_refresh_rate(self, update=False, wait_for_completion=False):
        value = self.max_refresh_rate[Constants.VALUE]
        if update and self.max_refresh_rate[Constants.UPDATING] is False:
            self.update(data_points=["max_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_clock_range(self, update=False, wait_for_completion=False):
        value = self.memory_clock_range[Constants.VALUE]
        if update and self.memory_clock_range[Constants.UPDATING] is False:
            self.update(data_points=["memory_clock_range"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_free(self, update=False, wait_for_completion=False):
        value = self.memory_free[Constants.VALUE]
        if update and self.memory_free[Constants.UPDATING] is False:
            self.update(data_points=["memory_free"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_reserved(self, update=False, wait_for_completion=False):
        value = self.memory_reserved[Constants.VALUE]
        if update and self.memory_reserved[Constants.UPDATING] is False:
            self.update(data_points=["memory_reserved"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_total(self, update=False, wait_for_completion=False):
        value = self.memory_total[Constants.VALUE]
        if update and self.memory_total[Constants.UPDATING] is False:
            self.update(data_points=["memory_total"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_used(self, update=False, wait_for_completion=False):
        value = self.memory_used[Constants.VALUE]
        if update and self.memory_used[Constants.UPDATING] is False:
            self.update(data_points=["memory_used"], wait_for_completion=wait_for_completion)
        return value

    def get_min_refresh_rate(self, update=False, wait_for_completion=False):
        value = self.min_refresh_rate[Constants.VALUE]
        if update and self.min_refresh_rate[Constants.UPDATING] is False:
            self.update(data_points=["min_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_monochrome(self, update=False, wait_for_completion=False):
        value = self.monochrome[Constants.VALUE]
        if update and self.monochrome[Constants.UPDATING] is False:
            self.update(data_points=["monochrome"], wait_for_completion=wait_for_completion)
        return value

    def get_multi_instance_GPU_mode_current(self, update=False, wait_for_completion=False):
        value = self.multi_instance_GPU_mode_current[Constants.VALUE]
        if update and self.multi_instance_GPU_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["multi_instance_GPU_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_multi_instance_GPU_mode_pending(self, update=False, wait_for_completion=False):
        value = self.multi_instance_GPU_mode_pending[Constants.VALUE]
        if update and self.multi_instance_GPU_mode_pending[Constants.UPDATING] is False:
            self.update(data_points=["multi_instance_GPU_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_name(self, update=False, wait_for_completion=False):
        value = self.name[Constants.VALUE]
        if update and self.name[Constants.UPDATING] is False:
            self.update(data_points=["name"], wait_for_completion=wait_for_completion)
        return value

    def get_number_of_color_planes(self, update=False, wait_for_completion=False):
        value = self.number_of_color_planes[Constants.VALUE]
        if update and self.number_of_color_planes[Constants.UPDATING] is False:
            self.update(data_points=["number_of_color_planes"], wait_for_completion=wait_for_completion)
        return value

    def get_number_of_video_pages(self, update=False, wait_for_completion=False):
        value = self.number_of_video_pages[Constants.VALUE]
        if update and self.number_of_video_pages[Constants.UPDATING] is False:
            self.update(data_points=["number_of_video_pages"], wait_for_completion=wait_for_completion)
        return value

    def get_operating_mode_current(self, update=False, wait_for_completion=False):
        value = self.operating_mode_current[Constants.VALUE]
        if update and self.operating_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["operating_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_operating_mode_pending(self, update=False, wait_for_completion=False):
        value = self.operating_mode_pending[Constants.VALUE]
        if update and self.operating_mode_pending[Constants.UPDATING] is False:
            self.update(data_points=["operating_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_bus(self, update=False, wait_for_completion=False):
        value = self.pci_bus[Constants.VALUE]
        if update and self.pci_bus[Constants.UPDATING] is False:
            self.update(data_points=["pci_bus"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_bus_id(self, update=False, wait_for_completion=False):
        value = self.pci_bus_id[Constants.VALUE]
        if update and self.pci_bus_id[Constants.UPDATING] is False:
            self.update(data_points=["pci_bus_id"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_device(self, update=False, wait_for_completion=False):
        value = self.pci_device[Constants.VALUE]
        if update and self.pci_device[Constants.UPDATING] is False:
            self.update(data_points=["pci_device"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_device_id(self, update=False, wait_for_completion=False):
        value = self.pci_device_id[Constants.VALUE]
        if update and self.pci_device_id[Constants.UPDATING] is False:
            self.update(data_points=["pci_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_domain(self, update=False, wait_for_completion=False):
        value = self.pci_domain[Constants.VALUE]
        if update and self.pci_domain[Constants.UPDATING] is False:
            self.update(data_points=["pci_domain"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_current(self, update=False, wait_for_completion=False):
        value = self.pci_link_generation_current[Constants.VALUE]
        if update and self.pci_link_generation_current[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_current"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_device_host_maximum(self, update=False, wait_for_completion=False):
        value = self.pci_link_generation_device_host_maximum[Constants.VALUE]
        if update and self.pci_link_generation_device_host_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_device_host_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_gpu_maximum(self, update=False, wait_for_completion=False):
        value = self.pci_link_generation_gpu_maximum[Constants.VALUE]
        if update and self.pci_link_generation_gpu_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_gpu_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_maximum(self, update=False, wait_for_completion=False):
        value = self.pci_link_generation_maximum[Constants.VALUE]
        if update and self.pci_link_generation_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_width_current(self, update=False, wait_for_completion=False):
        value = self.pci_link_width_current[Constants.VALUE]
        if update and self.pci_link_width_current[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_width_current"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_width_maximum(self, update=False, wait_for_completion=False):
        value = self.pci_link_width_maximum[Constants.VALUE]
        if update and self.pci_link_width_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_width_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_sub_device_id(self, update=False, wait_for_completion=False):
        value = self.pci_sub_device_id[Constants.VALUE]
        if update and self.pci_sub_device_id[Constants.UPDATING] is False:
            self.update(data_points=["pci_sub_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_persistence_mode(self, update=False, wait_for_completion=False):
        value = self.persistence_mode[Constants.VALUE]
        if update and self.persistence_mode[Constants.UPDATING] is False:
            self.update(data_points=["persistence_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_PNP_device_id(self, update=False, wait_for_completion=False):
        value = self.PNP_device_id[Constants.VALUE]
        if update and self.PNP_device_id[Constants.UPDATING] is False:
            self.update(data_points=["PNP_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw(self, update=False, wait_for_completion=False):
        value = self.power_draw[Constants.VALUE]
        if update and self.power_draw[Constants.UPDATING] is False:
            self.update(data_points=["power_draw"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_average(self, update=False, wait_for_completion=False):
        value = self.power_draw_average[Constants.VALUE]
        if update and self.power_draw_average[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_average"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_default_limit(self, update=False, wait_for_completion=False):
        value = self.power_draw_default_limit[Constants.VALUE]
        if update and self.power_draw_default_limit[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_default_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_enforced_limit(self, update=False, wait_for_completion=False):
        value = self.power_draw_enforced_limit[Constants.VALUE]
        if update and self.power_draw_enforced_limit[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_enforced_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_instant(self, update=False, wait_for_completion=False):
        value = self.power_draw_instant[Constants.VALUE]
        if update and self.power_draw_instant[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_instant"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_limit(self, update=False, wait_for_completion=False):
        value = self.power_draw_limit[Constants.VALUE]
        if update and self.power_draw_limit[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_maximum(self, update=False, wait_for_completion=False):
        value = self.power_draw_maximum[Constants.VALUE]
        if update and self.power_draw_maximum[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_minimum(self, update=False, wait_for_completion=False):
        value = self.power_draw_minimum[Constants.VALUE]
        if update and self.power_draw_minimum[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_minimum"], wait_for_completion=wait_for_completion)
        return value

    def get_power_management_capabilities(self, update=False, wait_for_completion=False):
        value = self.power_management_capabilities[Constants.VALUE]
        if update and self.power_management_capabilities[Constants.UPDATING] is False:
            self.update(data_points=["power_management_capabilities"], wait_for_completion=wait_for_completion)
        return value

    def get_power_management_supported(self, update=False, wait_for_completion=False):
        value = self.power_management_supported[Constants.VALUE]
        if update and self.power_management_supported[Constants.UPDATING] is False:
            self.update(data_points=["power_management_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_free(self, update=False, wait_for_completion=False):
        value = self.protected_memory_free[Constants.VALUE]
        if update and self.protected_memory_free[Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_free"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_total(self, update=False, wait_for_completion=False):
        value = self.protected_memory_total[Constants.VALUE]
        if update and self.protected_memory_total[Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_total"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_used(self, update=False, wait_for_completion=False):
        value = self.protected_memory_used[Constants.VALUE]
        if update and self.protected_memory_used[Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_used"], wait_for_completion=wait_for_completion)
        return value

    def get_protocol_supported(self, update=False, wait_for_completion=False):
        value = self.protocol_supported[Constants.VALUE]
        if update and self.protocol_supported[Constants.UPDATING] is False:
            self.update(data_points=["protocol_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_performance_state(self, update=False, wait_for_completion=False):
        value = self.performance_state[Constants.VALUE]
        if update and self.performance_state[Constants.UPDATING] is False:
            self.update(data_points=["performance_state"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_double_bit_ecc_errors_count(self, update=False, wait_for_completion=False):
        value = self.retired_pages_double_bit_ecc_errors_count[Constants.VALUE]
        if update and self.retired_pages_double_bit_ecc_errors_count[Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_double_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_single_bit_ecc_errors_count(self, update=False, wait_for_completion=False):
        value = self.retired_pages_single_bit_ecc_errors_count[Constants.VALUE]
        if update and self.retired_pages_single_bit_ecc_errors_count[Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_single_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_pending(self, update=False, wait_for_completion=False):
        value = self.retired_pages_pending[Constants.VALUE]
        if update and self.retired_pages_pending[Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_reserved_system_palette_entries(self, update=False, wait_for_completion=False):
        value = self.reserved_system_palette_entries[Constants.VALUE]
        if update and self.reserved_system_palette_entries[Constants.UPDATING] is False:
            self.update(data_points=["reserved_system_palette_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_reset_required(self, update=False, wait_for_completion=False):
        value = self.reset_required[Constants.VALUE]
        if update and self.reset_required[Constants.UPDATING] is False:
            self.update(data_points=["reset_required"], wait_for_completion=wait_for_completion)
        return value

    def get_reset_and_drain_recommended(self, update=False, wait_for_completion=False):
        value = self.reset_and_drain_recommended[Constants.VALUE]
        if update and self.reset_and_drain_recommended[Constants.UPDATING] is False:
            self.update(data_points=["reset_and_drain_recommended"], wait_for_completion=wait_for_completion)
        return value

    def get_serial(self, update=False, wait_for_completion=False):
        value = self.serial[Constants.VALUE]
        if update and self.serial[Constants.UPDATING] is False:
            self.update(data_points=["serial"], wait_for_completion=wait_for_completion)
        return value

    def get_specification_version(self, update=False, wait_for_completion=False):
        value = self.specification_version[Constants.VALUE]
        if update and self.specification_version[Constants.UPDATING] is False:
            self.update(data_points=["specification_version"], wait_for_completion=wait_for_completion)
        return value

    def get_status(self, update=False, wait_for_completion=False):
        value = self.status[Constants.VALUE]
        if update and self.status[Constants.UPDATING] is False:
            self.update(data_points=["status"], wait_for_completion=wait_for_completion)
        return value

    def get_status_info(self, update=False, wait_for_completion=False):
        value = self.status_info[Constants.VALUE]
        if update and self.status_info[Constants.UPDATING] is False:
            self.update(data_points=["status_info"], wait_for_completion=wait_for_completion)
        return value

    def get_system_creation_class_name(self, update=False, wait_for_completion=False):
        value = self.system_creation_class_name[Constants.VALUE]
        if update and self.system_creation_class_name[Constants.UPDATING] is False:
            self.update(data_points=["system_creation_class_name"], wait_for_completion=wait_for_completion)
        return value

    def get_system_name(self, update=False, wait_for_completion=False):
        value = self.system_name[Constants.VALUE]
        if update and self.system_name[Constants.UPDATING] is False:
            self.update(data_points=["system_name"], wait_for_completion=wait_for_completion)
        return value

    def get_system_palette_entries(self, update=False, wait_for_completion=False):
        value = self.system_palette_entries[Constants.VALUE]
        if update and self.system_palette_entries[Constants.UPDATING] is False:
            self.update(data_points=["system_palette_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_GPU_system_processor_mode_current(self, update=False, wait_for_completion=False):
        value = self.GPU_system_processor_mode_current[Constants.VALUE]
        if update and self.GPU_system_processor_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["GPU_system_processor_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_GPU_system_processor_mode_default(self, update=False, wait_for_completion=False):
        value = self.GPU_system_processor_mode_default[Constants.VALUE]
        if update and self.GPU_system_processor_mode_default[Constants.UPDATING] is False:
            self.update(data_points=["GPU_system_processor_mode_default"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_core(self, update=False, wait_for_completion=False):
        value = self.temperature_core[Constants.VALUE]
        if update and self.temperature_core[Constants.UPDATING] is False:
            self.update(data_points=["temperature_core"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_core_limit(self, update=False, wait_for_completion=False):
        value = self.temperature_core_limit[Constants.VALUE]
        if update and self.temperature_core_limit[Constants.UPDATING] is False:
            self.update(data_points=["temperature_core_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_memory(self, update=False, wait_for_completion=False):
        value = self.temperature_memory[Constants.VALUE]
        if update and self.temperature_memory[Constants.UPDATING] is False:
            self.update(data_points=["temperature_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_time_of_last_reset(self, update=False, wait_for_completion=False):
        value = self.time_of_last_reset[Constants.VALUE]
        if update and self.time_of_last_reset[Constants.UPDATING] is False:
            self.update(data_points=["time_of_last_reset"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_decoder(self, update=False, wait_for_completion=False):
        value = self.utilization_decoder[Constants.VALUE]
        if update and self.utilization_decoder[Constants.UPDATING] is False:
            self.update(data_points=["utilization_decoder"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_encoder(self, update=False, wait_for_completion=False):
        value = self.utilization_encoder[Constants.VALUE]
        if update and self.utilization_encoder[Constants.UPDATING] is False:
            self.update(data_points=["utilization_encoder"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_gpu(self, update=False, wait_for_completion=False):
        value = self.utilization_gpu[Constants.VALUE]
        if update and self.utilization_gpu[Constants.UPDATING] is False:
            self.update(data_points=["utilization_gpu"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_jpeg(self, update=False, wait_for_completion=False):
        value = self.utilization_jpeg[Constants.VALUE]
        if update and self.utilization_jpeg[Constants.UPDATING] is False:
            self.update(data_points=["utilization_jpeg"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_memory(self, update=False, wait_for_completion=False):
        value = self.utilization_memory[Constants.VALUE]
        if update and self.utilization_memory[Constants.UPDATING] is False:
            self.update(data_points=["utilization_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_optical_flow(self, update=False, wait_for_completion=False):
        value = self.utilization_optical_flow[Constants.VALUE]
        if update and self.utilization_optical_flow[Constants.UPDATING] is False:
            self.update(data_points=["utilization_optical_flow"], wait_for_completion=wait_for_completion)
        return value

    def get_uuid(self, update=False, wait_for_completion=False):
        value = self.uuid[Constants.VALUE]
        if update and self.uuid[Constants.UPDATING] is False:
            self.update(data_points=["uuid"], wait_for_completion=wait_for_completion)
        return value

    def get_vbios_version(self, update=False, wait_for_completion=False):
        value = self.vbios_version[Constants.VALUE]
        if update and self.vbios_version[Constants.UPDATING] is False:
            self.update(data_points=["vbios_version"], wait_for_completion=wait_for_completion)
        return value

    def get_video_architecture(self, update=False, wait_for_completion=False):
        value = self.video_architecture[Constants.VALUE]
        if update and self.video_architecture[Constants.UPDATING] is False:
            self.update(data_points=["video_architecture"], wait_for_completion=wait_for_completion)
        return value

    def get_video_memory_type(self, update=False, wait_for_completion=False):
        value = self.video_memory_type[Constants.VALUE]
        if update and self.video_memory_type[Constants.UPDATING] is False:
            self.update(data_points=["video_memory_type"], wait_for_completion=wait_for_completion)
        return value

    def get_video_mode(self, update=False, wait_for_completion=False):
        value = self.video_mode[Constants.VALUE]
        if update and self.video_mode[Constants.UPDATING] is False:
            self.update(data_points=["video_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_video_mode_description(self, update=False, wait_for_completion=False):
        value = self.video_mode_description[Constants.VALUE]
        if update and self.video_mode_description[Constants.UPDATING] is False:
            self.update(data_points=["video_mode_description"], wait_for_completion=wait_for_completion)
        return value

    def get_video_processor(self, update=False, wait_for_completion=False):
        value = self.video_processor[Constants.VALUE]
        if update and self.video_processor[Constants.UPDATING] is False:
            self.update(data_points=["video_processor"], wait_for_completion=wait_for_completion)
        return value

    def set_accelerator_capabilities(self, value=None):
        self.accelerator_capabilities[Constants.MANUALLY_SET] = value != None
        self.accelerator_capabilities = value

    def set_accounting_mode_enabled(self, value=None):
        self.accounting_mode_enabled[Constants.MANUALLY_SET] = value != None
        self.accounting_mode_enabled = value

    def set_accounting_mode_buffer_size(self, value=None):
        self.accounting_mode_buffer_size[Constants.MANUALLY_SET] = value != None
        self.accounting_mode_buffer_size = value

    def set_adapter_compatibility(self, value=None):
        self.adapter_compatibility[Constants.MANUALLY_SET] = value != None
        self.adapter_compatibility = value

    def set_adapter_DAC_type(self, value=None):
        self.adapter_DAC_type[Constants.MANUALLY_SET] = value != None
        self.adapter_DAC_type = value

    def set_adapter_id(self, value=None):
        self.adapter_id[Constants.MANUALLY_SET] = value != None
        self.adapter_id = value

    def set_adapter_index(self, value=None):
        self.adapter_index[Constants.MANUALLY_SET] = value != None
        self.adapter_index = value

    def set_addressing_mode(self, value=None):
        self.addressing_mode[Constants.MANUALLY_SET] = value != None
        self.addressing_mode = value

    def set_availability(self, value=None):
        self.availability[Constants.MANUALLY_SET] = value != None
        self.availability = value

    def set_capability_descriptions(self, value=None):
        self.capability_descriptions[Constants.MANUALLY_SET] = value != None
        self.capability_descriptions = value

    def set_caption(self, value=None):
        self.caption[Constants.MANUALLY_SET] = value != None
        self.caption = value

    def set_chip_to_chip_interconnect_mode(self, value=None):
        self.chip_to_chip_interconnect_mode[Constants.MANUALLY_SET] = value != None
        self.chip_to_chip_interconnect_mode = value

    def set_clock_event_reasons_as_bitmap(self, value=None):
        self.clock_event_reasons_as_bitmap[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_as_bitmap = value

    def set_clock_event_reasons_application_setting(self, value=None):
        self.clock_event_reasons_application_setting[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_application_setting = value

    def set_clock_event_reasons_is_hardware_limited(self, value=None):
        self.clock_event_reasons_is_hardware_limited[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_is_hardware_limited = value

    def set_clock_event_reasons_gpu_idle_limited(self, value=None):
        self.clock_event_reasons_gpu_idle_limited[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_gpu_idle_limited = value

    def set_clock_event_reasons_software_power_limited(self, value=None):
        self.clock_event_reasons_software_power_limited[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_software_power_limited = value

    def set_clock_event_reasons_software_thermal_limited(self, value=None):
        self.clock_event_reasons_software_thermal_limited[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_software_thermal_limited = value

    def set_clock_event_reasons_power_break_slowdown_limited(self, value=None):
        self.clock_event_reasons_power_break_slowdown_limited[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_power_break_slowdown_limited = value

    def set_clock_event_reasons_supported(self, value=None):
        self.clock_event_reasons_supported[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_supported = value

    def set_clock_event_reasons_sync_boost(self, value=None):
        self.clock_event_reasons_sync_boost[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_sync_boost = value

    def set_clock_event_reasons_thermal_limited(self, value=None):
        self.clock_event_reasons_thermal_limited[Constants.MANUALLY_SET] = value != None
        self.clock_event_reasons_thermal_limited = value

    def set_color_table_entries(self, value=None):
        self.color_table_entries[Constants.MANUALLY_SET] = value != None
        self.color_table_entries = value

    def set_compute_cap(self, value=None):
        self.compute_cap[Constants.MANUALLY_SET] = value != None
        self.compute_cap = value

    def set_compute_mode(self, value=None):
        self.compute_mode[Constants.MANUALLY_SET] = value != None
        self.compute_mode = value

    def set_config_manager_error_code(self, value=None):
        self.config_manager_error_code[Constants.MANUALLY_SET] = value != None
        self.config_manager_error_code = value

    def set_config_manager_user_config(self, value=None):
        self.config_manager_user_config[Constants.MANUALLY_SET] = value != None
        self.config_manager_user_config = value

    def set_core_voltage(self, value=None):
        self.core_voltage[Constants.MANUALLY_SET] = value != None
        self.core_voltage = value

    def set_core_voltage_range(self, value=None):
        self.core_voltage_range[Constants.MANUALLY_SET] = value != None
        self.core_voltage_range = value

    def set_creation_class_name(self, value=None):
        self.creation_class_name[Constants.MANUALLY_SET] = value != None
        self.creation_class_name = value

    def set_current_bits_per_pixel(self, value=None):
        self.current_bits_per_pixel[Constants.MANUALLY_SET] = value != None
        self.current_bits_per_pixel = value

    def set_current_horizontal_resolution(self, value=None):
        self.current_horizontal_resolution[Constants.MANUALLY_SET] = value != None
        self.current_horizontal_resolution = value

    def set_current_number_of_colors(self, value=None):
        self.current_number_of_colors[Constants.MANUALLY_SET] = value != None
        self.current_number_of_colors = value

    def set_current_number_of_columns(self, value=None):
        self.current_number_of_columns[Constants.MANUALLY_SET] = value != None
        self.current_number_of_columns = value

    def set_current_number_of_rows(self, value=None):
        self.current_number_of_rows[Constants.MANUALLY_SET] = value != None
        self.current_number_of_rows = value

    def set_current_refresh_rate(self, value=None):
        self.current_refresh_rate[Constants.MANUALLY_SET] = value != None
        self.current_refresh_rate = value

    def set_current_scan_mode(self, value=None):
        self.current_scan_mode[Constants.MANUALLY_SET] = value != None
        self.current_scan_mode = value

    def set_current_vertical_resolution(self, value=None):
        self.current_vertical_resolution[Constants.MANUALLY_SET] = value != None
        self.current_vertical_resolution = value

    def set_description(self, value=None):
        self.description[Constants.MANUALLY_SET] = value != None
        self.description = value

    def set_device_id(self, value=None):
        self.device_id[Constants.MANUALLY_SET] = value != None
        self.device_id = value

    def set_device_specific_pens(self, value=None):
        self.device_specific_pens[Constants.MANUALLY_SET] = value != None
        self.device_specific_pens = value

    def set_display_active(self, value=None):
        self.display_active[Constants.MANUALLY_SET] = value != None
        self.display_active = value

    def set_display_mode(self, value=None):
        self.display_mode[Constants.MANUALLY_SET] = value != None
        self.display_mode = value

    def set_dither_type(self, value=None):
        self.dither_type[Constants.MANUALLY_SET] = value != None
        self.dither_type = value

    def set_driver_date(self, value=None):
        self.driver_date[Constants.MANUALLY_SET] = value != None
        self.driver_date = value

    def set_driver_model_current(self, value=None):
        self.driver_model_current[Constants.MANUALLY_SET] = value != None
        self.driver_model_current = value

    def set_driver_model_pending(self, value=None):
        self.driver_model_pending[Constants.MANUALLY_SET] = value != None
        self.driver_model_pending = value

    def set_driver_version(self, value=None):
        self.driver_version[Constants.MANUALLY_SET] = value != None
        self.driver_version = value

    def set_ecc_errors_corrected_all_time_in_cbu(self, value=None):
        self.ecc_errors_corrected_all_time_in_cbu[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_cbu = value

    def set_ecc_errors_corrected_all_time_in_primary_cache(self, value=None):
        self.ecc_errors_corrected_all_time_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_primary_cache = value

    def set_ecc_errors_corrected_all_time_in_register_file(self, value=None):
        self.ecc_errors_corrected_all_time_in_register_file[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_register_file = value

    def set_ecc_errors_corrected_all_time_in_secondary_cache(self, value=None):
        self.ecc_errors_corrected_all_time_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_secondary_cache = value

    def set_ecc_errors_corrected_all_time_in_shared_memory(self, value=None):
        self.ecc_errors_corrected_all_time_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_shared_memory = value

    def set_ecc_errors_corrected_all_time_in_sram(self, value=None):
        self.ecc_errors_corrected_all_time_in_sram[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_sram = value

    def set_ecc_errors_corrected_all_time_in_texture_memory(self, value=None):
        self.ecc_errors_corrected_all_time_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_texture_memory = value

    def set_ecc_errors_corrected_all_time_in_total(self, value=None):
        self.ecc_errors_corrected_all_time_in_total[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_total = value

    def set_ecc_errors_corrected_all_time_in_video_memory(self, value=None):
        self.ecc_errors_corrected_all_time_in_video_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_all_time_in_video_memory = value

    def set_ecc_errors_corrected_since_reboot_in_cbu(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_cbu[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_cbu = value

    def set_ecc_errors_corrected_since_reboot_in_primary_cache(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_register_file(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_register_file[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_register_file = value

    def set_ecc_errors_corrected_since_reboot_in_secondary_cache(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_shared_memory(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_corrected_since_reboot_in_sram(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_sram[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_sram = value

    def set_ecc_errors_corrected_since_reboot_in_texture_memory(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_corrected_since_reboot_in_total(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_total[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_total = value

    def set_ecc_errors_corrected_since_reboot_in_video_memory(self, value=None):
        self.ecc_errors_corrected_since_reboot_in_video_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_corrected_since_reboot_in_video_memory = value

    def set_ecc_errors_uncorrected_all_time_in_cbu(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_cbu[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_cbu = value

    def set_ecc_errors_uncorrected_all_time_in_primary_cache(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_primary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_register_file(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_register_file[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_register_file = value

    def set_ecc_errors_uncorrected_all_time_in_secondary_cache(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_secondary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_shared_memory(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_shared_memory = value

    def set_ecc_errors_uncorrected_all_time_in_sram(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_sram[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_sram = value

    def set_ecc_errors_uncorrected_all_time_in_texture_memory(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_texture_memory = value

    def set_ecc_errors_uncorrected_all_time_in_total(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_total[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_total = value

    def set_ecc_errors_uncorrected_all_time_in_video_memory(self, value=None):
        self.ecc_errors_uncorrected_all_time_in_video_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_all_time_in_video_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_cbu(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_cbu[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_cbu = value

    def set_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_register_file(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_register_file[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_register_file = value

    def set_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_sram(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_sram[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_sram = value

    def set_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_total(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_total[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_total = value

    def set_ecc_errors_uncorrected_since_reboot_in_video_memory(self, value=None):
        self.ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.MANUALLY_SET] = value != None
        self.ecc_errors_uncorrected_since_reboot_in_video_memory = value

    def set_ecc_mode_current(self, value=None):
        self.ecc_mode_current[Constants.MANUALLY_SET] = value != None
        self.ecc_mode_current = value

    def set_ecc_mode_pending(self, value=None):
        self.ecc_mode_pending[Constants.MANUALLY_SET] = value != None
        self.ecc_mode_pending = value

    def set_encoder_average_FPS(self, value=None):
        self.encoder_average_FPS[Constants.MANUALLY_SET] = value != None
        self.encoder_average_FPS = value

    def set_encoder_average_latency(self, value=None):
        self.encoder_average_latency[Constants.MANUALLY_SET] = value != None
        self.encoder_average_latency = value

    def set_encoder_session_count(self, value=None):
        self.encoder_session_count[Constants.MANUALLY_SET] = value != None
        self.encoder_session_count = value

    def set_engine_clock_range(self, value=None):
        self.engine_clock_range[Constants.MANUALLY_SET] = value != None
        self.engine_clock_range = value

    def set_error_cleared(self, value=None):
        self.error_cleared[Constants.MANUALLY_SET] = value != None
        self.error_cleared = value

    def set_error_description(self, value=None):
        self.error_description[Constants.MANUALLY_SET] = value != None
        self.error_description = value

    def set_fabric_state(self, value=None):
        self.fabric_state[Constants.MANUALLY_SET] = value != None
        self.fabric_state = value

    def set_fabric_status(self, value=None):
        self.fabric_status[Constants.MANUALLY_SET] = value != None
        self.fabric_status = value

    def set_fan_speed_percentage(self, value=None):
        self.fan_speed_percentage[Constants.MANUALLY_SET] = value != None
        self.fan_speed_percentage = value

    def set_fan_speed_percentage_range(self, value=None):
        self.fan_speed_percentage_range[Constants.MANUALLY_SET] = value != None
        self.fan_speed_percentage_range = value

    def set_fan_speed_RPM(self, value=None):
        self.fan_speed_RPM[Constants.MANUALLY_SET] = value != None
        self.fan_speed_RPM = value

    def set_fan_speed_RPM_range(self, value=None):
        self.fan_speed_RPM_range[Constants.MANUALLY_SET] = value != None
        self.fan_speed_RPM_range = value

    def set_fractional_multi_vGPU(self, value=None):
        self.fractional_multi_vGPU[Constants.MANUALLY_SET] = value != None
        self.fractional_multi_vGPU = value

    def set_frequency_application_default_shader_clock(self, value=None):
        self.frequency_application_default_shader_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_application_default_shader_clock = value

    def set_frequency_application_default_memory_clock(self, value=None):
        self.frequency_application_default_memory_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_application_default_memory_clock = value

    def set_frequency_application_memory_clock(self, value=None):
        self.frequency_application_memory_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_application_memory_clock = value

    def set_frequency_application_shader_clock(self, value=None):
        self.frequency_application_shader_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_application_shader_clock = value

    def set_frequency_maximum_memory_clock(self, value=None):
        self.frequency_maximum_memory_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_maximum_memory_clock = value

    def set_frequency_maximum_shader_clock(self, value=None):
        self.frequency_maximum_shader_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_maximum_shader_clock = value

    def set_frequency_maximum_streaming_multiprocessor_clock(self, value=None):
        self.frequency_maximum_streaming_multiprocessor_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_maximum_streaming_multiprocessor_clock = value

    def set_frequency_memory_clock(self, value=None):
        self.frequency_memory_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_memory_clock = value

    def set_frequency_shader_clock(self, value=None):
        self.frequency_shader_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_shader_clock = value

    def set_frequency_streaming_multiprocessor_clock(self, value=None):
        self.frequency_streaming_multiprocessor_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_streaming_multiprocessor_clock = value

    def set_frequency_video_clock(self, value=None):
        self.frequency_video_clock[Constants.MANUALLY_SET] = value != None
        self.frequency_video_clock = value

    def set_heterogenous_multi_vGPU(self, value=None):
        self.heterogenous_multi_vGPU[Constants.MANUALLY_SET] = value != None
        self.heterogenous_multi_vGPU = value

    def set_heterogenous_time_slice_profile(self, value=None):
        self.heterogenous_time_slice_profile[Constants.MANUALLY_SET] = value != None
        self.heterogenous_time_slice_profile = value

    def set_heterogenous_time_slice_sizes(self, value=None):
        self.heterogenous_time_slice_sizes[Constants.MANUALLY_SET] = value != None
        self.heterogenous_time_slice_sizes = value

    def set_ICM_indent(self, value=None):
        self.ICM_indent[Constants.MANUALLY_SET] = value != None
        self.ICM_indent = value

    def set_ICM_method(self, value=None):
        self.ICM_method[Constants.MANUALLY_SET] = value != None
        self.ICM_method = value

    def set_inf_filename(self, value=None):
        self.inf_filename[Constants.MANUALLY_SET] = value != None
        self.inf_filename = value

    def set_inf_section(self, value=None):
        self.inf_section[Constants.MANUALLY_SET] = value != None
        self.inf_section = value

    def set_info_ROM_ecc(self, value=None):
        self.info_ROM_ecc[Constants.MANUALLY_SET] = value != None
        self.info_ROM_ecc = value

    def set_info_ROM_oem(self, value=None):
        self.info_ROM_oem[Constants.MANUALLY_SET] = value != None
        self.info_ROM_oem = value

    def set_info_ROM_power(self, value=None):
        self.info_ROM_power[Constants.MANUALLY_SET] = value != None
        self.info_ROM_power = value

    def set_info_ROM_version(self, value=None):
        self.info_ROM_version[Constants.MANUALLY_SET] = value != None
        self.info_ROM_version = value

    def set_install_date(self, value=None):
        self.install_date[Constants.MANUALLY_SET] = value != None
        self.install_date = value

    def set_installed_display_drivers(self, value=None):
        self.installed_display_drivers[Constants.MANUALLY_SET] = value != None
        self.installed_display_drivers = value

    def set_last_error_code(self, value=None):
        self.last_error_code[Constants.MANUALLY_SET] = value != None
        self.last_error_code = value

    def set_max_memory_supported(self, value=None):
        self.max_memory_supported[Constants.MANUALLY_SET] = value != None
        self.max_memory_supported = value

    def set_max_number_controlled(self, value=None):
        self.max_number_controlled[Constants.MANUALLY_SET] = value != None
        self.max_number_controlled = value

    def set_max_refresh_rate(self, value=None):
        self.max_refresh_rate[Constants.MANUALLY_SET] = value != None
        self.max_refresh_rate = value

    def set_memory_clock_range(self, value=None):
        self.memory_clock_range[Constants.MANUALLY_SET] = value != None
        self.memory_clock_range = value

    def set_memory_free(self, value=None):
        self.memory_free[Constants.MANUALLY_SET] = value != None
        self.memory_free = value

    def set_memory_reserved(self, value=None):
        self.memory_reserved[Constants.MANUALLY_SET] = value != None
        self.memory_reserved = value

    def set_memory_total(self, value=None):
        self.memory_total[Constants.MANUALLY_SET] = value != None
        self.memory_total = value

    def set_memory_used(self, value=None):
        self.memory_used[Constants.MANUALLY_SET] = value != None
        self.memory_used = value

    def set_min_refresh_rate(self, value=None):
        self.min_refresh_rate[Constants.MANUALLY_SET] = value != None
        self.min_refresh_rate = value

    def set_monochrome(self, value=None):
        self.monochrome[Constants.MANUALLY_SET] = value != None
        self.monochrome = value

    def set_multi_instance_GPU_mode_current(self, value=None):
        self.multi_instance_GPU_mode_current[Constants.MANUALLY_SET] = value != None
        self.multi_instance_GPU_mode_current = value

    def set_multi_instance_GPU_mode_pending(self, value=None):
        self.multi_instance_GPU_mode_pending[Constants.MANUALLY_SET] = value != None
        self.multi_instance_GPU_mode_pending = value

    def set_name(self, value=None):
        self.name[Constants.MANUALLY_SET] = value != None
        self.name = value

    def set_number_of_color_planes(self, value=None):
        self.number_of_color_planes[Constants.MANUALLY_SET] = value != None
        self.number_of_color_planes = value

    def set_number_of_video_pages(self, value=None):
        self.number_of_video_pages[Constants.MANUALLY_SET] = value != None
        self.number_of_video_pages = value

    def set_operating_mode_current(self, value=None):
        self.operating_mode_current[Constants.MANUALLY_SET] = value != None
        self.operating_mode_current = value

    def set_operating_mode_pending(self, value=None):
        self.operating_mode_pending[Constants.MANUALLY_SET] = value != None
        self.operating_mode_pending = value

    def set_pci_bus(self, value=None):
        self.pci_bus[Constants.MANUALLY_SET] = value != None
        self.pci_bus = value

    def set_pci_bus_id(self, value=None):
        self.pci_bus_id[Constants.MANUALLY_SET] = value != None
        self.pci_bus_id = value

    def set_pci_device(self, value=None):
        self.pci_device[Constants.MANUALLY_SET] = value != None
        self.pci_device = value

    def set_pci_device_id(self, value=None):
        self.pci_device_id[Constants.MANUALLY_SET] = value != None
        self.pci_device_id = value

    def set_pci_domain(self, value=None):
        self.pci_domain[Constants.MANUALLY_SET] = value != None
        self.pci_domain = value

    def set_pci_link_generation_current(self, value=None):
        self.pci_link_generation_current[Constants.MANUALLY_SET] = value != None
        self.pci_link_generation_current = value

    def set_pci_link_generation_device_host_maximum(self, value=None):
        self.pci_link_generation_device_host_maximum[Constants.MANUALLY_SET] = value != None
        self.pci_link_generation_device_host_maximum = value

    def set_pci_link_generation_gpu_maximum(self, value=None):
        self.pci_link_generation_gpu_maximum[Constants.MANUALLY_SET] = value != None
        self.pci_link_generation_gpu_maximum = value

    def set_pci_link_generation_maximum(self, value=None):
        self.pci_link_generation_maximum[Constants.MANUALLY_SET] = value != None
        self.pci_link_generation_maximum = value

    def set_pci_link_width_current(self, value=None):
        self.pci_link_width_current[Constants.MANUALLY_SET] = value != None
        self.pci_link_width_current = value

    def set_pci_link_width_maximum(self, value=None):
        self.pci_link_width_maximum[Constants.MANUALLY_SET] = value != None
        self.pci_link_width_maximum = value

    def set_pci_sub_device_id(self, value=None):
        self.pci_sub_device_id[Constants.MANUALLY_SET] = value != None
        self.pci_sub_device_id = value

    def set_persistence_mode(self, value=None):
        self.persistence_mode[Constants.MANUALLY_SET] = value != None
        self.persistence_mode = value

    def set_PNP_device_id(self, value=None):
        self.PNP_device_id[Constants.MANUALLY_SET] = value != None
        self.PNP_device_id = value

    def set_power_draw(self, value=None):
        self.power_draw[Constants.MANUALLY_SET] = value != None
        self.power_draw = value

    def set_power_draw_average(self, value=None):
        self.power_draw_average[Constants.MANUALLY_SET] = value != None
        self.power_draw_average = value

    def set_power_draw_default_limit(self, value=None):
        self.power_draw_default_limit[Constants.MANUALLY_SET] = value != None
        self.power_draw_default_limit = value

    def set_power_draw_enforced_limit(self, value=None):
        self.power_draw_enforced_limit[Constants.MANUALLY_SET] = value != None
        self.power_draw_enforced_limit = value

    def set_power_draw_instant(self, value=None):
        self.power_draw_instant[Constants.MANUALLY_SET] = value != None
        self.power_draw_instant = value

    def set_power_draw_limit(self, value=None):
        self.power_draw_limit[Constants.MANUALLY_SET] = value != None
        self.power_draw_limit = value

    def set_power_draw_maximum(self, value=None):
        self.power_draw_maximum[Constants.MANUALLY_SET] = value != None
        self.power_draw_maximum = value

    def set_power_draw_minimum(self, value=None):
        self.power_draw_minimum[Constants.MANUALLY_SET] = value != None
        self.power_draw_minimum = value

    def set_power_management_capabilities(self, value=None):
        self.power_management_capabilities[Constants.MANUALLY_SET] = value != None
        self.power_management_capabilities = value

    def set_power_management_supported(self, value=None):
        self.power_management_supported[Constants.MANUALLY_SET] = value != None
        self.power_management_supported = value

    def set_protected_memory_free(self, value=None):
        self.protected_memory_free[Constants.MANUALLY_SET] = value != None
        self.protected_memory_free = value

    def set_protected_memory_total(self, value=None):
        self.protected_memory_total[Constants.MANUALLY_SET] = value != None
        self.protected_memory_total = value

    def set_protected_memory_used(self, value=None):
        self.protected_memory_used[Constants.MANUALLY_SET] = value != None
        self.protected_memory_used = value

    def set_protocol_supported(self, value=None):
        self.protocol_supported[Constants.MANUALLY_SET] = value != None
        self.protocol_supported = value

    def set_performance_state(self, value=None):
        self.performance_state[Constants.MANUALLY_SET] = value != None
        self.performance_state = value

    def set_retired_pages_double_bit_ecc_errors_count(self, value=None):
        self.retired_pages_double_bit_ecc_errors_count[Constants.MANUALLY_SET] = value != None
        self.retired_pages_double_bit_ecc_errors_count = value

    def set_retired_pages_single_bit_ecc_errors_count(self, value=None):
        self.retired_pages_single_bit_ecc_errors_count[Constants.MANUALLY_SET] = value != None
        self.retired_pages_single_bit_ecc_errors_count = value

    def set_retired_pages_pending(self, value=None):
        self.retired_pages_pending[Constants.MANUALLY_SET] = value != None
        self.retired_pages_pending = value

    def set_reserved_system_palette_entries(self, value=None):
        self.reserved_system_palette_entries[Constants.MANUALLY_SET] = value != None
        self.reserved_system_palette_entries = value

    def set_reset_required(self, value=None):
        self.reset_required[Constants.MANUALLY_SET] = value != None
        self.reset_required = value

    def set_reset_and_drain_recommended(self, value=None):
        self.reset_and_drain_recommended[Constants.MANUALLY_SET] = value != None
        self.reset_and_drain_recommended = value

    def set_serial(self, value=None):
        self.serial[Constants.MANUALLY_SET] = value != None
        self.serial = value

    def set_specification_version(self, value=None):
        self.specification_version[Constants.MANUALLY_SET] = value != None
        self.specification_version = value

    def set_status(self, value=None):
        self.status[Constants.MANUALLY_SET] = value != None
        self.status = value

    def set_status_info(self, value=None):
        self.status_info[Constants.MANUALLY_SET] = value != None
        self.status_info = value

    def set_system_creation_class_name(self, value=None):
        self.system_creation_class_name[Constants.MANUALLY_SET] = value != None
        self.system_creation_class_name = value

    def set_system_name(self, value=None):
        self.system_name[Constants.MANUALLY_SET] = value != None
        self.system_name = value

    def set_system_palette_entries(self, value=None):
        self.system_palette_entries[Constants.MANUALLY_SET] = value != None
        self.system_palette_entries = value

    def set_GPU_system_processor_mode_current(self, value=None):
        self.GPU_system_processor_mode_current[Constants.MANUALLY_SET] = value != None
        self.GPU_system_processor_mode_current = value

    def set_GPU_system_processor_mode_default(self, value=None):
        self.GPU_system_processor_mode_default[Constants.MANUALLY_SET] = value != None
        self.GPU_system_processor_mode_default = value

    def set_temperature_core(self, value=None):
        self.temperature_core[Constants.MANUALLY_SET] = value != None
        self.temperature_core = value

    def set_temperature_core_limit(self, value=None):
        self.temperature_core_limit[Constants.MANUALLY_SET] = value != None
        self.temperature_core_limit = value

    def set_temperature_memory(self, value=None):
        self.temperature_memory[Constants.MANUALLY_SET] = value != None
        self.temperature_memory = value

    def set_time_of_last_reset(self, value=None):
        self.time_of_last_reset[Constants.MANUALLY_SET] = value != None
        self.time_of_last_reset = value

    def set_utilization_decoder(self, value=None):
        self.utilization_decoder[Constants.MANUALLY_SET] = value != None
        self.utilization_decoder = value

    def set_utilization_encoder(self, value=None):
        self.utilization_encoder[Constants.MANUALLY_SET] = value != None
        self.utilization_encoder = value

    def set_utilization_gpu(self, value=None):
        self.utilization_gpu[Constants.MANUALLY_SET] = value != None
        self.utilization_gpu = value

    def set_utilization_jpeg(self, value=None):
        self.utilization_jpeg[Constants.MANUALLY_SET] = value != None
        self.utilization_jpeg = value

    def set_utilization_memory(self, value=None):
        self.utilization_memory[Constants.MANUALLY_SET] = value != None
        self.utilization_memory = value

    def set_utilization_optical_flow(self, value=None):
        self.utilization_optical_flow[Constants.MANUALLY_SET] = value != None
        self.utilization_optical_flow = value

    def set_uuid(self, value=None):
        self.uuid[Constants.MANUALLY_SET] = value != None
        self.uuid = value

    def set_vbios_version(self, value=None):
        self.vbios_version[Constants.MANUALLY_SET] = value != None
        self.vbios_version = value

    def set_video_architecture(self, value=None):
        self.video_architecture[Constants.MANUALLY_SET] = value != None
        self.video_architecture = value

    def set_video_memory_type(self, value=None):
        self.video_memory_type[Constants.MANUALLY_SET] = value != None
        self.video_memory_type = value

    def set_video_mode(self, value=None):
        self.video_mode[Constants.MANUALLY_SET] = value != None
        self.video_mode = value

    def set_video_mode_description(self, value=None):
        self.video_mode_description[Constants.MANUALLY_SET] = value != None
        self.video_mode_description = value

    def set_video_processor(self, value=None):
        self.video_processor[Constants.MANUALLY_SET] = value != None
        self.video_processor = value

    def update_accelerator_capabilities(self, wait_for_completion=True):
        self.accelerator_capabilities[Constants.UPDATING] = True
        self.update(data_points=["accelerator_capabilities"], wait_for_completion=wait_for_completion)

    def update_accounting_mode_enabled(self, wait_for_completion=True):
        self.accounting_mode_enabled[Constants.UPDATING] = True
        self.update(data_points=["accounting_mode_enabled"], wait_for_completion=wait_for_completion)

    def update_accounting_mode_buffer_size(self, wait_for_completion=True):
        self.accounting_mode_buffer_size[Constants.UPDATING] = True
        self.update(data_points=["accounting_mode_buffer_size"], wait_for_completion=wait_for_completion)

    def update_adapter_compatibility(self, wait_for_completion=True):
        self.adapter_compatibility[Constants.UPDATING] = True
        self.update(data_points=["adapter_compatibility"], wait_for_completion=wait_for_completion)

    def update_adapter_DAC_type(self, wait_for_completion=True):
        self.adapter_DAC_type[Constants.UPDATING] = True
        self.update(data_points=["adapter_DAC_type"], wait_for_completion=wait_for_completion)

    def update_adapter_id(self, wait_for_completion=True):
        self.adapter_id[Constants.UPDATING] = True
        self.update(data_points=["adapter_id"], wait_for_completion=wait_for_completion)

    def update_adapter_index(self, wait_for_completion=True):
        self.adapter_index[Constants.UPDATING] = True
        self.update(data_points=["adapter_index"], wait_for_completion=wait_for_completion)

    def update_addressing_mode(self, wait_for_completion=True):
        self.addressing_mode[Constants.UPDATING] = True
        self.update(data_points=["addressing_mode"], wait_for_completion=wait_for_completion)

    def update_availability(self, wait_for_completion=True):
        self.availability[Constants.UPDATING] = True
        self.update(data_points=["availability"], wait_for_completion=wait_for_completion)

    def update_capability_descriptions(self, wait_for_completion=True):
        self.capability_descriptions[Constants.UPDATING] = True
        self.update(data_points=["capability_descriptions"], wait_for_completion=wait_for_completion)

    def update_caption(self, wait_for_completion=True):
        self.caption[Constants.UPDATING] = True
        self.update(data_points=["caption"], wait_for_completion=wait_for_completion)

    def update_chip_to_chip_interconnect_mode(self, wait_for_completion=True):
        self.chip_to_chip_interconnect_mode[Constants.UPDATING] = True
        self.update(data_points=["chip_to_chip_interconnect_mode"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_as_bitmap(self, wait_for_completion=True):
        self.clock_event_reasons_as_bitmap[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_as_bitmap"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_application_updateting(self, wait_for_completion=True):
        self.clock_event_reasons_application_updateting[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_application_updateting"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_is_hardware_limited(self, wait_for_completion=True):
        self.clock_event_reasons_is_hardware_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_is_hardware_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_gpu_idle_limited(self, wait_for_completion=True):
        self.clock_event_reasons_gpu_idle_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_gpu_idle_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_software_power_limited(self, wait_for_completion=True):
        self.clock_event_reasons_software_power_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_software_power_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_software_thermal_limited(self, wait_for_completion=True):
        self.clock_event_reasons_software_thermal_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_software_thermal_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_power_break_slowdown_limited(self, wait_for_completion=True):
        self.clock_event_reasons_power_break_slowdown_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_power_break_slowdown_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_supported(self, wait_for_completion=True):
        self.clock_event_reasons_supported[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_supported"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_sync_boost(self, wait_for_completion=True):
        self.clock_event_reasons_sync_boost[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_sync_boost"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_thermal_limited(self, wait_for_completion=True):
        self.clock_event_reasons_thermal_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_thermal_limited"], wait_for_completion=wait_for_completion)

    def update_color_table_entries(self, wait_for_completion=True):
        self.color_table_entries[Constants.UPDATING] = True
        self.update(data_points=["color_table_entries"], wait_for_completion=wait_for_completion)

    def update_compute_cap(self, wait_for_completion=True):
        self.compute_cap[Constants.UPDATING] = True
        self.update(data_points=["compute_cap"], wait_for_completion=wait_for_completion)

    def update_compute_mode(self, wait_for_completion=True):
        self.compute_mode[Constants.UPDATING] = True
        self.update(data_points=["compute_mode"], wait_for_completion=wait_for_completion)

    def update_config_manager_error_code(self, wait_for_completion=True):
        self.config_manager_error_code[Constants.UPDATING] = True
        self.update(data_points=["config_manager_error_code"], wait_for_completion=wait_for_completion)

    def update_config_manager_user_config(self, wait_for_completion=True):
        self.config_manager_user_config[Constants.UPDATING] = True
        self.update(data_points=["config_manager_user_config"], wait_for_completion=wait_for_completion)

    def update_core_voltage(self, wait_for_completion=True):
        self.core_voltage[Constants.UPDATING] = True
        self.update(data_points=["core_voltage"], wait_for_completion=wait_for_completion)

    def update_core_voltage_range(self, wait_for_completion=True):
        self.core_voltage_range[Constants.UPDATING] = True
        self.update(data_points=["core_voltage_range"], wait_for_completion=wait_for_completion)

    def update_creation_class_name(self, wait_for_completion=True):
        self.creation_class_name[Constants.UPDATING] = True
        self.update(data_points=["creation_class_name"], wait_for_completion=wait_for_completion)

    def update_current_bits_per_pixel(self, wait_for_completion=True):
        self.current_bits_per_pixel[Constants.UPDATING] = True
        self.update(data_points=["current_bits_per_pixel"], wait_for_completion=wait_for_completion)

    def update_current_horizontal_resolution(self, wait_for_completion=True):
        self.current_horizontal_resolution[Constants.UPDATING] = True
        self.update(data_points=["current_horizontal_resolution"], wait_for_completion=wait_for_completion)

    def update_current_number_of_colors(self, wait_for_completion=True):
        self.current_number_of_colors[Constants.UPDATING] = True
        self.update(data_points=["current_number_of_colors"], wait_for_completion=wait_for_completion)

    def update_current_number_of_columns(self, wait_for_completion=True):
        self.current_number_of_columns[Constants.UPDATING] = True
        self.update(data_points=["current_number_of_columns"], wait_for_completion=wait_for_completion)

    def update_current_number_of_rows(self, wait_for_completion=True):
        self.current_number_of_rows[Constants.UPDATING] = True
        self.update(data_points=["current_number_of_rows"], wait_for_completion=wait_for_completion)

    def update_current_refresh_rate(self, wait_for_completion=True):
        self.current_refresh_rate[Constants.UPDATING] = True
        self.update(data_points=["current_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_current_scan_mode(self, wait_for_completion=True):
        self.current_scan_mode[Constants.UPDATING] = True
        self.update(data_points=["current_scan_mode"], wait_for_completion=wait_for_completion)

    def update_current_vertical_resolution(self, wait_for_completion=True):
        self.current_vertical_resolution[Constants.UPDATING] = True
        self.update(data_points=["current_vertical_resolution"], wait_for_completion=wait_for_completion)

    def update_description(self, wait_for_completion=True):
        self.description[Constants.UPDATING] = True
        self.update(data_points=["description"], wait_for_completion=wait_for_completion)

    def update_device_id(self, wait_for_completion=True):
        self.device_id[Constants.UPDATING] = True
        self.update(data_points=["device_id"], wait_for_completion=wait_for_completion)

    def update_device_specific_pens(self, wait_for_completion=True):
        self.device_specific_pens[Constants.UPDATING] = True
        self.update(data_points=["device_specific_pens"], wait_for_completion=wait_for_completion)

    def update_display_active(self, wait_for_completion=True):
        self.display_active[Constants.UPDATING] = True
        self.update(data_points=["display_active"], wait_for_completion=wait_for_completion)

    def update_display_mode(self, wait_for_completion=True):
        self.display_mode[Constants.UPDATING] = True
        self.update(data_points=["display_mode"], wait_for_completion=wait_for_completion)

    def update_dither_type(self, wait_for_completion=True):
        self.dither_type[Constants.UPDATING] = True
        self.update(data_points=["dither_type"], wait_for_completion=wait_for_completion)

    def update_driver_date(self, wait_for_completion=True):
        self.driver_date[Constants.UPDATING] = True
        self.update(data_points=["driver_date"], wait_for_completion=wait_for_completion)

    def update_driver_model_current(self, wait_for_completion=True):
        self.driver_model_current[Constants.UPDATING] = True
        self.update(data_points=["driver_model_current"], wait_for_completion=wait_for_completion)

    def update_driver_model_pending(self, wait_for_completion=True):
        self.driver_model_pending[Constants.UPDATING] = True
        self.update(data_points=["driver_model_pending"], wait_for_completion=wait_for_completion)

    def update_driver_version(self, wait_for_completion=True):
        self.driver_version[Constants.UPDATING] = True
        self.update(data_points=["driver_version"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_cbu(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_primary_cache(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_register_file(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_secondary_cache(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_shared_memory(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_sram(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_texture_memory(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_total(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_video_memory(self, wait_for_completion=True):
        self.ecc_errors_corrected_all_time_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_cbu(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_primary_cache(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_register_file(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_secondary_cache(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_shared_memory(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_sram(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_texture_memory(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_total(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_video_memory(self, wait_for_completion=True):
        self.ecc_errors_corrected_since_reboot_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_cbu(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_primary_cache(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_register_file(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_secondary_cache(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_shared_memory(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_sram(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_texture_memory(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_total(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_video_memory(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_all_time_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_cbu(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_register_file(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_sram(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_total(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_video_memory(self, wait_for_completion=True):
        self.ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_mode_current(self, wait_for_completion=True):
        self.ecc_mode_current[Constants.UPDATING] = True
        self.update(data_points=["ecc_mode_current"], wait_for_completion=wait_for_completion)

    def update_ecc_mode_pending(self, wait_for_completion=True):
        self.ecc_mode_pending[Constants.UPDATING] = True
        self.update(data_points=["ecc_mode_pending"], wait_for_completion=wait_for_completion)

    def update_encoder_average_FPS(self, wait_for_completion=True):
        self.encoder_average_FPS[Constants.UPDATING] = True
        self.update(data_points=["encoder_average_FPS"], wait_for_completion=wait_for_completion)

    def update_encoder_average_latency(self, wait_for_completion=True):
        self.encoder_average_latency[Constants.UPDATING] = True
        self.update(data_points=["encoder_average_latency"], wait_for_completion=wait_for_completion)

    def update_encoder_session_count(self, wait_for_completion=True):
        self.encoder_session_count[Constants.UPDATING] = True
        self.update(data_points=["encoder_session_count"], wait_for_completion=wait_for_completion)

    def update_engine_clock_range(self, wait_for_completion=True):
        self.engine_clock_range[Constants.UPDATING] = True
        self.update(data_points=["engine_clock_range"], wait_for_completion=wait_for_completion)

    def update_error_cleared(self, wait_for_completion=True):
        self.error_cleared[Constants.UPDATING] = True
        self.update(data_points=["error_cleared"], wait_for_completion=wait_for_completion)

    def update_error_description(self, wait_for_completion=True):
        self.error_description[Constants.UPDATING] = True
        self.update(data_points=["error_description"], wait_for_completion=wait_for_completion)

    def update_fabric_state(self, wait_for_completion=True):
        self.fabric_state[Constants.UPDATING] = True
        self.update(data_points=["fabric_state"], wait_for_completion=wait_for_completion)

    def update_fabric_status(self, wait_for_completion=True):
        self.fabric_status[Constants.UPDATING] = True
        self.update(data_points=["fabric_status"], wait_for_completion=wait_for_completion)

    def update_fan_speed_percentage(self, wait_for_completion=True):
        self.fan_speed_percentage[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_percentage"], wait_for_completion=wait_for_completion)

    def update_fan_speed_percentage_range(self, wait_for_completion=True):
        self.fan_speed_percentage_range[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_percentage_range"], wait_for_completion=wait_for_completion)

    def update_fan_speed_RPM(self, wait_for_completion=True):
        self.fan_speed_RPM[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_RPM"], wait_for_completion=wait_for_completion)

    def update_fan_speed_RPM_range(self, wait_for_completion=True):
        self.fan_speed_RPM_range[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_RPM_range"], wait_for_completion=wait_for_completion)

    def update_fractional_multi_vGPU(self, wait_for_completion=True):
        self.fractional_multi_vGPU[Constants.UPDATING] = True
        self.update(data_points=["fractional_multi_vGPU"], wait_for_completion=wait_for_completion)

    def update_frequency_application_default_shader_clock(self, wait_for_completion=True):
        self.frequency_application_default_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_default_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_default_memory_clock(self, wait_for_completion=True):
        self.frequency_application_default_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_default_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_memory_clock(self, wait_for_completion=True):
        self.frequency_application_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_shader_clock(self, wait_for_completion=True):
        self.frequency_application_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_memory_clock(self, wait_for_completion=True):
        self.frequency_maximum_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_shader_clock(self, wait_for_completion=True):
        self.frequency_maximum_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_streaming_multiprocessor_clock(self, wait_for_completion=True):
        self.frequency_maximum_streaming_multiprocessor_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_memory_clock(self, wait_for_completion=True):
        self.frequency_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_shader_clock(self, wait_for_completion=True):
        self.frequency_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_streaming_multiprocessor_clock(self, wait_for_completion=True):
        self.frequency_streaming_multiprocessor_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_video_clock(self, wait_for_completion=True):
        self.frequency_video_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_video_clock"], wait_for_completion=wait_for_completion)

    def update_heterogenous_multi_vGPU(self, wait_for_completion=True):
        self.heterogenous_multi_vGPU[Constants.UPDATING] = True
        self.update(data_points=["heterogenous_multi_vGPU"], wait_for_completion=wait_for_completion)

    def update_heterogenous_time_slice_profile(self, wait_for_completion=True):
        self.heterogenous_time_slice_profile[Constants.UPDATING] = True
        self.update(data_points=["heterogenous_time_slice_profile"], wait_for_completion=wait_for_completion)

    def update_heterogenous_time_slice_sizes(self, wait_for_completion=True):
        self.heterogenous_time_slice_sizes[Constants.UPDATING] = True
        self.update(data_points=["heterogenous_time_slice_sizes"], wait_for_completion=wait_for_completion)

    def update_ICM_indent(self, wait_for_completion=True):
        self.ICM_indent[Constants.UPDATING] = True
        self.update(data_points=["ICM_indent"], wait_for_completion=wait_for_completion)

    def update_ICM_method(self, wait_for_completion=True):
        self.ICM_method[Constants.UPDATING] = True
        self.update(data_points=["ICM_method"], wait_for_completion=wait_for_completion)

    def update_inf_filename(self, wait_for_completion=True):
        self.inf_filename[Constants.UPDATING] = True
        self.update(data_points=["inf_filename"], wait_for_completion=wait_for_completion)

    def update_inf_section(self, wait_for_completion=True):
        self.inf_section[Constants.UPDATING] = True
        self.update(data_points=["inf_section"], wait_for_completion=wait_for_completion)

    def update_info_ROM_ecc(self, wait_for_completion=True):
        self.info_ROM_ecc[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_ecc"], wait_for_completion=wait_for_completion)

    def update_info_ROM_oem(self, wait_for_completion=True):
        self.info_ROM_oem[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_oem"], wait_for_completion=wait_for_completion)

    def update_info_ROM_power(self, wait_for_completion=True):
        self.info_ROM_power[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_power"], wait_for_completion=wait_for_completion)

    def update_info_ROM_version(self, wait_for_completion=True):
        self.info_ROM_version[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_version"], wait_for_completion=wait_for_completion)

    def update_install_date(self, wait_for_completion=True):
        self.install_date[Constants.UPDATING] = True
        self.update(data_points=["install_date"], wait_for_completion=wait_for_completion)

    def update_installed_display_drivers(self, wait_for_completion=True):
        self.installed_display_drivers[Constants.UPDATING] = True
        self.update(data_points=["installed_display_drivers"], wait_for_completion=wait_for_completion)

    def update_last_error_code(self, wait_for_completion=True):
        self.last_error_code[Constants.UPDATING] = True
        self.update(data_points=["last_error_code"], wait_for_completion=wait_for_completion)

    def update_max_memory_supported(self, wait_for_completion=True):
        self.max_memory_supported[Constants.UPDATING] = True
        self.update(data_points=["max_memory_supported"], wait_for_completion=wait_for_completion)

    def update_max_number_controlled(self, wait_for_completion=True):
        self.max_number_controlled[Constants.UPDATING] = True
        self.update(data_points=["max_number_controlled"], wait_for_completion=wait_for_completion)

    def update_max_refresh_rate(self, wait_for_completion=True):
        self.max_refresh_rate[Constants.UPDATING] = True
        self.update(data_points=["max_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_memory_clock_range(self, wait_for_completion=True):
        self.memory_clock_range[Constants.UPDATING] = True
        self.update(data_points=["memory_clock_range"], wait_for_completion=wait_for_completion)

    def update_memory_free(self, wait_for_completion=True):
        self.memory_free[Constants.UPDATING] = True
        self.update(data_points=["memory_free"], wait_for_completion=wait_for_completion)

    def update_memory_reserved(self, wait_for_completion=True):
        self.memory_reserved[Constants.UPDATING] = True
        self.update(data_points=["memory_reserved"], wait_for_completion=wait_for_completion)

    def update_memory_total(self, wait_for_completion=True):
        self.memory_total[Constants.UPDATING] = True
        self.update(data_points=["memory_total"], wait_for_completion=wait_for_completion)

    def update_memory_used(self, wait_for_completion=True):
        self.memory_used[Constants.UPDATING] = True
        self.update(data_points=["memory_used"], wait_for_completion=wait_for_completion)

    def update_min_refresh_rate(self, wait_for_completion=True):
        self.min_refresh_rate[Constants.UPDATING] = True
        self.update(data_points=["min_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_monochrome(self, wait_for_completion=True):
        self.monochrome[Constants.UPDATING] = True
        self.update(data_points=["monochrome"], wait_for_completion=wait_for_completion)

    def update_multi_instance_GPU_mode_current(self, wait_for_completion=True):
        self.multi_instance_GPU_mode_current[Constants.UPDATING] = True
        self.update(data_points=["multi_instance_GPU_mode_current"], wait_for_completion=wait_for_completion)

    def update_multi_instance_GPU_mode_pending(self, wait_for_completion=True):
        self.multi_instance_GPU_mode_pending[Constants.UPDATING] = True
        self.update(data_points=["multi_instance_GPU_mode_pending"], wait_for_completion=wait_for_completion)

    def update_name(self, wait_for_completion=True):
        self.name[Constants.UPDATING] = True
        self.update(data_points=["name"], wait_for_completion=wait_for_completion)

    def update_number_of_color_planes(self, wait_for_completion=True):
        self.number_of_color_planes[Constants.UPDATING] = True
        self.update(data_points=["number_of_color_planes"], wait_for_completion=wait_for_completion)

    def update_number_of_video_pages(self, wait_for_completion=True):
        self.number_of_video_pages[Constants.UPDATING] = True
        self.update(data_points=["number_of_video_pages"], wait_for_completion=wait_for_completion)

    def update_operating_mode_current(self, wait_for_completion=True):
        self.operating_mode_current[Constants.UPDATING] = True
        self.update(data_points=["operating_mode_current"], wait_for_completion=wait_for_completion)

    def update_operating_mode_pending(self, wait_for_completion=True):
        self.operating_mode_pending[Constants.UPDATING] = True
        self.update(data_points=["operating_mode_pending"], wait_for_completion=wait_for_completion)

    def update_pci_bus(self, wait_for_completion=True):
        self.pci_bus[Constants.UPDATING] = True
        self.update(data_points=["pci_bus"], wait_for_completion=wait_for_completion)

    def update_pci_bus_id(self, wait_for_completion=True):
        self.pci_bus_id[Constants.UPDATING] = True
        self.update(data_points=["pci_bus_id"], wait_for_completion=wait_for_completion)

    def update_pci_device(self, wait_for_completion=True):
        self.pci_device[Constants.UPDATING] = True
        self.update(data_points=["pci_device"], wait_for_completion=wait_for_completion)

    def update_pci_device_id(self, wait_for_completion=True):
        self.pci_device_id[Constants.UPDATING] = True
        self.update(data_points=["pci_device_id"], wait_for_completion=wait_for_completion)

    def update_pci_domain(self, wait_for_completion=True):
        self.pci_domain[Constants.UPDATING] = True
        self.update(data_points=["pci_domain"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_current(self, wait_for_completion=True):
        self.pci_link_generation_current[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_current"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_device_host_maximum(self, wait_for_completion=True):
        self.pci_link_generation_device_host_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_device_host_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_gpu_maximum(self, wait_for_completion=True):
        self.pci_link_generation_gpu_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_gpu_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_maximum(self, wait_for_completion=True):
        self.pci_link_generation_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_width_current(self, wait_for_completion=True):
        self.pci_link_width_current[Constants.UPDATING] = True
        self.update(data_points=["pci_link_width_current"], wait_for_completion=wait_for_completion)

    def update_pci_link_width_maximum(self, wait_for_completion=True):
        self.pci_link_width_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_width_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_sub_device_id(self, wait_for_completion=True):
        self.pci_sub_device_id[Constants.UPDATING] = True
        self.update(data_points=["pci_sub_device_id"], wait_for_completion=wait_for_completion)

    def update_persistence_mode(self, wait_for_completion=True):
        self.persistence_mode[Constants.UPDATING] = True
        self.update(data_points=["persistence_mode"], wait_for_completion=wait_for_completion)

    def update_PNP_device_id(self, wait_for_completion=True):
        self.PNP_device_id[Constants.UPDATING] = True
        self.update(data_points=["PNP_device_id"], wait_for_completion=wait_for_completion)

    def update_power_draw(self, wait_for_completion=True):
        self.power_draw[Constants.UPDATING] = True
        self.update(data_points=["power_draw"], wait_for_completion=wait_for_completion)

    def update_power_draw_average(self, wait_for_completion=True):
        self.power_draw_average[Constants.UPDATING] = True
        self.update(data_points=["power_draw_average"], wait_for_completion=wait_for_completion)

    def update_power_draw_default_limit(self, wait_for_completion=True):
        self.power_draw_default_limit[Constants.UPDATING] = True
        self.update(data_points=["power_draw_default_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_enforced_limit(self, wait_for_completion=True):
        self.power_draw_enforced_limit[Constants.UPDATING] = True
        self.update(data_points=["power_draw_enforced_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_instant(self, wait_for_completion=True):
        self.power_draw_instant[Constants.UPDATING] = True
        self.update(data_points=["power_draw_instant"], wait_for_completion=wait_for_completion)

    def update_power_draw_limit(self, wait_for_completion=True):
        self.power_draw_limit[Constants.UPDATING] = True
        self.update(data_points=["power_draw_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_maximum(self, wait_for_completion=True):
        self.power_draw_maximum[Constants.UPDATING] = True
        self.update(data_points=["power_draw_maximum"], wait_for_completion=wait_for_completion)

    def update_power_draw_minimum(self, wait_for_completion=True):
        self.power_draw_minimum[Constants.UPDATING] = True
        self.update(data_points=["power_draw_minimum"], wait_for_completion=wait_for_completion)

    def update_power_management_capabilities(self, wait_for_completion=True):
        self.power_management_capabilities[Constants.UPDATING] = True
        self.update(data_points=["power_management_capabilities"], wait_for_completion=wait_for_completion)

    def update_power_management_supported(self, wait_for_completion=True):
        self.power_management_supported[Constants.UPDATING] = True
        self.update(data_points=["power_management_supported"], wait_for_completion=wait_for_completion)

    def update_protected_memory_free(self, wait_for_completion=True):
        self.protected_memory_free[Constants.UPDATING] = True
        self.update(data_points=["protected_memory_free"], wait_for_completion=wait_for_completion)

    def update_protected_memory_total(self, wait_for_completion=True):
        self.protected_memory_total[Constants.UPDATING] = True
        self.update(data_points=["protected_memory_total"], wait_for_completion=wait_for_completion)

    def update_protected_memory_used(self, wait_for_completion=True):
        self.protected_memory_used[Constants.UPDATING] = True
        self.update(data_points=["protected_memory_used"], wait_for_completion=wait_for_completion)

    def update_protocol_supported(self, wait_for_completion=True):
        self.protocol_supported[Constants.UPDATING] = True
        self.update(data_points=["protocol_supported"], wait_for_completion=wait_for_completion)

    def update_performance_state(self, wait_for_completion=True):
        self.performance_state[Constants.UPDATING] = True
        self.update(data_points=["performance_state"], wait_for_completion=wait_for_completion)

    def update_retired_pages_double_bit_ecc_errors_count(self, wait_for_completion=True):
        self.retired_pages_double_bit_ecc_errors_count[Constants.UPDATING] = True
        self.update(data_points=["retired_pages_double_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)

    def update_retired_pages_single_bit_ecc_errors_count(self, wait_for_completion=True):
        self.retired_pages_single_bit_ecc_errors_count[Constants.UPDATING] = True
        self.update(data_points=["retired_pages_single_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)

    def update_retired_pages_pending(self, wait_for_completion=True):
        self.retired_pages_pending[Constants.UPDATING] = True
        self.update(data_points=["retired_pages_pending"], wait_for_completion=wait_for_completion)

    def update_reserved_system_palette_entries(self, wait_for_completion=True):
        self.reserved_system_palette_entries[Constants.UPDATING] = True
        self.update(data_points=["reserved_system_palette_entries"], wait_for_completion=wait_for_completion)

    def update_reset_required(self, wait_for_completion=True):
        self.reset_required[Constants.UPDATING] = True
        self.update(data_points=["reset_required"], wait_for_completion=wait_for_completion)

    def update_reset_and_drain_recommended(self, wait_for_completion=True):
        self.reset_and_drain_recommended[Constants.UPDATING] = True
        self.update(data_points=["reset_and_drain_recommended"], wait_for_completion=wait_for_completion)

    def update_serial(self, wait_for_completion=True):
        self.serial[Constants.UPDATING] = True
        self.update(data_points=["serial"], wait_for_completion=wait_for_completion)

    def update_specification_version(self, wait_for_completion=True):
        self.specification_version[Constants.UPDATING] = True
        self.update(data_points=["specification_version"], wait_for_completion=wait_for_completion)

    def update_status(self, wait_for_completion=True):
        self.status[Constants.UPDATING] = True
        self.update(data_points=["status"], wait_for_completion=wait_for_completion)

    def update_status_info(self, wait_for_completion=True):
        self.status_info[Constants.UPDATING] = True
        self.update(data_points=["status_info"], wait_for_completion=wait_for_completion)

    def update_system_creation_class_name(self, wait_for_completion=True):
        self.system_creation_class_name[Constants.UPDATING] = True
        self.update(data_points=["system_creation_class_name"], wait_for_completion=wait_for_completion)

    def update_system_name(self, wait_for_completion=True):
        self.system_name[Constants.UPDATING] = True
        self.update(data_points=["system_name"], wait_for_completion=wait_for_completion)

    def update_system_palette_entries(self, wait_for_completion=True):
        self.system_palette_entries[Constants.UPDATING] = True
        self.update(data_points=["system_palette_entries"], wait_for_completion=wait_for_completion)

    def update_GPU_system_processor_mode_current(self, wait_for_completion=True):
        self.GPU_system_processor_mode_current[Constants.UPDATING] = True
        self.update(data_points=["GPU_system_processor_mode_current"], wait_for_completion=wait_for_completion)

    def update_GPU_system_processor_mode_default(self, wait_for_completion=True):
        self.GPU_system_processor_mode_default[Constants.UPDATING] = True
        self.update(data_points=["GPU_system_processor_mode_default"], wait_for_completion=wait_for_completion)

    def update_temperature_core(self, wait_for_completion=True):
        self.temperature_core[Constants.UPDATING] = True
        self.update(data_points=["temperature_core"], wait_for_completion=wait_for_completion)

    def update_temperature_core_limit(self, wait_for_completion=True):
        self.temperature_core_limit[Constants.UPDATING] = True
        self.update(data_points=["temperature_core_limit"], wait_for_completion=wait_for_completion)

    def update_temperature_memory(self, wait_for_completion=True):
        self.temperature_memory[Constants.UPDATING] = True
        self.update(data_points=["temperature_memory"], wait_for_completion=wait_for_completion)

    def update_time_of_last_reset(self, wait_for_completion=True):
        self.time_of_last_reset[Constants.UPDATING] = True
        self.update(data_points=["time_of_last_reset"], wait_for_completion=wait_for_completion)

    def update_utilization_decoder(self, wait_for_completion=True):
        self.utilization_decoder[Constants.UPDATING] = True
        self.update(data_points=["utilization_decoder"], wait_for_completion=wait_for_completion)

    def update_utilization_encoder(self, wait_for_completion=True):
        self.utilization_encoder[Constants.UPDATING] = True
        self.update(data_points=["utilization_encoder"], wait_for_completion=wait_for_completion)

    def update_utilization_gpu(self, wait_for_completion=True):
        self.utilization_gpu[Constants.UPDATING] = True
        self.update(data_points=["utilization_gpu"], wait_for_completion=wait_for_completion)

    def update_utilization_jpeg(self, wait_for_completion=True):
        self.utilization_jpeg[Constants.UPDATING] = True
        self.update(data_points=["utilization_jpeg"], wait_for_completion=wait_for_completion)

    def update_utilization_memory(self, wait_for_completion=True):
        self.utilization_memory[Constants.UPDATING] = True
        self.update(data_points=["utilization_memory"], wait_for_completion=wait_for_completion)

    def update_utilization_optical_flow(self, wait_for_completion=True):
        self.utilization_optical_flow[Constants.UPDATING] = True
        self.update(data_points=["utilization_optical_flow"], wait_for_completion=wait_for_completion)

    def update_uuid(self, wait_for_completion=True):
        self.uuid[Constants.UPDATING] = True
        self.update(data_points=["uuid"], wait_for_completion=wait_for_completion)

    def update_vbios_version(self, wait_for_completion=True):
        self.vbios_version[Constants.UPDATING] = True
        self.update(data_points=["vbios_version"], wait_for_completion=wait_for_completion)

    def update_video_architecture(self, wait_for_completion=True):
        self.video_architecture[Constants.UPDATING] = True
        self.update(data_points=["video_architecture"], wait_for_completion=wait_for_completion)

    def update_video_memory_type(self, wait_for_completion=True):
        self.video_memory_type[Constants.UPDATING] = True
        self.update(data_points=["video_memory_type"], wait_for_completion=wait_for_completion)

    def update_video_mode(self, wait_for_completion=True):
        self.video_mode[Constants.UPDATING] = True
        self.update(data_points=["video_mode"], wait_for_completion=wait_for_completion)

    def update_video_mode_description(self, wait_for_completion=True):
        self.video_mode_description[Constants.UPDATING] = True
        self.update(data_points=["video_mode_description"], wait_for_completion=wait_for_completion)

    def update_video_processor(self, wait_for_completion=True):
        self.video_processor[Constants.UPDATING] = True
        self.update(data_points=["video_processor"], wait_for_completion=wait_for_completion)
