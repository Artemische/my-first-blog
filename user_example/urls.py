
from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('roboti', views.rob, name='rob'),
    path('avtom1', views.avt, name='rob'),
    path('avtom2', views.avtt, name='rob'),

]
