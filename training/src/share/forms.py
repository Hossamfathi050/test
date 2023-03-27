from django import forms
from . models import Share




class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = '__all__'
        exclude = ['author','created_at','slug']


        #fields = ['teacher_name' , 'supervisiorname']
        #fields = ['teacher_name' , 'supervisiorname']

