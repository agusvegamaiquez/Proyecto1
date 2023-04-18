from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso


# Create your views here.

def curso (self, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>Curso:{curso.nombre} - Camada:{curso.camada} </p>
    """) 

def lista_curso(self):

    lista = Curso.objects.all()

    return render(self, "lista_cursos.html", {"lista_curso": lista})

def inicio (self):
    return HttpResponse('inicio.html')

def cursos (self):
    return HttpResponse('cursos.html')

def profesores (self):
    return HttpResponse('profesores.html')

def estudiantes (self):
    return HttpResponse('estudiantes.html')

def entregables (self):
    return HttpResponse('entregables.html')

