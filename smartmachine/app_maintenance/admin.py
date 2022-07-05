from django.contrib import admin
from .models import Fault, FaultCode, Status


class FaultAdmin(admin.ModelAdmin):
    model = Fault
    list_display = ['id', 'code', 'start', 'end', ]


class FaultCodeAdmin(admin.ModelAdmin):
    model = FaultCode
    list_display = ['id', 'description', 'type', 'priority', 'station', ]
    list_filter = ['type', 'priority', 'station', ]


admin.site.register(Fault, FaultAdmin)
admin.site.register(FaultCode, FaultCodeAdmin)
admin.site.register(Status)
