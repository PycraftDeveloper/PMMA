import pmma

from pedalboard import Chorus

pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\videoplayback (1).wav")

audio.play()