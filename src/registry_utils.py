if __name__ != "__main__":
    try:
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start PMMA",
            f"A problem occurred whilst trying to start PMMA.\nMore Details: {error}")

    class Registry:
        #root = path_utils.Path(__file__)
        #for _ in range(4):
            #root.up()
        #base_path = root.path
        y = "Yellow"
else:
    MESSAGE = "You need to run this through PMMA "
    MESSAGE += "please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
