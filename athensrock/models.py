# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Song(models.Model):
    raw_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    spotify_id = models.CharField(max_length=255)
    added_to_playlist = models.BooleanField()
    created = models.DateTimeField(default=timezone.localtime(timezone.now()))
