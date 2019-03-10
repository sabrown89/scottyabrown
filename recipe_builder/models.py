from django.db import models


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    prep_time = models.CharField(max_length=50, blank=True)
    cook_time = models.CharField(max_length=50, blank=True)
    weeknight = models.BooleanField(blank=True)
    cuisine = models.CharField(max_length=100, blank=True)
    publication = models.CharField(max_length=100, blank=True)
    page_number = models.SmallIntegerField(blank=True)
    overnight = models.BooleanField(blank=True)

    class Meta:
        ordering = ('created',)
