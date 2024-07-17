import dill

class PMMA_helper_class:
    def __init__(self):
        pass

    def serialize(self):
        return dill.dumps(self)

    @staticmethod
    def deserialize(serialized_obj):
        return dill.loads(serialized_obj)