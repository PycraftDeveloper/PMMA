import time
import tkinter

import numpy

import pmma

pmma.init(use_c_acceleration=True)
########################################################################

print("Testing MATH")
math = pmma.Math()
print("Testing MATH: Smooth-Step")
math.smooth_step(0.1)
print("Testing MATH: Pythag")
math.pythag([1, 2])
print("Testing MATH: Ranger")
math.ranger(10, [0, 10], [0, 1])
print("Testing MATH: Nparray-Ranger")
math.nparray_ranger(numpy.array([10, 10]), [0, 10], [0, 1])
print("Testing MATH: Compute-Position")
math.compute_position(numpy.array([0, 0, 0]), numpy.array([0, 0, 1]), numpy.array([0, 1, 0]))
print("Testing MATH: Perspective-FOV")
math.perspective_fov(70, 16/9, 0.1, 1000)
print("Testing MATH: Look-At")
math.look_at(numpy.array([0, 0, 0]), numpy.array([0, 0, 1]), numpy.array([0, 1, 0]))
print("Testing MATH: Multiply")
math.multiply(numpy.array([1, 2, 3]), numpy.array([4, 5, 6]))
print("Testing MATH: Quit")
math.quit()

########################################################################

def simple_procedure():
    for i in range(5):
        print(i)
        time.sleep(1)

print("Testing THREAD")
print("Testing THREAD: Creation")
thread = pmma.Thread(target=simple_procedure)
print("Testing THREAD: Start")
thread.start()
print("Testing THREAD: Waiting for THREE SECONDS")
time.sleep(3)
print("Testing THREAD: Kill")
thread.kill()
print("Testing THREAD: Waiting for FIVE SECONDS")
time.sleep(5)

print("Testing THREAD: No additional output should have been observed since previous log.")
########################################################################

root = tkinter.Tk()

print("Testing TKINTER")
_tkinter = pmma.Tkinter()
print("Testing TKINTER: Style")
_tkinter.style(pmma.Constants.TKINTER_STYLE_LABEL)
print("Testing TKINTER: Get-Display-Size")
_tkinter.get_display_size()
print("Testing TKINTER: Set-Window-Size")
_tkinter.set_window_size(root, 64, 64, x_position=pmma.Constants.CENTER, y_position=0)

root.update_idletasks()

print("Testing TKINTER: Quit")
_tkinter.quit()
root.destroy()
root.quit()

########################################################################

print("Testing FILE")
file = pmma.File(__file__)
print("Testing FILE: Get-Directory")
TestDirectory = file.get_directory()
print("Testing FILE: Quit")

########################################################################

print("Testing AUDIO")
audio = pmma.Audio()
print("Testing AUDIO: Load-From-File")
audio.load_from_file(f"{TestDirectory}\\resources\\Cymatics - 2020 Nostalgic Melody Loop 7 - 150 BPM B Min.wav")

print("Testing AUDIO: Get-Sample-Rate")
audio.get_sample_rate()
print("Testing AUDIO: Get-Number-Of-Channels")
audio.get_number_of_channels()

print("Testing AUDIO: Audio should play for THREE SECONDS.")
audio.play(blocking=False)

time.sleep(3)

print("Testing AUDIO: Audio should PAUSE for ONE SECOND.")
audio.pause()

time.sleep(1)

print("Testing AUDIO: Audio should RESUME for THREE SECONDS.")
audio.resume()

time.sleep(3)

print("Testing AUDIO: Audio should STOP.")
audio.stop()

time.sleep(1)

print("Testing AUDIO: Audio should LOOP twice.")
audio.set_looping(True)
audio.play(blocking=False)

time.sleep(24)

print("Testing AUDIO: Audio should STOP for ONE SECOND.")
audio.stop()
audio.set_looping(False)

time.sleep(1)

print("Testing AUDIO: Audio should play again, and the next print statement will appear when the sound has finished playing.")
audio.play(blocking=True)
audio.stop()

time.sleep(1)

print("Testing AUDIO: Audio should play again, after a ONE SECOND DELAY for FIVE SECONDS.")
audio.play(blocking=False, delay=1)

time.sleep(5)

print("Testing AUDIO: Audio should STOP.")
audio.stop()

time.sleep(1)

print("Testing AUDIO: Audio should start playing.")
audio.play(blocking=False)

time.sleep(2)
print("Testing AUDIO: Audio should be at half volume")
audio.set_volume(50)

time.sleep(2)
print("Testing AUDIO: Audio should be at full volume")
audio.set_volume(100)

time.sleep(2)
print("Testing AUDIO: Audio should play from the LEFT.")
audio.set_pan(-100)

time.sleep(2)
print("Testing AUDIO: Audio should play from the RIGHT.")
audio.set_pan(100)

time.sleep(2)
print("Testing AUDIO: Audio should play from the CENTER.")
audio.set_pan(0)

time.sleep(2)
print("Testing AUDIO: Audio should STOP.")
audio.stop()

#####################################

def EffectApplicator(effect):
    print("Playing WITH effect")
    audio.add_effect(effect)
    audio.play(blocking=False)
    time.sleep(2)
    audio.stop()
    audio.remove_effect(effect)
    print("Playing WITHOUT effect")
    audio.play(blocking=False)
    time.sleep(2)
    audio.stop()

print("WARNING: NEXT THE AUDIO EFFECTS ARE BEING TESTED, THIS MAY CAUSE AUDITORY DISTRESS!!!")

time.sleep(5)

print("Testing BITCRUSH")
effect = pmma.BitCrush()
print("Testing BITCRUSH: Set Bit-Depth")
effect.set_bit_depth(4)

print("Applying effect to audio")
EffectApplicator(effect)
print("Resetting.")

print("Testing BITCRUSH: Quit")
effect.quit()

print("Testing CHORUS")
effect = pmma.Chorus()
print("Testing CHORUS: Set-Center-Delay")
effect.set_center_delay(10)
print("Testing CHORUS: Set-Mix")
effect.set_mix(100)
print("Testing CHORUS: Set-Depth")
effect.set_depth(100)
print("Testing CHORUS: Set-Rate")
effect.set_rate(100)
print("Testing CHORUS: Set-Feedback")
effect.set_feedback(0)

EffectApplicator(effect)
print("Resetting.")

print("Testing CHORUS: Quit")
effect.quit()
# ...

print("Testing AUDIO: Quit")
audio.quit()

########################################################################

print("All tests ran successfully!")