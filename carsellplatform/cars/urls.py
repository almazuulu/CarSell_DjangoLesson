from django.urls import path
from .views import allcars, cardetails

urlpatterns = [
    path('', allcars, name = 'cars'),
    path('<str:id>', cardetails, name = 'cardetails')
]
