# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from athensrock.spotify_auth import SpotifyAuth

def index(request):
    return render(request, 'home/index.html')
