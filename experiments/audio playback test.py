import pmma
import threading
import time


pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\videoplayback (1).wav")

audio.play(blocking=False)

time.sleep(50)