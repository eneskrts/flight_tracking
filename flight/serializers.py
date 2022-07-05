from django.contrib.admin.utils import lookup_field
from rest_framework import serializers

from .models import Airport, Flight


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    from_airport_id = serializers.PrimaryKeyRelatedField(queryset=Airport.objects.all(),
                                                         source="from_airport", write_only=True)
    to_airport_id = serializers.PrimaryKeyRelatedField(queryset=Airport.objects.all(),
                                                       source="to_airport", write_only=True)

    class Meta:
        model = Flight
        fields = '__all__'
        depth = 1


class FlightInfoSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Flight
        fields = ('flight_number', 'count')


