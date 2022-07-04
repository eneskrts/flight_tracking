from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AirportViewSet, FlightViewSet

router = DefaultRouter()
router.register('airport', AirportViewSet)
router.register('flight', FlightViewSet)

urlpatterns = [
    path('', include(router.urls))
]