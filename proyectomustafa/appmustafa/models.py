from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Animal(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    situacion= models.TextField(max_length=750)
    imagen=models.ImageField(upload_to='images/animales')
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
    def __str__(self):
        return self.nombre
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='images/animales') 
    contenido=models.TextField(max_length=1000)
    fecha_publicacion=models.DateField()
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
    def __str__(self):
        return self.titulo
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="noticias")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuarios")
    contenido=models.TextField(max_length=1000)
    def __str__(self):
        return self
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'