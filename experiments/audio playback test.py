import pmma
import threading
import time


pmma.init()

def lower(inst):
    bd = 0
    while True:
        bd += 1.66666666666666666666666666666666666
        inst.set_room_size(bd/100)
        if bd > 100:
            inst.set_room_size(1)
            break
        print(bd)
        time.sleep(1)

audio = pmma.Audio()
audio.load_from_file(r"H:\Downloads\videoplayback (1).wav")
crush = pmma.Reverb()
audio.add_effect(crush)
crush.set_freeze_mode(True)
crush.set_room_size(1)
threading.Thread(target=lower, args=(crush,))#.start()

audio.play()