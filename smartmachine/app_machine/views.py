from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Station, Pallet
from .serializers import PalletSerializer, StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class PalletViewSet(viewsets.ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer
