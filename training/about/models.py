
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


Contactus_CAT=[
    ('انتاج ونصميم المقررات الإلكترونية','انتاج ونصميم المقررات الإلكترونية'),
    ('التقويم الإلكتروني عن بعد','التقويم الإلكتروني عن بعد'),
    ('إدارة الفصول الإفتراضية','إدارة الفصول الإفتراضية'),
    ('تطبيقات الحوسبة السحابية','تطبيقات الحوسبة السحابية'),
    ('بيئة التدريب','بيئة التدريب'),
    ('عام','عام'),
    ]


# Create your models here.
class Contactus(models.Model):
    contacter = models.ForeignKey(User, related_name='user_contactus', on_delete=models.CASCADE)
    contact_name = models.CharField(_("اسم المرسل"),max_length=15)
    contactus_title = models.CharField(_("العنوان"),max_length=50)
    contactus_description  = models.TextField(_("- الموضوع"),max_length=500)
    contactus_category = models.CharField(_("المجال"),max_length=50,choices= Contactus_CAT)
    slug = models.SlugField(null=True , blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
 
 
 
    
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.created_at)    
       super(Contactus, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.contactus_title


    class Meta:
        ordering = ['-id']
 

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
 