import gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.backpack import Backpack
from pmma.python_src.display import Display
from pmma.python_src.events import Events
from pmma.__init__ import init

class QuickStart:
    def __init__(self, width=None, height=None, fullscreen=True, resizable=False, caption="PMMA Display", vsync=True, alpha=False):
        self.attributes = []

        if Registry.pmma_initialized is False:
            init()

        Registry.pmma_object_instances[id(self)] = self
        self._shut_down = False

        self.display = Display()
        self.display.create(width=width, height=height, fullscreen=fullscreen, resizable=resizable, caption=caption, vsync=vsync, alpha=alpha)
        self.events = Events()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self.display.quit()
            self.events.quit()
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def start(self, clear_color=None, enable_toggle_fullscreen=True, enable_close=True, return_events=True):
        self.events.handle(enable_toggle_fullscreen=enable_toggle_fullscreen, enable_close=enable_close, return_events=return_events)
        self.display.clear(clear_color)

    def end(self,refresh_rate=None):
        compute()
        self.display.refresh(refresh_rate=refresh_rate)
        return Registry.running is False or Backpack.running is False