from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Animal, Noticia
from .forms import animales_form, noticias_form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def principal(request):
    return render(request, 'appmustafa/principal.html')
def animales(request):
    return render(request, 'appmustafa/animales.html')
def noticias(request):
    return render(request, 'appmustafa/noticias.html')

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
    

    