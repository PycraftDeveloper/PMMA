try:
    import pyadl
    pyadl_available = True
except Exception as error:
    if type(error) != ModuleNotFoundError:
        pyadl_available = False
    else:
        raise error

import threading
import json

from pmma.core.py_src.Executor import Executor
from pmma.core.py_src.Constants import Constants, InternalConstants
from pmma.core.py_src.General import General

if General.get_operating_system() == Constants.WINDOWS:
    import wmi
    from pythoncom import CoInitialize

def uuid_cleaner(uuid):
    uuid = uuid.strip()
    uuid = uuid.replace("\\", "_")
    return uuid[:66]

class GPUsInternal:
    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            raise RuntimeError("GPUsInternal can only be instantiated once.")
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._unique_gpus = {} # {"bus": n, "uuid": n}: {SMI: n, ADL: n, WMI, n}

        if pyadl_available:
            raw_GPUs = pyadl.ADLManager().getInstance().getDevices()
            adl_index = 0
            for raw_gpu in raw_GPUs:
                adl_bus = raw_gpu.__dict__["busNumber"]
                adl_uuid: bytes = raw_gpu.__dict__["uuid"]
                adl_uuid = adl_uuid.decode("utf-8")
                adl_uuid = uuid_cleaner(adl_uuid)
                json_identifier = json.dumps({"bus": adl_bus, "uuid": adl_uuid})
                self._unique_gpus[json_identifier] = {InternalConstants.SMI: None, InternalConstants.WMI: None, InternalConstants.PYADL: adl_index}
                adl_index += 1

        nvidia_smi = General.find_executable_nvidia_smi()
        if nvidia_smi is not None:
            self._executor = Executor()
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
                        unloaded_key = json.loads(key)
                        if unloaded_key["bus"] == smi_bus:
                            self._unique_gpus[key][InternalConstants.SMI] = smi_index

        if General.get_operating_system() == Constants.WINDOWS:
            computer = wmi.WMI()
            wmi_index = 0
            for gpu in computer.Win32_VideoController():
                wmi_uuid = getattr(gpu, "PNPDeviceID")
                wmi_uuid = uuid_cleaner(wmi_uuid)
                for key in self._unique_gpus:
                    unloaded_key = json.loads(key)
                    if unloaded_key["uuid"] == wmi_uuid:
                        self._unique_gpus[key][InternalConstants.WMI] = wmi_index

                wmi_index += 1

        gpu_instances = []
        self._gpu_instances = []
        for key in self._unique_gpus:
            gpu_instances.append(GPU(self._unique_gpus[key]))

        threads = []
        for gpu in gpu_instances:
            thread = threading.Thread(target=gpu.update, kwargs={"everything": True, "wait_for_completion": True})
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
            print("No GPU devices were detected.")
            print("PMMA was unable to detect any GPU devices. \
Whilst this doesn't mean that PMMA wont run, it does mean that some \
mechanics may run slower than expected.")

    @classmethod
    def identify_gpus(cls):
        for i in range(len(cls._instance._gpu_instances)):
            print(f"GPU: {i}, has name: {cls._instance._gpu_instances[i].get_name()}")

    @classmethod
    def get_gpu(cls, gpu_index):
        return cls._instance._gpu_instances[gpu_index]

    @classmethod
    def all_gpus_are_unique(cls):
        return cls._instance._all_gpus_are_unique

    @classmethod
    def get_gpu_count(cls):
        return len(cls._instance._gpu_instances)

    @classmethod
    def get_all_gpus(cls):
        return cls._instance._gpu_instances

    @classmethod
    def is_instantiated(cls):
        return cls._instance is not None

class GPUs:
    def __init__(self):
        if not GPUsInternal.is_instantiated():
            GPUsInternal()

    def identify_gpus(self):
        GPUsInternal.identify_gpus()

    def get_gpu(self, gpu_index):
        return GPUsInternal.get_gpu(gpu_index)

    def all_gpus_are_unique(self):
        return GPUsInternal.all_gpus_are_unique()

