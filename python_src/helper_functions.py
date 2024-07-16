import inspect

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

def check_if_object_is_class_or_function(param):
    if inspect.isclass(param):
        return Constants.CLASS
    elif isinstance(param, object) and not inspect.isfunction(param):
        return Constants.CLASS_INSTANCE
    elif inspect.isfunction(param):
        return Constants.FUNCTION
    else:
        return Constants.UNKNOWN