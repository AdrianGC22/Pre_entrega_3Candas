from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("alta_curso/", views.formulario_alta_curso, name="alta_curso"),
    path("alta_alumno/<nombre>/<DNI>", views.alta_alumno),
    path("alta_profesor/<nombre>/<DNI>/<titulo>", views.alta_profesor),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores")
]
