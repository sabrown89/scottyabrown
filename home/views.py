# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from athensrock.spotify_auth import SpotifyAuth
from IPython import embed

def index(request):
    return render(request, 'home/index.html')

def cocktails(request):
    return render(request, 'home/cocktails.html')
