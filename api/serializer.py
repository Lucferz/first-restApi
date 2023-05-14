from rest_framework import serializers
from . import models

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pelicula
        fields = ['id', 'titulo', 'estreno', 'sinopsis']