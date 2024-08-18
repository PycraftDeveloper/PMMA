from pmma.python_src.constants import Constants

class GPU:
    def __init__(self):
        self.accelerator_capabilities = None
        self.accounting_mode_enabled = None
        self.accounting_mode_buffer_size = None
        self.adapter_compatibility = None
        self.adapter_DAC_type = None
        self.adapter_id = None
        self.adapter_index = None
        self.adapter_name = None
        self.addressing_mode = None
        self.availability = None
        self.bus_number = None
        self.capability_descriptions = None
        self.caption = None
        self.chip_to_chip_interconnect_mode = None
        self.clock_event_reasons_activity_limited = None
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
        self.GPU_system_processor_mode_pending = None
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
        self.manually_set__adapter_name = False
        self.manually_set__addressing_mode = False
        self.manually_set__availability = False
        self.manually_set__bus_number = False
        self.manually_set__capability_descriptions = False
        self.manually_set__caption = False
        self.manually_set__chip_to_chip_interconnect_mode = False
        self.manually_set__clock_event_reasons_activity_limited = False
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
        self.manually_set__GPU_system_processor_mode_pending = False
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


        self.operating_system_compatibility__accelerator_capabilities = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__accounting_mode_enabled = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__accounting_mode_buffer_size = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__adapter_compatibility = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__adapter_DAC_type = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__adapter_id = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__adapter_index = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__adapter_name = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__addressing_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__availability = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__bus_number = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__capability_descriptions = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__caption = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__chip_to_chip_interconnect_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_activity_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_application_setting = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_is_hardware_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_gpu_idle_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_software_power_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_software_thermal_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_power_break_slowdown_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_supported = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_sync_boost = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__clock_event_reasons_thermal_limited = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__color_table_entries = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__compute_cap = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__compute_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__config_manager_error_code = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__config_manager_user_config = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__core_voltage = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__core_voltage_range = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__creation_class_name = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_bits_per_pixel = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_horizontal_resolution = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_number_of_colors = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_number_of_columns = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_number_of_rows = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_refresh_rate = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_scan_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__current_vertical_resolution = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__description = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__device_id = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__device_specific_pens = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__display_active = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__display_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__dither_type = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__driver_date = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__driver_model_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__driver_model_pending = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__driver_version = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_cbu = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_primary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_register_file = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_secondary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_shared_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_sram = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_texture_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_total = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_all_time_in_video_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_cbu = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_primary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_register_file = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_secondary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_shared_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_sram = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_texture_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_total = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_corrected_since_reboot_in_video_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_cbu = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_primary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_register_file = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_secondary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_shared_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_sram = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_texture_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_total = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_all_time_in_video_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_cbu = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_primary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_register_file = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_secondary_cache = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_shared_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_sram = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_texture_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_total = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_errors_uncorrected_since_reboot_in_video_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_mode_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ecc_mode_pending = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__encoder_average_FPS = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__encoder_average_latency = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__encoder_session_count = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__engine_clock_range = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__error_cleared = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__error_description = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fabric_state = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fabric_status = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fan_speed_percentage = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fan_speed_percentage_range = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fan_speed_RPM = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fan_speed_RPM_range = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__fractional_multi_vGPU = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_application_default_shader_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_application_default_memory_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_application_memory_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_application_shader_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_maximum_memory_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_maximum_shader_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_maximum_streaming_multiprocessor_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_memory_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_shader_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_streaming_multiprocessor_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__frequency_video_clock = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__heterogenous_multi_vGPU = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__heterogenous_time_slice_profile = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__heterogenous_time_slice_sizes = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ICM_indent = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__ICM_method = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__inf_filename = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__inf_section = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__info_ROM_ecc = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__info_ROM_oem = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__info_ROM_power = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__info_ROM_version = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__install_date = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__installed_display_drivers = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__last_error_code = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__max_memory_supported = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__max_number_controlled = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__max_refresh_rate = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__memory_clock_range = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__memory_free = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__memory_reserved = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__memory_total = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__memory_used = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__min_refresh_rate = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__monochrome = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__multi_instance_GPU_mode_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__multi_instance_GPU_mode_pending = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__name = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__number_of_color_planes = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__number_of_video_pages = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__operating_mode_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__operating_mode_pending = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_bus = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_bus_id = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_device = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_device_id = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_domain = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_link_generation_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_link_generation_device_host_maximum = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_link_generation_gpu_maximum = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_link_generation_maximum = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_link_width_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_link_width_maximum = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__pci_sub_device_id = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__persistence_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__PNP_device_id = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_average = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_default_limit = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_enforced_limit = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_instant = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_limit = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_maximum = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_draw_minimum = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_management_capabilities = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__power_management_supported = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__protected_memory_free = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__protected_memory_total = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__protected_memory_used = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__protocol_supported = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__performance_state = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__retired_pages_double_bit_ecc_errors_count = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__retired_pages_single_bit_ecc_errors_count = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__retired_pages_pending = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__reserved_system_palette_entries = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__reset_required = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__reset_and_drain_recommended = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__serial = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__specification_version = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__status = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__status_info = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__system_creation_class_name = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__system_name = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__system_palette_entries = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__GPU_system_processor_mode_current = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__GPU_system_processor_mode_pending = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__temperature_core = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__temperature_core_limit = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__temperature_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__time_of_last_reset = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__utilization_decoder = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__utilization_encoder = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__utilization_gpu = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__utilization_jpeg = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__utilization_memory = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__utilization_optical_flow = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__uuid = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__vbios_version = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__video_architecture = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__video_memory_type = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__video_mode = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__video_mode_description = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}
        self.operating_system_compatibility__video_processor = {Constants.WINDOWS: None, Constants.LINUX: None, Constants.MACOS: None, Constants.JAVA: None}


        self.internal_name__accelerator_capabilities = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__accounting_mode_enabled = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__accounting_mode_buffer_size = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__adapter_compatibility = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__adapter_DAC_type = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__adapter_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__adapter_index = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__adapter_name = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__addressing_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__availability = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__bus_number = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__capability_descriptions = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__caption = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__chip_to_chip_interconnect_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_activity_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_application_setting = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_is_hardware_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_gpu_idle_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_software_power_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_software_thermal_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_power_break_slowdown_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_supported = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_sync_boost = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__clock_event_reasons_thermal_limited = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__color_table_entries = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__compute_cap = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__compute_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__config_manager_error_code = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__config_manager_user_config = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__core_voltage = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__core_voltage_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__creation_class_name = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_bits_per_pixel = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_horizontal_resolution = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_number_of_colors = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_number_of_columns = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_number_of_rows = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_refresh_rate = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_scan_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__current_vertical_resolution = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__description = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__device_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__device_specific_pens = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__display_active = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__display_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__dither_type = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__driver_date = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__driver_model_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__driver_model_pending = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__driver_version = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_cbu = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_primary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_register_file = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_secondary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_shared_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_sram = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_texture_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_total = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_all_time_in_video_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_cbu = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_primary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_register_file = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_secondary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_shared_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_sram = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_texture_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_total = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_corrected_since_reboot_in_video_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_cbu = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_primary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_register_file = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_secondary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_shared_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_sram = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_texture_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_total = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_all_time_in_video_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_cbu = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_primary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_register_file = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_secondary_cache = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_shared_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_sram = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_texture_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_total = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_errors_uncorrected_since_reboot_in_video_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_mode_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ecc_mode_pending = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__encoder_average_FPS = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__encoder_average_latency = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__encoder_session_count = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__engine_clock_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__error_cleared = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__error_description = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fabric_state = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fabric_status = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fan_speed_percentage = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fan_speed_percentage_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fan_speed_RPM = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fan_speed_RPM_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__fractional_multi_vGPU = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_default_shader_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_default_memory_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_memory_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_application_shader_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_maximum_memory_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_maximum_shader_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_maximum_streaming_multiprocessor_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_memory_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_shader_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_streaming_multiprocessor_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__frequency_video_clock = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__heterogenous_multi_vGPU = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__heterogenous_time_slice_profile = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__heterogenous_time_slice_sizes = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ICM_indent = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__ICM_method = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__inf_filename = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__inf_section = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_ecc = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_oem = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_power = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__info_ROM_version = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__install_date = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__installed_display_drivers = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__last_error_code = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__max_memory_supported = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__max_number_controlled = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__max_refresh_rate = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_clock_range = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_free = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_reserved = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_total = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__memory_used = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__min_refresh_rate = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__monochrome = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__multi_instance_GPU_mode_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__multi_instance_GPU_mode_pending = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__name = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__number_of_color_planes = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__number_of_video_pages = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__operating_mode_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__operating_mode_pending = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_bus = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_bus_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_device = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_device_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_domain = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_device_host_maximum = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_gpu_maximum = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_generation_maximum = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_width_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_link_width_maximum = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__pci_sub_device_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__persistence_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__PNP_device_id = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_average = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_default_limit = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_enforced_limit = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_instant = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_limit = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_maximum = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_draw_minimum = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_management_capabilities = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__power_management_supported = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protected_memory_free = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protected_memory_total = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protected_memory_used = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__protocol_supported = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__performance_state = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__retired_pages_double_bit_ecc_errors_count = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__retired_pages_single_bit_ecc_errors_count = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__retired_pages_pending = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__reserved_system_palette_entries = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__reset_required = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__reset_and_drain_recommended = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__serial = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__specification_version = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__status = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__status_info = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__system_creation_class_name = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__system_name = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__system_palette_entries = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__GPU_system_processor_mode_current = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__GPU_system_processor_mode_pending = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__temperature_core = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__temperature_core_limit = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__temperature_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__time_of_last_reset = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_decoder = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_encoder = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_gpu = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_jpeg = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_memory = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__utilization_optical_flow = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__uuid = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__vbios_version = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__video_architecture = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__video_memory_type = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__video_mode = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__video_mode_description = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}
        self.internal_name__video_processor = {Constants.SMI: [], Constants.WMI: [], Constants.PYADL: []}

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

    def get_adapter_name(self):
            return self.adapter_name

    def get_addressing_mode(self):
            return self.addressing_mode

    def get_availability(self):
            return self.availability

    def get_bus_number(self):
            return self.bus_number

    def get_capability_descriptions(self):
            return self.capability_descriptions

    def get_caption(self):
            return self.caption

    def get_chip_to_chip_interconnect_mode(self):
            return self.chip_to_chip_interconnect_mode

    def get_clock_event_reasons_activity_limited(self):
            return self.clock_event_reasons_activity_limited

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

    def get_GPU_system_processor_mode_pending(self):
            return self.GPU_system_processor_mode_pending

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

    def set_adapter_name(self, value=None):
        if value != None:
            self.manually_set__adapter_name = True
        else:
            self.manually_set__adapter_name = False

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

    def set_bus_number(self, value=None):
        if value != None:
            self.manually_set__bus_number = True
        else:
            self.manually_set__bus_number = False

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

    def set_clock_event_reasons_activity_limited(self, value=None):
        if value != None:
            self.manually_set__clock_event_reasons_activity_limited = True
        else:
            self.manually_set__clock_event_reasons_activity_limited = False

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

    def set_GPU_system_processor_mode_pending(self, value=None):
        if value != None:
            self.manually_set__GPU_system_processor_mode_pending = True
        else:
            self.manually_set__GPU_system_processor_mode_pending = False

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

    def update_adapter_name(self):
            return self.adapter_name

    def update_addressing_mode(self):
            return self.addressing_mode

    def update_availability(self):
            return self.availability

    def update_bus_number(self):
            return self.bus_number

    def update_capability_descriptions(self):
            return self.capability_descriptions

    def update_caption(self):
            return self.caption

    def update_chip_to_chip_interconnect_mode(self):
            return self.chip_to_chip_interconnect_mode

    def update_clock_event_reasons_activity_limited(self):
            return self.clock_event_reasons_activity_limited

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

    def update_GPU_system_processor_mode_pending(self):
            return self.GPU_system_processor_mode_pending

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
