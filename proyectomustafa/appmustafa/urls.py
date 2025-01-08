"""
URL configuration for proyectomustafa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.principal, name="principal"),
    path('animales/', views.animales, name="animales"),
    path('animales/<int:pk>', views.verAnimales, name="verAnimales"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:pk>', views.verNoticias, name="verNoticias"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login, name="login"),
    path('usuario/', views.usuario, name="usuario"),
    path('usuario/animalesQueridos', views.animalesQueridos, name="animalesQueridos"),
    path('usuario/admin/crearAnimal', views.crearAnimal, name="crearAnimal"),
    path('usuario/admin/editarAnimal', views.editarAnimal, name="editarAnimal"),
    path('usuario/admin/borrarAnimal', views.borrarAnimal, name="borrarAnimal"),
    path('usuario/admin/crearNoticia', views.crearNoticia, name="crearNoticia"),
    path('usuario/admin/editarNoticia', views.editarNoticia, name="editarNoticia"),
    path('usuario/admin/borrarNoticia', views.borrarNoticia, name="borrarNoticia"),
    path('usuario/admin/datosAnimales', views.datosAnimales, name="datosAnimales"),
    path('usuario/admin/datosNoticias', views.datosNoticias, name="datosNoticias"),
]
