import pmma

pmma.init()

audio = pmma.Audio()
audio.load_from_file(r"A:\Audio Loops\Thomas Jebson - Pycraft (original) - Forest Theme.ogg")

effect = pmma.Reverb()
audio.add_effect(effect)

audio.play(blocking=True)