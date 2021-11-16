from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_item, name='add_item'),
    path('adjust/<item_id>', views.adjust_item, name='adjust_item'),
    path('remove/<item_id>', views.remove_item, name='remove_item')
]
