from django.conf.urls import url
from django.contrib import admin

from uploads.core import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('main/', views.index, name='main'),
    url('countries/', views.countries, name='country'),
    url('booking/', views.register, name='register'),
    url('contact/', views.contact, name='contact')
]