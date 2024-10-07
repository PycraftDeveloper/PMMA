from gc import collect as _gc__collect

from PIL import Image as _PIL__Image
from moderngl import LINEAR as _moderngl__LINEAR

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Texture:
    def __init__(self):
        _initialize(self)

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

        self._logger = _InternalLogger()

    def prepare_for_recreation(self):
        pass # WIP

    def create(self, size, data=None, components=_Constants.RGB, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None, samples=None, internal=True):
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
        self._texture.write(data)

    def load_from_file(self, file_path, scaling=_moderngl__LINEAR, x_scaling=None, y_scaling=None):
        image = _PIL__Image.open(file_path)
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
        if x_scaling is None:
            x_scaling = scaling
        if y_scaling is None:
            y_scaling = scaling

        self._scaling = (x_scaling, y_scaling)

    def get_samples(self):
        return self._samples

    def get_intended_samples(self):
        return self._intended_samples

    def texture_to_PIL_image(self):
        if self._texture is not None:
            return _PIL__Image.frombytes("RGB", self._size, self._texture.read())

    def get_texture(self):
        return self._texture

    def use(self, location=0):
        if self._texture is not None:
            self._texture.use(location=location)

    def get_size(self):
        return self._size

    def get_components(self):
        return self._components

    def get_data(self):
        return self._data

    def build_mipmaps(self, base=0, max_level=1000):
        if self._texture is not None:
            self._texture.build_mipmaps(base=base, max_level=max_level)

    def recreate(self):
        if self._texture is not None:
            self._texture.release()

            self._texture = _Registry.context.texture(self._size, self._components, self._data, samples=self._samples)
            self._texture.filter = (self._scaling[0], self._scaling[1])

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._texture is not None:
                self._texture.release()
            del _Registry.opengl_objects[self._unique_identifier]
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_created(self):
        return self._created