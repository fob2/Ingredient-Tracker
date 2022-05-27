from django.forms import ModelForm
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from .forms import *

def home(request):
    ingredients = Ingredients.objects.all()

    context = {
        "ingredients":ingredients,
    }  
    return render(request, "ingredients/ingredients.html", context)

def menu_items(request):
    menu = Menu_Items.objects.all()

    context = {
        "menu":menu,
    } 
    return render(request, "ingredients/menu_items.html", context)

def purchase_history(request):
    menu = Menu_Items.objects.all()

    context = {
        "menu_item":menu
    }
    
    return render(request, "ingredients/purchase_history.html", context)

def purchase_history_log(request, lpk):

    menu = Menu_Items.objects.get(id=lpk)

    if request.method == "POST":
        return redirect("/purchase_history/")

    context = {
        "menu_item":menu
    }

    return render(request, "ingredients/purchase_history_log.html", context)

def update_ingredient(request, pk):
    
    ingredient = Ingredients.objects.get(id=pk)
    form = Ingredients_Form(instance=ingredient)
 
    if request.method == "POST":
        form = Ingredients_Form(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {"form":form}
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

def delete_ingredient(request, pk):
    ingredient = Ingredients.objects.get(id=pk)
    if request.method == "POST":
        ingredient.delete()
        return redirect("/")

    context = {"ingredient":ingredient}
    return render(request, "ingredients/delete.html", context)

def add_menu_item(request):
    submitted = False
    if request.method == "POST":
        form = Menu_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_menu_item?submitted=True")
    else:
        form = Menu_Form
        if "submitted" in request.GET:
            submitted = True

    context = {"form":form, "submitted":submitted}
    return render(request, 'ingredients/add_menu_item.html', context)

def delete_menu_item(request, mpk):

    item = Menu_Items.objects.get(id=mpk)
    if request.method == "POST":
        item.delete()
        return redirect("/menu_items/")

    context = {"item":item}
    return render(request, "ingredients/delete_menu_item.html", context)

def update_menu_item(request, mpk):
    
    item = Menu_Items.objects.get(id=mpk)
    form = Menu_Form(instance=item)
 
    if request.method == "POST":
        form = Menu_Form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/menu_items/")
    
    context = {"form":form}
    return render(request, 'ingredients/update_menu_item.html', context)

""" def log_purchase(request, lpk):

    item = Menu_Items.objects.get(id=lpk)
    system = request.POST.get("{{ item }}", None)
    form = Purchase_Form(request.POST, instance=item)

    if request.method == "POST":
        form = Purchase_Form
        form.save()
        return redirect("/purchase_history")

    context = {"form":form, "item":item, "system":system} 
    return render(request, 'ingredients/log_purchase.html', context) """

