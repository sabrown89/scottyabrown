# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
from django.db.models import ObjectDoesNotExist
from decimal import Decimal
from IPython import embed

class HikingDayManager(models.Manager):
    STATES_LIST = ['GA','NC','TN','VA','WV','MD','PA','NJ','NY','CT','MA','VT','NH','ME']

    def hiking_days_per_state(self):
        days_per_state = self.values('state').annotate(total=Count('state'))
        return [days_per_state.get(state=state)['total'] for state in self.STATES_LIST]

    def precipitation_days_per_state(self):
        precip_days_per_state = self.values('state').filter(precipitation=True).annotate(total=Count('state'))
        result_list = []
        for state in self.STATES_LIST:
            try:
                precip_days = precip_days_per_state.get(state=state)['total']
                result_list.append(precip_days)
            except ObjectDoesNotExist:
                result_list.append(0)
        return result_list

    def days_with_precipitation(self):
        return self.filter(precipitation=True).count()

    def resupply_days(self):
        return self.filter(resupply=True).count()

    def resupply_data(self):
        rs = self.filter(resupply=True).values('day','resupply_location','state').order_by('day')

    def hiking_dates(self):
        return [s['day'].strftime('%Y-%m-%d') for s in self.values('day').order_by('day')]

    def mileage_per_day(self):
        return [hd['miles_hiked'].to_eng_string() for hd in self.values('miles_hiked').order_by('day')]

    def hiking_dates_by_miles_hiked(self):
        return [s['day'].strftime('%Y-%m-%d') for s in self.values('day').filter(day_off=False).order_by('miles_hiked')]

    def mileage_per_day_by_miles_hiked(self):
        return [hd['miles_hiked'].to_eng_string() for hd in self.values('miles_hiked').filter(day_off=False).order_by('miles_hiked')]


    def populate_miles_hiked(self):
        miles = list(self.order_by('mile'))
        for m in miles:
            if m.miles_hiked > 0.0:
                pass
            else:
                previous_mile = miles.index(m) - 1
                miles_hiked = m.mile - miles[previous_mile].mile
                m.miles_hiked = miles_hiked
                print(m.miles_hiked)
                m.save()

    def resupply_data(self):
        days_off = 0
        days = 0
        resupplies = []
        for ad in self.all().order_by('day'):
            days += 1
            if ad.day_off == True:
                days_off += 1
            if ad.resupply == True:
                ad.days_between_resupply = days - days_off
                if len(resupplies) == 0:
                    ad.miles_between_resupply = ad.mile + Decimal('8.2')
                    resupplies.append(ad)
                    days_off = 0
                    days = 0
                else:
                    ad.miles_between_resupply = ad.mile - resupplies[-1].mile
                    resupplies.append(ad)
                    days_off = 0
                    days = 0
        return resupplies

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
    resupply = models.BooleanField(default=False)
    resupply_location = models.CharField(default='', max_length=255, blank=True)
    miles_hiked = models.DecimalField(max_digits=8, decimal_places=1, default=0.0)

    objects = HikingDayManager()
