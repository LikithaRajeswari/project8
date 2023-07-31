from django.shortcuts import render,HttpResponse
from django.urls import *

# Create your views here.

def new2(request):
    return render(request,'new2.html')


def new3(request):
    return render(request,'new3.html')