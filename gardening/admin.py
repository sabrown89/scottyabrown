from django.contrib import admin
from .models import Seed

class SeedAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        #'spacing',
        'species',
        'classification',
        'sub_classification',
        #'spring_first_plant_date',
        #'spring_last_plant_date', 
        #'fall_first_plant_date',
        #'fall_last_plant_date',
        #'days_to_transplant',
        'average_days_to_harvest',
        #'planting_depth_in_inches',
        #'start_method',
        'purchase_date',
        'provider',
        'picture'
    ]

admin.site.register(Seed, SeedAdmin)
