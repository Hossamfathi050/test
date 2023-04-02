  
from django.urls import path
from . import views
 
from django.conf.urls import url



app_name = 'tasksinfo'

urlpatterns = [
     path('tasksinfo' , views.tasksinfo,name='tasksinfo'),

 
]