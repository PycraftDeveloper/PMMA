import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True)

events = pmma.Events()

video = pmma.Video()
video.load_from_file(r"H:\Videos\2024-09-26 13-14-30.mp4") # fix audio sync issues

n = 200
c = 0
while True:
    display.clear()

    events.handle()

    video.render()

    pmma.compute()
    display.refresh()

    if c > n:
        video.pause()
        if c > n*2:
            video.resume()
    c += 1