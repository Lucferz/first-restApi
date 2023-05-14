from django.urls import path, include
from . import views
urlpatterns = [
    #path('peliculas', views.peliculas), #Django Native or w/o ApiView Class
    #path('peliculas/<int:id>', views.pelicula),#Django Native or w/o ApiView Class
    path('peliculas/', views.PeliculasApiView.as_view()),# with ApiView class
    path('peliculas/<int:id>', views.PeliculaApiView.as_view()),#Django Native or w/o ApiView Class
]
