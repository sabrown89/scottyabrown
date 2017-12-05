import os
import spotipy
from athensrock.retrieve_songs import RetrieveSongs
from athensrock.spotify_auth import SpotifyAuth
from django.db import models
from athensrock.models import Song
from athensrock.exceptions import SpotifyException

class AddSongsToSpotify(object):
    def __init__(self):
        self.user = 'scottyspompom'
        self.spotify = SpotifyAuth('').spotify_auth()
        self.song_list = RetrieveSongs().clean_song_list()

    def add_songs_to_spotify(self):
        for song in self.song_list:
            try:
                spotify_dict = self.spotify_attributes_for(song)
                self.add_to_playlist([spotify_dict['uri']])
                self.save_to_database(spotify_dict, song, True)
            except SpotifyException:
                spotify_dict = self.spotify_attributes_for(song)
                self.save_to_database(spotify_dict, song, False)
            except IndexError:
                spotify_dict = {'name': '', 'artist': '', 'uri': ''}
                self.save_to_database(spotify_dict, song, False)

    def save_to_database(self, spotify, song, to_playlist):
        s = Song(
                 raw_name=song['full_song'],
                 name=spotify['name'],
                 artist=spotify['artist'],
                 spotify_id=spotify['uri'],
                 added_to_playlist = to_playlist
                )
        s.save()

    def spotify_attributes_for(self, song):
        s = self.spotify.search(song['full_song'], type='track')
        spotify = s['tracks']['items'][0]
        return {'name': spotify['name'],
                'artist': spotify['artists'][0]['name'],
                'uri': spotify['uri'],
                'added_to_playlist': None
                }

    def add_to_playlist(self, track_list):
        self.spotify.user_playlist_add_tracks(self.user,
                                         os.environ['PLAYLIST_ID_SPOTIFY'],
                                         track_list,
                                         position=0
        )
