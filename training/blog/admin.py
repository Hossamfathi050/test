
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin



from .models import Post
@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass

admin.site.site_header=" لوحة التحكم - بيئة التدريب الإلكترونية القائمة على تقنيات الذكاء الإصطناعي  "
admin.site.site_title=" Ai-training-HOSSAM FAHI "

# @admin.register(Post)
class TopicAdmin(admin.ModelAdmin):
    fields=all
    list_display=('title','skills_category','description',)
    search_fields=('skills_category')
    
    
    
     