from os import environ

from pmma.python_src.registry import Registry

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