from django.contrib import admin
from .models import Fault, FaultCode, Status
from import_export import resources
from import_export.admin import ImportExportModelAdmin


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



### IMPORT EXPORT ###

# StatusResource
class StatusResource(resources.ModelResource):
    class Meta:
        model = Status

class StatusResourceAdmin(ImportExportModelAdmin):
    resource_class = StatusResource


# FaultCodeResource
class FaultCodeResource(resources.ModelResource):
    class Meta:
        model = FaultCode

class FaultCodeResourceAdmin(ImportExportModelAdmin):
    resource_class = FaultCodeResource


# FaultResource
class FaultResource(resources.ModelResource):
    class Meta:
        model = Fault

class FaultResourceAdmin(ImportExportModelAdmin):
    resource_class = FaultResource