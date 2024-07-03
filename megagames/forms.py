from django import forms
from .models import juego
from django.contrib.auth.forms import UserCreationForm

class JuegoForm(forms.ModelForm):
    class Meta:
        model = juego
        fields = ['nombre', 'precio', 'imagen', 'descripcion', 'stock']

class CustomUserCreationForm(UserCreationForm):
    pass
    # email = forms.EmailField(required=True)

    # class Meta:
    #     model = usuario
    #     fields = ("username", "email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user