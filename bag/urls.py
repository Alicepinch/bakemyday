from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_item, name='add_item'),
    path('adjust/<item_id>', views.adjust_item, name='adjust_item')
]