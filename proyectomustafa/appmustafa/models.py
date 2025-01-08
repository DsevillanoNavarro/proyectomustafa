from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    situacion= models.TextField(max_length=750)
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    fecha_publicacion=models.DateField()
    imagen=models.ImageField(upload_to='images/') 
    contenido=models.TextField(max_length=1000)
