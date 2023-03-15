from rest_framework import serializers
from django.contrib.auth.models import User
from cars.models import Car
from website.models import Team 
from uaccounts.models import Comment



class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    
    class Meta:
        model = Car
        #fields = ('id', 'owner', 'car_title', 'state', 'city', 'color', 'model', 'year', 'condition', 'price', 'features', 'body_style', 'engine', 'transmission', 'interior', 'kilometers', 'doors', 'passengers', 'fuel_type', 'no_of_owners', 'fuel_mileage')
        fields = "__all__"

def validate_features(value_list):
    allowed_options = [option[0] for option in Car.featured_options]
    invalid_values = [value for value in value_list if value not in allowed_options]
    
    if invalid_values:
        raise serializers.ValidationError(f"Invalid feature values: {', '.join(invalid_values)}")
    return value_list

class CarCreateSerializer(serializers.ModelSerializer):
    features = serializers.ListField(child=serializers.CharField(), validators=[validate_features])
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
      
        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class CommentDetailViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('date_added',)