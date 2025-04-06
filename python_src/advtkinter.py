from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.constants import Constants as _Constants

class Tkinter:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._tkinter__module = _ModuleManager.import_module("tkinter")
        self._tkinter_ttk__module = _ModuleManager.import_module("tkinter.ttk")

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def style(self, widget):
        """
        🟩 **R** -
        """
        style = self._tkinter_ttk__module.Style()
        style.configure(
            widget,
            background="white",
            foreground="black",
            borderwidth=1,
            focusthickness=3,
            focuscolor="none")

        style.map(
            widget,
            background=[
                ("active", "white")])

    def get_display_size(self):
        """
        🟩 **R** -
        """
        try:
            root = self._tkinter__module.Tk()

            screen_size_x = root.winfo_screenwidth()
            screen_size_y = root.winfo_screenheight()
            root.destroy()

            return (
                screen_size_x,
                screen_size_y)
        except:
            return (0, 0)

    def set_window_size(self, root, x_size, y_size, x_position=_Constants.CENTER, y_position=_Constants.CENTER):
        """
        🟩 **R** -
        """
        window_size = (x_size, y_size)

        if x_position == _Constants.CENTER or y_position == _Constants.CENTER:
            screen_size = self.get_display_size()
            if x_position == _Constants.CENTER:
                x_position = int((screen_size[0]-window_size[0])/2)
            else:
                y_position = int((screen_size[1]-window_size[1])/2)

        root.geometry(f"{window_size[0]}x{window_size[1]}+{x_position}+{y_position}")