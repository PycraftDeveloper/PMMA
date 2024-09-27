import threading as _threading
import gc as _gc
import queue as _queue

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

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import ProportionConverter as _ProportionConverter

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Audio:
    def __init__(self):
        _initialize(self)

        self._file = None
        self._sample_rate = None
        self._audio_loaded = False
        self._effects_list = []
        self._start_frame = 0
        self._paused = False
        self._stop_signal = False
        self._playback_thread = None
        self._volume = _ProportionConverter()  # Default volume is 100%
        self._volume.set_value(1.0)
        self._pan = _ProportionConverter()  # Pan: -1 (left) to 1 (right), 0 is center
        self._pan.set_value(0.0)
        self._channels = 2
        self._queue_max_size = 600
        self._audio_queue = _queue.Queue(maxsize=self._queue_max_size)
        self._audio_data = None
        self._from_moviepy = False
        self._moviepy_audio_itr = None
        self._queue_maintainer_thread = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._stop_signal = True

            if self._playback_thread is not None:
                self._playback_thread.join()

            if self._queue_maintainer_thread is not None:
                self._queue_maintainer_thread.join()

            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def load_from_file(self, file_path):
        self._file = _sound_file.SoundFile(file_path)
        self._sample_rate = self._file.samplerate
        self._channels = self._file.channels
        self._audio_loaded = True

    def load_from_moviepy(self, audio):
        self._audio_data = audio
        self._sample_rate = audio.fps
        self._channels = audio.nchannels
        self._audio_loaded = True
        self._from_moviepy = True
        self._moviepy_audio_itr = self._audio_generator(2048)

        # Pre-fill the queue with initial chunks
        for _ in range(self._queue_max_size):
            try:
                self._audio_queue.put_nowait(next(self._moviepy_audio_itr))
            except StopIteration:
                break

    def add_effect(self, effect):
        self._effects_list.append(effect)

    def set_volume(self, volume, format=_Constants.PERCENTAGE):
        """Set the volume (0.0 to 1.0)"""
        self._volume.set_value(volume, format=format)

    def set_pan(self, pan, format=_Constants.PERCENTAGE):
        """Set the panning (-1.0 to 1.0, where 0 is center)"""
        self._pan.set_value(pan, format=format)

    def play(self, blocking=True):
        if self._audio_loaded:
            self._effects = _Pedalboard(self._effects_list)
            self._paused = False
            self._stop_signal = False

            if self._from_moviepy:
                self._queue_maintainer_thread = _threading.Thread(target=self._maintain_audio_queue)
                self._queue_maintainer_thread.daemon = True
                self._queue_maintainer_thread.start()

            if blocking:
                # Start playback in the current thread (blocking)
                self._start_playback()
            else:
                # Start playback in a separate thread (non-blocking)
                self._playback_thread = _threading.Thread(target=self._start_playback)
                self._playback_thread.daemon = True
                self._playback_thread.start()

    def _wait_until_queue_running_low(self):
        return self._audio_queue.qsize() < self._queue_max_size

    def _maintain_audio_queue(self):
        while self._stop_signal is False:
            if self._wait_until_queue_running_low():
                try:
                    self._audio_queue.put_nowait(next(self._moviepy_audio_itr))
                except StopIteration:
                    self._moviepy_audio_itr = self._audio_generator(2048)
                    self._audio_queue.put_nowait(next(self._moviepy_audio_itr))

    def _wait_for_chunk_to_play(self):
        return self._stop_signal

    def _start_playback(self):
        # Start the audio stream
        with _sound_device.OutputStream(callback=self._audio_callback, samplerate=self._sample_rate, channels=self._channels, blocksize=2048):
            # Loop while playback is ongoing and not stopped
            _waiting.wait(self._wait_for_chunk_to_play)

    def _audio_generator(self, chunk_size):
        while self._stop_signal is False:
            for chunk in self._audio_data.iter_chunks(fps=self._sample_rate, chunksize=chunk_size):
                yield chunk

    def _audio_callback(self, outdata, frames, time, status):
        if status:
            print(status)

        if self._paused or self._stop_signal:
            outdata[:] = _numpy.zeros(outdata.shape)
            return

        if self._from_moviepy:
            try:
                chunk = self._audio_queue.get_nowait()
            except _queue.Empty:
                outdata.fill(0)

        else:
            chunk = self._file.read(frames, dtype='float32')

        chunk = _numpy.concatenate((chunk, chunk[::-1]))
        chunk = chunk[:frames]

        # Apply volume and panning
        chunk = self._apply_volume_and_pan(chunk)

        # Apply effects
        processed_audio = self._effects(chunk, self._sample_rate)

        # Output the processed audio
        outdata[:] = processed_audio

        self._start_frame += frames

    def _apply_volume_and_pan(self, chunk):
        """Apply volume and panning to the chunk of audio"""
        chunk = chunk * self._volume.get_value()

        if self._channels == 2:  # Stereo audio
            left = 1 - max(self._pan.get_value(), 0)  # Reduce left channel when panning right
            right = 1 - max(-self._pan.get_value(), 0)  # Reduce right channel when panning left
            chunk[:, 0] *= left
            chunk[:, 1] *= right
        return chunk

    def pause(self):
        self._paused = True

    def resume(self):
        if self._paused:
            self._paused = False

    def stop(self):
        self._stop_signal = True
        self._start_frame = 0  # Reset playback position

    def get_playing(self):
        return self._playback_thread is not None and self._playback_thread.is_alive()

