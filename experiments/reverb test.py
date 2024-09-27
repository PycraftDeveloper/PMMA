import numpy as np
import sounddevice as sd
import time
import pmma

pmma.init()

# Audio parameters
sample_rate = 44100  # Samples per second
duration = 5  # Duration of the sine wave in seconds
silent_duration = 3  # Duration of silence in seconds
frequency = 220  # Frequency of the sine wave (A3 note)
num_samples = int(sample_rate * duration)

# Generate a sine wave
t = np.linspace(0, duration, num_samples, endpoint=False)
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Initialize the Reverb effect with noticeable parameters
room_size = 90  # Room size (0 to 1)
damping = 80    # Damping factor (0 to 1)
wet_level = 80  # Wet level (0 to 1)
dry_level = 50  # Dry level (0 to 1)
freeze_mode = False

# Create an instance of the Reverb class
reverb = pmma.Reverb(
    room_size=room_size,
    damping=damping,
    wet_level=wet_level,
    dry_level=dry_level,
    freeze_mode=freeze_mode,
)

# Process the audio in chunks to ensure reverb is applied
buffer_size = 1024  # Buffer size
processed_audio = np.zeros(len(sine_wave), dtype=np.float32)

# Process in chunks
for i in range(0, len(sine_wave), buffer_size):
    chunk = sine_wave[i:i + buffer_size]
    processed_chunk = reverb(chunk, sample_rate=sample_rate, buffer_size=buffer_size)
    processed_audio[i:i + buffer_size] = processed_chunk

# Create silence to add to the end
silent_samples = int(sample_rate * silent_duration)
silence = np.zeros(silent_samples)

# Combine processed audio with silence
final_audio = np.concatenate((processed_audio, silence))

# Play the final audio with reverb decay
sd.play(final_audio, samplerate=sample_rate)
sd.wait()  # Wait until the audio is finished playing

# Optionally, keep the program running to listen
time.sleep(duration + silent_duration + 1)  # Sleep to allow time for playback
