from django.contrib.admin.utils import lookup_field
from rest_framework import serializers

from .models import Airport, Flight


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        depth = 1


