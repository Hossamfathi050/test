from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

  


def tasksinfo(request):
    return render(request, 'tasksinfo/tasksinfo.html')

