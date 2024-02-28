import pyaudio
import numpy as np
import threading

from pmma.src.registry import Registry

class GetAudioData(Registry):
    volume = 0
    frequency = []
    chunk = 2048
    rate = 44100
    do_sampling = True

    def sampler(self):
        p = pyaudio.PyAudio()
        stream=p.open(
            format=pyaudio.paInt32,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk)

        while self.do_sampling:
            data = np.frombuffer(
                stream.read(self.chunk),
                dtype=np.int16)

            peak = np.average(np.abs(data))*2

            self.volume = peak

            data = data * np.hanning(len(data))
            self.frequency = abs(np.fft.fft(data).real)

        stream.stop_stream()
        stream.close()

    def start_sampling(self):
        self.do_sampling = True
        self.sampler_thread = threading.Thread(target=self.sampler)
        self.sampler_thread.daemon = True
        self.sampler_thread.name = "GetAudioData:Sampler_thread"
        self.sampler_thread.start()

    def stop_sampling(self):
        self.do_sampling = False

    def get_volume(self):
        return self.volume

    def get_frequency(self):
        return self.frequency