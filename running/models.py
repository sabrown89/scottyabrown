from django.db import models


class RunningDayManager(models.Manager):

    def running_dates(self):
        return [rd['day'].strftime('%Y-%m-%d') for rd in self.values('day').order_by('day')]

    def mileage_per_day(self):
        return [rd['mileage'].to_eng_string() for rd in self.values('mileage').order_by('day')]

class RunningDay(models.Model):
    day = models.DateField()
    mileage = models.DecimalField(max_digits=4, decimal_places=1)
    location = models.CharField(max_length=255)
    type_of_run = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    objects = RunningDayManager()
