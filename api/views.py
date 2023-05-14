from django.shortcuts import render
from . import models

# importaciones necesarias para hacer http sin el framework
from django.http import HttpResponse
# Create your views here.


def peliculas(request):
    if request.method == 'GET':
        peliculas = models.Pelicula.objects.all()
        print(peliculas)
        respuesta =[]
        for pelicula in peliculas:
            dict = {}
            dict['titulo'] = pelicula.titulo
            dict['sinopsis'] = pelicula.sinopsis
        return HttpResponse(status=200)