from django.shortcuts import render
# from .models import Post
# from .models import Quiz #Question

from django.core.files.storage import FileSystemStorage

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
        data_text = fullname + ";" + email + ";" + country + ";\n"
        f = open("booking.csv", 'a+')
        f.write(data_text)
        f.close()
        unforbiden = ["africa", "afryka", "egipt", "egypt"]
        if country.lower() not in unforbiden:
            text = fullname + ", dziękujemy za zainteresowanie się naszymi ofertami. Niestety nie mamy aktyalnie żadnych turów do " + country + ". Kiedy pojawi się oferta, wyślemy ją pod adresem: " + email
        else:
            text = fullname + ", dziękujemy za zainteresowanie się naszymi ofertami. Już wysłaliśmy maila dotyczącego aktualnych turów do " + country + " pod adresem: " + email
        if country in ["africa", "afryka", "африка"]:
            text += "\n Ciekawostka: czy wiesz, że w " + country + " jest gorąco?"
        elif country in ["egipt", "egypt"]:
            text += "\n Ciekawostka: czy wiesz, że w " + country + " są girafy?"
        else:
            text += "\n Nie dowiesz się o żadnych ciekawostkach z " + country
        return render(request, 'register.html', { 'display': True, 'text': text })
        
    return render(request, 'register.html', { 'display': False })

def contact(request):
    return render(request, 'contact.html')