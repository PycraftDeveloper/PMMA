from moderngl import LINEAR as _moderngl__LINEAR

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Texture:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._PIL_Image__module = _ModuleManager.import_module("PIL.Image")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._unique_identifier = id(self)
        _Registry.opengl_objects[self._unique_identifier] = self

        self._texture = None
        self._size = (None, None)
        self._components = None
        self._data = None
        self._scaling = None
        self._samples = None
        self._intended_samples = None

        self._created = False

        self._logger = self._logging_utils__module.InternalLogger()

    def create(self, size, data=None, components=_Constants.RGB, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None, samples=None, internal=True):
        """
        🟩 **R** -
        """
        if self._texture is not None:
            self._texture.release()

        self._size = size
        self._components = len(components)
        self._data = data

        if samples is None:
            samples = 0

        self._intended_samples = samples

        if samples != 0:
            if internal is False:
                self._logger.log_development("You are using an anti-aliased texture. Therefore, please \
make sure that you update your shader that uses this texture accordingly, otherwise you will \
encounter visual issues with that texture when you go to render something using it.")

        if samples > _Registry.context.max_samples:
            if internal is False:
                self._logger.log_development("The requested number of samples is greater than the maximum \
number of samples supported by your system. The maximum number of samples will be used instead. The \
maximum number of samples supported by your system is: {}", variables=[_Registry.context.max_samples])
            samples = _Registry.context.max_samples

        self._samples = samples

        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

        self._texture = _Registry.context.texture(self._size, self._components, self._data, samples=self._samples)
        self._texture.filter = (self._scaling[0], self._scaling[1])
        self._created = True

    def write(self, data):
        """
        🟩 **R** -
        """
        self._texture.write(data)

    def load_from_file(self, file_path, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None):
        """
        🟩 **R** -
        """
        image = self._PIL_Image__module.open(file_path)
        self._size = image.size
        self._components = len(image.mode)
        self._data = image.tobytes()
        image.close()

        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

        self._texture = _Registry.context.texture(self._size, self._components, self._data)
        self._texture.filter = (self._scaling[0], self._scaling[1])

    def set_scaling(self, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None):
        """
        🟩 **R** -
        """
        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

    def get_samples(self):
        """
        🟩 **R** -
        """
        return self._samples

    def get_intended_samples(self):
        """
        🟩 **R** -
        """
        return self._intended_samples

    def texture_to_PIL_image(self):
        """
        🟩 **R** -
        """
        if self._texture is not None:
            return self._PIL_Image__module.frombytes("RGB", self._size, self._texture.read())

    def get_texture(self):
        """
        🟩 **R** -
        """
        return self._texture

    def use(self, location=0):
        """
        🟩 **R** -
        """
        if self._texture is not None:
            self._texture.use(location=location)

    def get_size(self):
        """
        🟩 **R** -
        """
        return self._size

    def get_components(self):
        """
        🟩 **R** -
        """
        return self._components

    def get_data(self):
        """
        🟩 **R** -
        """
        return self._data

    def build_mipmaps(self, base=0, max_level=1000):
        """
        🟩 **R** -
        """
        if self._texture is not None:
            self._texture.build_mipmaps(base=base, max_level=max_level)

    def recreate(self):
        """
        🟩 **R** -
        """
        if self._texture is not None:
            self._texture.release()

            self._texture = _Registry.context.texture(self._size, self._components, self._data, samples=self._samples)
            self._texture.filter = (self._scaling[0], self._scaling[1])

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._created = False
            if self._texture is not None:
                self._texture.release()
            del _Registry.opengl_objects[self._unique_identifier]

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def get_created(self):
        """
        🟩 **R** -
        """
        return self._created