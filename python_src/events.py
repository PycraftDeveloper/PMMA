from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Events:
    def __init__(self, canvas=None):
        self.raw_events = []
        self.canvas = canvas

    def __get(self):
        self.raw_events = []
        if Registry.display_mode == Constants.PYGAME:
            self.raw_events += Registry.graphics_backend.event.get()

    def handle(self, enable_toggle_fullscreen=True, enable_close=True, return_events=True, canvas=None):
        if canvas is None:
            canvas = self.canvas
        self.__get()
        if enable_toggle_fullscreen or enable_close:
            for event in self.raw_events:
                if Registry.display_mode == Constants.PYGAME:
                    if event.type == Registry.graphics_backend.QUIT:
                        if enable_close:
                            Registry.running = False
                    elif event.type == Registry.graphics_backend.KEYDOWN:
                        if event.key == Registry.graphics_backend.K_ESCAPE:
                            if enable_close:
                                Registry.running = False
                        elif event.key == Registry.graphics_backend.K_F11:
                            if enable_toggle_fullscreen:
                                canvas.toggle_fullscreen()

        if return_events:
            #events = []
            #for event in self.raw_events:
            return self.raw_events

    def get_events(self, update_events=False):
        if update_events:
            self.__get()

        return self.events