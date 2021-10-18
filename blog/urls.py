from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add-blogpost/', views.add_blogpost, name='add_blogpost'),
    path('<int:blogpost_id>/',views.blog_detail, name='blog_detail'),
]