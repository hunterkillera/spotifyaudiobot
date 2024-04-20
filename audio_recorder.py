# audio_recorder.py
import pyaudio
import wave
import threading

class AudioRecorder:
    def __init__(self, sample_rate=44100, num_channels=1, chunk=1024, format=pyaudio.paInt16):
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.chunk = chunk
        self.format = format
        self.frames = []
        self.is_recording = False
        self.p = pyaudio.PyAudio()

    def start_recording(self):
        self.frames = []
        self.stream = self.p.open(format=self.format, channels=self.num_channels,
                                  rate=self.sample_rate, input=True, frames_per_buffer=self.chunk)
        self.thread = threading.Thread(target=self.record)
        self.thread.start()
        print("Recording started...")

    def record(self):
        while self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop_recording(self):
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()
        print("Finished recording.")

    def save_recording(self, filename="output.wav"):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.num_channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print(f"Recording saved as {filename}")
