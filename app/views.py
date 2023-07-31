from django.shortcuts import render,HttpResponse

from django.urls import *

# Create your views here.

def new(request):
    return render(request,'new.html')

def new1(request):
    return render(request,'new1.html')

def string(request):
    return HttpResponse('this my first commit')