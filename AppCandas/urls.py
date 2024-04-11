from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("alta_curso/<nombre>/<comision>", views.alta_curso),
    path("alta_alumno/<nombre>/<DNI>", views.alta_alumno),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
]
