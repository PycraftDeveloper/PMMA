import tkinter as tk
from tkinter import ttk

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Tkinter:
    def __init__(self):
        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def style(self, widget):
        style = ttk.Style()
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
            root = tk.Tk()

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
            root = Registry.root

        screen_size = self.get_display_size()
        window_size = (x, y)
        centred_x_position = int((screen_size[0]-window_size[0])/2)
        centred_y_position = int((screen_size[1]-window_size[1])/2)

        root.geometry(f"{window_size[0]}x{window_size[1]}+{centred_x_position}+{centred_y_position}")