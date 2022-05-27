from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ingredients-home'),
    path('menu_items/', views.menu_items, name='ingredients-menu_items'),
    path('purchase_history/', views.purchase_history, name='ingredients-purchase_history'),
    path('purchase_history_log/<str:lpk>/', views.purchase_history_log, name='ingredients-purchase_history_log'),
    path('add_ingredient/', views.add_ingredient, name='ingredients-add_ingredient'),
    path('update_ingredient/<str:pk>/', views.update_ingredient, name='ingredients-update_ingredient'),
    path('delete_ingredient/<str:pk>/', views.delete_ingredient, name='ingredients-delete_ingredient'),
    path('add_menu_item/', views.add_menu_item, name='ingredients-add_menu_item'),
    path('update_menu_item/<str:mpk>/', views.update_menu_item, name='ingredients-update_menu_item'),
    path('delete_menu_item/<str:mpk>/', views.delete_menu_item, name='ingredients-delete_menu_item'),
    
]

#path('log_purchase/<str:lpk>/', views.log_purchase, name='ingredients-log_purchase')