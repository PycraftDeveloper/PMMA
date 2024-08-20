import json as _json
import gc as _gc

import wmi as _wmi
import pyadl as _pyadl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.executor import Executor as _Executor

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

        self.gpu_instances = []
        for key in self.unique_gpus:
            self.gpu_instances.append(_GPU(self.unique_gpus[key]))

        print(self.gpu_instances[0].__dict__)

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

        self.accelerator_capabilities = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['AcceleratorCapabilities'], Constants.PYADL: []}}
        self.accounting_mode_enabled = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['accounting.mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.accounting_mode_buffer_size = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['accounting.buffer_size'], Constants.WMI: [], Constants.PYADL: []}}
        self.adapter_compatibility = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['AdapterCompatibility'], Constants.PYADL: []}}
        self.adapter_DAC_type = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['AdapterDACType'], Constants.PYADL: []}}
        self.adapter_id = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['adapterID']}}
        self.adapter_index = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['adapterIndex']}}
        self.addressing_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['addressing_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.availability = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['Availability'], Constants.PYADL: []}}
        self.capability_descriptions = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CapabilityDescriptions'], Constants.PYADL: []}}
        self.caption = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['Caption'], Constants.PYADL: []}}
        self.chip_to_chip_interconnect_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['c2c.mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_as_bitmap = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.active', 'clocks_throttle_reasons.active'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_application_setting = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.applications_clocks_setting', 'clocks_throttle_reasons.applications_clocks_setting'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_is_hardware_limited = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.hw_slowdown', 'clocks_throttle_reasons.hw_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_gpu_idle_limited = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.gpu_idle', 'clocks_throttle_reasons.gpu_idle'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_software_power_limited = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.sw_power_cap', 'clocks_throttle_reasons.sw_power_cap'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_software_thermal_limited = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.sw_thermal_slowdown', 'clocks_throttle_reasons.sw_thermal_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_power_break_slowdown_limited = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.hw_power_brake_slowdown', 'clocks_throttle_reasons.hw_power_brake_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_supported = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.supported', 'clocks_throttle_reasons.supported'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_sync_boost = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.sync_boost', 'clocks_throttle_reasons.sync_boost'], Constants.WMI: [], Constants.PYADL: []}}
        self.clock_event_reasons_thermal_limited = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks_event_reasons.hw_thermal_slowdown', 'clocks_throttle_reasons.hw_thermal_slowdown'], Constants.WMI: [], Constants.PYADL: []}}
        self.color_table_entries = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ColorTableEntries'], Constants.PYADL: []}}
        self.compute_cap = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['compute_cap'], Constants.WMI: [], Constants.PYADL: []}}
        self.compute_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['compute_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.config_manager_error_code = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ConfigManagerErrorCode'], Constants.PYADL: []}}
        self.config_manager_user_config = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ConfigManagerUserConfig'], Constants.PYADL: []}}
        self.core_voltage = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getCurrentCoreVoltage']}}
        self.core_voltage_range = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['coreVoltageRange']}}
        self.creation_class_name = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CreationClassName'], Constants.PYADL: []}}
        self.current_bits_per_pixel = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentBitsPerPixel'], Constants.PYADL: []}}
        self.current_horizontal_resolution = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentHorizontalResolution'], Constants.PYADL: []}}
        self.current_number_of_colors = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentNumberOfColors'], Constants.PYADL: []}}
        self.current_number_of_columns = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentNumberOfColumns'], Constants.PYADL: []}}
        self.current_number_of_rows = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentNumberOfRows'], Constants.PYADL: []}}
        self.current_refresh_rate = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentRefreshRate'], Constants.PYADL: []}}
        self.current_scan_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentScanMode'], Constants.PYADL: []}}
        self.current_vertical_resolution = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['CurrentVerticalResolution'], Constants.PYADL: []}}
        self.description = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['Description'], Constants.PYADL: []}}
        self.device_id = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['DeviceID'], Constants.PYADL: []}}
        self.device_specific_pens = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['DeviceSpecificPens'], Constants.PYADL: []}}
        self.display_active = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['display_active'], Constants.WMI: [], Constants.PYADL: []}}
        self.display_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['display_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.dither_type = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['DitherType'], Constants.PYADL: []}}
        self.driver_date = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['DriverDate'], Constants.PYADL: []}}
        self.driver_model_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['driver_model.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.driver_model_pending = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['driver_model.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.driver_version = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['driver_version'], Constants.WMI: ['DriverVersion'], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_cbu = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_primary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_register_file = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_secondary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_shared_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_sram = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_texture_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_total = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_all_time_in_video_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.aggregate.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_cbu = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_primary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_register_file = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_secondary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_shared_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_sram = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_texture_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_total = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_corrected_since_reboot_in_video_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.corrected.volatile.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_cbu = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_primary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_register_file = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_secondary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_shared_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_sram = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_texture_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_total = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_all_time_in_video_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.aggregate.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_cbu = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.cbu'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.l1_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_register_file = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.register_file'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.l2_cache'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.dram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_sram = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.sram'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.texture_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_total = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_errors_uncorrected_since_reboot_in_video_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.errors.uncorrected.volatile.device_memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_mode_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.ecc_mode_pending = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['ecc.mode.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.encoder_average_FPS = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['encoder.stats.averageFps'], Constants.WMI: [], Constants.PYADL: []}}
        self.encoder_average_latency = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['encoder.stats.averageLatency'], Constants.WMI: [], Constants.PYADL: []}}
        self.encoder_session_count = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['encoder.stats.sessionCount'], Constants.WMI: [], Constants.PYADL: []}}
        self.engine_clock_range = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['engineClockRange']}}
        self.error_cleared = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ErrorCleared'], Constants.PYADL: []}}
        self.error_description = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ErrorDescription'], Constants.PYADL: []}}
        self.fabric_state = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['fabric.state'], Constants.WMI: [], Constants.PYADL: []}}
        self.fabric_status = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['fabric.status'], Constants.WMI: [], Constants.PYADL: []}}
        self.fan_speed_percentage = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['fan.speed'], Constants.WMI: [], Constants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self.fan_speed_percentage_range = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self.fan_speed_RPM = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self.fan_speed_RPM_range = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self.fractional_multi_vGPU = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['vgpu_device_capability.fractional_multiVgpu'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_default_shader_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.default_applications.graphics', 'clocks.default_applications.gr'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_default_memory_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.default_applications.memory', 'clocks.default_applications.mem'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_memory_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.applications.memory', 'clocks.applications.mem'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_application_shader_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.applications.graphics', 'clocks.applications.gr'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_maximum_memory_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.max.memory', 'clocks.max.mem'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_maximum_shader_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.max.graphics', 'clocks.max.gr'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_maximum_streaming_multiprocessor_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.max.sm', 'clocks.max.sm'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_memory_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.current.memory', 'clocks.mem'], Constants.WMI: [], Constants.PYADL: ['getCurrentMemoryClock']}}
        self.frequency_shader_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.current.graphics', 'clocks.gr'], Constants.WMI: [], Constants.PYADL: ['getCurrentEngineClock']}}
        self.frequency_streaming_multiprocessor_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.current.sm', 'clocks.sm'], Constants.WMI: [], Constants.PYADL: []}}
        self.frequency_video_clock = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['clocks.current.video', 'clocks.video'], Constants.WMI: [], Constants.PYADL: []}}
        self.heterogenous_multi_vGPU = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['vgpu_driver_capability.heterogenous_multivGPU'], Constants.WMI: [], Constants.PYADL: []}}
        self.heterogenous_time_slice_profile = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_profile'], Constants.WMI: [], Constants.PYADL: []}}
        self.heterogenous_time_slice_sizes = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_sizes'], Constants.WMI: [], Constants.PYADL: []}}
        self.ICM_indent = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ICMIntent'], Constants.PYADL: []}}
        self.ICM_method = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ICMMethod'], Constants.PYADL: []}}
        self.inf_filename = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['InfFilename'], Constants.PYADL: []}}
        self.inf_section = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['InfSection'], Constants.PYADL: []}}
        self.info_ROM_ecc = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['inforom.ecc'], Constants.WMI: [], Constants.PYADL: []}}
        self.info_ROM_oem = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['inforom.oem'], Constants.WMI: [], Constants.PYADL: []}}
        self.info_ROM_power = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['inforom.pwr', 'inforom.power'], Constants.WMI: [], Constants.PYADL: []}}
        self.info_ROM_version = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['inforom.img', 'inforom.image'], Constants.WMI: [], Constants.PYADL: []}}
        self.install_date = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['InstallDate'], Constants.PYADL: []}}
        self.installed_display_drivers = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['InstalledDisplayDrivers'], Constants.PYADL: []}}
        self.last_error_code = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['LastErrorCode'], Constants.PYADL: []}}
        self.max_memory_supported = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['MaxMemorySupported'], Constants.PYADL: []}}
        self.max_number_controlled = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['MaxNumberControlled'], Constants.PYADL: []}}
        self.max_refresh_rate = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['MaxRefreshRate'], Constants.PYADL: []}}
        self.memory_clock_range = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ['getMemoryClockRange']}}
        self.memory_free = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['memory.free'], Constants.WMI: [], Constants.PYADL: []}}
        self.memory_reserved = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['memory.reserved'], Constants.WMI: [], Constants.PYADL: []}}
        self.memory_total = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['memory.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.memory_used = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['memory.used'], Constants.WMI: [], Constants.PYADL: []}}
        self.min_refresh_rate = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['MinRefreshRate'], Constants.PYADL: []}}
        self.monochrome = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['Monochrome'], Constants.PYADL: []}}
        self.multi_instance_GPU_mode_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['mig.mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.multi_instance_GPU_mode_pending = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['mig.mode.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.name = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['name', 'gpu_name'], Constants.WMI: ['Name'], Constants.PYADL: ['adapterName']}}
        self.number_of_color_planes = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['NumberOfColorPlanes'], Constants.PYADL: []}}
        self.number_of_video_pages = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['NumberOfVideoPages'], Constants.PYADL: []}}
        self.operating_mode_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['gom.current', 'gpu_operation_mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.operating_mode_pending = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['gom.pending', 'gpu_operation_mode.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_bus = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pci.bus'], Constants.WMI: [], Constants.PYADL: ['busNumber']}}
        self.pci_bus_id = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pci.bus_id', 'gpu_bus_id'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_device = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pci.device'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_device_id = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pci.device_id'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_domain = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pci.domain'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pcie.link.gen.gpucurrent'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_device_host_maximum = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pcie.link.gen.max'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_gpu_maximum = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pcie.link.gen.gpumax'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_generation_maximum = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pcie.link.gen.hostmax'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_width_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pcie.link.width.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_link_width_maximum = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pcie.link.width.max'], Constants.WMI: [], Constants.PYADL: []}}
        self.pci_sub_device_id = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pci.sub_device_id'], Constants.WMI: [], Constants.PYADL: []}}
        self.persistence_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['persistence_mode'], Constants.WMI: [], Constants.PYADL: []}}
        self.PNP_device_id = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['PNPDeviceID'], Constants.PYADL: []}}
        self.power_draw = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.draw'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_average = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.draw.average'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_default_limit = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.default_limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_enforced_limit = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['enforced.power.limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_instant = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.draw.instant'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_limit = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_maximum = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.max_limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_draw_minimum = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.min_limit'], Constants.WMI: [], Constants.PYADL: []}}
        self.power_management_capabilities = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['PowerManagementCapabilities'], Constants.PYADL: []}}
        self.power_management_supported = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['power.management'], Constants.WMI: ['PowerManagementSupported'], Constants.PYADL: []}}
        self.protected_memory_free = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['protected_memory.free'], Constants.WMI: [], Constants.PYADL: []}}
        self.protected_memory_total = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['protected_memory.total'], Constants.WMI: [], Constants.PYADL: []}}
        self.protected_memory_used = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['protected_memory.used'], Constants.WMI: [], Constants.PYADL: []}}
        self.protocol_supported = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ProtocolSupported'], Constants.PYADL: []}}
        self.performance_state = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['pstate'], Constants.WMI: [], Constants.PYADL: []}}
        self.retired_pages_double_bit_ecc_errors_count = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['retired_pages.double_bit.count', 'retired_pages.dbe'], Constants.WMI: [], Constants.PYADL: []}}
        self.retired_pages_single_bit_ecc_errors_count = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['retired_pages.single_bit_ecc.count', 'retired_pages.sbe'], Constants.WMI: [], Constants.PYADL: []}}
        self.retired_pages_pending = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['retired_pages.pending'], Constants.WMI: [], Constants.PYADL: []}}
        self.reserved_system_palette_entries = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['ReservedSystemPaletteEntries'], Constants.PYADL: []}}
        self.reset_required = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['reset_status.reset_required'], Constants.WMI: [], Constants.PYADL: []}}
        self.reset_and_drain_recommended = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['reset_status.drain_and_reset_recommended'], Constants.WMI: [], Constants.PYADL: []}}
        self.serial = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['serial', 'gpu_serial'], Constants.WMI: [], Constants.PYADL: []}}
        self.specification_version = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['SpecificationVersion'], Constants.PYADL: []}}
        self.status = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['Status'], Constants.PYADL: []}}
        self.status_info = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['StatusInfo'], Constants.PYADL: []}}
        self.system_creation_class_name = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['SystemCreationClassName'], Constants.PYADL: []}}
        self.system_name = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['SystemName'], Constants.PYADL: []}}
        self.system_palette_entries = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['SystemPaletteEntries'], Constants.PYADL: []}}
        self.GPU_system_processor_mode_current = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['gsp.mode.current'], Constants.WMI: [], Constants.PYADL: []}}
        self.GPU_system_processor_mode_default = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['gsp.mode.default'], Constants.WMI: [], Constants.PYADL: []}}
        self.temperature_core = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['temperature.gpu'], Constants.WMI: [], Constants.PYADL: ['getCurrentTemperature']}}
        self.temperature_core_limit = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['temperature.gpu.tlimit'], Constants.WMI: [], Constants.PYADL: []}}
        self.temperature_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['temperature.memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.time_of_last_reset = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['TimeOfLastReset'], Constants.PYADL: []}}
        self.utilization_decoder = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['utilization.decoder'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_encoder = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['utilization.encoder'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_gpu = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['utilization.gpu'], Constants.WMI: [], Constants.PYADL: ['getCurrentUsage']}}
        self.utilization_jpeg = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['utilization.jpeg'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_memory = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['utilization.memory'], Constants.WMI: [], Constants.PYADL: []}}
        self.utilization_optical_flow = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['utilization.ofa'], Constants.WMI: [], Constants.PYADL: []}}
        self.uuid = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['uuid', 'gpu_uuid'], Constants.WMI: [], Constants.PYADL: ['uuid']}}
        self.vbios_version = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: ['vbios_version'], Constants.WMI: [], Constants.PYADL: []}}
        self.video_architecture = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['VideoArchitecture'], Constants.PYADL: []}}
        self.video_memory_type = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['VideoMemoryType'], Constants.PYADL: []}}
        self.video_mode = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['VideoMode'], Constants.PYADL: []}}
        self.video_mode_description = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['VideoModeDescription'], Constants.PYADL: []}}
        self.video_processor = {"value": None, "updating": True, "manually set": False, "data collection methods": {Constants.SMI: [], Constants.WMI: ['VideoProcessor'], Constants.PYADL: []}}

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

        self.update(everything=True)

    def update(self, everything=False, data_points=None):
        if data_points is None:
            data_points = self.gpu_data_points
        smi_data = ""
        smi_data_points = []
        adl_data = []
        adl_data_points = []
        wmi_data = []
        wmi_data_points = []
        for data_point in data_points:
            self.__dict__[data_point]["updating"] = False
            if self.__dict__[data_point]["manually set"] is False or everything:
                data_collection_strategies = self.__dict__[data_point]["data collection methods"]
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
                        self.__dict__[data_point]["value"] = data
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
                        self.__dict__[data_point]["value"] = data
                        if data is not None:
                            set_attributes.append(data_point)

            elif priority == Constants.WMI and _wmi != []:
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
                        self.__dict__[data_point]["value"] = data
                        if data is not None:
                            set_attributes.append(data_point)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_accelerator_capabilities(self):
        return self.accelerator_capabilities

    def get_accounting_mode_enabled(self):
        return self.accounting_mode_enabled

    def get_accounting_mode_buffer_size(self):
        return self.accounting_mode_buffer_size

    def get_adapter_compatibility(self):
        return self.adapter_compatibility

    def get_adapter_DAC_type(self):
        return self.adapter_DAC_type

    def get_adapter_id(self):
        return self.adapter_id

    def get_adapter_index(self):
        return self.adapter_index

    def get_addressing_mode(self):
        return self.addressing_mode

    def get_availability(self):
        return self.availability

    def get_capability_descriptions(self):
        return self.capability_descriptions

    def get_caption(self):
        return self.caption

    def get_chip_to_chip_interconnect_mode(self):
        return self.chip_to_chip_interconnect_mode

    def get_clock_event_reasons_as_bitmap(self):
        return self.clock_event_reasons_as_bitmap

    def get_clock_event_reasons_application_setting(self):
        return self.clock_event_reasons_application_setting

    def get_clock_event_reasons_is_hardware_limited(self):
        return self.clock_event_reasons_is_hardware_limited

    def get_clock_event_reasons_gpu_idle_limited(self):
        return self.clock_event_reasons_gpu_idle_limited

    def get_clock_event_reasons_software_power_limited(self):
        return self.clock_event_reasons_software_power_limited

    def get_clock_event_reasons_software_thermal_limited(self):
        return self.clock_event_reasons_software_thermal_limited

    def get_clock_event_reasons_power_break_slowdown_limited(self):
        return self.clock_event_reasons_power_break_slowdown_limited

    def get_clock_event_reasons_supported(self):
        return self.clock_event_reasons_supported

    def get_clock_event_reasons_sync_boost(self):
        return self.clock_event_reasons_sync_boost

    def get_clock_event_reasons_thermal_limited(self):
        return self.clock_event_reasons_thermal_limited

    def get_color_table_entries(self):
        return self.color_table_entries

    def get_compute_cap(self):
        return self.compute_cap

    def get_compute_mode(self):
        return self.compute_mode

    def get_config_manager_error_code(self):
        return self.config_manager_error_code

    def get_config_manager_user_config(self):
        return self.config_manager_user_config

    def get_core_voltage(self):
        return self.core_voltage

    def get_core_voltage_range(self):
        return self.core_voltage_range

    def get_creation_class_name(self):
        return self.creation_class_name

    def get_current_bits_per_pixel(self):
        return self.current_bits_per_pixel

    def get_current_horizontal_resolution(self):
        return self.current_horizontal_resolution

    def get_current_number_of_colors(self):
        return self.current_number_of_colors

    def get_current_number_of_columns(self):
        return self.current_number_of_columns

    def get_current_number_of_rows(self):
        return self.current_number_of_rows

    def get_current_refresh_rate(self):
        return self.current_refresh_rate

    def get_current_scan_mode(self):
        return self.current_scan_mode

    def get_current_vertical_resolution(self):
        return self.current_vertical_resolution

    def get_description(self):
        return self.description

    def get_device_id(self):
        return self.device_id

    def get_device_specific_pens(self):
        return self.device_specific_pens

    def get_display_active(self):
        return self.display_active

    def get_display_mode(self):
        return self.display_mode

    def get_dither_type(self):
        return self.dither_type

    def get_driver_date(self):
        return self.driver_date

    def get_driver_model_current(self):
        return self.driver_model_current

    def get_driver_model_pending(self):
        return self.driver_model_pending

    def get_driver_version(self):
        return self.driver_version

    def get_ecc_errors_corrected_all_time_in_cbu(self):
        return self.ecc_errors_corrected_all_time_in_cbu

    def get_ecc_errors_corrected_all_time_in_primary_cache(self):
        return self.ecc_errors_corrected_all_time_in_primary_cache

    def get_ecc_errors_corrected_all_time_in_register_file(self):
        return self.ecc_errors_corrected_all_time_in_register_file

    def get_ecc_errors_corrected_all_time_in_secondary_cache(self):
        return self.ecc_errors_corrected_all_time_in_secondary_cache

    def get_ecc_errors_corrected_all_time_in_shared_memory(self):
        return self.ecc_errors_corrected_all_time_in_shared_memory

    def get_ecc_errors_corrected_all_time_in_sram(self):
        return self.ecc_errors_corrected_all_time_in_sram

    def get_ecc_errors_corrected_all_time_in_texture_memory(self):
        return self.ecc_errors_corrected_all_time_in_texture_memory

    def get_ecc_errors_corrected_all_time_in_total(self):
        return self.ecc_errors_corrected_all_time_in_total

    def get_ecc_errors_corrected_all_time_in_video_memory(self):
        return self.ecc_errors_corrected_all_time_in_video_memory

    def get_ecc_errors_corrected_since_reboot_in_cbu(self):
        return self.ecc_errors_corrected_since_reboot_in_cbu

    def get_ecc_errors_corrected_since_reboot_in_primary_cache(self):
        return self.ecc_errors_corrected_since_reboot_in_primary_cache

    def get_ecc_errors_corrected_since_reboot_in_register_file(self):
        return self.ecc_errors_corrected_since_reboot_in_register_file

    def get_ecc_errors_corrected_since_reboot_in_secondary_cache(self):
        return self.ecc_errors_corrected_since_reboot_in_secondary_cache

    def get_ecc_errors_corrected_since_reboot_in_shared_memory(self):
        return self.ecc_errors_corrected_since_reboot_in_shared_memory

    def get_ecc_errors_corrected_since_reboot_in_sram(self):
        return self.ecc_errors_corrected_since_reboot_in_sram

    def get_ecc_errors_corrected_since_reboot_in_texture_memory(self):
        return self.ecc_errors_corrected_since_reboot_in_texture_memory

    def get_ecc_errors_corrected_since_reboot_in_total(self):
        return self.ecc_errors_corrected_since_reboot_in_total

    def get_ecc_errors_corrected_since_reboot_in_video_memory(self):
        return self.ecc_errors_corrected_since_reboot_in_video_memory

    def get_ecc_errors_uncorrected_all_time_in_cbu(self):
        return self.ecc_errors_uncorrected_all_time_in_cbu

    def get_ecc_errors_uncorrected_all_time_in_primary_cache(self):
        return self.ecc_errors_uncorrected_all_time_in_primary_cache

    def get_ecc_errors_uncorrected_all_time_in_register_file(self):
        return self.ecc_errors_uncorrected_all_time_in_register_file

    def get_ecc_errors_uncorrected_all_time_in_secondary_cache(self):
        return self.ecc_errors_uncorrected_all_time_in_secondary_cache

    def get_ecc_errors_uncorrected_all_time_in_shared_memory(self):
        return self.ecc_errors_uncorrected_all_time_in_shared_memory

    def get_ecc_errors_uncorrected_all_time_in_sram(self):
        return self.ecc_errors_uncorrected_all_time_in_sram

    def get_ecc_errors_uncorrected_all_time_in_texture_memory(self):
        return self.ecc_errors_uncorrected_all_time_in_texture_memory

    def get_ecc_errors_uncorrected_all_time_in_total(self):
        return self.ecc_errors_uncorrected_all_time_in_total

    def get_ecc_errors_uncorrected_all_time_in_video_memory(self):
        return self.ecc_errors_uncorrected_all_time_in_video_memory

    def get_ecc_errors_uncorrected_since_reboot_in_cbu(self):
        return self.ecc_errors_uncorrected_since_reboot_in_cbu

    def get_ecc_errors_uncorrected_since_reboot_in_primary_cache(self):
        return self.ecc_errors_uncorrected_since_reboot_in_primary_cache

    def get_ecc_errors_uncorrected_since_reboot_in_register_file(self):
        return self.ecc_errors_uncorrected_since_reboot_in_register_file

    def get_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self):
        return self.ecc_errors_uncorrected_since_reboot_in_secondary_cache

    def get_ecc_errors_uncorrected_since_reboot_in_shared_memory(self):
        return self.ecc_errors_uncorrected_since_reboot_in_shared_memory

    def get_ecc_errors_uncorrected_since_reboot_in_sram(self):
        return self.ecc_errors_uncorrected_since_reboot_in_sram

    def get_ecc_errors_uncorrected_since_reboot_in_texture_memory(self):
        return self.ecc_errors_uncorrected_since_reboot_in_texture_memory

    def get_ecc_errors_uncorrected_since_reboot_in_total(self):
        return self.ecc_errors_uncorrected_since_reboot_in_total

    def get_ecc_errors_uncorrected_since_reboot_in_video_memory(self):
        return self.ecc_errors_uncorrected_since_reboot_in_video_memory

    def get_ecc_mode_current(self):
        return self.ecc_mode_current

    def get_ecc_mode_pending(self):
        return self.ecc_mode_pending

    def get_encoder_average_FPS(self):
        return self.encoder_average_FPS

    def get_encoder_average_latency(self):
        return self.encoder_average_latency

    def get_encoder_session_count(self):
        return self.encoder_session_count

    def get_engine_clock_range(self):
        return self.engine_clock_range

    def get_error_cleared(self):
        return self.error_cleared

    def get_error_description(self):
        return self.error_description

    def get_fabric_state(self):
        return self.fabric_state

    def get_fabric_status(self):
        return self.fabric_status

    def get_fan_speed_percentage(self):
        return self.fan_speed_percentage

    def get_fan_speed_percentage_range(self):
        return self.fan_speed_percentage_range

    def get_fan_speed_RPM(self):
        return self.fan_speed_RPM

    def get_fan_speed_RPM_range(self):
        return self.fan_speed_RPM_range

    def get_fractional_multi_vGPU(self):
        return self.fractional_multi_vGPU

    def get_frequency_application_default_shader_clock(self):
        return self.frequency_application_default_shader_clock

    def get_frequency_application_default_memory_clock(self):
        return self.frequency_application_default_memory_clock

    def get_frequency_application_memory_clock(self):
        return self.frequency_application_memory_clock

    def get_frequency_application_shader_clock(self):
        return self.frequency_application_shader_clock

    def get_frequency_maximum_memory_clock(self):
        return self.frequency_maximum_memory_clock

    def get_frequency_maximum_shader_clock(self):
        return self.frequency_maximum_shader_clock

    def get_frequency_maximum_streaming_multiprocessor_clock(self):
        return self.frequency_maximum_streaming_multiprocessor_clock

    def get_frequency_memory_clock(self):
        return self.frequency_memory_clock

    def get_frequency_shader_clock(self):
        return self.frequency_shader_clock

    def get_frequency_streaming_multiprocessor_clock(self):
        return self.frequency_streaming_multiprocessor_clock

    def get_frequency_video_clock(self):
        return self.frequency_video_clock

    def get_heterogenous_multi_vGPU(self):
        return self.heterogenous_multi_vGPU

    def get_heterogenous_time_slice_profile(self):
        return self.heterogenous_time_slice_profile

    def get_heterogenous_time_slice_sizes(self):
        return self.heterogenous_time_slice_sizes

    def get_ICM_indent(self):
        return self.ICM_indent

    def get_ICM_method(self):
        return self.ICM_method

    def get_inf_filename(self):
        return self.inf_filename

    def get_inf_section(self):
        return self.inf_section

    def get_info_ROM_ecc(self):
        return self.info_ROM_ecc

    def get_info_ROM_oem(self):
        return self.info_ROM_oem

    def get_info_ROM_power(self):
        return self.info_ROM_power

    def get_info_ROM_version(self):
        return self.info_ROM_version

    def get_install_date(self):
        return self.install_date

    def get_installed_display_drivers(self):
        return self.installed_display_drivers

    def get_last_error_code(self):
        return self.last_error_code

    def get_max_memory_supported(self):
        return self.max_memory_supported

    def get_max_number_controlled(self):
        return self.max_number_controlled

    def get_max_refresh_rate(self):
        return self.max_refresh_rate

    def get_memory_clock_range(self):
        return self.memory_clock_range

    def get_memory_free(self):
        return self.memory_free

    def get_memory_reserved(self):
        return self.memory_reserved

    def get_memory_total(self):
        return self.memory_total

    def get_memory_used(self):
        return self.memory_used

    def get_min_refresh_rate(self):
        return self.min_refresh_rate

    def get_monochrome(self):
        return self.monochrome

    def get_multi_instance_GPU_mode_current(self):
        return self.multi_instance_GPU_mode_current

    def get_multi_instance_GPU_mode_pending(self):
        return self.multi_instance_GPU_mode_pending

    def get_name(self):
        return self.name

    def get_number_of_color_planes(self):
        return self.number_of_color_planes

    def get_number_of_video_pages(self):
        return self.number_of_video_pages

    def get_operating_mode_current(self):
        return self.operating_mode_current

    def get_operating_mode_pending(self):
        return self.operating_mode_pending

    def get_pci_bus(self):
        return self.pci_bus

    def get_pci_bus_id(self):
        return self.pci_bus_id

    def get_pci_device(self):
        return self.pci_device

    def get_pci_device_id(self):
        return self.pci_device_id

    def get_pci_domain(self):
        return self.pci_domain

    def get_pci_link_generation_current(self):
        return self.pci_link_generation_current

    def get_pci_link_generation_device_host_maximum(self):
        return self.pci_link_generation_device_host_maximum

    def get_pci_link_generation_gpu_maximum(self):
        return self.pci_link_generation_gpu_maximum

    def get_pci_link_generation_maximum(self):
        return self.pci_link_generation_maximum

    def get_pci_link_width_current(self):
        return self.pci_link_width_current

    def get_pci_link_width_maximum(self):
        return self.pci_link_width_maximum

    def get_pci_sub_device_id(self):
        return self.pci_sub_device_id

    def get_persistence_mode(self):
        return self.persistence_mode

    def get_PNP_device_id(self):
        return self.PNP_device_id

    def get_power_draw(self):
        return self.power_draw

    def get_power_draw_average(self):
        return self.power_draw_average

    def get_power_draw_default_limit(self):
        return self.power_draw_default_limit

    def get_power_draw_enforced_limit(self):
        return self.power_draw_enforced_limit

    def get_power_draw_instant(self):
        return self.power_draw_instant

    def get_power_draw_limit(self):
        return self.power_draw_limit

    def get_power_draw_maximum(self):
        return self.power_draw_maximum

    def get_power_draw_minimum(self):
        return self.power_draw_minimum

    def get_power_management_capabilities(self):
        return self.power_management_capabilities

    def get_power_management_supported(self):
        return self.power_management_supported

    def get_protected_memory_free(self):
        return self.protected_memory_free

    def get_protected_memory_total(self):
        return self.protected_memory_total

    def get_protected_memory_used(self):
        return self.protected_memory_used

    def get_protocol_supported(self):
        return self.protocol_supported

    def get_performance_state(self):
        return self.performance_state

    def get_retired_pages_double_bit_ecc_errors_count(self):
        return self.retired_pages_double_bit_ecc_errors_count

    def get_retired_pages_single_bit_ecc_errors_count(self):
        return self.retired_pages_single_bit_ecc_errors_count

    def get_retired_pages_pending(self):
        return self.retired_pages_pending

    def get_reserved_system_palette_entries(self):
        return self.reserved_system_palette_entries

    def get_reset_required(self):
        return self.reset_required

    def get_reset_and_drain_recommended(self):
        return self.reset_and_drain_recommended

    def get_serial(self):
        return self.serial

    def get_specification_version(self):
        return self.specification_version

    def get_status(self):
        return self.status

    def get_status_info(self):
        return self.status_info

    def get_system_creation_class_name(self):
        return self.system_creation_class_name

    def get_system_name(self):
        return self.system_name

    def get_system_palette_entries(self):
        return self.system_palette_entries

    def get_GPU_system_processor_mode_current(self):
        return self.GPU_system_processor_mode_current

    def get_GPU_system_processor_mode_default(self):
        return self.GPU_system_processor_mode_default

    def get_temperature_core(self):
        return self.temperature_core

    def get_temperature_core_limit(self):
        return self.temperature_core_limit

    def get_temperature_memory(self):
        return self.temperature_memory

    def get_time_of_last_reset(self):
        return self.time_of_last_reset

    def get_utilization_decoder(self):
        return self.utilization_decoder

    def get_utilization_encoder(self):
        return self.utilization_encoder

    def get_utilization_gpu(self):
        return self.utilization_gpu

    def get_utilization_jpeg(self):
        return self.utilization_jpeg

    def get_utilization_memory(self):
        return self.utilization_memory

    def get_utilization_optical_flow(self):
        return self.utilization_optical_flow

    def get_uuid(self):
        return self.uuid

    def get_vbios_version(self):
        return self.vbios_version

    def get_video_architecture(self):
        return self.video_architecture

    def get_video_memory_type(self):
        return self.video_memory_type

    def get_video_mode(self):
        return self.video_mode

    def get_video_mode_description(self):
        return self.video_mode_description

    def get_video_processor(self):
        return self.video_processor

    def set_accelerator_capabilities(self, value=None):
        if value != None:
            self.manually_set__accelerator_capabilities = True
        else:
            self.manually_set__accelerator_capabilities = False
        self.accelerator_capabilities = value

    def set_accounting_mode_enabled(self, value=None):
        if value != None:
            self.manually_set__accounting_mode_enabled = True
        else:
            self.manually_set__accounting_mode_enabled = False
        self.accounting_mode_enabled = value

    def set_accounting_mode_buffer_size(self, value=None):
        if value != None:
            self.manually_set__accounting_mode_buffer_size = True
        else:
            self.manually_set__accounting_mode_buffer_size = False
        self.accounting_mode_buffer_size = value

    def set_adapter_compatibility(self, value=None):
        if value != None:
            self.manually_set__adapter_compatibility = True
        else:
            self.manually_set__adapter_compatibility = False
        self.adapter_compatibility = value

    def set_adapter_DAC_type(self, value=None):
        if value != None:
            self.manually_set__adapter_DAC_type = True
        else:
            self.manually_set__adapter_DAC_type = False
        self.adapter_DAC_type = value

    def set_adapter_id(self, value=None):
        if value != None:
            self.manually_set__adapter_id = True
        else:
            self.manually_set__adapter_id = False
        self.adapter_id = value

    def set_adapter_index(self, value=None):
        if value != None:
            self.manually_set__adapter_index = True
        else:
            self.manually_set__adapter_index = False
        self.adapter_index = value

    def set_addressing_mode(self, value=None):
        if value != None:
            self.manually_set__addressing_mode = True
        else:
            self.manually_set__addressing_mode = False
        self.addressing_mode = value

    def set_availability(self, value=None):
        if value != None:
            self.manually_set__availability = True
        else:
            self.manually_set__availability = False
        self.availability = value

    def set_capability_descriptions(self, value=None):
        if value != None:
            self.manually_set__capability_descriptions = True
        else:
            self.manually_set__capability_descriptions = False
        self.capability_descriptions = value

    def set_caption(self, value=None):
        if value != None:
            self.manually_set__caption = True
        else:
            self.manually_set__caption = False
        self.caption = value

    def set_chip_to_chip_interconnect_mode(self, value=None):
        if value != None:
            self.manually_set__chip_to_chip_interconnect_mode = True
        else:
            self.manually_set__chip_to_chip_interconnect_mode = False
        self.chip_to_chip_interconnect_mode = value

    def set_clock_event_reasons_as_bitmap(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_as_bitmap = True
        else:
            self.manually_set__clock_event_reasons_as_bitmap = False
        self.clock_event_reasons_as_bitmap = value

    def set_clock_event_reasons_application_setting(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_application_setting = True
        else:
            self.manually_set__clock_event_reasons_application_setting = False
        self.clock_event_reasons_application_setting = value

    def set_clock_event_reasons_is_hardware_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_is_hardware_limited = True
        else:
            self.manually_set__clock_event_reasons_is_hardware_limited = False
        self.clock_event_reasons_is_hardware_limited = value

    def set_clock_event_reasons_gpu_idle_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_gpu_idle_limited = True
        else:
            self.manually_set__clock_event_reasons_gpu_idle_limited = False
        self.clock_event_reasons_gpu_idle_limited = value

    def set_clock_event_reasons_software_power_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_software_power_limited = True
        else:
            self.manually_set__clock_event_reasons_software_power_limited = False
        self.clock_event_reasons_software_power_limited = value

    def set_clock_event_reasons_software_thermal_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_software_thermal_limited = True
        else:
            self.manually_set__clock_event_reasons_software_thermal_limited = False
        self.clock_event_reasons_software_thermal_limited = value

    def set_clock_event_reasons_power_break_slowdown_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_power_break_slowdown_limited = True
        else:
            self.manually_set__clock_event_reasons_power_break_slowdown_limited = False
        self.clock_event_reasons_power_break_slowdown_limited = value

    def set_clock_event_reasons_supported(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_supported = True
        else:
            self.manually_set__clock_event_reasons_supported = False
        self.clock_event_reasons_supported = value

    def set_clock_event_reasons_sync_boost(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_sync_boost = True
        else:
            self.manually_set__clock_event_reasons_sync_boost = False
        self.clock_event_reasons_sync_boost = value

    def set_clock_event_reasons_thermal_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_thermal_limited = True
        else:
            self.manually_set__clock_event_reasons_thermal_limited = False
        self.clock_event_reasons_thermal_limited = value

    def set_color_table_entries(self, value=None):
        if value != None:
            self.manually_set__color_table_entries = True
        else:
            self.manually_set__color_table_entries = False
        self.color_table_entries = value

    def set_compute_cap(self, value=None):
        if value != None:
            self.manually_set__compute_cap = True
        else:
            self.manually_set__compute_cap = False
        self.compute_cap = value

    def set_compute_mode(self, value=None):
        if value != None:
            self.manually_set__compute_mode = True
        else:
            self.manually_set__compute_mode = False
        self.compute_mode = value

    def set_config_manager_error_code(self, value=None):
        if value != None:
            self.manually_set__config_manager_error_code = True
        else:
            self.manually_set__config_manager_error_code = False
        self.config_manager_error_code = value

    def set_config_manager_user_config(self, value=None):
        if value != None:
            self.manually_set__config_manager_user_config = True
        else:
            self.manually_set__config_manager_user_config = False
        self.config_manager_user_config = value

    def set_core_voltage(self, value=None):
        if value != None:
            self.manually_set__core_voltage = True
        else:
            self.manually_set__core_voltage = False
        self.core_voltage = value

    def set_core_voltage_range(self, value=None):
        if value != None:
            self.manually_set__core_voltage_range = True
        else:
            self.manually_set__core_voltage_range = False
        self.core_voltage_range = value

    def set_creation_class_name(self, value=None):
        if value != None:
            self.manually_set__creation_class_name = True
        else:
            self.manually_set__creation_class_name = False
        self.creation_class_name = value

    def set_current_bits_per_pixel(self, value=None):
        if value != None:
            self.manually_set__current_bits_per_pixel = True
        else:
            self.manually_set__current_bits_per_pixel = False
        self.current_bits_per_pixel = value

    def set_current_horizontal_resolution(self, value=None):
        if value != None:
            self.manually_set__current_horizontal_resolution = True
        else:
            self.manually_set__current_horizontal_resolution = False
        self.current_horizontal_resolution = value

    def set_current_number_of_colors(self, value=None):
        if value != None:
            self.manually_set__current_number_of_colors = True
        else:
            self.manually_set__current_number_of_colors = False
        self.current_number_of_colors = value

    def set_current_number_of_columns(self, value=None):
        if value != None:
            self.manually_set__current_number_of_columns = True
        else:
            self.manually_set__current_number_of_columns = False
        self.current_number_of_columns = value

    def set_current_number_of_rows(self, value=None):
        if value != None:
            self.manually_set__current_number_of_rows = True
        else:
            self.manually_set__current_number_of_rows = False
        self.current_number_of_rows = value

    def set_current_refresh_rate(self, value=None):
        if value != None:
            self.manually_set__current_refresh_rate = True
        else:
            self.manually_set__current_refresh_rate = False
        self.current_refresh_rate = value

    def set_current_scan_mode(self, value=None):
        if value != None:
            self.manually_set__current_scan_mode = True
        else:
            self.manually_set__current_scan_mode = False
        self.current_scan_mode = value

    def set_current_vertical_resolution(self, value=None):
        if value != None:
            self.manually_set__current_vertical_resolution = True
        else:
            self.manually_set__current_vertical_resolution = False
        self.current_vertical_resolution = value

    def set_description(self, value=None):
        if value != None:
            self.manually_set__description = True
        else:
            self.manually_set__description = False
        self.description = value

    def set_device_id(self, value=None):
        if value != None:
            self.manually_set__device_id = True
        else:
            self.manually_set__device_id = False
        self.device_id = value

    def set_device_specific_pens(self, value=None):
        if value != None:
            self.manually_set__device_specific_pens = True
        else:
            self.manually_set__device_specific_pens = False
        self.device_specific_pens = value

    def set_display_active(self, value=None):
        if value != None:
            self.manually_set__display_active = True
        else:
            self.manually_set__display_active = False
        self.display_active = value

    def set_display_mode(self, value=None):
        if value != None:
            self.manually_set__display_mode = True
        else:
            self.manually_set__display_mode = False
        self.display_mode = value

    def set_dither_type(self, value=None):
        if value != None:
            self.manually_set__dither_type = True
        else:
            self.manually_set__dither_type = False
        self.dither_type = value

    def set_driver_date(self, value=None):
        if value != None:
            self.manually_set__driver_date = True
        else:
            self.manually_set__driver_date = False
        self.driver_date = value

    def set_driver_model_current(self, value=None):
        if value != None:
            self.manually_set__driver_model_current = True
        else:
            self.manually_set__driver_model_current = False
        self.driver_model_current = value

    def set_driver_model_pending(self, value=None):
        if value != None:
            self.manually_set__driver_model_pending = True
        else:
            self.manually_set__driver_model_pending = False
        self.driver_model_pending = value

    def set_driver_version(self, value=None):
        if value != None:
            self.manually_set__driver_version = True
        else:
            self.manually_set__driver_version = False
        self.driver_version = value

    def set_ecc_errors_corrected_all_time_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_cbu = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_cbu = False
        self.ecc_errors_corrected_all_time_in_cbu = value

    def set_ecc_errors_corrected_all_time_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_primary_cache = False
        self.ecc_errors_corrected_all_time_in_primary_cache = value

    def set_ecc_errors_corrected_all_time_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_register_file = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_register_file = False
        self.ecc_errors_corrected_all_time_in_register_file = value

    def set_ecc_errors_corrected_all_time_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_secondary_cache = False
        self.ecc_errors_corrected_all_time_in_secondary_cache = value

    def set_ecc_errors_corrected_all_time_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_shared_memory = False
        self.ecc_errors_corrected_all_time_in_shared_memory = value

    def set_ecc_errors_corrected_all_time_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_sram = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_sram = False
        self.ecc_errors_corrected_all_time_in_sram = value

    def set_ecc_errors_corrected_all_time_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_texture_memory = False
        self.ecc_errors_corrected_all_time_in_texture_memory = value

    def set_ecc_errors_corrected_all_time_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_total = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_total = False
        self.ecc_errors_corrected_all_time_in_total = value

    def set_ecc_errors_corrected_all_time_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_video_memory = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_video_memory = False
        self.ecc_errors_corrected_all_time_in_video_memory = value

    def set_ecc_errors_corrected_since_reboot_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_cbu = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_cbu = False
        self.ecc_errors_corrected_since_reboot_in_cbu = value

    def set_ecc_errors_corrected_since_reboot_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_primary_cache = False
        self.ecc_errors_corrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_register_file = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_register_file = False
        self.ecc_errors_corrected_since_reboot_in_register_file = value

    def set_ecc_errors_corrected_since_reboot_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_secondary_cache = False
        self.ecc_errors_corrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_shared_memory = False
        self.ecc_errors_corrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_corrected_since_reboot_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_sram = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_sram = False
        self.ecc_errors_corrected_since_reboot_in_sram = value

    def set_ecc_errors_corrected_since_reboot_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_texture_memory = False
        self.ecc_errors_corrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_corrected_since_reboot_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_total = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_total = False
        self.ecc_errors_corrected_since_reboot_in_total = value

    def set_ecc_errors_corrected_since_reboot_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_video_memory = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_video_memory = False
        self.ecc_errors_corrected_since_reboot_in_video_memory = value

    def set_ecc_errors_uncorrected_all_time_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_cbu = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_cbu = False
        self.ecc_errors_uncorrected_all_time_in_cbu = value

    def set_ecc_errors_uncorrected_all_time_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_primary_cache = False
        self.ecc_errors_uncorrected_all_time_in_primary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_register_file = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_register_file = False
        self.ecc_errors_uncorrected_all_time_in_register_file = value

    def set_ecc_errors_uncorrected_all_time_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_secondary_cache = False
        self.ecc_errors_uncorrected_all_time_in_secondary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_shared_memory = False
        self.ecc_errors_uncorrected_all_time_in_shared_memory = value

    def set_ecc_errors_uncorrected_all_time_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_sram = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_sram = False
        self.ecc_errors_uncorrected_all_time_in_sram = value

    def set_ecc_errors_uncorrected_all_time_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_texture_memory = False
        self.ecc_errors_uncorrected_all_time_in_texture_memory = value

    def set_ecc_errors_uncorrected_all_time_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_total = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_total = False
        self.ecc_errors_uncorrected_all_time_in_total = value

    def set_ecc_errors_uncorrected_all_time_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_video_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_video_memory = False
        self.ecc_errors_uncorrected_all_time_in_video_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_cbu = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_cbu = False
        self.ecc_errors_uncorrected_since_reboot_in_cbu = value

    def set_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_primary_cache = False
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_register_file = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_register_file = False
        self.ecc_errors_uncorrected_since_reboot_in_register_file = value

    def set_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_secondary_cache = False
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_shared_memory = False
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_sram = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_sram = False
        self.ecc_errors_uncorrected_since_reboot_in_sram = value

    def set_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_texture_memory = False
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_total = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_total = False
        self.ecc_errors_uncorrected_since_reboot_in_total = value

    def set_ecc_errors_uncorrected_since_reboot_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_video_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_video_memory = False
        self.ecc_errors_uncorrected_since_reboot_in_video_memory = value

    def set_ecc_mode_current(self, value=None):
        if value != None:
            self.manually_set__ecc_mode_current = True
        else:
            self.manually_set__ecc_mode_current = False
        self.ecc_mode_current = value

    def set_ecc_mode_pending(self, value=None):
        if value != None:
            self.manually_set__ecc_mode_pending = True
        else:
            self.manually_set__ecc_mode_pending = False
        self.ecc_mode_pending = value

    def set_encoder_average_FPS(self, value=None):
        if value != None:
            self.manually_set__encoder_average_FPS = True
        else:
            self.manually_set__encoder_average_FPS = False
        self.encoder_average_FPS = value

    def set_encoder_average_latency(self, value=None):
        if value != None:
            self.manually_set__encoder_average_latency = True
        else:
            self.manually_set__encoder_average_latency = False
        self.encoder_average_latency = value

    def set_encoder_session_count(self, value=None):
        if value != None:
            self.manually_set__encoder_session_count = True
        else:
            self.manually_set__encoder_session_count = False
        self.encoder_session_count = value

    def set_engine_clock_range(self, value=None):
        if value != None:
            self.manually_set__engine_clock_range = True
        else:
            self.manually_set__engine_clock_range = False
        self.engine_clock_range = value

    def set_error_cleared(self, value=None):
        if value != None:
            self.manually_set__error_cleared = True
        else:
            self.manually_set__error_cleared = False
        self.error_cleared = value

    def set_error_description(self, value=None):
        if value != None:
            self.manually_set__error_description = True
        else:
            self.manually_set__error_description = False
        self.error_description = value

    def set_fabric_state(self, value=None):
        if value != None:
            self.manually_set__fabric_state = True
        else:
            self.manually_set__fabric_state = False
        self.fabric_state = value

    def set_fabric_status(self, value=None):
        if value != None:
            self.manually_set__fabric_status = True
        else:
            self.manually_set__fabric_status = False
        self.fabric_status = value

    def set_fan_speed_percentage(self, value=None):
        if value != None:
            self.manually_set__fan_speed_percentage = True
        else:
            self.manually_set__fan_speed_percentage = False
        self.fan_speed_percentage = value

    def set_fan_speed_percentage_range(self, value=None):
        if value != None:
            self.manually_set__fan_speed_percentage_range = True
        else:
            self.manually_set__fan_speed_percentage_range = False
        self.fan_speed_percentage_range = value

    def set_fan_speed_RPM(self, value=None):
        if value != None:
            self.manually_set__fan_speed_RPM = True
        else:
            self.manually_set__fan_speed_RPM = False
        self.fan_speed_RPM = value

    def set_fan_speed_RPM_range(self, value=None):
        if value != None:
            self.manually_set__fan_speed_RPM_range = True
        else:
            self.manually_set__fan_speed_RPM_range = False
        self.fan_speed_RPM_range = value

    def set_fractional_multi_vGPU(self, value=None):
        if value != None:
            self.manually_set__fractional_multi_vGPU = True
        else:
            self.manually_set__fractional_multi_vGPU = False
        self.fractional_multi_vGPU = value

    def set_frequency_application_default_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_default_shader_clock = True
        else:
            self.manually_set__frequency_application_default_shader_clock = False
        self.frequency_application_default_shader_clock = value

    def set_frequency_application_default_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_default_memory_clock = True
        else:
            self.manually_set__frequency_application_default_memory_clock = False
        self.frequency_application_default_memory_clock = value

    def set_frequency_application_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_memory_clock = True
        else:
            self.manually_set__frequency_application_memory_clock = False
        self.frequency_application_memory_clock = value

    def set_frequency_application_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_shader_clock = True
        else:
            self.manually_set__frequency_application_shader_clock = False
        self.frequency_application_shader_clock = value

    def set_frequency_maximum_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_maximum_memory_clock = True
        else:
            self.manually_set__frequency_maximum_memory_clock = False
        self.frequency_maximum_memory_clock = value

    def set_frequency_maximum_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_maximum_shader_clock = True
        else:
            self.manually_set__frequency_maximum_shader_clock = False
        self.frequency_maximum_shader_clock = value

    def set_frequency_maximum_streaming_multiprocessor_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_maximum_streaming_multiprocessor_clock = True
        else:
            self.manually_set__frequency_maximum_streaming_multiprocessor_clock = False
        self.frequency_maximum_streaming_multiprocessor_clock = value

    def set_frequency_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_memory_clock = True
        else:
            self.manually_set__frequency_memory_clock = False
        self.frequency_memory_clock = value

    def set_frequency_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_shader_clock = True
        else:
            self.manually_set__frequency_shader_clock = False
        self.frequency_shader_clock = value

    def set_frequency_streaming_multiprocessor_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_streaming_multiprocessor_clock = True
        else:
            self.manually_set__frequency_streaming_multiprocessor_clock = False
        self.frequency_streaming_multiprocessor_clock = value

    def set_frequency_video_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_video_clock = True
        else:
            self.manually_set__frequency_video_clock = False
        self.frequency_video_clock = value

    def set_heterogenous_multi_vGPU(self, value=None):
        if value != None:
            self.manually_set__heterogenous_multi_vGPU = True
        else:
            self.manually_set__heterogenous_multi_vGPU = False
        self.heterogenous_multi_vGPU = value

    def set_heterogenous_time_slice_profile(self, value=None):
        if value != None:
            self.manually_set__heterogenous_time_slice_profile = True
        else:
            self.manually_set__heterogenous_time_slice_profile = False
        self.heterogenous_time_slice_profile = value

    def set_heterogenous_time_slice_sizes(self, value=None):
        if value != None:
            self.manually_set__heterogenous_time_slice_sizes = True
        else:
            self.manually_set__heterogenous_time_slice_sizes = False
        self.heterogenous_time_slice_sizes = value

    def set_ICM_indent(self, value=None):
        if value != None:
            self.manually_set__ICM_indent = True
        else:
            self.manually_set__ICM_indent = False
        self.ICM_indent = value

    def set_ICM_method(self, value=None):
        if value != None:
            self.manually_set__ICM_method = True
        else:
            self.manually_set__ICM_method = False
        self.ICM_method = value

    def set_inf_filename(self, value=None):
        if value != None:
            self.manually_set__inf_filename = True
        else:
            self.manually_set__inf_filename = False
        self.inf_filename = value

    def set_inf_section(self, value=None):
        if value != None:
            self.manually_set__inf_section = True
        else:
            self.manually_set__inf_section = False
        self.inf_section = value

    def set_info_ROM_ecc(self, value=None):
        if value != None:
            self.manually_set__info_ROM_ecc = True
        else:
            self.manually_set__info_ROM_ecc = False
        self.info_ROM_ecc = value

    def set_info_ROM_oem(self, value=None):
        if value != None:
            self.manually_set__info_ROM_oem = True
        else:
            self.manually_set__info_ROM_oem = False
        self.info_ROM_oem = value

    def set_info_ROM_power(self, value=None):
        if value != None:
            self.manually_set__info_ROM_power = True
        else:
            self.manually_set__info_ROM_power = False
        self.info_ROM_power = value

    def set_info_ROM_version(self, value=None):
        if value != None:
            self.manually_set__info_ROM_version = True
        else:
            self.manually_set__info_ROM_version = False
        self.info_ROM_version = value

    def set_install_date(self, value=None):
        if value != None:
            self.manually_set__install_date = True
        else:
            self.manually_set__install_date = False
        self.install_date = value

    def set_installed_display_drivers(self, value=None):
        if value != None:
            self.manually_set__installed_display_drivers = True
        else:
            self.manually_set__installed_display_drivers = False
        self.installed_display_drivers = value

    def set_last_error_code(self, value=None):
        if value != None:
            self.manually_set__last_error_code = True
        else:
            self.manually_set__last_error_code = False
        self.last_error_code = value

    def set_max_memory_supported(self, value=None):
        if value != None:
            self.manually_set__max_memory_supported = True
        else:
            self.manually_set__max_memory_supported = False
        self.max_memory_supported = value

    def set_max_number_controlled(self, value=None):
        if value != None:
            self.manually_set__max_number_controlled = True
        else:
            self.manually_set__max_number_controlled = False
        self.max_number_controlled = value

    def set_max_refresh_rate(self, value=None):
        if value != None:
            self.manually_set__max_refresh_rate = True
        else:
            self.manually_set__max_refresh_rate = False
        self.max_refresh_rate = value

    def set_memory_clock_range(self, value=None):
        if value != None:
            self.manually_set__memory_clock_range = True
        else:
            self.manually_set__memory_clock_range = False
        self.memory_clock_range = value

    def set_memory_free(self, value=None):
        if value != None:
            self.manually_set__memory_free = True
        else:
            self.manually_set__memory_free = False
        self.memory_free = value

    def set_memory_reserved(self, value=None):
        if value != None:
            self.manually_set__memory_reserved = True
        else:
            self.manually_set__memory_reserved = False
        self.memory_reserved = value

    def set_memory_total(self, value=None):
        if value != None:
            self.manually_set__memory_total = True
        else:
            self.manually_set__memory_total = False
        self.memory_total = value

    def set_memory_used(self, value=None):
        if value != None:
            self.manually_set__memory_used = True
        else:
            self.manually_set__memory_used = False
        self.memory_used = value

    def set_min_refresh_rate(self, value=None):
        if value != None:
            self.manually_set__min_refresh_rate = True
        else:
            self.manually_set__min_refresh_rate = False
        self.min_refresh_rate = value

    def set_monochrome(self, value=None):
        if value != None:
            self.manually_set__monochrome = True
        else:
            self.manually_set__monochrome = False
        self.monochrome = value

    def set_multi_instance_GPU_mode_current(self, value=None):
        if value != None:
            self.manually_set__multi_instance_GPU_mode_current = True
        else:
            self.manually_set__multi_instance_GPU_mode_current = False
        self.multi_instance_GPU_mode_current = value

    def set_multi_instance_GPU_mode_pending(self, value=None):
        if value != None:
            self.manually_set__multi_instance_GPU_mode_pending = True
        else:
            self.manually_set__multi_instance_GPU_mode_pending = False
        self.multi_instance_GPU_mode_pending = value

    def set_name(self, value=None):
        if value != None:
            self.manually_set__name = True
        else:
            self.manually_set__name = False
        self.name = value

    def set_number_of_color_planes(self, value=None):
        if value != None:
            self.manually_set__number_of_color_planes = True
        else:
            self.manually_set__number_of_color_planes = False
        self.number_of_color_planes = value

    def set_number_of_video_pages(self, value=None):
        if value != None:
            self.manually_set__number_of_video_pages = True
        else:
            self.manually_set__number_of_video_pages = False
        self.number_of_video_pages = value

    def set_operating_mode_current(self, value=None):
        if value != None:
            self.manually_set__operating_mode_current = True
        else:
            self.manually_set__operating_mode_current = False
        self.operating_mode_current = value

    def set_operating_mode_pending(self, value=None):
        if value != None:
            self.manually_set__operating_mode_pending = True
        else:
            self.manually_set__operating_mode_pending = False
        self.operating_mode_pending = value

    def set_pci_bus(self, value=None):
        if value != None:
            self.manually_set__pci_bus = True
        else:
            self.manually_set__pci_bus = False
        self.pci_bus = value

    def set_pci_bus_id(self, value=None):
        if value != None:
            self.manually_set__pci_bus_id = True
        else:
            self.manually_set__pci_bus_id = False
        self.pci_bus_id = value

    def set_pci_device(self, value=None):
        if value != None:
            self.manually_set__pci_device = True
        else:
            self.manually_set__pci_device = False
        self.pci_device = value

    def set_pci_device_id(self, value=None):
        if value != None:
            self.manually_set__pci_device_id = True
        else:
            self.manually_set__pci_device_id = False
        self.pci_device_id = value

    def set_pci_domain(self, value=None):
        if value != None:
            self.manually_set__pci_domain = True
        else:
            self.manually_set__pci_domain = False
        self.pci_domain = value

    def set_pci_link_generation_current(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_current = True
        else:
            self.manually_set__pci_link_generation_current = False
        self.pci_link_generation_current = value

    def set_pci_link_generation_device_host_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_device_host_maximum = True
        else:
            self.manually_set__pci_link_generation_device_host_maximum = False
        self.pci_link_generation_device_host_maximum = value

    def set_pci_link_generation_gpu_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_gpu_maximum = True
        else:
            self.manually_set__pci_link_generation_gpu_maximum = False
        self.pci_link_generation_gpu_maximum = value

    def set_pci_link_generation_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_maximum = True
        else:
            self.manually_set__pci_link_generation_maximum = False
        self.pci_link_generation_maximum = value

    def set_pci_link_width_current(self, value=None):
        if value != None:
            self.manually_set__pci_link_width_current = True
        else:
            self.manually_set__pci_link_width_current = False
        self.pci_link_width_current = value

    def set_pci_link_width_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_width_maximum = True
        else:
            self.manually_set__pci_link_width_maximum = False
        self.pci_link_width_maximum = value

    def set_pci_sub_device_id(self, value=None):
        if value != None:
            self.manually_set__pci_sub_device_id = True
        else:
            self.manually_set__pci_sub_device_id = False
        self.pci_sub_device_id = value

    def set_persistence_mode(self, value=None):
        if value != None:
            self.manually_set__persistence_mode = True
        else:
            self.manually_set__persistence_mode = False
        self.persistence_mode = value

    def set_PNP_device_id(self, value=None):
        if value != None:
            self.manually_set__PNP_device_id = True
        else:
            self.manually_set__PNP_device_id = False
        self.PNP_device_id = value

    def set_power_draw(self, value=None):
        if value != None:
            self.manually_set__power_draw = True
        else:
            self.manually_set__power_draw = False
        self.power_draw = value

    def set_power_draw_average(self, value=None):
        if value != None:
            self.manually_set__power_draw_average = True
        else:
            self.manually_set__power_draw_average = False
        self.power_draw_average = value

    def set_power_draw_default_limit(self, value=None):
        if value != None:
            self.manually_set__power_draw_default_limit = True
        else:
            self.manually_set__power_draw_default_limit = False
        self.power_draw_default_limit = value

    def set_power_draw_enforced_limit(self, value=None):
        if value != None:
            self.manually_set__power_draw_enforced_limit = True
        else:
            self.manually_set__power_draw_enforced_limit = False
        self.power_draw_enforced_limit = value

    def set_power_draw_instant(self, value=None):
        if value != None:
            self.manually_set__power_draw_instant = True
        else:
            self.manually_set__power_draw_instant = False
        self.power_draw_instant = value

    def set_power_draw_limit(self, value=None):
        if value != None:
            self.manually_set__power_draw_limit = True
        else:
            self.manually_set__power_draw_limit = False
        self.power_draw_limit = value

    def set_power_draw_maximum(self, value=None):
        if value != None:
            self.manually_set__power_draw_maximum = True
        else:
            self.manually_set__power_draw_maximum = False
        self.power_draw_maximum = value

    def set_power_draw_minimum(self, value=None):
        if value != None:
            self.manually_set__power_draw_minimum = True
        else:
            self.manually_set__power_draw_minimum = False
        self.power_draw_minimum = value

    def set_power_management_capabilities(self, value=None):
        if value != None:
            self.manually_set__power_management_capabilities = True
        else:
            self.manually_set__power_management_capabilities = False
        self.power_management_capabilities = value

    def set_power_management_supported(self, value=None):
        if value != None:
            self.manually_set__power_management_supported = True
        else:
            self.manually_set__power_management_supported = False
        self.power_management_supported = value

    def set_protected_memory_free(self, value=None):
        if value != None:
            self.manually_set__protected_memory_free = True
        else:
            self.manually_set__protected_memory_free = False
        self.protected_memory_free = value

    def set_protected_memory_total(self, value=None):
        if value != None:
            self.manually_set__protected_memory_total = True
        else:
            self.manually_set__protected_memory_total = False
        self.protected_memory_total = value

    def set_protected_memory_used(self, value=None):
        if value != None:
            self.manually_set__protected_memory_used = True
        else:
            self.manually_set__protected_memory_used = False
        self.protected_memory_used = value

    def set_protocol_supported(self, value=None):
        if value != None:
            self.manually_set__protocol_supported = True
        else:
            self.manually_set__protocol_supported = False
        self.protocol_supported = value

    def set_performance_state(self, value=None):
        if value != None:
            self.manually_set__performance_state = True
        else:
            self.manually_set__performance_state = False
        self.performance_state = value

    def set_retired_pages_double_bit_ecc_errors_count(self, value=None):
        if value != None:
            self.manually_set__retired_pages_double_bit_ecc_errors_count = True
        else:
            self.manually_set__retired_pages_double_bit_ecc_errors_count = False
        self.retired_pages_double_bit_ecc_errors_count = value

    def set_retired_pages_single_bit_ecc_errors_count(self, value=None):
        if value != None:
            self.manually_set__retired_pages_single_bit_ecc_errors_count = True
        else:
            self.manually_set__retired_pages_single_bit_ecc_errors_count = False
        self.retired_pages_single_bit_ecc_errors_count = value

    def set_retired_pages_pending(self, value=None):
        if value != None:
            self.manually_set__retired_pages_pending = True
        else:
            self.manually_set__retired_pages_pending = False
        self.retired_pages_pending = value

    def set_reserved_system_palette_entries(self, value=None):
        if value != None:
            self.manually_set__reserved_system_palette_entries = True
        else:
            self.manually_set__reserved_system_palette_entries = False
        self.reserved_system_palette_entries = value

    def set_reset_required(self, value=None):
        if value != None:
            self.manually_set__reset_required = True
        else:
            self.manually_set__reset_required = False
        self.reset_required = value

    def set_reset_and_drain_recommended(self, value=None):
        if value != None:
            self.manually_set__reset_and_drain_recommended = True
        else:
            self.manually_set__reset_and_drain_recommended = False
        self.reset_and_drain_recommended = value

    def set_serial(self, value=None):
        if value != None:
            self.manually_set__serial = True
        else:
            self.manually_set__serial = False
        self.serial = value

    def set_specification_version(self, value=None):
        if value != None:
            self.manually_set__specification_version = True
        else:
            self.manually_set__specification_version = False
        self.specification_version = value

    def set_status(self, value=None):
        if value != None:
            self.manually_set__status = True
        else:
            self.manually_set__status = False
        self.status = value

    def set_status_info(self, value=None):
        if value != None:
            self.manually_set__status_info = True
        else:
            self.manually_set__status_info = False
        self.status_info = value

    def set_system_creation_class_name(self, value=None):
        if value != None:
            self.manually_set__system_creation_class_name = True
        else:
            self.manually_set__system_creation_class_name = False
        self.system_creation_class_name = value

    def set_system_name(self, value=None):
        if value != None:
            self.manually_set__system_name = True
        else:
            self.manually_set__system_name = False
        self.system_name = value

    def set_system_palette_entries(self, value=None):
        if value != None:
            self.manually_set__system_palette_entries = True
        else:
            self.manually_set__system_palette_entries = False
        self.system_palette_entries = value

    def set_GPU_system_processor_mode_current(self, value=None):
        if value != None:
            self.manually_set__GPU_system_processor_mode_current = True
        else:
            self.manually_set__GPU_system_processor_mode_current = False
        self.GPU_system_processor_mode_current = value

    def set_GPU_system_processor_mode_default(self, value=None):
        if value != None:
            self.manually_set__GPU_system_processor_mode_default = True
        else:
            self.manually_set__GPU_system_processor_mode_default = False
        self.GPU_system_processor_mode_default = value

    def set_temperature_core(self, value=None):
        if value != None:
            self.manually_set__temperature_core = True
        else:
            self.manually_set__temperature_core = False
        self.temperature_core = value

    def set_temperature_core_limit(self, value=None):
        if value != None:
            self.manually_set__temperature_core_limit = True
        else:
            self.manually_set__temperature_core_limit = False
        self.temperature_core_limit = value

    def set_temperature_memory(self, value=None):
        if value != None:
            self.manually_set__temperature_memory = True
        else:
            self.manually_set__temperature_memory = False
        self.temperature_memory = value

    def set_time_of_last_reset(self, value=None):
        if value != None:
            self.manually_set__time_of_last_reset = True
        else:
            self.manually_set__time_of_last_reset = False
        self.time_of_last_reset = value

    def set_utilization_decoder(self, value=None):
        if value != None:
            self.manually_set__utilization_decoder = True
        else:
            self.manually_set__utilization_decoder = False
        self.utilization_decoder = value

    def set_utilization_encoder(self, value=None):
        if value != None:
            self.manually_set__utilization_encoder = True
        else:
            self.manually_set__utilization_encoder = False
        self.utilization_encoder = value

    def set_utilization_gpu(self, value=None):
        if value != None:
            self.manually_set__utilization_gpu = True
        else:
            self.manually_set__utilization_gpu = False
        self.utilization_gpu = value

    def set_utilization_jpeg(self, value=None):
        if value != None:
            self.manually_set__utilization_jpeg = True
        else:
            self.manually_set__utilization_jpeg = False
        self.utilization_jpeg = value

    def set_utilization_memory(self, value=None):
        if value != None:
            self.manually_set__utilization_memory = True
        else:
            self.manually_set__utilization_memory = False
        self.utilization_memory = value

    def set_utilization_optical_flow(self, value=None):
        if value != None:
            self.manually_set__utilization_optical_flow = True
        else:
            self.manually_set__utilization_optical_flow = False
        self.utilization_optical_flow = value

    def set_uuid(self, value=None):
        if value != None:
            self.manually_set__uuid = True
        else:
            self.manually_set__uuid = False
        self.uuid = value

    def set_vbios_version(self, value=None):
        if value != None:
            self.manually_set__vbios_version = True
        else:
            self.manually_set__vbios_version = False
        self.vbios_version = value

    def set_video_architecture(self, value=None):
        if value != None:
            self.manually_set__video_architecture = True
        else:
            self.manually_set__video_architecture = False
        self.video_architecture = value

    def set_video_memory_type(self, value=None):
        if value != None:
            self.manually_set__video_memory_type = True
        else:
            self.manually_set__video_memory_type = False
        self.video_memory_type = value

    def set_video_mode(self, value=None):
        if value != None:
            self.manually_set__video_mode = True
        else:
            self.manually_set__video_mode = False
        self.video_mode = value

    def set_video_mode_description(self, value=None):
        if value != None:
            self.manually_set__video_mode_description = True
        else:
            self.manually_set__video_mode_description = False
        self.video_mode_description = value

    def set_video_processor(self, value=None):
        if value != None:
            self.manually_set__video_processor = True
        else:
            self.manually_set__video_processor = False
        self.video_processor = value

    def update_accelerator_capabilities(self):
        return self.accelerator_capabilities

    def update_accounting_mode_enabled(self):
            return self.accounting_mode_enabled

    def update_accounting_mode_buffer_size(self):
            return self.accounting_mode_buffer_size

    def update_adapter_compatibility(self):
            return self.adapter_compatibility

    def update_adapter_DAC_type(self):
            return self.adapter_DAC_type

    def update_adapter_id(self):
            return self.adapter_id

    def update_adapter_index(self):
            return self.adapter_index

    def update_addressing_mode(self):
            return self.addressing_mode

    def update_availability(self):
            return self.availability

    def update_capability_descriptions(self):
            return self.capability_descriptions

    def update_caption(self):
            return self.caption

    def update_chip_to_chip_interconnect_mode(self):
            return self.chip_to_chip_interconnect_mode

    def update_clock_event_reasons_as_bitmap(self):
            return self.clock_event_reasons_as_bitmap

    def update_clock_event_reasons_application_updateting(self):
            return self.clock_event_reasons_application_updateting

    def update_clock_event_reasons_is_hardware_limited(self):
            return self.clock_event_reasons_is_hardware_limited

    def update_clock_event_reasons_gpu_idle_limited(self):
            return self.clock_event_reasons_gpu_idle_limited

    def update_clock_event_reasons_software_power_limited(self):
            return self.clock_event_reasons_software_power_limited

    def update_clock_event_reasons_software_thermal_limited(self):
            return self.clock_event_reasons_software_thermal_limited

    def update_clock_event_reasons_power_break_slowdown_limited(self):
            return self.clock_event_reasons_power_break_slowdown_limited

    def update_clock_event_reasons_supported(self):
            return self.clock_event_reasons_supported

    def update_clock_event_reasons_sync_boost(self):
            return self.clock_event_reasons_sync_boost

    def update_clock_event_reasons_thermal_limited(self):
            return self.clock_event_reasons_thermal_limited

    def update_color_table_entries(self):
            return self.color_table_entries

    def update_compute_cap(self):
            return self.compute_cap

    def update_compute_mode(self):
            return self.compute_mode

    def update_config_manager_error_code(self):
            return self.config_manager_error_code

    def update_config_manager_user_config(self):
            return self.config_manager_user_config

    def update_core_voltage(self):
            return self.core_voltage

    def update_core_voltage_range(self):
            return self.core_voltage_range

    def update_creation_class_name(self):
            return self.creation_class_name

    def update_current_bits_per_pixel(self):
            return self.current_bits_per_pixel

    def update_current_horizontal_resolution(self):
            return self.current_horizontal_resolution

    def update_current_number_of_colors(self):
            return self.current_number_of_colors

    def update_current_number_of_columns(self):
            return self.current_number_of_columns

    def update_current_number_of_rows(self):
            return self.current_number_of_rows

    def update_current_refresh_rate(self):
            return self.current_refresh_rate

    def update_current_scan_mode(self):
            return self.current_scan_mode

    def update_current_vertical_resolution(self):
            return self.current_vertical_resolution

    def update_description(self):
            return self.description

    def update_device_id(self):
            return self.device_id

    def update_device_specific_pens(self):
            return self.device_specific_pens

    def update_display_active(self):
            return self.display_active

    def update_display_mode(self):
            return self.display_mode

    def update_dither_type(self):
            return self.dither_type

    def update_driver_date(self):
            return self.driver_date

    def update_driver_model_current(self):
            return self.driver_model_current

    def update_driver_model_pending(self):
            return self.driver_model_pending

    def update_driver_version(self):
            return self.driver_version

    def update_ecc_errors_corrected_all_time_in_cbu(self):
            return self.ecc_errors_corrected_all_time_in_cbu

    def update_ecc_errors_corrected_all_time_in_primary_cache(self):
            return self.ecc_errors_corrected_all_time_in_primary_cache

    def update_ecc_errors_corrected_all_time_in_register_file(self):
            return self.ecc_errors_corrected_all_time_in_register_file

    def update_ecc_errors_corrected_all_time_in_secondary_cache(self):
            return self.ecc_errors_corrected_all_time_in_secondary_cache

    def update_ecc_errors_corrected_all_time_in_shared_memory(self):
            return self.ecc_errors_corrected_all_time_in_shared_memory

    def update_ecc_errors_corrected_all_time_in_sram(self):
            return self.ecc_errors_corrected_all_time_in_sram

    def update_ecc_errors_corrected_all_time_in_texture_memory(self):
            return self.ecc_errors_corrected_all_time_in_texture_memory

    def update_ecc_errors_corrected_all_time_in_total(self):
            return self.ecc_errors_corrected_all_time_in_total

    def update_ecc_errors_corrected_all_time_in_video_memory(self):
            return self.ecc_errors_corrected_all_time_in_video_memory

    def update_ecc_errors_corrected_since_reboot_in_cbu(self):
            return self.ecc_errors_corrected_since_reboot_in_cbu

    def update_ecc_errors_corrected_since_reboot_in_primary_cache(self):
            return self.ecc_errors_corrected_since_reboot_in_primary_cache

    def update_ecc_errors_corrected_since_reboot_in_register_file(self):
            return self.ecc_errors_corrected_since_reboot_in_register_file

    def update_ecc_errors_corrected_since_reboot_in_secondary_cache(self):
            return self.ecc_errors_corrected_since_reboot_in_secondary_cache

    def update_ecc_errors_corrected_since_reboot_in_shared_memory(self):
            return self.ecc_errors_corrected_since_reboot_in_shared_memory

    def update_ecc_errors_corrected_since_reboot_in_sram(self):
            return self.ecc_errors_corrected_since_reboot_in_sram

    def update_ecc_errors_corrected_since_reboot_in_texture_memory(self):
            return self.ecc_errors_corrected_since_reboot_in_texture_memory

    def update_ecc_errors_corrected_since_reboot_in_total(self):
            return self.ecc_errors_corrected_since_reboot_in_total

    def update_ecc_errors_corrected_since_reboot_in_video_memory(self):
            return self.ecc_errors_corrected_since_reboot_in_video_memory

    def update_ecc_errors_uncorrected_all_time_in_cbu(self):
            return self.ecc_errors_uncorrected_all_time_in_cbu

    def update_ecc_errors_uncorrected_all_time_in_primary_cache(self):
            return self.ecc_errors_uncorrected_all_time_in_primary_cache

    def update_ecc_errors_uncorrected_all_time_in_register_file(self):
            return self.ecc_errors_uncorrected_all_time_in_register_file

    def update_ecc_errors_uncorrected_all_time_in_secondary_cache(self):
            return self.ecc_errors_uncorrected_all_time_in_secondary_cache

    def update_ecc_errors_uncorrected_all_time_in_shared_memory(self):
            return self.ecc_errors_uncorrected_all_time_in_shared_memory

    def update_ecc_errors_uncorrected_all_time_in_sram(self):
            return self.ecc_errors_uncorrected_all_time_in_sram

    def update_ecc_errors_uncorrected_all_time_in_texture_memory(self):
            return self.ecc_errors_uncorrected_all_time_in_texture_memory

    def update_ecc_errors_uncorrected_all_time_in_total(self):
            return self.ecc_errors_uncorrected_all_time_in_total

    def update_ecc_errors_uncorrected_all_time_in_video_memory(self):
            return self.ecc_errors_uncorrected_all_time_in_video_memory

    def update_ecc_errors_uncorrected_since_reboot_in_cbu(self):
            return self.ecc_errors_uncorrected_since_reboot_in_cbu

    def update_ecc_errors_uncorrected_since_reboot_in_primary_cache(self):
            return self.ecc_errors_uncorrected_since_reboot_in_primary_cache

    def update_ecc_errors_uncorrected_since_reboot_in_register_file(self):
            return self.ecc_errors_uncorrected_since_reboot_in_register_file

    def update_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self):
            return self.ecc_errors_uncorrected_since_reboot_in_secondary_cache

    def update_ecc_errors_uncorrected_since_reboot_in_shared_memory(self):
            return self.ecc_errors_uncorrected_since_reboot_in_shared_memory

    def update_ecc_errors_uncorrected_since_reboot_in_sram(self):
            return self.ecc_errors_uncorrected_since_reboot_in_sram

    def update_ecc_errors_uncorrected_since_reboot_in_texture_memory(self):
            return self.ecc_errors_uncorrected_since_reboot_in_texture_memory

    def update_ecc_errors_uncorrected_since_reboot_in_total(self):
            return self.ecc_errors_uncorrected_since_reboot_in_total

    def update_ecc_errors_uncorrected_since_reboot_in_video_memory(self):
            return self.ecc_errors_uncorrected_since_reboot_in_video_memory

    def update_ecc_mode_current(self):
            return self.ecc_mode_current

    def update_ecc_mode_pending(self):
            return self.ecc_mode_pending

    def update_encoder_average_FPS(self):
            return self.encoder_average_FPS

    def update_encoder_average_latency(self):
            return self.encoder_average_latency

    def update_encoder_session_count(self):
            return self.encoder_session_count

    def update_engine_clock_range(self):
            return self.engine_clock_range

    def update_error_cleared(self):
            return self.error_cleared

    def update_error_description(self):
            return self.error_description

    def update_fabric_state(self):
            return self.fabric_state

    def update_fabric_status(self):
            return self.fabric_status

    def update_fan_speed_percentage(self):
            return self.fan_speed_percentage

    def update_fan_speed_percentage_range(self):
            return self.fan_speed_percentage_range

    def update_fan_speed_RPM(self):
            return self.fan_speed_RPM

    def update_fan_speed_RPM_range(self):
            return self.fan_speed_RPM_range

    def update_fractional_multi_vGPU(self):
            return self.fractional_multi_vGPU

    def update_frequency_application_default_shader_clock(self):
            return self.frequency_application_default_shader_clock

    def update_frequency_application_default_memory_clock(self):
            return self.frequency_application_default_memory_clock

    def update_frequency_application_memory_clock(self):
            return self.frequency_application_memory_clock

    def update_frequency_application_shader_clock(self):
            return self.frequency_application_shader_clock

    def update_frequency_maximum_memory_clock(self):
            return self.frequency_maximum_memory_clock

    def update_frequency_maximum_shader_clock(self):
            return self.frequency_maximum_shader_clock

    def update_frequency_maximum_streaming_multiprocessor_clock(self):
            return self.frequency_maximum_streaming_multiprocessor_clock

    def update_frequency_memory_clock(self):
            return self.frequency_memory_clock

    def update_frequency_shader_clock(self):
            return self.frequency_shader_clock

    def update_frequency_streaming_multiprocessor_clock(self):
            return self.frequency_streaming_multiprocessor_clock

    def update_frequency_video_clock(self):
            return self.frequency_video_clock

    def update_heterogenous_multi_vGPU(self):
            return self.heterogenous_multi_vGPU

    def update_heterogenous_time_slice_profile(self):
            return self.heterogenous_time_slice_profile

    def update_heterogenous_time_slice_sizes(self):
            return self.heterogenous_time_slice_sizes

    def update_ICM_indent(self):
            return self.ICM_indent

    def update_ICM_method(self):
            return self.ICM_method

    def update_inf_filename(self):
            return self.inf_filename

    def update_inf_section(self):
            return self.inf_section

    def update_info_ROM_ecc(self):
            return self.info_ROM_ecc

    def update_info_ROM_oem(self):
            return self.info_ROM_oem

    def update_info_ROM_power(self):
            return self.info_ROM_power

    def update_info_ROM_version(self):
            return self.info_ROM_version

    def update_install_date(self):
            return self.install_date

    def update_installed_display_drivers(self):
            return self.installed_display_drivers

    def update_last_error_code(self):
            return self.last_error_code

    def update_max_memory_supported(self):
            return self.max_memory_supported

    def update_max_number_controlled(self):
            return self.max_number_controlled

    def update_max_refresh_rate(self):
            return self.max_refresh_rate

    def update_memory_clock_range(self):
            return self.memory_clock_range

    def update_memory_free(self):
            return self.memory_free

    def update_memory_reserved(self):
            return self.memory_reserved

    def update_memory_total(self):
            return self.memory_total

    def update_memory_used(self):
            return self.memory_used

    def update_min_refresh_rate(self):
            return self.min_refresh_rate

    def update_monochrome(self):
            return self.monochrome

    def update_multi_instance_GPU_mode_current(self):
            return self.multi_instance_GPU_mode_current

    def update_multi_instance_GPU_mode_pending(self):
            return self.multi_instance_GPU_mode_pending

    def update_name(self):
            return self.name

    def update_number_of_color_planes(self):
            return self.number_of_color_planes

    def update_number_of_video_pages(self):
            return self.number_of_video_pages

    def update_operating_mode_current(self):
            return self.operating_mode_current

    def update_operating_mode_pending(self):
            return self.operating_mode_pending

    def update_pci_bus(self):
            return self.pci_bus

    def update_pci_bus_id(self):
            return self.pci_bus_id

    def update_pci_device(self):
            return self.pci_device

    def update_pci_device_id(self):
            return self.pci_device_id

    def update_pci_domain(self):
            return self.pci_domain

    def update_pci_link_generation_current(self):
            return self.pci_link_generation_current

    def update_pci_link_generation_device_host_maximum(self):
            return self.pci_link_generation_device_host_maximum

    def update_pci_link_generation_gpu_maximum(self):
            return self.pci_link_generation_gpu_maximum

    def update_pci_link_generation_maximum(self):
            return self.pci_link_generation_maximum

    def update_pci_link_width_current(self):
            return self.pci_link_width_current

    def update_pci_link_width_maximum(self):
            return self.pci_link_width_maximum

    def update_pci_sub_device_id(self):
            return self.pci_sub_device_id

    def update_persistence_mode(self):
            return self.persistence_mode

    def update_PNP_device_id(self):
            return self.PNP_device_id

    def update_power_draw(self):
            return self.power_draw

    def update_power_draw_average(self):
            return self.power_draw_average

    def update_power_draw_default_limit(self):
            return self.power_draw_default_limit

    def update_power_draw_enforced_limit(self):
            return self.power_draw_enforced_limit

    def update_power_draw_instant(self):
            return self.power_draw_instant

    def update_power_draw_limit(self):
            return self.power_draw_limit

    def update_power_draw_maximum(self):
            return self.power_draw_maximum

    def update_power_draw_minimum(self):
            return self.power_draw_minimum

    def update_power_management_capabilities(self):
            return self.power_management_capabilities

    def update_power_management_supported(self):
            return self.power_management_supported

    def update_protected_memory_free(self):
            return self.protected_memory_free

    def update_protected_memory_total(self):
            return self.protected_memory_total

    def update_protected_memory_used(self):
            return self.protected_memory_used

    def update_protocol_supported(self):
            return self.protocol_supported

    def update_performance_state(self):
            return self.performance_state

    def update_retired_pages_double_bit_ecc_errors_count(self):
            return self.retired_pages_double_bit_ecc_errors_count

    def update_retired_pages_single_bit_ecc_errors_count(self):
            return self.retired_pages_single_bit_ecc_errors_count

    def update_retired_pages_pending(self):
            return self.retired_pages_pending

    def update_reserved_system_palette_entries(self):
            return self.reserved_system_palette_entries

    def update_reset_required(self):
            return self.reset_required

    def update_reset_and_drain_recommended(self):
            return self.reset_and_drain_recommended

    def update_serial(self):
            return self.serial

    def update_specification_version(self):
            return self.specification_version

    def update_status(self):
            return self.status

    def update_status_info(self):
            return self.status_info

    def update_system_creation_class_name(self):
            return self.system_creation_class_name

    def update_system_name(self):
            return self.system_name

    def update_system_palette_entries(self):
            return self.system_palette_entries

    def update_GPU_system_processor_mode_current(self):
            return self.GPU_system_processor_mode_current

    def update_GPU_system_processor_mode_default(self):
            return self.GPU_system_processor_mode_default

    def update_temperature_core(self):
            return self.temperature_core

    def update_temperature_core_limit(self):
            return self.temperature_core_limit

    def update_temperature_memory(self):
            return self.temperature_memory

    def update_time_of_last_reset(self):
            return self.time_of_last_reset

    def update_utilization_decoder(self):
            return self.utilization_decoder

    def update_utilization_encoder(self):
            return self.utilization_encoder

    def update_utilization_gpu(self):
            return self.utilization_gpu

    def update_utilization_jpeg(self):
            return self.utilization_jpeg

    def update_utilization_memory(self):
            return self.utilization_memory

    def update_utilization_optical_flow(self):
            return self.utilization_optical_flow

    def update_uuid(self):
            return self.uuid

    def update_vbios_version(self):
            return self.vbios_version

    def update_video_architecture(self):
            return self.video_architecture

    def update_video_memory_type(self):
            return self.video_memory_type

    def update_video_mode(self):
            return self.video_mode

    def update_video_mode_description(self):
            return self.video_mode_description

    def update_video_processor(self):
            return self.video_processor
