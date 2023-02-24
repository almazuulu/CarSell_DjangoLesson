from django.shortcuts import render, redirect
from .models import Car, CarPhoto
from django.core.paginator import Paginator
from .forms import CarForm, CarsPhotoForm
from django.contrib.auth.decorators import login_required

def allcars(request):
    allcars = Car.objects.all() #select * from cars;
    paginator = Paginator(allcars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    year_search = list(set(year_search))
    year_search.sort()
    bs_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transimssion_search = Car.objects.values_list('transmission', flat=True).distinct()
    
    context = {
        'model_search': set(model_search),
        'city_search': set(city_search),
        'transimssion_search': set(transimssion_search),
        'bs_style_search': set(bs_style_search),
        'year_search': year_search,
        'paged_cars': paged_cars,
        'allcars': allcars,
    }
    
    return render(request, 'cars/cars.html', context)

def cardetails(request, id):
    car = Car.objects.get(pk = id)
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context)


def search(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    year_search = list(set(year_search))
    year_search.sort()
    bs_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains = keyword) 
    
    if 'model' in request.GET:
        model = request.GET['model']
        
        if model:
            cars = cars.filter(model__iexact = model)
    
    if 'city' in request.GET:
        city = request.GET['city']
        
        if city:
            cars = cars.filter(city__iexact = city)
            
    if 'year' in request.GET:
        year = request.GET['year']
        
        if year:
            cars = cars.filter(year__iexact = year)
        
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        
        if body_style:
            cars = cars.filter(body_style__iexact = body_style)
    
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        
        if transmission:
            cars = cars.filter(transmission__iexact = transmission)
    
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price )

    
    context = {
        'cars': cars,
        'model_search': set(model_search),
        'city_search': set(city_search),
        'transimssion_search': set(transmission_search),
        'bs_style_search': set(bs_search),
        'year_search': year_search,
    }
    return render(request, 'cars/search.html', context)

@login_required
def add_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        cars_photo_form = CarsPhotoForm(request.POST, request.FILES)
        
        if car_form.is_valid() and cars_photo_form.is_valid():
            car = car_form.save(commit=False)
            car.save()
            cars_photo_form.instance.car_photo = car
            cars_photo_form.save()
            
            # Saving main photo
            if 'car_main_photo' in request.FILES:
                car.car_main_phot = request.FILES['car_main_photo']
                car.save()
            return redirect('cardetails', id = car.id)
    else:
        car_form = CarForm()
        cars_photo_form = CarsPhotoForm()
    
    return render(request, 'cars/add_car.html', {
        'car_form': car_form,
        'cars_photo_form': cars_photo_form,
    })

    
            
    
    