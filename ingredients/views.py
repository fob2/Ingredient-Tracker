from django.forms import ModelForm
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.core import serializers
from .forms import *

def home(request):
    ingredients_table = serializers.serialize("python", Ingredients.objects.all())

    context = {
        "ingredients_table":ingredients_table,
    }  
    return render(request, "ingredients/ingredients.html", context)

def menu_items(request):
    menu = serializers.serialize("python", Menu_Items.objects.all())

    context = {
        "menu":menu,
    } 
    return render(request, "ingredients/menu_items.html", context)

def purchase_history(request):

    
    return render(request, "ingredients/purchase_history.html")

def update_ingredient(request, ingredient_id):
    ingredient = Ingredients.objects.get(pk=ingredient_id)

    context = {
        "ingredient":ingredient,
    }
    return render(request, 'ingredients/update_ingredient.html', context)




def add_ingredient(request):
    submitted = False
    if request.method == "POST":
        form = Ingredients_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_ingredient?submitted=True")
    else:
        form = Ingredients_Form
        if "submitted" in request.GET:
            submitted = True

    context = {"form":form, "submitted":submitted}
    return render(request, 'ingredients/add_ingredient.html', context)