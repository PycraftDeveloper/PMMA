import os
from pmma.registry import Registry

class Canvas(Registry):
    PYGAME = "pygame"
    def __init__(self, display_mode=PYGAME):
        if display_mode == Canvas.PYGAME:
            import pygame
            pygame.init()

        self.display = None
        Registry.display_mode = display_mode
        self.graphics_backend = __import__(display_mode)
        if Registry.display_mode == Canvas.PYGAME:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
            self.clock = self.graphics_backend.time.Clock()

    def create_canvas(self, width, height, caption="Canvas"):
        if Registry.display_mode == Canvas.PYGAME:
            self.display = self.graphics_backend.display.set_mode((width, height))
            self.graphics_backend.display.set_caption(caption)
        else:
            raise NotImplementedError

    def clear(self, *args):
        if Registry.display_mode == Canvas.PYGAME:
            self.display.fill(args)
        else:
            raise NotImplementedError

    def refresh(self, refresh_rate=60):
        if Registry.display_mode == Canvas.PYGAME:
            self.graphics_backend.display.update()
            self.clock.tick(refresh_rate)
        else:
            raise NotImplementedError

    def close(self):
        if Registry.display_mode == Canvas.PYGAME:
            self.graphics_backend.quit()
        else:
            raise NotImplementedError

    def get_fps(self):
        if self.display_mode == Canvas.PYGAME:
            return self.clock.get_fps()
        else:
            raise NotImplementedError