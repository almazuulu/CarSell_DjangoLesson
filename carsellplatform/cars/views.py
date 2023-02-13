from django.shortcuts import render
from .models import Car, CarPhoto

# Create your views here.

def allcars(request):
    allcars = Car.objects.all() #select * from cars;
    text_blue = 'text-primary'
    textSome = 'Some$Text$Django$Lesson'
    context = {
        'allcars': allcars,
        'text_blue': text_blue,
        'textSome': textSome,
    }
    
    return render(request, 'cars/cars.html', context)

def cardetails(request, id):
    car = Car.objects.get(pk = id)
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context)
    
