from django.contrib import admin
from .models import Car, CarPhoto
from django.utils.html import format_html


class CarImageAdmin(admin.StackedInline):
    model = CarPhoto

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        html_code = '<img src = "{}" width= "40" style ="border-radius: 50px;"/>'
        return format_html(html_code.format(object.car_main_photo.url))
    
    inlines = [CarImageAdmin]
    list_display = ('thumbnail', 'car_title', 'model', 'color', 'year', 'fuel_type', 'is_featured')
    search_fields = ('car_title', 'model',  'fuel_type', 'body_style')
    list_filter = ('fuel_type', 'color', 'color')
    list_display_links = ('thumbnail', 'car_title')
    list_editable = ('is_featured',)
    
    class Meta:
        model = Car
        
@admin.register(CarPhoto)
class CarImageAdmin(admin.ModelAdmin):
    pass