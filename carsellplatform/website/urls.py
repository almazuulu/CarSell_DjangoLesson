from django.contrib import admin
from django.urls import path, re_path
from .views import index, contact_us, about_us

urlpatterns = [
    path('', index),
    path('contact/', contact_us ),
    path('about/', about_us ),
]
