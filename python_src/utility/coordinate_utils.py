from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.advmath import Math

class CoordinateIntermediary:
    def __init__(
            self,
            in_type=Constants.CARTESIAN,
            *args):

        self.in_type = in_type
        self.points = args

        self.math = Math()

    def out(self, out_type):
        return self.points

    def convert_range(self, in_range, out_range):
        points = []
        for point in self.points:
            new_point = []
            for dimension in point:
                new_point.append(
                    self.math.ranger(
                        dimension,
                        in_range,
                        out_range))

            points.append(new_point)
        return points