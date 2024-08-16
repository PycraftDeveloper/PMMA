from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class GPUs:
    def __init__(self):
        initialize(unique_instance=Constants.GPUS_OBJECT, add_to_pmma_module_spine=True)