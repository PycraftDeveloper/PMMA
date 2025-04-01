import importlib

class ModuleManager:
    imported_modules = {}

    def import_module(module_name):
        module = ModuleManager.imported_modules.get(module_name)
        if module is None:
            module = importlib.import_module(module_name)
            ModuleManager.imported_modules[module_name] = module
        return module