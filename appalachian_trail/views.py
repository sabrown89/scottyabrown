# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from appalachian_trail.models import HikingDay
from django.http import JsonResponse
from django.db.models import Count

def show(request):
    return render(request, 'appalachian_trail/show.html')

def index(request):
    hiking_days = HikingDay.objects.order_by('day')
    return render(request, 'appalachian_trail/index.html', {
        'hiking_days': hiking_days,
    })

def dashboard(request):
    hd = HikingDay.objects
    hiking_days = hd.count() - hd.filter(day_off=True).count()
    return render(request, 'appalachian_trail/dashboard.html',{
        'states_list': hd.STATES_LIST,
        'hiking_days_per_state': hd.hiking_days_per_state(),
        'precipitation_days_per_state': hd.precipitation_days_per_state(),
        'hiking_days': hiking_days,
        'days_with_precipitation': hd.filter(precipitation=True).count(),
        'resupply_days': hd.filter(resupply=True).count(),
        'resupplys': hd.resupply_data(),
        'days_off': hd.filter(day_off=True).count(),
        'days_with_precipitation_while_hiking': hd.filter(precip_status__contains='hiking').count(),
        'hiking_dates': hd.hiking_dates(),
        'mileage_per_day': hd.mileage_per_day(),
        'hiking_dates_by_miles_hiked': hd.hiking_dates_by_miles_hiked(),
        'mileage_per_day_by_miles_hiked': hd.mileage_per_day_by_miles_hiked(),
   })

def pictures(request):
    return render(request, 'appalachian_trail/pictures.html')

def faq(request):
    return render(request, 'appalachian_trail/faq.html')

def gear(request):
    return render(request, 'appalachian_trail/gear.html')
