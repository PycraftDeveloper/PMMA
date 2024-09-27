import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=False)

events = pmma.Events()

video = pmma.Video()
video.load_from_file(r"H:\Videos\2024-09-26 13-14-30.mp4")

while True:
    display.clear()

    events.handle()

    video.render()

    pmma.compute()
    display.refresh(refresh_rate=2000)