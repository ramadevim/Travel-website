from django.shortcuts import render

# Create your views here.
from .models import Destination

def index(request):
    dest1=Destination.objects.all()
    return render(request,'index.html',{'dests':dest1})