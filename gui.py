import tkinter as tk
from tkinter import ttk
from audio_recorder import AudioRecorder
from PIL import Image, ImageTk  # For adding icons

class RecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Spotify Audio Control")
        self.master.geometry('300x150')  # Set the window size

        self.recorder = AudioRecorder()

        # Styling
        style = ttk.Style()
        style.configure("TButton", font=('Calibri', 12), borderwidth='4')
        style.configure("TFrame", background='light blue')

        # Layout: Use a frame to contain the controls
        self.frame = ttk.Frame(master, padding="10 10 10 10", style='TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Record Button
        self.record_photo = ImageTk.PhotoImage(Image.open("record_icon.png").resize((50, 50)))  # Adjust path as necessary
        self.record_button = ttk.Button(self.frame, text="Record", command=self.start_recording, image=self.record_photo, compound=tk.TOP)
        self.record_button.grid(column=1, row=1, padx=10, pady=20)

        # Stop Button
        self.stop_photo = ImageTk.PhotoImage(Image.open("stop_icon.png").resize((50, 50)))  # Adjust path as necessary
        self.stop_button = ttk.Button(self.frame, text="Stop", command=self.stop_recording, state=tk.DISABLED, image=self.stop_photo, compound=tk.TOP)
        self.stop_button.grid(column=2, row=1, padx=10, pady=20)

        # Configure grid
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)

    def start_recording(self):
        self.recorder.is_recording = True
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.recorder.start_recording()

    def stop_recording(self):
        self.recorder.stop_recording()
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.recorder.save_recording()