class BitCrush(_Bitcrush):
    def __init__(self, bit_depth=8):
        _initialize(self)

        super().__init__(bit_depth=bit_depth)

    def set_bit_depth(self, bit_depth):
        self.bit_depth = bit_depth

    def get_bit_depth(self):
        return self.bit_depth

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Chorus(_Chorus):
    def __init__(
            self,
            rate=1,
            depth=25,
            center_delay=0.007,
            feedback=0,
            mix=50,
            format=_Constants.PERCENTAGE,
            depth_format=None,
            feedback_format=None,
            mix_format=None):

        _initialize(self)

        if depth_format is None:
            depth_format = format
        if feedback_format is None:
            feedback_format = format
        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_depth = _ProportionConverter()
        self._proportion_adjusted_depth.set_value(depth, format=depth_format)
        self._proportion_adjusted_feedback = _ProportionConverter()
        self._proportion_adjusted_feedback.set_value(feedback, format=feedback_format)
        self._proportion_adjusted_mix = _ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            rate_hz=rate,
            depth=self._proportion_adjusted_depth.get_value(format=_Constants.DECIMAL),
            centre_delay_ms=center_delay * 1000, # s to ms
            feedback=self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL),
            mix=self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL))

    def set_rate(self, rate):
        self.rate_hz = rate

    def get_rate(self):
        return self.rate_hz

    def set_depth(self, depth, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_depth.set_value(depth, format=format)
        self.depth = self._proportion_adjusted_depth.get_value(format=_Constants.DECIMAL)

    def get_depth(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_depth.get_value(format=format)

    def set_center_delay(self, center_delay):
        self.centre_delay_ms = center_delay * 1000

    def get_center_delay(self):
        return self.centre_delay_ms / 1000

    def set_feedback(self, feedback, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_feedback.set_value(feedback, format=format)
        self.feedback = self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL)

    def get_feedback(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_feedback.get_value(format=format)

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def get_mix(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_mix.get_value(format=format)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Clipping(_Clipping):
    def __init__(self, threshold=-6):
        _initialize(self)

        super().__init__(threshold_db=threshold)

    def set_threshold(self, threshold):
        self.threshold_db = threshold

    def get_threshold(self):
        return self.threshold_db

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Compressor(_Compressor):
    def __init__(
            self,
            threshold=0,
            ratio=4,
            attack=0.001,
            release=0.1):

        _initialize(self)

        super().__init__(
            threshold_db=threshold,
            ratio=ratio,
            attack_ms=attack * 1000,
            release_ms=release * 1000)

    def set_threshold(self, threshold):
        self.threshold_db = threshold

    def get_threshold(self):
        return self.threshold_db

    def set_ratio(self, ratio):
        self.ratio = ratio

    def get_ratio(self):
        return self.ratio

    def set_attack(self, attack):
        self.attack_ms = attack * 1000

    def get_attack(self):
        return self.attack_ms / 1000

    def set_release(self, release):
        self.release_ms = release * 1000

    def get_release(self):
        return self.release_ms / 1000

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Convolution(_Convolution):
    def __init__(
            self,
            impulse_response_filename,
            mix=100,
            sample_rate=None,
            format=_Constants.PERCENTAGE,
            mix_format=None):

        _initialize(self)

        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_mix = _ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            impulse_response_filename=impulse_response_filename,
            mix=self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL),
            sample_rate=sample_rate)

    def set_impulse_response_filename(self, impulse_response):
        self.impulse_response = impulse_response

    def get_impulse_response_filename(self):
        return self.impulse_response

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def get_mix(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_mix.get_value(format=format)

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        return self.sample_rate

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Delay(_Delay):
    def __init__(
            self,
            delay=0.5,
            feedback=0,
            mix=50,
            format=_Constants.PERCENTAGE,
            feedback_format=None,
            mix_format=None):

        _initialize(self)

        if feedback_format is None:
            feedback_format = format
        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_feedback = _ProportionConverter()
        self._proportion_adjusted_feedback.set_value(feedback, format=feedback_format)
        self._proportion_adjusted_mix = _ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            delay_seconds=delay,
            feedback=self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL),
            mix=self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL))

    def set_delay(self, delay):
        self.delay_seconds = delay

    def get_delay(self):
        return self.delay_seconds

    def set_feedback(self, feedback, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_feedback.set_value(feedback, format=format)
        self.feedback = self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL)

    def get_feedback(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_feedback.get_value(format=format)

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def get_mix(self):
        return self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Distortion(_Distortion):
    def __init__(self, drive=10):
        _initialize(self)

        super().__init__(drive_db=drive)

    def set_drive(self, drive):
        self.drive_db = drive

    def get_drive(self):
        return self.drive_db

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class GSMFullRateCompressor(_GSMFullRateCompressor):
    def __init__(self):
        _initialize(self)

        super().__init__()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Gain(_Gain):
    def __init__(self, gain=1):
        _initialize(self)

        super().__init__(gain_db=gain)

    def set_gain(self, gain):
        self.gain_db = gain

    def get_gain(self):
        return self.gain_db

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class HighShelfFilter(_HighShelfFilter):
    def __init__(self, cutoff=440, gain=0, q=0.7071067690849304):
        _initialize(self)

        super().__init__(cutoff_hz=cutoff, gain_db=gain, q=q)

    def set_cutoff(self, cutoff):
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        return self.cutoff_hz

    def set_gain(self, gain):
        self.gain_db = gain

    def get_gain(self):
        return self.gain_db

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class HighPassFilter(_HighpassFilter):
    def __init__(self, cutoff=50):
        _initialize(self)

        super().__init__(cutoff_hz=cutoff)

    def set_cutoff(self, cutoff):
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        return self.cutoff_hz

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class LadderFilter(_LadderFilter):
    def __init__(self, cutoff=200, resonance=0, drive=1):
        _initialize(self)

        super().__init__(cutoff_hz=cutoff, resonance=resonance, drive=drive)

    def set_cutoff(self, cutoff):
        self.cutoff_hz = cutoff

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

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Limiter(_Limiter):
    def __init__(self, threshold=-10, release=0.1):
        _initialize(self)

        super().__init__(threshold_db=threshold, release_ms=release / 1000)

    def set_threshold(self, threshold):
        self.threshold_db = threshold

    def get_threshold(self):
        return self.threshold_db

    def set_release(self, release):
        self.release_ms = release * 1000

    def get_release(self):
        return self.release_ms / 1000

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class LowShelfFilter(_LowShelfFilter):
    def __init__(self, cutoff=440, gain=0, q=0.7071067690849304):
        _initialize(self)

        super().__init__(cutoff_hz=cutoff, gain_db=gain, q=q)

    def set_cutoff(self, cutoff):
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        return self.cutoff_hz

    def set_gain(self, gain):
        self.gain_db = gain

    def get_gain(self):
        return self.gain_db

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class LowPassFilter(_LowpassFilter):
    def __init__(self, cutoff=50):
        _initialize(self)

        super().__init__(cutoff_hz=cutoff)

    def set_cutoff(self, cutoff):
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        return self.cutoff_hz

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class MP3Compressor(_MP3Compressor):
    def __init__(self, vbr_quality=3):
        _initialize(self)

        super().__init__(vbr_quality=vbr_quality)

    def set_vbr_quality(self, vbr_quality):
        self.vbr_quality = vbr_quality

    def get_vbr_quality(self):
        return self.vbr_quality

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class NoiseGate(_NoiseGate):
    def __init__(
            self,
            threshold=-100,
            ratio=10,
            attack=0.001,
            release=0.1):

        _initialize(self)

        super().__init__(
            threshold_db=threshold,
            ratio=ratio,
            attack_ms=attack * 1000,
            release_ms=release * 1000)

    def set_threshold(self, threshold):
        self.threshold_db = threshold

    def get_threshold(self):
        return self.threshold_db

    def set_ratio(self, ratio):
        self.ratio = ratio

    def get_ratio(self):
        return self.ratio

    def set_attack(self, attack):
        self.attack_ms = attack * 1000

    def get_attack(self):
        return self.attack_ms / 1000

    def set_release(self, release):
        self.release_ms = release * 1000

    def get_release(self):
        return self.release_ms / 1000

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class PeakFilter(_PeakFilter):
    def __init__(self, frequency=1000, gain=0, q=0.7071067690849304):
        _initialize(self)

        super().__init__(frequency_hz=frequency, gain_db=gain, q=q)

    def set_frequency(self, frequency):
        self.frequency_hz = frequency

    def get_frequency(self):
        return self.frequency_hz

    def set_gain(self, gain):
        self.gain_db = gain

    def get_gain(self):
        return self.gain_db

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Phaser(_Phaser):
    def __init__(
            self,
            rate=1,
            depth=50,
            center_frequency=1300,
            feedback=0,
            mix=50,
            format=_Constants.PERCENTAGE,
            depth_format=None,
            feedback_format=None,
            mix_format=None):

        _initialize(self)

        if depth_format is None:
            depth_format = format
        if feedback_format is None:
            feedback_format = format
        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_depth = _ProportionConverter()
        self._proportion_adjusted_depth.set_value(depth, format=depth_format)
        self._proportion_adjusted_feedback = _ProportionConverter()
        self._proportion_adjusted_feedback.set_value(feedback, format=feedback_format)
        self._proportion_adjusted_mix = _ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            rate_hz=rate,
            depth=self._proportion_adjusted_depth.get_value(_Constants.DECIMAL),
            centre_frequency_hz=center_frequency,
            feedback=self._proportion_adjusted_feedback.get_value(_Constants.DECIMAL),
            mix=self._proportion_adjusted_mix.get_value(_Constants.DECIMAL))

    def set_rate(self, rate):
        self.rate_hz = rate

    def get_rate(self):
        return self.rate_hz

    def set_depth(self, depth, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_depth.set_value(depth, format=format)
        self.depth = self._proportion_adjusted_depth.get_value(_Constants.DECIMAL)

    def get_depth(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_depth.get_value(format=format)

    def set_center_frequency(self, center_frequency):
        self.centre_frequency_hz = center_frequency

    def get_center_frequency(self):
        return self.centre_frequency_hz

    def set_feedback(self, feedback, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_feedback.set_value(feedback, format=format)
        self.feedback = self._proportion_adjusted_feedback.get_value(_Constants.DECIMAL)

    def get_feedback(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_feedback.get_value(format=format)

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(_Constants.DECIMAL)

    def get_mix(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_mix.get_value(format=format)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class PitchShift(_PitchShift):
    def __init__(self, semitones=0):
        _initialize(self)

        super().__init__(semitones=semitones)

    def set_semitones(self, pitch_shift_semitones):
        self.pitch_shift_semitones = pitch_shift_semitones

    def get_semitones(self):
        return self.pitch_shift_semitones

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class ReSample(_Resample):
    def __init__(self, sample_rate=8000):
        _initialize(self)

        super().__init__(sample_rate=sample_rate)

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        return self.sample_rate

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class Reverb(_Reverb):
    def __init__(
            self,
            room_size=100,
            damping=50,
            wet_level=33,
            dry_level=40,
            width=100,
            freeze_mode=False,
            format=_Constants.PERCENTAGE,
            room_size_format=None,
            damping_format=None,
            wet_level_format=None,
            dry_level_format=None,
            width_format=None):

        _initialize(self)

        if room_size_format is None:
            room_size_format = format
        if damping_format is None:
            damping_format = format
        if wet_level_format is None:
            wet_level_format = format
        if dry_level_format is None:
            dry_level_format = format
        if width_format is None:
            width_format = format

        self._proportion_adjusted_room_size = _ProportionConverter()
        self._proportion_adjusted_room_size.set_value(room_size, format=room_size_format)
        self._proportion_adjusted_damping = _ProportionConverter()
        self._proportion_adjusted_damping.set_value(damping, format=damping_format)
        self._proportion_adjusted_wet_level = _ProportionConverter()
        self._proportion_adjusted_wet_level.set_value(wet_level, format=wet_level_format)
        self._proportion_adjusted_dry_level = _ProportionConverter()
        self._proportion_adjusted_dry_level.set_value(dry_level, format=dry_level_format)
        self._proportion_adjusted_width = _ProportionConverter()
        self._proportion_adjusted_width.set_value(width, format=width_format)

        super().__init__(
            room_size=self._proportion_adjusted_room_size.get_value(_Constants.DECIMAL),
            damping=self._proportion_adjusted_damping.get_value(_Constants.DECIMAL),
            wet_level=self._proportion_adjusted_wet_level.get_value(_Constants.DECIMAL),
            dry_level=self._proportion_adjusted_dry_level.get_value(_Constants.DECIMAL),
            width=self._proportion_adjusted_width.get_value(_Constants.DECIMAL),
            freeze_mode=freeze_mode)

    def set_room_size(self, room_size, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_room_size.set_value(room_size, format=format)
        self.room_size = self._proportion_adjusted_room_size.get_value(_Constants.DECIMAL)

    def get_room_size(self):
        return self._proportion_adjusted_room_size.get_value(_Constants.PERCENTAGE)

    def set_damping(self, damping, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_damping.set_value(damping, format=format)
        self.damping = self._proportion_adjusted_damping.get_value(_Constants.DECIMAL)

    def get_damping(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_damping.get_value(format=format)

    def set_wet_level(self, wet_level, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_wet_level.set_value(wet_level, format=format)
        self.wet_level = self._proportion_adjusted_wet_level.get_value(_Constants.DECIMAL)

    def get_wet_level(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_wet_level.get_value(format=format)

    def set_dry_level(self, dry_level, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_dry_level.set_value(dry_level, format=format)
        self.dry_level = self._proportion_adjusted_dry_level.get_value(_Constants.DECIMAL)

    def get_dry_level(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_dry_level.get_value(format=format)

    def set_width(self, width, format=_Constants.PERCENTAGE):
        self._proportion_adjusted_width.set_value(width, format=format)
        self.width = self._proportion_adjusted_width.get_value(_Constants.DECIMAL)

    def get_width(self, format=_Constants.PERCENTAGE):
        return self._proportion_adjusted_width.get_value(format=format)

    def set_freeze_mode(self, freeze_mode):
        self.freeze_mode = freeze_mode

    def get_freeze_mode(self):
        return self.freeze_mode

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True