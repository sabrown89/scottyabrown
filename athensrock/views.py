# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from athensrock.models import Song
from athensrock.spotify_auth import SpotifyAuth
from athensrock.add_songs_to_spotify import AddSongsToSpotify
from django.utils import timezone

def index(request):
    most_recent_song = Song.objects.latest('created')
    sp = SpotifyAuth('')
    time_diff = timezone.localtime(timezone.now()) - most_recent_song.created
    songs_added_in_last_two_hours = int(time_diff.total_seconds()) < 7200
    time_left = 120 - int(time_diff.total_seconds() / 60)
    if sp.needs_authentication():
        result = render(request, 'athensrock/callback.html')

    return render(request, 'athensrock/index.html', {
        'most_recent_song': most_recent_song,
        'sp': sp,
        'songs_added_in_last_two_hours': songs_added_in_last_two_hours,
        'time_left': time_left,
    })

def callback(request):
    code = request.__dict__['environ']['QUERY_STRING'][5:]
    sp_code = SpotifyAuth(code)
    sp_code.get_access_token()
    return render(request, 'athensrock/index.html',{
        'sp_code': sp_code,
    })

def dashboard(request):
    songs = Song.objects.order_by('-created')
    found_songs = Song.objects.filter(added_to_playlist=True)
    song_percentage = (found_songs.count() / songs.count()) * 100
    song_accuracy = round(song_percentage, 2)
    return render(request, 'athensrock/dashboard.html',{
        'songs': songs,
        'song_accuracy' : song_accuracy,
    })

def add_songs(request):
    adts = AddSongsToSpotify()
    adts.add_songs_to_spotify()
    songs = Song.objects.order_by('-created')
    found_songs = Song.objects.filter(added_to_playlist=True)
    song_percentage = (found_songs.count() / songs.count()) * 100
    song_accuracy = round(song_percentage, 2)
    return render(request, 'athensrock/dashboard.html',{
        'songs': songs,
        'song_accuracy' : song_accuracy,
    })

def listen(request):
    return render(request, 'athensrock/listen.html')
