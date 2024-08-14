import threading
import gc

import pyaudio
import numpy as np

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Sampler:
    volume = None
    frequency = None
    chunk = 2048
    rate = 44100
    do_sampling = True
    input_device = Constants.DEFAULT

    def __init__(self):
        initialize(self)

        self.pyaudio = pyaudio.PyAudio()
        self.sampling = False

        self.attributes = []

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_default_input_device(self):
        try:
            return self.pyaudio.get_default_input_device_info()["index"]
        except IOError:
            return

    def sampler(self):
        if self.input_device == Constants.DEFAULT:
            input_device = self.get_default_input_device()
        else:
            input_device = self.input_device

        stream = self.pyaudio.open(
            format=pyaudio.paInt32,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
            input_device_index=input_device)

        while self.do_sampling:
            data = np.frombuffer(
                stream.read(self.chunk),
                dtype=np.int16)

            peak = np.average(np.abs(data))*2

            self.volume = peak

            data = data * np.hanning(len(data))
            self.frequency = abs(np.fft.fft(data).real)

            if self.sampling is False:
                self.sampling = True

        self.sampling = False
        stream.stop_stream()
        stream.close()

    def start_sampling(self, input_device_id=0):
        self.do_sampling = True
        self.sampler_thread = threading.Thread(
            target=self.sampler,
            args=(input_device_id,))

        self.sampler_thread.daemon = True
        self.sampler_thread.name = "Sampler:Sampler_thread"
        self.sampler_thread.start()

    def stop_sampling(self):
        self.do_sampling = False

    def get_volume(self):
        return self.volume

    def get_frequency(self):
        return self.frequency

    def is_sampling(self):
        return self.sampling