  
from django.urls import path
from . import views
# from blog.views import post_add

# from django.conf.urls import url



app_name = 'blog'

urlpatterns = [
    path('' , views.PostList.as_view(),name='post_list'),
    path('main_skills' , views.main_skills,name='main_skills'),
    path('<slug:slug>' ,views.PostDetail.as_view(),name='post_detail' ),
  
  
    
    
    
    # path('<slug:slug>' ,views.PostDetail.as_view(),name='post_detail' ),
    # path('ict' , views.post_add,name='ict'),


]