from django.db.models import Count
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


from .serializers import AirportSerializer, FlightSerializer, FlightInfoSerializer
from .models import Airport, Flight


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    lookup_field = 'code'


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightInfoApiView(ListModelMixin, GenericAPIView):
    serializer_class = FlightInfoSerializer

    def get_queryset(self):
        return Flight.objects.values('flight_number') \
            .annotate(count=Count('flight_number')) \
            .order_by()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
