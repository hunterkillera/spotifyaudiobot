import tkinter as tk
import threading
import pyaudio
import wave

class AudioRecorder:
    def __init__(self, master):
        self.master = master
        self.is_recording = False
        self.filename = "output.wav"
        self.sample_rate = 44100
        self.num_channels = 1
        self.format = pyaudio.paInt16
        self.chunk = 1024
        self.frames = []

        # Setting up the PyAudio object
        self.p = pyaudio.PyAudio()
        
        # UI Components
        self.record_button = tk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack(pady=5)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_recording(self):
        self.is_recording = True
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start recording
        self.frames = []
        self.stream = self.p.open(format=self.format, channels=self.num_channels, rate=self.sample_rate, input=True, frames_per_buffer=self.chunk)
        self.thread = threading.Thread(target=self.record)
        self.thread.start()
        print("Recording started...")

    def record(self):
        while self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
    
    def stop_recording(self):
        self.is_recording = False
        print("Finished recording.")

        # Stop and close the audio stream
        self.stream.stop_stream()
        self.stream.close()

        # Disable stop button and enable record button
        self.stop_button.config(state=tk.DISABLED)
        self.record_button.config(state=tk.NORMAL)

        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.num_channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

def main():
    root = tk.Tk()
    root.title("Audio Recorder")
    app = AudioRecorder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
