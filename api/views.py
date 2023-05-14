from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
# importaciones necesarias para hacer api rest sin el framework djangorestframework
from django.http import HttpResponse, JsonResponse
import json
# importaciones necesarias para utilizar el framework djangorestframework
from . import serializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status # Posibly enum class with most of the http response with description so it is easier to find
# Create your views here.

#
#   Starting the use of api_views decorator to simplify the code 
#
#   A decorator is a line of code that provides a function with certain methods, similar to extend a class
#   but in a simplier way
#
#   Here we implement the Response class, this is usefull specially for test and debug, because it provides different type
#   of output depending on the header accept content type that is used, and it also it abstract the logic of sending an 
#   http response or a JsonResponse
#

@api_view(['GET', 'POST']) # in this case we need to specify the http method/s that we're going to use
def peliculas(request): #hecho con django REST Framework
    if request.method == 'GET':
        peliculas = models.Pelicula.objects.all()
        
        #ordenar por query params
        ordenar_por = request.GET.get('ordenarPor', '')
        if ordenar_por:
            peliculas = peliculas.order_by(ordenar_por)

        respuesta = serializer.PeliculaSerializer(peliculas, many=True)

        return Response(respuesta.data)
    if request.method == 'POST':
        serialized_data = serializer.PeliculaSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE']) 
def pelicula(request, id):
    try:
        pelicula = models.Pelicula.objects.get(pk=id)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        respuesta = serializer.PeliculaSerializer(pelicula)
        return Response(respuesta)
    
    if request.method == 'PUT':
        serialized_data = serializer.PeliculaSerializer(pelicula, data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data) 

    if request.method == 'DELETE':
        pelicula.delete()      
        return Response(status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


#
#   Starting to use rest framework
#

@csrf_exempt #Anotacion para poder hacer peticiones post de manera segura en django
def peliculas_rest_framework(request): #hecho con django REST Framework
    if request.method == 'GET':
        peliculas = models.Pelicula.objects.all()
        
        #ordenar por query params
        ordenar_por = request.GET.get('ordenarPor', '')
        if ordenar_por:
            peliculas = peliculas.order_by(ordenar_por)

        respuesta = serializer.PeliculaSerializer(peliculas, many=True)

        return JsonResponse(respuesta.data, safe=False)
    if request.method == 'POST':
        if request.content_type != 'application/json':
            return HttpResponse(status=400) #bad request
        data = JSONParser().parse(request)
        serialized_data = serializer.PeliculaSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=201)

        return JsonResponse(serialized_data.errors, status=400)
    

@csrf_exempt 
def pelicula_rest_framework(request, id):
    try:
        pelicula = models.Pelicula.objects.get(pk=id)
    except Exception:
        return HttpResponse(status=404)
    if request.method == 'GET':
        respuesta = serializer.PeliculaSerializer(pelicula)
        return JsonResponse(respuesta, safe=False)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serialized_data = serializer.PeliculaSerializer(pelicula, data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data) 

    if request.method == 'DELETE':
        pelicula.delete()      
        return HttpResponse(status=200)

    return JsonResponse(serialized_data.errors, status=400)      


#
#   Django Native Rest Service
#


@csrf_exempt #Anotacion para poder hacer peticiones post de manera segura en django
def peliculas_django_native(request):
    if request.method == 'GET':
        peliculas = models.Pelicula.objects.all()
        
        #ordenar por query params
        ordenar_por = request.GET.get('ordenarPor', '')
        if ordenar_por:
            peliculas = peliculas.order_by(ordenar_por)

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


def pelicula_django_native(request, id):
    try:
        pelicula = models.Pelicula.objects.get(pk=id)
    except Exception:
        return HttpResponse(status=404)
    respuesta = {
        "titulo" : pelicula.titulo,
        "sinopsis" : pelicula.sinopsis
    }

    return JsonResponse(respuesta, safe=False)