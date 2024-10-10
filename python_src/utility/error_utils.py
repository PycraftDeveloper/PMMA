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

class DisplayNotYetCreatedError(Exception):
    """Display was not yet created!"""
    pass

class UnexpectedBufferAttributeFormatError(Exception):
    """Unexpected buffer attribute format!"""
    pass

class UnknownDataTypeError(Exception):
    """Unknown data type!"""
    pass

class UnexpectedBufferAttributeError(Exception):
    """Unexpected buffer attribute!"""
    pass

class ShapeRadiusNotSpecifiedError(Exception):
    """Shape radius was not specified!"""
    pass

class OpenGLObjectNotPreparedForRecreation(Exception):
    """OpenGL object was not prepared for recreation!"""
    pass