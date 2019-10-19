from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def hello(request):
#     return HttpResponse('hello rama')

def hello(request):
    return render(request,'home.html',{'name':'rama'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res = val1 + val2
    return render(request,'result.html',{'result':res})