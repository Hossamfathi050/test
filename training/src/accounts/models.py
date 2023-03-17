from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils.translation import gettext_lazy as _

 
# 
# Create your models here.



Style_Traning=[
    ('تنافسي','تنافسي'),
    ('تشاركي','تشاركي'),
    ]



class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/'  , blank=True, null=True)
    phone_number = models.CharField(max_length=16 , blank=True, null=True)
    school = models.CharField(max_length=50 , blank=True, null=True)
    style_traning=models.CharField(max_length=50,choices= Style_Traning)
     
    def __str__(self):
        return str(self.user)

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            