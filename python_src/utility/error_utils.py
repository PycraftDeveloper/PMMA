class InitializationError(Exception):
    """PMMA was unable to initialize!"""
    pass

class DidNotInitializeError(Exception):
    """PMMA was not initialized!"""
    pass

class TooManyInstancesError(Exception):
    """Too many instances of a PMMA object were created!"""
    pass

class NoInputDevicesFoundError(Exception):
    """No input devices were found!"""
    pass

class UnableToReadAudioSampleError(Exception):
    """Unable to read audio sample!"""
    pass

class OpenGLNotYetInitializedError(Exception):
    """OpenGL was not yet initialized!"""
    pass

class LoggingNotInitializedError(Exception):
    """Logging was not yet initialized!"""
    pass