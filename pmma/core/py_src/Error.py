class NoInputDevicesFoundError(Exception):
    """No input devices were found!"""
    pass

class UnableToReadAudioSampleError(Exception):
    """Unable to read audio sample!"""
    pass

class PassportNotInitializedError(Exception):
    """Passport not initialized!"""
    pass

class PassportNotRegisteredError(Exception):
    """Passport has not been registered!"""
    pass

class DirectoryNotFoundError(Exception):
    """Directory not found!"""
    pass

class DirectoryAlreadyExistsError(Exception):
    """Directory already exists!"""
    pass