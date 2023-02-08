from django.shortcuts import render
from .models import Car, CarPhoto

# Create your views here.

def allcars(request):
    allcars = Car.objects.all() #select * from cars;
    
    context = {
        'allcars': allcars
    }
    
    return render(request, 'cars/cars.html', context)
