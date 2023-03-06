from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .utils import get_search_filters, CarOwnerOrAdminMixin
from .forms import CarForm, CarsPhotoForm
from uaccounts.forms import CommentForm
from .models import Car, CarPhoto


class AllCarsView(TemplateView):
    template_name = 'cars/cars.html'
    
    def get_context_data(self, **kwargs):
        allcars = Car.objects.all() #select * from cars;
        paginator = Paginator(allcars, 4)
        page = self.request.GET.get('page')
        paged_cars = paginator.get_page(page)
        
        context = super().get_context_data(**kwargs)
        context['allcars'] = allcars
        context['paged_cars'] = paged_cars
        context.update(**get_search_filters())
        
        return context        

# def allcars(request):
#     allcars = Car.objects.all() #select * from cars;
#     paginator = Paginator(allcars, 2)
#     page = request.GET.get('page')
#     paged_cars = paginator.get_page(page)
    
#     context = {
#         'paged_cars': paged_cars,
#         'allcars': allcars,
#         **get_search_filters(),
#     }
    
#     return render(request, 'cars/cars.html', context)


class CarDetailsView(DetailView):
    model = Car
    template_name = 'cars/car-details.html'
    context_object_name = 'car'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

# def cardetails(request, id):
#     car = Car.objects.get(pk = id)
#     context = {
#         'car': car,
#     }
#     return render(request, 'cars/car-details.html', context)

class SearchView(View):
    def get(self, request):
        cars = Car.objects.order_by('-created_date')
        
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
            **get_search_filters(),
        }
        return render(request, 'cars/search.html', context)
    
# def search(request):
#     cars = Car.objects.order_by('-created_date')
    
#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
#         if keyword:
#             cars = cars.filter(description__icontains = keyword) 
    
#     if 'model' in request.GET:
#         model = request.GET['model']
        
#         if model:
#             cars = cars.filter(model__iexact = model)
    
#     if 'city' in request.GET:
#         city = request.GET['city']
        
#         if city:
#             cars = cars.filter(city__iexact = city)
            
#     if 'year' in request.GET:
#         year = request.GET['year']
        
#         if year:
#             cars = cars.filter(year__iexact = year)
        
#     if 'body_style' in request.GET:
#         body_style = request.GET['body_style']
        
#         if body_style:
#             cars = cars.filter(body_style__iexact = body_style)
    
#     if 'transmission' in request.GET:
#         transmission = request.GET['transmission']
        
#         if transmission:
#             cars = cars.filter(transmission__iexact = transmission)
    
#     if 'min_price' in request.GET:
#         min_price = request.GET['min_price']
#         max_price = request.GET['max_price']

#         if max_price:
#             cars = cars.filter(price__gte=min_price, price__lte=max_price )

#     context = {
#         'cars': cars,
#         **get_search_filters(),
#     }
#     return render(request, 'cars/search.html', context)

    
class CarCreateView(LoginRequiredMixin, CreateView):
        model = Car
        login_url = 'login'
        form_class = CarForm
        template_name = 'cars/add_car.html'
        
        def get_success_url(self):
            id = self.object.id
            return reverse_lazy('cardetails', kwargs={'id': id})
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.POST:
                context['car_photos'] = [CarsPhotoForm(self.request.POST, self.request.FILES, prefix=str(x)) for x in range(3)]
            else:
                context['car_photos'] = [CarsPhotoForm(prefix=str(x)) for x in range(3)]

            return context
            
        def form_valid(self, form):
            context = self.get_context_data()
            car_photos = context['car_photos']
            
            with transaction.atomic():
                form.instance.owner = self.request.user
                self.object = form.save()
                if car_photos and all([photo.is_valid() for photo in car_photos]):
                    for photo in car_photos:
                        photo.instance.car_photo = self.object
                        photo.save()
                        
            return super().form_valid(form)
    
#@login_required(login_url='login')
#def add_car(request):
#     if request.method == 'POST':
#         car_form = CarForm(request.POST, request.FILES)
#         cars_photo_form = CarsPhotoForm(request.POST, request.FILES)
        
#         if car_form.is_valid() and cars_photo_form.is_valid():
#             car = car_form.save(commit=False)
#             car.owner = request.user
#             car.save()
#             cars_photo_form.instance.car_photo = car
#             cars_photo_form.save()
            
#             # Saving main photo
#             if 'car_main_photo' in request.FILES:
#                 car.car_main_phot = request.FILES['car_main_photo']
#                 car.save()
#             return redirect('cardetails', id = car.id)
#     else:
#         car_form = CarForm()
#         cars_photo_form = CarsPhotoForm()
    
#     return render(request, 'cars/add_car.html', {
#         'car_form': car_form,
#         'cars_photo_form': cars_photo_form,
#     })


class CarDeleteView(LoginRequiredMixin, CarOwnerOrAdminMixin, DeleteView):
    model = Car
    login_url = 'login'
    success_url = reverse_lazy('user_cars')
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['car'] = self.object.car_title
        return context
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs )
    
@login_required(login_url='login')
def delete_car(request, id):
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    Car.objects.filter(id=id, owner=user).delete()
    messages.success(request, 'Your car was successfully deleted!')

    return redirect('/accounts/user_cars')


class UpdateCar(LoginRequiredMixin, CarOwnerOrAdminMixin, UpdateView):
        model = Car
        login_url = 'login'
        form_class = CarForm
        template_name = 'cars/update_car.html'
        
        def get_success_url(self):
            id = self.object.id
            return reverse_lazy('cardetails', kwargs={'id': id})
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.POST:
                context['car_photos'] = [CarsPhotoForm(self.request.POST, self.request.FILES, prefix=str(x), instance = self.object.carphoto_set.all()[x-1]) for x in range(1,4)]
            else:
                car_photos = self.object.carphoto_set.all()
                if len(car_photos) == 3:
                    context['car_photos'] = [CarsPhotoForm(prefix=str(x), instance = car_photos[x-1]) for x in range(1,4)]
                else:
                    context['car_photos'] = [CarsPhotoForm(prefix=str(x)) for x in range(1,4)]
                    
            return context
                
        def form_valid(self, form):
            context = self.get_context_data()
            car_photos = context['car_photos']
            
            with transaction.atomic():
                form.instance.owner = self.request.user
                self.object = form.save()
                
                for i, photo in enumerate(car_photos):
                    if photo.is_valid():
                        photo.instance.car_photo = self.object
                        photo.save()
                    else:
                        photo = CarPhoto.objects.get(car_photo=self.object, id=i+1)
                        photo.delete()
                        
            return super().form_valid(form)


class OwnersCarsView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        usercars  = user.cars.all()
        
        context ={
            'owner': user,
            'usercars': usercars,
        }
        
        return render(request, 'cars/ownerscars.html', context)
        
    
    
# @login_required(login_url='login')
# def update_car(request, id):
#     user_id = request.user.id
#     user = User.objects.get(id = user_id)
#     car = get_object_or_404(Car, id=id, owner=user)
    
#     if request.method == "POST":
#         car_form = CarForm(request.POST, instance=car)
        
#         if car_form.is_valid():
#             car = car_form.save(commit = False)
#             car.save()
            
#             #Updating main photo
#             if 'car_main_photo' in request.FILES:
#                 car.car_main_photo = request.FILES['car_main_photo']
#                 car.save()
                
#                 return redirect('cardetails', id=car.id)

#             return redirect('cardetails', id=car.id)
            
#     else:
#         car_form = CarForm(instance=car)
    
#     context = {
#             'car_form': car_form,
#             'car': car,
#     }
#     return render(request, 'cars/update_car.html', context)
