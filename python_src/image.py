import time as _time

from PIL import Image as _ImageModule
import pygame as _pygame

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.memory_manager import MemoryManager as _MemoryManager

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class Image:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._memory_manager_instance = _MemoryManager()

        self._graphics_backend_image_address = None

        self._pil_image_address = None

        if not _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DISPLAY_OBJECT)
            from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
            _DisplayIntermediary()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def create_from_file(self, image_path):
        """
        🟩 **R** -
        """
        if self._pil_image_address is not None:
            self._memory_manager_instance.remove(
                self._pil_image_address)

        start = _time.perf_counter()
        pil_image = _ImageModule.open(image_path)
        end = _time.perf_counter()
        self._pil_image_address = self._memory_manager_instance.add(
            pil_image,
            object_creation_time=end-start,
            recreatable_object=True)

    def create_from_bytes(self, image_bytes):
        """
        🟩 **R** -
        """
        if self._pil_image_address is not None:
            self._memory_manager_instance.remove(
                self._pil_image_address)

        start = _time.perf_counter()
        pil_image = _ImageModule.frombytes(image_bytes)
        end = _time.perf_counter()

        self._pil_image_address = self._memory_manager_instance.add(
            pil_image,
            object_creation_time=end-start,
            recreatable_object=False)

    def image_to_PIL_object(self):
        """
        🟩 **R** -
        """
        return self._memory_manager_instance.get(
            self._pil_image_address)

    def image_to_display_renderable_object(self, auto_optimize=True):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()
        pil_image = self._memory_manager_instance.get(
            self._pil_image_address)

        if pil_image is None and self._pil_image_address is not None:
            self.create_from_file(self._pil_image_address)
            pil_image = self._memory_manager_instance.get(
                self._pil_image_address)

        graphics_backend_image = _pygame.image.fromstring(
            pil_image.tobytes(),
            pil_image.size,
            pil_image.mode)
        if auto_optimize:
            if pil_image.mode == "RGBA":
                graphics_backend_image = graphics_backend_image.convert_alpha()
            else:
                graphics_backend_image = graphics_backend_image.convert()

        end = _time.perf_counter()

        self._graphics_backend_image_address = self._memory_manager_instance.add(
            graphics_backend_image,
            object_creation_time=end-start)

        return graphics_backend_image

    def blit(self, position, surface=None):
        """
        🟩 **R** -
        """
        if surface is None:
            surface = self._display

        if self._memory_manager_instance.get(self._graphics_backend_image_address) is None:
            object = self.image_to_display_renderable_object()
        else:

            object = self._memory_manager_instance.get(
                self._graphics_backend_image_address)

        surface.blit(object, position)