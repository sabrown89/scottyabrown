from django.db import models


class RunningDay(models.Model):
    day = models.DateField()
    mileage = models.DecimalField(max_digits=4, decimal_places=1)
    location = models.CharField(max_length=255)
    type_of_run = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
