import datetime
from django.db import models
from app_machine.models import Pallet, Station
from app_production.models import Product


class FaultCode(models.Model):
    """
    Lista błędów zarejestrowanych na lini przemysłowej (do dodania - pole z referencją?)
    """
    TYPE = [
        (0, '---'),
        (1, 'SAFETY'),
        (2, 'MEDIA'),
        (3, 'PROCESS'),
        (4, 'DEVICE'),
        (5, 'OTHER'),
    ]
    PRIORITY = [
        (0, 'CRITICAL'),
        (1, 'HIGH'),
        (2, 'MEDIUM'),
        (3, 'LOW'),
        (4, 'INFO'),
        (5, '---'),
    ]
    type = models.IntegerField(choices=TYPE, default=0)
    priority = models.IntegerField(choices=PRIORITY, default=5)
    description = models.CharField(max_length=255, blank=True)
    solution = models.CharField(max_length=255, blank=True)

    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault_code')

    def __str__(self):
        return str(self.id)


class Fault(models.Model):
    """
    Opis błędów zgłoszonych przez linie produkcyjną lub operatora.
    Błąd może wskazywać na produkt / paletkę / stację lub jeżeli nic nie zostanie wskazane -
    zgłaszać usterkę bez powiązań.
    """
    code = models.ForeignKey(FaultCode, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault')
    start = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault') # if the station is producing
    pallet = models.ForeignKey(Pallet, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault')   # if the station has pallet -> mayby not have component
    operator = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "F#" + str(self.code)


class Status(models.Model):
    """
    Machine operating status
    """
    NOP = 0
    OFF = 1
    HOMING = 2
    CHANGEOVER = 3
    PRODUCTION = 4
    MANU = 5
    ALARM = 6
    SAFETY = 7

    STATUS_TYPE = [
        (NOP, '---'),
        (OFF, 'OFF'),
        (HOMING, 'Bazowanie'),
        (CHANGEOVER, 'Przezbrojenie'),
        (PRODUCTION, 'Produkcja'),
        (MANU, 'Tryb ręczny'),
        (ALARM, 'Awaria'),
        (SAFETY, 'Błąd bezpieczeństwa'),
    ]

    type = models.SmallIntegerField(choices=STATUS_TYPE, default=0)
    station = models.ForeignKey(Station, null=True, on_delete=models.SET_NULL, blank=True, related_name='status')
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.station) + str(' - ') + str(self.type)