import pmma
import threading
import time


pmma.init()

def lower(inst):
    bd = 8
    while True:
        bd -= 0.3
        inst.set_bit_depth(bd)
        if bd < 3:
            break
        time.sleep(1)

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\videoplayback (1).wav")
crush = pmma.BitCrush()
audio.add_effect(crush)
threading.Thread(target=lower, args=(crush,)).start()

audio.play()