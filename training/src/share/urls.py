  
from django.urls import path
from . import views
from .views import Share

from django.conf.urls import url



app_name = 'share'

urlpatterns = [
    path('' , views.SHAREList.as_view(),name='share_list'),
    path('myshare_list' , views.myshare_list,name='myshare_list'),

    path('insert' , views.share_add,name='insert'),

 
]