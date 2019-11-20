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


    name = models.CharField(max_length=30) #поля модели; atrybut clasy; komórka bazy danych
    country_choises = models.CharField(max_length=1, choices=COUNTRY_CHOISES) 
    gender_choises = models.CharField(max_length=1, choices=GENDER_CHOISES) 



