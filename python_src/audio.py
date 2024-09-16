import sounddevice as _sound_device
import soundfile as _sound_file
from pedalboard import Pedalboard as _Pedalboard
from pedalboard import Bitcrush as _Bitcrush
from pedalboard import Chorus as _Chorus
from pedalboard import Clipping as _Clipping
from pedalboard import Compressor as _Compressor
from pedalboard import Convolution as _Convolution
from pedalboard import Delay as _Delay
from pedalboard import Distortion as _Distortion
from pedalboard import GSMFullRateCompressor as _GSMFullRateCompressor
from pedalboard import Gain as _Gain
from pedalboard import HighShelfFilter as _HighShelfFilter
from pedalboard import HighpassFilter as _HighpassFilter
from pedalboard import LadderFilter as _LadderFilter
from pedalboard import Limiter as _Limiter
from pedalboard import LowShelfFilter as _LowShelfFilter
from pedalboard import LowpassFilter as _LowpassFilter
from pedalboard import MP3Compressor as _MP3Compressor
from pedalboard import NoiseGate as _NoiseGate
from pedalboard import PeakFilter as _PeakFilter
from pedalboard import Phaser as _Phaser
from pedalboard import PitchShift as _PitchShift
from pedalboard import Resample as _Resample
from pedalboard import Reverb as _Reverb
import numpy as _numpy

class Audio:
    def __init__(self):
        self._input_audio = None
        self._sample_rate = None
        self._audio_loaded = False
        self._effects_list = []
        self._start_frame = 0

    def load_from_file(self, file_path):
        self._input_audio, self._sample_rate = _sound_file.read(file_path)
        self._audio_loaded = True

    def add_effect(self, effect):
        self._effects_list.append(effect)

    def play(self):
        if self._audio_loaded:
            self._effects = _Pedalboard(self._effects_list)
            # Start the audio stream
            with _sound_device.OutputStream(callback=self._audio_callback, samplerate=self._sample_rate, channels=self._input_audio.shape[1]):
                _sound_device.sleep(int(len(self._input_audio) / self._sample_rate * 1000))  # Play for the duration of the file

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

class BitCrush(_Bitcrush):
    def __init__(self, bit_depth=8, *args, **kwargs):
        super().__init__(bit_depth=bit_depth, *args, **kwargs)
        self._bit_depth = bit_depth

    def set_bit_depth(self, bit_depth): # from transition manager :)
        self._bit_depth = bit_depth
        self.bit_depth = bit_depth  # Update the internal bit depth of the effect