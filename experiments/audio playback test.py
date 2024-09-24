import pmma
import threading
import time


pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\videoplayback (1).wav")

effect = pmma.Compressor()
audio.add_effect(effect)
effect.set_ratio(40)

audio.play(blocking=False)

time.sleep(50)