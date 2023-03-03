from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from cars.utils import get_search_filters
from .forms import ContactForm
from cars.models import Car
from .models import Team


class IndexView(TemplateView):
    template_name = 'website/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_cars'] =  Car.objects.order_by('-created_date').filter(is_featured=True)
        context['all_cars'] = Car.objects.order_by('-created_date')
        context['teams'] = Team.objects.all()  # select * from Team;
        context['title'] = 'Cars.KG Home Page'
        context.update(**get_search_filters())
        
        return context

# def index(request):
#     featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
#     all_cars = Car.objects.order_by('-created_date')
#     context = {
#         'title': 'Cars.KG Home Page',
#         'featured_cars': featured_cars,
#         'all_cars': all_cars,
#         **get_search_filters(),
#     }
#     return render(request, 'website/index.html', context)

class TeamsView(TemplateView):
    template_name = 'website/teams.html'
    
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['teams'] = Team.objects.all()  # select * from Team;
    #     context['something'] = 'something444'

        # return context 


class ContactUsView(FormView):
    template_name = 'website/contactus.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        
        message_mail = f'You have message in CarSelling Platform from { full_name } \
            regarding: {message} \
            \n\nSender Details: Phone: {phone}; Email: {email}'
    
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
            subject,
            mark_safe(message_mail),
            email,
            [admin_email],
            fail_silently=False,
            )
        messages.success(self.request, 'Your message has been successfully sent!')
        
        return super().form_valid(form)
    
    
# def contact_us(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
        
#         if form.is_valid():
#             full_name = form.cleaned_data['full_name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             phone = form.cleaned_data['phone']
#             message = form.cleaned_data['message']
            
#             message_mail = f'You have message in CarSelling Platform from { full_name } \
#             regarding: {message} \
#             \n\nSender Details: Phone: {phone}; Email: {email}'
    
#             admin_info = User.objects.get(is_superuser=True)
#             admin_email = admin_info.email
        
#             send_mail(
#             subject,
#             mark_safe(message_mail),
#             email,
#             [admin_email],
#             fail_silently=False,
#             )
#             messages.success(request, 'Your message has been successfully sent!')
#     else:
#         form = ContactForm()
    
#     context = {
#         'title': 'Contact us',
#         'form': form,
        
#     }
#     return render(request, 'website/contactus.html', context)

class AboutView(TemplateView):
    template_name = 'website/aboutus.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About us'
        context['teams'] = Team.objects.all()
        
        return context
        

# def about_us(request):
#     context = {
#         'title': 'About us'
#     }
#     return render(request, 'website/aboutus.html', context)

class ServiceView(TemplateView):
    template_name = 'website/services.html'
    






