from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView
from .models import Share
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q

from . forms import ShareForm



class SHAREList(ListView):
    model = Share
     
    # ordering = ['created_at']
    
    paginate_by =15  
   
  


def myshare_list(request):
      user_share = Share.objects.filter(author=request.user)
      return render(request,'myshare_list.html' , {'user_share':user_share})

    

def share_add(request,*args,**kwargs):
    if request.method == 'POST':
        form =ShareForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            # return redirect('/share/')
            return redirect('/accounts/my_share')
    else:
        form = ShareForm()
        return render(request, 'share/share_add.html',{'form':form})
