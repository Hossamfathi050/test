from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView
from .models import Contactus
from django.db.models import Count
from django.db.models.query_utils import Q

from . forms import ContactusForm



class ContactusList(ListView):
    model = Contactus
     
    # ordering = ['created_at']
    
    # paginate_by =15  
   
  
    # ===========================================


# def Contactus_add(request,*args,**kwargs):
#     if request.method == 'POST':
#         form =ContactusForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.contacter = request.user
#             form.save()
#             return redirect('/about/')
#     else:
#         form = ContactusForm()
#         return render(request, 'about/contactus.html',{'form':form})

# ===========================================


def contactme_add(request,*args,**kwargs):
    if request.method == 'POST':
        form =ContactusForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.contacter = request.user
            form.save()
            
            return render(request, 'about/thanks.html')

            # return redirect('/about/thanks.html')
    else:
        form = ContactusForm()
        return render(request, 'about/contactme.html',{'form':form})

 
# =========================================

def trainer(request):
    return render(request, 'about/trainer.html')


def training_idea(request):
    return render(request, 'about/training_idea.html')


  

def contactus(request):
    return render(request, 'about/contactus.html')


  
