from django.contrib import admin
from .models import Reference, ReferenceDataField, ReferenceDataValue


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "label", )
    list_filter = ("name", "code", "label", )


@admin.register(ReferenceDataField)
class ReferenceDataFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "description", )
    list_filter = ("name", "type", )


@admin.register(ReferenceDataValue)
class ReferenceDataValueAdmin(admin.ModelAdmin):
    list_display = ("reference", "field", "value", )
    list_filter = ("reference", "field", )
