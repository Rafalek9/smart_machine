from django.contrib import admin
from .models import Fault, FaultCode


class FaultAdmin(admin.ModelAdmin):
    model = Fault
    list_display = ['station', 'pallet', 'product', 'detect_time', 'operator']


class FaultCodeAdmin(admin.ModelAdmin):
    model = FaultCode
    list_display = ['code', 'type', 'description']


admin.site.register(Fault, FaultAdmin)
admin.site.register(FaultCode, FaultCodeAdmin)
