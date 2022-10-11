from django.shortcuts import render
from django.http import HttpResponse

from . models import Hot

def index(request):
    nill=Hot.objects.all()
    return render(request,'index.html',{'nill':nill})
    