class GPU:
    def __init__(self, module_identification_indices):
        self._module_identification_indices = module_identification_indices
        self._executor = Executor()

        self._accelerator_capabilities = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['AcceleratorCapabilities'], InternalConstants.PYADL: []}}
        self._accounting_mode_enabled = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['accounting.mode'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._accounting_mode_buffer_size = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['accounting.buffer_size'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._adapter_compatibility = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['AdapterCompatibility'], InternalConstants.PYADL: []}}
        self._adapter_DAC_type = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['AdapterDACType'], InternalConstants.PYADL: []}}
        self._adapter_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['adapterID']}}
        self._adapter_index = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['adapterIndex']}}
        self._addressing_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['addressing_mode'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._availability = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['Availability'], InternalConstants.PYADL: []}}
        self._capability_descriptions = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CapabilityDescriptions'], InternalConstants.PYADL: []}}
        self._caption = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['Caption'], InternalConstants.PYADL: []}}
        self._chip_to_chip_interconnect_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['c2c.mode'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_as_bitmap = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.active', 'clocks_throttle_reasons.active'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_application_setting = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.applications_clocks_setting', 'clocks_throttle_reasons.applications_clocks_setting'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_is_hardware_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.hw_slowdown', 'clocks_throttle_reasons.hw_slowdown'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_gpu_idle_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.gpu_idle', 'clocks_throttle_reasons.gpu_idle'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_software_power_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.sw_power_cap', 'clocks_throttle_reasons.sw_power_cap'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_software_thermal_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.sw_thermal_slowdown', 'clocks_throttle_reasons.sw_thermal_slowdown'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_power_break_slowdown_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.hw_power_brake_slowdown', 'clocks_throttle_reasons.hw_power_brake_slowdown'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.supported', 'clocks_throttle_reasons.supported'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_sync_boost = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.sync_boost', 'clocks_throttle_reasons.sync_boost'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._clock_event_reasons_thermal_limited = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks_event_reasons.hw_thermal_slowdown', 'clocks_throttle_reasons.hw_thermal_slowdown'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._color_table_entries = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ColorTableEntries'], InternalConstants.PYADL: []}}
        self._compute_cap = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['compute_cap'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._compute_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['compute_mode'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._config_manager_error_code = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ConfigManagerErrorCode'], InternalConstants.PYADL: []}}
        self._config_manager_user_config = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ConfigManagerUserConfig'], InternalConstants.PYADL: []}}
        self._core_voltage = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentCoreVoltage']}}
        self._core_voltage_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['coreVoltageRange']}}
        self._creation_class_name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CreationClassName'], InternalConstants.PYADL: []}}
        self._current_bits_per_pixel = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentBitsPerPixel'], InternalConstants.PYADL: []}}
        self._current_horizontal_resolution = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentHorizontalResolution'], InternalConstants.PYADL: []}}
        self._current_number_of_colors = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentNumberOfColors'], InternalConstants.PYADL: []}}
        self._current_number_of_columns = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentNumberOfColumns'], InternalConstants.PYADL: []}}
        self._current_number_of_rows = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentNumberOfRows'], InternalConstants.PYADL: []}}
        self._current_refresh_rate = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentRefreshRate'], InternalConstants.PYADL: []}}
        self._current_scan_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentScanMode'], InternalConstants.PYADL: []}}
        self._current_vertical_resolution = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['CurrentVerticalResolution'], InternalConstants.PYADL: []}}
        self._description = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['Description'], InternalConstants.PYADL: []}}
        self._device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['DeviceID'], InternalConstants.PYADL: []}}
        self._device_specific_pens = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['DeviceSpecificPens'], InternalConstants.PYADL: []}}
        self._display_active = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['display_active'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._display_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['display_mode'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._dither_type = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['DitherType'], InternalConstants.PYADL: []}}
        self._driver_date = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['DriverDate'], InternalConstants.PYADL: []}}
        self._driver_model_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['driver_model.current'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._driver_model_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['driver_model.pending'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._driver_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['driver_version'], InternalConstants.WMI: ['DriverVersion'], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.cbu'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.l1_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.register_file'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.l2_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.dram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.sram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.texture_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.total'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_all_time_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.aggregate.device_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.cbu'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.l1_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.register_file'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.l2_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.dram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.sram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.texture_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.total'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_corrected_since_reboot_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.corrected.volatile.device_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.cbu'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.l1_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.register_file'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.l2_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.dram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.sram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.texture_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.total'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_all_time_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.aggregate.device_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_cbu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.cbu'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.l1_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_register_file = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.register_file'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.l2_cache'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.dram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_sram = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.sram'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.texture_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.total'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_errors_uncorrected_since_reboot_in_video_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.errors.uncorrected.volatile.device_memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.mode.current'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ecc_mode_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['ecc.mode.pending'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._encoder_average_FPS = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['encoder.stats.averageFps'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._encoder_average_latency = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['encoder.stats.averageLatency'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._encoder_session_count = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['encoder.stats.sessionCount'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._engine_clock_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['engineClockRange']}}
        self._error_cleared = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ErrorCleared'], InternalConstants.PYADL: []}}
        self._error_description = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ErrorDescription'], InternalConstants.PYADL: []}}
        self._fabric_state = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['fabric.state'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._fabric_status = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['fabric.status'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._fan_speed_percentage = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['fan.speed'], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self._fan_speed_percentage_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE']}}
        self._fan_speed_RPM = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentFanSpeed:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self._fan_speed_RPM_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['getFanSpeedRange:ADL_DEVICE_FAN_SPEED_TYPE_RPM']}}
        self._fractional_multi_vGPU = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['vgpu_device_capability.fractional_multiVgpu'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_application_default_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.default_applications.graphics', 'clocks.default_applications.gr'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_application_default_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.default_applications.memory', 'clocks.default_applications.mem'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_application_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.applications.memory', 'clocks.applications.mem'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_application_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.applications.graphics', 'clocks.applications.gr'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_maximum_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.max.memory', 'clocks.max.mem'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_maximum_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.max.graphics', 'clocks.max.gr'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_maximum_streaming_multiprocessor_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.max.sm', 'clocks.max.sm'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_memory_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.current.memory', 'clocks.mem'], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentMemoryClock']}}
        self._frequency_shader_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.current.graphics', 'clocks.gr'], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentEngineClock']}}
        self._frequency_streaming_multiprocessor_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.current.sm', 'clocks.sm'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._frequency_video_clock = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['clocks.current.video', 'clocks.video'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._heterogenous_multi_vGPU = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['vgpu_driver_capability.heterogenous_multivGPU'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._heterogenous_time_slice_profile = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_profile'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._heterogenous_time_slice_sizes = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['vgpu_device_capability.heterogeneous_timeSlice_sizes'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._ICM_indent = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ICMIntent'], InternalConstants.PYADL: []}}
        self._ICM_method = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ICMMethod'], InternalConstants.PYADL: []}}
        self._inf_filename = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['InfFilename'], InternalConstants.PYADL: []}}
        self._inf_section = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['InfSection'], InternalConstants.PYADL: []}}
        self._info_ROM_ecc = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['inforom.ecc'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._info_ROM_oem = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['inforom.oem'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._info_ROM_power = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['inforom.pwr', 'inforom.power'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._info_ROM_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['inforom.img', 'inforom.image'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._install_date = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['InstallDate'], InternalConstants.PYADL: []}}
        self._installed_display_drivers = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['InstalledDisplayDrivers'], InternalConstants.PYADL: []}}
        self._last_error_code = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['LastErrorCode'], InternalConstants.PYADL: []}}
        self._max_memory_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['MaxMemorySupported'], InternalConstants.PYADL: []}}
        self._max_number_controlled = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['MaxNumberControlled'], InternalConstants.PYADL: []}}
        self._max_refresh_rate = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['MaxRefreshRate'], InternalConstants.PYADL: []}}
        self._memory_clock_range = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: [], InternalConstants.PYADL: ['getMemoryClockRange']}}
        self._memory_free = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['memory.free'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._memory_reserved = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['memory.reserved'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._memory_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['memory.total'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._memory_used = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['memory.used'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._min_refresh_rate = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['MinRefreshRate'], InternalConstants.PYADL: []}}
        self._monochrome = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['Monochrome'], InternalConstants.PYADL: []}}
        self._multi_instance_GPU_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['mig.mode.current'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._multi_instance_GPU_mode_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['mig.mode.pending'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['name', 'gpu_name'], InternalConstants.WMI: ['Name'], InternalConstants.PYADL: ['adapterName']}}
        self._number_of_color_planes = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['NumberOfColorPlanes'], InternalConstants.PYADL: []}}
        self._number_of_video_pages = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['NumberOfVideoPages'], InternalConstants.PYADL: []}}
        self._operating_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['gom.current', 'gpu_operation_mode.current'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._operating_mode_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['gom.pending', 'gpu_operation_mode.pending'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_bus = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pci.bus'], InternalConstants.WMI: [], InternalConstants.PYADL: ['busNumber']}}
        self._pci_bus_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pci.bus_id', 'gpu_bus_id'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_device = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pci.device'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pci.device_id'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_domain = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pci.domain'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_link_generation_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pcie.link.gen.gpucurrent'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_link_generation_device_host_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pcie.link.gen.max'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_link_generation_gpu_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pcie.link.gen.gpumax'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_link_generation_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pcie.link.gen.hostmax'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_link_width_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pcie.link.width.current'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_link_width_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pcie.link.width.max'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._pci_sub_device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pci.sub_device_id'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._persistence_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['persistence_mode'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._PNP_device_id = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['PNPDeviceID'], InternalConstants.PYADL: []}}
        self._power_draw = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.draw'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_average = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.draw.average'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_default_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.default_limit'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_enforced_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['enforced.power.limit'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_instant = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.draw.instant'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.limit'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_maximum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.max_limit'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_draw_minimum = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.min_limit'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._power_management_capabilities = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['PowerManagementCapabilities'], InternalConstants.PYADL: []}}
        self._power_management_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['power.management'], InternalConstants.WMI: ['PowerManagementSupported'], InternalConstants.PYADL: []}}
        self._protected_memory_free = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['protected_memory.free'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._protected_memory_total = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['protected_memory.total'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._protected_memory_used = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['protected_memory.used'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._protocol_supported = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ProtocolSupported'], InternalConstants.PYADL: []}}
        self._performance_state = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['pstate'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._retired_pages_double_bit_ecc_errors_count = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['retired_pages.double_bit.count', 'retired_pages.dbe'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._retired_pages_single_bit_ecc_errors_count = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['retired_pages.single_bit_ecc.count', 'retired_pages.sbe'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._retired_pages_pending = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['retired_pages.pending'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._reserved_system_palette_entries = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['ReservedSystemPaletteEntries'], InternalConstants.PYADL: []}}
        self._reset_required = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['reset_status.reset_required'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._reset_and_drain_recommended = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['reset_status.drain_and_reset_recommended'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._serial = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['serial', 'gpu_serial'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._specification_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['SpecificationVersion'], InternalConstants.PYADL: []}}
        self._status = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['Status'], InternalConstants.PYADL: []}}
        self._status_info = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['StatusInfo'], InternalConstants.PYADL: []}}
        self._system_creation_class_name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['SystemCreationClassName'], InternalConstants.PYADL: []}}
        self._system_name = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['SystemName'], InternalConstants.PYADL: []}}
        self._system_palette_entries = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['SystemPaletteEntries'], InternalConstants.PYADL: []}}
        self._GPU_system_processor_mode_current = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['gsp.mode.current'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._GPU_system_processor_mode_default = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['gsp.mode.default'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._temperature_core = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['temperature.gpu'], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentTemperature']}}
        self._temperature_core_limit = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['temperature.gpu.tlimit'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._temperature_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['temperature.memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._time_of_last_reset = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['TimeOfLastReset'], InternalConstants.PYADL: []}}
        self._utilization_decoder = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['utilization.decoder'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._utilization_encoder = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['utilization.encoder'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._utilization_gpu = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['utilization.gpu'], InternalConstants.WMI: [], InternalConstants.PYADL: ['getCurrentUsage']}}
        self._utilization_jpeg = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['utilization.jpeg'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._utilization_memory = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['utilization.memory'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._utilization_optical_flow = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['utilization.ofa'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._uuid = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['uuid', 'gpu_uuid'], InternalConstants.WMI: [], InternalConstants.PYADL: ['uuid']}}
        self._vbios_version = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: ['vbios_version'], InternalConstants.WMI: [], InternalConstants.PYADL: []}}
        self._video_architecture = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['VideoArchitecture'], InternalConstants.PYADL: []}}
        self._video_memory_type = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['VideoMemoryType'], InternalConstants.PYADL: []}}
        self._video_mode = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['VideoMode'], InternalConstants.PYADL: []}}
        self._video_mode_description = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['VideoModeDescription'], InternalConstants.PYADL: []}}
        self._video_processor = {Constants.VALUE: None, Constants.UPDATING: True, Constants.MANUALLY_SET: False, InternalConstants.DATA_COLLECTION_METHODS: {InternalConstants.SMI: [], InternalConstants.WMI: ['VideoProcessor'], InternalConstants.PYADL: []}}

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

        self._priorities = [InternalConstants.SMI, InternalConstants.PYADL, InternalConstants.WMI]

        if pyadl_available is False:
            print("PMMA is unable to interface with AMD/ATI GPUs. \
This is most likely because no AMD/API GPUs where found on your system, \
although this can also imply that there are driver issues somewhere. If this is unexpected \
- which is to say; you have an AMD/ATI GPU - double check your driver install \
and that other software is able to interact with the GPU. On any virtual machines \
make sure that you are able to pass through the GPU device.")

    def update(self, everything=False, data_points=None, wait_for_completion=False):
        if General.get_operating_system() == Constants.WINDOWS:
            CoInitialize()
        if wait_for_completion:
            self._update(everything=everything, data_points=data_points)
        else:
            thread = threading.Thread(target=self._update, args=(everything, data_points))
            thread.daemon = True
            thread.name = "GPU:Update_Data_Thread"
            thread.start()

    def _update(self, everything, data_points):
        if data_points is None:
            data_points = self._gpu_data_points
        smi_data = ""
        smi_data_points = []
        adl_data = []
        adl_data_points = []
        wmi_data = []
        wmi_data_points = []
        for data_point in data_points:
            if self.__dict__[data_point][Constants.MANUALLY_SET] is False or everything:
                data_collection_strategies = self.__dict__[data_point][InternalConstants.DATA_COLLECTION_METHODS] # keys changed
                for query_command in data_collection_strategies[InternalConstants.SMI]:
                    if self._module_identification_indices[InternalConstants.SMI] is not None:
                        smi_data += f"{query_command},"
                        smi_data_points.append(data_point)
                for query_command in data_collection_strategies[InternalConstants.PYADL]:
                    if self._module_identification_indices[InternalConstants.PYADL] is not None:
                        adl_data.append(query_command)
                        adl_data_points.append(data_point)
                for query_command in data_collection_strategies[InternalConstants.WMI]:
                    if self._module_identification_indices[InternalConstants.WMI] is not None:
                        wmi_data.append(query_command)
                        wmi_data_points.append(data_point)

        smi_data = smi_data[:-1]

        set_attributes = []

        for priority in self._priorities:
            if priority == InternalConstants.SMI and smi_data != "":
                self._executor.run([
                    General.find_executable_nvidia_smi(),
                    f"--query-gpu={smi_data}",
                    "--format=csv,noheader,nounits",
                    f"-i={self._module_identification_indices[InternalConstants.SMI]}"])

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
                        self.__dict__[data_point][Constants.VALUE] = data
                        if data is not None:
                            set_attributes.append(data_point)

            elif priority == InternalConstants.PYADL and adl_data != [] and pyadl_available:
                gpu_data = pyadl.ADLManager.getInstance().getDevices()[self._module_identification_indices[InternalConstants.PYADL]]
                result = []
                for data_point in adl_data:
                    if ":" in data_point:
                        split_data_point = data_point.split(":")
                        name = split_data_point[0]
                        args = getattr(pyadl, split_data_point[1])
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

            elif priority == InternalConstants.WMI and wmi_data != [] and General.get_operating_system() == Constants.WINDOWS:
                computer = wmi.WMI()
                gpu_data = computer.Win32_VideoController()[self._module_identification_indices[InternalConstants.WMI]]
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

    def get_accelerator_capabilities(self, update=False, wait_for_completion=False):
        value = self._accelerator_capabilities[Constants.VALUE]
        if update and self._accelerator_capabilities[Constants.UPDATING] is False:
            self.update(data_points=["accelerator_capabilities"], wait_for_completion=wait_for_completion)
        return value

    def get_accounting_mode_enabled(self, update=False, wait_for_completion=False):
        value = self._accounting_mode_enabled[Constants.VALUE]
        if update and self._accounting_mode_enabled[Constants.UPDATING] is False:
            self.update(data_points=["accounting_mode_enabled"], wait_for_completion=wait_for_completion)
        return value

    def get_accounting_mode_buffer_size(self, update=False, wait_for_completion=False):
        value = self._accounting_mode_buffer_size[Constants.VALUE]
        if update and self._accounting_mode_buffer_size[Constants.UPDATING] is False:
            self.update(data_points=["accounting_mode_buffer_size"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_compatibility(self, update=False, wait_for_completion=False):
        value = self._adapter_compatibility[Constants.VALUE]
        if update and self._adapter_compatibility[Constants.UPDATING] is False:
            self.update(data_points=["adapter_compatibility"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_DAC_type(self, update=False, wait_for_completion=False):
        value = self._adapter_DAC_type[Constants.VALUE]
        if update and self._adapter_DAC_type[Constants.UPDATING] is False:
            self.update(data_points=["adapter_DAC_type"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_id(self, update=False, wait_for_completion=False):
        value = self._adapter_id[Constants.VALUE]
        if update and self._adapter_id[Constants.UPDATING] is False:
            self.update(data_points=["adapter_id"], wait_for_completion=wait_for_completion)
        return value

    def get_adapter_index(self, update=False, wait_for_completion=False):
        value = self._adapter_index[Constants.VALUE]
        if update and self._adapter_index[Constants.UPDATING] is False:
            self.update(data_points=["adapter_index"], wait_for_completion=wait_for_completion)
        return value

    def get_addressing_mode(self, update=False, wait_for_completion=False):
        value = self._addressing_mode[Constants.VALUE]
        if update and self._addressing_mode[Constants.UPDATING] is False:
            self.update(data_points=["addressing_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_availability(self, update=False, wait_for_completion=False):
        value = self._availability[Constants.VALUE]
        if update and self._availability[Constants.UPDATING] is False:
            self.update(data_points=["availability"], wait_for_completion=wait_for_completion)
        return value

    def get_capability_descriptions(self, update=False, wait_for_completion=False):
        value = self._capability_descriptions[Constants.VALUE]
        if update and self._capability_descriptions[Constants.UPDATING] is False:
            self.update(data_points=["capability_descriptions"], wait_for_completion=wait_for_completion)
        return value

    def get_caption(self, update=False, wait_for_completion=False):
        value = self._caption[Constants.VALUE]
        if update and self._caption[Constants.UPDATING] is False:
            self.update(data_points=["caption"], wait_for_completion=wait_for_completion)
        return value

    def get_chip_to_chip_interconnect_mode(self, update=False, wait_for_completion=False):
        value = self._chip_to_chip_interconnect_mode[Constants.VALUE]
        if update and self._chip_to_chip_interconnect_mode[Constants.UPDATING] is False:
            self.update(data_points=["chip_to_chip_interconnect_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_as_bitmap(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_as_bitmap[Constants.VALUE]
        if update and self._clock_event_reasons_as_bitmap[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_as_bitmap"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_application_setting(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_application_setting[Constants.VALUE]
        if update and self._clock_event_reasons_application_setting[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_application_setting"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_is_hardware_limited(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_is_hardware_limited[Constants.VALUE]
        if update and self._clock_event_reasons_is_hardware_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_is_hardware_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_gpu_idle_limited(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_gpu_idle_limited[Constants.VALUE]
        if update and self._clock_event_reasons_gpu_idle_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_gpu_idle_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_software_power_limited(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_software_power_limited[Constants.VALUE]
        if update and self._clock_event_reasons_software_power_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_software_power_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_software_thermal_limited(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_software_thermal_limited[Constants.VALUE]
        if update and self._clock_event_reasons_software_thermal_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_software_thermal_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_power_break_slowdown_limited(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_power_break_slowdown_limited[Constants.VALUE]
        if update and self._clock_event_reasons_power_break_slowdown_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_power_break_slowdown_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_supported(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_supported[Constants.VALUE]
        if update and self._clock_event_reasons_supported[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_sync_boost(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_sync_boost[Constants.VALUE]
        if update and self._clock_event_reasons_sync_boost[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_sync_boost"], wait_for_completion=wait_for_completion)
        return value

    def get_clock_event_reasons_thermal_limited(self, update=False, wait_for_completion=False):
        value = self._clock_event_reasons_thermal_limited[Constants.VALUE]
        if update and self._clock_event_reasons_thermal_limited[Constants.UPDATING] is False:
            self.update(data_points=["clock_event_reasons_thermal_limited"], wait_for_completion=wait_for_completion)
        return value

    def get_color_table_entries(self, update=False, wait_for_completion=False):
        value = self._color_table_entries[Constants.VALUE]
        if update and self._color_table_entries[Constants.UPDATING] is False:
            self.update(data_points=["color_table_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_compute_cap(self, update=False, wait_for_completion=False):
        value = self._compute_cap[Constants.VALUE]
        if update and self._compute_cap[Constants.UPDATING] is False:
            self.update(data_points=["compute_cap"], wait_for_completion=wait_for_completion)
        return value

    def get_compute_mode(self, update=False, wait_for_completion=False):
        value = self._compute_mode[Constants.VALUE]
        if update and self._compute_mode[Constants.UPDATING] is False:
            self.update(data_points=["compute_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_config_manager_error_code(self, update=False, wait_for_completion=False):
        value = self._config_manager_error_code[Constants.VALUE]
        if update and self._config_manager_error_code[Constants.UPDATING] is False:
            self.update(data_points=["config_manager_error_code"], wait_for_completion=wait_for_completion)
        return value

    def get_config_manager_user_config(self, update=False, wait_for_completion=False):
        value = self._config_manager_user_config[Constants.VALUE]
        if update and self._config_manager_user_config[Constants.UPDATING] is False:
            self.update(data_points=["config_manager_user_config"], wait_for_completion=wait_for_completion)
        return value

    def get_core_voltage(self, update=False, wait_for_completion=False):
        value = self._core_voltage[Constants.VALUE]
        if update and self._core_voltage[Constants.UPDATING] is False:
            self.update(data_points=["core_voltage"], wait_for_completion=wait_for_completion)
        return value

    def get_core_voltage_range(self, update=False, wait_for_completion=False):
        value = self._core_voltage_range[Constants.VALUE]
        if update and self._core_voltage_range[Constants.UPDATING] is False:
            self.update(data_points=["core_voltage_range"], wait_for_completion=wait_for_completion)
        return value

    def get_creation_class_name(self, update=False, wait_for_completion=False):
        value = self._creation_class_name[Constants.VALUE]
        if update and self._creation_class_name[Constants.UPDATING] is False:
            self.update(data_points=["creation_class_name"], wait_for_completion=wait_for_completion)
        return value

    def get_current_bits_per_pixel(self, update=False, wait_for_completion=False):
        value = self._current_bits_per_pixel[Constants.VALUE]
        if update and self._current_bits_per_pixel[Constants.UPDATING] is False:
            self.update(data_points=["current_bits_per_pixel"], wait_for_completion=wait_for_completion)
        return value

    def get_current_horizontal_resolution(self, update=False, wait_for_completion=False):
        value = self._current_horizontal_resolution[Constants.VALUE]
        if update and self._current_horizontal_resolution[Constants.UPDATING] is False:
            self.update(data_points=["current_horizontal_resolution"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_colors(self, update=False, wait_for_completion=False):
        value = self._current_number_of_colors[Constants.VALUE]
        if update and self._current_number_of_colors[Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_colors"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_columns(self, update=False, wait_for_completion=False):
        value = self._current_number_of_columns[Constants.VALUE]
        if update and self._current_number_of_columns[Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_columns"], wait_for_completion=wait_for_completion)
        return value

    def get_current_number_of_rows(self, update=False, wait_for_completion=False):
        value = self._current_number_of_rows[Constants.VALUE]
        if update and self._current_number_of_rows[Constants.UPDATING] is False:
            self.update(data_points=["current_number_of_rows"], wait_for_completion=wait_for_completion)
        return value

    def get_current_refresh_rate(self, update=False, wait_for_completion=False):
        value = self._current_refresh_rate[Constants.VALUE]
        if update and self._current_refresh_rate[Constants.UPDATING] is False:
            self.update(data_points=["current_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_current_scan_mode(self, update=False, wait_for_completion=False):
        value = self._current_scan_mode[Constants.VALUE]
        if update and self._current_scan_mode[Constants.UPDATING] is False:
            self.update(data_points=["current_scan_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_current_vertical_resolution(self, update=False, wait_for_completion=False):
        value = self._current_vertical_resolution[Constants.VALUE]
        if update and self._current_vertical_resolution[Constants.UPDATING] is False:
            self.update(data_points=["current_vertical_resolution"], wait_for_completion=wait_for_completion)
        return value

    def get_description(self, update=False, wait_for_completion=False):
        value = self._description[Constants.VALUE]
        if update and self._description[Constants.UPDATING] is False:
            self.update(data_points=["description"], wait_for_completion=wait_for_completion)
        return value

    def get_device_id(self, update=False, wait_for_completion=False):
        value = self._device_id[Constants.VALUE]
        if update and self._device_id[Constants.UPDATING] is False:
            self.update(data_points=["device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_device_specific_pens(self, update=False, wait_for_completion=False):
        value = self._device_specific_pens[Constants.VALUE]
        if update and self._device_specific_pens[Constants.UPDATING] is False:
            self.update(data_points=["device_specific_pens"], wait_for_completion=wait_for_completion)
        return value

    def get_display_active(self, update=False, wait_for_completion=False):
        value = self._display_active[Constants.VALUE]
        if update and self._display_active[Constants.UPDATING] is False:
            self.update(data_points=["display_active"], wait_for_completion=wait_for_completion)
        return value

    def get_display_mode(self, update=False, wait_for_completion=False):
        value = self._display_mode[Constants.VALUE]
        if update and self._display_mode[Constants.UPDATING] is False:
            self.update(data_points=["display_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_dither_type(self, update=False, wait_for_completion=False):
        value = self._dither_type[Constants.VALUE]
        if update and self._dither_type[Constants.UPDATING] is False:
            self.update(data_points=["dither_type"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_date(self, update=False, wait_for_completion=False):
        value = self._driver_date[Constants.VALUE]
        if update and self._driver_date[Constants.UPDATING] is False:
            self.update(data_points=["driver_date"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_model_current(self, update=False, wait_for_completion=False):
        value = self._driver_model_current[Constants.VALUE]
        if update and self._driver_model_current[Constants.UPDATING] is False:
            self.update(data_points=["driver_model_current"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_model_pending(self, update=False, wait_for_completion=False):
        value = self._driver_model_pending[Constants.VALUE]
        if update and self._driver_model_pending[Constants.UPDATING] is False:
            self.update(data_points=["driver_model_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_driver_version(self, update=False, wait_for_completion=False):
        value = self._driver_version[Constants.VALUE]
        if update and self._driver_version[Constants.UPDATING] is False:
            self.update(data_points=["driver_version"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_cbu(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_cbu[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_primary_cache[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_register_file(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_register_file[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_secondary_cache[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_shared_memory[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_sram(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_sram[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_texture_memory[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_total(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_total[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_all_time_in_video_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_all_time_in_video_memory[Constants.VALUE]
        if update and self._ecc_errors_corrected_all_time_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_cbu(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_cbu[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_primary_cache[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_register_file(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_register_file[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_shared_memory[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_sram(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_sram[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_texture_memory[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_total(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_total[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_corrected_since_reboot_in_video_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_corrected_since_reboot_in_video_memory[Constants.VALUE]
        if update and self._ecc_errors_corrected_since_reboot_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_corrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_cbu(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_cbu[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_primary_cache[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_register_file(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_register_file[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_shared_memory[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_sram(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_sram[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_texture_memory[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_total(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_total[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_all_time_in_video_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_all_time_in_video_memory[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_all_time_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_cbu(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_cbu[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_cbu[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_register_file(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_register_file[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_register_file[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_sram(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_sram[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_sram[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_total(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_total[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_total[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_errors_uncorrected_since_reboot_in_video_memory(self, update=False, wait_for_completion=False):
        value = self._ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.VALUE]
        if update and self._ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.UPDATING] is False:
            self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_mode_current(self, update=False, wait_for_completion=False):
        value = self._ecc_mode_current[Constants.VALUE]
        if update and self._ecc_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["ecc_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_ecc_mode_pending(self, update=False, wait_for_completion=False):
        value = self._ecc_mode_pending[Constants.VALUE]
        if update and self._ecc_mode_pending[Constants.UPDATING] is False:
            self.update(data_points=["ecc_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_average_FPS(self, update=False, wait_for_completion=False):
        value = self._encoder_average_FPS[Constants.VALUE]
        if update and self._encoder_average_FPS[Constants.UPDATING] is False:
            self.update(data_points=["encoder_average_FPS"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_average_latency(self, update=False, wait_for_completion=False):
        value = self._encoder_average_latency[Constants.VALUE]
        if update and self._encoder_average_latency[Constants.UPDATING] is False:
            self.update(data_points=["encoder_average_latency"], wait_for_completion=wait_for_completion)
        return value

    def get_encoder_session_count(self, update=False, wait_for_completion=False):
        value = self._encoder_session_count[Constants.VALUE]
        if update and self._encoder_session_count[Constants.UPDATING] is False:
            self.update(data_points=["encoder_session_count"], wait_for_completion=wait_for_completion)
        return value

    def get_engine_clock_range(self, update=False, wait_for_completion=False):
        value = self._engine_clock_range[Constants.VALUE]
        if update and self._engine_clock_range[Constants.UPDATING] is False:
            self.update(data_points=["engine_clock_range"], wait_for_completion=wait_for_completion)
        return value

    def get_error_cleared(self, update=False, wait_for_completion=False):
        value = self._error_cleared[Constants.VALUE]
        if update and self._error_cleared[Constants.UPDATING] is False:
            self.update(data_points=["error_cleared"], wait_for_completion=wait_for_completion)
        return value

    def get_error_description(self, update=False, wait_for_completion=False):
        value = self._error_description[Constants.VALUE]
        if update and self._error_description[Constants.UPDATING] is False:
            self.update(data_points=["error_description"], wait_for_completion=wait_for_completion)
        return value

    def get_fabric_state(self, update=False, wait_for_completion=False):
        value = self._fabric_state[Constants.VALUE]
        if update and self._fabric_state[Constants.UPDATING] is False:
            self.update(data_points=["fabric_state"], wait_for_completion=wait_for_completion)
        return value

    def get_fabric_status(self, update=False, wait_for_completion=False):
        value = self._fabric_status[Constants.VALUE]
        if update and self._fabric_status[Constants.UPDATING] is False:
            self.update(data_points=["fabric_status"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_percentage(self, update=False, wait_for_completion=False):
        value = self._fan_speed_percentage[Constants.VALUE]
        if update and self._fan_speed_percentage[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_percentage"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_percentage_range(self, update=False, wait_for_completion=False):
        value = self._fan_speed_percentage_range[Constants.VALUE]
        if update and self._fan_speed_percentage_range[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_percentage_range"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_RPM(self, update=False, wait_for_completion=False):
        value = self._fan_speed_RPM[Constants.VALUE]
        if update and self._fan_speed_RPM[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_RPM"], wait_for_completion=wait_for_completion)
        return value

    def get_fan_speed_RPM_range(self, update=False, wait_for_completion=False):
        value = self._fan_speed_RPM_range[Constants.VALUE]
        if update and self._fan_speed_RPM_range[Constants.UPDATING] is False:
            self.update(data_points=["fan_speed_RPM_range"], wait_for_completion=wait_for_completion)
        return value

    def get_fractional_multi_vGPU(self, update=False, wait_for_completion=False):
        value = self._fractional_multi_vGPU[Constants.VALUE]
        if update and self._fractional_multi_vGPU[Constants.UPDATING] is False:
            self.update(data_points=["fractional_multi_vGPU"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_default_shader_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_application_default_shader_clock[Constants.VALUE]
        if update and self._frequency_application_default_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_default_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_default_memory_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_application_default_memory_clock[Constants.VALUE]
        if update and self._frequency_application_default_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_default_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_memory_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_application_memory_clock[Constants.VALUE]
        if update and self._frequency_application_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_application_shader_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_application_shader_clock[Constants.VALUE]
        if update and self._frequency_application_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_application_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_memory_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_maximum_memory_clock[Constants.VALUE]
        if update and self._frequency_maximum_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_shader_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_maximum_shader_clock[Constants.VALUE]
        if update and self._frequency_maximum_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_maximum_streaming_multiprocessor_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_maximum_streaming_multiprocessor_clock[Constants.VALUE]
        if update and self._frequency_maximum_streaming_multiprocessor_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_maximum_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_memory_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_memory_clock[Constants.VALUE]
        if update and self._frequency_memory_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_memory_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_shader_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_shader_clock[Constants.VALUE]
        if update and self._frequency_shader_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_shader_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_streaming_multiprocessor_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_streaming_multiprocessor_clock[Constants.VALUE]
        if update and self._frequency_streaming_multiprocessor_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_frequency_video_clock(self, update=False, wait_for_completion=False):
        value = self._frequency_video_clock[Constants.VALUE]
        if update and self._frequency_video_clock[Constants.UPDATING] is False:
            self.update(data_points=["frequency_video_clock"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_multi_vGPU(self, update=False, wait_for_completion=False):
        value = self._heterogenous_multi_vGPU[Constants.VALUE]
        if update and self._heterogenous_multi_vGPU[Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_multi_vGPU"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_time_slice_profile(self, update=False, wait_for_completion=False):
        value = self._heterogenous_time_slice_profile[Constants.VALUE]
        if update and self._heterogenous_time_slice_profile[Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_time_slice_profile"], wait_for_completion=wait_for_completion)
        return value

    def get_heterogenous_time_slice_sizes(self, update=False, wait_for_completion=False):
        value = self._heterogenous_time_slice_sizes[Constants.VALUE]
        if update and self._heterogenous_time_slice_sizes[Constants.UPDATING] is False:
            self.update(data_points=["heterogenous_time_slice_sizes"], wait_for_completion=wait_for_completion)
        return value

    def get_ICM_indent(self, update=False, wait_for_completion=False):
        value = self._ICM_indent[Constants.VALUE]
        if update and self._ICM_indent[Constants.UPDATING] is False:
            self.update(data_points=["ICM_indent"], wait_for_completion=wait_for_completion)
        return value

    def get_ICM_method(self, update=False, wait_for_completion=False):
        value = self._ICM_method[Constants.VALUE]
        if update and self._ICM_method[Constants.UPDATING] is False:
            self.update(data_points=["ICM_method"], wait_for_completion=wait_for_completion)
        return value

    def get_inf_filename(self, update=False, wait_for_completion=False):
        value = self._inf_filename[Constants.VALUE]
        if update and self._inf_filename[Constants.UPDATING] is False:
            self.update(data_points=["inf_filename"], wait_for_completion=wait_for_completion)
        return value

    def get_inf_section(self, update=False, wait_for_completion=False):
        value = self._inf_section[Constants.VALUE]
        if update and self._inf_section[Constants.UPDATING] is False:
            self.update(data_points=["inf_section"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_ecc(self, update=False, wait_for_completion=False):
        value = self._info_ROM_ecc[Constants.VALUE]
        if update and self._info_ROM_ecc[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_ecc"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_oem(self, update=False, wait_for_completion=False):
        value = self._info_ROM_oem[Constants.VALUE]
        if update and self._info_ROM_oem[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_oem"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_power(self, update=False, wait_for_completion=False):
        value = self._info_ROM_power[Constants.VALUE]
        if update and self._info_ROM_power[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_power"], wait_for_completion=wait_for_completion)
        return value

    def get_info_ROM_version(self, update=False, wait_for_completion=False):
        value = self._info_ROM_version[Constants.VALUE]
        if update and self._info_ROM_version[Constants.UPDATING] is False:
            self.update(data_points=["info_ROM_version"], wait_for_completion=wait_for_completion)
        return value

    def get_install_date(self, update=False, wait_for_completion=False):
        value = self._install_date[Constants.VALUE]
        if update and self._install_date[Constants.UPDATING] is False:
            self.update(data_points=["install_date"], wait_for_completion=wait_for_completion)
        return value

    def get_installed_display_drivers(self, update=False, wait_for_completion=False):
        value = self._installed_display_drivers[Constants.VALUE]
        if update and self._installed_display_drivers[Constants.UPDATING] is False:
            self.update(data_points=["installed_display_drivers"], wait_for_completion=wait_for_completion)
        return value

    def get_last_error_code(self, update=False, wait_for_completion=False):
        value = self._last_error_code[Constants.VALUE]
        if update and self._last_error_code[Constants.UPDATING] is False:
            self.update(data_points=["last_error_code"], wait_for_completion=wait_for_completion)
        return value

    def get_max_memory_supported(self, update=False, wait_for_completion=False):
        value = self._max_memory_supported[Constants.VALUE]
        if update and self._max_memory_supported[Constants.UPDATING] is False:
            self.update(data_points=["max_memory_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_max_number_controlled(self, update=False, wait_for_completion=False):
        value = self._max_number_controlled[Constants.VALUE]
        if update and self._max_number_controlled[Constants.UPDATING] is False:
            self.update(data_points=["max_number_controlled"], wait_for_completion=wait_for_completion)
        return value

    def get_max_refresh_rate(self, update=False, wait_for_completion=False):
        value = self._max_refresh_rate[Constants.VALUE]
        if update and self._max_refresh_rate[Constants.UPDATING] is False:
            self.update(data_points=["max_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_clock_range(self, update=False, wait_for_completion=False):
        value = self._memory_clock_range[Constants.VALUE]
        if update and self._memory_clock_range[Constants.UPDATING] is False:
            self.update(data_points=["memory_clock_range"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_free(self, update=False, wait_for_completion=False):
        value = self._memory_free[Constants.VALUE]
        if update and self._memory_free[Constants.UPDATING] is False:
            self.update(data_points=["memory_free"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_reserved(self, update=False, wait_for_completion=False):
        value = self._memory_reserved[Constants.VALUE]
        if update and self._memory_reserved[Constants.UPDATING] is False:
            self.update(data_points=["memory_reserved"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_total(self, update=False, wait_for_completion=False):
        value = self._memory_total[Constants.VALUE]
        if update and self._memory_total[Constants.UPDATING] is False:
            self.update(data_points=["memory_total"], wait_for_completion=wait_for_completion)
        return value

    def get_memory_used(self, update=False, wait_for_completion=False):
        value = self._memory_used[Constants.VALUE]
        if update and self._memory_used[Constants.UPDATING] is False:
            self.update(data_points=["memory_used"], wait_for_completion=wait_for_completion)
        return value

    def get_min_refresh_rate(self, update=False, wait_for_completion=False):
        value = self._min_refresh_rate[Constants.VALUE]
        if update and self._min_refresh_rate[Constants.UPDATING] is False:
            self.update(data_points=["min_refresh_rate"], wait_for_completion=wait_for_completion)
        return value

    def get_monochrome(self, update=False, wait_for_completion=False):
        value = self._monochrome[Constants.VALUE]
        if update and self._monochrome[Constants.UPDATING] is False:
            self.update(data_points=["monochrome"], wait_for_completion=wait_for_completion)
        return value

    def get_multi_instance_GPU_mode_current(self, update=False, wait_for_completion=False):
        value = self._multi_instance_GPU_mode_current[Constants.VALUE]
        if update and self._multi_instance_GPU_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["multi_instance_GPU_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_multi_instance_GPU_mode_pending(self, update=False, wait_for_completion=False):
        value = self._multi_instance_GPU_mode_pending[Constants.VALUE]
        if update and self._multi_instance_GPU_mode_pending[Constants.UPDATING] is False:
            self.update(data_points=["multi_instance_GPU_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_name(self, update=False, wait_for_completion=False):
        value = self._name[Constants.VALUE]
        if update and self._name[Constants.UPDATING] is False:
            self.update(data_points=["name"], wait_for_completion=wait_for_completion)
        return value

    def get_number_of_color_planes(self, update=False, wait_for_completion=False):
        value = self._number_of_color_planes[Constants.VALUE]
        if update and self._number_of_color_planes[Constants.UPDATING] is False:
            self.update(data_points=["number_of_color_planes"], wait_for_completion=wait_for_completion)
        return value

    def get_number_of_video_pages(self, update=False, wait_for_completion=False):
        value = self._number_of_video_pages[Constants.VALUE]
        if update and self._number_of_video_pages[Constants.UPDATING] is False:
            self.update(data_points=["number_of_video_pages"], wait_for_completion=wait_for_completion)
        return value

    def get_operating_mode_current(self, update=False, wait_for_completion=False):
        value = self._operating_mode_current[Constants.VALUE]
        if update and self._operating_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["operating_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_operating_mode_pending(self, update=False, wait_for_completion=False):
        value = self._operating_mode_pending[Constants.VALUE]
        if update and self._operating_mode_pending[Constants.UPDATING] is False:
            self.update(data_points=["operating_mode_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_bus(self, update=False, wait_for_completion=False):
        value = self._pci_bus[Constants.VALUE]
        if update and self._pci_bus[Constants.UPDATING] is False:
            self.update(data_points=["pci_bus"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_bus_id(self, update=False, wait_for_completion=False):
        value = self._pci_bus_id[Constants.VALUE]
        if update and self._pci_bus_id[Constants.UPDATING] is False:
            self.update(data_points=["pci_bus_id"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_device(self, update=False, wait_for_completion=False):
        value = self._pci_device[Constants.VALUE]
        if update and self._pci_device[Constants.UPDATING] is False:
            self.update(data_points=["pci_device"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_device_id(self, update=False, wait_for_completion=False):
        value = self._pci_device_id[Constants.VALUE]
        if update and self._pci_device_id[Constants.UPDATING] is False:
            self.update(data_points=["pci_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_domain(self, update=False, wait_for_completion=False):
        value = self._pci_domain[Constants.VALUE]
        if update and self._pci_domain[Constants.UPDATING] is False:
            self.update(data_points=["pci_domain"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_current(self, update=False, wait_for_completion=False):
        value = self._pci_link_generation_current[Constants.VALUE]
        if update and self._pci_link_generation_current[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_current"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_device_host_maximum(self, update=False, wait_for_completion=False):
        value = self._pci_link_generation_device_host_maximum[Constants.VALUE]
        if update and self._pci_link_generation_device_host_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_device_host_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_gpu_maximum(self, update=False, wait_for_completion=False):
        value = self._pci_link_generation_gpu_maximum[Constants.VALUE]
        if update and self._pci_link_generation_gpu_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_gpu_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_generation_maximum(self, update=False, wait_for_completion=False):
        value = self._pci_link_generation_maximum[Constants.VALUE]
        if update and self._pci_link_generation_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_generation_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_width_current(self, update=False, wait_for_completion=False):
        value = self._pci_link_width_current[Constants.VALUE]
        if update and self._pci_link_width_current[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_width_current"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_link_width_maximum(self, update=False, wait_for_completion=False):
        value = self._pci_link_width_maximum[Constants.VALUE]
        if update and self._pci_link_width_maximum[Constants.UPDATING] is False:
            self.update(data_points=["pci_link_width_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_pci_sub_device_id(self, update=False, wait_for_completion=False):
        value = self._pci_sub_device_id[Constants.VALUE]
        if update and self._pci_sub_device_id[Constants.UPDATING] is False:
            self.update(data_points=["pci_sub_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_persistence_mode(self, update=False, wait_for_completion=False):
        value = self._persistence_mode[Constants.VALUE]
        if update and self._persistence_mode[Constants.UPDATING] is False:
            self.update(data_points=["persistence_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_PNP_device_id(self, update=False, wait_for_completion=False):
        value = self._PNP_device_id[Constants.VALUE]
        if update and self._PNP_device_id[Constants.UPDATING] is False:
            self.update(data_points=["PNP_device_id"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw(self, update=False, wait_for_completion=False):
        value = self._power_draw[Constants.VALUE]
        if update and self._power_draw[Constants.UPDATING] is False:
            self.update(data_points=["power_draw"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_average(self, update=False, wait_for_completion=False):
        value = self._power_draw_average[Constants.VALUE]
        if update and self._power_draw_average[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_average"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_default_limit(self, update=False, wait_for_completion=False):
        value = self._power_draw_default_limit[Constants.VALUE]
        if update and self._power_draw_default_limit[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_default_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_enforced_limit(self, update=False, wait_for_completion=False):
        value = self._power_draw_enforced_limit[Constants.VALUE]
        if update and self._power_draw_enforced_limit[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_enforced_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_instant(self, update=False, wait_for_completion=False):
        value = self._power_draw_instant[Constants.VALUE]
        if update and self._power_draw_instant[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_instant"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_limit(self, update=False, wait_for_completion=False):
        value = self._power_draw_limit[Constants.VALUE]
        if update and self._power_draw_limit[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_maximum(self, update=False, wait_for_completion=False):
        value = self._power_draw_maximum[Constants.VALUE]
        if update and self._power_draw_maximum[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_maximum"], wait_for_completion=wait_for_completion)
        return value

    def get_power_draw_minimum(self, update=False, wait_for_completion=False):
        value = self._power_draw_minimum[Constants.VALUE]
        if update and self._power_draw_minimum[Constants.UPDATING] is False:
            self.update(data_points=["power_draw_minimum"], wait_for_completion=wait_for_completion)
        return value

    def get_power_management_capabilities(self, update=False, wait_for_completion=False):
        value = self._power_management_capabilities[Constants.VALUE]
        if update and self._power_management_capabilities[Constants.UPDATING] is False:
            self.update(data_points=["power_management_capabilities"], wait_for_completion=wait_for_completion)
        return value

    def get_power_management_supported(self, update=False, wait_for_completion=False):
        value = self._power_management_supported[Constants.VALUE]
        if update and self._power_management_supported[Constants.UPDATING] is False:
            self.update(data_points=["power_management_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_free(self, update=False, wait_for_completion=False):
        value = self._protected_memory_free[Constants.VALUE]
        if update and self._protected_memory_free[Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_free"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_total(self, update=False, wait_for_completion=False):
        value = self._protected_memory_total[Constants.VALUE]
        if update and self._protected_memory_total[Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_total"], wait_for_completion=wait_for_completion)
        return value

    def get_protected_memory_used(self, update=False, wait_for_completion=False):
        value = self._protected_memory_used[Constants.VALUE]
        if update and self._protected_memory_used[Constants.UPDATING] is False:
            self.update(data_points=["protected_memory_used"], wait_for_completion=wait_for_completion)
        return value

    def get_protocol_supported(self, update=False, wait_for_completion=False):
        value = self._protocol_supported[Constants.VALUE]
        if update and self._protocol_supported[Constants.UPDATING] is False:
            self.update(data_points=["protocol_supported"], wait_for_completion=wait_for_completion)
        return value

    def get_performance_state(self, update=False, wait_for_completion=False):
        value = self._performance_state[Constants.VALUE]
        if update and self._performance_state[Constants.UPDATING] is False:
            self.update(data_points=["performance_state"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_double_bit_ecc_errors_count(self, update=False, wait_for_completion=False):
        value = self._retired_pages_double_bit_ecc_errors_count[Constants.VALUE]
        if update and self._retired_pages_double_bit_ecc_errors_count[Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_double_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_single_bit_ecc_errors_count(self, update=False, wait_for_completion=False):
        value = self._retired_pages_single_bit_ecc_errors_count[Constants.VALUE]
        if update and self._retired_pages_single_bit_ecc_errors_count[Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_single_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)
        return value

    def get_retired_pages_pending(self, update=False, wait_for_completion=False):
        value = self._retired_pages_pending[Constants.VALUE]
        if update and self._retired_pages_pending[Constants.UPDATING] is False:
            self.update(data_points=["retired_pages_pending"], wait_for_completion=wait_for_completion)
        return value

    def get_reserved_system_palette_entries(self, update=False, wait_for_completion=False):
        value = self._reserved_system_palette_entries[Constants.VALUE]
        if update and self._reserved_system_palette_entries[Constants.UPDATING] is False:
            self.update(data_points=["reserved_system_palette_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_reset_required(self, update=False, wait_for_completion=False):
        value = self._reset_required[Constants.VALUE]
        if update and self._reset_required[Constants.UPDATING] is False:
            self.update(data_points=["reset_required"], wait_for_completion=wait_for_completion)
        return value

    def get_reset_and_drain_recommended(self, update=False, wait_for_completion=False):
        value = self._reset_and_drain_recommended[Constants.VALUE]
        if update and self._reset_and_drain_recommended[Constants.UPDATING] is False:
            self.update(data_points=["reset_and_drain_recommended"], wait_for_completion=wait_for_completion)
        return value

    def get_serial(self, update=False, wait_for_completion=False):
        value = self._serial[Constants.VALUE]
        if update and self._serial[Constants.UPDATING] is False:
            self.update(data_points=["serial"], wait_for_completion=wait_for_completion)
        return value

    def get_specification_version(self, update=False, wait_for_completion=False):
        value = self._specification_version[Constants.VALUE]
        if update and self._specification_version[Constants.UPDATING] is False:
            self.update(data_points=["specification_version"], wait_for_completion=wait_for_completion)
        return value

    def get_status(self, update=False, wait_for_completion=False):
        value = self._status[Constants.VALUE]
        if update and self._status[Constants.UPDATING] is False:
            self.update(data_points=["status"], wait_for_completion=wait_for_completion)
        return value

    def get_status_info(self, update=False, wait_for_completion=False):
        value = self._status_info[Constants.VALUE]
        if update and self._status_info[Constants.UPDATING] is False:
            self.update(data_points=["status_info"], wait_for_completion=wait_for_completion)
        return value

    def get_system_creation_class_name(self, update=False, wait_for_completion=False):
        value = self._system_creation_class_name[Constants.VALUE]
        if update and self._system_creation_class_name[Constants.UPDATING] is False:
            self.update(data_points=["system_creation_class_name"], wait_for_completion=wait_for_completion)
        return value

    def get_system_name(self, update=False, wait_for_completion=False):
        value = self._system_name[Constants.VALUE]
        if update and self._system_name[Constants.UPDATING] is False:
            self.update(data_points=["system_name"], wait_for_completion=wait_for_completion)
        return value

    def get_system_palette_entries(self, update=False, wait_for_completion=False):
        value = self._system_palette_entries[Constants.VALUE]
        if update and self._system_palette_entries[Constants.UPDATING] is False:
            self.update(data_points=["system_palette_entries"], wait_for_completion=wait_for_completion)
        return value

    def get_GPU_system_processor_mode_current(self, update=False, wait_for_completion=False):
        value = self._GPU_system_processor_mode_current[Constants.VALUE]
        if update and self._GPU_system_processor_mode_current[Constants.UPDATING] is False:
            self.update(data_points=["GPU_system_processor_mode_current"], wait_for_completion=wait_for_completion)
        return value

    def get_GPU_system_processor_mode_default(self, update=False, wait_for_completion=False):
        value = self._GPU_system_processor_mode_default[Constants.VALUE]
        if update and self._GPU_system_processor_mode_default[Constants.UPDATING] is False:
            self.update(data_points=["GPU_system_processor_mode_default"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_core(self, update=False, wait_for_completion=False):
        value = self._temperature_core[Constants.VALUE]
        if update and self._temperature_core[Constants.UPDATING] is False:
            self.update(data_points=["temperature_core"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_core_limit(self, update=False, wait_for_completion=False):
        value = self._temperature_core_limit[Constants.VALUE]
        if update and self._temperature_core_limit[Constants.UPDATING] is False:
            self.update(data_points=["temperature_core_limit"], wait_for_completion=wait_for_completion)
        return value

    def get_temperature_memory(self, update=False, wait_for_completion=False):
        value = self._temperature_memory[Constants.VALUE]
        if update and self._temperature_memory[Constants.UPDATING] is False:
            self.update(data_points=["temperature_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_time_of_last_reset(self, update=False, wait_for_completion=False):
        value = self._time_of_last_reset[Constants.VALUE]
        if update and self._time_of_last_reset[Constants.UPDATING] is False:
            self.update(data_points=["time_of_last_reset"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_decoder(self, update=False, wait_for_completion=False):
        value = self._utilization_decoder[Constants.VALUE]
        if update and self._utilization_decoder[Constants.UPDATING] is False:
            self.update(data_points=["utilization_decoder"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_encoder(self, update=False, wait_for_completion=False):
        value = self._utilization_encoder[Constants.VALUE]
        if update and self._utilization_encoder[Constants.UPDATING] is False:
            self.update(data_points=["utilization_encoder"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_gpu(self, update=False, wait_for_completion=False):
        value = self._utilization_gpu[Constants.VALUE]
        if update and self._utilization_gpu[Constants.UPDATING] is False:
            self.update(data_points=["utilization_gpu"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_jpeg(self, update=False, wait_for_completion=False):
        value = self._utilization_jpeg[Constants.VALUE]
        if update and self._utilization_jpeg[Constants.UPDATING] is False:
            self.update(data_points=["utilization_jpeg"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_memory(self, update=False, wait_for_completion=False):
        value = self._utilization_memory[Constants.VALUE]
        if update and self._utilization_memory[Constants.UPDATING] is False:
            self.update(data_points=["utilization_memory"], wait_for_completion=wait_for_completion)
        return value

    def get_utilization_optical_flow(self, update=False, wait_for_completion=False):
        value = self._utilization_optical_flow[Constants.VALUE]
        if update and self._utilization_optical_flow[Constants.UPDATING] is False:
            self.update(data_points=["utilization_optical_flow"], wait_for_completion=wait_for_completion)
        return value

    def get_uuid(self, update=False, wait_for_completion=False):
        value = self._uuid[Constants.VALUE]
        if update and self._uuid[Constants.UPDATING] is False:
            self.update(data_points=["uuid"], wait_for_completion=wait_for_completion)
        return value

    def get_vbios_version(self, update=False, wait_for_completion=False):
        value = self._vbios_version[Constants.VALUE]
        if update and self._vbios_version[Constants.UPDATING] is False:
            self.update(data_points=["vbios_version"], wait_for_completion=wait_for_completion)
        return value

    def get_video_architecture(self, update=False, wait_for_completion=False):
        value = self._video_architecture[Constants.VALUE]
        if update and self._video_architecture[Constants.UPDATING] is False:
            self.update(data_points=["video_architecture"], wait_for_completion=wait_for_completion)
        return value

    def get_video_memory_type(self, update=False, wait_for_completion=False):
        value = self._video_memory_type[Constants.VALUE]
        if update and self._video_memory_type[Constants.UPDATING] is False:
            self.update(data_points=["video_memory_type"], wait_for_completion=wait_for_completion)
        return value

    def get_video_mode(self, update=False, wait_for_completion=False):
        value = self._video_mode[Constants.VALUE]
        if update and self._video_mode[Constants.UPDATING] is False:
            self.update(data_points=["video_mode"], wait_for_completion=wait_for_completion)
        return value

    def get_video_mode_description(self, update=False, wait_for_completion=False):
        value = self._video_mode_description[Constants.VALUE]
        if update and self._video_mode_description[Constants.UPDATING] is False:
            self.update(data_points=["video_mode_description"], wait_for_completion=wait_for_completion)
        return value

    def get_video_processor(self, update=False, wait_for_completion=False):
        value = self._video_processor[Constants.VALUE]
        if update and self._video_processor[Constants.UPDATING] is False:
            self.update(data_points=["video_processor"], wait_for_completion=wait_for_completion)
        return value

    def set_accelerator_capabilities(self, value=None):
        self._accelerator_capabilities[Constants.MANUALLY_SET] = value != None
        self._accelerator_capabilities = value

    def set_accounting_mode_enabled(self, value=None):
        self._accounting_mode_enabled[Constants.MANUALLY_SET] = value != None
        self._accounting_mode_enabled = value

    def set_accounting_mode_buffer_size(self, value=None):
        self._accounting_mode_buffer_size[Constants.MANUALLY_SET] = value != None
        self._accounting_mode_buffer_size = value

    def set_adapter_compatibility(self, value=None):
        self._adapter_compatibility[Constants.MANUALLY_SET] = value != None
        self._adapter_compatibility = value

    def set_adapter_DAC_type(self, value=None):
        self._adapter_DAC_type[Constants.MANUALLY_SET] = value != None
        self._adapter_DAC_type = value

    def set_adapter_id(self, value=None):
        self._adapter_id[Constants.MANUALLY_SET] = value != None
        self._adapter_id = value

    def set_adapter_index(self, value=None):
        self._adapter_index[Constants.MANUALLY_SET] = value != None
        self._adapter_index = value

    def set_addressing_mode(self, value=None):
        self._addressing_mode[Constants.MANUALLY_SET] = value != None
        self._addressing_mode = value

    def set_availability(self, value=None):
        self._availability[Constants.MANUALLY_SET] = value != None
        self._availability = value

    def set_capability_descriptions(self, value=None):
        self._capability_descriptions[Constants.MANUALLY_SET] = value != None
        self._capability_descriptions = value

    def set_caption(self, value=None):
        self._caption[Constants.MANUALLY_SET] = value != None
        self._caption = value

    def set_chip_to_chip_interconnect_mode(self, value=None):
        self._chip_to_chip_interconnect_mode[Constants.MANUALLY_SET] = value != None
        self._chip_to_chip_interconnect_mode = value

    def set_clock_event_reasons_as_bitmap(self, value=None):
        self._clock_event_reasons_as_bitmap[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_as_bitmap = value

    def set_clock_event_reasons_application_setting(self, value=None):
        self._clock_event_reasons_application_setting[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_application_setting = value

    def set_clock_event_reasons_is_hardware_limited(self, value=None):
        self._clock_event_reasons_is_hardware_limited[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_is_hardware_limited = value

    def set_clock_event_reasons_gpu_idle_limited(self, value=None):
        self._clock_event_reasons_gpu_idle_limited[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_gpu_idle_limited = value

    def set_clock_event_reasons_software_power_limited(self, value=None):
        self._clock_event_reasons_software_power_limited[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_software_power_limited = value

    def set_clock_event_reasons_software_thermal_limited(self, value=None):
        self._clock_event_reasons_software_thermal_limited[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_software_thermal_limited = value

    def set_clock_event_reasons_power_break_slowdown_limited(self, value=None):
        self._clock_event_reasons_power_break_slowdown_limited[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_power_break_slowdown_limited = value

    def set_clock_event_reasons_supported(self, value=None):
        self._clock_event_reasons_supported[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_supported = value

    def set_clock_event_reasons_sync_boost(self, value=None):
        self._clock_event_reasons_sync_boost[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_sync_boost = value

    def set_clock_event_reasons_thermal_limited(self, value=None):
        self._clock_event_reasons_thermal_limited[Constants.MANUALLY_SET] = value != None
        self._clock_event_reasons_thermal_limited = value

    def set_color_table_entries(self, value=None):
        self._color_table_entries[Constants.MANUALLY_SET] = value != None
        self._color_table_entries = value

    def set_compute_cap(self, value=None):
        self._compute_cap[Constants.MANUALLY_SET] = value != None
        self._compute_cap = value

    def set_compute_mode(self, value=None):
        self._compute_mode[Constants.MANUALLY_SET] = value != None
        self._compute_mode = value

    def set_config_manager_error_code(self, value=None):
        self._config_manager_error_code[Constants.MANUALLY_SET] = value != None
        self._config_manager_error_code = value

    def set_config_manager_user_config(self, value=None):
        self._config_manager_user_config[Constants.MANUALLY_SET] = value != None
        self._config_manager_user_config = value

    def set_core_voltage(self, value=None):
        self._core_voltage[Constants.MANUALLY_SET] = value != None
        self._core_voltage = value

    def set_core_voltage_range(self, value=None):
        self._core_voltage_range[Constants.MANUALLY_SET] = value != None
        self._core_voltage_range = value

    def set_creation_class_name(self, value=None):
        self._creation_class_name[Constants.MANUALLY_SET] = value != None
        self._creation_class_name = value

    def set_current_bits_per_pixel(self, value=None):
        self._current_bits_per_pixel[Constants.MANUALLY_SET] = value != None
        self._current_bits_per_pixel = value

    def set_current_horizontal_resolution(self, value=None):
        self._current_horizontal_resolution[Constants.MANUALLY_SET] = value != None
        self._current_horizontal_resolution = value

    def set_current_number_of_colors(self, value=None):
        self._current_number_of_colors[Constants.MANUALLY_SET] = value != None
        self._current_number_of_colors = value

    def set_current_number_of_columns(self, value=None):
        self._current_number_of_columns[Constants.MANUALLY_SET] = value != None
        self._current_number_of_columns = value

    def set_current_number_of_rows(self, value=None):
        self._current_number_of_rows[Constants.MANUALLY_SET] = value != None
        self._current_number_of_rows = value

    def set_current_refresh_rate(self, value=None):
        self._current_refresh_rate[Constants.MANUALLY_SET] = value != None
        self._current_refresh_rate = value

    def set_current_scan_mode(self, value=None):
        self._current_scan_mode[Constants.MANUALLY_SET] = value != None
        self._current_scan_mode = value

    def set_current_vertical_resolution(self, value=None):
        self._current_vertical_resolution[Constants.MANUALLY_SET] = value != None
        self._current_vertical_resolution = value

    def set_description(self, value=None):
        self._description[Constants.MANUALLY_SET] = value != None
        self._description = value

    def set_device_id(self, value=None):
        self._device_id[Constants.MANUALLY_SET] = value != None
        self._device_id = value

    def set_device_specific_pens(self, value=None):
        self._device_specific_pens[Constants.MANUALLY_SET] = value != None
        self._device_specific_pens = value

    def set_display_active(self, value=None):
        self._display_active[Constants.MANUALLY_SET] = value != None
        self._display_active = value

    def set_display_mode(self, value=None):
        self._display_mode[Constants.MANUALLY_SET] = value != None
        self._display_mode = value

    def set_dither_type(self, value=None):
        self._dither_type[Constants.MANUALLY_SET] = value != None
        self._dither_type = value

    def set_driver_date(self, value=None):
        self._driver_date[Constants.MANUALLY_SET] = value != None
        self._driver_date = value

    def set_driver_model_current(self, value=None):
        self._driver_model_current[Constants.MANUALLY_SET] = value != None
        self._driver_model_current = value

    def set_driver_model_pending(self, value=None):
        self._driver_model_pending[Constants.MANUALLY_SET] = value != None
        self._driver_model_pending = value

    def set_driver_version(self, value=None):
        self._driver_version[Constants.MANUALLY_SET] = value != None
        self._driver_version = value

    def set_ecc_errors_corrected_all_time_in_cbu(self, value=None):
        self._ecc_errors_corrected_all_time_in_cbu[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_cbu = value

    def set_ecc_errors_corrected_all_time_in_primary_cache(self, value=None):
        self._ecc_errors_corrected_all_time_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_primary_cache = value

    def set_ecc_errors_corrected_all_time_in_register_file(self, value=None):
        self._ecc_errors_corrected_all_time_in_register_file[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_register_file = value

    def set_ecc_errors_corrected_all_time_in_secondary_cache(self, value=None):
        self._ecc_errors_corrected_all_time_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_secondary_cache = value

    def set_ecc_errors_corrected_all_time_in_shared_memory(self, value=None):
        self._ecc_errors_corrected_all_time_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_shared_memory = value

    def set_ecc_errors_corrected_all_time_in_sram(self, value=None):
        self._ecc_errors_corrected_all_time_in_sram[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_sram = value

    def set_ecc_errors_corrected_all_time_in_texture_memory(self, value=None):
        self._ecc_errors_corrected_all_time_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_texture_memory = value

    def set_ecc_errors_corrected_all_time_in_total(self, value=None):
        self._ecc_errors_corrected_all_time_in_total[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_total = value

    def set_ecc_errors_corrected_all_time_in_video_memory(self, value=None):
        self._ecc_errors_corrected_all_time_in_video_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_all_time_in_video_memory = value

    def set_ecc_errors_corrected_since_reboot_in_cbu(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_cbu[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_cbu = value

    def set_ecc_errors_corrected_since_reboot_in_primary_cache(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_register_file(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_register_file[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_register_file = value

    def set_ecc_errors_corrected_since_reboot_in_secondary_cache(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_corrected_since_reboot_in_shared_memory(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_corrected_since_reboot_in_sram(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_sram[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_sram = value

    def set_ecc_errors_corrected_since_reboot_in_texture_memory(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_corrected_since_reboot_in_total(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_total[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_total = value

    def set_ecc_errors_corrected_since_reboot_in_video_memory(self, value=None):
        self._ecc_errors_corrected_since_reboot_in_video_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_corrected_since_reboot_in_video_memory = value

    def set_ecc_errors_uncorrected_all_time_in_cbu(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_cbu[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_cbu = value

    def set_ecc_errors_uncorrected_all_time_in_primary_cache(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_primary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_register_file(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_register_file[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_register_file = value

    def set_ecc_errors_uncorrected_all_time_in_secondary_cache(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_secondary_cache = value

    def set_ecc_errors_uncorrected_all_time_in_shared_memory(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_shared_memory = value

    def set_ecc_errors_uncorrected_all_time_in_sram(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_sram[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_sram = value

    def set_ecc_errors_uncorrected_all_time_in_texture_memory(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_texture_memory = value

    def set_ecc_errors_uncorrected_all_time_in_total(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_total[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_total = value

    def set_ecc_errors_uncorrected_all_time_in_video_memory(self, value=None):
        self._ecc_errors_uncorrected_all_time_in_video_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_all_time_in_video_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_cbu(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_cbu[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_cbu = value

    def set_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_register_file(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_register_file[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_register_file = value

    def set_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache = value

    def set_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_sram(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_sram[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_sram = value

    def set_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory = value

    def set_ecc_errors_uncorrected_since_reboot_in_total(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_total[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_total = value

    def set_ecc_errors_uncorrected_since_reboot_in_video_memory(self, value=None):
        self._ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.MANUALLY_SET] = value != None
        self._ecc_errors_uncorrected_since_reboot_in_video_memory = value

    def set_ecc_mode_current(self, value=None):
        self._ecc_mode_current[Constants.MANUALLY_SET] = value != None
        self._ecc_mode_current = value

    def set_ecc_mode_pending(self, value=None):
        self._ecc_mode_pending[Constants.MANUALLY_SET] = value != None
        self._ecc_mode_pending = value

    def set_encoder_average_FPS(self, value=None):
        self._encoder_average_FPS[Constants.MANUALLY_SET] = value != None
        self._encoder_average_FPS = value

    def set_encoder_average_latency(self, value=None):
        self._encoder_average_latency[Constants.MANUALLY_SET] = value != None
        self._encoder_average_latency = value

    def set_encoder_session_count(self, value=None):
        self._encoder_session_count[Constants.MANUALLY_SET] = value != None
        self._encoder_session_count = value

    def set_engine_clock_range(self, value=None):
        self._engine_clock_range[Constants.MANUALLY_SET] = value != None
        self._engine_clock_range = value

    def set_error_cleared(self, value=None):
        self._error_cleared[Constants.MANUALLY_SET] = value != None
        self._error_cleared = value

    def set_error_description(self, value=None):
        self._error_description[Constants.MANUALLY_SET] = value != None
        self._error_description = value

    def set_fabric_state(self, value=None):
        self._fabric_state[Constants.MANUALLY_SET] = value != None
        self._fabric_state = value

    def set_fabric_status(self, value=None):
        self._fabric_status[Constants.MANUALLY_SET] = value != None
        self._fabric_status = value

    def set_fan_speed_percentage(self, value=None):
        self._fan_speed_percentage[Constants.MANUALLY_SET] = value != None
        self._fan_speed_percentage = value

    def set_fan_speed_percentage_range(self, value=None):
        self._fan_speed_percentage_range[Constants.MANUALLY_SET] = value != None
        self._fan_speed_percentage_range = value

    def set_fan_speed_RPM(self, value=None):
        self._fan_speed_RPM[Constants.MANUALLY_SET] = value != None
        self._fan_speed_RPM = value

    def set_fan_speed_RPM_range(self, value=None):
        self._fan_speed_RPM_range[Constants.MANUALLY_SET] = value != None
        self._fan_speed_RPM_range = value

    def set_fractional_multi_vGPU(self, value=None):
        self._fractional_multi_vGPU[Constants.MANUALLY_SET] = value != None
        self._fractional_multi_vGPU = value

    def set_frequency_application_default_shader_clock(self, value=None):
        self._frequency_application_default_shader_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_application_default_shader_clock = value

    def set_frequency_application_default_memory_clock(self, value=None):
        self._frequency_application_default_memory_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_application_default_memory_clock = value

    def set_frequency_application_memory_clock(self, value=None):
        self._frequency_application_memory_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_application_memory_clock = value

    def set_frequency_application_shader_clock(self, value=None):
        self._frequency_application_shader_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_application_shader_clock = value

    def set_frequency_maximum_memory_clock(self, value=None):
        self._frequency_maximum_memory_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_maximum_memory_clock = value

    def set_frequency_maximum_shader_clock(self, value=None):
        self._frequency_maximum_shader_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_maximum_shader_clock = value

    def set_frequency_maximum_streaming_multiprocessor_clock(self, value=None):
        self._frequency_maximum_streaming_multiprocessor_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_maximum_streaming_multiprocessor_clock = value

    def set_frequency_memory_clock(self, value=None):
        self._frequency_memory_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_memory_clock = value

    def set_frequency_shader_clock(self, value=None):
        self._frequency_shader_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_shader_clock = value

    def set_frequency_streaming_multiprocessor_clock(self, value=None):
        self._frequency_streaming_multiprocessor_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_streaming_multiprocessor_clock = value

    def set_frequency_video_clock(self, value=None):
        self._frequency_video_clock[Constants.MANUALLY_SET] = value != None
        self._frequency_video_clock = value

    def set_heterogenous_multi_vGPU(self, value=None):
        self._heterogenous_multi_vGPU[Constants.MANUALLY_SET] = value != None
        self._heterogenous_multi_vGPU = value

    def set_heterogenous_time_slice_profile(self, value=None):
        self._heterogenous_time_slice_profile[Constants.MANUALLY_SET] = value != None
        self._heterogenous_time_slice_profile = value

    def set_heterogenous_time_slice_sizes(self, value=None):
        self._heterogenous_time_slice_sizes[Constants.MANUALLY_SET] = value != None
        self._heterogenous_time_slice_sizes = value

    def set_ICM_indent(self, value=None):
        self._ICM_indent[Constants.MANUALLY_SET] = value != None
        self._ICM_indent = value

    def set_ICM_method(self, value=None):
        self._ICM_method[Constants.MANUALLY_SET] = value != None
        self._ICM_method = value

    def set_inf_filename(self, value=None):
        self._inf_filename[Constants.MANUALLY_SET] = value != None
        self._inf_filename = value

    def set_inf_section(self, value=None):
        self._inf_section[Constants.MANUALLY_SET] = value != None
        self._inf_section = value

    def set_info_ROM_ecc(self, value=None):
        self._info_ROM_ecc[Constants.MANUALLY_SET] = value != None
        self._info_ROM_ecc = value

    def set_info_ROM_oem(self, value=None):
        self._info_ROM_oem[Constants.MANUALLY_SET] = value != None
        self._info_ROM_oem = value

    def set_info_ROM_power(self, value=None):
        self._info_ROM_power[Constants.MANUALLY_SET] = value != None
        self._info_ROM_power = value

    def set_info_ROM_version(self, value=None):
        self._info_ROM_version[Constants.MANUALLY_SET] = value != None
        self._info_ROM_version = value

    def set_install_date(self, value=None):
        self._install_date[Constants.MANUALLY_SET] = value != None
        self._install_date = value

    def set_installed_display_drivers(self, value=None):
        self._installed_display_drivers[Constants.MANUALLY_SET] = value != None
        self._installed_display_drivers = value

    def set_last_error_code(self, value=None):
        self._last_error_code[Constants.MANUALLY_SET] = value != None
        self._last_error_code = value

    def set_max_memory_supported(self, value=None):
        self._max_memory_supported[Constants.MANUALLY_SET] = value != None
        self._max_memory_supported = value

    def set_max_number_controlled(self, value=None):
        self._max_number_controlled[Constants.MANUALLY_SET] = value != None
        self._max_number_controlled = value

    def set_max_refresh_rate(self, value=None):
        self._max_refresh_rate[Constants.MANUALLY_SET] = value != None
        self._max_refresh_rate = value

    def set_memory_clock_range(self, value=None):
        self._memory_clock_range[Constants.MANUALLY_SET] = value != None
        self._memory_clock_range = value

    def set_memory_free(self, value=None):
        self._memory_free[Constants.MANUALLY_SET] = value != None
        self._memory_free = value

    def set_memory_reserved(self, value=None):
        self._memory_reserved[Constants.MANUALLY_SET] = value != None
        self._memory_reserved = value

    def set_memory_total(self, value=None):
        self._memory_total[Constants.MANUALLY_SET] = value != None
        self._memory_total = value

    def set_memory_used(self, value=None):
        self._memory_used[Constants.MANUALLY_SET] = value != None
        self._memory_used = value

    def set_min_refresh_rate(self, value=None):
        self._min_refresh_rate[Constants.MANUALLY_SET] = value != None
        self._min_refresh_rate = value

    def set_monochrome(self, value=None):
        self._monochrome[Constants.MANUALLY_SET] = value != None
        self._monochrome = value

    def set_multi_instance_GPU_mode_current(self, value=None):
        self._multi_instance_GPU_mode_current[Constants.MANUALLY_SET] = value != None
        self._multi_instance_GPU_mode_current = value

    def set_multi_instance_GPU_mode_pending(self, value=None):
        self._multi_instance_GPU_mode_pending[Constants.MANUALLY_SET] = value != None
        self._multi_instance_GPU_mode_pending = value

    def set_name(self, value=None):
        self._name[Constants.MANUALLY_SET] = value != None
        self._name = value

    def set_number_of_color_planes(self, value=None):
        self._number_of_color_planes[Constants.MANUALLY_SET] = value != None
        self._number_of_color_planes = value

    def set_number_of_video_pages(self, value=None):
        self._number_of_video_pages[Constants.MANUALLY_SET] = value != None
        self._number_of_video_pages = value

    def set_operating_mode_current(self, value=None):
        self._operating_mode_current[Constants.MANUALLY_SET] = value != None
        self._operating_mode_current = value

    def set_operating_mode_pending(self, value=None):
        self._operating_mode_pending[Constants.MANUALLY_SET] = value != None
        self._operating_mode_pending = value

    def set_pci_bus(self, value=None):
        self._pci_bus[Constants.MANUALLY_SET] = value != None
        self._pci_bus = value

    def set_pci_bus_id(self, value=None):
        self._pci_bus_id[Constants.MANUALLY_SET] = value != None
        self._pci_bus_id = value

    def set_pci_device(self, value=None):
        self._pci_device[Constants.MANUALLY_SET] = value != None
        self._pci_device = value

    def set_pci_device_id(self, value=None):
        self._pci_device_id[Constants.MANUALLY_SET] = value != None
        self._pci_device_id = value

    def set_pci_domain(self, value=None):
        self._pci_domain[Constants.MANUALLY_SET] = value != None
        self._pci_domain = value

    def set_pci_link_generation_current(self, value=None):
        self._pci_link_generation_current[Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_current = value

    def set_pci_link_generation_device_host_maximum(self, value=None):
        self._pci_link_generation_device_host_maximum[Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_device_host_maximum = value

    def set_pci_link_generation_gpu_maximum(self, value=None):
        self._pci_link_generation_gpu_maximum[Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_gpu_maximum = value

    def set_pci_link_generation_maximum(self, value=None):
        self._pci_link_generation_maximum[Constants.MANUALLY_SET] = value != None
        self._pci_link_generation_maximum = value

    def set_pci_link_width_current(self, value=None):
        self._pci_link_width_current[Constants.MANUALLY_SET] = value != None
        self._pci_link_width_current = value

    def set_pci_link_width_maximum(self, value=None):
        self._pci_link_width_maximum[Constants.MANUALLY_SET] = value != None
        self._pci_link_width_maximum = value

    def set_pci_sub_device_id(self, value=None):
        self._pci_sub_device_id[Constants.MANUALLY_SET] = value != None
        self._pci_sub_device_id = value

    def set_persistence_mode(self, value=None):
        self._persistence_mode[Constants.MANUALLY_SET] = value != None
        self._persistence_mode = value

    def set_PNP_device_id(self, value=None):
        self._PNP_device_id[Constants.MANUALLY_SET] = value != None
        self._PNP_device_id = value

    def set_power_draw(self, value=None):
        self._power_draw[Constants.MANUALLY_SET] = value != None
        self._power_draw = value

    def set_power_draw_average(self, value=None):
        self._power_draw_average[Constants.MANUALLY_SET] = value != None
        self._power_draw_average = value

    def set_power_draw_default_limit(self, value=None):
        self._power_draw_default_limit[Constants.MANUALLY_SET] = value != None
        self._power_draw_default_limit = value

    def set_power_draw_enforced_limit(self, value=None):
        self._power_draw_enforced_limit[Constants.MANUALLY_SET] = value != None
        self._power_draw_enforced_limit = value

    def set_power_draw_instant(self, value=None):
        self._power_draw_instant[Constants.MANUALLY_SET] = value != None
        self._power_draw_instant = value

    def set_power_draw_limit(self, value=None):
        self._power_draw_limit[Constants.MANUALLY_SET] = value != None
        self._power_draw_limit = value

    def set_power_draw_maximum(self, value=None):
        self._power_draw_maximum[Constants.MANUALLY_SET] = value != None
        self._power_draw_maximum = value

    def set_power_draw_minimum(self, value=None):
        self._power_draw_minimum[Constants.MANUALLY_SET] = value != None
        self._power_draw_minimum = value

    def set_power_management_capabilities(self, value=None):
        self._power_management_capabilities[Constants.MANUALLY_SET] = value != None
        self._power_management_capabilities = value

    def set_power_management_supported(self, value=None):
        self._power_management_supported[Constants.MANUALLY_SET] = value != None
        self._power_management_supported = value

    def set_protected_memory_free(self, value=None):
        self._protected_memory_free[Constants.MANUALLY_SET] = value != None
        self._protected_memory_free = value

    def set_protected_memory_total(self, value=None):
        self._protected_memory_total[Constants.MANUALLY_SET] = value != None
        self._protected_memory_total = value

    def set_protected_memory_used(self, value=None):
        self._protected_memory_used[Constants.MANUALLY_SET] = value != None
        self._protected_memory_used = value

    def set_protocol_supported(self, value=None):
        self._protocol_supported[Constants.MANUALLY_SET] = value != None
        self._protocol_supported = value

    def set_performance_state(self, value=None):
        self._performance_state[Constants.MANUALLY_SET] = value != None
        self._performance_state = value

    def set_retired_pages_double_bit_ecc_errors_count(self, value=None):
        self._retired_pages_double_bit_ecc_errors_count[Constants.MANUALLY_SET] = value != None
        self._retired_pages_double_bit_ecc_errors_count = value

    def set_retired_pages_single_bit_ecc_errors_count(self, value=None):
        self._retired_pages_single_bit_ecc_errors_count[Constants.MANUALLY_SET] = value != None
        self._retired_pages_single_bit_ecc_errors_count = value

    def set_retired_pages_pending(self, value=None):
        self._retired_pages_pending[Constants.MANUALLY_SET] = value != None
        self._retired_pages_pending = value

    def set_reserved_system_palette_entries(self, value=None):
        self._reserved_system_palette_entries[Constants.MANUALLY_SET] = value != None
        self._reserved_system_palette_entries = value

    def set_reset_required(self, value=None):
        self._reset_required[Constants.MANUALLY_SET] = value != None
        self._reset_required = value

    def set_reset_and_drain_recommended(self, value=None):
        self._reset_and_drain_recommended[Constants.MANUALLY_SET] = value != None
        self._reset_and_drain_recommended = value

    def set_serial(self, value=None):
        self._serial[Constants.MANUALLY_SET] = value != None
        self._serial = value

    def set_specification_version(self, value=None):
        self._specification_version[Constants.MANUALLY_SET] = value != None
        self._specification_version = value

    def set_status(self, value=None):
        self._status[Constants.MANUALLY_SET] = value != None
        self._status = value

    def set_status_info(self, value=None):
        self._status_info[Constants.MANUALLY_SET] = value != None
        self._status_info = value

    def set_system_creation_class_name(self, value=None):
        self._system_creation_class_name[Constants.MANUALLY_SET] = value != None
        self._system_creation_class_name = value

    def set_system_name(self, value=None):
        self._system_name[Constants.MANUALLY_SET] = value != None
        self._system_name = value

    def set_system_palette_entries(self, value=None):
        self._system_palette_entries[Constants.MANUALLY_SET] = value != None
        self._system_palette_entries = value

    def set_GPU_system_processor_mode_current(self, value=None):
        self._GPU_system_processor_mode_current[Constants.MANUALLY_SET] = value != None
        self._GPU_system_processor_mode_current = value

    def set_GPU_system_processor_mode_default(self, value=None):
        self._GPU_system_processor_mode_default[Constants.MANUALLY_SET] = value != None
        self._GPU_system_processor_mode_default = value

    def set_temperature_core(self, value=None):
        self._temperature_core[Constants.MANUALLY_SET] = value != None
        self._temperature_core = value

    def set_temperature_core_limit(self, value=None):
        self._temperature_core_limit[Constants.MANUALLY_SET] = value != None
        self._temperature_core_limit = value

    def set_temperature_memory(self, value=None):
        self._temperature_memory[Constants.MANUALLY_SET] = value != None
        self._temperature_memory = value

    def set_time_of_last_reset(self, value=None):
        self._time_of_last_reset[Constants.MANUALLY_SET] = value != None
        self._time_of_last_reset = value

    def set_utilization_decoder(self, value=None):
        self._utilization_decoder[Constants.MANUALLY_SET] = value != None
        self._utilization_decoder = value

    def set_utilization_encoder(self, value=None):
        self._utilization_encoder[Constants.MANUALLY_SET] = value != None
        self._utilization_encoder = value

    def set_utilization_gpu(self, value=None):
        self._utilization_gpu[Constants.MANUALLY_SET] = value != None
        self._utilization_gpu = value

    def set_utilization_jpeg(self, value=None):
        self._utilization_jpeg[Constants.MANUALLY_SET] = value != None
        self._utilization_jpeg = value

    def set_utilization_memory(self, value=None):
        self._utilization_memory[Constants.MANUALLY_SET] = value != None
        self._utilization_memory = value

    def set_utilization_optical_flow(self, value=None):
        self._utilization_optical_flow[Constants.MANUALLY_SET] = value != None
        self._utilization_optical_flow = value

    def set_uuid(self, value=None):
        self._uuid[Constants.MANUALLY_SET] = value != None
        self._uuid = value

    def set_vbios_version(self, value=None):
        self._vbios_version[Constants.MANUALLY_SET] = value != None
        self._vbios_version = value

    def set_video_architecture(self, value=None):
        self._video_architecture[Constants.MANUALLY_SET] = value != None
        self._video_architecture = value

    def set_video_memory_type(self, value=None):
        self._video_memory_type[Constants.MANUALLY_SET] = value != None
        self._video_memory_type = value

    def set_video_mode(self, value=None):
        self._video_mode[Constants.MANUALLY_SET] = value != None
        self._video_mode = value

    def set_video_mode_description(self, value=None):
        self._video_mode_description[Constants.MANUALLY_SET] = value != None
        self._video_mode_description = value

    def set_video_processor(self, value=None):
        self._video_processor[Constants.MANUALLY_SET] = value != None
        self._video_processor = value

    def update_accelerator_capabilities(self, wait_for_completion=True):
        self._accelerator_capabilities[Constants.UPDATING] = True
        self.update(data_points=["accelerator_capabilities"], wait_for_completion=wait_for_completion)

    def update_accounting_mode_enabled(self, wait_for_completion=True):
        self._accounting_mode_enabled[Constants.UPDATING] = True
        self.update(data_points=["accounting_mode_enabled"], wait_for_completion=wait_for_completion)

    def update_accounting_mode_buffer_size(self, wait_for_completion=True):
        self._accounting_mode_buffer_size[Constants.UPDATING] = True
        self.update(data_points=["accounting_mode_buffer_size"], wait_for_completion=wait_for_completion)

    def update_adapter_compatibility(self, wait_for_completion=True):
        self._adapter_compatibility[Constants.UPDATING] = True
        self.update(data_points=["adapter_compatibility"], wait_for_completion=wait_for_completion)

    def update_adapter_DAC_type(self, wait_for_completion=True):
        self._adapter_DAC_type[Constants.UPDATING] = True
        self.update(data_points=["adapter_DAC_type"], wait_for_completion=wait_for_completion)

    def update_adapter_id(self, wait_for_completion=True):
        self._adapter_id[Constants.UPDATING] = True
        self.update(data_points=["adapter_id"], wait_for_completion=wait_for_completion)

    def update_adapter_index(self, wait_for_completion=True):
        self._adapter_index[Constants.UPDATING] = True
        self.update(data_points=["adapter_index"], wait_for_completion=wait_for_completion)

    def update_addressing_mode(self, wait_for_completion=True):
        self._addressing_mode[Constants.UPDATING] = True
        self.update(data_points=["addressing_mode"], wait_for_completion=wait_for_completion)

    def update_availability(self, wait_for_completion=True):
        self._availability[Constants.UPDATING] = True
        self.update(data_points=["availability"], wait_for_completion=wait_for_completion)

    def update_capability_descriptions(self, wait_for_completion=True):
        self._capability_descriptions[Constants.UPDATING] = True
        self.update(data_points=["capability_descriptions"], wait_for_completion=wait_for_completion)

    def update_caption(self, wait_for_completion=True):
        self._caption[Constants.UPDATING] = True
        self.update(data_points=["caption"], wait_for_completion=wait_for_completion)

    def update_chip_to_chip_interconnect_mode(self, wait_for_completion=True):
        self._chip_to_chip_interconnect_mode[Constants.UPDATING] = True
        self.update(data_points=["chip_to_chip_interconnect_mode"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_as_bitmap(self, wait_for_completion=True):
        self._clock_event_reasons_as_bitmap[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_as_bitmap"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_application_setting(self, wait_for_completion=True):
        self._clock_event_reasons_application_setting[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_application_setting"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_is_hardware_limited(self, wait_for_completion=True):
        self._clock_event_reasons_is_hardware_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_is_hardware_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_gpu_idle_limited(self, wait_for_completion=True):
        self._clock_event_reasons_gpu_idle_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_gpu_idle_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_software_power_limited(self, wait_for_completion=True):
        self._clock_event_reasons_software_power_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_software_power_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_software_thermal_limited(self, wait_for_completion=True):
        self._clock_event_reasons_software_thermal_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_software_thermal_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_power_break_slowdown_limited(self, wait_for_completion=True):
        self._clock_event_reasons_power_break_slowdown_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_power_break_slowdown_limited"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_supported(self, wait_for_completion=True):
        self._clock_event_reasons_supported[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_supported"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_sync_boost(self, wait_for_completion=True):
        self._clock_event_reasons_sync_boost[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_sync_boost"], wait_for_completion=wait_for_completion)

    def update_clock_event_reasons_thermal_limited(self, wait_for_completion=True):
        self._clock_event_reasons_thermal_limited[Constants.UPDATING] = True
        self.update(data_points=["clock_event_reasons_thermal_limited"], wait_for_completion=wait_for_completion)

    def update_color_table_entries(self, wait_for_completion=True):
        self._color_table_entries[Constants.UPDATING] = True
        self.update(data_points=["color_table_entries"], wait_for_completion=wait_for_completion)

    def update_compute_cap(self, wait_for_completion=True):
        self._compute_cap[Constants.UPDATING] = True
        self.update(data_points=["compute_cap"], wait_for_completion=wait_for_completion)

    def update_compute_mode(self, wait_for_completion=True):
        self._compute_mode[Constants.UPDATING] = True
        self.update(data_points=["compute_mode"], wait_for_completion=wait_for_completion)

    def update_config_manager_error_code(self, wait_for_completion=True):
        self._config_manager_error_code[Constants.UPDATING] = True
        self.update(data_points=["config_manager_error_code"], wait_for_completion=wait_for_completion)

    def update_config_manager_user_config(self, wait_for_completion=True):
        self._config_manager_user_config[Constants.UPDATING] = True
        self.update(data_points=["config_manager_user_config"], wait_for_completion=wait_for_completion)

    def update_core_voltage(self, wait_for_completion=True):
        self._core_voltage[Constants.UPDATING] = True
        self.update(data_points=["core_voltage"], wait_for_completion=wait_for_completion)

    def update_core_voltage_range(self, wait_for_completion=True):
        self._core_voltage_range[Constants.UPDATING] = True
        self.update(data_points=["core_voltage_range"], wait_for_completion=wait_for_completion)

    def update_creation_class_name(self, wait_for_completion=True):
        self._creation_class_name[Constants.UPDATING] = True
        self.update(data_points=["creation_class_name"], wait_for_completion=wait_for_completion)

    def update_current_bits_per_pixel(self, wait_for_completion=True):
        self._current_bits_per_pixel[Constants.UPDATING] = True
        self.update(data_points=["current_bits_per_pixel"], wait_for_completion=wait_for_completion)

    def update_current_horizontal_resolution(self, wait_for_completion=True):
        self._current_horizontal_resolution[Constants.UPDATING] = True
        self.update(data_points=["current_horizontal_resolution"], wait_for_completion=wait_for_completion)

    def update_current_number_of_colors(self, wait_for_completion=True):
        self._current_number_of_colors[Constants.UPDATING] = True
        self.update(data_points=["current_number_of_colors"], wait_for_completion=wait_for_completion)

    def update_current_number_of_columns(self, wait_for_completion=True):
        self._current_number_of_columns[Constants.UPDATING] = True
        self.update(data_points=["current_number_of_columns"], wait_for_completion=wait_for_completion)

    def update_current_number_of_rows(self, wait_for_completion=True):
        self._current_number_of_rows[Constants.UPDATING] = True
        self.update(data_points=["current_number_of_rows"], wait_for_completion=wait_for_completion)

    def update_current_refresh_rate(self, wait_for_completion=True):
        self._current_refresh_rate[Constants.UPDATING] = True
        self.update(data_points=["current_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_current_scan_mode(self, wait_for_completion=True):
        self._current_scan_mode[Constants.UPDATING] = True
        self.update(data_points=["current_scan_mode"], wait_for_completion=wait_for_completion)

    def update_current_vertical_resolution(self, wait_for_completion=True):
        self._current_vertical_resolution[Constants.UPDATING] = True
        self.update(data_points=["current_vertical_resolution"], wait_for_completion=wait_for_completion)

    def update_description(self, wait_for_completion=True):
        self._description[Constants.UPDATING] = True
        self.update(data_points=["description"], wait_for_completion=wait_for_completion)

    def update_device_id(self, wait_for_completion=True):
        self._device_id[Constants.UPDATING] = True
        self.update(data_points=["device_id"], wait_for_completion=wait_for_completion)

    def update_device_specific_pens(self, wait_for_completion=True):
        self._device_specific_pens[Constants.UPDATING] = True
        self.update(data_points=["device_specific_pens"], wait_for_completion=wait_for_completion)

    def update_display_active(self, wait_for_completion=True):
        self._display_active[Constants.UPDATING] = True
        self.update(data_points=["display_active"], wait_for_completion=wait_for_completion)

    def update_display_mode(self, wait_for_completion=True):
        self._display_mode[Constants.UPDATING] = True
        self.update(data_points=["display_mode"], wait_for_completion=wait_for_completion)

    def update_dither_type(self, wait_for_completion=True):
        self._dither_type[Constants.UPDATING] = True
        self.update(data_points=["dither_type"], wait_for_completion=wait_for_completion)

    def update_driver_date(self, wait_for_completion=True):
        self._driver_date[Constants.UPDATING] = True
        self.update(data_points=["driver_date"], wait_for_completion=wait_for_completion)

    def update_driver_model_current(self, wait_for_completion=True):
        self._driver_model_current[Constants.UPDATING] = True
        self.update(data_points=["driver_model_current"], wait_for_completion=wait_for_completion)

    def update_driver_model_pending(self, wait_for_completion=True):
        self._driver_model_pending[Constants.UPDATING] = True
        self.update(data_points=["driver_model_pending"], wait_for_completion=wait_for_completion)

    def update_driver_version(self, wait_for_completion=True):
        self._driver_version[Constants.UPDATING] = True
        self.update(data_points=["driver_version"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_cbu(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_primary_cache(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_register_file(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_secondary_cache(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_shared_memory(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_sram(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_texture_memory(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_total(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_all_time_in_video_memory(self, wait_for_completion=True):
        self._ecc_errors_corrected_all_time_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_cbu(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_primary_cache(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_register_file(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_secondary_cache(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_shared_memory(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_sram(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_texture_memory(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_total(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_corrected_since_reboot_in_video_memory(self, wait_for_completion=True):
        self._ecc_errors_corrected_since_reboot_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_corrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_cbu(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_primary_cache(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_register_file(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_secondary_cache(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_shared_memory(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_sram(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_texture_memory(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_total(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_all_time_in_video_memory(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_all_time_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_all_time_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_cbu(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_cbu[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_cbu"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_primary_cache(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_primary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_primary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_register_file(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_register_file[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_register_file"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_secondary_cache(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_secondary_cache[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_secondary_cache"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_shared_memory(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_shared_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_shared_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_sram(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_sram[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_sram"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_texture_memory(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_texture_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_texture_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_total(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_total[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_total"], wait_for_completion=wait_for_completion)

    def update_ecc_errors_uncorrected_since_reboot_in_video_memory(self, wait_for_completion=True):
        self._ecc_errors_uncorrected_since_reboot_in_video_memory[Constants.UPDATING] = True
        self.update(data_points=["ecc_errors_uncorrected_since_reboot_in_video_memory"], wait_for_completion=wait_for_completion)

    def update_ecc_mode_current(self, wait_for_completion=True):
        self._ecc_mode_current[Constants.UPDATING] = True
        self.update(data_points=["ecc_mode_current"], wait_for_completion=wait_for_completion)

    def update_ecc_mode_pending(self, wait_for_completion=True):
        self._ecc_mode_pending[Constants.UPDATING] = True
        self.update(data_points=["ecc_mode_pending"], wait_for_completion=wait_for_completion)

    def update_encoder_average_FPS(self, wait_for_completion=True):
        self._encoder_average_FPS[Constants.UPDATING] = True
        self.update(data_points=["encoder_average_FPS"], wait_for_completion=wait_for_completion)

    def update_encoder_average_latency(self, wait_for_completion=True):
        self._encoder_average_latency[Constants.UPDATING] = True
        self.update(data_points=["encoder_average_latency"], wait_for_completion=wait_for_completion)

    def update_encoder_session_count(self, wait_for_completion=True):
        self._encoder_session_count[Constants.UPDATING] = True
        self.update(data_points=["encoder_session_count"], wait_for_completion=wait_for_completion)

    def update_engine_clock_range(self, wait_for_completion=True):
        self._engine_clock_range[Constants.UPDATING] = True
        self.update(data_points=["engine_clock_range"], wait_for_completion=wait_for_completion)

    def update_error_cleared(self, wait_for_completion=True):
        self._error_cleared[Constants.UPDATING] = True
        self.update(data_points=["error_cleared"], wait_for_completion=wait_for_completion)

    def update_error_description(self, wait_for_completion=True):
        self._error_description[Constants.UPDATING] = True
        self.update(data_points=["error_description"], wait_for_completion=wait_for_completion)

    def update_fabric_state(self, wait_for_completion=True):
        self._fabric_state[Constants.UPDATING] = True
        self.update(data_points=["fabric_state"], wait_for_completion=wait_for_completion)

    def update_fabric_status(self, wait_for_completion=True):
        self._fabric_status[Constants.UPDATING] = True
        self.update(data_points=["fabric_status"], wait_for_completion=wait_for_completion)

    def update_fan_speed_percentage(self, wait_for_completion=True):
        self._fan_speed_percentage[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_percentage"], wait_for_completion=wait_for_completion)

    def update_fan_speed_percentage_range(self, wait_for_completion=True):
        self._fan_speed_percentage_range[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_percentage_range"], wait_for_completion=wait_for_completion)

    def update_fan_speed_RPM(self, wait_for_completion=True):
        self._fan_speed_RPM[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_RPM"], wait_for_completion=wait_for_completion)

    def update_fan_speed_RPM_range(self, wait_for_completion=True):
        self._fan_speed_RPM_range[Constants.UPDATING] = True
        self.update(data_points=["fan_speed_RPM_range"], wait_for_completion=wait_for_completion)

    def update_fractional_multi_vGPU(self, wait_for_completion=True):
        self._fractional_multi_vGPU[Constants.UPDATING] = True
        self.update(data_points=["fractional_multi_vGPU"], wait_for_completion=wait_for_completion)

    def update_frequency_application_default_shader_clock(self, wait_for_completion=True):
        self._frequency_application_default_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_default_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_default_memory_clock(self, wait_for_completion=True):
        self._frequency_application_default_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_default_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_memory_clock(self, wait_for_completion=True):
        self._frequency_application_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_application_shader_clock(self, wait_for_completion=True):
        self._frequency_application_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_application_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_memory_clock(self, wait_for_completion=True):
        self._frequency_maximum_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_shader_clock(self, wait_for_completion=True):
        self._frequency_maximum_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_maximum_streaming_multiprocessor_clock(self, wait_for_completion=True):
        self._frequency_maximum_streaming_multiprocessor_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_maximum_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_memory_clock(self, wait_for_completion=True):
        self._frequency_memory_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_memory_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_shader_clock(self, wait_for_completion=True):
        self._frequency_shader_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_shader_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_streaming_multiprocessor_clock(self, wait_for_completion=True):
        self._frequency_streaming_multiprocessor_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_streaming_multiprocessor_clock"], wait_for_completion=wait_for_completion)

    def update_frequency_video_clock(self, wait_for_completion=True):
        self._frequency_video_clock[Constants.UPDATING] = True
        self.update(data_points=["frequency_video_clock"], wait_for_completion=wait_for_completion)

    def update_heterogenous_multi_vGPU(self, wait_for_completion=True):
        self._heterogenous_multi_vGPU[Constants.UPDATING] = True
        self.update(data_points=["heterogenous_multi_vGPU"], wait_for_completion=wait_for_completion)

    def update_heterogenous_time_slice_profile(self, wait_for_completion=True):
        self._heterogenous_time_slice_profile[Constants.UPDATING] = True
        self.update(data_points=["heterogenous_time_slice_profile"], wait_for_completion=wait_for_completion)

    def update_heterogenous_time_slice_sizes(self, wait_for_completion=True):
        self._heterogenous_time_slice_sizes[Constants.UPDATING] = True
        self.update(data_points=["heterogenous_time_slice_sizes"], wait_for_completion=wait_for_completion)

    def update_ICM_indent(self, wait_for_completion=True):
        self._ICM_indent[Constants.UPDATING] = True
        self.update(data_points=["ICM_indent"], wait_for_completion=wait_for_completion)

    def update_ICM_method(self, wait_for_completion=True):
        self._ICM_method[Constants.UPDATING] = True
        self.update(data_points=["ICM_method"], wait_for_completion=wait_for_completion)

    def update_inf_filename(self, wait_for_completion=True):
        self._inf_filename[Constants.UPDATING] = True
        self.update(data_points=["inf_filename"], wait_for_completion=wait_for_completion)

    def update_inf_section(self, wait_for_completion=True):
        self._inf_section[Constants.UPDATING] = True
        self.update(data_points=["inf_section"], wait_for_completion=wait_for_completion)

    def update_info_ROM_ecc(self, wait_for_completion=True):
        self._info_ROM_ecc[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_ecc"], wait_for_completion=wait_for_completion)

    def update_info_ROM_oem(self, wait_for_completion=True):
        self._info_ROM_oem[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_oem"], wait_for_completion=wait_for_completion)

    def update_info_ROM_power(self, wait_for_completion=True):
        self._info_ROM_power[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_power"], wait_for_completion=wait_for_completion)

    def update_info_ROM_version(self, wait_for_completion=True):
        self._info_ROM_version[Constants.UPDATING] = True
        self.update(data_points=["info_ROM_version"], wait_for_completion=wait_for_completion)

    def update_install_date(self, wait_for_completion=True):
        self._install_date[Constants.UPDATING] = True
        self.update(data_points=["install_date"], wait_for_completion=wait_for_completion)

    def update_installed_display_drivers(self, wait_for_completion=True):
        self._installed_display_drivers[Constants.UPDATING] = True
        self.update(data_points=["installed_display_drivers"], wait_for_completion=wait_for_completion)

    def update_last_error_code(self, wait_for_completion=True):
        self._last_error_code[Constants.UPDATING] = True
        self.update(data_points=["last_error_code"], wait_for_completion=wait_for_completion)

    def update_max_memory_supported(self, wait_for_completion=True):
        self._max_memory_supported[Constants.UPDATING] = True
        self.update(data_points=["max_memory_supported"], wait_for_completion=wait_for_completion)

    def update_max_number_controlled(self, wait_for_completion=True):
        self._max_number_controlled[Constants.UPDATING] = True
        self.update(data_points=["max_number_controlled"], wait_for_completion=wait_for_completion)

    def update_max_refresh_rate(self, wait_for_completion=True):
        self._max_refresh_rate[Constants.UPDATING] = True
        self.update(data_points=["max_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_memory_clock_range(self, wait_for_completion=True):
        self._memory_clock_range[Constants.UPDATING] = True
        self.update(data_points=["memory_clock_range"], wait_for_completion=wait_for_completion)

    def update_memory_free(self, wait_for_completion=True):
        self._memory_free[Constants.UPDATING] = True
        self.update(data_points=["memory_free"], wait_for_completion=wait_for_completion)

    def update_memory_reserved(self, wait_for_completion=True):
        self._memory_reserved[Constants.UPDATING] = True
        self.update(data_points=["memory_reserved"], wait_for_completion=wait_for_completion)

    def update_memory_total(self, wait_for_completion=True):
        self._memory_total[Constants.UPDATING] = True
        self.update(data_points=["memory_total"], wait_for_completion=wait_for_completion)

    def update_memory_used(self, wait_for_completion=True):
        self._memory_used[Constants.UPDATING] = True
        self.update(data_points=["memory_used"], wait_for_completion=wait_for_completion)

    def update_min_refresh_rate(self, wait_for_completion=True):
        self._min_refresh_rate[Constants.UPDATING] = True
        self.update(data_points=["min_refresh_rate"], wait_for_completion=wait_for_completion)

    def update_monochrome(self, wait_for_completion=True):
        self._monochrome[Constants.UPDATING] = True
        self.update(data_points=["monochrome"], wait_for_completion=wait_for_completion)

    def update_multi_instance_GPU_mode_current(self, wait_for_completion=True):
        self._multi_instance_GPU_mode_current[Constants.UPDATING] = True
        self.update(data_points=["multi_instance_GPU_mode_current"], wait_for_completion=wait_for_completion)

    def update_multi_instance_GPU_mode_pending(self, wait_for_completion=True):
        self._multi_instance_GPU_mode_pending[Constants.UPDATING] = True
        self.update(data_points=["multi_instance_GPU_mode_pending"], wait_for_completion=wait_for_completion)

    def update_name(self, wait_for_completion=True):
        self._name[Constants.UPDATING] = True
        self.update(data_points=["name"], wait_for_completion=wait_for_completion)

    def update_number_of_color_planes(self, wait_for_completion=True):
        self._number_of_color_planes[Constants.UPDATING] = True
        self.update(data_points=["number_of_color_planes"], wait_for_completion=wait_for_completion)

    def update_number_of_video_pages(self, wait_for_completion=True):
        self._number_of_video_pages[Constants.UPDATING] = True
        self.update(data_points=["number_of_video_pages"], wait_for_completion=wait_for_completion)

    def update_operating_mode_current(self, wait_for_completion=True):
        self._operating_mode_current[Constants.UPDATING] = True
        self.update(data_points=["operating_mode_current"], wait_for_completion=wait_for_completion)

    def update_operating_mode_pending(self, wait_for_completion=True):
        self._operating_mode_pending[Constants.UPDATING] = True
        self.update(data_points=["operating_mode_pending"], wait_for_completion=wait_for_completion)

    def update_pci_bus(self, wait_for_completion=True):
        self._pci_bus[Constants.UPDATING] = True
        self.update(data_points=["pci_bus"], wait_for_completion=wait_for_completion)

    def update_pci_bus_id(self, wait_for_completion=True):
        self._pci_bus_id[Constants.UPDATING] = True
        self.update(data_points=["pci_bus_id"], wait_for_completion=wait_for_completion)

    def update_pci_device(self, wait_for_completion=True):
        self._pci_device[Constants.UPDATING] = True
        self.update(data_points=["pci_device"], wait_for_completion=wait_for_completion)

    def update_pci_device_id(self, wait_for_completion=True):
        self._pci_device_id[Constants.UPDATING] = True
        self.update(data_points=["pci_device_id"], wait_for_completion=wait_for_completion)

    def update_pci_domain(self, wait_for_completion=True):
        self._pci_domain[Constants.UPDATING] = True
        self.update(data_points=["pci_domain"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_current(self, wait_for_completion=True):
        self._pci_link_generation_current[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_current"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_device_host_maximum(self, wait_for_completion=True):
        self._pci_link_generation_device_host_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_device_host_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_gpu_maximum(self, wait_for_completion=True):
        self._pci_link_generation_gpu_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_gpu_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_generation_maximum(self, wait_for_completion=True):
        self._pci_link_generation_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_generation_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_link_width_current(self, wait_for_completion=True):
        self._pci_link_width_current[Constants.UPDATING] = True
        self.update(data_points=["pci_link_width_current"], wait_for_completion=wait_for_completion)

    def update_pci_link_width_maximum(self, wait_for_completion=True):
        self._pci_link_width_maximum[Constants.UPDATING] = True
        self.update(data_points=["pci_link_width_maximum"], wait_for_completion=wait_for_completion)

    def update_pci_sub_device_id(self, wait_for_completion=True):
        self._pci_sub_device_id[Constants.UPDATING] = True
        self.update(data_points=["pci_sub_device_id"], wait_for_completion=wait_for_completion)

    def update_persistence_mode(self, wait_for_completion=True):
        self._persistence_mode[Constants.UPDATING] = True
        self.update(data_points=["persistence_mode"], wait_for_completion=wait_for_completion)

    def update_PNP_device_id(self, wait_for_completion=True):
        self._PNP_device_id[Constants.UPDATING] = True
        self.update(data_points=["PNP_device_id"], wait_for_completion=wait_for_completion)

    def update_power_draw(self, wait_for_completion=True):
        self._power_draw[Constants.UPDATING] = True
        self.update(data_points=["power_draw"], wait_for_completion=wait_for_completion)

    def update_power_draw_average(self, wait_for_completion=True):
        self._power_draw_average[Constants.UPDATING] = True
        self.update(data_points=["power_draw_average"], wait_for_completion=wait_for_completion)

    def update_power_draw_default_limit(self, wait_for_completion=True):
        self._power_draw_default_limit[Constants.UPDATING] = True
        self.update(data_points=["power_draw_default_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_enforced_limit(self, wait_for_completion=True):
        self._power_draw_enforced_limit[Constants.UPDATING] = True
        self.update(data_points=["power_draw_enforced_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_instant(self, wait_for_completion=True):
        self._power_draw_instant[Constants.UPDATING] = True
        self.update(data_points=["power_draw_instant"], wait_for_completion=wait_for_completion)

    def update_power_draw_limit(self, wait_for_completion=True):
        self._power_draw_limit[Constants.UPDATING] = True
        self.update(data_points=["power_draw_limit"], wait_for_completion=wait_for_completion)

    def update_power_draw_maximum(self, wait_for_completion=True):
        self._power_draw_maximum[Constants.UPDATING] = True
        self.update(data_points=["power_draw_maximum"], wait_for_completion=wait_for_completion)

    def update_power_draw_minimum(self, wait_for_completion=True):
        self._power_draw_minimum[Constants.UPDATING] = True
        self.update(data_points=["power_draw_minimum"], wait_for_completion=wait_for_completion)

    def update_power_management_capabilities(self, wait_for_completion=True):
        self._power_management_capabilities[Constants.UPDATING] = True
        self.update(data_points=["power_management_capabilities"], wait_for_completion=wait_for_completion)

    def update_power_management_supported(self, wait_for_completion=True):
        self._power_management_supported[Constants.UPDATING] = True
        self.update(data_points=["power_management_supported"], wait_for_completion=wait_for_completion)

    def update_protected_memory_free(self, wait_for_completion=True):
        self._protected_memory_free[Constants.UPDATING] = True
        self.update(data_points=["protected_memory_free"], wait_for_completion=wait_for_completion)

    def update_protected_memory_total(self, wait_for_completion=True):
        self._protected_memory_total[Constants.UPDATING] = True
        self.update(data_points=["protected_memory_total"], wait_for_completion=wait_for_completion)

    def update_protected_memory_used(self, wait_for_completion=True):
        self._protected_memory_used[Constants.UPDATING] = True
        self.update(data_points=["protected_memory_used"], wait_for_completion=wait_for_completion)

    def update_protocol_supported(self, wait_for_completion=True):
        self._protocol_supported[Constants.UPDATING] = True
        self.update(data_points=["protocol_supported"], wait_for_completion=wait_for_completion)

    def update_performance_state(self, wait_for_completion=True):
        self._performance_state[Constants.UPDATING] = True
        self.update(data_points=["performance_state"], wait_for_completion=wait_for_completion)

    def update_retired_pages_double_bit_ecc_errors_count(self, wait_for_completion=True):
        self._retired_pages_double_bit_ecc_errors_count[Constants.UPDATING] = True
        self.update(data_points=["retired_pages_double_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)

    def update_retired_pages_single_bit_ecc_errors_count(self, wait_for_completion=True):
        self._retired_pages_single_bit_ecc_errors_count[Constants.UPDATING] = True
        self.update(data_points=["retired_pages_single_bit_ecc_errors_count"], wait_for_completion=wait_for_completion)

    def update_retired_pages_pending(self, wait_for_completion=True):
        self._retired_pages_pending[Constants.UPDATING] = True
        self.update(data_points=["retired_pages_pending"], wait_for_completion=wait_for_completion)

    def update_reserved_system_palette_entries(self, wait_for_completion=True):
        self._reserved_system_palette_entries[Constants.UPDATING] = True
        self.update(data_points=["reserved_system_palette_entries"], wait_for_completion=wait_for_completion)

    def update_reset_required(self, wait_for_completion=True):
        self._reset_required[Constants.UPDATING] = True
        self.update(data_points=["reset_required"], wait_for_completion=wait_for_completion)

    def update_reset_and_drain_recommended(self, wait_for_completion=True):
        self._reset_and_drain_recommended[Constants.UPDATING] = True
        self.update(data_points=["reset_and_drain_recommended"], wait_for_completion=wait_for_completion)

    def update_serial(self, wait_for_completion=True):
        self._serial[Constants.UPDATING] = True
        self.update(data_points=["serial"], wait_for_completion=wait_for_completion)

    def update_specification_version(self, wait_for_completion=True):
        self._specification_version[Constants.UPDATING] = True
        self.update(data_points=["specification_version"], wait_for_completion=wait_for_completion)

    def update_status(self, wait_for_completion=True):
        self._status[Constants.UPDATING] = True
        self.update(data_points=["status"], wait_for_completion=wait_for_completion)

    def update_status_info(self, wait_for_completion=True):
        self._status_info[Constants.UPDATING] = True
        self.update(data_points=["status_info"], wait_for_completion=wait_for_completion)

    def update_system_creation_class_name(self, wait_for_completion=True):
        self._system_creation_class_name[Constants.UPDATING] = True
        self.update(data_points=["system_creation_class_name"], wait_for_completion=wait_for_completion)

    def update_system_name(self, wait_for_completion=True):
        self._system_name[Constants.UPDATING] = True
        self.update(data_points=["system_name"], wait_for_completion=wait_for_completion)

    def update_system_palette_entries(self, wait_for_completion=True):
        self._system_palette_entries[Constants.UPDATING] = True
        self.update(data_points=["system_palette_entries"], wait_for_completion=wait_for_completion)

    def update_GPU_system_processor_mode_current(self, wait_for_completion=True):
        self._GPU_system_processor_mode_current[Constants.UPDATING] = True
        self.update(data_points=["GPU_system_processor_mode_current"], wait_for_completion=wait_for_completion)

    def update_GPU_system_processor_mode_default(self, wait_for_completion=True):
        self._GPU_system_processor_mode_default[Constants.UPDATING] = True
        self.update(data_points=["GPU_system_processor_mode_default"], wait_for_completion=wait_for_completion)

    def update_temperature_core(self, wait_for_completion=True):
        self._temperature_core[Constants.UPDATING] = True
        self.update(data_points=["temperature_core"], wait_for_completion=wait_for_completion)

    def update_temperature_core_limit(self, wait_for_completion=True):
        self._temperature_core_limit[Constants.UPDATING] = True
        self.update(data_points=["temperature_core_limit"], wait_for_completion=wait_for_completion)

    def update_temperature_memory(self, wait_for_completion=True):
        self._temperature_memory[Constants.UPDATING] = True
        self.update(data_points=["temperature_memory"], wait_for_completion=wait_for_completion)

    def update_time_of_last_reset(self, wait_for_completion=True):
        self._time_of_last_reset[Constants.UPDATING] = True
        self.update(data_points=["time_of_last_reset"], wait_for_completion=wait_for_completion)

    def update_utilization_decoder(self, wait_for_completion=True):
        self._utilization_decoder[Constants.UPDATING] = True
        self.update(data_points=["utilization_decoder"], wait_for_completion=wait_for_completion)

    def update_utilization_encoder(self, wait_for_completion=True):
        self._utilization_encoder[Constants.UPDATING] = True
        self.update(data_points=["utilization_encoder"], wait_for_completion=wait_for_completion)

    def update_utilization_gpu(self, wait_for_completion=True):
        self._utilization_gpu[Constants.UPDATING] = True
        self.update(data_points=["utilization_gpu"], wait_for_completion=wait_for_completion)

    def update_utilization_jpeg(self, wait_for_completion=True):
        self._utilization_jpeg[Constants.UPDATING] = True
        self.update(data_points=["utilization_jpeg"], wait_for_completion=wait_for_completion)

    def update_utilization_memory(self, wait_for_completion=True):
        self._utilization_memory[Constants.UPDATING] = True
        self.update(data_points=["utilization_memory"], wait_for_completion=wait_for_completion)

    def update_utilization_optical_flow(self, wait_for_completion=True):
        self._utilization_optical_flow[Constants.UPDATING] = True
        self.update(data_points=["utilization_optical_flow"], wait_for_completion=wait_for_completion)

    def update_uuid(self, wait_for_completion=True):
        self._uuid[Constants.UPDATING] = True
        self.update(data_points=["uuid"], wait_for_completion=wait_for_completion)

    def update_vbios_version(self, wait_for_completion=True):
        self._vbios_version[Constants.UPDATING] = True
        self.update(data_points=["vbios_version"], wait_for_completion=wait_for_completion)

    def update_video_architecture(self, wait_for_completion=True):
        self._video_architecture[Constants.UPDATING] = True
        self.update(data_points=["video_architecture"], wait_for_completion=wait_for_completion)

    def update_video_memory_type(self, wait_for_completion=True):
        self._video_memory_type[Constants.UPDATING] = True
        self.update(data_points=["video_memory_type"], wait_for_completion=wait_for_completion)

    def update_video_mode(self, wait_for_completion=True):
        self._video_mode[Constants.UPDATING] = True
        self.update(data_points=["video_mode"], wait_for_completion=wait_for_completion)

    def update_video_mode_description(self, wait_for_completion=True):
        self._video_mode_description[Constants.UPDATING] = True
        self.update(data_points=["video_mode_description"], wait_for_completion=wait_for_completion)

    def update_video_processor(self, wait_for_completion=True):
        self._video_processor[Constants.UPDATING] = True
        self.update(data_points=["video_processor"], wait_for_completion=wait_for_completion)