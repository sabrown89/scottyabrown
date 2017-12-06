# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class HikingDay(models.Model):
    day = models.DateField()
    mile = models.DecimalField(max_digits=8, decimal_places=1)
    state = models.CharField(max_length=2)
    location = models.CharField(max_length=255)
    day_off = models.BooleanField()
    precipitation = models.BooleanField()
    precip_status = models.CharField(max_length=100, blank=True)
    notes = models.TextField()
    trail_magic = models.BooleanField(default=False)
