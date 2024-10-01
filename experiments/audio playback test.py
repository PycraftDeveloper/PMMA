import pmma
import threading
import time


pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\1kHz Sine Wave Test Tone Signal.mp3")

effect = pmma.Reverb(chunk_size=2048)
audio.add_effect(effect)

audio.play(blocking=True)