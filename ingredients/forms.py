from django import forms
from django.forms import ModelForm
from .models import Ingredients

class Ingredients_Form(ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"

class Ingredients_Edit(ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"