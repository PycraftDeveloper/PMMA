import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=True)

events = pmma.Events()

video = pmma.Video()
video.load_from_file(r"H:\Videos\edited\Land mine.mp4", automatically_optimize_silent_videos=True) # fix audio sync issues
video.play()
video.set_looping(True)

while True:
    display.clear()

    events.handle()

    video.render()

    pmma.compute()
    display.refresh()