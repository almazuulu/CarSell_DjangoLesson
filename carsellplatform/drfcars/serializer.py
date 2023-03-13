from rest_framework import serializers
from django.contrib.auth.models import User
from cars.models import Car
from website.models import Team 



class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    
    class Meta:
        model = Car
        #fields = ('id', 'owner', 'car_title', 'state', 'city', 'color', 'model', 'year', 'condition', 'price', 'features', 'body_style', 'engine', 'transmission', 'interior', 'kilometers', 'doors', 'passengers', 'fuel_type', 'no_of_owners', 'fuel_mileage')
        fields = "__all__"

class CarCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        exclude = ('car_main_photo',)


class CarDetailViewSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)

    class Meta:
        model = Car
        exclude = ('car_main_photo', 'vin_no', 'is_featured', 'created_date', )
        

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class TeamDetailViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        exclude = ('photo', 'created_date', )