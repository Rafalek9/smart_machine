import datetime
from django.db import models
from app_machine.models import Pallet, Station
from app_production.models import Product


class FaultCode(models.Model):
    """
    Lista błędów zarejestrowanych na lini przemysłowej
    """
    code = models.CharField(max_length=10, unique=True)
    TYPE = [
        ('0', '---'),
        ('1', 'SAFETY'),
        ('2', 'MEDIA'),
        ('3', 'PROCESS'),
        ('4', 'PART DEFECT'),
    ]
    type = models.CharField(max_length=1, choices=TYPE, default='0')
    description = models.CharField(max_length=255, blank=True)
    solution = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.code) + " - " + str(self.type)


class Fault(models.Model):
    """
    Opis błędów zgłoszonych przez linie produkcyjną lub operatora.
    Błąd może wskazywać na produkt / paletkę / stację lub jeżeli nic nie zostanie wskazane -
    zgłaszać usterkę globalną linii.
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault')
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault')
    pallet = models.ForeignKey(Pallet, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault')
    detect_time = models.DateTimeField(default=datetime.datetime.now())
    end_time = models.DateTimeField(default=datetime.datetime.now())
    operator = models.IntegerField(null=True, blank=True)
    code = models.ForeignKey(FaultCode, on_delete=models.SET_NULL, null=True, blank=True, related_name='fault')

    def __str__(self):
        return "F#" + str(self.code) + " (" + str(self.station) + ")"


