from moderngl import Context as _moderngl__Context
from pprofile import Profile as _pprofile__Profile

class Registry:
    """
    🟩 **R** -
    """
    compile_math_functions = True
    running = True
    temporary_files_path = None
    base_path = None
    custom_compiled_behavior = {}
    cython_acceleration_available = False
    cython_acceleration_enabled = False
    pmma_module_spine = {}
    do_anti_aliasing = False
    anti_aliasing_level = 0
    manually_set_anti_aliasing_level = None
    manually_set_do_anti_aliasing = None
    development_mode = True
    refresh_rate = 60
    display_initialized = False
    context: "_moderngl__Context" = None
    power_saving_mode = False
    pmma_initialized = False
    pygame_launch_message = ""
    in_game_loop = False
    application_start_time = None
    application_finished_loading_time = None
    perlin_noise_prefill_single_samples = 0
    perlin_noise_prefill_array_samples = 0
    window_context = None
    number_of_instantiated_objects = 0
    iteration_id = None
    language = None
    opengl_objects = {}
    handled_events = False
    compute_component_called = False
    displayed_pygame_start_message = False
    shape_quality = 0.27341772151898736 # 0.75
    initial_shape_quality = None
    profiler: "_pprofile__Profile" = None
    general_profile_application = None
    targeted_profile_application = None
    profile_result_path = None
    logging_path = None
    internal_log_duration = 1
    external_log_duration = 1
    power_status_checked_time = None
    clean_profile = True
    version = "4.2.0"
    last_checked_for_updates = None
    update_available = None
    shape_count = 0
    application_average_frame_rate = {"Samples": 0, "Mean": 0}
    pmma_identifier = 0
    render_pipeline_acceleration_available = False