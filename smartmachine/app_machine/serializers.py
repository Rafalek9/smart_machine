from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Station, Pallet


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['number', 'title', 'type', ]


class PalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pallet
        fields = ['number', 'type', 'register_date', 'number_of_cycle', 'cycle_limit', 'defect_limit', ]
