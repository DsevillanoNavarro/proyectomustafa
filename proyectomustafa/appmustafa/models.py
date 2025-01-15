from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Animal(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    situacion= models.TextField(max_length=750)
    imagen=models.ImageField(upload_to='images/animales'  ) 
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='images/noticias') 
    contenido=models.TextField(max_length=1000)
    fecha_publicacion=models.DateField()
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="noticias")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuarios")
    contenido=models.TextField(max_length=1000)