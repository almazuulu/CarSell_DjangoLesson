from django.shortcuts import render
from rest_framework import generics
from cars.models import Car
from .serializer import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CarsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        lst = Car.objects.all().values()
        return Response({'cars': list(lst)})
    
    def post(self, request, format=None):
        return Response({'title': 'Ferrari f1'})


# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    
