import time

from PIL import Image as ImageModule
import pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Image:
    def __init__(self):
        self.memory_manager_instance = Registry.pmma_module_spine[Constants.MEMORYMANAGER_OBJECT]

        self.attributes = []

        self.graphics_backend_image_address = None

        self.pil_image_address = None

        Registry.pmma_object_instances[id(self)] = self
        self._shut_down = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self):
        self.__del__()
        self._shut_down = True

    def create_from_file(self, image_path):
        if self.pil_image_address is not None:
            self.memory_manager_instance.remove_object(
                self.pil_image_address)

        start = time.perf_counter()
        pil_image = ImageModule.open(image_path)
        end = time.perf_counter()
        self.pil_image_address = self.memory_manager_instance.add_object(
            pil_image,
            object_creation_time=end-start,
            recreatable_object=True)

    def create_from_bytes(self, image_bytes):
        if self.pil_image_address is not None:
            self.memory_manager_instance.remove_object(
                self.pil_image_address)

        start = time.perf_counter()
        pil_image = ImageModule.frombytes(image_bytes)
        end = time.perf_counter()

        self.pil_image_address = self.memory_manager_instance.add_object(
            pil_image,
            object_creation_time=end-start,
            recreatable_object=False)

    def image_to_PIL_object(self):
        return self.memory_manager_instance.get_object(
            self.pil_image_address)

    def image_to_display_renderable_object(self, auto_optimize=True):
        start = time.perf_counter()
        pil_image = self.memory_manager_instance.get_object(
            self.pil_image_address)

        if pil_image is None:
            self.load_image()
            pil_image = self.memory_manager_instance.get_object(
                self.pil_image_address)

        if Registry.display_mode == Constants.PYGAME:
            graphics_backend_image = pygame.image.fromstring(
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

        self.graphics_backend_image_address = self.memory_manager_instance.add_object(
            graphics_backend_image,
            object_creation_time=end-start)

        return graphics_backend_image

    def blit(self, position, surface=None):
        if surface is None:
            surface = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if self.memory_manager_instance.get_object(self.graphics_backend_image_address) is None:
            object = self.image_to_display_renderable_object()
        else:

            object = self.memory_manager_instance.get_object(
                self.graphics_backend_image_address)

        surface.blit(object, position)