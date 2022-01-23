from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from .views import PalletViewSet, StationViewSet


router = routers.DefaultRouter()
router.register(r'pallet', PalletViewSet)
router.register(r'station', StationViewSet)

app_name = "app_machine"
urlpatterns = [
    path('api/', include(router.urls)),
]
