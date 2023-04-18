from django.urls import path 
from AppCod import views
from django.contrib import admin
from django.urls import path
from AppCod.views import curso , lista_curso, inicio,cursos,profesores,estudiantes,entregables


urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_curso),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),   

]

