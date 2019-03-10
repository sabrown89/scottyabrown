from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'prep_time',
        'weeknight',
        'cuisine',
        'publication',
        'page_number',
        'overnight'
    ]

admin.site.register(Recipe, RecipeAdmin)
