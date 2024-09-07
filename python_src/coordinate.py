import gc as _gc

from pmma.python_src.constants import Constants

from pmma.python_src.utility.coordinate_utils import CoordinateIntermediary as _CoordinateIntermediary
from pmma.python_src.utility.general_utils import initialize as _initialize

class Coordinate:
    def __init__(self):
        _initialize(self)

        self._intermediary = _CoordinateIntermediary()

    def input_coordinates(self, coordinate, format=Constants.CONVENTIONAL_COORDINATES):
        self._intermediary.set_coordinate(coordinate, in_type=format)

    def output_coordinates(self, format=Constants.CONVENTIONAL_COORDINATES):
        return self._intermediary.get_coordinate(out_type=format)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True