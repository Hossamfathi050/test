from django.contrib import admin

# Register your models here.
from .models import Share
from import_export.admin import ImportExportModelAdmin




@admin.register(Share)
class PostImportExport(ImportExportModelAdmin):
    pass

