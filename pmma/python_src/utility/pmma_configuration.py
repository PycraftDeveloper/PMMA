from json import dumps
from json import loads

from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.registry_utils import Registry as _Registry

def load_configuration():
    """
    🟩 **R** -
    """
    try:
        with open(_path_builder(_Registry.base_path, "configuration", "config.json"), "r") as f:
            saved_configurations = loads(f.read())

        for key in saved_configurations:
            setattr(_Registry, key, saved_configurations[key])
    except:
        pass

def save_configuration():
    """
    🟩 **R** -
    """
    saved_configurations = {
        "last_checked_for_updates": _Registry.last_checked_for_updates,
        "update_available": _Registry.update_available,
    }

    with open(_path_builder(_Registry.base_path, "configuration", "config.json"), "w") as f:
        f.write(dumps(saved_configurations, indent=4))