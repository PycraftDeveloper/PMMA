from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class QuickStart:
    """
    🟩 **R** -
    """
    def __init__(self,
            width=None,
            height=None,
            full_screen=True,
            resizable=False,
            no_frame=False,
            caption=None,
            vsync=True,
            icon=None,
            transparent_display=False,
            centered=True):
        """
        🟩 **R** -
        """

        _initialize(self)

        self._backpack__module = _ModuleManager.import_module("pmma.python_src.backpack")
        self._display__module = _ModuleManager.import_module("pmma.python_src.display")
        self._events__module = _ModuleManager.import_module("pmma.python_src.events")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

        self._display = self._display__module.Display()
        self._display.create(
            width=width,
            height=height,
            full_screen=full_screen,
            resizable=resizable,
            no_frame=no_frame,
            caption=caption,
            vsync=vsync,
            icon=icon,
            transparent_display=transparent_display,
            centered=centered)

        self._events = self._events__module.Events()

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._display.quit()
            self._events.quit()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def start(
            self,
            do_display_clearing=True,
            clear_color=None,
            handle_full_screen_events=True,
            handle_exit_events=True,
            grab_extended_keyboard_events=False):
        """
        🟩 **R** -
        """

        self._events.handle(
            handle_full_screen_events=handle_full_screen_events,
            handle_exit_events=handle_exit_events,
            grab_extended_keyboard_events=grab_extended_keyboard_events)

        if do_display_clearing:
            self._display.clear(clear_color)

    def end(self, refresh_rate=None):
        """
        🟩 **R** -
        """
        self._internal_general_utils.compute()
        self._display.refresh(refresh_rate=refresh_rate)
        return _Registry.running is False or self._backpack__module.Backpack.running is False