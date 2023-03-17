from datetime import timezone
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.db import models

# Create your models here.




SKILLS_CAT=[
    ('انتاج ونصميم المقررات الإلكترونية','انتاج ونصميم المقررات الإلكترونية'),
    ('التقويم الإلكتروني عن بعد','التقويم الإلكتروني عن بعد'),
    ('إدارة الفصول الإفتراضية','إدارة الفصول الإفتراضية'),
    ('تطبيقات الحوسبة السحابية','تطبيقات الحوسبة السحابية'),

    ]

class Post(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField(max_length=15000)
    skills_category = models.CharField(_("skills"),max_length=50,choices= SKILLS_CAT)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True , blank=True)

    arrang_post=models.IntegerField()


   # image = models.ImageField(upload_to='post/')
 #   uploadpdf = models.FileField(upload_to='uploadpdf/')
    # category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    # # slug = models.SlugField(null=True , blank=True)
   
   
    def __str__(self):
          return self.title 
        
        
   
    class Meta:
        ordering = ['arrang_post']
        # ordering = ['-id']
    
    

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.created_at)    
       super(Post, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    


  

# from django import forms
# from . models import Share




# class ShareForm(forms.ModelForm):
#     class Meta:
#         model = Share
#         fields = '__all__'
#         exclude = ['author','created_at','slug']

        


#     def save(self, *args, **kwargs):
#        if not self.slug:
#            self.slug = slugify(self.created_at)    
#        super(Share, self).save(*args, **kwargs) # Call the real save() method

#     def __str__(self):
#         return self.share_title

    
  

#     class Meta:
#         ordering = ['-id']
 


# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name