from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cars.models import Car
from website.models import Team
from .serializer import *



class CarsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
        # lst = Car.objects.all().values()
        # return Response({'cars': list(lst)})
    
    # def post(self, request, format=None):
    #     return Response({'title': 'Ferrari f1'})


class CarCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        car = CarCreateSerializer(data=request.data)
        if car.is_valid():
            car.save()
            
        return Response(status=201)


class CarDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        serializer = CarDetailViewSerializer(car)
        
        return Response(serializer.data)
    

class TeamAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        team = TeamSerializer(data=request.data)
        if team.is_valid():
            team.save()
        return Response(status=201)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed!"})
        try:
            isinstance = Team.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist!"})
        
        serializer =  TeamSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    # def post(self, request, format=None):
    #     team_create = Team.objects.create(
    #         first_name = request.data['first_name'],
    #         last_name = request.data['last_name'],
    #         designation = request.data['designation'],
    #     )
        
    #     return Response({'team': model_to_dict(team_create)})
    

class TeamDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        serializer = TeamDetailViewSerializer(team)

        return Response(serializer.data)
        
    
# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    
