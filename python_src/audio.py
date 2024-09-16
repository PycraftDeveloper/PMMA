import sounddevice as sd
import soundfile as sf
from pedalboard import Pedalboard, Delay
from pedalboard.io import AudioFile
import numpy as _numpy

class Audio:
    def __init__(self):
        self._input_audio = None
        self._sample_rate = None
        self._audio_loaded = False
        self._effects = Pedalboard([])
        self._start_frame = 0

    def load_from_file(self, file_path):
        self._input_audio, self._sample_rate = sf.read(file_path)
        self._audio_loaded = True

    def add_effect(self, effect):
        self._effects.append(effect)

    def play(self):
        if self._audio_loaded:
            # Start the audio stream
            with sd.OutputStream(callback=self._audio_callback, samplerate=self._sample_rate, channels=self._input_audio.shape[1]):
                sd.sleep(int(len(self._input_audio) / self._sample_rate * 1000))  # Play for the duration of the file

    def _audio_callback(self, outdata, frames, time, status):
        if status:
            print(status)

        # Slice the input audio correctly based on the frames
        chunk = self._input_audio[self._start_frame:self._start_frame + frames]

        # Ensure the chunk is the correct size
        if len(chunk) < frames:
            chunk = _numpy.pad(chunk, ((0, frames - len(chunk)), (0, 0)), mode='constant')

        # Apply the effects
        processed_audio = self._effects(chunk, self._sample_rate)

        # Output the processed audio
        outdata[:len(processed_audio)] = processed_audio

        self._start_frame += frames