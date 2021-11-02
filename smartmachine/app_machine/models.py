import datetime

from django.db import models
from django.contrib.auth.models import User



class Station(models.Model):
    """
    Opis stacji/stanowiska na lini produkcyjnej
    """
    STATION_TYPE = [
        ('M', 'Manual process'),
        ('A', 'Auto process'),
        ('SA', 'Semi-auto process'),
    ]
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=STATION_TYPE, default='SA')

    def __str__(self):
        return "ST " + str(self.number)


class Pallet(models.Model):
    """
    Opis paletki produkcyjnej
    """
    number = models.IntegerField(unique=True)
    type = models.IntegerField(default=0)
    register_date = models.DateTimeField(default=datetime.datetime.now())
    number_of_cycle = models.BigIntegerField(default=0)
    cycle_limit = models.IntegerField(default=1000)
    defect_limit = models.IntegerField(default=100)

    def __str__(self):
        return str(self.number)


class Camera(models.Model):
    """
    Opis kamer na linii produkcyjnej
    """
    name = models.CharField(max_length=20)
    station = models.ForeignKey(Station, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return str(self.name)