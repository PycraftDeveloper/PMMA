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

        self.accelerator_capabilities = None
        self.accounting_mode_enabled = None
        self.accounting_mode_buffer_size = None
        self.adapter_compatibility = None
        self.adapter_DAC_type = None
        self.adapter_id = None
        self.adapter_index = None
        self.addressing_mode = None
        self.availability = None
        self.capability_descriptions = None
        self.caption = None
        self.chip_to_chip_interconnect_mode = None
        self.clock_event_reasons_as_bitmap = None
        self.clock_event_reasons_application_setting = None
        self.clock_event_reasons_is_hardware_limited = None
        self.clock_event_reasons_gpu_idle_limited = None
        self.clock_event_reasons_software_power_limited = None
        self.clock_event_reasons_software_thermal_limited = None
        self.clock_event_reasons_power_break_slowdown_limited = None
        self.clock_event_reasons_supported = None
        self.clock_event_reasons_sync_boost = None
        self.clock_event_reasons_thermal_limited = None
        self.color_table_entries = None
        self.compute_cap = None
        self.compute_mode = None
        self.config_manager_error_code = None
        self.config_manager_user_config = None
        self.core_voltage = None
        self.core_voltage_range = None
        self.creation_class_name = None
        self.current_bits_per_pixel = None
        self.current_horizontal_resolution = None
        self.current_number_of_colors = None
        self.current_number_of_columns = None
        self.current_number_of_rows = None
        self.current_refresh_rate = None
        self.current_scan_mode = None
        self.current_vertical_resolution = None
        self.description = None
        self.device_id = None
        self.device_specific_pens = None
        self.display_active = None
        self.display_mode = None
        self.dither_type = None
        self.driver_date = None
        self.driver_model_current = None
        self.driver_model_pending = None
        self.driver_version = None
        self.ecc_errors_corrected_all_time_in_cbu = None
        self.ecc_errors_corrected_all_time_in_primary_cache = None
        self.ecc_errors_corrected_all_time_in_register_file = None
        self.ecc_errors_corrected_all_time_in_secondary_cache = None
        self.ecc_errors_corrected_all_time_in_shared_memory = None
        self.ecc_errors_corrected_all_time_in_sram = None
        self.ecc_errors_corrected_all_time_in_texture_memory = None
        self.ecc_errors_corrected_all_time_in_total = None
        self.ecc_errors_corrected_all_time_in_video_memory = None
        self.ecc_errors_corrected_since_reboot_in_cbu = None
        self.ecc_errors_corrected_since_reboot_in_primary_cache = None
        self.ecc_errors_corrected_since_reboot_in_register_file = None
        self.ecc_errors_corrected_since_reboot_in_secondary_cache = None
        self.ecc_errors_corrected_since_reboot_in_shared_memory = None
        self.ecc_errors_corrected_since_reboot_in_sram = None
        self.ecc_errors_corrected_since_reboot_in_texture_memory = None
        self.ecc_errors_corrected_since_reboot_in_total = None
        self.ecc_errors_corrected_since_reboot_in_video_memory = None
        self.ecc_errors_uncorrected_all_time_in_cbu = None
        self.ecc_errors_uncorrected_all_time_in_primary_cache = None
        self.ecc_errors_uncorrected_all_time_in_register_file = None
        self.ecc_errors_uncorrected_all_time_in_secondary_cache = None
        self.ecc_errors_uncorrected_all_time_in_shared_memory = None
        self.ecc_errors_uncorrected_all_time_in_sram = None
        self.ecc_errors_uncorrected_all_time_in_texture_memory = None
        self.ecc_errors_uncorrected_all_time_in_total = None
        self.ecc_errors_uncorrected_all_time_in_video_memory = None
        self.ecc_errors_uncorrected_since_reboot_in_cbu = None
        self.ecc_errors_uncorrected_since_reboot_in_primary_cache = None
        self.ecc_errors_uncorrected_since_reboot_in_register_file = None
        self.ecc_errors_uncorrected_since_reboot_in_secondary_cache = None
        self.ecc_errors_uncorrected_since_reboot_in_shared_memory = None
        self.ecc_errors_uncorrected_since_reboot_in_sram = None
        self.ecc_errors_uncorrected_since_reboot_in_texture_memory = None
        self.ecc_errors_uncorrected_since_reboot_in_total = None
        self.ecc_errors_uncorrected_since_reboot_in_video_memory = None
        self.ecc_mode_current = None
        self.ecc_mode_pending = None
        self.encoder_average_FPS = None
        self.encoder_average_latency = None
        self.encoder_session_count = None
        self.engine_clock_range = None
        self.error_cleared = None
        self.error_description = None
        self.fabric_state = None
        self.fabric_status = None
        self.fan_speed_percentage = None
        self.fan_speed_percentage_range = None
        self.fan_speed_RPM = None
        self.fan_speed_RPM_range = None
        self.fractional_multi_vGPU = None
        self.frequency_application_default_shader_clock = None
        self.frequency_application_default_memory_clock = None
        self.frequency_application_memory_clock = None
        self.frequency_application_shader_clock = None
        self.frequency_maximum_memory_clock = None
        self.frequency_maximum_shader_clock = None
        self.frequency_maximum_streaming_multiprocessor_clock = None
        self.frequency_memory_clock = None
        self.frequency_shader_clock = None
        self.frequency_streaming_multiprocessor_clock = None
        self.frequency_video_clock = None
        self.heterogenous_multi_vGPU = None
        self.heterogenous_time_slice_profile = None
        self.heterogenous_time_slice_sizes = None
        self.ICM_indent = None
        self.ICM_method = None
        self.inf_filename = None
        self.inf_section = None
        self.info_ROM_ecc = None
        self.info_ROM_oem = None
        self.info_ROM_power = None
        self.info_ROM_version = None
        self.install_date = None
        self.installed_display_drivers = None
        self.last_error_code = None
        self.max_memory_supported = None
        self.max_number_controlled = None
        self.max_refresh_rate = None
        self.memory_clock_range = None
        self.memory_free = None
        self.memory_reserved = None
        self.memory_total = None
        self.memory_used = None
        self.min_refresh_rate = None
        self.monochrome = None
        self.multi_instance_GPU_mode_current = None
        self.multi_instance_GPU_mode_pending = None
        self.name = None
        self.number_of_color_planes = None
        self.number_of_video_pages = None
        self.operating_mode_current = None
        self.operating_mode_pending = None
        self.pci_bus = None
        self.pci_bus_id = None
        self.pci_device = None
        self.pci_device_id = None
        self.pci_domain = None
        self.pci_link_generation_current = None
        self.pci_link_generation_device_host_maximum = None
        self.pci_link_generation_gpu_maximum = None
        self.pci_link_generation_maximum = None
        self.pci_link_width_current = None
        self.pci_link_width_maximum = None
        self.pci_sub_device_id = None
        self.persistence_mode = None
        self.PNP_device_id = None
        self.power_draw = None
        self.power_draw_average = None
        self.power_draw_default_limit = None
        self.power_draw_enforced_limit = None
        self.power_draw_instant = None
        self.power_draw_limit = None
        self.power_draw_maximum = None
        self.power_draw_minimum = None
        self.power_management_capabilities = None
        self.power_management_supported = None
        self.protected_memory_free = None
        self.protected_memory_total = None
        self.protected_memory_used = None
        self.protocol_supported = None
        self.performance_state = None
        self.retired_pages_double_bit_ecc_errors_count = None
        self.retired_pages_single_bit_ecc_errors_count = None
        self.retired_pages_pending = None
        self.reserved_system_palette_entries = None
        self.reset_required = None
        self.reset_and_drain_recommended = None
        self.serial = None
        self.specification_version = None
        self.status = None
        self.status_info = None
        self.system_creation_class_name = None
        self.system_name = None
        self.system_palette_entries = None
        self.GPU_system_processor_mode_current = None
        self.GPU_system_processor_mode_default = None
        self.temperature_core = None
        self.temperature_core_limit = None
        self.temperature_memory = None
        self.time_of_last_reset = None
        self.utilization_decoder = None
        self.utilization_encoder = None
        self.utilization_gpu = None
        self.utilization_jpeg = None
        self.utilization_memory = None
        self.utilization_optical_flow = None
        self.uuid = None
        self.vbios_version = None
        self.video_architecture = None
        self.video_memory_type = None
        self.video_mode = None
        self.video_mode_description = None
        self.video_processor = None


        self.manually_set__accelerator_capabilities = False
        self.manually_set__accounting_mode_enabled = False
        self.manually_set__accounting_mode_buffer_size = False
        self.manually_set__adapter_compatibility = False
        self.manually_set__adapter_DAC_type = False
        self.manually_set__adapter_id = False
        self.manually_set__adapter_index = False
        self.manually_set__addressing_mode = False
        self.manually_set__availability = False
        self.manually_set__capability_descriptions = False
        self.manually_set__caption = False
        self.manually_set__chip_to_chip_interconnect_mode = False
        self.manually_set__clock_event_reasons_as_bitmap = False
        self.manually_set__clock_event_reasons_application_setting = False
        self.manually_set__clock_event_reasons_is_hardware_limited = False
        self.manually_set__clock_event_reasons_gpu_idle_limited = False
        self.manually_set__clock_event_reasons_software_power_limited = False
        self.manually_set__clock_event_reasons_software_thermal_limited = False
        self.manually_set__clock_event_reasons_power_break_slowdown_limited = False
        self.manually_set__clock_event_reasons_supported = False
        self.manually_set__clock_event_reasons_sync_boost = False
        self.manually_set__clock_event_reasons_thermal_limited = False
        self.manually_set__color_table_entries = False
        self.manually_set__compute_cap = False
        self.manually_set__compute_mode = False
        self.manually_set__config_manager_error_code = False
        self.manually_set__config_manager_user_config = False
        self.manually_set__core_voltage = False
        self.manually_set__core_voltage_range = False
        self.manually_set__creation_class_name = False
        self.manually_set__current_bits_per_pixel = False
        self.manually_set__current_horizontal_resolution = False
        self.manually_set__current_number_of_colors = False
        self.manually_set__current_number_of_columns = False
        self.manually_set__current_number_of_rows = False
        self.manually_set__current_refresh_rate = False
        self.manually_set__current_scan_mode = False
        self.manually_set__current_vertical_resolution = False
        self.manually_set__description = False
        self.manually_set__device_id = False
        self.manually_set__device_specific_pens = False
        self.manually_set__display_active = False
        self.manually_set__display_mode = False
        self.manually_set__dither_type = False
        self.manually_set__driver_date = False
        self.manually_set__driver_model_current = False
        self.manually_set__driver_model_pending = False
        self.manually_set__driver_version = False
        self.manually_set__ecc_errors_corrected_all_time_in_cbu = False
        self.manually_set__ecc_errors_corrected_all_time_in_primary_cache = False
        self.manually_set__ecc_errors_corrected_all_time_in_register_file = False
        self.manually_set__ecc_errors_corrected_all_time_in_secondary_cache = False
        self.manually_set__ecc_errors_corrected_all_time_in_shared_memory = False
        self.manually_set__ecc_errors_corrected_all_time_in_sram = False
        self.manually_set__ecc_errors_corrected_all_time_in_texture_memory = False
        self.manually_set__ecc_errors_corrected_all_time_in_total = False
        self.manually_set__ecc_errors_corrected_all_time_in_video_memory = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_cbu = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_primary_cache = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_register_file = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_secondary_cache = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_shared_memory = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_sram = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_texture_memory = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_total = False
        self.manually_set__ecc_errors_corrected_since_reboot_in_video_memory = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_cbu = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_primary_cache = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_register_file = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_secondary_cache = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_shared_memory = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_sram = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_texture_memory = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_total = False
        self.manually_set__ecc_errors_uncorrected_all_time_in_video_memory = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_cbu = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_primary_cache = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_register_file = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_secondary_cache = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_shared_memory = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_sram = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_texture_memory = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_total = False
        self.manually_set__ecc_errors_uncorrected_since_reboot_in_video_memory = False
        self.manually_set__ecc_mode_current = False
        self.manually_set__ecc_mode_pending = False
        self.manually_set__encoder_average_FPS = False
        self.manually_set__encoder_average_latency = False
        self.manually_set__encoder_session_count = False
        self.manually_set__engine_clock_range = False
        self.manually_set__error_cleared = False
        self.manually_set__error_description = False
        self.manually_set__fabric_state = False
        self.manually_set__fabric_status = False
        self.manually_set__fan_speed_percentage = False
        self.manually_set__fan_speed_percentage_range = False
        self.manually_set__fan_speed_RPM = False
        self.manually_set__fan_speed_RPM_range = False
        self.manually_set__fractional_multi_vGPU = False
        self.manually_set__frequency_application_default_shader_clock = False
        self.manually_set__frequency_application_default_memory_clock = False
        self.manually_set__frequency_application_memory_clock = False
        self.manually_set__frequency_application_shader_clock = False
        self.manually_set__frequency_maximum_memory_clock = False
        self.manually_set__frequency_maximum_shader_clock = False
        self.manually_set__frequency_maximum_streaming_multiprocessor_clock = False
        self.manually_set__frequency_memory_clock = False
        self.manually_set__frequency_shader_clock = False
        self.manually_set__frequency_streaming_multiprocessor_clock = False
        self.manually_set__frequency_video_clock = False
        self.manually_set__heterogenous_multi_vGPU = False
        self.manually_set__heterogenous_time_slice_profile = False
        self.manually_set__heterogenous_time_slice_sizes = False
        self.manually_set__ICM_indent = False
        self.manually_set__ICM_method = False
        self.manually_set__inf_filename = False
        self.manually_set__inf_section = False
        self.manually_set__info_ROM_ecc = False
        self.manually_set__info_ROM_oem = False
        self.manually_set__info_ROM_power = False
        self.manually_set__info_ROM_version = False
        self.manually_set__install_date = False
        self.manually_set__installed_display_drivers = False
        self.manually_set__last_error_code = False
        self.manually_set__max_memory_supported = False
        self.manually_set__max_number_controlled = False
        self.manually_set__max_refresh_rate = False
        self.manually_set__memory_clock_range = False
        self.manually_set__memory_free = False
        self.manually_set__memory_reserved = False
        self.manually_set__memory_total = False
        self.manually_set__memory_used = False
        self.manually_set__min_refresh_rate = False
        self.manually_set__monochrome = False
        self.manually_set__multi_instance_GPU_mode_current = False
        self.manually_set__multi_instance_GPU_mode_pending = False
        self.manually_set__name = False
        self.manually_set__number_of_color_planes = False
        self.manually_set__number_of_video_pages = False
        self.manually_set__operating_mode_current = False
        self.manually_set__operating_mode_pending = False
        self.manually_set__pci_bus = False
        self.manually_set__pci_bus_id = False
        self.manually_set__pci_device = False
        self.manually_set__pci_device_id = False
        self.manually_set__pci_domain = False
        self.manually_set__pci_link_generation_current = False
        self.manually_set__pci_link_generation_device_host_maximum = False
        self.manually_set__pci_link_generation_gpu_maximum = False
        self.manually_set__pci_link_generation_maximum = False
        self.manually_set__pci_link_width_current = False
        self.manually_set__pci_link_width_maximum = False
        self.manually_set__pci_sub_device_id = False
        self.manually_set__persistence_mode = False
        self.manually_set__PNP_device_id = False
        self.manually_set__power_draw = False
        self.manually_set__power_draw_average = False
        self.manually_set__power_draw_default_limit = False
        self.manually_set__power_draw_enforced_limit = False
        self.manually_set__power_draw_instant = False
        self.manually_set__power_draw_limit = False
        self.manually_set__power_draw_maximum = False
        self.manually_set__power_draw_minimum = False
        self.manually_set__power_management_capabilities = False
        self.manually_set__power_management_supported = False
        self.manually_set__protected_memory_free = False
        self.manually_set__protected_memory_total = False
        self.manually_set__protected_memory_used = False
        self.manually_set__protocol_supported = False
        self.manually_set__performance_state = False
        self.manually_set__retired_pages_double_bit_ecc_errors_count = False
        self.manually_set__retired_pages_single_bit_ecc_errors_count = False
        self.manually_set__retired_pages_pending = False
        self.manually_set__reserved_system_palette_entries = False
        self.manually_set__reset_required = False
        self.manually_set__reset_and_drain_recommended = False
        self.manually_set__serial = False
        self.manually_set__specification_version = False
        self.manually_set__status = False
        self.manually_set__status_info = False
        self.manually_set__system_creation_class_name = False
        self.manually_set__system_name = False
        self.manually_set__system_palette_entries = False
        self.manually_set__GPU_system_processor_mode_current = False
        self.manually_set__GPU_system_processor_mode_default = False
        self.manually_set__temperature_core = False
        self.manually_set__temperature_core_limit = False
        self.manually_set__temperature_memory = False
        self.manually_set__time_of_last_reset = False
        self.manually_set__utilization_decoder = False
        self.manually_set__utilization_encoder = False
        self.manually_set__utilization_gpu = False
        self.manually_set__utilization_jpeg = False
        self.manually_set__utilization_memory = False
        self.manually_set__utilization_optical_flow = False
        self.manually_set__uuid = False
        self.manually_set__vbios_version = False
        self.manually_set__video_architecture = False
        self.manually_set__video_memory_type = False
        self.manually_set__video_mode = False
        self.manually_set__video_mode_description = False
        self.manually_set__video_processor = False


        self.internal_name__accelerator_capabilities = {Constants.SMI: [], Constants.WMI: ["AcceleratorCapabilities"], Constants.PYADL: []}
        self.internal_name__accounting_mode_enabled = {Constants.SMI: ["accounting.mode"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__accounting_mode_buffer_size = {Constants.SMI: ["accounting.buffer_size"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__adapter_compatibility = {Constants.SMI: [], Constants.WMI: ["AdapterCompatibility"], Constants.PYADL: []}
        self.internal_name__adapter_DAC_type = {Constants.SMI: [], Constants.WMI: ["AdapterDACType"], Constants.PYADL: []}
        self.internal_name__adapter_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["adapterID"]}
        self.internal_name__adapter_index = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["adapterIndex"]}
        self.internal_name__addressing_mode = {Constants.SMI: ["addressing_mode"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__availability = {Constants.SMI: [], Constants.WMI: ["Availability"], Constants.PYADL: []}
        self.internal_name__capability_descriptions = {Constants.SMI: [], Constants.WMI: ["CapabilityDescriptions"], Constants.PYADL: []}
        self.internal_name__caption = {Constants.SMI: [], Constants.WMI: ["Caption"], Constants.PYADL: []}
        self.internal_name__chip_to_chip_interconnect_mode = {Constants.SMI: ["c2c.mode"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_as_bitmap = {Constants.SMI: ["clocks_event_reasons.active", "clocks_throttle_reasons.active"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_application_setting = {Constants.SMI: ["clocks_event_reasons.applications_clocks_setting", "clocks_throttle_reasons.applications_clocks_setting"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_is_hardware_limited = {Constants.SMI: ["clocks_event_reasons.hw_slowdown", "clocks_throttle_reasons.hw_slowdown"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_gpu_idle_limited = {Constants.SMI: ["clocks_event_reasons.gpu_idle", "clocks_throttle_reasons.gpu_idle"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_software_power_limited = {Constants.SMI: ["clocks_event_reasons.sw_power_cap", "clocks_throttle_reasons.sw_power_cap"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_software_thermal_limited = {Constants.SMI: ["clocks_event_reasons.sw_thermal_slowdown", "clocks_throttle_reasons.sw_thermal_slowdown"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_power_break_slowdown_limited = {Constants.SMI: ["clocks_event_reasons.hw_power_brake_slowdown", "clocks_throttle_reasons.hw_power_brake_slowdown"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_supported = {Constants.SMI: ["clocks_event_reasons.supported", "clocks_throttle_reasons.supported"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_sync_boost = {Constants.SMI: ["clocks_event_reasons.sync_boost", "clocks_throttle_reasons.sync_boost"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_thermal_limited = {Constants.SMI: ["clocks_event_reasons.hw_thermal_slowdown", "clocks_throttle_reasons.hw_thermal_slowdown"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__color_table_entries = {Constants.SMI: [], Constants.WMI: ["ColorTableEntries"], Constants.PYADL: []}
        self.internal_name__compute_cap = {Constants.SMI: ["compute_cap"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__compute_mode = {Constants.SMI: ["compute_mode"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__config_manager_error_code = {Constants.SMI: [], Constants.WMI: ["ConfigManagerErrorCode"], Constants.PYADL: []}
        self.internal_name__config_manager_user_config = {Constants.SMI: [], Constants.WMI: ["ConfigManagerUserConfig"], Constants.PYADL: []}
        self.internal_name__core_voltage = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["getCurrentCoreVoltage"]}
        self.internal_name__core_voltage_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["coreVoltageRange"]}
        self.internal_name__creation_class_name = {Constants.SMI: [], Constants.WMI: ["CreationClassName"], Constants.PYADL: []}
        self.internal_name__current_bits_per_pixel = {Constants.SMI: [], Constants.WMI: ["CurrentBitsPerPixel"], Constants.PYADL: []}
        self.internal_name__current_horizontal_resolution = {Constants.SMI: [], Constants.WMI: ["CurrentHorizontalResolution"], Constants.PYADL: []}
        self.internal_name__current_number_of_colors = {Constants.SMI: [], Constants.WMI: ["CurrentNumberOfColors"], Constants.PYADL: []}
        self.internal_name__current_number_of_columns = {Constants.SMI: [], Constants.WMI: ["CurrentNumberOfColumns"], Constants.PYADL: []}
        self.internal_name__current_number_of_rows = {Constants.SMI: [], Constants.WMI: ["CurrentNumberOfRows"], Constants.PYADL: []}
        self.internal_name__current_refresh_rate = {Constants.SMI: [], Constants.WMI: ["CurrentRefreshRate"], Constants.PYADL: []}
        self.internal_name__current_scan_mode = {Constants.SMI: [], Constants.WMI: ["CurrentScanMode"], Constants.PYADL: []}
        self.internal_name__current_vertical_resolution = {Constants.SMI: [], Constants.WMI: ["CurrentVerticalResolution"], Constants.PYADL: []}
        self.internal_name__description = {Constants.SMI: [], Constants.WMI: ["Description"], Constants.PYADL: []}
        self.internal_name__device_id = {Constants.SMI: [], Constants.WMI: ["DeviceID"], Constants.PYADL: []}
        self.internal_name__device_specific_pens = {Constants.SMI: [], Constants.WMI: ["DeviceSpecificPens"], Constants.PYADL: []}
        self.internal_name__display_active = {Constants.SMI: ["display_active"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__display_mode = {Constants.SMI: ["display_mode"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__dither_type = {Constants.SMI: [], Constants.WMI: ["DitherType"], Constants.PYADL: []}
        self.internal_name__driver_date = {Constants.SMI: [], Constants.WMI: ["DriverDate"], Constants.PYADL: []}
        self.internal_name__driver_model_current = {Constants.SMI: ["driver_model.current"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__driver_model_pending = {Constants.SMI: ["driver_model.pending"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__driver_version = {Constants.SMI: ["driver_version"], Constants.WMI: ["DriverVersion"], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_cbu = {Constants.SMI: ["ecc.errors.corrected.aggregate.cbu"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_primary_cache = {Constants.SMI: ["ecc.errors.corrected.aggregate.l1_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_register_file = {Constants.SMI: ["ecc.errors.corrected.aggregate.register_file"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_secondary_cache = {Constants.SMI: ["ecc.errors.corrected.aggregate.l2_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_shared_memory = {Constants.SMI: ["ecc.errors.corrected.aggregate.dram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_sram = {Constants.SMI: ["ecc.errors.corrected.aggregate.sram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_texture_memory = {Constants.SMI: ["ecc.errors.corrected.aggregate.texture_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_total = {Constants.SMI: ["ecc.errors.corrected.aggregate.total"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_video_memory = {Constants.SMI: ["ecc.errors.corrected.aggregate.device_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_cbu = {Constants.SMI: ["ecc.errors.corrected.volatile.cbu"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_primary_cache = {Constants.SMI: ["ecc.errors.corrected.volatile.l1_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_register_file = {Constants.SMI: ["ecc.errors.corrected.volatile.register_file"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_secondary_cache = {Constants.SMI: ["ecc.errors.corrected.volatile.l2_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_shared_memory = {Constants.SMI: ["ecc.errors.corrected.volatile.dram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_sram = {Constants.SMI: ["ecc.errors.corrected.volatile.sram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_texture_memory = {Constants.SMI: ["ecc.errors.corrected.volatile.texture_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_total = {Constants.SMI: ["ecc.errors.corrected.volatile.total"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_video_memory = {Constants.SMI: ["ecc.errors.corrected.volatile.device_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_cbu = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.cbu"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_primary_cache = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.l1_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_register_file = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.register_file"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_secondary_cache = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.l2_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_shared_memory = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.dram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_sram = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.sram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_texture_memory = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.texture_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_total = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.total"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_video_memory = {Constants.SMI: ["ecc.errors.uncorrected.aggregate.device_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_cbu = {Constants.SMI: ["ecc.errors.uncorrected.volatile.cbu"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_primary_cache = {Constants.SMI: ["ecc.errors.uncorrected.volatile.l1_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_register_file = {Constants.SMI: ["ecc.errors.uncorrected.volatile.register_file"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_secondary_cache = {Constants.SMI: ["ecc.errors.uncorrected.volatile.l2_cache"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_shared_memory = {Constants.SMI: ["ecc.errors.uncorrected.volatile.dram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_sram = {Constants.SMI: ["ecc.errors.uncorrected.volatile.sram"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_texture_memory = {Constants.SMI: ["ecc.errors.uncorrected.volatile.texture_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_total = {Constants.SMI: ["ecc.errors.uncorrected.volatile.total"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_video_memory = {Constants.SMI: ["ecc.errors.uncorrected.volatile.device_memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_mode_current = {Constants.SMI: ["ecc.mode.current"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_mode_pending = {Constants.SMI: ["ecc.mode.pending"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__encoder_average_FPS = {Constants.SMI: ["encoder.stats.averageFps"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__encoder_average_latency = {Constants.SMI: ["encoder.stats.averageLatency"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__encoder_session_count = {Constants.SMI: ["encoder.stats.sessionCount"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__engine_clock_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["engineClockRange"]}
        self.internal_name__error_cleared = {Constants.SMI: [], Constants.WMI: ["ErrorCleared"], Constants.PYADL: []}
        self.internal_name__error_description = {Constants.SMI: [], Constants.WMI: ["ErrorDescription"], Constants.PYADL: []}
        self.internal_name__fabric_state = {Constants.SMI: ["fabric.state"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fabric_status = {Constants.SMI: ["fabric.status"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fan_speed_percentage = {Constants.SMI: ["fan.speed"], Constants.WMI: [], Constants.PYADL: ["getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE"]}
        self.internal_name__fan_speed_percentage_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE"]}
        self.internal_name__fan_speed_RPM = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_RPM"]}
        self.internal_name__fan_speed_RPM_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_RPM"]}
        self.internal_name__fractional_multi_vGPU = {Constants.SMI: ["vgpu_device_capability.fractional_multiVgpu"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_default_shader_clock = {Constants.SMI: ["clocks.default_applications.graphics", "clocks.default_applications.gr"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_default_memory_clock = {Constants.SMI: ["clocks.default_applications.memory", "clocks.default_applications.mem"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_memory_clock = {Constants.SMI: ["clocks.applications.memory", "clocks.applications.mem"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_shader_clock = {Constants.SMI: ["clocks.applications.graphics", "clocks.applications.gr"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_maximum_memory_clock = {Constants.SMI: ["clocks.max.memory", "clocks.max.mem"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_maximum_shader_clock = {Constants.SMI: ["clocks.max.graphics", "clocks.max.gr"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_maximum_streaming_multiprocessor_clock = {Constants.SMI: ["clocks.max.sm", "clocks.max.sm"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_memory_clock = {Constants.SMI: ["clocks.current.memory", "clocks.mem"], Constants.WMI: [], Constants.PYADL: ["getCurrentMemoryClock"]}
        self.internal_name__frequency_shader_clock = {Constants.SMI: ["clocks.current.graphics", "clocks.gr"], Constants.WMI: [], Constants.PYADL: ["getCurrentEngineClock"]}
        self.internal_name__frequency_streaming_multiprocessor_clock = {Constants.SMI: ["clocks.current.sm", "clocks.sm"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_video_clock = {Constants.SMI: ["clocks.current.video", "clocks.video"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__heterogenous_multi_vGPU = {Constants.SMI: ["vgpu_driver_capability.heterogenous_multivGPU"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__heterogenous_time_slice_profile = {Constants.SMI: ["vgpu_device_capability.heterogeneous_timeSlice_profile"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__heterogenous_time_slice_sizes = {Constants.SMI: ["vgpu_device_capability.heterogeneous_timeSlice_sizes"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ICM_indent = {Constants.SMI: [], Constants.WMI: ["ICMIntent"], Constants.PYADL: []}
        self.internal_name__ICM_method = {Constants.SMI: [], Constants.WMI: ["ICMMethod"], Constants.PYADL: []}
        self.internal_name__inf_filename = {Constants.SMI: [], Constants.WMI: ["InfFilename"], Constants.PYADL: []}
        self.internal_name__inf_section = {Constants.SMI: [], Constants.WMI: ["InfSection"], Constants.PYADL: []}
        self.internal_name__info_ROM_ecc = {Constants.SMI: ["inforom.ecc"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_oem = {Constants.SMI: ["inforom.oem"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_power = {Constants.SMI: ["inforom.pwr", "inforom.power"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_version = {Constants.SMI: ["inforom.img", "inforom.image"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__install_date = {Constants.SMI: [], Constants.WMI: ["InstallDate"], Constants.PYADL: []}
        self.internal_name__installed_display_drivers = {Constants.SMI: [], Constants.WMI: ["InstalledDisplayDrivers"], Constants.PYADL: []}
        self.internal_name__last_error_code = {Constants.SMI: [], Constants.WMI: ["LastErrorCode"], Constants.PYADL: []}
        self.internal_name__max_memory_supported = {Constants.SMI: [], Constants.WMI: ["MaxMemorySupported"], Constants.PYADL: []}
        self.internal_name__max_number_controlled = {Constants.SMI: [], Constants.WMI: ["MaxNumberControlled"], Constants.PYADL: []}
        self.internal_name__max_refresh_rate = {Constants.SMI: [], Constants.WMI: ["MaxRefreshRate"], Constants.PYADL: []}
        self.internal_name__memory_clock_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: ["getMemoryClockRange"]}
        self.internal_name__memory_free = {Constants.SMI: ["memory.free"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_reserved = {Constants.SMI: ["memory.reserved"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_total = {Constants.SMI: ["memory.total"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_used = {Constants.SMI: ["memory.used"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__min_refresh_rate = {Constants.SMI: [], Constants.WMI: ["MinRefreshRate"], Constants.PYADL: []}
        self.internal_name__monochrome = {Constants.SMI: [], Constants.WMI: ["Monochrome"], Constants.PYADL: []}
        self.internal_name__multi_instance_GPU_mode_current = {Constants.SMI: ["mig.mode.current"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__multi_instance_GPU_mode_pending = {Constants.SMI: ["mig.mode.pending"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__name = {Constants.SMI: ["name", "gpu_name"], Constants.WMI: ["Name"], Constants.PYADL: ["adapterName"]}
        self.internal_name__number_of_color_planes = {Constants.SMI: [], Constants.WMI: ["NumberOfColorPlanes"], Constants.PYADL: []}
        self.internal_name__number_of_video_pages = {Constants.SMI: [], Constants.WMI: ["NumberOfVideoPages"], Constants.PYADL: []}
        self.internal_name__operating_mode_current = {Constants.SMI: ["gom.current", "gpu_operation_mode.current"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__operating_mode_pending = {Constants.SMI: ["gom.pending", "gpu_operation_mode.pending"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_bus = {Constants.SMI: ["pci.bus"], Constants.WMI: [], Constants.PYADL: ["busNumber"]}
        self.internal_name__pci_bus_id = {Constants.SMI: ["pci.bus_id", "gpu_bus_id"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_device = {Constants.SMI: ["pci.device"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_device_id = {Constants.SMI: ["pci.device_id"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_domain = {Constants.SMI: ["pci.domain"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_current = {Constants.SMI: ["pcie.link.gen.gpucurrent"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_device_host_maximum = {Constants.SMI: ["pcie.link.gen.max"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_gpu_maximum = {Constants.SMI: ["pcie.link.gen.gpumax"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_maximum = {Constants.SMI: ["pcie.link.gen.hostmax"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_width_current = {Constants.SMI: ["pcie.link.width.current"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_width_maximum = {Constants.SMI: ["pcie.link.width.max"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_sub_device_id = {Constants.SMI: ["pci.sub_device_id"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__persistence_mode = {Constants.SMI: ["persistence_mode"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__PNP_device_id = {Constants.SMI: [], Constants.WMI: ["PNPDeviceID"], Constants.PYADL: []}
        self.internal_name__power_draw = {Constants.SMI: ["power.draw"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_average = {Constants.SMI: ["power.draw.average"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_default_limit = {Constants.SMI: ["power.default_limit"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_enforced_limit = {Constants.SMI: ["enforced.power.limit"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_instant = {Constants.SMI: ["power.draw.instant"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_limit = {Constants.SMI: ["power.limit"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_maximum = {Constants.SMI: ["power.max_limit"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_minimum = {Constants.SMI: ["power.min_limit"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_management_capabilities = {Constants.SMI: [], Constants.WMI: ["PowerManagementCapabilities"], Constants.PYADL: []}
        self.internal_name__power_management_supported = {Constants.SMI: ["power.management"], Constants.WMI: ["PowerManagementSupported"], Constants.PYADL: []}
        self.internal_name__protected_memory_free = {Constants.SMI: ["protected_memory.free"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protected_memory_total = {Constants.SMI: ["protected_memory.total"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protected_memory_used = {Constants.SMI: ["protected_memory.used"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protocol_supported = {Constants.SMI: [], Constants.WMI: ["ProtocolSupported"], Constants.PYADL: []}
        self.internal_name__performance_state = {Constants.SMI: ["pstate"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__retired_pages_double_bit_ecc_errors_count = {Constants.SMI: ["retired_pages.double_bit.count", "retired_pages.dbe"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__retired_pages_single_bit_ecc_errors_count = {Constants.SMI: ["retired_pages.single_bit_ecc.count", "retired_pages.sbe"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__retired_pages_pending = {Constants.SMI: ["retired_pages.pending"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__reserved_system_palette_entries = {Constants.SMI: [], Constants.WMI: ["ReservedSystemPaletteEntries"], Constants.PYADL: []}
        self.internal_name__reset_required = {Constants.SMI: ["reset_status.reset_required"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__reset_and_drain_recommended = {Constants.SMI: ["reset_status.drain_and_reset_recommended"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__serial = {Constants.SMI: ["serial", "gpu_serial"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__specification_version = {Constants.SMI: [], Constants.WMI: ["SpecificationVersion"], Constants.PYADL: []}
        self.internal_name__status = {Constants.SMI: [], Constants.WMI: ["Status"], Constants.PYADL: []}
        self.internal_name__status_info = {Constants.SMI: [], Constants.WMI: ["StatusInfo"], Constants.PYADL: []}
        self.internal_name__system_creation_class_name = {Constants.SMI: [], Constants.WMI: ["SystemCreationClassName"], Constants.PYADL: []}
        self.internal_name__system_name = {Constants.SMI: [], Constants.WMI: ["SystemName"], Constants.PYADL: []}
        self.internal_name__system_palette_entries = {Constants.SMI: [], Constants.WMI: ["SystemPaletteEntries"], Constants.PYADL: []}
        self.internal_name__GPU_system_processor_mode_current = {Constants.SMI: ["gsp.mode.current"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__GPU_system_processor_mode_default = {Constants.SMI: ["gsp.mode.default"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__temperature_core = {Constants.SMI: ["temperature.gpu"], Constants.WMI: [], Constants.PYADL: ["getCurrentTemperature"]}
        self.internal_name__temperature_core_limit = {Constants.SMI: ["temperature.gpu.tlimit"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__temperature_memory = {Constants.SMI: ["temperature.memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__time_of_last_reset = {Constants.SMI: [], Constants.WMI: ["TimeOfLastReset"], Constants.PYADL: []}
        self.internal_name__utilization_decoder = {Constants.SMI: ["utilization.decoder"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_encoder = {Constants.SMI: ["utilization.encoder"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_gpu = {Constants.SMI: ["utilization.gpu"], Constants.WMI: [], Constants.PYADL: ["getCurrentUsage"]}
        self.internal_name__utilization_jpeg = {Constants.SMI: ["utilization.jpeg"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_memory = {Constants.SMI: ["utilization.memory"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_optical_flow = {Constants.SMI: ["utilization.ofa"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__uuid = {Constants.SMI: ["uuid", "gpu_uuid"], Constants.WMI: [], Constants.PYADL: ["uuid"]}
        self.internal_name__vbios_version = {Constants.SMI: ["vbios_version"], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__video_architecture = {Constants.SMI: [], Constants.WMI: ["VideoArchitecture"], Constants.PYADL: []}
        self.internal_name__video_memory_type = {Constants.SMI: [], Constants.WMI: ["VideoMemoryType"], Constants.PYADL: []}
        self.internal_name__video_mode = {Constants.SMI: [], Constants.WMI: ["VideoMode"], Constants.PYADL: []}
        self.internal_name__video_mode_description = {Constants.SMI: [], Constants.WMI: ["VideoModeDescription"], Constants.PYADL: []}
        self.internal_name__video_processor = {Constants.SMI: [], Constants.WMI: ["VideoProcessor"], Constants.PYADL: []}

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

        self.internal_name = "internal_name__"
        self.operating_system_compatibility = "operating_system_compatibility__"
        self.manually_set = "manually_set__"

        self.priorities = [Constants.SMI, Constants.PYADL, Constants.WMI]

        self.update(everything=True)

    def update(self, everything=False):
        smi_data = ""
        smi_data_points = []
        adl_data = []
        adl_data_points = []
        wmi_data = []
        wmi_data_points = []
        for data_point in self.gpu_data_points:
            if getattr(self, f"{self.manually_set}{data_point}") is False or everything:
                data_collection_strategies = getattr(self, f"{self.internal_name}{data_point}")
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
                        setattr(self, data_point, data)
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
                        setattr(self, data_point, data)
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
                        setattr(self, data_point, data)
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

    def set_accounting_mode_enabled(self, value=None):
        if value != None:
            self.manually_set__accounting_mode_enabled = True
        else:
            self.manually_set__accounting_mode_enabled = False

    def set_accounting_mode_buffer_size(self, value=None):
        if value != None:
            self.manually_set__accounting_mode_buffer_size = True
        else:
            self.manually_set__accounting_mode_buffer_size = False

    def set_adapter_compatibility(self, value=None):
        if value != None:
            self.manually_set__adapter_compatibility = True
        else:
            self.manually_set__adapter_compatibility = False

    def set_adapter_DAC_type(self, value=None):
        if value != None:
            self.manually_set__adapter_DAC_type = True
        else:
            self.manually_set__adapter_DAC_type = False

    def set_adapter_id(self, value=None):
        if value != None:
            self.manually_set__adapter_id = True
        else:
            self.manually_set__adapter_id = False

    def set_adapter_index(self, value=None):
        if value != None:
            self.manually_set__adapter_index = True
        else:
            self.manually_set__adapter_index = False

    def set_addressing_mode(self, value=None):
        if value != None:
            self.manually_set__addressing_mode = True
        else:
            self.manually_set__addressing_mode = False

    def set_availability(self, value=None):
        if value != None:
            self.manually_set__availability = True
        else:
            self.manually_set__availability = False

    def set_capability_descriptions(self, value=None):
        if value != None:
            self.manually_set__capability_descriptions = True
        else:
            self.manually_set__capability_descriptions = False

    def set_caption(self, value=None):
        if value != None:
            self.manually_set__caption = True
        else:
            self.manually_set__caption = False

    def set_chip_to_chip_interconnect_mode(self, value=None):
        if value != None:
            self.manually_set__chip_to_chip_interconnect_mode = True
        else:
            self.manually_set__chip_to_chip_interconnect_mode = False

    def set_clock_event_reasons_as_bitmap(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_as_bitmap = True
        else:
            self.manually_set__clock_event_reasons_as_bitmap = False

    def set_clock_event_reasons_application_setting(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_application_setting = True
        else:
            self.manually_set__clock_event_reasons_application_setting = False

    def set_clock_event_reasons_is_hardware_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_is_hardware_limited = True
        else:
            self.manually_set__clock_event_reasons_is_hardware_limited = False

    def set_clock_event_reasons_gpu_idle_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_gpu_idle_limited = True
        else:
            self.manually_set__clock_event_reasons_gpu_idle_limited = False

    def set_clock_event_reasons_software_power_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_software_power_limited = True
        else:
            self.manually_set__clock_event_reasons_software_power_limited = False

    def set_clock_event_reasons_software_thermal_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_software_thermal_limited = True
        else:
            self.manually_set__clock_event_reasons_software_thermal_limited = False

    def set_clock_event_reasons_power_break_slowdown_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_power_break_slowdown_limited = True
        else:
            self.manually_set__clock_event_reasons_power_break_slowdown_limited = False

    def set_clock_event_reasons_supported(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_supported = True
        else:
            self.manually_set__clock_event_reasons_supported = False

    def set_clock_event_reasons_sync_boost(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_sync_boost = True
        else:
            self.manually_set__clock_event_reasons_sync_boost = False

    def set_clock_event_reasons_thermal_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_thermal_limited = True
        else:
            self.manually_set__clock_event_reasons_thermal_limited = False

    def set_color_table_entries(self, value=None):
        if value != None:
            self.manually_set__color_table_entries = True
        else:
            self.manually_set__color_table_entries = False

    def set_compute_cap(self, value=None):
        if value != None:
            self.manually_set__compute_cap = True
        else:
            self.manually_set__compute_cap = False

    def set_compute_mode(self, value=None):
        if value != None:
            self.manually_set__compute_mode = True
        else:
            self.manually_set__compute_mode = False

    def set_config_manager_error_code(self, value=None):
        if value != None:
            self.manually_set__config_manager_error_code = True
        else:
            self.manually_set__config_manager_error_code = False

    def set_config_manager_user_config(self, value=None):
        if value != None:
            self.manually_set__config_manager_user_config = True
        else:
            self.manually_set__config_manager_user_config = False

    def set_core_voltage(self, value=None):
        if value != None:
            self.manually_set__core_voltage = True
        else:
            self.manually_set__core_voltage = False

    def set_core_voltage_range(self, value=None):
        if value != None:
            self.manually_set__core_voltage_range = True
        else:
            self.manually_set__core_voltage_range = False

    def set_creation_class_name(self, value=None):
        if value != None:
            self.manually_set__creation_class_name = True
        else:
            self.manually_set__creation_class_name = False

    def set_current_bits_per_pixel(self, value=None):
        if value != None:
            self.manually_set__current_bits_per_pixel = True
        else:
            self.manually_set__current_bits_per_pixel = False

    def set_current_horizontal_resolution(self, value=None):
        if value != None:
            self.manually_set__current_horizontal_resolution = True
        else:
            self.manually_set__current_horizontal_resolution = False

    def set_current_number_of_colors(self, value=None):
        if value != None:
            self.manually_set__current_number_of_colors = True
        else:
            self.manually_set__current_number_of_colors = False

    def set_current_number_of_columns(self, value=None):
        if value != None:
            self.manually_set__current_number_of_columns = True
        else:
            self.manually_set__current_number_of_columns = False

    def set_current_number_of_rows(self, value=None):
        if value != None:
            self.manually_set__current_number_of_rows = True
        else:
            self.manually_set__current_number_of_rows = False

    def set_current_refresh_rate(self, value=None):
        if value != None:
            self.manually_set__current_refresh_rate = True
        else:
            self.manually_set__current_refresh_rate = False

    def set_current_scan_mode(self, value=None):
        if value != None:
            self.manually_set__current_scan_mode = True
        else:
            self.manually_set__current_scan_mode = False

    def set_current_vertical_resolution(self, value=None):
        if value != None:
            self.manually_set__current_vertical_resolution = True
        else:
            self.manually_set__current_vertical_resolution = False

    def set_description(self, value=None):
        if value != None:
            self.manually_set__description = True
        else:
            self.manually_set__description = False

    def set_device_id(self, value=None):
        if value != None:
            self.manually_set__device_id = True
        else:
            self.manually_set__device_id = False

    def set_device_specific_pens(self, value=None):
        if value != None:
            self.manually_set__device_specific_pens = True
        else:
            self.manually_set__device_specific_pens = False

    def set_display_active(self, value=None):
        if value != None:
            self.manually_set__display_active = True
        else:
            self.manually_set__display_active = False

    def set_display_mode(self, value=None):
        if value != None:
            self.manually_set__display_mode = True
        else:
            self.manually_set__display_mode = False

    def set_dither_type(self, value=None):
        if value != None:
            self.manually_set__dither_type = True
        else:
            self.manually_set__dither_type = False

    def set_driver_date(self, value=None):
        if value != None:
            self.manually_set__driver_date = True
        else:
            self.manually_set__driver_date = False

    def set_driver_model_current(self, value=None):
        if value != None:
            self.manually_set__driver_model_current = True
        else:
            self.manually_set__driver_model_current = False

    def set_driver_model_pending(self, value=None):
        if value != None:
            self.manually_set__driver_model_pending = True
        else:
            self.manually_set__driver_model_pending = False

    def set_driver_version(self, value=None):
        if value != None:
            self.manually_set__driver_version = True
        else:
            self.manually_set__driver_version = False

    def set_ecc_errors_corrected_all_time_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_cbu = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_cbu = False

    def set_ecc_errors_corrected_all_time_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_primary_cache = False

    def set_ecc_errors_corrected_all_time_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_register_file = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_register_file = False

    def set_ecc_errors_corrected_all_time_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_secondary_cache = False

    def set_ecc_errors_corrected_all_time_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_shared_memory = False

    def set_ecc_errors_corrected_all_time_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_sram = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_sram = False

    def set_ecc_errors_corrected_all_time_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_texture_memory = False

    def set_ecc_errors_corrected_all_time_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_total = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_total = False

    def set_ecc_errors_corrected_all_time_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_all_time_in_video_memory = True
        else:
            self.manually_set__ecc_errors_corrected_all_time_in_video_memory = False

    def set_ecc_errors_corrected_since_reboot_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_cbu = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_cbu = False

    def set_ecc_errors_corrected_since_reboot_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_primary_cache = False

    def set_ecc_errors_corrected_since_reboot_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_register_file = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_register_file = False

    def set_ecc_errors_corrected_since_reboot_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_secondary_cache = False

    def set_ecc_errors_corrected_since_reboot_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_shared_memory = False

    def set_ecc_errors_corrected_since_reboot_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_sram = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_sram = False

    def set_ecc_errors_corrected_since_reboot_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_texture_memory = False

    def set_ecc_errors_corrected_since_reboot_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_total = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_total = False

    def set_ecc_errors_corrected_since_reboot_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_corrected_since_reboot_in_video_memory = True
        else:
            self.manually_set__ecc_errors_corrected_since_reboot_in_video_memory = False

    def set_ecc_errors_uncorrected_all_time_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_cbu = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_cbu = False

    def set_ecc_errors_uncorrected_all_time_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_primary_cache = False

    def set_ecc_errors_uncorrected_all_time_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_register_file = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_register_file = False

    def set_ecc_errors_uncorrected_all_time_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_secondary_cache = False

    def set_ecc_errors_uncorrected_all_time_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_shared_memory = False

    def set_ecc_errors_uncorrected_all_time_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_sram = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_sram = False

    def set_ecc_errors_uncorrected_all_time_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_texture_memory = False

    def set_ecc_errors_uncorrected_all_time_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_total = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_total = False

    def set_ecc_errors_uncorrected_all_time_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_all_time_in_video_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_all_time_in_video_memory = False

    def set_ecc_errors_uncorrected_since_reboot_in_cbu(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_cbu = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_cbu = False

    def set_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_primary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_primary_cache = False

    def set_ecc_errors_uncorrected_since_reboot_in_register_file(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_register_file = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_register_file = False

    def set_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_secondary_cache = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_secondary_cache = False

    def set_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_shared_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_shared_memory = False

    def set_ecc_errors_uncorrected_since_reboot_in_sram(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_sram = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_sram = False

    def set_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_texture_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_texture_memory = False

    def set_ecc_errors_uncorrected_since_reboot_in_total(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_total = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_total = False

    def set_ecc_errors_uncorrected_since_reboot_in_video_memory(self, value=None):
        if value != None:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_video_memory = True
        else:
            self.manually_set__ecc_errors_uncorrected_since_reboot_in_video_memory = False

    def set_ecc_mode_current(self, value=None):
        if value != None:
            self.manually_set__ecc_mode_current = True
        else:
            self.manually_set__ecc_mode_current = False

    def set_ecc_mode_pending(self, value=None):
        if value != None:
            self.manually_set__ecc_mode_pending = True
        else:
            self.manually_set__ecc_mode_pending = False

    def set_encoder_average_FPS(self, value=None):
        if value != None:
            self.manually_set__encoder_average_FPS = True
        else:
            self.manually_set__encoder_average_FPS = False

    def set_encoder_average_latency(self, value=None):
        if value != None:
            self.manually_set__encoder_average_latency = True
        else:
            self.manually_set__encoder_average_latency = False

    def set_encoder_session_count(self, value=None):
        if value != None:
            self.manually_set__encoder_session_count = True
        else:
            self.manually_set__encoder_session_count = False

    def set_engine_clock_range(self, value=None):
        if value != None:
            self.manually_set__engine_clock_range = True
        else:
            self.manually_set__engine_clock_range = False

    def set_error_cleared(self, value=None):
        if value != None:
            self.manually_set__error_cleared = True
        else:
            self.manually_set__error_cleared = False

    def set_error_description(self, value=None):
        if value != None:
            self.manually_set__error_description = True
        else:
            self.manually_set__error_description = False

    def set_fabric_state(self, value=None):
        if value != None:
            self.manually_set__fabric_state = True
        else:
            self.manually_set__fabric_state = False

    def set_fabric_status(self, value=None):
        if value != None:
            self.manually_set__fabric_status = True
        else:
            self.manually_set__fabric_status = False

    def set_fan_speed_percentage(self, value=None):
        if value != None:
            self.manually_set__fan_speed_percentage = True
        else:
            self.manually_set__fan_speed_percentage = False

    def set_fan_speed_percentage_range(self, value=None):
        if value != None:
            self.manually_set__fan_speed_percentage_range = True
        else:
            self.manually_set__fan_speed_percentage_range = False

    def set_fan_speed_RPM(self, value=None):
        if value != None:
            self.manually_set__fan_speed_RPM = True
        else:
            self.manually_set__fan_speed_RPM = False

    def set_fan_speed_RPM_range(self, value=None):
        if value != None:
            self.manually_set__fan_speed_RPM_range = True
        else:
            self.manually_set__fan_speed_RPM_range = False

    def set_fractional_multi_vGPU(self, value=None):
        if value != None:
            self.manually_set__fractional_multi_vGPU = True
        else:
            self.manually_set__fractional_multi_vGPU = False

    def set_frequency_application_default_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_default_shader_clock = True
        else:
            self.manually_set__frequency_application_default_shader_clock = False

    def set_frequency_application_default_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_default_memory_clock = True
        else:
            self.manually_set__frequency_application_default_memory_clock = False

    def set_frequency_application_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_memory_clock = True
        else:
            self.manually_set__frequency_application_memory_clock = False

    def set_frequency_application_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_application_shader_clock = True
        else:
            self.manually_set__frequency_application_shader_clock = False

    def set_frequency_maximum_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_maximum_memory_clock = True
        else:
            self.manually_set__frequency_maximum_memory_clock = False

    def set_frequency_maximum_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_maximum_shader_clock = True
        else:
            self.manually_set__frequency_maximum_shader_clock = False

    def set_frequency_maximum_streaming_multiprocessor_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_maximum_streaming_multiprocessor_clock = True
        else:
            self.manually_set__frequency_maximum_streaming_multiprocessor_clock = False

    def set_frequency_memory_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_memory_clock = True
        else:
            self.manually_set__frequency_memory_clock = False

    def set_frequency_shader_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_shader_clock = True
        else:
            self.manually_set__frequency_shader_clock = False

    def set_frequency_streaming_multiprocessor_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_streaming_multiprocessor_clock = True
        else:
            self.manually_set__frequency_streaming_multiprocessor_clock = False

    def set_frequency_video_clock(self, value=None):
        if value != None:
            self.manually_set__frequency_video_clock = True
        else:
            self.manually_set__frequency_video_clock = False

    def set_heterogenous_multi_vGPU(self, value=None):
        if value != None:
            self.manually_set__heterogenous_multi_vGPU = True
        else:
            self.manually_set__heterogenous_multi_vGPU = False

    def set_heterogenous_time_slice_profile(self, value=None):
        if value != None:
            self.manually_set__heterogenous_time_slice_profile = True
        else:
            self.manually_set__heterogenous_time_slice_profile = False

    def set_heterogenous_time_slice_sizes(self, value=None):
        if value != None:
            self.manually_set__heterogenous_time_slice_sizes = True
        else:
            self.manually_set__heterogenous_time_slice_sizes = False

    def set_ICM_indent(self, value=None):
        if value != None:
            self.manually_set__ICM_indent = True
        else:
            self.manually_set__ICM_indent = False

    def set_ICM_method(self, value=None):
        if value != None:
            self.manually_set__ICM_method = True
        else:
            self.manually_set__ICM_method = False

    def set_inf_filename(self, value=None):
        if value != None:
            self.manually_set__inf_filename = True
        else:
            self.manually_set__inf_filename = False

    def set_inf_section(self, value=None):
        if value != None:
            self.manually_set__inf_section = True
        else:
            self.manually_set__inf_section = False

    def set_info_ROM_ecc(self, value=None):
        if value != None:
            self.manually_set__info_ROM_ecc = True
        else:
            self.manually_set__info_ROM_ecc = False

    def set_info_ROM_oem(self, value=None):
        if value != None:
            self.manually_set__info_ROM_oem = True
        else:
            self.manually_set__info_ROM_oem = False

    def set_info_ROM_power(self, value=None):
        if value != None:
            self.manually_set__info_ROM_power = True
        else:
            self.manually_set__info_ROM_power = False

    def set_info_ROM_version(self, value=None):
        if value != None:
            self.manually_set__info_ROM_version = True
        else:
            self.manually_set__info_ROM_version = False

    def set_install_date(self, value=None):
        if value != None:
            self.manually_set__install_date = True
        else:
            self.manually_set__install_date = False

    def set_installed_display_drivers(self, value=None):
        if value != None:
            self.manually_set__installed_display_drivers = True
        else:
            self.manually_set__installed_display_drivers = False

    def set_last_error_code(self, value=None):
        if value != None:
            self.manually_set__last_error_code = True
        else:
            self.manually_set__last_error_code = False

    def set_max_memory_supported(self, value=None):
        if value != None:
            self.manually_set__max_memory_supported = True
        else:
            self.manually_set__max_memory_supported = False

    def set_max_number_controlled(self, value=None):
        if value != None:
            self.manually_set__max_number_controlled = True
        else:
            self.manually_set__max_number_controlled = False

    def set_max_refresh_rate(self, value=None):
        if value != None:
            self.manually_set__max_refresh_rate = True
        else:
            self.manually_set__max_refresh_rate = False

    def set_memory_clock_range(self, value=None):
        if value != None:
            self.manually_set__memory_clock_range = True
        else:
            self.manually_set__memory_clock_range = False

    def set_memory_free(self, value=None):
        if value != None:
            self.manually_set__memory_free = True
        else:
            self.manually_set__memory_free = False

    def set_memory_reserved(self, value=None):
        if value != None:
            self.manually_set__memory_reserved = True
        else:
            self.manually_set__memory_reserved = False

    def set_memory_total(self, value=None):
        if value != None:
            self.manually_set__memory_total = True
        else:
            self.manually_set__memory_total = False

    def set_memory_used(self, value=None):
        if value != None:
            self.manually_set__memory_used = True
        else:
            self.manually_set__memory_used = False

    def set_min_refresh_rate(self, value=None):
        if value != None:
            self.manually_set__min_refresh_rate = True
        else:
            self.manually_set__min_refresh_rate = False

    def set_monochrome(self, value=None):
        if value != None:
            self.manually_set__monochrome = True
        else:
            self.manually_set__monochrome = False

    def set_multi_instance_GPU_mode_current(self, value=None):
        if value != None:
            self.manually_set__multi_instance_GPU_mode_current = True
        else:
            self.manually_set__multi_instance_GPU_mode_current = False

    def set_multi_instance_GPU_mode_pending(self, value=None):
        if value != None:
            self.manually_set__multi_instance_GPU_mode_pending = True
        else:
            self.manually_set__multi_instance_GPU_mode_pending = False

    def set_name(self, value=None):
        if value != None:
            self.manually_set__name = True
        else:
            self.manually_set__name = False

    def set_number_of_color_planes(self, value=None):
        if value != None:
            self.manually_set__number_of_color_planes = True
        else:
            self.manually_set__number_of_color_planes = False

    def set_number_of_video_pages(self, value=None):
        if value != None:
            self.manually_set__number_of_video_pages = True
        else:
            self.manually_set__number_of_video_pages = False

    def set_operating_mode_current(self, value=None):
        if value != None:
            self.manually_set__operating_mode_current = True
        else:
            self.manually_set__operating_mode_current = False

    def set_operating_mode_pending(self, value=None):
        if value != None:
            self.manually_set__operating_mode_pending = True
        else:
            self.manually_set__operating_mode_pending = False

    def set_pci_bus(self, value=None):
        if value != None:
            self.manually_set__pci_bus = True
        else:
            self.manually_set__pci_bus = False

    def set_pci_bus_id(self, value=None):
        if value != None:
            self.manually_set__pci_bus_id = True
        else:
            self.manually_set__pci_bus_id = False

    def set_pci_device(self, value=None):
        if value != None:
            self.manually_set__pci_device = True
        else:
            self.manually_set__pci_device = False

    def set_pci_device_id(self, value=None):
        if value != None:
            self.manually_set__pci_device_id = True
        else:
            self.manually_set__pci_device_id = False

    def set_pci_domain(self, value=None):
        if value != None:
            self.manually_set__pci_domain = True
        else:
            self.manually_set__pci_domain = False

    def set_pci_link_generation_current(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_current = True
        else:
            self.manually_set__pci_link_generation_current = False

    def set_pci_link_generation_device_host_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_device_host_maximum = True
        else:
            self.manually_set__pci_link_generation_device_host_maximum = False

    def set_pci_link_generation_gpu_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_gpu_maximum = True
        else:
            self.manually_set__pci_link_generation_gpu_maximum = False

    def set_pci_link_generation_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_generation_maximum = True
        else:
            self.manually_set__pci_link_generation_maximum = False

    def set_pci_link_width_current(self, value=None):
        if value != None:
            self.manually_set__pci_link_width_current = True
        else:
            self.manually_set__pci_link_width_current = False

    def set_pci_link_width_maximum(self, value=None):
        if value != None:
            self.manually_set__pci_link_width_maximum = True
        else:
            self.manually_set__pci_link_width_maximum = False

    def set_pci_sub_device_id(self, value=None):
        if value != None:
            self.manually_set__pci_sub_device_id = True
        else:
            self.manually_set__pci_sub_device_id = False

    def set_persistence_mode(self, value=None):
        if value != None:
            self.manually_set__persistence_mode = True
        else:
            self.manually_set__persistence_mode = False

    def set_PNP_device_id(self, value=None):
        if value != None:
            self.manually_set__PNP_device_id = True
        else:
            self.manually_set__PNP_device_id = False

    def set_power_draw(self, value=None):
        if value != None:
            self.manually_set__power_draw = True
        else:
            self.manually_set__power_draw = False

    def set_power_draw_average(self, value=None):
        if value != None:
            self.manually_set__power_draw_average = True
        else:
            self.manually_set__power_draw_average = False

    def set_power_draw_default_limit(self, value=None):
        if value != None:
            self.manually_set__power_draw_default_limit = True
        else:
            self.manually_set__power_draw_default_limit = False

    def set_power_draw_enforced_limit(self, value=None):
        if value != None:
            self.manually_set__power_draw_enforced_limit = True
        else:
            self.manually_set__power_draw_enforced_limit = False

    def set_power_draw_instant(self, value=None):
        if value != None:
            self.manually_set__power_draw_instant = True
        else:
            self.manually_set__power_draw_instant = False

    def set_power_draw_limit(self, value=None):
        if value != None:
            self.manually_set__power_draw_limit = True
        else:
            self.manually_set__power_draw_limit = False

    def set_power_draw_maximum(self, value=None):
        if value != None:
            self.manually_set__power_draw_maximum = True
        else:
            self.manually_set__power_draw_maximum = False

    def set_power_draw_minimum(self, value=None):
        if value != None:
            self.manually_set__power_draw_minimum = True
        else:
            self.manually_set__power_draw_minimum = False

    def set_power_management_capabilities(self, value=None):
        if value != None:
            self.manually_set__power_management_capabilities = True
        else:
            self.manually_set__power_management_capabilities = False

    def set_power_management_supported(self, value=None):
        if value != None:
            self.manually_set__power_management_supported = True
        else:
            self.manually_set__power_management_supported = False

    def set_protected_memory_free(self, value=None):
        if value != None:
            self.manually_set__protected_memory_free = True
        else:
            self.manually_set__protected_memory_free = False

    def set_protected_memory_total(self, value=None):
        if value != None:
            self.manually_set__protected_memory_total = True
        else:
            self.manually_set__protected_memory_total = False

    def set_protected_memory_used(self, value=None):
        if value != None:
            self.manually_set__protected_memory_used = True
        else:
            self.manually_set__protected_memory_used = False

    def set_protocol_supported(self, value=None):
        if value != None:
            self.manually_set__protocol_supported = True
        else:
            self.manually_set__protocol_supported = False

    def set_performance_state(self, value=None):
        if value != None:
            self.manually_set__performance_state = True
        else:
            self.manually_set__performance_state = False

    def set_retired_pages_double_bit_ecc_errors_count(self, value=None):
        if value != None:
            self.manually_set__retired_pages_double_bit_ecc_errors_count = True
        else:
            self.manually_set__retired_pages_double_bit_ecc_errors_count = False

    def set_retired_pages_single_bit_ecc_errors_count(self, value=None):
        if value != None:
            self.manually_set__retired_pages_single_bit_ecc_errors_count = True
        else:
            self.manually_set__retired_pages_single_bit_ecc_errors_count = False

    def set_retired_pages_pending(self, value=None):
        if value != None:
            self.manually_set__retired_pages_pending = True
        else:
            self.manually_set__retired_pages_pending = False

    def set_reserved_system_palette_entries(self, value=None):
        if value != None:
            self.manually_set__reserved_system_palette_entries = True
        else:
            self.manually_set__reserved_system_palette_entries = False

    def set_reset_required(self, value=None):
        if value != None:
            self.manually_set__reset_required = True
        else:
            self.manually_set__reset_required = False

    def set_reset_and_drain_recommended(self, value=None):
        if value != None:
            self.manually_set__reset_and_drain_recommended = True
        else:
            self.manually_set__reset_and_drain_recommended = False

    def set_serial(self, value=None):
        if value != None:
            self.manually_set__serial = True
        else:
            self.manually_set__serial = False

    def set_specification_version(self, value=None):
        if value != None:
            self.manually_set__specification_version = True
        else:
            self.manually_set__specification_version = False

    def set_status(self, value=None):
        if value != None:
            self.manually_set__status = True
        else:
            self.manually_set__status = False

    def set_status_info(self, value=None):
        if value != None:
            self.manually_set__status_info = True
        else:
            self.manually_set__status_info = False

    def set_system_creation_class_name(self, value=None):
        if value != None:
            self.manually_set__system_creation_class_name = True
        else:
            self.manually_set__system_creation_class_name = False

    def set_system_name(self, value=None):
        if value != None:
            self.manually_set__system_name = True
        else:
            self.manually_set__system_name = False

    def set_system_palette_entries(self, value=None):
        if value != None:
            self.manually_set__system_palette_entries = True
        else:
            self.manually_set__system_palette_entries = False

    def set_GPU_system_processor_mode_current(self, value=None):
        if value != None:
            self.manually_set__GPU_system_processor_mode_current = True
        else:
            self.manually_set__GPU_system_processor_mode_current = False

    def set_GPU_system_processor_mode_default(self, value=None):
        if value != None:
            self.manually_set__GPU_system_processor_mode_default = True
        else:
            self.manually_set__GPU_system_processor_mode_default = False

    def set_temperature_core(self, value=None):
        if value != None:
            self.manually_set__temperature_core = True
        else:
            self.manually_set__temperature_core = False

    def set_temperature_core_limit(self, value=None):
        if value != None:
            self.manually_set__temperature_core_limit = True
        else:
            self.manually_set__temperature_core_limit = False

    def set_temperature_memory(self, value=None):
        if value != None:
            self.manually_set__temperature_memory = True
        else:
            self.manually_set__temperature_memory = False

    def set_time_of_last_reset(self, value=None):
        if value != None:
            self.manually_set__time_of_last_reset = True
        else:
            self.manually_set__time_of_last_reset = False

    def set_utilization_decoder(self, value=None):
        if value != None:
            self.manually_set__utilization_decoder = True
        else:
            self.manually_set__utilization_decoder = False

    def set_utilization_encoder(self, value=None):
        if value != None:
            self.manually_set__utilization_encoder = True
        else:
            self.manually_set__utilization_encoder = False

    def set_utilization_gpu(self, value=None):
        if value != None:
            self.manually_set__utilization_gpu = True
        else:
            self.manually_set__utilization_gpu = False

    def set_utilization_jpeg(self, value=None):
        if value != None:
            self.manually_set__utilization_jpeg = True
        else:
            self.manually_set__utilization_jpeg = False

    def set_utilization_memory(self, value=None):
        if value != None:
            self.manually_set__utilization_memory = True
        else:
            self.manually_set__utilization_memory = False

    def set_utilization_optical_flow(self, value=None):
        if value != None:
            self.manually_set__utilization_optical_flow = True
        else:
            self.manually_set__utilization_optical_flow = False

    def set_uuid(self, value=None):
        if value != None:
            self.manually_set__uuid = True
        else:
            self.manually_set__uuid = False

    def set_vbios_version(self, value=None):
        if value != None:
            self.manually_set__vbios_version = True
        else:
            self.manually_set__vbios_version = False

    def set_video_architecture(self, value=None):
        if value != None:
            self.manually_set__video_architecture = True
        else:
            self.manually_set__video_architecture = False

    def set_video_memory_type(self, value=None):
        if value != None:
            self.manually_set__video_memory_type = True
        else:
            self.manually_set__video_memory_type = False

    def set_video_mode(self, value=None):
        if value != None:
            self.manually_set__video_mode = True
        else:
            self.manually_set__video_mode = False

    def set_video_mode_description(self, value=None):
        if value != None:
            self.manually_set__video_mode_description = True
        else:
            self.manually_set__video_mode_description = False

    def set_video_processor(self, value=None):
        if value != None:
            self.manually_set__video_processor = True
        else:
            self.manually_set__video_processor = False

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
