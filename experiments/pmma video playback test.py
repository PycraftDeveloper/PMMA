import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True)

events = pmma.Events()

video = pmma.Video()
video.load_from_file(r"H:\Videos\Timeline 1.mp4") # fix audio sync issues

audio = video.get_audio_channel()

while True:
    display.clear()

    events.handle()

    video.render()

    pmma.compute()
    display.refresh()