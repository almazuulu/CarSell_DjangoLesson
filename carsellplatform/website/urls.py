from django.contrib import admin
from django.urls import path, re_path
from .views import IndexView, contact_us, ServiceView, AboutView, TeamsView

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'),
    path('contact/', contact_us, name ='contact'),
    path('about/', AboutView.as_view(), name = 'aboutus'),
    path('services', ServiceView.as_view(), name='services'),
    path('teams', TeamsView.as_view(), name='teams'),
]
