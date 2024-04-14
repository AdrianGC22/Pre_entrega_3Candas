from django.shortcuts import render
from AppCandas.models import Curso, Alumno, Profesor
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def formulario_alta_curso(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
        curso.save()
        return render(request, "formulario_alta_curso.html")
    return render(request, "formulario_alta_curso.html")

def alta_alumno(request, nombre, DNI):
    alumno = Alumno(nombre=nombre, DNI=DNI)
    alumno.save()
    texto = f"Se actualizo la base de datos con el alumno: {alumno.nombre} {alumno.DNI}"
    return HttpResponse(texto)

def alta_profesor(request, nombre, DNI, titulo):
    profesor = Profesor(nombre=nombre, DNI=DNI, titulo=titulo)
    profesor.save()
    texto = f"Se actualizo la base de datos con el profesor: {profesor.nombre} {profesor.DNI}"
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

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

