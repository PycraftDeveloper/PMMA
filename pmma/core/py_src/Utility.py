import threading

class Registry:
    render_thread = None
    checking_for_updates = True
    update_checking_thread = None
    passport_instance = None
    profiler_instance = None


def require_render_thread(func):
    def wrapper(*args, **kwargs):
        if threading.current_thread() != Registry.render_thread:
            raise RuntimeError(f"{func.__name__} must be called from the render thread.")
        return func(*args, **kwargs)
    return wrapper