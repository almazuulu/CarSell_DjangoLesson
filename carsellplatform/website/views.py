from django.shortcuts import render, HttpResponse
from .models import Team

def index(request):
    teams = Team.objects.all()  # select * from Team;
    cars =  Cars.objects.all()
    context = {
        'teams': teams,
        'cars': cars
    }
    return render(request, 'website/index.html', context)

def contact_us(request):
    return render(request, 'website/contactus.html')

def about_us(request):
    return render(request, 'website/aboutus.html')

def services(request):
    return render(request, 'website/services.html')



