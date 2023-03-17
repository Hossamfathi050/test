from django.urls import path

#from .views import profile , profile_edit , signup , my_reservation , add_feedback
# from .views import myproperty


from .views import profile , profile_edit , signup , my_share,logged_out




app_name = 'accounts'

urlpatterns = [
    path('logged_out',logged_out,name='logged_out'),
    path('signup',signup , name='signup'),
    path('mydata',profile,name='mydata'),
    path('profile/',profile,name='profile'),
    path('profile/edit/', profile_edit , name='profile_edit') ,
    path('my_share', my_share , name='my_share') ,


    # path('profile/myproperty', myproperty , name='myproperty') ,



 #  path('profile/booking', my_reservation , name='my_reservation') ,
  # path('profile/booking/<slug:slug>/review', add_feedback , name='add_feedback') 
]
