import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-modify-playback-state user-read-playback-state user-read-currently-playing streaming"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='14bb0ab50208464995cca8c06d330d6c',
                                               client_secret='d58374d9a1ef48508599f27d2fa07970',
                                               redirect_uri='https://github.com/hunterkillera/spotifyaudiobot',
                                               scope=scope))

# Now you can access authorized Spotify API methods
