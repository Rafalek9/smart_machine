from django.db import models


class Reference(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, blank=True)
    label = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return str(self.name)


class ReferenceDataField(models.Model):
    """
    """
    FIELD_TYPE = [
        ('B', 'BOOL'),
        ('I', 'INT'),
        ('R', 'REAL'),
        ('S', 'STRING'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=2, choices=FIELD_TYPE, default='R')

    def __str__(self):
        return str(self.name)


class ReferenceDataValue(models.Model):
    """
    """
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE, related_name="ReferenceDataValue", null=True, blank=True)
    field = models.ForeignKey(ReferenceDataField, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=50)

    def __str__(self):
        return str(self.reference) + str(' - ') + str(self.field)