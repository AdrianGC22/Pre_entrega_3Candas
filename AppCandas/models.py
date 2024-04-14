from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    DNI = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    DNI = models.IntegerField()
    titulo = models.CharField(max_length=50)