from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'index.html')


def country(request):
   return render (request, 'country.html' )


def register(request):  #booking
   return render (request, 'register.html' )


def contact(request):
    return render(request, 'contact.html')


def quiz(request):
    return render(request, 'quiz.html')
