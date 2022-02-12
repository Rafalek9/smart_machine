from django.contrib import admin
from .models import Fault, FaultCode


class FaultAdmin(admin.ModelAdmin):
    model = Fault
    list_display = ['id', 'code', 'start', 'end', ]


class FaultCodeAdmin(admin.ModelAdmin):
    model = FaultCode
    list_display = ['id', 'type', 'priority', 'station', ]


admin.site.register(Fault, FaultAdmin)
admin.site.register(FaultCode, FaultCodeAdmin)
