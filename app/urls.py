from django.urls import path
from app.views import *
app_name='something'
urlpatterns=[
    path('new/',new,name='new'),
    path('new1/',new1,name='new1'),
    path('string/',string,name='string'),
]