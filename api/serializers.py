from rest_framework import serializers
from .models import UserProfile, CareerSuggestion

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CareerSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSuggestion
        fields = '__all__'
