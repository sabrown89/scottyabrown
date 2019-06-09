from django.shortcuts import render

from recipe_builder.models import Recipe
from recipe_builder.forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    return render(
        request,
        'recipe_builder/index.html', {
            'recipes': recipes
        }
    )

def create(request):
    import pdb
    pdb.set_trace()
    if request.method == 'GET':
        return render(request, 'recipe_builder/create.html')

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            return render('recipe_builder/index.html')
    else:
        form = RecipeForm()

    return render(request, 'recipe_builder/index.html', {'form': form})
