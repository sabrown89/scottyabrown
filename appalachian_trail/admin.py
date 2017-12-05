# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import HikingDay

class HikingDayAdmin(admin.ModelAdmin):
    list_display = ['day',
                    'mile',
                    'state',
                    'location',
                    'day_off',
                    'precipitation',
                    'precip_status',
                    'notes'
                    ]

admin.site.register(HikingDay, HikingDayAdmin)
