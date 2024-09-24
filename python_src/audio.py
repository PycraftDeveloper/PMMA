import threading as _threading

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
import waiting as _waiting

class Audio:
    def __init__(self):
        self._input_audio = None
        self._sample_rate = None
        self._audio_loaded = False
        self._effects_list = []
        self._start_frame = 0
        self._paused = False
        self._stop_signal = False
        self._playback_thread = None

    def load_from_file(self, file_path):
        self._input_audio, self._sample_rate = _sound_file.read(file_path)
        self._audio_loaded = True

    def add_effect(self, effect):
        self._effects_list.append(effect)

    def play(self, blocking=True):
        if self._audio_loaded:
            self._effects = _Pedalboard(self._effects_list)
            self._paused = False
            self._stop_signal = False

            if blocking:
                # Start playback in the current thread (blocking)
                self._start_playback()
            else:
                # Start playback in a separate thread (non-blocking)
                self._playback_thread = _threading.Thread(target=self._start_playback)
                self._playback_thread.daemon = True
                self._playback_thread.start()

    def play_in_background(self):
        self.play(blocking=False)

    def play_in_foreground(self):
        self.play(blocking=True)

    def _wait_for_chunk_to_play(self):
        return not (self._start_frame < len(self._input_audio) and not self._stop_signal)

    def _start_playback(self):
        # Start the audio stream
        with _sound_device.OutputStream(callback=self._audio_callback, samplerate=self._sample_rate, channels=self._input_audio.shape[1]):
            # Loop while playback is ongoing and not stopped
            _waiting.wait(self._wait_for_chunk_to_play)

    def _audio_callback(self, outdata, frames, time, status):
        if status:
            print(status)

        if self._paused or self._stop_signal:
            # Output silence if paused or stopped
            outdata[:] = _numpy.zeros(outdata.shape)
            return

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

    def pause(self):
        self._paused = True

    def resume(self):
        if self._paused:
            self._paused = False

    def stop(self):
        self._stop_signal = True
        self._start_frame = 0  # Reset the playback position

    def is_playing(self):
        return self._playback_thread is not None and self._playback_thread.is_alive()

class BitCrush(_Bitcrush):
    def __init__(self, bit_depth=8):
        super().__init__(bit_depth=bit_depth)

    def set_bit_depth(self, bit_depth):
        self.bit_depth = bit_depth

    def get_bit_depth(self):
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

class Clipping(_Clipping):
    def __init__(self, threshold_db=-6):
        super().__init__(threshold_db=threshold_db)

    def set_threshold(self, threshold_db):
        self.threshold_db = threshold_db

    def get_threshold(self):
        return self.threshold_db

class Compressor(_Compressor):
    def __init__(self, threshold_db=0, ratio=4, attack_ms=1, release_ms=100):
        super().__init__(threshold_db=threshold_db, ratio=ratio, attack_ms=attack_ms, release_ms=release_ms)

    def set_threshold(self, threshold_db):
        self.threshold_db = threshold_db

    def get_threshold(self):
        return self.threshold_db

    def set_ratio(self, ratio):
        self.ratio = ratio

    def get_ratio(self):
        return self.ratio

    def set_attack_ms(self, attack_ms):
        self.attack_ms = attack_ms

    def get_attack_ms(self):
        return self.attack_ms

    def set_release_ms(self, release_ms):
        self.release_ms = release_ms

    def get_release_ms(self):
        return self.release_ms

class Convolution(_Convolution):
    def __init__(self, impulse_response_filename, mix=1, sample_rate=None):
        super().__init__(impulse_response_filename=impulse_response_filename, mix=mix, sample_rate=sample_rate)

    def set_impulse_response_filename(self, impulse_response):
        self.impulse_response = impulse_response

    def get_impulse_response_filename(self):
        return self.impulse_response

    def set_mix(self, mix):
        self.mix = mix

    def get_mix(self):
        return self.mix

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        return self.sample_rate

class Delay(_Delay):
    def __init__(self, delay_seconds=0.5, feedback=0, mix=0.5):
        super().__init__(delay_seconds=delay_seconds, feedback=feedback, mix=mix)

    def set_delay_seconds(self, delay_seconds):
        self.delay_seconds = delay_seconds

    def get_delay_seconds(self):
        return self.delay_seconds

    def set_feedback(self, feedback):
        self.feedback = feedback

    def get_feedback(self):
        return self.feedback

    def set_mix(self, mix):
        self.mix = mix

    def get_mix(self):
        return self.mix

class Distortion(_Distortion):
    def __init__(self, drive_db=10):
        super().__init__(drive_db=drive_db)

    def set_drive(self, drive_db):
        self.drive_db = drive_db

    def get_drive(self):
        return self.drive_db

class GSMFullRateCompressor(_GSMFullRateCompressor):
    def __init__(self):
        super().__init__()

class Gain(_Gain):
    def __init__(self, gain_db=1):
        super().__init__(gain_db=gain_db)

    def set_gain(self, gain_db):
        self.gain_db = gain_db

    def get_gain(self):
        return self.gain_db

