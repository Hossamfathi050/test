from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


SHARE_CAT=[
    ('انتاج ونصميم المقررات الإلكترونية','انتاج ونصميم المقررات الإلكترونية'),
    ('التقويم الإلكتروني عن بعد','التقويم الإلكتروني عن بعد'),
    ('إدارة الفصول الإفتراضية','إدارة الفصول الإفتراضية'),
    ('تطبيقات الحوسبة السحابية','تطبيقات الحوسبة السحابية'),
    ]


# Create your models here.
class Share(models.Model):
    author = models.ForeignKey(User, related_name='user_share', on_delete=models.CASCADE)
    author_name = models.CharField(_("الاسم"),max_length=15)

    share_title = models.CharField(_("العنوان"),max_length=50)
    description  = models.TextField(_("التعليق-حشد المصادر"),max_length=500)
    share_category = models.CharField(_("المجال"),max_length=50,choices= SHARE_CAT)
    slug = models.SlugField(null=True , blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
 
    

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.created_at)    
       super(Share, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.share_title


    class Meta:
        ordering = ['-id']
 


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name