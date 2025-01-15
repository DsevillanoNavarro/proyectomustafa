from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Animal, Noticia
from .forms import animales_form, noticias_form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def principal(request):
    return render(request, 'appmustafa/principal.html')

class Animales(ListView):
    model=Animal
    template_name='appmustafa/animales.html'
    context_object_name = 'animales'
    
class CrearAnimales(LoginRequiredMixin, CreateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/crearAnimales.html'
    success_url = reverse_lazy('listarAnimales')
class EditarAnimales(UpdateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/editarAnimales.html'
    success_url = reverse_lazy('listarAnimales')

class BorrarAnimales(DeleteView):
    model=Animal
    template_name = 'appmustafa/borrarAnimales.html'
    success_url = reverse_lazy('listarAnimales')
    
class ListarAnimales(ListView):
    model=Animal
    template_name='appmustafa/listarAnimalesAdmin.html'
    context_object_name = 'animales'
    
class DetallesAnimales(DetailView):
    model = Animal
    template_name = 'appmustafa/detalleAnimal.html' 
    context_object_name = 'animal'
    
class CrearNoticias(CreateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/crearNoticias.html'
    success_url = reverse_lazy('noticias')

class UserMenuView(TemplateView):
    template_name = 'appmustafa/usuario.html'
    
class CrearNoticias(LoginRequiredMixin, CreateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/crearNoticias.html'
    success_url = reverse_lazy('listarNoticias')
    
class ListarNoticias(ListView):
    model=Noticia
    template_name='appmustafa/listarNoticiasAdmin.html'
    context_object_name = 'noticias'
    
class EditarNoticias(UpdateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/editarNoticias.html'
    success_url = reverse_lazy('listarNoticias')
class BorrarNoticias(DeleteView):
    model=Noticia
    template_name = 'appmustafa/borrarNoticias.html'
    success_url = reverse_lazy('listarNoticias')

class Noticias(ListView):
    model=Noticia
    template_name='appmustafa/noticias.html'
    context_object_name = 'noticias'
class DetallesNoticias(DetailView):
    model = Noticia
    template_name = 'appmustafa/detalleNoticia.html' 
    context_object_name = 'noticia'