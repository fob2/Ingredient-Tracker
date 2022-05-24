from tkinter import CASCADE
from django.db import models
from datetime import datetime, date

class Ingredients(models.Model):
    ingredients = models.CharField(max_length=30, null=False)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    #stock = models.IntegerField(null=True)

    def __str__(self):
        return self.ingredients

class Menu_Items(models.Model):
    menu_items = models.CharField(max_length=30, null=False)
    ingredients = models.ManyToManyField(Ingredients, through="Stock_Required")
    #price = models.FloatField(null=True)
    
    def __str__(self):
        return self.menu_item

class Stock_Required(models.Model):
    menu_items = models.ForeignKey(Menu_Items, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    ingredients_quantity = models.IntegerField(null=False)
    

""" class Purchase_History(models.Model):
    menu_item = models.ForeignKey(Menu_Items, null=True, on_delete=models.SET_NULL)
    price = models.ForeignKey(Menu_Items, null=True, on_delete=models.SET_NULL, related_name="meal_price")
    date_purchased = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.menu_item} {self.date_purchased}" """


    
    

   
