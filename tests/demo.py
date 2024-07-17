from demo_pmma_class_core import PMMA_helper_class

from batch import Comp


class BasicDrawOperation(PMMA_helper_class):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.result = None

    def perform_operation(self):
        # Perform some operation and store the result
        self.result = f"Operation with {self.param1} and {self.param2}"

d = BasicDrawOperation()

inst = Comp()