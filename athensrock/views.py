# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from athensrock.models import Song
from athensrock.spotify_auth import SpotifyAuth

def index(request):
    songs = Song.objects.all()
    code = 'code not retrived'
    sp = SpotifyAuth(code)
    return render(request, 'athensrock/index.html', {
        'songs': songs,
        'sp': sp,
    })

def song_detail(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        raise Http404('This song does not exist')
    return render(request, 'athensrock/song_detail.html', {
        'song': song,
    })
