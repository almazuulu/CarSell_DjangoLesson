from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    # Cars API
    path('carslist/', CarsAPIView.as_view()),
    path('carcreate/', CarCreateAPIView.as_view()),
    path('car/<str:pk>', CarDetailAPIView.as_view()),
    path('carupdate/<str:pk>', CarUpdateAPIView.as_view()),
    path('cardelete/<str:pk>', CarDeleteAPIView.as_view()),
    # Team API
    path('teamslist/', TeamAPIView.as_view()),
    path('team/<str:pk>', TeamDetailView.as_view()),
    path('teamslist/<str:pk>', TeamAPIView.as_view()),
    path('teamdelete/<str:pk>', TeamDeleteAPIView.as_view()),
    # Comment API
    path('commentlist/', CommentAPIView.as_view()),
    path('commentlist/<str:pk>', CommentAPIView.as_view()),
    path('comment/<str:pk>', CommentDetailView.as_view()),
]