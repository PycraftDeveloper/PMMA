import gc as _gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.utility.coordinate_utils import CoordinateIntermediary as _CoordinateIntermediary

class Coordinate:
    def __init__(self, in_type=Constants.CARTESIAN, *args):
        initialize(self)

        self.in_type = in_type
        self.points = args

        self.intermediary = _CoordinateIntermediary(in_type, *args)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def out(self, out_type):
        return self.intermediary.out(out_type)

    def convert_range(self, in_range, out_range):
        return self.intermediary.convert_range(in_range, out_range)