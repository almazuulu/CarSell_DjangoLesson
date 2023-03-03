from .models import Car
from django.contrib.auth.mixins import UserPassesTestMixin

def get_search_filters():
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    year_search = list(set(year_search))
    year_search.sort()
    bs_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    
    context = {
        'model_search': set(model_search),
        'city_search': set(city_search),
        'transimssion_search': set(transmission_search),
        'bs_style_search': set(bs_search),
        'year_search': year_search,
    }

    return context

class CarOwnerOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner or self.request.user.is_superuser

