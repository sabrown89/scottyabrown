from django.contrib import admin
from .models import RunningDay


class RunningDayAdmin(admin.ModelAdmin):
    list_display = ['day',
                    'mileage',
                    'location',
                    'type_of_run',
                    'notes'
    ]


admin.site.register(RunningDay, RunningDayAdmin)
