from django.urls import path
from .views import AllCarsView, CarDetailsView, SearchView, CarCreateView, CarDeleteView, UpdateCar, OwnersCarsView
urlpatterns = [
    path('', AllCarsView.as_view(), name = 'cars'),
    path('search', SearchView.as_view(), name='search'),
    path('add_car',CarCreateView.as_view(), name='add_car'),
    path('ownerscars/<str:id>', OwnersCarsView.as_view(), name = 'ownerscars'),
    path('cardetails/<str:id>', CarDetailsView.as_view(), name = 'cardetails'),
    path('delete_car/<str:id>', CarDeleteView.as_view(), name = 'delete_car'),
    path('update_car/<uuid:pk>', UpdateCar.as_view(), name = 'update_car'),
]
