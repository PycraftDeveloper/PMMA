import moderngl as _moderngl

class Registry:
    compile_math_functions = True
    display_mode = None
    running = True
    precise_math_constants = True
    temporary_files_path = None
    base_path = None
    custom_compiled_behavior = {}
    cython_acceleration_available = False
    cython_acceleration_enabled = False
    python_acceleration_enabled = False
    pmma_module_spine = {}
    do_anti_aliasing = True
    development_mode = True
    refresh_rate = 60
    display_initialized = False
    context: "_moderngl.Context" = None
    power_saving_mode = False
    number_of_draw_calls = 0
    total_time_spent_drawing = 0
    pmma_initialized = False
    formatted_developer_messages = []
    pygame_launch_message = ""
    in_game_loop = False
    application_start_time = None
    application_average_frame_rate = {"Samples": 0, "Mean": 0}
    perlin_noise_prefill_single_samples = 0
    perlin_noise_prefill_array_samples = 0
    window_context = None
    display_mode_set = False
    number_of_instantiated_objects = 0
    iteration_id = None
    language = None
    opengl_objects = {}