from django.contrib import admin
from .models import Product, Process, ProcessDataField, ProcessDataValue, Image
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProcessDataFieldAdmin(admin.ModelAdmin):
    model = ProcessDataField


class ProcessDataValueAdmin(admin.ModelAdmin):
    model = ProcessDataValue


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'reference', 'status', ]
    list_filter = ['status', 'reference', ]


class ProcessAdmin(admin.ModelAdmin):
    model = Process
    list_display = ['product', 'station', 'pallet', 'status', 'start_process', ]
    list_filter = ['product', 'station', 'pallet', 'status', 'start_process', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ProcessDataField, ProcessDataFieldAdmin)
admin.site.register(ProcessDataValue, ProcessDataValueAdmin)
admin.site.register(Image)



### IMPORT EXPORT ###

# ProductResource
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProductResourceAdmin(ImportExportModelAdmin):
    resource_class = ProductResource


# ProcessResource
class ProcessResource(resources.ModelResource):
    class Meta:
        model = Process

class ProcessResourceAdmin(ImportExportModelAdmin):
    resource_class = ProcessResource


# ProcessDataFieldResource
class ProcessDataFieldResource(resources.ModelResource):
    class Meta:
        model = ProcessDataField

class ProcessDataFieldResourceAdmin(ImportExportModelAdmin):
    resource_class = ProcessDataFieldResource


# ProcessDataValueResource
class ProcessDataValueResource(resources.ModelResource):
    class Meta:
        model = ProcessDataValue

class ProcessDataValueResourceAdmin(ImportExportModelAdmin):
    resource_class = ProcessDataValueResource


# ImageResource
class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

class ImageResourceAdmin(ImportExportModelAdmin):
    resource_class = ImageResource
