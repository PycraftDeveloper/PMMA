import threading

class Registry:
    render_thread = None

def require_render_thread(func):
    def wrapper(*args, **kwargs):
        if threading.current_thread() != Registry.render_thread:
            raise RuntimeError(f"{func.__name__} must be called from the render thread.")
        return func(*args, **kwargs)
    return wrapper