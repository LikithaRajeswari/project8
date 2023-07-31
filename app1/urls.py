from django.urls import path
from app1.views import *
app1_name='nothing'
urlpatterns=[
    path('new2/',new2,name='new2'),
    path('new3/',new3,name='new3'),
]