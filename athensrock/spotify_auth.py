import sys
import os
import spotipy
import spotipy.util as util
from IPython import embed

class SpotifyAuth(object):
    def __init__(self, code):
        self.username = 'scottyspompom'
        self.scope = 'user-library-read playlist-modify-public user-read-email'
        self.redirect_uri = 'http://67.205.140.221:8000/callback'
        self.cache = '.spotipyoauthcache'
        self.code = code

    def needs_authentication(self):
        if self.get_access_token():
            return False
        else:
            return True

    def get_access_token(self):
        token_info = self.spotify_oauth().get_cached_token()
        if token_info:
            return token_info['access_token']
        else:
            token_info = self.spotify_oauth().get_access_token(self.code)
            return token_info['access_token']

    def spotify_oauth(self):
        return spotipy.oauth2.SpotifyOAuth(os.environ['CLIENT_ID_SPOTIFY'],
                                          os.environ['CLIENT_SECRET_SPOTIFY'],
                                          self.redirect_uri,
                                          scope=self.scope,
                                          cache_path=self.cache
                                          )
    def spotify_auth(self):
        return spotipy.Spotify(auth=self.get_access_token())

    def get_authorize_url(self):
        return self.spotify_oauth().get_authorize_url()
