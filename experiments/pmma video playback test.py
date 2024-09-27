import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True)

events = pmma.Events()

video = pmma.Video()
video.load_from_file(r"H:\Videos\2024-09-26 13-14-30.mp4") # fix audio sync issues

audio = video.get_audio_channel()

fx = pmma.Reverb()
fx.set_damping(0)
fx.set_room_size(1)
audio.add_effect(fx)
while True:
    display.clear()

    events.handle()

    video.render()

    pmma.compute()
    display.refresh()