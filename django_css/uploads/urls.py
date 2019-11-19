from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('', views.index, name='index'),
    url ('country/', views.country, name='country'),
    url('contact/', views.contact, name='contact'),
]
