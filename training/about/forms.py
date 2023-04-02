from django import forms
from . models import Contactus




class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
        exclude = ['contacter','created_at','slug']

 



 

