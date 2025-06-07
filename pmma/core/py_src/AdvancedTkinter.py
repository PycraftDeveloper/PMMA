from tkinter import ttk

from pmma.core.py_src.Constants import InternalConstants

class Tkinter:
    @staticmethod
    def style(widget):
        if widget not in InternalConstants.TKINTER_STYLES:
            print("This is not a valid widget name, the valid widget names are: Constants.TKINTER_STYLE_BUTTON, Constants.TKINTER_STYLE_CHECKBUTTON, Constants.TKINTER_STYLE_COMBOBOX, Constants.TKINTER_STYLE_ENTRY, Constants.TKINTER_STYLE_FRAME, Constants.TKINTER_STYLE_LABEL, Constants.TKINTER_STYLE_LABELFRAME, Constants.TKINTER_STYLE_MENUBUTTON, Constants.TKINTER_STYLE_NOTEBOOK, Constants.TKINTER_STYLE_PANEDWINDOW, Constants.TKINTER_STYLE_HORIZONTAL_PROGRESSBAR, Constants.TKINTER_STYLE_VERTICAL_PROGRESSBAR, Constants.TKINTER_STYLE_RADIOBUTTON, Constants.TKINTER_STYLE_HORIZONTAL_SCALE, Constants.TKINTER_STYLE_VERTICAL_SCALE, Constants.TKINTER_STYLE_HORIZONTAL_SCROLLBAR, Constants.TKINTER_STYLE_VERTICAL_SCROLLBAR, Constants.TKINTER_STYLE_SEPARATOR, Constants.TKINTER_STYLE_SIZEGRIP and Constants.TKINTER_STYLE_TREEVIEW.")
            return

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