# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from appalachian_trail.models import HikingDay

def index(request):
    hiking_days = HikingDay.objects.order_by('day')
    return render(request, 'appalachian_trail/index.html', {
        'hiking_days': hiking_days,
    })
