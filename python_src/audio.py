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
    def __init__(self, bit_depth=8):
        super().__init__(bit_depth=bit_depth)

    def set_bit_depth(self, bit_depth): # from transition manager :)
        self.bit_depth = bit_depth  # Update the internal bit depth of the effect

    def get_bit_depth(self): # from transition manager :)
        return self.bit_depth

class Chorus(_Chorus):
    def __init__(self, rate=1, depth=0.25, center_delay_ms=7, feedback=0, mix=0.5):
        super().__init__(rate_hz=rate, depth=depth, centre_delay_ms=center_delay_ms, feedback=feedback, mix=mix)

    def set_rate(self, rate):
        self.rate_hz = rate

    def get_rate(self):
        return self.rate_hz

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

    def set_center_delay_ms(self, center_delay_ms):
        self.centre_delay_ms = center_delay_ms

    def get_center_delay_ms(self):
        return self.centre_delay_ms

    def set_feedback(self, feedback):
        self.feedback = feedback

    def get_feedback(self):
        return self.feedback

    def set_mix(self, mix):
        self.mix = mix

    def get_mix(self):
        return self.mix

class Reverb(_Reverb):
    def __init__(self, room_size=1, damping=0.5, wet_level=0.33, dry_level=0.4, width=1, freeze_mode=False): # percentages eventually
        super().__init__(room_size=room_size, damping=damping, wet_level=wet_level, dry_level=dry_level, width=width, freeze_mode=freeze_mode)

    def set_room_size(self, room_size):
        self.room_size = room_size

    def get_room_size(self):
        return self.room_size

    def set_damping(self, damping):
        self.damping = damping

    def get_damping(self):
        return self.damping

    def set_wet_level(self, wet_level):
        self.wet_level = wet_level

    def get_wet_level(self):
        return self.wet_level

    def set_dry_level(self, dry_level):
        self.dry_level = dry_level

    def get_dry_level(self):
        return self.dry_level

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_freeze_mode(self, freeze_mode):
        self.freeze_mode = freeze_mode

    def get_freeze_mode(self):
        return self.freeze_mode