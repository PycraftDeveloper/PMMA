from pmma.registry import Registry
from pmma.constants import Constants

class Events(Registry, Constants):
    def __init__(self):
        self.events = []

    def __get(self):
        self.events = []
        if Registry.display_mode == Constants.PYGAME:
            self.events += Registry.graphics_backend.event.get()

    def handle(self, canvas, enable_toggle_fullscreen=True, enable_close=True):
        self.__get()
        if enable_toggle_fullscreen or enable_close:
            for event in self.events:
                if Registry.display_mode == Constants.PYGAME:
                    if event.type == Registry.graphics_backend.QUIT:
                        if enable_close:
                            Registry.running = False
                    if event.type == self.graphics_backend.KEYDOWN:
                        if event.key == Registry.graphics_backend.K_ESCAPE:
                            if enable_close:
                                Registry.running = False
                        if event.key == Registry.graphics_backend.K_F11:
                            if enable_toggle_fullscreen:
                                canvas.toggle_fullscreen()

        return self.events

    def get_events(self, update_events=False):
        if update_events:
            self.__get()

        return self.events