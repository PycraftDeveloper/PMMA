from importlib import import_module as _importlib__import_module
from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.error_utils import TooManyInstancesError as _TooManyInstancesError

def initialize(instance, unique_instance=None, add_to_pmma_module_spine=False, logging_instantiation=False):
    instance._shut_down = False
    instance._attributes = []

    if _Registry.pmma_initialized is False:
        if not logging_instantiation:
            _importlib__import_module("pmma.__init__").init()
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                "You haven't yet initialized PMMA. This can be done by calling \
'pmma.init()' any time before using any of PMMA functions. As you haven't called \
`pmma.init()` yet, we have initialized PMMA for you, and made assumptions about \
how you intend to use it. Whilst this shouldn't be a problem for most people, \
doing this can heavily customize PMMA's behavior.")

    if unique_instance is not None:
        if unique_instance in _Constants.OBJECT_IDENTIFIERS:
            if unique_instance in _Registry.pmma_module_spine.keys():
                if not logging_instantiation:
                    _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_warning(
                        "{} object already exists.",
                        variables=[unique_instance.capitalize()])

                if not logging_instantiation:
                    _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                        "Some PMMA objects can only be initialized once. \
This is to avoid creating unexpected behavior.")

                raise _TooManyInstancesError(f"{unique_instance.capitalize()} object already exists.")
        else:
            if not logging_instantiation:
                _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("{} name was not recognized to \
PMMA. To register it, make sure it exists in the '_Constants' object, and in its attribute \
'OBJECT_IDENTIFIERS' list.", variables=[" ".join(word.capitalize() for word in unique_instance.split())])

    if add_to_pmma_module_spine:
        _Registry.pmma_module_spine[unique_instance] = instance

    _Registry.number_of_instantiated_objects += 1