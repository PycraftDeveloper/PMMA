import threading as _threading
import gc as _gc
import time as _time

import pyaudio as _pyaudio
import numpy as _numpy

from pmma.python_src.general import *
from pmma.python_src.registry import Registry

from pmma.python_src.utility.error_utils import *
from pmma.python_src.utility.general_utils import initialize as _initialize

class Sampler:
    def __init__(self, chunk_size=2048, sampling_rate=44100, input_device_id=None):
        _initialize(self)

        self._pyaudio_instance = _pyaudio.PyAudio()

        if input_device_id is None:
            self._input_device = self.get_default_input_device()
        else:
            self._input_device = input_device_id

        self._do_sampling = True
        self._is_sampling_running = False
        self._do_pause_sampling = False

        self._sampling_rate = sampling_rate
        self._chunk_size = chunk_size

        self._volume = 0
        self._frequency = []
        self._loudest_frequency = 0

        self._sampler_thread = _threading.Thread(
            target=self.sampler)
        self._sampler_thread.daemon = True
        self._sampler_thread.name = "Sampler:Sampler_Thread"

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._do_sampling = False

            if self._is_sampling_running:
                self._sampler_thread.join()

            del self
            if do_garbage_collection:
                _gc.collect()

    def print_input_devices(self):
        info = self._pyaudio_instance.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(numdevices):
            if (self._pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                input_device_name = self._pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('name')
                print(f"Input Device id {i} - {input_device_name}")

    def get_input_devices(self):
        input_devices = []
        info = self._pyaudio_instance.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(numdevices):
            if (self._pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                input_device_name = self._pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('name')
                input_devices.append(input_device_name)
        return input_devices

    def set_input_device(self, input_device_id=None):
        if input_device_id is None:
            input_device = self.get_default_input_device()
        else:
            input_device = input_device_id

        if self._input_device != input_device:
            self._input_device = input_device

            if self._is_sampling_running:
                self.stop()
                self.start()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_default_input_device(self):
        try:
            return self._pyaudio_instance.get_default_input_device_info()["index"]
        except IOError:
            return

    def sampler(self, wait_time=None):
        self._is_sampling_running = True

        if self._input_device is None:
            log_development("No input device was found. The easiest reason \
for this is because the operating system hasn't detected any input device \
either. Therefore the first step for troubleshooting this is to make sure \
that you have an input device connected to your current machine. Likewise \
also make sure that the device is behaving as expected. Should this fail and \
the operating system has detected your device, consider running the \
'print_input_devices()' command and manually selecting the device you want to use.")

            raise NoInputDevicesFoundError("No audio input devices were found!")

        stream = self._pyaudio_instance.open(
            format=_pyaudio.paInt16,
            channels=1,
            rate=self._sampling_rate,
            input=True,
            frames_per_buffer=self._chunk_size,
            input_device_index=self._input_device)

        while self._do_sampling:
            if self._do_pause_sampling:
                if wait_time is None:
                    wait_time = 1/Registry.refresh_rate
                _time.sleep(wait_time)
                continue

            try:
                stream_data = stream.read(self._chunk_size)
            except Exception as error:
                log_development("Unable to read the current audio sample. Whilst \
the exact cause of this error is unknown, it's likely that the cause for this error \
was that the audio input device was disconnected without first having had the sampling \
process stopped. Please use the existing 'stop()' method in order to avoid this error being \
raised when the audio device is removed.")
                raise UnableToReadAudioSampleError("Unable to read audio sample!") from error

            data = _numpy.frombuffer(
                stream_data,
                dtype=_numpy.int16)

            peak = _numpy.average(_numpy.abs(data))*2

            self._volume = peak

            data = data * _numpy.hanning(len(data))
            self._frequency = abs(_numpy.fft.fft(data).real)

            fft = self._frequency[:int(len(self._frequency)/2)]
            freq = _numpy.fft.fftfreq(self._chunk_size, 1.0/self._sampling_rate)
            freq = freq[:int(len(freq)/2)]
            self._loudest_frequency = freq[_numpy.where(fft==_numpy.max(fft))[0][0]]+1

        self._is_sampling_running = False
        stream.stop_stream()
        stream.close()

    def start(self):
        if self._is_sampling_running is False:
            self._do_sampling = True

            self._sampler_thread = _threading.Thread(
                target=self.sampler)
            self._sampler_thread.daemon = True
            self._sampler_thread.name = "Sampler:Sampler_Thread"
            self._sampler_thread.start()

    def stop(self, wait_until_stopped=True):
        self._do_sampling = False
        if wait_until_stopped:
            self._sampler_thread.join()

    def pause(self):
        self._do_pause_sampling = True

    def unpause(self):
        self._do_pause_sampling = False

    def get_volume(self):
        return self._volume

    def get_frequency(self):
        return self._frequency

    def get_loudest_frequency(self):
        return self._loudest_frequency

    def is_sampling(self):
        return self._is_sampling_running