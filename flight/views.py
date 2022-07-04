from rest_framework import viewsets
from rest_framework.generics import GenericAPIView

from .serializers import AirportSerializer, FlightSerializer
from.models import Airport, Flight


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    lookup_field = 'code'


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


