from django.db import models
from django.db import models

class Seed(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    spacing = models.IntegerField(blank=True)
    species =  models.CharField(max_length=255, blank=True) # Solanum lycopersicum
    classification =  models.CharField(max_length=255) # vegetable
    started = models.DateField(blank=True)
    staring_soil = models.CharField(max_length=255, blank=True)
    planting_start_days_to_first_frost = models.IntegerField(blank=True)#
    planting_end_days_to_first_frost = models.IntegerField(blank=True)
    planting_depth_in_inches = models.IntegerField(blank=True)
    planting_method = models.CharField(max_length=255, blank=True) # direct sow, 
    picture = models.URLField(max_length=255, blank=True)
