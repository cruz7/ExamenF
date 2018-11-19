from django.db import models
from django.contrib import admin

# Create your models here.

class Curso(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")


    class Meta:
                verbose_name="Curso"
                verbose_name_plural="Cursos"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre



class Grado(models.Model):

    nombre = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    curso = models.ManyToManyField(Curso,verbose_name="curso")

    class Meta:
                verbose_name="Grado"
                verbose_name_plural="Grados"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre

class Seccion(models.Model):

    nombre = models.CharField(max_length=100)

    class Meta:
                verbose_name="Seccion"
                verbose_name_plural="Secciones"
                ordering = ["-vue"]

    def __str__(self):
        return self.nombre
