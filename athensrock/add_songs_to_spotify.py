import os
import spotipy
from IPython import embed

class AddSongsToSpotify(object):
    def __init__(self, song_list):
        self.song_list = song_list
        self.user = 'scottyspompom'
        self.spotify = SpotifyAuth(code).spotify_auth()

    def add_songs_to_spotify(self):
        self.add_to_playlist(self.track_list)

    def track_list(self):
        track_list = []
        for song in self.song_list:
            track_list.append(self.return_spotify_uri_for(song))
        return track_list

    def return_spotify_uri_for(self, song):
        result = self.spotify.search("{full_song}", type='track').format(**song)
        return result['tracks']['items'][0]['uri']

    def add_to_playlist(self, track_list):
        self.spotify.user_playlist_add_tracks(self.user,
                                         os.environ['PLAYLIST_ID_SPOTIFY'],
                                         track_list,
                                         position=0
        )
