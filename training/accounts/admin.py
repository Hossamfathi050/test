
from django.contrib import admin

# Register your models here.
from .models import Profile,User
from import_export.admin import ImportExportModelAdmin



@admin.register(Profile)
class ProfileImportExport(ImportExportModelAdmin):
    pass

