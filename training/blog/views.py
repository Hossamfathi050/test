from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.views.generic import ListView , DetailView
from .models import Post 
# from taggit.models import Tag
# from django.db.models import Count
# from django.db.models.query_utils import Q



class PostList(ListView):
    model = Post
   # ordering = ['-arrang_post']
    
    # ordering = ['created_at']
    
    paginate_by = 2
   


class PostDetail(DetailView):
    model = Post



def main_skills(request):
    return render(request, 'blog/main_skills.html')
