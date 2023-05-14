from django.urls import path, include
from . import views
urlpatterns = [
    path('peliculas', views.peliculas),
    path('peliculas/<int:id>', views.pelicula),
]
