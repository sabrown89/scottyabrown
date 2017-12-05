import requests
from bs4 import BeautifulSoup
import html.parser
from IPython import embed
from athensrock.clean_song import CleanSong

class RetrieveSongs(object):

    def __init__(self):
        self.url = 'http://www.athensrock.com'

    def clean_song_list(self):
        clean_list = []
        for raw_song in self.delimited_song_list():
            song = raw_song.split('\r')
            song = song[0].strip()
            clean_list.append(CleanSong(song).clean_song())
        #    clean_list.append(song[0].strip())
        return clean_list

    def delimited_song_list(self):
        delimited_songs = self.raw_song_list().split(self.song_delimiter())
        return delimited_songs[1:] # removes playlist title from song list

    def page_request(self):
        return requests.get(self.url)

    def validate_url_status(self):
        if self.page_request().status_code == 200:
            pass
        else:
            print("The Athens Rock Website is currently down")
            exit(1)

    def raw_song_list(self):
        self.validate_url_status()
        page_text = BeautifulSoup(self.page_request().text, 'html.parser')
        return page_text.find_all('td')[3].get_text()

    def song_delimiter(self):
        return html.unescape('&raquo;')
