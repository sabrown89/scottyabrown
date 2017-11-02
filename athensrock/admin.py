# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ['raw_name',
                    'name',
                    'artist',
                    'spotify_id',
                    'added_to_playlist',
                    'created'
                    ]

admin.site.register(Song, SongAdmin)
