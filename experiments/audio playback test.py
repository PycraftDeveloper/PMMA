import pmma
import threading
import time


pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"H:\Music\the cleaner synthwave.wav")

effect = pmma.Reverb()
audio.add_effect(effect)

audio.play(blocking=False)
time.sleep(1)
audio.play(blocking=True)