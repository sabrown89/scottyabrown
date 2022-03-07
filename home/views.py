# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from athensrock.spotify_auth import SpotifyAuth
from gardening.models import Seed
from IPython import embed

def index(request):
    seeds = Seed.objects.all()
    classifications = seeds.values('classification').distinct()
    seed_classes = {}
    for cla_dict in classifications:
        cla = cla_dict['classification']
        seed_classes[cla] = seeds.filter(classification=cla)
    return render(request, 'home/index.html', {'seed_classes': seed_classes})

def cocktails(request):
    return render(request, 'home/cocktails.html')
