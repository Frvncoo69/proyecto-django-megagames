from django.shortcuts import render
from .models import juego

def principal (request):
    context ={}
    return render (request, 'megagames/principal.html',context)

def soporte (request):
    context ={}
    return render (request, 'megagames/soporte.html',context)

def acercade (request):
    context ={}
    return render (request, 'megagames/acerca-de.html',context)

def carrito (request):
    context ={}
    return render (request, 'megagames/carrito.html',context)

def crearusuario (request):
    context ={}
    return render (request, 'megagames/crear-usuario.html',context)

def juegounico (request):
    context ={}
    return render (request, 'megagames/juego-unico.html',context)

def juegos(request):
    juegos = juego.objects.all()
    context = {'juegos': juegos}
    return render(request, 'megagames/juegos.html', context)

def login (request):
    context ={}
    return render (request, 'megagames/login.html',context)

def tienda (request):
    context ={}
    return render (request, 'megagames/tienda.html',context)