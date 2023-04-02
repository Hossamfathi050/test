  
from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    
    # path('contactus' , views.contactus,name='contactus'),
    path('contactme' , views.contactme_add,name='contactme'),
    path('trainer' , views.trainer,name='trainer'),
    path('training_idea' , views.training_idea,name='training_idea'),

]