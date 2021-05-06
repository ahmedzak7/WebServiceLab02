from django.urls import path
from . import views
from .views import index, getProducts


urlpatterns = [
    path('', views.index, name='index'),
    path('soup/', getProducts, name='soup'), 
]