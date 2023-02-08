from django.urls import path
from .views import allcars

urlpatterns = [
    path('', allcars, name = 'cars'),
    #path('', allcars, name = 'cars'),
]
