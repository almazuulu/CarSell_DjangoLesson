from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('carslist/', CarsAPIView.as_view()),
    path('carcreate/', CarCreateView.as_view()),
    path('teamslist/', TeamAPIView.as_view()),
    path('teamslist/<str:pk>', TeamAPIView.as_view()),
    path('car/<str:pk>', CarDetailView.as_view()),
    path('team/<str:pk>', TeamDetailView.as_view()),
]