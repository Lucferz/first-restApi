from django.urls import path, include
from . import views
urlpatterns = [
    #path('peliculas', views.peliculas),
    path('peliculas/', views.PeliculaApiView.as_view()),# with ApiView class
    path('peliculas/<int:id>', views.pelicula),
]
