import os
from pmma.src.registry import Registry
from pmma.src.constants import Constants

class Canvas(Registry, Constants):
    def __init__(self, display_mode=Constants.PYGAME):
        Registry.graphics_backend = __import__(display_mode)
        if display_mode == Constants.PYGAME:
            Registry.graphics_backend.init()

        self.display = None
        Registry.display_mode = display_mode
        if Registry.display_mode == Constants.PYGAME:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
            self.clock = Registry.graphics_backend.time.Clock()

        self.fullscreen = None
        self.display_attributes = []

    def create_canvas(self, width, height, fullscreen=False, resizable=False, caption="Canvas", native_fullscreen=True, vsync=True):
        if Registry.display_mode == Constants.PYGAME:
            flags = 0
            if fullscreen:
                self.flags = flags or Registry.graphics_backend.FULLSCREEN
                if native_fullscreen:
                    width, height = 0, 0

            else:
                if resizable:
                    flags = flags or Registry.graphics_backend.RESIZABLE

            display_size = width, height
            self.display_attributes = [display_size, flags, vsync]
            self.display = Registry.graphics_backend.display.set_mode(display_size, flags, vsync=vsync)
            Registry.graphics_backend.display.set_caption(caption)
        else:
            raise NotImplementedError

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            if Registry.display_mode == Constants.PYGAME:
                self.display = Registry.graphics_backend.display.set_mode(
                    (0, 0),
                    self.display_attributes[1],
                    vsync=self.display_attributes[2])
        else:
            if Registry.display_mode == Constants.PYGAME:
                self.display = Registry.graphics_backend.display.set_mode(
                    self.display_attributes[0],
                    self.display_attributes[1],
                    vsync=self.display_attributes[2])


    def blit(self, content, position=[0, 0]):
        self.display.blit(content, position)

    def get_size(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.display.get_size()
        else:
            raise NotImplementedError

    def get_height(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.display.get_height()
        else:
            raise NotImplementedError

    def get_width(self):
        if Registry.display_mode == Constants.PYGAME:
            return self.display.get_width()
        else:
            raise NotImplementedError

    def clear(self, *args):
        if Registry.display_mode == Constants.PYGAME:
            self.display.fill(args)
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=60):
        if Registry.display_mode == Constants.PYGAME:
            self.graphics_backend.display.update()
            self.clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Constants.PYGAME:
            self.graphics_backend.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if self.display_mode == Constants.PYGAME:
            return self.clock.get_fps()
        else:
            raise NotImplementedError