import datetime

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from app_maintenance.serializers import FaultSerializer
from app_maintenance.models import Fault
from rest_framework import viewsets
from django.http import JsonResponse


class FaultViewSet(viewsets.ModelViewSet):
    queryset = Fault.objects.all()
    serializer_class = FaultSerializer


def clear_selected_faults(request, code):
    """
    Funkcja widoku. Usuwa aktualne alarmy o przekazanym kodzie błędu.
    Ustawia czas zakończenia usterki na aktualny czas serwera.
    """
    faults = Fault.objects.filter(code=code, end=None, )
    quantity = faults.count()
    for fault in faults:
        fault.end = datetime.datetime.now()
        fault.save()
    json = {
        "fixed code": code,
        "quantity": quantity,
    }
    return JsonResponse(json)


def clear_station_faults(request, station_number):
    """
    Funkcja widoku. Usuwa aktualne alarmy przypisane do numeru stacji.
    Ustawia czas zakończenia usterki na aktualny czas serwera.
    """
    faults = Fault.objects.filter(code__station__number=station_number, end=None, )
    quantity = faults.count()
    for fault in faults:
        fault.end = datetime.datetime.now()
        fault.save()
    json = {
        "fixed station": station_number,
        "quantity": quantity,
    }
    return JsonResponse(json)


def clear_all_faults(request):
    """

    Funkcja widoku. Usuwa aktualne alarmy całej maszyny.
    Ustawia czas zakończenia usterki na aktualny czas serwera.

    """
    faults = Fault.objects.filter(end=None, )
    quantity = faults.count()
    for fault in faults:
        fault.end = datetime.datetime.now()
        fault.save()
    json = {
        "quantity": quantity,
    }
    return JsonResponse(json)