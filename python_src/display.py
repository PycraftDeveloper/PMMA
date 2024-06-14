import os

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Display:
    def __init__(self, display_mode=Constants.PYGAME):
        Registry.graphics_backend = __import__(display_mode)
        if display_mode == Constants.PYGAME:
            Registry.graphics_backend.init()

        self.surface = None
        Registry.display_mode = display_mode
        if Registry.display_mode == Constants.PYGAME:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
            self.clock = Registry.graphics_backend.time.Clock()

        self.fullscreen = None
        self.surface_attributes = []

    def create(self, width, height, fullscreen=False, resizable=False, caption="Display", native_fullscreen=True, vsync=True, alpha=False):
        if Registry.display_mode == Constants.PYGAME:
            flags = 0
            if fullscreen:
                self.flags = flags or Registry.graphics_backend.FULLSCREEN or Registry.graphics_backend.NOFRAME
                if native_fullscreen:
                    width, height = 0, 0

            else:
                if resizable:
                    flags = flags or Registry.graphics_backend.RESIZABLE

            display_size = width, height
            self.surface_attributes = [display_size, flags, vsync]
            self.surface = Registry.graphics_backend.display.set_mode(display_size, flags, vsync=vsync)
            Registry.graphics_backend.display.set_caption(caption)
        else:
            raise NotImplementedError

    def set_caption(self, caption):
        Registry.graphics_backend.display.set_caption(caption)

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            if Registry.display_mode == Constants.PYGAME:
                self.surface = Registry.graphics_backend.display.set_mode(
                    (0, 0),
                    self.surface_attributes[1],
                    vsync=self.surface_attributes[2])
        else:
            if Registry.display_mode == Constants.PYGAME:
                self.surface = Registry.graphics_backend.display.set_mode(
                    self.surface_attributes[0],
                    self.surface_attributes[1],
                    vsync=self.surface_attributes[2])


    def blit(self, content, position=[0, 0]):
        self.surface.blit(content, position)

    def get_size(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.surface.get_size()
        else:
            raise NotImplementedError

    def get_height(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.surface.get_height()
        else:
            raise NotImplementedError

    def get_width(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.surface.get_width()
        else:
            raise NotImplementedError

    def clear(self, *args):
        if args == ():
            args = (0, 0, 0)
        if Registry.display_mode == Constants.PYGAME:
            self.surface.fill(args)
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=60):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.display.update()
            if refresh_rate > 0:
                self.clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.clock.get_fps()
        else:
            raise NotImplementedError

    def get_center(self, as_integer=True):
        if Registry.display_mode == Constants.PYGAME:
            if as_integer:
                return self.surface.get_width() // 2, self.surface.get_height() // 2
            return self.surface.get_width() / 2, self.surface.get_height() / 2
        else:
            raise NotImplementedError