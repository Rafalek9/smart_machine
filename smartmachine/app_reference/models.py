from django.db import models


class Reference(models.Model):
    """
    Opis referencji przyspisnych do lini produkcyjnej
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.name)
