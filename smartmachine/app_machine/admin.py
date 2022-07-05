from django.contrib import admin
from .models import Station, Pallet, Camera
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(Station)
admin.site.register(Pallet)
admin.site.register(Camera)


### IMPORT EXPORT ###

# StationResource
class StationResource(resources.ModelResource):
    class Meta:
        model = Station


# PalletResource
class PalletResource(resources.ModelResource):
    class Meta:
        model = Pallet


# CameraResource
class CameraResource(resources.ModelResource):
    class Meta:
        model = Camera
