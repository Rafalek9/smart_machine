from django.contrib import admin
from .models import Product, Process, ProcessDataField, ProcessDataValue, Image
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProcessDataFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "station", )
    list_filter = ("name", "type", "station", )


class ProcessDataValueAdmin(admin.ModelAdmin):
    model = ProcessDataValue


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'reference', 'status', ]
    list_filter = ['status', 'reference', ]


class ProcessAdmin(admin.ModelAdmin):
    model = Process
    list_display = ['product', 'station', 'pallet', 'status', 'start_process', ]
    list_filter = ['station', 'pallet', 'status', 'start_process', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ProcessDataField, ProcessDataFieldAdmin)
#admin.site.register(ProcessDataValue, ProcessDataValueAdmin)
admin.site.register(Image)


