import gc as _gc

from pmma.python_src.general import *
from pmma.python_src.utils.registry import Registry as _Registry
from pmma.python_src.backpack import Backpack as _Backpack
from pmma.python_src.display import Display as _Display
from pmma.python_src.events import Events as _Events

from pmma.python_src.utility.general_utils import initialize as _initialize

class QuickStart:
    def __init__(self, width=None, height=None, fullscreen=True, resizable=False, caption="PMMA Display", vsync=True, alpha=False):
        _initialize(self)

        self._display = _Display()
        self._display.create(width=width, height=height, fullscreen=fullscreen, resizable=resizable, caption=caption, vsync=vsync, alpha=alpha)
        self._events = _Events()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._display.quit()
            self._events.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def start(self, do_display_clearing=True, clear_color=None, enable_toggle_fullscreen=True, enable_close=True, return_events=True):
        self._events.handle(enable_toggle_fullscreen=enable_toggle_fullscreen, enable_close=enable_close, return_events=return_events)
        if do_display_clearing:
            self._display.clear(clear_color)

    def end(self, refresh_rate=None):
        compute()
        self._display.refresh(refresh_rate=refresh_rate)
        return Registry.running is False or _Backpack.running is False