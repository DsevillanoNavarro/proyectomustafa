from datetime import date
from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from appmustafa.models import Animal, Noticia
class animales_form(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            }

class noticias_form(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'fecha_publicacion': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            }

    