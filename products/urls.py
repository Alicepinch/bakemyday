from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        '<int:product_id>/',
        views.product_detail, name='product_detail'),
    path(
        'add-product/',
        views.add_product, name='add_product'),
    path(
        'delete-product/<int:product_id>/',
        views.delete_product, name='delete_product'),
    path(
        'edit-product/<int:product_id>/',
        views.edit_product, name='edit_product'),
]
