class NoInputDevicesFoundError(Exception):
    """No input devices were found!"""
    pass

class UnableToReadAudioSampleError(Exception):
    """Unable to read audio sample!"""
    pass