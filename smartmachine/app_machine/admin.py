from django.contrib import admin
from .models import Station, Pallet, Camera, Status


admin.site.register(Station)
admin.site.register(Pallet)
admin.site.register(Camera)
admin.site.register(Status)

