from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ingredients-home'),
    path('menu_items/', views.menu_items, name='ingredients-menu_items'),
    path('purchase_history/', views.purchase_history, name='ingredients-purchase_history'),
    path('add_ingredient/', views.add_ingredient, name='ingredients-add_ingredient'),
    path('update_ingredient/<ingredient_id>', views.update_ingredient, name='ingredients-update_ingredient')
]