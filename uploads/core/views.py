from django.shortcuts import render
# from .models import Post
# from .models import Quiz #Question


def index(request):
    return render(request, 'index.html')


def countries(request):
   return render (request, 'country.html' )


def register(request):  #booking
    if request.method == 'POST':
        form = request.POST
        name = form["name"]
        surname = form["surname"]
        fullname = name + " " + surname
        email = form["email"]
        country = form["country"]
        unforbiden = ["africa", "france", ""]
        if country.lower() not in unforbiden:
            text = fullname + ", мы сейчас вас нафиг пошлем, пушо в" + country + " не ездим, но потом отпишем на мыло: " + email
        else:
            text = fullname + ", го бабки платите и езжайте в свою " + country
        if country in ["africa", "африка"]:
            text += "\nТы шо дурак? там жарко"
        return render(request, 'register.html', { 'display': True, 'text': text })
        
    return render(request, 'register.html', { 'display': False })

def contact(request):
    return render(request, 'contact.html')