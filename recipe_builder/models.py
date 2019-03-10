from django.db import models


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    prep_time = models.CharField(max_length=50, blank=True)
    cook_time = models.CharField(max_length=50, blank=True)
    weeknight = models.BooleanField(default=False)
    cuisine = models.CharField(max_length=100, blank=True)
    publication = models.CharField(max_length=100, blank=True)
    page_number = models.SmallIntegerField(default=0)
    overnight = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    ingredient_amounts = models.ManyToManyField(Recipe, through='IngredientAmount')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
