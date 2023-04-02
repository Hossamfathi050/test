from django.contrib import admin

# Register your models here.
from .models import Contactus
from import_export.admin import ImportExportModelAdmin




@admin.register(Contactus)
class PostImportExport(ImportExportModelAdmin):
    pass

