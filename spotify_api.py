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

def test_search_track():
    track_query = "knock the heavens door"
    results = sp.search(q=track_query, limit=1, type='track')
    tracks = results['tracks']['items']
    if tracks:
        print(f"Top result for '{track_query}': {tracks[0]['name']} by {tracks[0]['artists'][0]['name']}")
    else:
        print(f"No results found for '{track_query}'.")

test_search_track()