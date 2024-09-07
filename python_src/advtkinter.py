import tkinter as _tk
from tkinter import ttk as _ttk
import gc as _gc

from pmma.python_src.utils.registry import Registry as _Registry

from pmma.python_src.utility.general_utils import initialize as _initialize

class Tkinter:
    def __init__(self):
        _initialize(self)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def style(self, widget):
        style = _ttk.Style()
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
        try:
            root = _tk.Tk()

            screen_size_x = root.winfo_screenwidth()
            screen_size_y = root.winfo_screenheight()
            root.destroy()

            return (
                screen_size_x,
                screen_size_y)
        except:
            return (0, 0)

    def set_size(self, x, y, root=None):
        if root is None:
            root = _Registry.root

        screen_size = self.get_display_size()
        window_size = (x, y)
        centred_x_position = int((screen_size[0]-window_size[0])/2)
        centred_y_position = int((screen_size[1]-window_size[1])/2)

        root.geometry(f"{window_size[0]}x{window_size[1]}+{centred_x_position}+{centred_y_position}")