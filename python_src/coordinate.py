from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.advmath import Math

class CoordinateIntermediary:
    def __init__(
            self,
            in_type=Constants.CARTESIAN,
            *args):

        self.in_type = in_type
        self.points = args

        self.math = Math()

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

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


class Coordinate:
    def __init__(self, in_type=Constants.CARTESIAN, *args):
        self.in_type = in_type
        self.points = args

        self.intermediary = CoordinateIntermediary(in_type, *args)

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def out(self, out_type):
        return self.intermediary.out(out_type)

    def convert_range(self, in_range, out_range):
        return self.intermediary.convert_range(in_range, out_range)