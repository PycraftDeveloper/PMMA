class InitializationError(Exception):
    """PMMA was unable to initialize!"""
    pass

class DidNotInitializeError(Exception):
    """PMMA was not initialized!"""
    pass

class TooManyInstancesError(Exception):
    """Too many instances of a PMMA object were created!"""
    pass