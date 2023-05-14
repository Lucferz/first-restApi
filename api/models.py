from django.db import models

# Create your models here.

class Pelicula(models.Model):

    titulo = models.CharField(max_length=100)
    estreno = models.DateField()
    sinopsis = models.TextField()

    def __str__(self) -> str:
        return self.titulo

