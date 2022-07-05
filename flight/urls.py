from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .models import Flight
from .views import AirportViewSet, FlightViewSet, FlightInfoApiView

router = DefaultRouter()
router.register('airport', AirportViewSet)
router.register('flight', FlightViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('flight_info', FlightInfoApiView.as_view())
]