class HighShelfFilter(_HighShelfFilter):
    def __init__(self, cutoff_hz=440, gain_db=0, q=0.7071067690849304):
        super().__init__(cutoff_hz=cutoff_hz, gain_db=gain_db, q=q)

    def set_cutoff(self, cutoff_hz):
        self.cutoff_hz = cutoff_hz

    def get_cutoff(self):
        return self.cutoff_hz

    def set_gain(self, gain_db):
        self.gain_db = gain_db

    def get_gain(self):
        return self.gain_db

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

class HighPassFilter(_HighpassFilter):
    def __init__(self, cutoff_hz=50):
        super().__init__(cutoff_hz=cutoff_hz)

    def set_cutoff(self, cutoff_hz):
        self.cutoff_hz = cutoff_hz

    def get_cutoff(self):
        return self.cutoff_hz

class LadderFilter(_LadderFilter):
    def __init__(self, cutoff_hz=200, resonance=0, drive=1):
        super().__init__(cutoff_hz=cutoff_hz, resonance=resonance, drive=drive)

    def set_cutoff(self, cutoff_hz):
        self.cutoff_hz = cutoff_hz

    def get_cutoff(self):
        return self.cutoff_hz

    def set_resonance(self, resonance):
        self.resonance = resonance

    def get_resonance(self):
        return self.resonance

    def set_drive(self, drive):
        self.drive = drive

    def get_drive(self):
        return self.drive

class Limiter(_Limiter):
    def __init__(self, threshold_db=-10, release_ms=100):
        super().__init__(threshold_db=threshold_db, release_ms=release_ms)

    def set_threshold(self, threshold_db):
        self.threshold_db = threshold_db

    def get_threshold(self):
        return self.threshold_db

    def set_release_ms(self, release_ms):
        self.release_ms = release_ms

    def get_release_ms(self):
        return self.release_ms

class LowShelfFilter(_LowShelfFilter):
    def __init__(self, cutoff_hz=440, gain_db=0, q=0.7071067690849304):
        super().__init__(cutoff_hz=cutoff_hz, gain_db=gain_db, q=q)

    def set_cutoff(self, cutoff_hz):
        self.cutoff_hz = cutoff_hz

    def get_cutoff(self):
        return self.cutoff_hz

    def set_gain(self, gain_db):
        self.gain_db = gain_db

    def get_gain(self):
        return self.gain_db

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

class LowPassFilter(_LowpassFilter):
    def __init__(self, cutoff_hz=50):
        super().__init__(cutoff_hz=cutoff_hz)

    def set_cutoff(self, cutoff_hz):
        self.cutoff_hz = cutoff_hz

    def get_cutoff(self):
        return self.cutoff_hz

class MP3Compressor(_MP3Compressor):
    def __init__(self, vbr_quality=3):
        super().__init__(vbr_quality=vbr_quality)

    def set_vbr_quality(self, vbr_quality):
        self.vbr_quality = vbr_quality

    def get_vbr_quality(self):
        return self.vbr_quality

class NoiseGate(_NoiseGate):
    def __init__(self, threshold_db=-100, ratio=10, attack_ms=1, release_ms=100):
        super().__init__(threshold_db=threshold_db, ratio=ratio, attack_ms=attack_ms, release_ms=release_ms)

    def set_threshold(self, threshold_db):
        self.threshold_db = threshold_db

    def get_threshold(self):
        return self.threshold_db

    def set_ratio(self, ratio):
        self.ratio = ratio

    def get_ratio(self):
        return self.ratio

    def set_attack_ms(self, attack_ms):
        self.attack_ms = attack_ms

    def get_attack_ms(self):
        return self.attack_ms

    def set_release_ms(self, release_ms):
        self.release_ms = release_ms

    def get_release_ms(self):
        return self.release_ms

class PeakFilter(_PeakFilter):
    def __init__(self, frequency_hz=1000, gain_db=0, q=0.7071067690849304):
        super().__init__(frequency_hz=frequency_hz, gain_db=gain_db, q=q)

    def set_frequency(self, frequency_hz):
        self.frequency_hz = frequency_hz

    def get_frequency(self):
        return self.frequency_hz

    def set_gain(self, gain_db):
        self.gain_db = gain_db

    def get_gain(self):
        return self.gain_db

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

class Phaser(_Phaser):
    def __init__(self, rate_hz=1, depth=0.5, center_frequency_hz=1300, feedback=0, mix=0.5):
        super().__init__(rate_hz=rate_hz, depth=depth, centre_frequency_hz=center_frequency_hz, feedback=feedback, mix=mix)

    def set_rate(self, rate_hz):
        self.rate_hz = rate_hz

    def get_rate(self):
        return self.rate_hz

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

    def set_center_frequency(self, center_frequency_hz):
        self.centre_frequency_hz = center_frequency_hz

    def get_center_frequency(self):
        return self.centre_frequency_hz

    def set_feedback(self, feedback):
        self.feedback = feedback

    def get_feedback(self):
        return self.feedback

    def set_mix(self, mix):
        self.mix = mix

    def get_mix(self):
        return self.mix

class PitchShift(_PitchShift):
    def __init__(self, semitones=0):
        super().__init__(semitones=semitones)

    def set_semitones(self, pitch_shift_semitones):
        self.pitch_shift_semitones = pitch_shift_semitones

    def get_semitones(self):
        return self.pitch_shift_semitones

class ReSample(_Resample):
    def __init__(self, sample_rate=8000):
        super().__init__(sample_rate=sample_rate)

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        return self.sample_rate

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