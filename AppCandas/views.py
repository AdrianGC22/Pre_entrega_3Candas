from django.shortcuts import render
from AppCandas.models import Curso, Alumno
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def alta_curso(request, nombre, comision):
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    texto = f"Se actualizo la base de datos con el curso: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def alta_alumno(request, nombre, DNI):
    alumno = Alumno(nombre=nombre, DNI=DNI)
    alumno.save()
    texto = f"Se actualizo la base de datos con el alumno: {alumno.nombre} {alumno.DNI}"
    return HttpResponse(texto)


def inicio(request):
    return render(request, "padre.html")

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)