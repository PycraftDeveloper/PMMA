import threading
import gc
import time

import pyaudio
import numpy as np

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Sampler:
    def __init__(self, chunk_size=2048, sampling_rate=44100, input_device_id=None):
        initialize(self)

        self.pyaudio_instance = pyaudio.PyAudio()

        if input_device_id is None:
            self.input_device = self.get_default_input_device()
        else:
            self.input_device = input_device_id

        self.do_sampling = True
        self.is_sampling_running = False
        self.do_pause_sampling = False

        self.sampling_rate = sampling_rate
        self.chunk_size = chunk_size

        self.volume = 0
        self.frequency = []
        self.loudest_frequency = 0

        self.sampler_thread = threading.Thread(
            target=self.sampler)
        self.sampler_thread.daemon = True
        self.sampler_thread.name = "Sampler:Sampler_thread"

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self.do_sampling = False

            if self.is_sampling_running:
                self.sampler_thread.join()

            del self
            if do_garbage_collection:
                gc.collect()

    def print_input_devices(self):
        info = self.pyaudio_instance.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(numdevices):
            if (self.pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                input_device_name = self.pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('name')
                print(f"Input Device id {i} - {input_device_name}")

    def get_input_devices(self):
        input_devices = []
        info = self.pyaudio_instance.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(numdevices):
            if (self.pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                input_device_name = self.pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('name')
                input_devices.append(input_device_name)
        return input_devices

    def set_input_device(self, input_device_id=None):
        if input_device_id is None:
            input_device = self.get_default_input_device()
        else:
            input_device = input_device_id

        if self.input_device != input_device:
            self.input_device = input_device

            if self.is_sampling_running:
                self.stop()
                self.start()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_default_input_device(self):
        try:
            return self.pyaudio_instance.get_default_input_device_info()["index"]
        except IOError:
            return

    def sampler(self, wait_time=None):
        self.is_sampling_running = True

        if self.input_device is None:
            log_development("No input device was found. The easiest reason \
for this is because the operating system hasn't detected any input device \
either. Therefore the first step for troubleshooting this is to make sure \
that you have an input device connected to your current machine. Likewise \
also make sure that the device is behaving as expected. Should this fail and \
the operating system has detected your device, consider running the \
'print_input_devices()' command and manually selecting the device you want to use.")

            raise NoInputDevicesFoundError("No audio input devices were found!")

        stream = self.pyaudio_instance.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.sampling_rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            input_device_index=self.input_device)

        while self.do_sampling:
            if self.do_pause_sampling:
                if wait_time is None:
                    wait_time = 1/Registry.refresh_rate
                time.sleep(wait_time)
                continue

            try:
                stream_data = stream.read(self.chunk_size)
            except Exception as error:
                log_development("Unable to read the current audio sample. Whilst \
the exact cause of this error is unknown, it's likely that the cause for this error \
was that the audio input device was disconnected without first having had the sampling \
process stopped. Please use the existing 'stop()' method in order to avoid this error being \
raised when the audio device is removed.")
                raise UnableToReadAudioSampleError("Unable to read audio sample!") from error

            data = np.frombuffer(
                stream_data,
                dtype=np.int16)

            peak = np.average(np.abs(data))*2

            self.volume = peak

            data = data * np.hanning(len(data))
            self.frequency = abs(np.fft.fft(data).real)

            fft = self.frequency[:int(len(self.frequency)/2)]
            freq = np.fft.fftfreq(self.chunk_size, 1.0/self.sampling_rate)
            freq = freq[:int(len(freq)/2)]
            self.loudest_frequency = freq[np.where(fft==np.max(fft))[0][0]]+1

        self.is_sampling_running = False
        stream.stop_stream()
        stream.close()

    def start(self):
        if self.is_sampling_running is False:
            self.do_sampling = True

            self.sampler_thread = threading.Thread(
                target=self.sampler)

            self.sampler_thread.daemon = True
            self.sampler_thread.name = "Sampler:Sampler_thread"
            self.sampler_thread.start()

    def stop(self, wait_until_stopped=True):
        self.do_sampling = False
        if wait_until_stopped:
            self.sampler_thread.join()

    def pause(self):
        self.do_pause_sampling = True

    def unpause(self):
        self.do_pause_sampling = False

    def get_volume(self):
        return self.volume

    def get_frequency(self):
        return self.frequency

    def get_loudest_frequency(self):
        return self.loudest_frequency

    def is_sampling(self):
        return self.is_sampling_running