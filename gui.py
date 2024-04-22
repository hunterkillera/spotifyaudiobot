# Main GUI application using Tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from audio_recorder import AudioRecorder
from PIL import Image, ImageTk
from chatcompletion import get_chat_completion  # Importing the chat completion function
from audiototext import transcribe_audio
import spotify_api

class RecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Spotify Audio Control")
        self.master.resizable(True, True)

        self.recorder = AudioRecorder(filename="output.wav")

        style = ttk.Style()
        style.configure("TButton", font=('Calibri', 12), borderwidth='4')
        style.configure("TFrame", background='light blue')

        self.frame = ttk.Frame(master, padding="10 10 10 10", style='TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True)

        try:
            self.record_photo = ImageTk.PhotoImage(Image.open("record_icon.png").resize((50, 50)))
            self.stop_photo = ImageTk.PhotoImage(Image.open("stop_icon.png").resize((50, 50)))
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Icon file not found: {e}")
            return

        self.record_button = ttk.Button(self.frame, text="Record", command=self.start_recording, image=self.record_photo, compound=tk.TOP)
        self.record_button.grid(column=1, row=1, padx=10, pady=20)
        self.stop_button = ttk.Button(self.frame, text="Stop", command=self.stop_recording, state=tk.DISABLED, image=self.stop_photo, compound=tk.TOP)
        self.stop_button.grid(column=2, row=1, padx=10, pady=20)

        self.text_area = ScrolledText(self.frame, height=10, width=50)
        self.text_area.grid(column=1, row=2, columnspan=2, sticky=tk.W+tk.E)

    def start_recording(self):
        self.recorder.start_recording()
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_recording(self):
        self.recorder.stop_recording()
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.update_transcription()

    def update_transcription(self):
        transcription = transcribe_audio("output.wav")
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, "Transcription: " + transcription + "\n")
        chat_response = get_chat_completion(transcription)  # Using the imported function
        self.text_area.insert(tk.END, "GPT-4 Response: " + chat_response + "\n")
        self.process_user_input(chat_response)  # Call process_user_input with chat_response
        self.master.update_idletasks()

    def process_user_input(self, chat_response):
        # Initialize a variable to track the action
        action_taken = None

        # Process user input and call Spotify API functions based on the response
        if "play" in chat_response.lower():
            spotify_api.play_music()
            action_taken = "play"
        elif "pause" in chat_response.lower():
            spotify_api.pause_music()
            action_taken = "pause"
        elif "skip" in chat_response.lower():
            spotify_api.skip_music()
            action_taken = "skip"
        # play specific song
        elif "song" in chat_response.lower() and "artist" not in chat_response.lower():
            song = chat_response.split(',')[1].strip()
            spotify_api.play_specific_music(song)
            action_taken = "play_specific_song"
        # play specific singer with the song
        elif "song" in chat_response.lower() and "artist" in chat_response.lower():
            chat_response = [item.strip() for item in chat_response.split(',')[1:]]
            artist = chat_response[0]
            song = chat_response[2]
            spotify_api.play_specific_song_by_artist(artist, song)
            action_taken = "play_specific_song_by_artist"
        # play specific artist
        elif "artist" in chat_response.lower():
            artist = [item.strip() for item in chat_response.split(',')[1:]]
            artist = ','.join(artist)
            spotify_api.play_specific_artist(artist)
            action_taken = "play_specific_artist"
        
        # Return the action taken
        return action_taken

