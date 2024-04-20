import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_secret = os.getenv('SpotifyClient_secret')
if not client_secret:
    raise ValueError("API key not found. Please set the SpotifyClient_secret environment variable.")

scope = "user-modify-playback-state user-read-playback-state user-read-currently-playing streaming"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='14bb0ab50208464995cca8c06d330d6c',
                                               client_secret=client_secret,
                                               redirect_uri='https://github.com/hunterkillera/spotifyaudiobot',
                                               scope=scope,
                                               cache_path="token.txt"))
def play_music():
    try:
        sp.start_playback()  # Starts the music playback
        print("Playback started successfully.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Failed to start playback: {e}")

def pause_music():
    try:
        sp.pause_playback()  # Pauses the music playback
        print("Playback paused successfully.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Failed to pause playback: {e}")

def skip_music():
    try:
        sp.next_track()  # Skips to the next track
        print("Skipped to the next track.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Failed to skip track: {e}")


#function to search for a song and get the uri
def search_song(song_name):
    results = sp.search(q=song_name, limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    else:
        return None
    
#function to play specific music by uri by passing the uri from search_song function
def play_specific_music(song_name):
    uri = search_song(song_name)
    if uri:
        try:
            sp.start_playback(uris=[uri])  # Starts the music playback
            print(f"Playback started for {song_name}.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Failed to start playback: {e}")
    else:
        print(f"Song {song_name} not found.")

#function to play specific genre
def play_specific_genre(genre):
    results = sp.recommendations(seed_genres=[genre])
    if results['tracks']:
        uris = [track['uri'] for track in results['tracks']]
        try:
            sp.start_playback(uris=uris)  # Starts the music playback
            print(f"Playback started for {genre}.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Failed to start playback: {e}")
    else:
        print(f"No tracks found for genre {genre}.")

#function to play specific album
def play_specific_album(album_name):
    results = sp.search(q=album_name, limit=1, type='album')
    if results['albums']['items']:
        album_uri = results['albums']['items'][0]['uri']
        tracks = sp.album_tracks(album_uri)
        uris = [track['uri'] for track in tracks['items']]
        try:
            sp.start_playback(uris=uris)  # Starts the music playback
            print(f"Playback started for {album_name}.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Failed to start playback: {e}")
    else:
        print(f"Album {album_name} not found.")

play_specific_genre("student")