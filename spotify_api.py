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
def handle_spotify_exception(e):
    print(f"Spotify API Error: {e}")

def play_music():
    try:
        sp.start_playback()  # Starts the music playback
        print("Playback started successfully.")
    except spotipy.exceptions.SpotifyException as e:
        handle_spotify_exception(e)

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


def search_song(song_name, limit=1):
    """Search for a song by name and return a list of URIs limited by `limit`."""
    try:
        results = sp.search(q=song_name, limit=limit)
        return [item['uri'] for item in results['tracks']['items']]
    except spotipy.exceptions.SpotifyException as e:
        handle_spotify_exception(e)
        return []

    
#function to play specific music by uri by passing the uri from search_song function
def play_specific_music(song_name):
    uris = search_song(song_name, limit=1)
    if uris:
        try:
            sp.start_playback(uris=uris)
            print(f"Playback started for {song_name}.")
        except spotipy.exceptions.SpotifyException as e:
            handle_spotify_exception(e)
    else:
        print(f"Song {song_name} not found.")


#function to play specific genre
def play_specific_genre(genre):
    results = sp.search(q="genre:" + '"' + genre + '"', type='track', limit=10)
    if results['tracks']['items']:
        track_uris = [track['uri'] for track in results['tracks']['items']]
        try:
            sp.start_playback(uris=track_uris)  # Starts the music playback for tracks in the genre
            print(f"Playback started for genre {genre}.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Failed to start playback for genre {genre}: {e}")
    else:
        print(f"No tracks found for genre {genre}.")


#function to play specific album
def play_specific_album(album_name):
    results = sp.search(q="album:" + album_name, type='album', limit=1)
    if results['albums']['items']:
        album_id = results['albums']['items'][0]['id']
        tracks = sp.album_tracks(album_id)
        track_uris = [track['uri'] for track in tracks['items']]
        try:
            sp.start_playback(uris=track_uris)  # Starts the music playback for all tracks in the album
            print(f"Playback started for the album {album_name}.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Failed to start playback for album {album_name}: {e}")
    else:
        print(f"Album {album_name} not found.")


def play_specific_artist(artist_name):
    """
    Plays music by a specific artist on Spotify using Spotipy.
    
    Args:
    artist_name (str): Name of the artist to play music from.

    Returns:
    None: Outputs status directly to console.
    """
    try:
        # Search for the artist by name
        results = sp.search(q="artist:" + artist_name, type='artist', limit=1)
        if results['artists']['items']:
            artist_id = results['artists']['items'][0]['id']
            # Get top tracks of the artist
            tracks = sp.artist_top_tracks(artist_id)
            track_uris = [track['uri'] for track in tracks['tracks']]
            
            if track_uris:
                # Start playback of the top tracks of this artist
                sp.start_playback(uris=track_uris)
                print(f"Playback started for artist {artist_name}.")
            else:
                print(f"No tracks found for artist {artist_name}.")
        else:
            print(f"Artist {artist_name} not found.")
    
    except spotipy.exceptions.SpotifyException as e:
        print(f"Failed to start playback for artist {artist_name}: {e}")

#function to play specific artist with its song name
def play_specific_song_by_artist(artist_name, track_name):
    """
    Plays a specific song by a specific artist on Spotify using Spotipy.
    
    Args:
    artist_name (str): Name of the artist.
    track_name (str): Name of the track to play.

    Returns:
    None: Outputs status directly to console.
    """
    try:
        # Search for the artist and track by name
        query = f"artist:{artist_name} track:{track_name}"
        results = sp.search(q=query, type='track', limit=1)
        
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            # Start playback of the found track
            sp.start_playback(uris=[track_uri])
            print(f"Playback started for '{track_name}' by {artist_name}.")
        else:
            print(f"Track '{track_name}' by artist {artist_name} not found.")

    except spotipy.exceptions.SpotifyException as e:
        print(f"Failed to start playback for '{track_name}' by {artist_name}: {e}")


#function to play specific album by specific artist
def play_specific_album_by_artist(artist_name, album):
    """
    Plays a specific album by a specific artist on Spotify using Spotipy.
    
    Args:
    artist_name (str): Name of the artist.
    album (str): Name of the album to play.

    Returns:
    None: Outputs status directly to console.
    """
    try:
        # Search for the artist and album by name
        query = f"artist:{artist_name} album:{album}"
        results = sp.search(q=query, type='album', limit=1)
        
        if results['albums']['items']:
            album_id = results['albums']['items'][0]['id']
            tracks = sp.album_tracks(album_id)
            track_uris = [track['uri'] for track in tracks['items']]
            
            if track_uris:
                # Start playback of all tracks in the album
                sp.start_playback(uris=track_uris)
                print(f"Playback started for the album '{album}' by {artist_name}.")
            else:
                print(f"No tracks found for the album '{album}' by artist {artist_name}.")
        else:
            print(f"Album '{album}' by artist {artist_name} not found.")

    except spotipy.exceptions.SpotifyException as e:
        print(f"Failed to start playback for the album '{album}' by {artist_name}: {e}")


#play_specific_song_by_artist("SHE","五月天")
#play_specific_music("Million Reasons")

play_specific_album_by_artist("Taylor Swift","Speak Now")