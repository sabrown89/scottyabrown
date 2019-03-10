from django.shortcuts import render
from recipe_builder.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(
        request,
        'recipe_builder/index.html', {
            'recipes': recipes
        }
    )

