from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
# importaciones necesarias para hacer http sin el framework
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

@csrf_exempt #Anotacion para poder hacer peticiones post de manera segura en django
def peliculas(request):
    if request.method == 'GET':
        peliculas = models.Pelicula.objects.all()
        print(peliculas)
        respuesta =[]
        for pelicula in peliculas:
            dict = {}
            dict['titulo'] = pelicula.titulo
            dict['sinopsis'] = pelicula.sinopsis
            dict['estreno'] = pelicula.estreno
            respuesta.append(dict)

        #return HttpResponse(status=200)
        return JsonResponse(respuesta, safe=False)
    if request.method == 'POST':
        if request.content_type != 'application/json':
            return HttpResponse(status=400) #bad request
        
        try:
            jsonData = json.loads(request.body.decode())
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        
        pelicula = models.Pelicula(
            titulo = jsonData.get('titulo', ''),
            estreno = jsonData.get('estreno', ''),
            sinopsis = jsonData.get('sinopsis','')
        )
        respuesta ={
            'id' : pelicula.pk,
            'titulo' : pelicula.titulo,
            'estreno' : pelicula.estreno
        }

        pelicula.save()
        return JsonResponse(respuesta, status=201) #created


def pelicula(request, id):
    try:
        pelicula = models.Pelicula.objects.get(pk=id)
    except Exception:
        return HttpResponse(status=404)
    respuesta = {
        "titulo" : pelicula.titulo,
        "sinopsis" : pelicula.sinopsis
    }

    return JsonResponse(respuesta, safe=False)