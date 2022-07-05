from django.contrib import admin
from .models import Reference
from import_export import resources


admin.site.register(Reference)
