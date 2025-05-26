from pedalboard import Pedalboard as _pedalboard__Pedalboard
from pedalboard import Bitcrush as _pedalboard__Bitcrush
from pedalboard import Chorus as _pedalboard__Chorus
from pedalboard import Clipping as _pedalboard__Clipping
from pedalboard import Compressor as _pedalboard__Compressor
from pedalboard import Convolution as _pedalboard__Convolution
from pedalboard import Delay as _pedalboard__Delay
from pedalboard import Distortion as _pedalboard__Distortion
from pedalboard import GSMFullRateCompressor as _pedalboard__GSMFullRateCompressor
from pedalboard import Gain as _pedalboard__Gain
from pedalboard import HighShelfFilter as _pedalboard__HighShelfFilter
from pedalboard import HighpassFilter as _pedalboard__HighpassFilter
from pedalboard import LadderFilter as _pedalboard__LadderFilter
from pedalboard import Limiter as _pedalboard__Limiter
from pedalboard import LowShelfFilter as _pedalboard__LowShelfFilter
from pedalboard import LowpassFilter as _pedalboard__LowpassFilter
from pedalboard import MP3Compressor as _pedalboard__MP3Compressor
from pedalboard import NoiseGate as _pedalboard__NoiseGate
from pedalboard import PeakFilter as _pedalboard__PeakFilter
from pedalboard import Phaser as _pedalboard__Phaser
from pedalboard import PitchShift as _pedalboard__PitchShift
from pedalboard import Resample as _pedalboard__Resample
from pedalboard import Reverb as _pedalboard__Reverb

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Audio:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._threading__module = _ModuleManager.import_module("threading")
        self._queue__module = _ModuleManager.import_module("queue")
        self._time__module = _ModuleManager.import_module("time")

        self._soundfile__module = _ModuleManager.import_module("soundfile")
        self._sounddevice__module = _ModuleManager.import_module("sounddevice")
        self._waiting__module = _ModuleManager.import_module("waiting")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        self._file = None
        self._sample_rate = None
        self._audio_loaded = False
        self._effects_list = []
        self._paused = False
        self._stop_signal = False
        self._playback_thread = None
        self._channels = 2
        self._queue_max_size = 60
        self._audio_queue = self._queue__module.Queue(maxsize=self._queue_max_size)
        self._audio_data = None
        self._from_moviepy = False
        self._moviepy_audio_itr = None

        self._volume = self._number_converter__module.ProportionConverter()  # Default volume is 100%
        self._volume.set_value(1.0)
        self._pan = self._number_converter__module.ProportionConverter()  # Pan: -1 (left) to 1 (right), 0 is center
        self._pan.set_value(0.0)

        self._playing = False
        self._logger = self._logging_utils__module.InternalLogger()
        self._first_run = True

        self._looping = False
        self._audio_duration = None
        self._audio_playing_start_time = None

        self._custom_audio_callback_pre_effects = None
        self._custom_audio_callback_post_effects = None

        self._custom_audio_callback_pre_effects_results = None
        self._custom_audio_callback_post_effects_results = None

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._stop_signal = True

            if self._playback_thread is not None:
                self._playback_thread.join()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def set_custom_audio_callback_function_pre_effects(self, function=None):
        """
        🟩 **R** -
        """
        self._custom_audio_callback_pre_effects = function

    def set_custom_audio_callback_function_post_effects(self, function=None):
        """
        🟩 **R** -
        """
        self._custom_audio_callback_post_effects = function

    def get_custom_audio_callback_function_pre_effects_results(self):
        """
        🟩 **R** -
        """
        return self._custom_audio_callback_pre_effects_results

    def get_custom_audio_callback_function_post_effects_results(self):
        """
        🟩 **R** -
        """
        return self._custom_audio_callback_post_effects_results

    def load_from_file(self, file_path):
        """
        🟩 **R** -
        """
        self._file = self._soundfile__module.SoundFile(file_path)
        self._sample_rate = self._file.samplerate
        self._channels = self._file.channels
        self._audio_duration = self._file.frames / self._sample_rate
        self._audio_loaded = True

    def get_sample_rate(self):
        """
        🟩 **R** -
        """
        return self._sample_rate

    def get_number_of_channels(self):
        """
        🟩 **R** -
        """
        return self._channels

    def set_looping(self, loop):
        """
        🟩 **R** -
        """
        self._looping = loop

    def get_looping(self):
        """
        🟩 **R** -
        """
        return self._looping

    def set_duration(self, duration):
        """
        🟩 **R** -
        """
        self._audio_duration = duration

    def set_silence_at_end_of_track(self, duration):
        """
        🟩 **R** -
        """
        self._audio_duration += duration

    def load_from_moviepy(self, audio):
        """
        🟩 **R** -
        """
        self._audio_data = audio
        self._sample_rate = audio.fps
        self._channels = audio.nchannels
        self._audio_loaded = True
        self._from_moviepy = True
        self._moviepy_audio_itr = self._audio_generator(2048)

        self._looping = True

        # Pre-fill the queue with initial chunks
        for _ in range(self._queue_max_size):
            try:
                self._audio_queue.put_nowait(next(self._moviepy_audio_itr))
            except StopIteration:
                break

    def add_effect(self, effect):
        """
        🟩 **R** -
        """
        self._effects_list.append(effect)

    def remove_effect(self, effect):
        """
        🟩 **R** -
        """
        self._effects_list.remove(effect)

    def set_volume(self, volume, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._volume.set_value(volume, format=format)

    def set_pan(self, pan, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._pan.set_value(pan, format=format)

    def play(self, blocking=True, delay=0):
        """
        🟩 **R** -
        """
        if self._audio_loaded:
            if self._playing:
                self._logger.log_development("You have attempted to play audio \
that's already playing. We will therefore ignore your request to prevent unexpected audio behavior.")

                return False
            if delay != 0:
                self._time__module.sleep(delay)
            self._effects = _pedalboard__Pedalboard(self._effects_list)
            self._paused = False
            self._stop_signal = False
            self._first_run = True

            self._playing = True

            if blocking:
                # Start playback in the current thread (blocking)
                self._start_playback()
            else:
                # Start playback in a separate thread (non-blocking)
                self._playback_thread = self._threading__module.Thread(target=self._start_playback)
                self._playback_thread.daemon = True
                self._playback_thread.name = "Audio:Playing_Audio_Thread"
                self._playback_thread.start()
            return True

    def _wait_for_chunk_to_play(self):
        """
        🟩 **R** -
        """
        return self._stop_signal

    def _start_playback(self):
        """
        🟩 **R** -
        """
        self._file.seek(0)
        # Start the audio stream
        with self._sounddevice__module.OutputStream(callback=self._audio_callback, samplerate=self._sample_rate, channels=self._channels, blocksize=2048):
            # Loop while playback is ongoing and not stopped
            self._waiting__module.wait(self._wait_for_chunk_to_play)

        self._audio_playing_start_time = None
        self._file.seek(0)

    def _audio_generator(self, chunk_size):
        """
        🟩 **R** -
        """
        buffer = self._numpy__module.empty((0, self._channels), dtype='float32')  # Buffer to store leftover samples

        while self._stop_signal is False:
            for chunk in self._audio_data.iter_chunks(fps=self._sample_rate, chunksize=chunk_size):
                # Add the new chunk to the buffer
                buffer = self._numpy__module.vstack([buffer, chunk])

                # Keep yielding exact-sized chunks from the buffer
                while len(buffer) >= chunk_size:
                    # Yield a chunk of the requested size
                    yield buffer[:chunk_size]
                    # Remove the yielded chunk from the buffer
                    buffer = buffer[chunk_size:]

            # If stop signal is raised or no more chunks, yield remaining data in buffer
            if len(buffer) > 0:
                yield buffer
                break

    def _audio_callback(self, outdata, frames, time, status):
        """
        🟩 **R** -
        """
        if self._audio_playing_start_time is None:
            self._audio_playing_start_time = self._time__module.perf_counter()

        if status:
            print(status)

        if self._paused or self._stop_signal or status:
            outdata[:] = self._numpy__module.zeros(outdata.shape)
            if self._custom_audio_callback_pre_effects is not None:
                self._custom_audio_callback_pre_effects_results = self._custom_audio_callback_pre_effects(outdata, frames, time, status)
                self._custom_audio_callback_post_effects_results = self._custom_audio_callback_post_effects(outdata, frames, time, status)
            return

        if self._from_moviepy:
            try:
                chunk = self._audio_queue.get_nowait()
                self._audio_queue.put_nowait(next(self._moviepy_audio_itr))
            except StopIteration:
                if self._looping:
                    self._moviepy_audio_itr = self._audio_generator(2048)
                    self._audio_queue.put_nowait(next(self._moviepy_audio_itr))
            except self._queue__module.Empty:
                if self._looping:
                    outdata.fill(0)
                else:
                    self._stop_signal = True
                    outdata[:] = self._numpy__module.zeros(outdata.shape)
                    if self._custom_audio_callback_pre_effects is not None:
                        self._custom_audio_callback_pre_effects_results = self._custom_audio_callback_pre_effects(outdata, frames, time, status)
                        self._custom_audio_callback_post_effects_results = self._custom_audio_callback_post_effects(outdata, frames, time, status)
                    return

        else:
            chunk = self._file.read(frames, dtype='float32')

            if self._time__module.perf_counter() - self._audio_playing_start_time > self._audio_duration:
                if self._looping:
                    self._file.seek(0)
                    self._audio_playing_start_time = None
                else:
                    self._stop_signal = True

        if len(chunk) < frames:
            padding_shape = (frames - len(chunk), chunk.shape[1])
            chunk = self._numpy__module.pad(chunk, ((0, padding_shape[0]), (0, 0)), mode='constant')

        if self._custom_audio_callback_pre_effects is not None:
            self._custom_audio_callback_pre_effects_results = self._custom_audio_callback_pre_effects(outdata, frames, time, status)

        # Apply volume and panning
        chunk = self._apply_volume_and_pan(chunk)

        # Apply effects
        processed_audio = self._effects(chunk, self._sample_rate, reset=self._first_run)

        # Output the processed audio
        outdata[:] = processed_audio

        if self._custom_audio_callback_post_effects is not None:
            self._custom_audio_callback_post_effects_results = self._custom_audio_callback_post_effects(outdata, frames, time, status)

        self._first_run = False

    def _apply_volume_and_pan(self, chunk):
        """
        🟩 **R** - Apply volume and panning to the chunk of audio
        """
        chunk = chunk * self._volume.get_value()

        if self._channels == 2:  # Stereo audio
            left = 1 - max(self._pan.get_value(), 0)  # Reduce left channel when panning right
            right = 1 - max(-self._pan.get_value(), 0)  # Reduce right channel when panning left
            chunk[:, 0] *= left
            chunk[:, 1] *= right
        return chunk

    def pause(self):
        """
        🟩 **R** -
        """
        self._paused = True

    def resume(self):
        """
        🟩 **R** -
        """
        if self._paused:
            self._paused = False

    def stop(self):
        """
        🟩 **R** -
        """
        self._stop_signal = True
        if self._playback_thread is not None: # wait until playback actually stops
            self._playback_thread.join()
        self._playing = False

    def get_paused(self):
        """
        🟩 **R** -
        """
        return self._paused

    def get_playing(self):
        """
        🟩 **R** -
        """
        return self._playing

class BitCrush(_pedalboard__Bitcrush):
    """
    🟩 **R** -
    """
    def __init__(self, bit_depth=8):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(bit_depth=bit_depth)

    def set_bit_depth(self, bit_depth):
        """
        🟩 **R** -
        """
        self.bit_depth = bit_depth

    def get_bit_depth(self):
        """
        🟩 **R** -
        """
        return self.bit_depth

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Chorus(_pedalboard__Chorus):
    """
    🟩 **R** -
    """
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
        """
        🟩 **R** -
        """

        _initialize(self)

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")

        if depth_format is None:
            depth_format = format
        if feedback_format is None:
            feedback_format = format
        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_depth = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_depth.set_value(depth, format=depth_format)
        self._proportion_adjusted_feedback = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_feedback.set_value(feedback, format=feedback_format)
        self._proportion_adjusted_mix = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            rate_hz=rate,
            depth=self._proportion_adjusted_depth.get_value(format=_Constants.DECIMAL),
            centre_delay_ms=center_delay * 1000, # s to ms
            feedback=self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL),
            mix=self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL))

    def set_rate(self, rate):
        """
        🟩 **R** -
        """
        self.rate_hz = rate

    def get_rate(self):
        """
        🟩 **R** -
        """
        return self.rate_hz

    def set_depth(self, depth, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_depth.set_value(depth, format=format)
        self.depth = self._proportion_adjusted_depth.get_value(format=_Constants.DECIMAL)

    def get_depth(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_depth.get_value(format=format)

    def set_center_delay(self, center_delay):
        """
        🟩 **R** -
        """
        self.centre_delay_ms = center_delay * 1000

    def get_center_delay(self):
        """
        🟩 **R** -
        """
        return self.centre_delay_ms / 1000

    def set_feedback(self, feedback, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_feedback.set_value(feedback, format=format)
        self.feedback = self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL)

    def get_feedback(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_feedback.get_value(format=format)

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def get_mix(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_mix.get_value(format=format)

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Clipping(_pedalboard__Clipping):
    """
    🟩 **R** -
    """
    def __init__(self, threshold=-6):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(threshold_db=threshold)

    def set_threshold(self, threshold):
        """
        🟩 **R** -
        """
        self.threshold_db = threshold

    def get_threshold(self):
        """
        🟩 **R** -
        """
        return self.threshold_db

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Compressor(_pedalboard__Compressor):
    """
    🟩 **R** -
    """
    def __init__(
            self,
            threshold=0,
            ratio=4,
            attack=0.001,
            release=0.1):
        """
        🟩 **R** -
        """

        _initialize(self)

        super().__init__(
            threshold_db=threshold,
            ratio=ratio,
            attack_ms=attack * 1000,
            release_ms=release * 1000)

    def set_threshold(self, threshold):
        """
        🟩 **R** -
        """
        self.threshold_db = threshold

    def get_threshold(self):
        """
        🟩 **R** -
        """
        return self.threshold_db

    def set_ratio(self, ratio):
        """
        🟩 **R** -
        """
        self.ratio = ratio

    def get_ratio(self):
        """
        🟩 **R** -
        """
        return self.ratio

    def set_attack(self, attack):
        """
        🟩 **R** -
        """
        self.attack_ms = attack * 1000

    def get_attack(self):
        """
        🟩 **R** -
        """
        return self.attack_ms / 1000

    def set_release(self, release):
        """
        🟩 **R** -
        """
        self.release_ms = release * 1000

    def get_release(self):
        """
        🟩 **R** -
        """
        return self.release_ms / 1000

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Convolution(_pedalboard__Convolution):
    """
    🟩 **R** -
    """
    def __init__(
            self,
            impulse_response_filename,
            mix=100,
            sample_rate=None,
            format=_Constants.PERCENTAGE,
            mix_format=None):
        """
        🟩 **R** -
        """

        _initialize(self)

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")

        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_mix = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            impulse_response_filename=impulse_response_filename,
            mix=self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL),
            sample_rate=sample_rate)

    def set_impulse_response_filename(self, impulse_response):
        """
        🟩 **R** -
        """
        self.impulse_response = impulse_response

    def get_impulse_response_filename(self):
        """
        🟩 **R** -
        """
        return self.impulse_response

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def get_mix(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_mix.get_value(format=format)

    def set_sample_rate(self, sample_rate):
        """
        🟩 **R** -
        """
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        """
        🟩 **R** -
        """
        return self.sample_rate

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Delay(_pedalboard__Delay):
    """
    🟩 **R** -
    """
    def __init__(
            self,
            delay=0.5,
            feedback=0,
            mix=50,
            format=_Constants.PERCENTAGE,
            feedback_format=None,
            mix_format=None):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")

        if feedback_format is None:
            feedback_format = format
        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_feedback = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_feedback.set_value(feedback, format=feedback_format)
        self._proportion_adjusted_mix = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            delay_seconds=delay,
            feedback=self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL),
            mix=self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL))

    def set_delay(self, delay):
        """
        🟩 **R** -
        """
        self.delay_seconds = delay

    def get_delay(self):
        """
        🟩 **R** -
        """
        return self.delay_seconds

    def set_feedback(self, feedback, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_feedback.set_value(feedback, format=format)
        self.feedback = self._proportion_adjusted_feedback.get_value(format=_Constants.DECIMAL)

    def get_feedback(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_feedback.get_value(format=format)

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def get_mix(self):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_mix.get_value(format=_Constants.DECIMAL)

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Distortion(_pedalboard__Distortion):
    """
    🟩 **R** -
    """
    def __init__(self, drive=10):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(drive_db=drive)

    def set_drive(self, drive):
        """
        🟩 **R** -
        """
        self.drive_db = drive

    def get_drive(self):
        """
        🟩 **R** -
        """
        return self.drive_db

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class GSMFullRateCompressor(_pedalboard__GSMFullRateCompressor):
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Gain(_pedalboard__Gain):
    """
    🟩 **R** -
    """
    def __init__(self, gain=1):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(gain_db=gain)

    def set_gain(self, gain):
        """
        🟩 **R** -
        """
        self.gain_db = gain

    def get_gain(self):
        """
        🟩 **R** -
        """
        return self.gain_db

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class HighShelfFilter(_pedalboard__HighShelfFilter):
    """
    🟩 **R** -
    """
    def __init__(self, cutoff=440, gain=0, q=0.7071067690849304):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(cutoff_hz=cutoff, gain_db=gain, q=q)

    def set_cutoff(self, cutoff):
        """
        🟩 **R** -
        """
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        """
        🟩 **R** -
        """
        return self.cutoff_hz

    def set_gain(self, gain):
        """
        🟩 **R** -
        """
        self.gain_db = gain

    def get_gain(self):
        """
        🟩 **R** -
        """
        return self.gain_db

    def set_q(self, q):
        """
        🟩 **R** -
        """
        self.q = q

    def get_q(self):
        """
        🟩 **R** -
        """
        return self.q

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class HighPassFilter(_pedalboard__HighpassFilter):
    """
    🟩 **R** -
    """
    def __init__(self, cutoff=50):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(cutoff_hz=cutoff)

    def set_cutoff(self, cutoff):
        """
        🟩 **R** -
        """
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        """
        🟩 **R** -
        """
        return self.cutoff_hz

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class LadderFilter(_pedalboard__LadderFilter):
    """
    🟩 **R** -
    """
    def __init__(self, cutoff=200, resonance=0, drive=1):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(cutoff_hz=cutoff, resonance=resonance, drive=drive)

    def set_cutoff(self, cutoff):
        """
        🟩 **R** -
        """
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        """
        🟩 **R** -
        """
        return self.cutoff_hz

    def set_resonance(self, resonance):
        """
        🟩 **R** -
        """
        self.resonance = resonance

    def get_resonance(self):
        """
        🟩 **R** -
        """
        return self.resonance

    def set_drive(self, drive):
        """
        🟩 **R** -
        """
        self.drive = drive

    def get_drive(self):
        """
        🟩 **R** -
        """
        return self.drive

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Limiter(_pedalboard__Limiter):
    """
    🟩 **R** -
    """
    def __init__(self, threshold=-10, release=0.1):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(threshold_db=threshold, release_ms=release / 1000)

    def set_threshold(self, threshold):
        """
        🟩 **R** -
        """
        self.threshold_db = threshold

    def get_threshold(self):
        """
        🟩 **R** -
        """
        return self.threshold_db

    def set_release(self, release):
        """
        🟩 **R** -
        """
        self.release_ms = release * 1000

    def get_release(self):
        """
        🟩 **R** -
        """
        return self.release_ms / 1000

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class LowShelfFilter(_pedalboard__LowShelfFilter):
    """
    🟩 **R** -
    """
    def __init__(self, cutoff=440, gain=0, q=0.7071067690849304):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(cutoff_hz=cutoff, gain_db=gain, q=q)

    def set_cutoff(self, cutoff):
        """
        🟩 **R** -
        """
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        """
        🟩 **R** -
        """
        return self.cutoff_hz

    def set_gain(self, gain):
        """
        🟩 **R** -
        """
        self.gain_db = gain

    def get_gain(self):
        """
        🟩 **R** -
        """
        return self.gain_db

    def set_q(self, q):
        """
        🟩 **R** -
        """
        self.q = q

    def get_q(self):
        """
        🟩 **R** -
        """
        return self.q

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class LowPassFilter(_pedalboard__LowpassFilter):
    """
    🟩 **R** -
    """
    def __init__(self, cutoff=50):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(cutoff_hz=cutoff)

    def set_cutoff(self, cutoff):
        """
        🟩 **R** -
        """
        self.cutoff_hz = cutoff

    def get_cutoff(self):
        """
        🟩 **R** -
        """
        return self.cutoff_hz

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class MP3Compressor(_pedalboard__MP3Compressor):
    """
    🟩 **R** -
    """
    def __init__(self, vbr_quality=3):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(vbr_quality=vbr_quality)

    def set_vbr_quality(self, vbr_quality):
        """
        🟩 **R** -
        """
        self.vbr_quality = vbr_quality

    def get_vbr_quality(self):
        """
        🟩 **R** -
        """
        return self.vbr_quality

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class NoiseGate(_pedalboard__NoiseGate):
    """
    🟩 **R** -
    """
    def __init__(
            self,
            threshold=-100,
            ratio=10,
            attack=0.001,
            release=0.1):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(
            threshold_db=threshold,
            ratio=ratio,
            attack_ms=attack * 1000,
            release_ms=release * 1000)

    def set_threshold(self, threshold):
        """
        🟩 **R** -
        """
        self.threshold_db = threshold

    def get_threshold(self):
        """
        🟩 **R** -
        """
        return self.threshold_db

    def set_ratio(self, ratio):
        """
        🟩 **R** -
        """
        self.ratio = ratio

    def get_ratio(self):
        """
        🟩 **R** -
        """
        return self.ratio

    def set_attack(self, attack):
        """
        🟩 **R** -
        """
        self.attack_ms = attack * 1000

    def get_attack(self):
        """
        🟩 **R** -
        """
        return self.attack_ms / 1000

    def set_release(self, release):
        """
        🟩 **R** -
        """
        self.release_ms = release * 1000

    def get_release(self):
        """
        🟩 **R** -
        """
        return self.release_ms / 1000

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class PeakFilter(_pedalboard__PeakFilter):
    """
    🟩 **R** -
    """
    def __init__(self, frequency=1000, gain=0, q=0.7071067690849304):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(frequency_hz=frequency, gain_db=gain, q=q)

    def set_frequency(self, frequency):
        """
        🟩 **R** -
        """
        self.frequency_hz = frequency

    def get_frequency(self):
        """
        🟩 **R** -
        """
        return self.frequency_hz

    def set_gain(self, gain):
        """
        🟩 **R** -
        """
        self.gain_db = gain

    def get_gain(self):
        """
        🟩 **R** -
        """
        return self.gain_db

    def set_q(self, q):
        """
        🟩 **R** -
        """
        self.q = q

    def get_q(self):
        """
        🟩 **R** -
        """
        return self.q

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Phaser(_pedalboard__Phaser):
    """
    🟩 **R** -
    """
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
        """
        🟩 **R** -
        """
        _initialize(self)

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")

        if depth_format is None:
            depth_format = format
        if feedback_format is None:
            feedback_format = format
        if mix_format is None:
            mix_format = format

        self._proportion_adjusted_depth = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_depth.set_value(depth, format=depth_format)
        self._proportion_adjusted_feedback = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_feedback.set_value(feedback, format=feedback_format)
        self._proportion_adjusted_mix = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_mix.set_value(mix, format=mix_format)

        super().__init__(
            rate_hz=rate,
            depth=self._proportion_adjusted_depth.get_value(_Constants.DECIMAL),
            centre_frequency_hz=center_frequency,
            feedback=self._proportion_adjusted_feedback.get_value(_Constants.DECIMAL),
            mix=self._proportion_adjusted_mix.get_value(_Constants.DECIMAL))

    def set_rate(self, rate):
        """
        🟩 **R** -
        """
        self.rate_hz = rate

    def get_rate(self):
        """
        🟩 **R** -
        """
        return self.rate_hz

    def set_depth(self, depth, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_depth.set_value(depth, format=format)
        self.depth = self._proportion_adjusted_depth.get_value(_Constants.DECIMAL)

    def get_depth(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_depth.get_value(format=format)

    def set_center_frequency(self, center_frequency):
        """
        🟩 **R** -
        """
        self.centre_frequency_hz = center_frequency

    def get_center_frequency(self):
        """
        🟩 **R** -
        """
        return self.centre_frequency_hz

    def set_feedback(self, feedback, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_feedback.set_value(feedback, format=format)
        self.feedback = self._proportion_adjusted_feedback.get_value(_Constants.DECIMAL)

    def get_feedback(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_feedback.get_value(format=format)

    def set_mix(self, mix, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_mix.set_value(mix, format=format)
        self.mix = self._proportion_adjusted_mix.get_value(_Constants.DECIMAL)

    def get_mix(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_mix.get_value(format=format)

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class PitchShift(_pedalboard__PitchShift):
    """
    🟩 **R** -
    """
    def __init__(self, semitones=0):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(semitones=semitones)

    def set_semitones(self, pitch_shift_semitones):
        """
        🟩 **R** -
        """
        self.pitch_shift_semitones = pitch_shift_semitones

    def get_semitones(self):
        """
        🟩 **R** -
        """
        return self.pitch_shift_semitones

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class ReSample(_pedalboard__Resample):
    """
    🟩 **R** -
    """
    def __init__(self, sample_rate=8000):
        """
        🟩 **R** -
        """
        _initialize(self)

        super().__init__(sample_rate=sample_rate)

    def set_sample_rate(self, sample_rate):
        """
        🟩 **R** -
        """
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        """
        🟩 **R** -
        """
        return self.sample_rate

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class Reverb(_pedalboard__Reverb):
    """
    🟩 **R** -
    """
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
        """
        🟩 **R** -
        """
        _initialize(self)

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")

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

        self._proportion_adjusted_room_size = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_room_size.set_value(room_size, format=room_size_format)
        self._proportion_adjusted_damping = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_damping.set_value(damping, format=damping_format)
        self._proportion_adjusted_wet_level = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_wet_level.set_value(wet_level, format=wet_level_format)
        self._proportion_adjusted_dry_level = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_dry_level.set_value(dry_level, format=dry_level_format)
        self._proportion_adjusted_width = self._number_converter__module.ProportionConverter()
        self._proportion_adjusted_width.set_value(width, format=width_format)

        super().__init__(
            room_size=self._proportion_adjusted_room_size.get_value(_Constants.DECIMAL),
            damping=self._proportion_adjusted_damping.get_value(_Constants.DECIMAL),
            wet_level=self._proportion_adjusted_wet_level.get_value(_Constants.DECIMAL),
            dry_level=self._proportion_adjusted_dry_level.get_value(_Constants.DECIMAL),
            width=self._proportion_adjusted_width.get_value(_Constants.DECIMAL),
            freeze_mode=freeze_mode)

    def set_room_size(self, room_size, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_room_size.set_value(room_size, format=format)
        self.room_size = self._proportion_adjusted_room_size.get_value(_Constants.DECIMAL)

    def get_room_size(self):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_room_size.get_value(_Constants.PERCENTAGE)

    def set_damping(self, damping, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_damping.set_value(damping, format=format)
        self.damping = self._proportion_adjusted_damping.get_value(_Constants.DECIMAL)

    def get_damping(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_damping.get_value(format=format)

    def set_wet_level(self, wet_level, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_wet_level.set_value(wet_level, format=format)
        self.wet_level = self._proportion_adjusted_wet_level.get_value(_Constants.DECIMAL)

    def get_wet_level(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_wet_level.get_value(format=format)

    def set_dry_level(self, dry_level, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_dry_level.set_value(dry_level, format=format)
        self.dry_level = self._proportion_adjusted_dry_level.get_value(_Constants.DECIMAL)

    def get_dry_level(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_dry_level.get_value(format=format)

    def set_width(self, width, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        self._proportion_adjusted_width.set_value(width, format=format)
        self.width = self._proportion_adjusted_width.get_value(_Constants.DECIMAL)

    def get_width(self, format=_Constants.PERCENTAGE):
        """
        🟩 **R** -
        """
        return self._proportion_adjusted_width.get_value(format=format)

    def set_freeze_mode(self, freeze_mode):
        """
        🟩 **R** -
        """
        self.freeze_mode = freeze_mode

    def get_freeze_mode(self):
        """
        🟩 **R** -
        """
        return self.freeze_mode

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True