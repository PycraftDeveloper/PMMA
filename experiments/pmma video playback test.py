import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=False)

events = pmma.Events()

video = pmma.Video()
video.load_from_file(r"H:\Videos\edited\4 point blur.mp4") # fix audio sync issues
video.play()
video.set_looping(True)

rev = pmma.Reverb()
video.get_audio_channel().add_effect(rev)

while True:
    display.clear()

    events.handle()

    video.render()

    pmma.compute()
    display.refresh(refresh_rate=2000)