from weatherdata.views import *
from django.urls import path , include

urlpatterns = [
    path('',index,name='index'),
    path('home',home,name='home'),
]