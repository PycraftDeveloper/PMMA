from os import environ

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.draw import DrawIntermediary

def environ_to_registry():
    for key in Registry.__dict__:
        check_key = f"PMMA_{key}"
        if check_key in environ:
            value = environ[check_key]
            if "." in value:
                data_type, value = value.split(".")
                data_type = data_type.lower()
                if data_type == "int":
                    value = int(value)
                elif data_type == "float":
                    value = float(value)
                elif data_type == "bool":
                    value = bool(0) if value.lower() == "false" else bool(1)
            setattr(Registry, key, value)

def log_development(message, do_traceback=False, repeat_for_effect=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_development(message, do_traceback=do_traceback, repeat_for_effect=repeat_for_effect)
        return True
    return False

def log_information(message, do_traceback=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_information(message, do_traceback=do_traceback)
        return True
    return False

def log_warning(message, do_traceback=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_warning(message, do_traceback=do_traceback)
        return True
    return False

def log_error(message, do_traceback=True):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_error(message, do_traceback=do_traceback)
        return True
    return False

def compute():
    number_of_draw_calls = DrawIntermediary.number_of_draw_calls
    total_time_spent_drawing = DrawIntermediary.total_time_spent_drawing
    DrawIntermediary.number_of_draw_calls = 0
    DrawIntermediary.total_time_spent_drawing = 0

    if number_of_draw_calls > 600:
        log_development(f"Your application performance might soon be degraded by the time spent handling draw calls. Consider switching to the more optimized Render Pipeline through PMMA to avoid any potential slowdowns.")

    if total_time_spent_drawing == 0:
        return

    if 1/(total_time_spent_drawing) < Registry.refresh_rate:
        log_development(f"Your application performance is limited by the total number of draw calls being made. The program spent {total_time_spent_drawing}s on {number_of_draw_calls} total render calls, limiting your maximum refresh rate to: {1/(total_time_spent_drawing)}. Switching to the more optimized Render Pipeline will likely improve application performance.")