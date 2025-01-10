from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Animal, Noticia
from .forms import animales_form, noticias_form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
def principal(request):
    return render(request,'appmustafa/principal.html')
def animales(request):
    return render(request,'appmustafa/animales.html')
def crearNoticias(request):
    return render(request,'appmustafa/crearNoticias.html')
def crearAnimales(request):
    return render(request,'appmustafa/crearAnimales.html')

class CrearAnimales(CreateView):
    model=Animal
    form_class = animales_form
    template_name = 'appmustafa/crearAnimales.html'
    success_url = reverse_lazy('animales')
    
class CrearNoticias(CreateView):
    model=Noticia
    form_class = noticias_form
    template_name = 'appmustafa/crearNoticias.html'
    success_url = reverse_lazy('noticias')