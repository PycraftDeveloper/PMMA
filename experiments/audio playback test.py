import pmma
import threading
import time


pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\videoplayback (1).wav")

audio.play(blocking=False)

time.sleep(3)

audio.pause()

time.sleep(1)

audio.resume()

time.sleep(50)