from __future__ import unicode_literals

from django.db import models

class Register_ankieta(models.Model):

    #lista wybory =список выбора
    #MIGRACJA CO RAZY po zmianie listy czy ...
    COUNTRY_CHOISES = [
        ('E', 'Egipt'),  #('1.znaczenie do bazy danych', '2.wyświetli się w formie')
        ('B', 'Brazylia'),
        ('S', 'Szwecja'),
        ('J', 'Japonia'),
    ]

    GENDER_CHOISES = [
        ('K', 'Kobieta'),
        ('M', 'Męzczyzna'),
    ]
    
    # <label for="name">Imię i nazwisko:</label>
    # <input id="name" type="text" required autofocus="true">
    # </div>
    # <div class="row">
    # <label for="email">Adres e-mail:</label>
    # <input id="email" type="email" required>
    # </div>

    first_name = models.CharField(max_length=30) #поля модели; atrybut clasy; komórka bazy danych
    last_name = models.CharField(max_length=30)
    country_choises = models.CharField(max_length=1, choices=COUNTRY_CHOISES) 
    gender_choises = models.CharField(max_length=1, choices=GENDER_CHOISES) 

    def b_status(self):
        #returns status
        #import datetime
        if cośtam:
            return "komunikat1"
        elif cośtam:
            return "komunikat2"
        else cośtam:
            return "komunikat3"

    def full_name(self):
        #returns the person's full name
        return '%s %s' % (self.first_name, self.last_name)


