from django.shortcuts import render
from .models import *
from django.core import serializers
#from .forms import OrderForm

def home(request):
    ingredredients_table = serializers.serialize("python", Ingredients.objects.all())

    context = {
        "ingredients_table":ingredredients_table,
    }  
    return render(request, "ingredients/ingredients.html", context)

def menu_items(request):
    return render(request, "ingredients/menu_items.html")

def purchase_history(request):
    return render(request, "ingredients/purchase_history.html")






#def add_ingredient(request):
  #  form = OrderForm()

  #  context = {"form":form}
  #  return render(request, "ingredients/add_ingredient.html", context)