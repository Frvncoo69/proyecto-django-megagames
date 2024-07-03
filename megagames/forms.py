from django import forms
from .models import juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = juego
        fields = ['nombre', 'precio', 'imagen', 'descripcion', 'stock']
