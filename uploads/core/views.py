from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def index(request):
    print('Home')
    return render(request, 'index.html')


def country(request):
   return render (request, 'country.html' )


def contact(request):
    print('Contact')
    return render(request, 'contact.html')
