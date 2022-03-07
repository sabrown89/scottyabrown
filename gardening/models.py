from django.db import models

class Seed(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    species =  models.CharField(max_length=255, blank=True, null=True) # Solanum lycopersicum
    classification =  models.CharField(max_length=255) # vegetable
    sub_classification = models.CharField(max_length=255, blank=True, null=True)
    average_days_to_harvest = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    picture = models.URLField(max_length=255, blank=True, null=True)
