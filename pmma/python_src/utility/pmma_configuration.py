from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.registry_utils import Registry as _Registry

from pmma.python_src.file import path_builder as _path_builder

class PMMAConfigurationIntermediary:
    def __init__(self):
        self._json__module = _ModuleManager.import_module("json")

    def load_configuration(self):
        """
        🟩 **R** -
        """
        try:
            with open(_path_builder(_Registry.base_path, "configuration", "config.json"), "r") as f:
                saved_configurations = self._json__module.loads(f.read())

            for key in saved_configurations:
                setattr(_Registry, key, saved_configurations[key])
        except:
            pass

    def save_configuration(self):
        """
        🟩 **R** -
        """
        saved_configurations = {
            "last_checked_for_updates": _Registry.last_checked_for_updates,
            "update_available": _Registry.update_available,
        }

        with open(_path_builder(_Registry.base_path, "configuration", "config.json"), "w") as f:
            f.write(self._json__module.dumps(saved_configurations, indent=4))