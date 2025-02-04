import threading as _threading

try:
    import pyadl as _pyadl
    pyadl_available = True
except Exception as error:
    if type(error) != ModuleNotFoundError:
        pyadl_available = False
    else:
        raise error

from pmma.python_src.general import get_operating_system as _get_operating_system
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.executor import Executor as _Executor

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.general_utils import find_executable_nvidia_smi as _find_executable_nvidia_smi
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

if _get_operating_system() == _Constants.WINDOWS:
    import wmi as _wmi
    import pythoncom as _pythoncom

class GPUs:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if not _Constants.GPUS_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.GPUS_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.gpu_utils import GPUsIntermediary as _GPUsIntermediary
            _GPUsIntermediary()

        self._gpu_intermediary = _Registry.pmma_module_spine[_Constants.GPUS_INTERMEDIARY_OBJECT]

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def identify_gpus(self):
        """
        🟩 **R** -
        """
        self._gpu_intermediary.identify_gpus()

    def get_gpu(self, gpu_index):
        """
        🟩 **R** -
        """
        return self._gpu_intermediary.get_gpu(gpu_index)

    def all_gpus_are_unique(self):
        """
        🟩 **R** -
        """
        return self._gpu_intermediary.all_gpus_are_unique()

class GPU:
    """
    🟩 **R** -
    """
    def __init__(self, module_identification_indices):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._module_identification_indices = module_identification_indices
        self._executor = _Executor()

        self._accelerator_capabilities = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['AcceleratorCapabilities'], _Constants.PYADL: []}}
        self._accounting_mode_enabled = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['accounting.mode'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._accounting_mode_buffer_size = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['accounting.buffer_size'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._adapter_compatibility = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['AdapterCompatibility'], _Constants.PYADL: []}}
        self._adapter_DAC_type = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['AdapterDACType'], _Constants.PYADL: []}}
        self._adapter_id = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['adapterID']}}
        self._adapter_index = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['adapterIndex']}}
        self._addressing_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['addressing_mode'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._availability = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['Availability'], _Constants.PYADL: []}}
        self._capability_descriptions = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CapabilityDescriptions'], _Constants.PYADL: []}}
        self._caption = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['Caption'], _Constants.PYADL: []}}
        self._chip_to_chip_interconnect_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['c2c.mode'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_as_bitmap = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.active', 'clocks_throttle_reasons.active'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_application_setting = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.applications_clocks_setting', 'clocks_throttle_reasons.applications_clocks_setting'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_is_hardware_limited = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.hw_slowdown', 'clocks_throttle_reasons.hw_slowdown'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_gpu_idle_limited = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.gpu_idle', 'clocks_throttle_reasons.gpu_idle'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_software_power_limited = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.sw_power_cap', 'clocks_throttle_reasons.sw_power_cap'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_software_thermal_limited = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.sw_thermal_slowdown', 'clocks_throttle_reasons.sw_thermal_slowdown'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_power_break_slowdown_limited = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.hw_power_brake_slowdown', 'clocks_throttle_reasons.hw_power_brake_slowdown'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_supported = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.supported', 'clocks_throttle_reasons.supported'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_sync_boost = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.sync_boost', 'clocks_throttle_reasons.sync_boost'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._clock_event_reasons_thermal_limited = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks_event_reasons.hw_thermal_slowdown', 'clocks_throttle_reasons.hw_thermal_slowdown'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._color_table_entries = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ColorTableEntries'], _Constants.PYADL: []}}
        self._compute_cap = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['compute_cap'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._compute_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['compute_mode'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._config_manager_error_code = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ConfigManagerErrorCode'], _Constants.PYADL: []}}
        self._config_manager_user_config = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ConfigManagerUserConfig'], _Constants.PYADL: []}}
        self._core_voltage = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['getCurrentCoreVoltage']}}
        self._core_voltage_range = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['coreVoltageRange']}}
        self._creation_class_name = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CreationClassName'], _Constants.PYADL: []}}
        self._current_bits_per_pixel = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentBitsPerPixel'], _Constants.PYADL: []}}
        self._current_horizontal_resolution = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentHorizontalResolution'], _Constants.PYADL: []}}
        self._current_number_of_colors = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentNumberOfColors'], _Constants.PYADL: []}}
        self._current_number_of_columns = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentNumberOfColumns'], _Constants.PYADL: []}}
        self._current_number_of_rows = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentNumberOfRows'], _Constants.PYADL: []}}
        self._current_refresh_rate = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentRefreshRate'], _Constants.PYADL: []}}
        self._current_scan_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentScanMode'], _Constants.PYADL: []}}
        self._current_vertical_resolution = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['CurrentVerticalResolution'], _Constants.PYADL: []}}
        self._description = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['Description'], _Constants.PYADL: []}}
        self._device_id = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['DeviceID'], _Constants.PYADL: []}}
        self._device_specific_pens = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['DeviceSpecificPens'], _Constants.PYADL: []}}
        self._display_active = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['display_active'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._display_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['display_mode'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._dither_type = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['DitherType'], _Constants.PYADL: []}}
        self._driver_date = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['DriverDate'], _Constants.PYADL: []}}
        self._driver_model_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['driver_model.current'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._driver_model_pending = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['driver_model.pending'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._driver_version = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['driver_version'], _Constants.WMI: ['DriverVersion'], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_cbu = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.cbu'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_primary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.l1_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_register_file = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.register_file'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_secondary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.l2_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_shared_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.dram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_sram = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.sram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_texture_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.texture_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_total = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.total'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_video_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.aggregate.device_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_cbu = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.cbu'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_primary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.l1_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_register_file = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.register_file'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_secondary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.l2_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_shared_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.dram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_sram = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.sram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_texture_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.texture_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_total = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.total'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_video_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.corrected.volatile.device_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_cbu = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.cbu'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_primary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.l1_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_register_file = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.register_file'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_secondary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.l2_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_shared_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.dram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_sram = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.sram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_texture_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.texture_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_total = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.total'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_video_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.aggregate.device_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_cbu = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.cbu'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.l1_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_register_file = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.register_file'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.l2_cache'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.dram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_sram = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.sram'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.texture_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_total = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.total'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_video_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.errors.uncorrected.volatile.device_memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_mode_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.mode.current'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ecc_mode_pending = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['ecc.mode.pending'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._encoder_average_FPS = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['encoder.stats.averageFps'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._encoder_average_latency = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['encoder.stats.averageLatency'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._encoder_session_count = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['encoder.stats.sessionCount'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._engine_clock_range = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['engineClockRange']}}
        self._error_cleared = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ErrorCleared'], _Constants.PYADL: []}}
        self._error_description = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ErrorDescription'], _Constants.PYADL: []}}
        self._fabric_state = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['fabric.state'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._fabric_status = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['fabric.status'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._fan_speed_percentage = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['fan.speed'], _Constants.WMI: [], _Constants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self._fan_speed_percentage_range = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self._fan_speed_RPM = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self._fan_speed_RPM_range = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self._fractional_multi_vGPU = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['vgpu_device_capability.fractional_multiVgpu'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_application_default_shader_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.default_applications.graphics', 'clocks.default_applications.gr'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_application_default_memory_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.default_applications.memory', 'clocks.default_applications.mem'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_application_memory_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.applications.memory', 'clocks.applications.mem'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_application_shader_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.applications.graphics', 'clocks.applications.gr'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_maximum_memory_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.max.memory', 'clocks.max.mem'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_maximum_shader_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.max.graphics', 'clocks.max.gr'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_maximum_streaming_multiprocessor_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.max.sm', 'clocks.max.sm'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_memory_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.current.memory', 'clocks.mem'], _Constants.WMI: [], _Constants.PYADL: ['getCurrentMemoryClock']}}
        self._frequency_shader_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.current.graphics', 'clocks.gr'], _Constants.WMI: [], _Constants.PYADL: ['getCurrentEngineClock']}}
        self._frequency_streaming_multiprocessor_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.current.sm', 'clocks.sm'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._frequency_video_clock = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['clocks.current.video', 'clocks.video'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._heterogenous_multi_vGPU = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['vgpu_driver_capability.heterogenous_multivGPU'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._heterogenous_time_slice_profile = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_profile'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._heterogenous_time_slice_sizes = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_sizes'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._ICM_indent = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ICMIntent'], _Constants.PYADL: []}}
        self._ICM_method = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ICMMethod'], _Constants.PYADL: []}}
        self._inf_filename = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['InfFilename'], _Constants.PYADL: []}}
        self._inf_section = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['InfSection'], _Constants.PYADL: []}}
        self._info_ROM_ecc = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['inforom.ecc'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._info_ROM_oem = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['inforom.oem'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._info_ROM_power = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['inforom.pwr', 'inforom.power'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._info_ROM_version = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['inforom.img', 'inforom.image'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._install_date = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['InstallDate'], _Constants.PYADL: []}}
        self._installed_display_drivers = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['InstalledDisplayDrivers'], _Constants.PYADL: []}}
        self._last_error_code = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['LastErrorCode'], _Constants.PYADL: []}}
        self._max_memory_supported = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['MaxMemorySupported'], _Constants.PYADL: []}}
        self._max_number_controlled = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['MaxNumberControlled'], _Constants.PYADL: []}}
        self._max_refresh_rate = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['MaxRefreshRate'], _Constants.PYADL: []}}
        self._memory_clock_range = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: [], _Constants.PYADL: ['getMemoryClockRange']}}
        self._memory_free = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['memory.free'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._memory_reserved = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['memory.reserved'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._memory_total = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['memory.total'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._memory_used = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['memory.used'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._min_refresh_rate = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['MinRefreshRate'], _Constants.PYADL: []}}
        self._monochrome = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['Monochrome'], _Constants.PYADL: []}}
        self._multi_instance_GPU_mode_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['mig.mode.current'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._multi_instance_GPU_mode_pending = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['mig.mode.pending'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._name = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['name', 'gpu_name'], _Constants.WMI: ['Name'], _Constants.PYADL: ['adapterName']}}
        self._number_of_color_planes = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['NumberOfColorPlanes'], _Constants.PYADL: []}}
        self._number_of_video_pages = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['NumberOfVideoPages'], _Constants.PYADL: []}}
        self._operating_mode_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['gom.current', 'gpu_operation_mode.current'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._operating_mode_pending = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['gom.pending', 'gpu_operation_mode.pending'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_bus = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pci.bus'], _Constants.WMI: [], _Constants.PYADL: ['busNumber']}}
        self._pci_bus_id = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pci.bus_id', 'gpu_bus_id'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_device = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pci.device'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_device_id = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pci.device_id'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_domain = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pci.domain'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_link_generation_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pcie.link.gen.gpucurrent'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_link_generation_device_host_maximum = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pcie.link.gen.max'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_link_generation_gpu_maximum = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pcie.link.gen.gpumax'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_link_generation_maximum = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pcie.link.gen.hostmax'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_link_width_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pcie.link.width.current'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_link_width_maximum = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pcie.link.width.max'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._pci_sub_device_id = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pci.sub_device_id'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._persistence_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['persistence_mode'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._PNP_device_id = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['PNPDeviceID'], _Constants.PYADL: []}}
        self._power_draw = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.draw'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_average = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.draw.average'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_default_limit = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.default_limit'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_enforced_limit = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['enforced.power.limit'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_instant = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.draw.instant'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_limit = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.limit'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_maximum = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.max_limit'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_draw_minimum = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.min_limit'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._power_management_capabilities = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['PowerManagementCapabilities'], _Constants.PYADL: []}}
        self._power_management_supported = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['power.management'], _Constants.WMI: ['PowerManagementSupported'], _Constants.PYADL: []}}
        self._protected_memory_free = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['protected_memory.free'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._protected_memory_total = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['protected_memory.total'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._protected_memory_used = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['protected_memory.used'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._protocol_supported = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ProtocolSupported'], _Constants.PYADL: []}}
        self._performance_state = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['pstate'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._retired_pages_double_bit_ecc_errors_count = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['retired_pages.double_bit.count', 'retired_pages.dbe'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._retired_pages_single_bit_ecc_errors_count = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['retired_pages.single_bit_ecc.count', 'retired_pages.sbe'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._retired_pages_pending = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['retired_pages.pending'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._reserved_system_palette_entries = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['ReservedSystemPaletteEntries'], _Constants.PYADL: []}}
        self._reset_required = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['reset_status.reset_required'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._reset_and_drain_recommended = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['reset_status.drain_and_reset_recommended'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._serial = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['serial', 'gpu_serial'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._specification_version = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['SpecificationVersion'], _Constants.PYADL: []}}
        self._status = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['Status'], _Constants.PYADL: []}}
        self._status_info = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['StatusInfo'], _Constants.PYADL: []}}
        self._system_creation_class_name = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['SystemCreationClassName'], _Constants.PYADL: []}}
        self._system_name = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['SystemName'], _Constants.PYADL: []}}
        self._system_palette_entries = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['SystemPaletteEntries'], _Constants.PYADL: []}}
        self._GPU_system_processor_mode_current = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['gsp.mode.current'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._GPU_system_processor_mode_default = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['gsp.mode.default'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._temperature_core = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['temperature.gpu'], _Constants.WMI: [], _Constants.PYADL: ['getCurrentTemperature']}}
        self._temperature_core_limit = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['temperature.gpu.tlimit'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._temperature_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['temperature.memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._time_of_last_reset = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['TimeOfLastReset'], _Constants.PYADL: []}}
        self._utilization_decoder = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['utilization.decoder'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._utilization_encoder = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['utilization.encoder'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._utilization_gpu = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['utilization.gpu'], _Constants.WMI: [], _Constants.PYADL: ['getCurrentUsage']}}
        self._utilization_jpeg = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['utilization.jpeg'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._utilization_memory = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['utilization.memory'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._utilization_optical_flow = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['utilization.ofa'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._uuid = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['uuid', 'gpu_uuid'], _Constants.WMI: [], _Constants.PYADL: ['uuid']}}
        self._vbios_version = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: ['vbios_version'], _Constants.WMI: [], _Constants.PYADL: []}}
        self._video_architecture = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['VideoArchitecture'], _Constants.PYADL: []}}
        self._video_memory_type = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['VideoMemoryType'], _Constants.PYADL: []}}
        self._video_mode = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['VideoMode'], _Constants.PYADL: []}}
        self._video_mode_description = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['VideoModeDescription'], _Constants.PYADL: []}}
        self._video_processor = {_Constants.VALUE: None, _Constants.UPDATING: True, _Constants.MANUALLY_SET: False, _Constants.DATA_COLLECTION_METHODS: {_Constants.SMI: [], _Constants.WMI: ['VideoProcessor'], _Constants.PYADL: []}}

        self._gpu_data_points = [
            "_accelerator_capabilities",
            "_accounting_mode_enabled",
            "_accounting_mode_buffer_size",
            "_adapter_compatibility",
            "_adapter_DAC_type",
            "_adapter_id",
            "_adapter_index",
            "_addressing_mode",
            "_availability",
            "_capability_descriptions",
            "_caption",
            "_chip_to_chip_interconnect_mode",
            "_clock_event_reasons_as_bitmap",
            "_clock_event_reasons_application_setting",
            "_clock_event_reasons_is_hardware_limited",
            "_clock_event_reasons_gpu_idle_limited",
            "_clock_event_reasons_software_power_limited",
            "_clock_event_reasons_software_thermal_limited",
            "_clock_event_reasons_power_break_slowdown_limited",
            "_clock_event_reasons_supported",
            "_clock_event_reasons_sync_boost",
            "_clock_event_reasons_thermal_limited",
            "_color_table_entries",
            "_compute_cap",
            "_compute_mode",
            "_config_manager_error_code",
            "_config_manager_user_config",
            "_core_voltage",
            "_core_voltage_range",
            "_creation_class_name",
            "_current_bits_per_pixel",
            "_current_horizontal_resolution",
            "_current_number_of_colors",
            "_current_number_of_columns",
            "_current_number_of_rows",
            "_current_refresh_rate",
            "_current_scan_mode",
            "_current_vertical_resolution",
            "_description",
            "_device_id",
            "_device_specific_pens",
            "_display_active",
            "_display_mode",
            "_dither_type",
            "_driver_date",
            "_driver_model_current",
            "_driver_model_pending",
            "_driver_version",
            "_ecc_errors_corrected_all_time_in_cbu",
            "_ecc_errors_corrected_all_time_in_primary_cache",
            "_ecc_errors_corrected_all_time_in_register_file",
            "_ecc_errors_corrected_all_time_in_secondary_cache",
            "_ecc_errors_corrected_all_time_in_shared_memory",
            "_ecc_errors_corrected_all_time_in_sram",
            "_ecc_errors_corrected_all_time_in_texture_memory",
            "_ecc_errors_corrected_all_time_in_total",
            "_ecc_errors_corrected_all_time_in_video_memory",
            "_ecc_errors_corrected_since_reboot_in_cbu",
            "_ecc_errors_corrected_since_reboot_in_primary_cache",
            "_ecc_errors_corrected_since_reboot_in_register_file",
            "_ecc_errors_corrected_since_reboot_in_secondary_cache",
            "_ecc_errors_corrected_since_reboot_in_shared_memory",
            "_ecc_errors_corrected_since_reboot_in_sram",
            "_ecc_errors_corrected_since_reboot_in_texture_memory",
            "_ecc_errors_corrected_since_reboot_in_total",
            "_ecc_errors_corrected_since_reboot_in_video_memory",
            "_ecc_errors_uncorrected_all_time_in_cbu",
            "_ecc_errors_uncorrected_all_time_in_primary_cache",
            "_ecc_errors_uncorrected_all_time_in_register_file",
            "_ecc_errors_uncorrected_all_time_in_secondary_cache",
            "_ecc_errors_uncorrected_all_time_in_shared_memory",
            "_ecc_errors_uncorrected_all_time_in_sram",
            "_ecc_errors_uncorrected_all_time_in_texture_memory",
            "_ecc_errors_uncorrected_all_time_in_total",
            "_ecc_errors_uncorrected_all_time_in_video_memory",
            "_ecc_errors_uncorrected_since_reboot_in_cbu",
            "_ecc_errors_uncorrected_since_reboot_in_primary_cache",
            "_ecc_errors_uncorrected_since_reboot_in_register_file",
            "_ecc_errors_uncorrected_since_reboot_in_secondary_cache",
            "_ecc_errors_uncorrected_since_reboot_in_shared_memory",
            "_ecc_errors_uncorrected_since_reboot_in_sram",
            "_ecc_errors_uncorrected_since_reboot_in_texture_memory",
            "_ecc_errors_uncorrected_since_reboot_in_total",
            "_ecc_errors_uncorrected_since_reboot_in_video_memory",
            "_ecc_mode_current",
            "_ecc_mode_pending",
            "_encoder_average_FPS",
            "_encoder_average_latency",
            "_encoder_session_count",
            "_engine_clock_range",
            "_error_cleared",
            "_error_description",
            "_fabric_state",
            "_fabric_status",
            "_fan_speed_percentage",
            "_fan_speed_percentage_range",
            "_fan_speed_RPM",
            "_fan_speed_RPM_range",
            "_fractional_multi_vGPU",
            "_frequency_application_default_shader_clock",
            "_frequency_application_default_memory_clock",
            "_frequency_application_memory_clock",
            "_frequency_application_shader_clock",
            "_frequency_maximum_memory_clock",
            "_frequency_maximum_shader_clock",
            "_frequency_maximum_streaming_multiprocessor_clock",
            "_frequency_memory_clock",
            "_frequency_shader_clock",
            "_frequency_streaming_multiprocessor_clock",
            "_frequency_video_clock",
            "_heterogenous_multi_vGPU",
            "_heterogenous_time_slice_profile",
            "_heterogenous_time_slice_sizes",
            "_ICM_indent",
            "_ICM_method",
            "_inf_filename",
            "_inf_section",
            "_info_ROM_ecc",
            "_info_ROM_oem",
            "_info_ROM_power",
            "_info_ROM_version",
            "_install_date",
            "_installed_display_drivers",
            "_last_error_code",
            "_max_memory_supported",
            "_max_number_controlled",
            "_max_refresh_rate",
            "_memory_clock_range",
            "_memory_free",
            "_memory_reserved",
            "_memory_total",
            "_memory_used",
            "_min_refresh_rate",
            "_monochrome",
            "_multi_instance_GPU_mode_current",
            "_multi_instance_GPU_mode_pending",
            "_name",
            "_number_of_color_planes",
            "_number_of_video_pages",
            "_operating_mode_current",
            "_operating_mode_pending",
            "_pci_bus",
            "_pci_bus_id",
            "_pci_device",
            "_pci_device_id",
            "_pci_domain",
            "_pci_link_generation_current",
            "_pci_link_generation_device_host_maximum",
            "_pci_link_generation_gpu_maximum",
            "_pci_link_generation_maximum",
            "_pci_link_width_current",
            "_pci_link_width_maximum",
            "_pci_sub_device_id",
            "_persistence_mode",
            "_PNP_device_id",
            "_power_draw",
            "_power_draw_average",
            "_power_draw_default_limit",
            "_power_draw_enforced_limit",
            "_power_draw_instant",
            "_power_draw_limit",
            "_power_draw_maximum",
            "_power_draw_minimum",
            "_power_management_capabilities",
            "_power_management_supported",
            "_protected_memory_free",
            "_protected_memory_total",
            "_protected_memory_used",
            "_protocol_supported",
            "_performance_state",
            "_retired_pages_double_bit_ecc_errors_count",
            "_retired_pages_single_bit_ecc_errors_count",
            "_retired_pages_pending",
            "_reserved_system_palette_entries",
            "_reset_required",
            "_reset_and_drain_recommended",
            "_serial",
            "_specification_version",
            "_status",
            "_status_info",
            "_system_creation_class_name",
            "_system_name",
            "_system_palette_entries",
            "_GPU_system_processor_mode_current",
            "_GPU_system_processor_mode_default",
            "_temperature_core",
            "_temperature_core_limit",
            "_temperature_memory",
            "_time_of_last_reset",
            "_utilization_decoder",
            "_utilization_encoder",
            "_utilization_gpu",
            "_utilization_jpeg",
            "_utilization_memory",
            "_utilization_optical_flow",
            "_uuid",
            "_vbios_version",
            "_video_architecture",
            "_video_memory_type",
            "_video_mode",
            "_video_mode_description",
            "_video_processor"
        ]

        self._priorities = [_Constants.SMI, _Constants.PYADL, _Constants.WMI]

        self._logger = _InternalLogger()

        if pyadl_available is False:
            self._logger.log_development("PMMA is unable to interface with AMD/ATI GPUs. \
This is most likely because no AMD/API GPUs where found on your system, \
although this can also imply that there are driver issues somewhere. If this is unexpected \
- which is to say; you have an AMD/ATI GPU - double check your driver install \
and that other software is able to interact with the GPU. On any virtual machines \
make sure that you are able to pass through the GPU device.")

    def update(self, everything=False, data_points=None, wait_for_completion=False):
        """
        🟩 **R** -
        """
        if _get_operating_system() == _Constants.WINDOWS:
            _pythoncom.CoInitialize()
        if wait_for_completion:
            self._update(everything=everything, data_points=data_points)
        else:
            thread = _threading.Thread(target=self._update, args=(everything, data_points))
            thread.daemon = True
            thread.name = "GPU:Update_Data_Thread"
            thread.start()

    def _update(self, everything, data_points):
        """
        🟩 **R** -
        """
        if data_points is None:
            data_points = self._gpu_data_points
        smi_data = ""
        smi_data_points = []
        adl_data = []
        adl_data_points = []
        wmi_data = []
        wmi_data_points = []
        for data_point in data_points:
            if self.__dict__[data_point][_Constants.MANUALLY_SET] is False or everything:
                data_collection_strategies = self.__dict__[data_point][_Constants.DATA_COLLECTION_METHODS] # keys changed
                for query_command in data_collection_strategies[_Constants.SMI]:
                    if self._module_identification_indices[_Constants.SMI] is not None:
                        smi_data += f"{query_command},"
                        smi_data_points.append(data_point)
                for query_command in data_collection_strategies[_Constants.PYADL]:
                    if self._module_identification_indices[_Constants.PYADL] is not None:
                        adl_data.append(query_command)
                        adl_data_points.append(data_point)
                for query_command in data_collection_strategies[_Constants.WMI]:
                    if self._module_identification_indices[_Constants.WMI] is not None:
                        wmi_data.append(query_command)
                        wmi_data_points.append(data_point)

        smi_data = smi_data[:-1]

        set_attributes = []

        for priority in self._priorities:
            if priority == _Constants.SMI and smi_data != "":
                self._executor.run([
                    _find_executable_nvidia_smi(),
                    f"--query-gpu={smi_data}",
                    "--format=csv,noheader,nounits",
                    f"-i={self._module_identification_indices[_Constants.SMI]}"])

                result = self._executor.get_result()
                split_result = result.split(", ")

                for data_point, data in zip(smi_data_points, split_result):
                    if "N/A" in data:
                        data = None
                    elif "Not Active" in data or "Disabled" in data:
                        data = False
                    elif "Active" in data or "Enabled" in data:
                        data = True
                    if data_point not in set_attributes:
                        self.__dict__[data_point][_Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

            elif priority == _Constants.PYADL and adl_data != [] and pyadl_available:
                gpu_data = _pyadl.ADLManager.getInstance().getDevices()[self._module_identification_indices[_Constants.PYADL]]
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
                        self.__dict__[data_point][_Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

            elif priority == _Constants.WMI and wmi_data != [] and _get_operating_system() == _Constants.WINDOWS:
                computer = _wmi.WMI()
                gpu_data = computer.Win32_VideoController()[self._module_identification_indices[_Constants.WMI]]
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
                        self.__dict__[data_point][_Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

        for data_point in data_points:
            self.__dict__[data_point][_Constants.UPDATING] = False

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def get_accelerator_capabilities(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._accelerator_capabilities[_Constants.VALUE]
        if update and self._accelerator_capabilities[_Constants.UPDATING] is False:
            self.update(data_points=["accelerator_capabilities"], wait_for_completion=wait_for_completion)
        return value

    def get_accounting_mode_enabled(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._accounting_mode_enabled[_Constants.VALUE]
        if update and self._accounting_mode_enabled[_Constants.UPDATING] is False:
            self.update(data_points=["accounting_mode_enabled"], wait_for_completion=wait_for_completion)
        return value

    def get_accounting_mode_buffer_size(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._accounting_mode_buffer_size[_Constants.VALUE]
        if update and self._accounting_mode_buffer_size[_Constants.UPDATING] is False:
            self.update(data_points=["accounting_mode_buffer_size"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_compatibility(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._adapter_compatibility[_Constants.VALUE]
        if update and self._adapter_compatibility[_Constants.UPDATING] is False:
            self.update(data_points=["adapter_compatibility"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_DAC_type(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._adapter_DAC_type[_Constants.VALUE]
        if update and self._adapter_DAC_type[_Constants.UPDATING] is False:
            self.update(data_points=["adapter_DAC_type"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_id(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._adapter_id[_Constants.VALUE]
        if update and self._adapter_id[_Constants.UPDATING] is False:
            self.update(data_points=["adapter_id"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_index(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._adapter_index[_Constants.VALUE]
        if update and self._adapter_index[_Constants.UPDATING] is False:
            self.update(data_points=["adapter_index"], wait_for_completion=wait_for_completion)
        return value

    def get_addressing_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._addressing_mode[_Constants.VALUE]
        if update and self._addressing_mode[_Constants.UPDATING] is False:
            self.update(data_points=["addressing_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_availability(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._availability[_Constants.VALUE]
        if update and self._availability[_Constants.UPDATING] is False:
            self.update(data_points=["availability"], wait_for_completion=wait_for_completion)
        return value

    def get_capability_descriptions(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._capability_descriptions[_Constants.VALUE]
        if update and self._capability_descriptions[_Constants.UPDATING] is False:
            self.update(data_points=["capability_descriptions"], wait_for_completion=wait_for_completion)
        return value

    def get_caption(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._caption[_Constants.VALUE]
        if update and self._caption[_Constants.UPDATING] is False:
            self.update(data_points=["caption"], wait_for_completion=wait_for_completion)
        return value

    def get_chip_to_chip_interconnect_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._chip_to_chip_interconnect_mode[_Constants.VALUE]
        if update and self._chip_to_chip_interconnect_mode[_Constants.UPDATING] is False:
            self.update(data_points=["chip_to_chip_interconnect_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_as_bitmap(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_as_bitmap[_Constants.VALUE]
        if update and self._clock_event_reasons_as_bitmap[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_as_bitmap"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_application_setting(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_application_setting[_Constants.VALUE]
        if update and self._clock_event_reasons_application_setting[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_application_setting"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_is_hardware_limited(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_is_hardware_limited[_Constants.VALUE]
        if update and self._clock_event_reasons_is_hardware_limited[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_is_hardware_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_gpu_idle_limited(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_gpu_idle_limited[_Constants.VALUE]
        if update and self._clock_event_reasons_gpu_idle_limited[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_gpu_idle_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_software_power_limited(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_software_power_limited[_Constants.VALUE]
        if update and self._clock_event_reasons_software_power_limited[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_software_power_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_software_thermal_limited(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_software_thermal_limited[_Constants.VALUE]
        if update and self._clock_event_reasons_software_thermal_limited[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_software_thermal_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_power_break_slowdown_limited(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_power_break_slowdown_limited[_Constants.VALUE]
        if update and self._clock_event_reasons_power_break_slowdown_limited[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_power_break_slowdown_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_supported(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_supported[_Constants.VALUE]
        if update and self._clock_event_reasons_supported[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_sync_boost(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_sync_boost[_Constants.VALUE]
        if update and self._clock_event_reasons_sync_boost[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_sync_boost"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_thermal_limited(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._clock_event_reasons_thermal_limited[_Constants.VALUE]
        if update and self._clock_event_reasons_thermal_limited[_Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_thermal_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_color_table_entries(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._color_table_entries[_Constants.VALUE]
        if update and self._color_table_entries[_Constants.UPDATING] is False:
            self.update(data_points=["color_table_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_compute_cap(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._compute_cap[_Constants.VALUE]
        if update and self._compute_cap[_Constants.UPDATING] is False:
            self.update(data_points=["compute_cap"], wait_for_completion=wait_for_completion)
        return value

    def get_compute_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._compute_mode[_Constants.VALUE]
        if update and self._compute_mode[_Constants.UPDATING] is False:
            self.update(data_points=["compute_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_config_manager_error_code(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._config_manager_error_code[_Constants.VALUE]
        if update and self._config_manager_error_code[_Constants.UPDATING] is False:
            self.update(data_points=["config_manager_error_code"], wait_for_completion=wait_for_completion)
        return value

    def get_config_manager_user_config(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._config_manager_user_config[_Constants.VALUE]
        if update and self._config_manager_user_config[_Constants.UPDATING] is False:
            self.update(data_points=["config_manager_user_config"], wait_for_completion=wait_for_completion)
        return value

    def get_core_voltage(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._core_voltage[_Constants.VALUE]
        if update and self._core_voltage[_Constants.UPDATING] is False:
            self.update(data_points=["core_voltage"], wait_for_completion=wait_for_completion)
        return value

    def get_core_voltage_range(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._core_voltage_range[_Constants.VALUE]
        if update and self._core_voltage_range[_Constants.UPDATING] is False:
            self.update(data_points=["core_voltage_range"], wait_for_completion=wait_for_completion)
        return value

    def get_creation_class_name(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._creation_class_name[_Constants.VALUE]
        if update and self._creation_class_name[_Constants.UPDATING] is False:
            self.update(data_points=["creation_class_name"], wait_for_completion=wait_for_completion)
        return value

    def get_current_bits_per_pixel(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_bits_per_pixel[_Constants.VALUE]
        if update and self._current_bits_per_pixel[_Constants.UPDATING] is False:
            self.update(data_points=["current_bits_per_pixel"], wait_for_completion=wait_for_completion)
        return value

    def get_current_horizontal_resolution(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_horizontal_resolution[_Constants.VALUE]
        if update and self._current_horizontal_resolution[_Constants.UPDATING] is False:
            self.update(data_points=["current_horizontal_resolution"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_colors(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_number_of_colors[_Constants.VALUE]
        if update and self._current_number_of_colors[_Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_colors"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_columns(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_number_of_columns[_Constants.VALUE]
        if update and self._current_number_of_columns[_Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_columns"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_rows(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_number_of_rows[_Constants.VALUE]
        if update and self._current_number_of_rows[_Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_rows"], wait_for_completion=wait_for_completion)
        return value

    def get_current_refresh_rate(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_refresh_rate[_Constants.VALUE]
        if update and self._current_refresh_rate[_Constants.UPDATING] is False:
            self.update(data_points=["current_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_current_scan_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_scan_mode[_Constants.VALUE]
        if update and self._current_scan_mode[_Constants.UPDATING] is False:
            self.update(data_points=["current_scan_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_current_vertical_resolution(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._current_vertical_resolution[_Constants.VALUE]
        if update and self._current_vertical_resolution[_Constants.UPDATING] is False:
            self.update(data_points=["current_vertical_resolution"], wait_for_completion=wait_for_completion)
        return value

    def get_description(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._description[_Constants.VALUE]
        if update and self._description[_Constants.UPDATING] is False:
            self.update(data_points=["description"], wait_for_completion=wait_for_completion)
        return value

    def get_device_id(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._device_id[_Constants.VALUE]
        if update and self._device_id[_Constants.UPDATING] is False:
            self.update(data_points=["device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_device_specific_pens(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._device_specific_pens[_Constants.VALUE]
        if update and self._device_specific_pens[_Constants.UPDATING] is False:
            self.update(data_points=["device_specific_pens"], wait_for_completion=wait_for_completion)
        return value

    def get_display_active(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._display_active[_Constants.VALUE]
        if update and self._display_active[_Constants.UPDATING] is False:
            self.update(data_points=["display_active"], wait_for_completion=wait_for_completion)
        return value

    def get_display_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._display_mode[_Constants.VALUE]
        if update and self._display_mode[_Constants.UPDATING] is False:
            self.update(data_points=["display_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_dither_type(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._dither_type[_Constants.VALUE]
        if update and self._dither_type[_Constants.UPDATING] is False:
            self.update(data_points=["dither_type"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_date(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._driver_date[_Constants.VALUE]
        if update and self._driver_date[_Constants.UPDATING] is False:
            self.update(data_points=["driver_date"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_model_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._driver_model_current[_Constants.VALUE]
        if update and self._driver_model_current[_Constants.UPDATING] is False:
            self.update(data_points=["driver_model_current"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_model_pending(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._driver_model_pending[_Constants.VALUE]
        if update and self._driver_model_pending[_Constants.UPDATING] is False:
            self.update(data_points=["driver_model_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_version(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._driver_version[_Constants.VALUE]
        if update and self._driver_version[_Constants.UPDATING] is False:
            self.update(data_points=["driver_version"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_cbu(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_cbu[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_cbu[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_primary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_primary_cache[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_primary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_register_file(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_register_file[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_register_file[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_secondary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_secondary_cache[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_secondary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_shared_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_shared_memory[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_shared_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_sram(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_sram[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_sram[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_texture_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_texture_memory[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_texture_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_total(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_total[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_total[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_video_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_all_time_in_video_memory[_Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_video_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_cbu(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_cbu[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_cbu[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_primary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_primary_cache[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_primary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_register_file(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_register_file[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_register_file[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_secondary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_secondary_cache[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_secondary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_shared_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_shared_memory[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_shared_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_sram(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_sram[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_sram[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_texture_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_texture_memory[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_texture_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_total(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_total[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_total[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_video_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_corrected_since_reboot_in_video_memory[_Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_video_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_cbu(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_cbu[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_cbu[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_primary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_primary_cache[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_primary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_register_file(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_register_file[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_register_file[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_secondary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_secondary_cache[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_secondary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_shared_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_shared_memory[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_shared_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_sram(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_sram[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_sram[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_texture_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_texture_memory[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_texture_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_total(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_total[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_total[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_video_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_all_time_in_video_memory[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_video_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_cbu(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_cbu[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_cbu[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_primary_cache[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_primary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_register_file(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_register_file[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_register_file[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_shared_memory[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_shared_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_sram(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_sram[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_sram[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_texture_memory[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_texture_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_total(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_total[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_total[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_video_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_errors_uncorrected_since_reboot_in_video_memory[_Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_video_memory[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_mode_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_mode_current[_Constants.VALUE]
        if update and self._ecc_mode_current[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_mode_pending(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ecc_mode_pending[_Constants.VALUE]
        if update and self._ecc_mode_pending[_Constants.UPDATING] is False:
            self.update(data_points=["ecc_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_average_FPS(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._encoder_average_FPS[_Constants.VALUE]
        if update and self._encoder_average_FPS[_Constants.UPDATING] is False:
            self.update(data_points=["encoder_average_FPS"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_average_latency(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._encoder_average_latency[_Constants.VALUE]
        if update and self._encoder_average_latency[_Constants.UPDATING] is False:
            self.update(data_points=["encoder_average_latency"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_session_count(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._encoder_session_count[_Constants.VALUE]
        if update and self._encoder_session_count[_Constants.UPDATING] is False:
            self.update(data_points=["encoder_session_count"], wait_for_completion=wait_for_completion)
        return value

    def get_engine_clock_range(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._engine_clock_range[_Constants.VALUE]
        if update and self._engine_clock_range[_Constants.UPDATING] is False:
            self.update(data_points=["engine_clock_range"], wait_for_completion=wait_for_completion)
        return value

    def get_error_cleared(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._error_cleared[_Constants.VALUE]
        if update and self._error_cleared[_Constants.UPDATING] is False:
            self.update(data_points=["error_cleared"], wait_for_completion=wait_for_completion)
        return value

    def get_error_description(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._error_description[_Constants.VALUE]
        if update and self._error_description[_Constants.UPDATING] is False:
            self.update(data_points=["error_description"], wait_for_completion=wait_for_completion)
        return value

    def get_fabric_state(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fabric_state[_Constants.VALUE]
        if update and self._fabric_state[_Constants.UPDATING] is False:
            self.update(data_points=["fabric_state"], wait_for_completion=wait_for_completion)
        return value

    def get_fabric_status(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fabric_status[_Constants.VALUE]
        if update and self._fabric_status[_Constants.UPDATING] is False:
            self.update(data_points=["fabric_status"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_percentage(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fan_speed_percentage[_Constants.VALUE]
        if update and self._fan_speed_percentage[_Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_percentage"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_percentage_range(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fan_speed_percentage_range[_Constants.VALUE]
        if update and self._fan_speed_percentage_range[_Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_percentage_range"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_RPM(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fan_speed_RPM[_Constants.VALUE]
        if update and self._fan_speed_RPM[_Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_RPM"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_RPM_range(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fan_speed_RPM_range[_Constants.VALUE]
        if update and self._fan_speed_RPM_range[_Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_RPM_range"], wait_for_completion=wait_for_completion)
        return value

    def get_fractional_multi_vGPU(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._fractional_multi_vGPU[_Constants.VALUE]
        if update and self._fractional_multi_vGPU[_Constants.UPDATING] is False:
            self.update(data_points=["fractional_multi_vGPU"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_default_shader_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_application_default_shader_clock[_Constants.VALUE]
        if update and self._frequency_application_default_shader_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_default_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_default_memory_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_application_default_memory_clock[_Constants.VALUE]
        if update and self._frequency_application_default_memory_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_default_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_memory_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_application_memory_clock[_Constants.VALUE]
        if update and self._frequency_application_memory_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_shader_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_application_shader_clock[_Constants.VALUE]
        if update and self._frequency_application_shader_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_memory_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_maximum_memory_clock[_Constants.VALUE]
        if update and self._frequency_maximum_memory_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_shader_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_maximum_shader_clock[_Constants.VALUE]
        if update and self._frequency_maximum_shader_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_streaming_multiprocessor_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_maximum_streaming_multiprocessor_clock[_Constants.VALUE]
        if update and self._frequency_maximum_streaming_multiprocessor_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_memory_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_memory_clock[_Constants.VALUE]
        if update and self._frequency_memory_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_shader_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_shader_clock[_Constants.VALUE]
        if update and self._frequency_shader_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_streaming_multiprocessor_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_streaming_multiprocessor_clock[_Constants.VALUE]
        if update and self._frequency_streaming_multiprocessor_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_video_clock(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._frequency_video_clock[_Constants.VALUE]
        if update and self._frequency_video_clock[_Constants.UPDATING] is False:
            self.update(data_points=["frequency_video_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_multi_vGPU(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._heterogenous_multi_vGPU[_Constants.VALUE]
        if update and self._heterogenous_multi_vGPU[_Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_multi_vGPU"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_time_slice_profile(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._heterogenous_time_slice_profile[_Constants.VALUE]
        if update and self._heterogenous_time_slice_profile[_Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_time_slice_profile"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_time_slice_sizes(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._heterogenous_time_slice_sizes[_Constants.VALUE]
        if update and self._heterogenous_time_slice_sizes[_Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_time_slice_sizes"], wait_for_completion=wait_for_completion)
        return value

    def get_ICM_indent(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ICM_indent[_Constants.VALUE]
        if update and self._ICM_indent[_Constants.UPDATING] is False:
            self.update(data_points=["ICM_indent"], wait_for_completion=wait_for_completion)
        return value

    def get_ICM_method(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._ICM_method[_Constants.VALUE]
        if update and self._ICM_method[_Constants.UPDATING] is False:
            self.update(data_points=["ICM_method"], wait_for_completion=wait_for_completion)
        return value

    def get_inf_filename(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._inf_filename[_Constants.VALUE]
        if update and self._inf_filename[_Constants.UPDATING] is False:
            self.update(data_points=["inf_filename"], wait_for_completion=wait_for_completion)
        return value

    def get_inf_section(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._inf_section[_Constants.VALUE]
        if update and self._inf_section[_Constants.UPDATING] is False:
            self.update(data_points=["inf_section"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_ecc(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._info_ROM_ecc[_Constants.VALUE]
        if update and self._info_ROM_ecc[_Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_ecc"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_oem(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._info_ROM_oem[_Constants.VALUE]
        if update and self._info_ROM_oem[_Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_oem"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_power(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._info_ROM_power[_Constants.VALUE]
        if update and self._info_ROM_power[_Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_power"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_version(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._info_ROM_version[_Constants.VALUE]
        if update and self._info_ROM_version[_Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_version"], wait_for_completion=wait_for_completion)
        return value

    def get_install_date(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._install_date[_Constants.VALUE]
        if update and self._install_date[_Constants.UPDATING] is False:
            self.update(data_points=["install_date"], wait_for_completion=wait_for_completion)
        return value

    def get_installed_display_drivers(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._installed_display_drivers[_Constants.VALUE]
        if update and self._installed_display_drivers[_Constants.UPDATING] is False:
            self.update(data_points=["installed_display_drivers"], wait_for_completion=wait_for_completion)
        return value

    def get_last_error_code(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._last_error_code[_Constants.VALUE]
        if update and self._last_error_code[_Constants.UPDATING] is False:
            self.update(data_points=["last_error_code"], wait_for_completion=wait_for_completion)
        return value

    def get_max_memory_supported(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._max_memory_supported[_Constants.VALUE]
        if update and self._max_memory_supported[_Constants.UPDATING] is False:
            self.update(data_points=["max_memory_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_max_number_controlled(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._max_number_controlled[_Constants.VALUE]
        if update and self._max_number_controlled[_Constants.UPDATING] is False:
            self.update(data_points=["max_number_controlled"], wait_for_completion=wait_for_completion)
        return value

    def get_max_refresh_rate(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._max_refresh_rate[_Constants.VALUE]
        if update and self._max_refresh_rate[_Constants.UPDATING] is False:
            self.update(data_points=["max_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_clock_range(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._memory_clock_range[_Constants.VALUE]
        if update and self._memory_clock_range[_Constants.UPDATING] is False:
            self.update(data_points=["memory_clock_range"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_free(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._memory_free[_Constants.VALUE]
        if update and self._memory_free[_Constants.UPDATING] is False:
            self.update(data_points=["memory_free"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_reserved(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._memory_reserved[_Constants.VALUE]
        if update and self._memory_reserved[_Constants.UPDATING] is False:
            self.update(data_points=["memory_reserved"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_total(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._memory_total[_Constants.VALUE]
        if update and self._memory_total[_Constants.UPDATING] is False:
            self.update(data_points=["memory_total"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_used(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._memory_used[_Constants.VALUE]
        if update and self._memory_used[_Constants.UPDATING] is False:
            self.update(data_points=["memory_used"], wait_for_completion=wait_for_completion)
        return value

    def get_min_refresh_rate(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._min_refresh_rate[_Constants.VALUE]
        if update and self._min_refresh_rate[_Constants.UPDATING] is False:
            self.update(data_points=["min_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_monochrome(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._monochrome[_Constants.VALUE]
        if update and self._monochrome[_Constants.UPDATING] is False:
            self.update(data_points=["monochrome"], wait_for_completion=wait_for_completion)
        return value

    def get_multi_instance_GPU_mode_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._multi_instance_GPU_mode_current[_Constants.VALUE]
        if update and self._multi_instance_GPU_mode_current[_Constants.UPDATING] is False:
            self.update(data_points=["multi_instance_GPU_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_multi_instance_GPU_mode_pending(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._multi_instance_GPU_mode_pending[_Constants.VALUE]
        if update and self._multi_instance_GPU_mode_pending[_Constants.UPDATING] is False:
            self.update(data_points=["multi_instance_GPU_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_name(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._name[_Constants.VALUE]
        if update and self._name[_Constants.UPDATING] is False:
            self.update(data_points=["name"], wait_for_completion=wait_for_completion)
        return value

    def get_number_of_color_planes(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._number_of_color_planes[_Constants.VALUE]
        if update and self._number_of_color_planes[_Constants.UPDATING] is False:
            self.update(data_points=["number_of_color_planes"], wait_for_completion=wait_for_completion)
        return value

    def get_number_of_video_pages(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._number_of_video_pages[_Constants.VALUE]
        if update and self._number_of_video_pages[_Constants.UPDATING] is False:
            self.update(data_points=["number_of_video_pages"], wait_for_completion=wait_for_completion)
        return value

    def get_operating_mode_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._operating_mode_current[_Constants.VALUE]
        if update and self._operating_mode_current[_Constants.UPDATING] is False:
            self.update(data_points=["operating_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_operating_mode_pending(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._operating_mode_pending[_Constants.VALUE]
        if update and self._operating_mode_pending[_Constants.UPDATING] is False:
            self.update(data_points=["operating_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_bus(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_bus[_Constants.VALUE]
        if update and self._pci_bus[_Constants.UPDATING] is False:
            self.update(data_points=["pci_bus"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_bus_id(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_bus_id[_Constants.VALUE]
        if update and self._pci_bus_id[_Constants.UPDATING] is False:
            self.update(data_points=["pci_bus_id"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_device(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_device[_Constants.VALUE]
        if update and self._pci_device[_Constants.UPDATING] is False:
            self.update(data_points=["pci_device"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_device_id(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_device_id[_Constants.VALUE]
        if update and self._pci_device_id[_Constants.UPDATING] is False:
            self.update(data_points=["pci_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_domain(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_domain[_Constants.VALUE]
        if update and self._pci_domain[_Constants.UPDATING] is False:
            self.update(data_points=["pci_domain"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_link_generation_current[_Constants.VALUE]
        if update and self._pci_link_generation_current[_Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_current"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_device_host_maximum(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_link_generation_device_host_maximum[_Constants.VALUE]
        if update and self._pci_link_generation_device_host_maximum[_Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_device_host_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_gpu_maximum(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_link_generation_gpu_maximum[_Constants.VALUE]
        if update and self._pci_link_generation_gpu_maximum[_Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_gpu_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_maximum(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_link_generation_maximum[_Constants.VALUE]
        if update and self._pci_link_generation_maximum[_Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_width_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_link_width_current[_Constants.VALUE]
        if update and self._pci_link_width_current[_Constants.UPDATING] is False:
            self.update(data_points=["pci_link_width_current"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_width_maximum(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_link_width_maximum[_Constants.VALUE]
        if update and self._pci_link_width_maximum[_Constants.UPDATING] is False:
            self.update(data_points=["pci_link_width_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_sub_device_id(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._pci_sub_device_id[_Constants.VALUE]
        if update and self._pci_sub_device_id[_Constants.UPDATING] is False:
            self.update(data_points=["pci_sub_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_persistence_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._persistence_mode[_Constants.VALUE]
        if update and self._persistence_mode[_Constants.UPDATING] is False:
            self.update(data_points=["persistence_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_PNP_device_id(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._PNP_device_id[_Constants.VALUE]
        if update and self._PNP_device_id[_Constants.UPDATING] is False:
            self.update(data_points=["PNP_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw[_Constants.VALUE]
        if update and self._power_draw[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_average(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_average[_Constants.VALUE]
        if update and self._power_draw_average[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_average"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_default_limit(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_default_limit[_Constants.VALUE]
        if update and self._power_draw_default_limit[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_default_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_enforced_limit(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_enforced_limit[_Constants.VALUE]
        if update and self._power_draw_enforced_limit[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_enforced_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_instant(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_instant[_Constants.VALUE]
        if update and self._power_draw_instant[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_instant"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_limit(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_limit[_Constants.VALUE]
        if update and self._power_draw_limit[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_maximum(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_maximum[_Constants.VALUE]
        if update and self._power_draw_maximum[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_minimum(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_draw_minimum[_Constants.VALUE]
        if update and self._power_draw_minimum[_Constants.UPDATING] is False:
            self.update(data_points=["power_draw_minimum"], wait_for_completion=wait_for_completion)
        return value

    def get_power_management_capabilities(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_management_capabilities[_Constants.VALUE]
        if update and self._power_management_capabilities[_Constants.UPDATING] is False:
            self.update(data_points=["power_management_capabilities"], wait_for_completion=wait_for_completion)
        return value

    def get_power_management_supported(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._power_management_supported[_Constants.VALUE]
        if update and self._power_management_supported[_Constants.UPDATING] is False:
            self.update(data_points=["power_management_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_free(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._protected_memory_free[_Constants.VALUE]
        if update and self._protected_memory_free[_Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_free"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_total(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._protected_memory_total[_Constants.VALUE]
        if update and self._protected_memory_total[_Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_total"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_used(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._protected_memory_used[_Constants.VALUE]
        if update and self._protected_memory_used[_Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_used"], wait_for_completion=wait_for_completion)
        return value

    def get_protocol_supported(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._protocol_supported[_Constants.VALUE]
        if update and self._protocol_supported[_Constants.UPDATING] is False:
            self.update(data_points=["protocol_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_performance_state(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._performance_state[_Constants.VALUE]
        if update and self._performance_state[_Constants.UPDATING] is False:
            self.update(data_points=["performance_state"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_double_bit_ecc_errors_count(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._retired_pages_double_bit_ecc_errors_count[_Constants.VALUE]
        if update and self._retired_pages_double_bit_ecc_errors_count[_Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_double_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_single_bit_ecc_errors_count(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._retired_pages_single_bit_ecc_errors_count[_Constants.VALUE]
        if update and self._retired_pages_single_bit_ecc_errors_count[_Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_single_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_pending(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._retired_pages_pending[_Constants.VALUE]
        if update and self._retired_pages_pending[_Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_reserved_system_palette_entries(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._reserved_system_palette_entries[_Constants.VALUE]
        if update and self._reserved_system_palette_entries[_Constants.UPDATING] is False:
            self.update(data_points=["reserved_system_palette_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_reset_required(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._reset_required[_Constants.VALUE]
        if update and self._reset_required[_Constants.UPDATING] is False:
            self.update(data_points=["reset_required"], wait_for_completion=wait_for_completion)
        return value

    def get_reset_and_drain_recommended(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._reset_and_drain_recommended[_Constants.VALUE]
        if update and self._reset_and_drain_recommended[_Constants.UPDATING] is False:
            self.update(data_points=["reset_and_drain_recommended"], wait_for_completion=wait_for_completion)
        return value

    def get_serial(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._serial[_Constants.VALUE]
        if update and self._serial[_Constants.UPDATING] is False:
            self.update(data_points=["serial"], wait_for_completion=wait_for_completion)
        return value

    def get_specification_version(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._specification_version[_Constants.VALUE]
        if update and self._specification_version[_Constants.UPDATING] is False:
            self.update(data_points=["specification_version"], wait_for_completion=wait_for_completion)
        return value

    def get_status(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._status[_Constants.VALUE]
        if update and self._status[_Constants.UPDATING] is False:
            self.update(data_points=["status"], wait_for_completion=wait_for_completion)
        return value

    def get_status_info(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._status_info[_Constants.VALUE]
        if update and self._status_info[_Constants.UPDATING] is False:
            self.update(data_points=["status_info"], wait_for_completion=wait_for_completion)
        return value

    def get_system_creation_class_name(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._system_creation_class_name[_Constants.VALUE]
        if update and self._system_creation_class_name[_Constants.UPDATING] is False:
            self.update(data_points=["system_creation_class_name"], wait_for_completion=wait_for_completion)
        return value

    def get_system_name(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._system_name[_Constants.VALUE]
        if update and self._system_name[_Constants.UPDATING] is False:
            self.update(data_points=["system_name"], wait_for_completion=wait_for_completion)
        return value

    def get_system_palette_entries(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._system_palette_entries[_Constants.VALUE]
        if update and self._system_palette_entries[_Constants.UPDATING] is False:
            self.update(data_points=["system_palette_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_GPU_system_processor_mode_current(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._GPU_system_processor_mode_current[_Constants.VALUE]
        if update and self._GPU_system_processor_mode_current[_Constants.UPDATING] is False:
            self.update(data_points=["GPU_system_processor_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_GPU_system_processor_mode_default(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._GPU_system_processor_mode_default[_Constants.VALUE]
        if update and self._GPU_system_processor_mode_default[_Constants.UPDATING] is False:
            self.update(data_points=["GPU_system_processor_mode_default"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_core(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._temperature_core[_Constants.VALUE]
        if update and self._temperature_core[_Constants.UPDATING] is False:
            self.update(data_points=["temperature_core"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_core_limit(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._temperature_core_limit[_Constants.VALUE]
        if update and self._temperature_core_limit[_Constants.UPDATING] is False:
            self.update(data_points=["temperature_core_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._temperature_memory[_Constants.VALUE]
        if update and self._temperature_memory[_Constants.UPDATING] is False:
            self.update(data_points=["temperature_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_time_of_last_reset(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._time_of_last_reset[_Constants.VALUE]
        if update and self._time_of_last_reset[_Constants.UPDATING] is False:
            self.update(data_points=["time_of_last_reset"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_decoder(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._utilization_decoder[_Constants.VALUE]
        if update and self._utilization_decoder[_Constants.UPDATING] is False:
            self.update(data_points=["utilization_decoder"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_encoder(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._utilization_encoder[_Constants.VALUE]
        if update and self._utilization_encoder[_Constants.UPDATING] is False:
            self.update(data_points=["utilization_encoder"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_gpu(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._utilization_gpu[_Constants.VALUE]
        if update and self._utilization_gpu[_Constants.UPDATING] is False:
            self.update(data_points=["utilization_gpu"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_jpeg(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._utilization_jpeg[_Constants.VALUE]
        if update and self._utilization_jpeg[_Constants.UPDATING] is False:
            self.update(data_points=["utilization_jpeg"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_memory(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._utilization_memory[_Constants.VALUE]
        if update and self._utilization_memory[_Constants.UPDATING] is False:
            self.update(data_points=["utilization_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_optical_flow(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._utilization_optical_flow[_Constants.VALUE]
        if update and self._utilization_optical_flow[_Constants.UPDATING] is False:
            self.update(data_points=["utilization_optical_flow"], wait_for_completion=wait_for_completion)
        return value

    def get_uuid(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._uuid[_Constants.VALUE]
        if update and self._uuid[_Constants.UPDATING] is False:
            self.update(data_points=["uuid"], wait_for_completion=wait_for_completion)
        return value

    def get_vbios_version(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._vbios_version[_Constants.VALUE]
        if update and self._vbios_version[_Constants.UPDATING] is False:
            self.update(data_points=["vbios_version"], wait_for_completion=wait_for_completion)
        return value

    def get_video_architecture(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._video_architecture[_Constants.VALUE]
        if update and self._video_architecture[_Constants.UPDATING] is False:
            self.update(data_points=["video_architecture"], wait_for_completion=wait_for_completion)
        return value

    def get_video_memory_type(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._video_memory_type[_Constants.VALUE]
        if update and self._video_memory_type[_Constants.UPDATING] is False:
            self.update(data_points=["video_memory_type"], wait_for_completion=wait_for_completion)
        return value

    def get_video_mode(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._video_mode[_Constants.VALUE]
        if update and self._video_mode[_Constants.UPDATING] is False:
            self.update(data_points=["video_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_video_mode_description(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._video_mode_description[_Constants.VALUE]
        if update and self._video_mode_description[_Constants.UPDATING] is False:
            self.update(data_points=["video_mode_description"], wait_for_completion=wait_for_completion)
        return value

    def get_video_processor(self, update=False, wait_for_completion=False):
        """
        🟩 **R** -
        """
        value = self._video_processor[_Constants.VALUE]
        if update and self._video_processor[_Constants.UPDATING] is False:
            self.update(data_points=["video_processor"], wait_for_completion=wait_for_completion)
        return value

    def set_accelerator_capabilities(self, value=None):
        """
        🟩 **R** -
        """
        self._accelerator_capabilities[_Constants.MANUALLY_SET] = value != None
        self._accelerator_capabilities = value

    def set_accounting_mode_enabled(self, value=None):
        """
        🟩 **R** -
        """
        self._accounting_mode_enabled[_Constants.MANUALLY_SET] = value != None
        self._accounting_mode_enabled = value

    def set_accounting_mode_buffer_size(self, value=None):
        """
        🟩 **R** -
        """
        self._accounting_mode_buffer_size[_Constants.MANUALLY_SET] = value != None
        self._accounting_mode_buffer_size = value

    def set_adapter_compatibility(self, value=None):
        """
        🟩 **R** -
        """
        self._adapter_compatibility[_Constants.MANUALLY_SET] = value != None
        self._adapter_compatibility = value

    def set_adapter_DAC_type(self, value=None):
        """
        🟩 **R** -
        """
        self._adapter_DAC_type[_Constants.MANUALLY_SET] = value != None
        self._adapter_DAC_type = value

    def set_adapter_id(self, value=None):
        """
        🟩 **R** -
        """
        self._adapter_id[_Constants.MANUALLY_SET] = value != None
        self._adapter_id = value

    def set_adapter_index(self, value=None):
        """
        🟩 **R** -
        """
        self._adapter_index[_Constants.MANUALLY_SET] = value != None
        self._adapter_index = value

    def set_addressing_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._addressing_mode[_Constants.MANUALLY_SET] = value != None
        self._addressing_mode = value

    def set_availability(self, value=None):
        """
        🟩 **R** -
        """
        self._availability[_Constants.MANUALLY_SET] = value != None
        self._availability = value

    def set_capability_descriptions(self, value=None):
        """
        🟩 **R** -
        """
        self._capability_descriptions[_Constants.MANUALLY_SET] = value != None
        self._capability_descriptions = value

    def set_caption(self, value=None):
        """
        🟩 **R** -
        """
        self._caption[_Constants.MANUALLY_SET] = value != None
        self._caption = value

    def set_chip_to_chip_interconnect_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._chip_to_chip_interconnect_mode[_Constants.MANUALLY_SET] = value != None
        self._chip_to_chip_interconnect_mode = value

    def set_clock_event_reasons_as_bitmap(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_as_bitmap[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_as_bitmap = value

    def set_clock_event_reasons_application_setting(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_application_setting[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_application_setting = value

    def set_clock_event_reasons_is_hardware_limited(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_is_hardware_limited[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_is_hardware_limited = value

    def set_clock_event_reasons_gpu_idle_limited(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_gpu_idle_limited[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_gpu_idle_limited = value

    def set_clock_event_reasons_software_power_limited(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_software_power_limited[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_software_power_limited = value

    def set_clock_event_reasons_software_thermal_limited(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_software_thermal_limited[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_software_thermal_limited = value

    def set_clock_event_reasons_power_break_slowdown_limited(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_power_break_slowdown_limited[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_power_break_slowdown_limited = value

    def set_clock_event_reasons_supported(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_supported[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_supported = value

    def set_clock_event_reasons_sync_boost(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_sync_boost[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_sync_boost = value

    def set_clock_event_reasons_thermal_limited(self, value=None):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_thermal_limited[_Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_thermal_limited = value

    def set_color_table_entries(self, value=None):
        """
        🟩 **R** -
        """
        self._color_table_entries[_Constants.MANUALLY_SET] = value != None
        self._color_table_entries = value

    def set_compute_cap(self, value=None):
        """
        🟩 **R** -
        """
        self._compute_cap[_Constants.MANUALLY_SET] = value != None
        self._compute_cap = value

    def set_compute_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._compute_mode[_Constants.MANUALLY_SET] = value != None
        self._compute_mode = value

    def set_config_manager_error_code(self, value=None):
        """
        🟩 **R** -
        """
        self._config_manager_error_code[_Constants.MANUALLY_SET] = value != None
        self._config_manager_error_code = value

    def set_config_manager_user_config(self, value=None):
        """
        🟩 **R** -
        """
        self._config_manager_user_config[_Constants.MANUALLY_SET] = value != None
        self._config_manager_user_config = value

    def set_core_voltage(self, value=None):
        """
        🟩 **R** -
        """
        self._core_voltage[_Constants.MANUALLY_SET] = value != None
        self._core_voltage = value

    def set_core_voltage_range(self, value=None):
        """
        🟩 **R** -
        """
        self._core_voltage_range[_Constants.MANUALLY_SET] = value != None
        self._core_voltage_range = value

    def set_creation_class_name(self, value=None):
        """
        🟩 **R** -
        """
        self._creation_class_name[_Constants.MANUALLY_SET] = value != None
        self._creation_class_name = value

    def set_current_bits_per_pixel(self, value=None):
        """
        🟩 **R** -
        """
        self._current_bits_per_pixel[_Constants.MANUALLY_SET] = value != None
        self._current_bits_per_pixel = value

    def set_current_horizontal_resolution(self, value=None):
        """
        🟩 **R** -
        """
        self._current_horizontal_resolution[_Constants.MANUALLY_SET] = value != None
        self._current_horizontal_resolution = value

    def set_current_number_of_colors(self, value=None):
        """
        🟩 **R** -
        """
        self._current_number_of_colors[_Constants.MANUALLY_SET] = value != None
        self._current_number_of_colors = value

    def set_current_number_of_columns(self, value=None):
        """
        🟩 **R** -
        """
        self._current_number_of_columns[_Constants.MANUALLY_SET] = value != None
        self._current_number_of_columns = value

    def set_current_number_of_rows(self, value=None):
        """
        🟩 **R** -
        """
        self._current_number_of_rows[_Constants.MANUALLY_SET] = value != None
        self._current_number_of_rows = value

    def set_current_refresh_rate(self, value=None):
        """
        🟩 **R** -
        """
        self._current_refresh_rate[_Constants.MANUALLY_SET] = value != None
        self._current_refresh_rate = value

    def set_current_scan_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._current_scan_mode[_Constants.MANUALLY_SET] = value != None
        self._current_scan_mode = value

    def set_current_vertical_resolution(self, value=None):
        """
        🟩 **R** -
        """
        self._current_vertical_resolution[_Constants.MANUALLY_SET] = value != None
        self._current_vertical_resolution = value

    def set_description(self, value=None):
        """
        🟩 **R** -
        """
        self._description[_Constants.MANUALLY_SET] = value != None
        self._description = value

    def set_device_id(self, value=None):
        """
        🟩 **R** -
        """
        self._device_id[_Constants.MANUALLY_SET] = value != None
        self._device_id = value

    def set_device_specific_pens(self, value=None):
        """
        🟩 **R** -
        """
        self._device_specific_pens[_Constants.MANUALLY_SET] = value != None
        self._device_specific_pens = value

    def set_display_active(self, value=None):
        """
        🟩 **R** -
        """
        self._display_active[_Constants.MANUALLY_SET] = value != None
        self._display_active = value

    def set_display_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._display_mode[_Constants.MANUALLY_SET] = value != None
        self._display_mode = value

    def set_dither_type(self, value=None):
        """
        🟩 **R** -
        """
        self._dither_type[_Constants.MANUALLY_SET] = value != None
        self._dither_type = value

    def set_driver_date(self, value=None):
        """
        🟩 **R** -
        """
        self._driver_date[_Constants.MANUALLY_SET] = value != None
        self._driver_date = value

    def set_driver_model_current(self, value=None):
        """
        🟩 **R** -
        """
        self._driver_model_current[_Constants.MANUALLY_SET] = value != None
        self._driver_model_current = value

    def set_driver_model_pending(self, value=None):
        """
        🟩 **R** -
        """
        self._driver_model_pending[_Constants.MANUALLY_SET] = value != None
        self._driver_model_pending = value

    def set_driver_version(self, value=None):
        """
        🟩 **R** -
        """
        self._driver_version[_Constants.MANUALLY_SET] = value != None
        self._driver_version = value

    def set_ecc_errors_corrected_all_time_in_cbu(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_cbu[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_cbu = value

    def set_ecc_errors_corrected_all_time_in_primary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_primary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_primary_cache = value

    def set_ecc_errors_corrected_all_time_in_register_file(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_register_file[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_register_file = value

    def set_ecc_errors_corrected_all_time_in_secondary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_secondary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_secondary_cache = value

    def set_ecc_errors_corrected_all_time_in_shared_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_shared_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_shared_memory = value

    def set_ecc_errors_corrected_all_time_in_sram(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_sram[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_sram = value

    def set_ecc_errors_corrected_all_time_in_texture_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_texture_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_texture_memory = value

    def set_ecc_errors_corrected_all_time_in_total(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_total[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_total = value

    def set_ecc_errors_corrected_all_time_in_video_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_video_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_video_memory = value

    def set_ecc_errors_corrected_since_reboot_in_cbu(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_cbu[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_cbu = value

    def set_ecc_errors_corrected_since_reboot_in_primary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_primary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_register_file(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_register_file[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_register_file = value

    def set_ecc_errors_corrected_since_reboot_in_secondary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_secondary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_shared_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_shared_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_corrected_since_reboot_in_sram(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_sram[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_sram = value

    def set_ecc_errors_corrected_since_reboot_in_texture_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_texture_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_corrected_since_reboot_in_total(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_total[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_total = value

    def set_ecc_errors_corrected_since_reboot_in_video_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_video_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_video_memory = value

    def set_ecc_errors_uncorrected_all_time_in_cbu(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_cbu[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_cbu = value

    def set_ecc_errors_uncorrected_all_time_in_primary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_primary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_primary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_register_file(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_register_file[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_register_file = value

    def set_ecc_errors_uncorrected_all_time_in_secondary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_secondary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_secondary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_shared_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_shared_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_shared_memory = value

    def set_ecc_errors_uncorrected_all_time_in_sram(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_sram[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_sram = value

    def set_ecc_errors_uncorrected_all_time_in_texture_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_texture_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_texture_memory = value

    def set_ecc_errors_uncorrected_all_time_in_total(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_total[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_total = value

    def set_ecc_errors_uncorrected_all_time_in_video_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_video_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_video_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_cbu(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_cbu[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_cbu = value

    def set_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_register_file(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_register_file[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_register_file = value

    def set_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_sram(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_sram[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_sram = value

    def set_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_total(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_total[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_total = value

    def set_ecc_errors_uncorrected_since_reboot_in_video_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_video_memory[_Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_video_memory = value

    def set_ecc_mode_current(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_mode_current[_Constants.MANUALLY_SET] = value != None
        self._ecc_mode_current = value

    def set_ecc_mode_pending(self, value=None):
        """
        🟩 **R** -
        """
        self._ecc_mode_pending[_Constants.MANUALLY_SET] = value != None
        self._ecc_mode_pending = value

    def set_encoder_average_FPS(self, value=None):
        """
        🟩 **R** -
        """
        self._encoder_average_FPS[_Constants.MANUALLY_SET] = value != None
        self._encoder_average_FPS = value

    def set_encoder_average_latency(self, value=None):
        """
        🟩 **R** -
        """
        self._encoder_average_latency[_Constants.MANUALLY_SET] = value != None
        self._encoder_average_latency = value

    def set_encoder_session_count(self, value=None):
        """
        🟩 **R** -
        """
        self._encoder_session_count[_Constants.MANUALLY_SET] = value != None
        self._encoder_session_count = value

    def set_engine_clock_range(self, value=None):
        """
        🟩 **R** -
        """
        self._engine_clock_range[_Constants.MANUALLY_SET] = value != None
        self._engine_clock_range = value

    def set_error_cleared(self, value=None):
        """
        🟩 **R** -
        """
        self._error_cleared[_Constants.MANUALLY_SET] = value != None
        self._error_cleared = value

    def set_error_description(self, value=None):
        """
        🟩 **R** -
        """
        self._error_description[_Constants.MANUALLY_SET] = value != None
        self._error_description = value

    def set_fabric_state(self, value=None):
        """
        🟩 **R** -
        """
        self._fabric_state[_Constants.MANUALLY_SET] = value != None
        self._fabric_state = value

    def set_fabric_status(self, value=None):
        """
        🟩 **R** -
        """
        self._fabric_status[_Constants.MANUALLY_SET] = value != None
        self._fabric_status = value

    def set_fan_speed_percentage(self, value=None):
        """
        🟩 **R** -
        """
        self._fan_speed_percentage[_Constants.MANUALLY_SET] = value != None
        self._fan_speed_percentage = value

    def set_fan_speed_percentage_range(self, value=None):
        """
        🟩 **R** -
        """
        self._fan_speed_percentage_range[_Constants.MANUALLY_SET] = value != None
        self._fan_speed_percentage_range = value

    def set_fan_speed_RPM(self, value=None):
        """
        🟩 **R** -
        """
        self._fan_speed_RPM[_Constants.MANUALLY_SET] = value != None
        self._fan_speed_RPM = value

    def set_fan_speed_RPM_range(self, value=None):
        """
        🟩 **R** -
        """
        self._fan_speed_RPM_range[_Constants.MANUALLY_SET] = value != None
        self._fan_speed_RPM_range = value

    def set_fractional_multi_vGPU(self, value=None):
        """
        🟩 **R** -
        """
        self._fractional_multi_vGPU[_Constants.MANUALLY_SET] = value != None
        self._fractional_multi_vGPU = value

    def set_frequency_application_default_shader_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_application_default_shader_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_application_default_shader_clock = value

    def set_frequency_application_default_memory_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_application_default_memory_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_application_default_memory_clock = value

    def set_frequency_application_memory_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_application_memory_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_application_memory_clock = value

    def set_frequency_application_shader_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_application_shader_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_application_shader_clock = value

    def set_frequency_maximum_memory_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_maximum_memory_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_maximum_memory_clock = value

    def set_frequency_maximum_shader_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_maximum_shader_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_maximum_shader_clock = value

    def set_frequency_maximum_streaming_multiprocessor_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_maximum_streaming_multiprocessor_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_maximum_streaming_multiprocessor_clock = value

    def set_frequency_memory_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_memory_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_memory_clock = value

    def set_frequency_shader_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_shader_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_shader_clock = value

    def set_frequency_streaming_multiprocessor_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_streaming_multiprocessor_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_streaming_multiprocessor_clock = value

    def set_frequency_video_clock(self, value=None):
        """
        🟩 **R** -
        """
        self._frequency_video_clock[_Constants.MANUALLY_SET] = value != None
        self._frequency_video_clock = value

    def set_heterogenous_multi_vGPU(self, value=None):
        """
        🟩 **R** -
        """
        self._heterogenous_multi_vGPU[_Constants.MANUALLY_SET] = value != None
        self._heterogenous_multi_vGPU = value

    def set_heterogenous_time_slice_profile(self, value=None):
        """
        🟩 **R** -
        """
        self._heterogenous_time_slice_profile[_Constants.MANUALLY_SET] = value != None
        self._heterogenous_time_slice_profile = value

    def set_heterogenous_time_slice_sizes(self, value=None):
        """
        🟩 **R** -
        """
        self._heterogenous_time_slice_sizes[_Constants.MANUALLY_SET] = value != None
        self._heterogenous_time_slice_sizes = value

    def set_ICM_indent(self, value=None):
        """
        🟩 **R** -
        """
        self._ICM_indent[_Constants.MANUALLY_SET] = value != None
        self._ICM_indent = value

    def set_ICM_method(self, value=None):
        """
        🟩 **R** -
        """
        self._ICM_method[_Constants.MANUALLY_SET] = value != None
        self._ICM_method = value

    def set_inf_filename(self, value=None):
        """
        🟩 **R** -
        """
        self._inf_filename[_Constants.MANUALLY_SET] = value != None
        self._inf_filename = value

    def set_inf_section(self, value=None):
        """
        🟩 **R** -
        """
        self._inf_section[_Constants.MANUALLY_SET] = value != None
        self._inf_section = value

    def set_info_ROM_ecc(self, value=None):
        """
        🟩 **R** -
        """
        self._info_ROM_ecc[_Constants.MANUALLY_SET] = value != None
        self._info_ROM_ecc = value

    def set_info_ROM_oem(self, value=None):
        """
        🟩 **R** -
        """
        self._info_ROM_oem[_Constants.MANUALLY_SET] = value != None
        self._info_ROM_oem = value

    def set_info_ROM_power(self, value=None):
        """
        🟩 **R** -
        """
        self._info_ROM_power[_Constants.MANUALLY_SET] = value != None
        self._info_ROM_power = value

    def set_info_ROM_version(self, value=None):
        """
        🟩 **R** -
        """
        self._info_ROM_version[_Constants.MANUALLY_SET] = value != None
        self._info_ROM_version = value

    def set_install_date(self, value=None):
        """
        🟩 **R** -
        """
        self._install_date[_Constants.MANUALLY_SET] = value != None
        self._install_date = value

    def set_installed_display_drivers(self, value=None):
        """
        🟩 **R** -
        """
        self._installed_display_drivers[_Constants.MANUALLY_SET] = value != None
        self._installed_display_drivers = value

    def set_last_error_code(self, value=None):
        """
        🟩 **R** -
        """
        self._last_error_code[_Constants.MANUALLY_SET] = value != None
        self._last_error_code = value

    def set_max_memory_supported(self, value=None):
        """
        🟩 **R** -
        """
        self._max_memory_supported[_Constants.MANUALLY_SET] = value != None
        self._max_memory_supported = value

    def set_max_number_controlled(self, value=None):
        """
        🟩 **R** -
        """
        self._max_number_controlled[_Constants.MANUALLY_SET] = value != None
        self._max_number_controlled = value

    def set_max_refresh_rate(self, value=None):
        """
        🟩 **R** -
        """
        self._max_refresh_rate[_Constants.MANUALLY_SET] = value != None
        self._max_refresh_rate = value

    def set_memory_clock_range(self, value=None):
        """
        🟩 **R** -
        """
        self._memory_clock_range[_Constants.MANUALLY_SET] = value != None
        self._memory_clock_range = value

    def set_memory_free(self, value=None):
        """
        🟩 **R** -
        """
        self._memory_free[_Constants.MANUALLY_SET] = value != None
        self._memory_free = value

    def set_memory_reserved(self, value=None):
        """
        🟩 **R** -
        """
        self._memory_reserved[_Constants.MANUALLY_SET] = value != None
        self._memory_reserved = value

    def set_memory_total(self, value=None):
        """
        🟩 **R** -
        """
        self._memory_total[_Constants.MANUALLY_SET] = value != None
        self._memory_total = value

    def set_memory_used(self, value=None):
        """
        🟩 **R** -
        """
        self._memory_used[_Constants.MANUALLY_SET] = value != None
        self._memory_used = value

    def set_min_refresh_rate(self, value=None):
        """
        🟩 **R** -
        """
        self._min_refresh_rate[_Constants.MANUALLY_SET] = value != None
        self._min_refresh_rate = value

    def set_monochrome(self, value=None):
        """
        🟩 **R** -
        """
        self._monochrome[_Constants.MANUALLY_SET] = value != None
        self._monochrome = value

    def set_multi_instance_GPU_mode_current(self, value=None):
        """
        🟩 **R** -
        """
        self._multi_instance_GPU_mode_current[_Constants.MANUALLY_SET] = value != None
        self._multi_instance_GPU_mode_current = value

    def set_multi_instance_GPU_mode_pending(self, value=None):
        """
        🟩 **R** -
        """
        self._multi_instance_GPU_mode_pending[_Constants.MANUALLY_SET] = value != None
        self._multi_instance_GPU_mode_pending = value

    def set_name(self, value=None):
        """
        🟩 **R** -
        """
        self._name[_Constants.MANUALLY_SET] = value != None
        self._name = value

    def set_number_of_color_planes(self, value=None):
        """
        🟩 **R** -
        """
        self._number_of_color_planes[_Constants.MANUALLY_SET] = value != None
        self._number_of_color_planes = value

    def set_number_of_video_pages(self, value=None):
        """
        🟩 **R** -
        """
        self._number_of_video_pages[_Constants.MANUALLY_SET] = value != None
        self._number_of_video_pages = value

    def set_operating_mode_current(self, value=None):
        """
        🟩 **R** -
        """
        self._operating_mode_current[_Constants.MANUALLY_SET] = value != None
        self._operating_mode_current = value

    def set_operating_mode_pending(self, value=None):
        """
        🟩 **R** -
        """
        self._operating_mode_pending[_Constants.MANUALLY_SET] = value != None
        self._operating_mode_pending = value

    def set_pci_bus(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_bus[_Constants.MANUALLY_SET] = value != None
        self._pci_bus = value

    def set_pci_bus_id(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_bus_id[_Constants.MANUALLY_SET] = value != None
        self._pci_bus_id = value

    def set_pci_device(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_device[_Constants.MANUALLY_SET] = value != None
        self._pci_device = value

    def set_pci_device_id(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_device_id[_Constants.MANUALLY_SET] = value != None
        self._pci_device_id = value

    def set_pci_domain(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_domain[_Constants.MANUALLY_SET] = value != None
        self._pci_domain = value

    def set_pci_link_generation_current(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_link_generation_current[_Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_current = value

    def set_pci_link_generation_device_host_maximum(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_link_generation_device_host_maximum[_Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_device_host_maximum = value

    def set_pci_link_generation_gpu_maximum(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_link_generation_gpu_maximum[_Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_gpu_maximum = value

    def set_pci_link_generation_maximum(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_link_generation_maximum[_Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_maximum = value

    def set_pci_link_width_current(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_link_width_current[_Constants.MANUALLY_SET] = value != None
        self._pci_link_width_current = value

    def set_pci_link_width_maximum(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_link_width_maximum[_Constants.MANUALLY_SET] = value != None
        self._pci_link_width_maximum = value

    def set_pci_sub_device_id(self, value=None):
        """
        🟩 **R** -
        """
        self._pci_sub_device_id[_Constants.MANUALLY_SET] = value != None
        self._pci_sub_device_id = value

    def set_persistence_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._persistence_mode[_Constants.MANUALLY_SET] = value != None
        self._persistence_mode = value

    def set_PNP_device_id(self, value=None):
        """
        🟩 **R** -
        """
        self._PNP_device_id[_Constants.MANUALLY_SET] = value != None
        self._PNP_device_id = value

    def set_power_draw(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw[_Constants.MANUALLY_SET] = value != None
        self._power_draw = value

    def set_power_draw_average(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_average[_Constants.MANUALLY_SET] = value != None
        self._power_draw_average = value

    def set_power_draw_default_limit(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_default_limit[_Constants.MANUALLY_SET] = value != None
        self._power_draw_default_limit = value

    def set_power_draw_enforced_limit(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_enforced_limit[_Constants.MANUALLY_SET] = value != None
        self._power_draw_enforced_limit = value

    def set_power_draw_instant(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_instant[_Constants.MANUALLY_SET] = value != None
        self._power_draw_instant = value

    def set_power_draw_limit(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_limit[_Constants.MANUALLY_SET] = value != None
        self._power_draw_limit = value

    def set_power_draw_maximum(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_maximum[_Constants.MANUALLY_SET] = value != None
        self._power_draw_maximum = value

    def set_power_draw_minimum(self, value=None):
        """
        🟩 **R** -
        """
        self._power_draw_minimum[_Constants.MANUALLY_SET] = value != None
        self._power_draw_minimum = value

    def set_power_management_capabilities(self, value=None):
        """
        🟩 **R** -
        """
        self._power_management_capabilities[_Constants.MANUALLY_SET] = value != None
        self._power_management_capabilities = value

    def set_power_management_supported(self, value=None):
        """
        🟩 **R** -
        """
        self._power_management_supported[_Constants.MANUALLY_SET] = value != None
        self._power_management_supported = value

    def set_protected_memory_free(self, value=None):
        """
        🟩 **R** -
        """
        self._protected_memory_free[_Constants.MANUALLY_SET] = value != None
        self._protected_memory_free = value

    def set_protected_memory_total(self, value=None):
        """
        🟩 **R** -
        """
        self._protected_memory_total[_Constants.MANUALLY_SET] = value != None
        self._protected_memory_total = value

    def set_protected_memory_used(self, value=None):
        """
        🟩 **R** -
        """
        self._protected_memory_used[_Constants.MANUALLY_SET] = value != None
        self._protected_memory_used = value

    def set_protocol_supported(self, value=None):
        """
        🟩 **R** -
        """
        self._protocol_supported[_Constants.MANUALLY_SET] = value != None
        self._protocol_supported = value

    def set_performance_state(self, value=None):
        """
        🟩 **R** -
        """
        self._performance_state[_Constants.MANUALLY_SET] = value != None
        self._performance_state = value

    def set_retired_pages_double_bit_ecc_errors_count(self, value=None):
        """
        🟩 **R** -
        """
        self._retired_pages_double_bit_ecc_errors_count[_Constants.MANUALLY_SET] = value != None
        self._retired_pages_double_bit_ecc_errors_count = value

    def set_retired_pages_single_bit_ecc_errors_count(self, value=None):
        """
        🟩 **R** -
        """
        self._retired_pages_single_bit_ecc_errors_count[_Constants.MANUALLY_SET] = value != None
        self._retired_pages_single_bit_ecc_errors_count = value

    def set_retired_pages_pending(self, value=None):
        """
        🟩 **R** -
        """
        self._retired_pages_pending[_Constants.MANUALLY_SET] = value != None
        self._retired_pages_pending = value

    def set_reserved_system_palette_entries(self, value=None):
        """
        🟩 **R** -
        """
        self._reserved_system_palette_entries[_Constants.MANUALLY_SET] = value != None
        self._reserved_system_palette_entries = value

    def set_reset_required(self, value=None):
        """
        🟩 **R** -
        """
        self._reset_required[_Constants.MANUALLY_SET] = value != None
        self._reset_required = value

    def set_reset_and_drain_recommended(self, value=None):
        """
        🟩 **R** -
        """
        self._reset_and_drain_recommended[_Constants.MANUALLY_SET] = value != None
        self._reset_and_drain_recommended = value

    def set_serial(self, value=None):
        """
        🟩 **R** -
        """
        self._serial[_Constants.MANUALLY_SET] = value != None
        self._serial = value

    def set_specification_version(self, value=None):
        """
        🟩 **R** -
        """
        self._specification_version[_Constants.MANUALLY_SET] = value != None
        self._specification_version = value

    def set_status(self, value=None):
        """
        🟩 **R** -
        """
        self._status[_Constants.MANUALLY_SET] = value != None
        self._status = value

    def set_status_info(self, value=None):
        """
        🟩 **R** -
        """
        self._status_info[_Constants.MANUALLY_SET] = value != None
        self._status_info = value

    def set_system_creation_class_name(self, value=None):
        """
        🟩 **R** -
        """
        self._system_creation_class_name[_Constants.MANUALLY_SET] = value != None
        self._system_creation_class_name = value

    def set_system_name(self, value=None):
        """
        🟩 **R** -
        """
        self._system_name[_Constants.MANUALLY_SET] = value != None
        self._system_name = value

    def set_system_palette_entries(self, value=None):
        """
        🟩 **R** -
        """
        self._system_palette_entries[_Constants.MANUALLY_SET] = value != None
        self._system_palette_entries = value

    def set_GPU_system_processor_mode_current(self, value=None):
        """
        🟩 **R** -
        """
        self._GPU_system_processor_mode_current[_Constants.MANUALLY_SET] = value != None
        self._GPU_system_processor_mode_current = value

    def set_GPU_system_processor_mode_default(self, value=None):
        """
        🟩 **R** -
        """
        self._GPU_system_processor_mode_default[_Constants.MANUALLY_SET] = value != None
        self._GPU_system_processor_mode_default = value

    def set_temperature_core(self, value=None):
        """
        🟩 **R** -
        """
        self._temperature_core[_Constants.MANUALLY_SET] = value != None
        self._temperature_core = value

    def set_temperature_core_limit(self, value=None):
        """
        🟩 **R** -
        """
        self._temperature_core_limit[_Constants.MANUALLY_SET] = value != None
        self._temperature_core_limit = value

    def set_temperature_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._temperature_memory[_Constants.MANUALLY_SET] = value != None
        self._temperature_memory = value

    def set_time_of_last_reset(self, value=None):
        """
        🟩 **R** -
        """
        self._time_of_last_reset[_Constants.MANUALLY_SET] = value != None
        self._time_of_last_reset = value

    def set_utilization_decoder(self, value=None):
        """
        🟩 **R** -
        """
        self._utilization_decoder[_Constants.MANUALLY_SET] = value != None
        self._utilization_decoder = value

    def set_utilization_encoder(self, value=None):
        """
        🟩 **R** -
        """
        self._utilization_encoder[_Constants.MANUALLY_SET] = value != None
        self._utilization_encoder = value

    def set_utilization_gpu(self, value=None):
        """
        🟩 **R** -
        """
        self._utilization_gpu[_Constants.MANUALLY_SET] = value != None
        self._utilization_gpu = value

    def set_utilization_jpeg(self, value=None):
        """
        🟩 **R** -
        """
        self._utilization_jpeg[_Constants.MANUALLY_SET] = value != None
        self._utilization_jpeg = value

    def set_utilization_memory(self, value=None):
        """
        🟩 **R** -
        """
        self._utilization_memory[_Constants.MANUALLY_SET] = value != None
        self._utilization_memory = value

    def set_utilization_optical_flow(self, value=None):
        """
        🟩 **R** -
        """
        self._utilization_optical_flow[_Constants.MANUALLY_SET] = value != None
        self._utilization_optical_flow = value

    def set_uuid(self, value=None):
        """
        🟩 **R** -
        """
        self._uuid[_Constants.MANUALLY_SET] = value != None
        self._uuid = value

    def set_vbios_version(self, value=None):
        """
        🟩 **R** -
        """
        self._vbios_version[_Constants.MANUALLY_SET] = value != None
        self._vbios_version = value

    def set_video_architecture(self, value=None):
        """
        🟩 **R** -
        """
        self._video_architecture[_Constants.MANUALLY_SET] = value != None
        self._video_architecture = value

    def set_video_memory_type(self, value=None):
        """
        🟩 **R** -
        """
        self._video_memory_type[_Constants.MANUALLY_SET] = value != None
        self._video_memory_type = value

    def set_video_mode(self, value=None):
        """
        🟩 **R** -
        """
        self._video_mode[_Constants.MANUALLY_SET] = value != None
        self._video_mode = value

    def set_video_mode_description(self, value=None):
        """
        🟩 **R** -
        """
        self._video_mode_description[_Constants.MANUALLY_SET] = value != None
        self._video_mode_description = value

    def set_video_processor(self, value=None):
        """
        🟩 **R** -
        """
        self._video_processor[_Constants.MANUALLY_SET] = value != None
        self._video_processor = value

    def update_accelerator_capabilities(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._accelerator_capabilities[_Constants.UPDATING] = True
        self.update(data_points=["accelerator_capabilities"], wait_for_completion=wait_for_completion)

    def update_accounting_mode_enabled(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._accounting_mode_enabled[_Constants.UPDATING] = True
        self.update(data_points=["accounting_mode_enabled"], wait_for_completion=wait_for_completion)

    def update_accounting_mode_buffer_size(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._accounting_mode_buffer_size[_Constants.UPDATING] = True
        self.update(data_points=["accounting_mode_buffer_size"], wait_for_completion=wait_for_completion)

    def update_adapter_compatibility(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._adapter_compatibility[_Constants.UPDATING] = True
        self.update(data_points=["adapter_compatibility"], wait_for_completion=wait_for_completion)

    def update_adapter_DAC_type(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._adapter_DAC_type[_Constants.UPDATING] = True
        self.update(data_points=["adapter_DAC_type"], wait_for_completion=wait_for_completion)

    def update_adapter_id(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._adapter_id[_Constants.UPDATING] = True
        self.update(data_points=["adapter_id"], wait_for_completion=wait_for_completion)

    def update_adapter_index(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._adapter_index[_Constants.UPDATING] = True
        self.update(data_points=["adapter_index"], wait_for_completion=wait_for_completion)

    def update_addressing_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._addressing_mode[_Constants.UPDATING] = True
        self.update(data_points=["addressing_mode"], wait_for_completion=wait_for_completion)

    def update_availability(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._availability[_Constants.UPDATING] = True
        self.update(data_points=["availability"], wait_for_completion=wait_for_completion)

    def update_capability_descriptions(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._capability_descriptions[_Constants.UPDATING] = True
        self.update(data_points=["capability_descriptions"], wait_for_completion=wait_for_completion)

    def update_caption(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._caption[_Constants.UPDATING] = True
        self.update(data_points=["caption"], wait_for_completion=wait_for_completion)

    def update_chip_to_chip_interconnect_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._chip_to_chip_interconnect_mode[_Constants.UPDATING] = True
        self.update(data_points=["chip_to_chip_interconnect_mode"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_as_bitmap(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_as_bitmap[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_as_bitmap"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_application_setting(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_application_setting[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_application_setting"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_is_hardware_limited(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_is_hardware_limited[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_is_hardware_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_gpu_idle_limited(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_gpu_idle_limited[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_gpu_idle_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_software_power_limited(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_software_power_limited[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_software_power_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_software_thermal_limited(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_software_thermal_limited[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_software_thermal_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_power_break_slowdown_limited(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_power_break_slowdown_limited[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_power_break_slowdown_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_supported(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_supported[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_supported"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_sync_boost(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_sync_boost[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_sync_boost"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_thermal_limited(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._clock_event_reasons_thermal_limited[_Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_thermal_limited"], wait_for_completion=wait_for_completion)

    def update_color_table_entries(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._color_table_entries[_Constants.UPDATING] = True
        self.update(data_points=["color_table_entries"], wait_for_completion=wait_for_completion)

    def update_compute_cap(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._compute_cap[_Constants.UPDATING] = True
        self.update(data_points=["compute_cap"], wait_for_completion=wait_for_completion)

    def update_compute_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._compute_mode[_Constants.UPDATING] = True
        self.update(data_points=["compute_mode"], wait_for_completion=wait_for_completion)

    def update_config_manager_error_code(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._config_manager_error_code[_Constants.UPDATING] = True
        self.update(data_points=["config_manager_error_code"], wait_for_completion=wait_for_completion)

    def update_config_manager_user_config(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._config_manager_user_config[_Constants.UPDATING] = True
        self.update(data_points=["config_manager_user_config"], wait_for_completion=wait_for_completion)

    def update_core_voltage(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._core_voltage[_Constants.UPDATING] = True
        self.update(data_points=["core_voltage"], wait_for_completion=wait_for_completion)

    def update_core_voltage_range(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._core_voltage_range[_Constants.UPDATING] = True
        self.update(data_points=["core_voltage_range"], wait_for_completion=wait_for_completion)

    def update_creation_class_name(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._creation_class_name[_Constants.UPDATING] = True
        self.update(data_points=["creation_class_name"], wait_for_completion=wait_for_completion)

    def update_current_bits_per_pixel(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_bits_per_pixel[_Constants.UPDATING] = True
        self.update(data_points=["current_bits_per_pixel"], wait_for_completion=wait_for_completion)

    def update_current_horizontal_resolution(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_horizontal_resolution[_Constants.UPDATING] = True
        self.update(data_points=["current_horizontal_resolution"], wait_for_completion=wait_for_completion)

    def update_current_number_of_colors(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_number_of_colors[_Constants.UPDATING] = True
        self.update(data_points=["current_number_of_colors"], wait_for_completion=wait_for_completion)

    def update_current_number_of_columns(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_number_of_columns[_Constants.UPDATING] = True
        self.update(data_points=["current_number_of_columns"], wait_for_completion=wait_for_completion)

    def update_current_number_of_rows(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_number_of_rows[_Constants.UPDATING] = True
        self.update(data_points=["current_number_of_rows"], wait_for_completion=wait_for_completion)

    def update_current_refresh_rate(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_refresh_rate[_Constants.UPDATING] = True
        self.update(data_points=["current_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_current_scan_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_scan_mode[_Constants.UPDATING] = True
        self.update(data_points=["current_scan_mode"], wait_for_completion=wait_for_completion)

    def update_current_vertical_resolution(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._current_vertical_resolution[_Constants.UPDATING] = True
        self.update(data_points=["current_vertical_resolution"], wait_for_completion=wait_for_completion)

    def update_description(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._description[_Constants.UPDATING] = True
        self.update(data_points=["description"], wait_for_completion=wait_for_completion)

    def update_device_id(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._device_id[_Constants.UPDATING] = True
        self.update(data_points=["device_id"], wait_for_completion=wait_for_completion)

    def update_device_specific_pens(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._device_specific_pens[_Constants.UPDATING] = True
        self.update(data_points=["device_specific_pens"], wait_for_completion=wait_for_completion)

    def update_display_active(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._display_active[_Constants.UPDATING] = True
        self.update(data_points=["display_active"], wait_for_completion=wait_for_completion)

    def update_display_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._display_mode[_Constants.UPDATING] = True
        self.update(data_points=["display_mode"], wait_for_completion=wait_for_completion)

    def update_dither_type(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._dither_type[_Constants.UPDATING] = True
        self.update(data_points=["dither_type"], wait_for_completion=wait_for_completion)

    def update_driver_date(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._driver_date[_Constants.UPDATING] = True
        self.update(data_points=["driver_date"], wait_for_completion=wait_for_completion)

    def update_driver_model_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._driver_model_current[_Constants.UPDATING] = True
        self.update(data_points=["driver_model_current"], wait_for_completion=wait_for_completion)

    def update_driver_model_pending(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._driver_model_pending[_Constants.UPDATING] = True
        self.update(data_points=["driver_model_pending"], wait_for_completion=wait_for_completion)

    def update_driver_version(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._driver_version[_Constants.UPDATING] = True
        self.update(data_points=["driver_version"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_cbu(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_cbu[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_primary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_primary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_register_file(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_register_file[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_secondary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_secondary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_shared_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_shared_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_sram(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_sram[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_texture_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_texture_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_total(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_total[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_video_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_all_time_in_video_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_cbu(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_cbu[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_primary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_primary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_register_file(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_register_file[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_secondary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_secondary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_shared_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_shared_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_sram(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_sram[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_texture_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_texture_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_total(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_total[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_video_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_corrected_since_reboot_in_video_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_cbu(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_cbu[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_primary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_primary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_register_file(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_register_file[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_secondary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_secondary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_shared_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_shared_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_sram(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_sram[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_texture_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_texture_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_total(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_total[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_video_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_all_time_in_video_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_cbu(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_cbu[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_register_file(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_register_file[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_sram(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_sram[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_total(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_total[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_video_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_errors_uncorrected_since_reboot_in_video_memory[_Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_mode_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_mode_current[_Constants.UPDATING] = True
        self.update(data_points=["ecc_mode_current"], wait_for_completion=wait_for_completion)

    def update_ecc_mode_pending(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ecc_mode_pending[_Constants.UPDATING] = True
        self.update(data_points=["ecc_mode_pending"], wait_for_completion=wait_for_completion)

    def update_encoder_average_FPS(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._encoder_average_FPS[_Constants.UPDATING] = True
        self.update(data_points=["encoder_average_FPS"], wait_for_completion=wait_for_completion)

    def update_encoder_average_latency(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._encoder_average_latency[_Constants.UPDATING] = True
        self.update(data_points=["encoder_average_latency"], wait_for_completion=wait_for_completion)

    def update_encoder_session_count(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._encoder_session_count[_Constants.UPDATING] = True
        self.update(data_points=["encoder_session_count"], wait_for_completion=wait_for_completion)

    def update_engine_clock_range(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._engine_clock_range[_Constants.UPDATING] = True
        self.update(data_points=["engine_clock_range"], wait_for_completion=wait_for_completion)

    def update_error_cleared(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._error_cleared[_Constants.UPDATING] = True
        self.update(data_points=["error_cleared"], wait_for_completion=wait_for_completion)

    def update_error_description(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._error_description[_Constants.UPDATING] = True
        self.update(data_points=["error_description"], wait_for_completion=wait_for_completion)

    def update_fabric_state(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fabric_state[_Constants.UPDATING] = True
        self.update(data_points=["fabric_state"], wait_for_completion=wait_for_completion)

    def update_fabric_status(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fabric_status[_Constants.UPDATING] = True
        self.update(data_points=["fabric_status"], wait_for_completion=wait_for_completion)

    def update_fan_speed_percentage(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fan_speed_percentage[_Constants.UPDATING] = True
        self.update(data_points=["fan_speed_percentage"], wait_for_completion=wait_for_completion)

    def update_fan_speed_percentage_range(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fan_speed_percentage_range[_Constants.UPDATING] = True
        self.update(data_points=["fan_speed_percentage_range"], wait_for_completion=wait_for_completion)

    def update_fan_speed_RPM(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fan_speed_RPM[_Constants.UPDATING] = True
        self.update(data_points=["fan_speed_RPM"], wait_for_completion=wait_for_completion)

    def update_fan_speed_RPM_range(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fan_speed_RPM_range[_Constants.UPDATING] = True
        self.update(data_points=["fan_speed_RPM_range"], wait_for_completion=wait_for_completion)

    def update_fractional_multi_vGPU(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._fractional_multi_vGPU[_Constants.UPDATING] = True
        self.update(data_points=["fractional_multi_vGPU"], wait_for_completion=wait_for_completion)

    def update_frequency_application_default_shader_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_application_default_shader_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_application_default_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_default_memory_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_application_default_memory_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_application_default_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_memory_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_application_memory_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_application_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_shader_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_application_shader_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_application_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_memory_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_maximum_memory_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_shader_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_maximum_shader_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_streaming_multiprocessor_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_maximum_streaming_multiprocessor_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_memory_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_memory_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_shader_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_shader_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_streaming_multiprocessor_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_streaming_multiprocessor_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_video_clock(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._frequency_video_clock[_Constants.UPDATING] = True
        self.update(data_points=["frequency_video_clock"], wait_for_completion=wait_for_completion)

    def update_heterogenous_multi_vGPU(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._heterogenous_multi_vGPU[_Constants.UPDATING] = True
        self.update(data_points=["heterogenous_multi_vGPU"], wait_for_completion=wait_for_completion)

    def update_heterogenous_time_slice_profile(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._heterogenous_time_slice_profile[_Constants.UPDATING] = True
        self.update(data_points=["heterogenous_time_slice_profile"], wait_for_completion=wait_for_completion)

    def update_heterogenous_time_slice_sizes(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._heterogenous_time_slice_sizes[_Constants.UPDATING] = True
        self.update(data_points=["heterogenous_time_slice_sizes"], wait_for_completion=wait_for_completion)

    def update_ICM_indent(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ICM_indent[_Constants.UPDATING] = True
        self.update(data_points=["ICM_indent"], wait_for_completion=wait_for_completion)

    def update_ICM_method(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._ICM_method[_Constants.UPDATING] = True
        self.update(data_points=["ICM_method"], wait_for_completion=wait_for_completion)

    def update_inf_filename(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._inf_filename[_Constants.UPDATING] = True
        self.update(data_points=["inf_filename"], wait_for_completion=wait_for_completion)

    def update_inf_section(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._inf_section[_Constants.UPDATING] = True
        self.update(data_points=["inf_section"], wait_for_completion=wait_for_completion)

    def update_info_ROM_ecc(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._info_ROM_ecc[_Constants.UPDATING] = True
        self.update(data_points=["info_ROM_ecc"], wait_for_completion=wait_for_completion)

    def update_info_ROM_oem(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._info_ROM_oem[_Constants.UPDATING] = True
        self.update(data_points=["info_ROM_oem"], wait_for_completion=wait_for_completion)

    def update_info_ROM_power(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._info_ROM_power[_Constants.UPDATING] = True
        self.update(data_points=["info_ROM_power"], wait_for_completion=wait_for_completion)

    def update_info_ROM_version(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._info_ROM_version[_Constants.UPDATING] = True
        self.update(data_points=["info_ROM_version"], wait_for_completion=wait_for_completion)

    def update_install_date(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._install_date[_Constants.UPDATING] = True
        self.update(data_points=["install_date"], wait_for_completion=wait_for_completion)

    def update_installed_display_drivers(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._installed_display_drivers[_Constants.UPDATING] = True
        self.update(data_points=["installed_display_drivers"], wait_for_completion=wait_for_completion)

    def update_last_error_code(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._last_error_code[_Constants.UPDATING] = True
        self.update(data_points=["last_error_code"], wait_for_completion=wait_for_completion)

    def update_max_memory_supported(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._max_memory_supported[_Constants.UPDATING] = True
        self.update(data_points=["max_memory_supported"], wait_for_completion=wait_for_completion)

    def update_max_number_controlled(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._max_number_controlled[_Constants.UPDATING] = True
        self.update(data_points=["max_number_controlled"], wait_for_completion=wait_for_completion)

    def update_max_refresh_rate(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._max_refresh_rate[_Constants.UPDATING] = True
        self.update(data_points=["max_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_memory_clock_range(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._memory_clock_range[_Constants.UPDATING] = True
        self.update(data_points=["memory_clock_range"], wait_for_completion=wait_for_completion)

    def update_memory_free(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._memory_free[_Constants.UPDATING] = True
        self.update(data_points=["memory_free"], wait_for_completion=wait_for_completion)

    def update_memory_reserved(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._memory_reserved[_Constants.UPDATING] = True
        self.update(data_points=["memory_reserved"], wait_for_completion=wait_for_completion)

    def update_memory_total(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._memory_total[_Constants.UPDATING] = True
        self.update(data_points=["memory_total"], wait_for_completion=wait_for_completion)

    def update_memory_used(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._memory_used[_Constants.UPDATING] = True
        self.update(data_points=["memory_used"], wait_for_completion=wait_for_completion)

    def update_min_refresh_rate(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._min_refresh_rate[_Constants.UPDATING] = True
        self.update(data_points=["min_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_monochrome(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._monochrome[_Constants.UPDATING] = True
        self.update(data_points=["monochrome"], wait_for_completion=wait_for_completion)

    def update_multi_instance_GPU_mode_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._multi_instance_GPU_mode_current[_Constants.UPDATING] = True
        self.update(data_points=["multi_instance_GPU_mode_current"], wait_for_completion=wait_for_completion)

    def update_multi_instance_GPU_mode_pending(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._multi_instance_GPU_mode_pending[_Constants.UPDATING] = True
        self.update(data_points=["multi_instance_GPU_mode_pending"], wait_for_completion=wait_for_completion)

    def update_name(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._name[_Constants.UPDATING] = True
        self.update(data_points=["name"], wait_for_completion=wait_for_completion)

    def update_number_of_color_planes(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._number_of_color_planes[_Constants.UPDATING] = True
        self.update(data_points=["number_of_color_planes"], wait_for_completion=wait_for_completion)

    def update_number_of_video_pages(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._number_of_video_pages[_Constants.UPDATING] = True
        self.update(data_points=["number_of_video_pages"], wait_for_completion=wait_for_completion)

    def update_operating_mode_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._operating_mode_current[_Constants.UPDATING] = True
        self.update(data_points=["operating_mode_current"], wait_for_completion=wait_for_completion)

    def update_operating_mode_pending(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._operating_mode_pending[_Constants.UPDATING] = True
        self.update(data_points=["operating_mode_pending"], wait_for_completion=wait_for_completion)

    def update_pci_bus(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_bus[_Constants.UPDATING] = True
        self.update(data_points=["pci_bus"], wait_for_completion=wait_for_completion)

    def update_pci_bus_id(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_bus_id[_Constants.UPDATING] = True
        self.update(data_points=["pci_bus_id"], wait_for_completion=wait_for_completion)

    def update_pci_device(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_device[_Constants.UPDATING] = True
        self.update(data_points=["pci_device"], wait_for_completion=wait_for_completion)

    def update_pci_device_id(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_device_id[_Constants.UPDATING] = True
        self.update(data_points=["pci_device_id"], wait_for_completion=wait_for_completion)

    def update_pci_domain(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_domain[_Constants.UPDATING] = True
        self.update(data_points=["pci_domain"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_link_generation_current[_Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_current"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_device_host_maximum(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_link_generation_device_host_maximum[_Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_device_host_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_gpu_maximum(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_link_generation_gpu_maximum[_Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_gpu_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_maximum(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_link_generation_maximum[_Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_width_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_link_width_current[_Constants.UPDATING] = True
        self.update(data_points=["pci_link_width_current"], wait_for_completion=wait_for_completion)

    def update_pci_link_width_maximum(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_link_width_maximum[_Constants.UPDATING] = True
        self.update(data_points=["pci_link_width_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_sub_device_id(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._pci_sub_device_id[_Constants.UPDATING] = True
        self.update(data_points=["pci_sub_device_id"], wait_for_completion=wait_for_completion)

    def update_persistence_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._persistence_mode[_Constants.UPDATING] = True
        self.update(data_points=["persistence_mode"], wait_for_completion=wait_for_completion)

    def update_PNP_device_id(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._PNP_device_id[_Constants.UPDATING] = True
        self.update(data_points=["PNP_device_id"], wait_for_completion=wait_for_completion)

    def update_power_draw(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw[_Constants.UPDATING] = True
        self.update(data_points=["power_draw"], wait_for_completion=wait_for_completion)

    def update_power_draw_average(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_average[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_average"], wait_for_completion=wait_for_completion)

    def update_power_draw_default_limit(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_default_limit[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_default_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_enforced_limit(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_enforced_limit[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_enforced_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_instant(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_instant[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_instant"], wait_for_completion=wait_for_completion)

    def update_power_draw_limit(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_limit[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_maximum(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_maximum[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_maximum"], wait_for_completion=wait_for_completion)

    def update_power_draw_minimum(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_draw_minimum[_Constants.UPDATING] = True
        self.update(data_points=["power_draw_minimum"], wait_for_completion=wait_for_completion)

    def update_power_management_capabilities(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_management_capabilities[_Constants.UPDATING] = True
        self.update(data_points=["power_management_capabilities"], wait_for_completion=wait_for_completion)

    def update_power_management_supported(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._power_management_supported[_Constants.UPDATING] = True
        self.update(data_points=["power_management_supported"], wait_for_completion=wait_for_completion)

    def update_protected_memory_free(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._protected_memory_free[_Constants.UPDATING] = True
        self.update(data_points=["protected_memory_free"], wait_for_completion=wait_for_completion)

    def update_protected_memory_total(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._protected_memory_total[_Constants.UPDATING] = True
        self.update(data_points=["protected_memory_total"], wait_for_completion=wait_for_completion)

    def update_protected_memory_used(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._protected_memory_used[_Constants.UPDATING] = True
        self.update(data_points=["protected_memory_used"], wait_for_completion=wait_for_completion)

    def update_protocol_supported(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._protocol_supported[_Constants.UPDATING] = True
        self.update(data_points=["protocol_supported"], wait_for_completion=wait_for_completion)

    def update_performance_state(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._performance_state[_Constants.UPDATING] = True
        self.update(data_points=["performance_state"], wait_for_completion=wait_for_completion)

    def update_retired_pages_double_bit_ecc_errors_count(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._retired_pages_double_bit_ecc_errors_count[_Constants.UPDATING] = True
        self.update(data_points=["retired_pages_double_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)

    def update_retired_pages_single_bit_ecc_errors_count(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._retired_pages_single_bit_ecc_errors_count[_Constants.UPDATING] = True
        self.update(data_points=["retired_pages_single_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)

    def update_retired_pages_pending(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._retired_pages_pending[_Constants.UPDATING] = True
        self.update(data_points=["retired_pages_pending"], wait_for_completion=wait_for_completion)

    def update_reserved_system_palette_entries(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._reserved_system_palette_entries[_Constants.UPDATING] = True
        self.update(data_points=["reserved_system_palette_entries"], wait_for_completion=wait_for_completion)

    def update_reset_required(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._reset_required[_Constants.UPDATING] = True
        self.update(data_points=["reset_required"], wait_for_completion=wait_for_completion)

    def update_reset_and_drain_recommended(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._reset_and_drain_recommended[_Constants.UPDATING] = True
        self.update(data_points=["reset_and_drain_recommended"], wait_for_completion=wait_for_completion)

    def update_serial(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._serial[_Constants.UPDATING] = True
        self.update(data_points=["serial"], wait_for_completion=wait_for_completion)

    def update_specification_version(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._specification_version[_Constants.UPDATING] = True
        self.update(data_points=["specification_version"], wait_for_completion=wait_for_completion)

    def update_status(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._status[_Constants.UPDATING] = True
        self.update(data_points=["status"], wait_for_completion=wait_for_completion)

    def update_status_info(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._status_info[_Constants.UPDATING] = True
        self.update(data_points=["status_info"], wait_for_completion=wait_for_completion)

    def update_system_creation_class_name(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._system_creation_class_name[_Constants.UPDATING] = True
        self.update(data_points=["system_creation_class_name"], wait_for_completion=wait_for_completion)

    def update_system_name(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._system_name[_Constants.UPDATING] = True
        self.update(data_points=["system_name"], wait_for_completion=wait_for_completion)

    def update_system_palette_entries(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._system_palette_entries[_Constants.UPDATING] = True
        self.update(data_points=["system_palette_entries"], wait_for_completion=wait_for_completion)

    def update_GPU_system_processor_mode_current(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._GPU_system_processor_mode_current[_Constants.UPDATING] = True
        self.update(data_points=["GPU_system_processor_mode_current"], wait_for_completion=wait_for_completion)

    def update_GPU_system_processor_mode_default(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._GPU_system_processor_mode_default[_Constants.UPDATING] = True
        self.update(data_points=["GPU_system_processor_mode_default"], wait_for_completion=wait_for_completion)

    def update_temperature_core(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._temperature_core[_Constants.UPDATING] = True
        self.update(data_points=["temperature_core"], wait_for_completion=wait_for_completion)

    def update_temperature_core_limit(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._temperature_core_limit[_Constants.UPDATING] = True
        self.update(data_points=["temperature_core_limit"], wait_for_completion=wait_for_completion)

    def update_temperature_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._temperature_memory[_Constants.UPDATING] = True
        self.update(data_points=["temperature_memory"], wait_for_completion=wait_for_completion)

    def update_time_of_last_reset(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._time_of_last_reset[_Constants.UPDATING] = True
        self.update(data_points=["time_of_last_reset"], wait_for_completion=wait_for_completion)

    def update_utilization_decoder(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._utilization_decoder[_Constants.UPDATING] = True
        self.update(data_points=["utilization_decoder"], wait_for_completion=wait_for_completion)

    def update_utilization_encoder(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._utilization_encoder[_Constants.UPDATING] = True
        self.update(data_points=["utilization_encoder"], wait_for_completion=wait_for_completion)

    def update_utilization_gpu(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._utilization_gpu[_Constants.UPDATING] = True
        self.update(data_points=["utilization_gpu"], wait_for_completion=wait_for_completion)

    def update_utilization_jpeg(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._utilization_jpeg[_Constants.UPDATING] = True
        self.update(data_points=["utilization_jpeg"], wait_for_completion=wait_for_completion)

    def update_utilization_memory(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._utilization_memory[_Constants.UPDATING] = True
        self.update(data_points=["utilization_memory"], wait_for_completion=wait_for_completion)

    def update_utilization_optical_flow(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._utilization_optical_flow[_Constants.UPDATING] = True
        self.update(data_points=["utilization_optical_flow"], wait_for_completion=wait_for_completion)

    def update_uuid(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._uuid[_Constants.UPDATING] = True
        self.update(data_points=["uuid"], wait_for_completion=wait_for_completion)

    def update_vbios_version(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._vbios_version[_Constants.UPDATING] = True
        self.update(data_points=["vbios_version"], wait_for_completion=wait_for_completion)

    def update_video_architecture(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._video_architecture[_Constants.UPDATING] = True
        self.update(data_points=["video_architecture"], wait_for_completion=wait_for_completion)

    def update_video_memory_type(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._video_memory_type[_Constants.UPDATING] = True
        self.update(data_points=["video_memory_type"], wait_for_completion=wait_for_completion)

    def update_video_mode(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._video_mode[_Constants.UPDATING] = True
        self.update(data_points=["video_mode"], wait_for_completion=wait_for_completion)

    def update_video_mode_description(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._video_mode_description[_Constants.UPDATING] = True
        self.update(data_points=["video_mode_description"], wait_for_completion=wait_for_completion)

    def update_video_processor(self, wait_for_completion=True):
        """
        🟩 **R** -
        """
        self._video_processor[_Constants.UPDATING] = True
        self.update(data_points=["video_processor"], wait_for_completion=wait_for_completion)