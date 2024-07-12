from PIL import Image as ImageModule
import time

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Image:
    def __init__(self, image_path):
        self.memory_manager_instance = Registry.pmma_module_spine[Constants.MEMORYMANAGER_OBJECT]

        self.image_path = image_path
        self.load_image()
        self.graphics_backend_image_address = None

    def load_image(self):
        start = time.perf_counter()
        pil_image = ImageModule.open(self.image_path)
        end = time.perf_counter()
        self.pil_image_address = self.memory_manager_instance.add_object(pil_image, object_creation_time=end-start)

    def image_to_display_renderable_object(self, auto_optimize=True):
        start = time.perf_counter()
        pil_image = self.memory_manager_instance.get_object(self.pil_image_address)

        if pil_image is None:
            self.load_image()
            pil_image = self.memory_manager_instance.get_object(self.pil_image_address)

        if Registry.display_mode == Constants.PYGAME:
            graphics_backend_image = Registry.graphics_backend.image.fromstring(
                pil_image.tobytes(),
                pil_image.size,
                pil_image.mode)
            if auto_optimize:
                if pil_image.mode == "RGBA":
                    graphics_backend_image = graphics_backend_image.convert_alpha()
                else:
                    graphics_backend_image = graphics_backend_image.convert()
        else:
            raise NotImplementedError

        end = time.perf_counter()
        self.graphics_backend_image_address = self.memory_manager_instance.add_object(graphics_backend_image, object_creation_time=end-start)

        return graphics_backend_image

    def blit(self, position, surface=None):
        if surface is None:
            surface = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if self.memory_manager_instance.get_object(self.graphics_backend_image_address) is None:
            object = self.image_to_display_renderable_object()
        else:
            object = self.memory_manager_instance.get_object(self.graphics_backend_image_address)

        surface.blit(object, position)