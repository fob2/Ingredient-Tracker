from django import forms
from django.forms import ModelForm
from .models import *

class Ingredients_Form(ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"

class Menu_Form(ModelForm):
    class Meta:
        model = Menu_Items
        fields = "__all__"

class Purchase_Form(ModelForm):
    class Meta:
        model = Purchase_History
        fields = ("menu_item",)

