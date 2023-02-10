from django.shortcuts import render, HttpResponse
from cars.models import Car
from .models import Team

def index(request):
    teams = Team.objects.all()  # select * from Team;
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    context = {
        'teams': teams,
        'title': 'Cars.KG Home Page',
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'website/index.html', context)

def contact_us(request):
    context = {
        'title': 'Contact us'
    }
    return render(request, 'website/contactus.html', context)

def about_us(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'website/aboutus.html', context)

def services(request):
    context = {
        'title': 'Services'
    }
    return render(request, 'website/services.html', context)



