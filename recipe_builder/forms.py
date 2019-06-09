from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=200)
