from django.shortcuts import render, get_object_or_404, redirect
from .models import juego
from .forms import JuegoForm

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
    juegos = juego.objects.all()  # Obtén todos los juegos desde la base de datos
    context = {'juegos': juegos}  # Crea un contexto con los juegos
    return render(request, 'megagames/juegos.html', context)  # Renderiza la plantilla con el contexto}

def login (request):
    context ={}
    return render (request, 'megagames/login.html',context)

def tienda (request):
    context ={}
    return render (request, 'megagames/tienda.html',context)

###########

def lista_juegos(request):
    juegos = juego.objects.all()
    return render(request, 'megagames/lista_juegos.html', {'juegos': juegos})

def juego_crear(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')
    else:
        form = JuegoForm()
    return render(request, 'megagames/juego_crear.html', {'form': form})

def editar_juego(request, nombre):
    juego_obj = get_object_or_404(juego, nombre=nombre)
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES, instance=juego_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')
    else:
        form = JuegoForm(instance=juego_obj)
    return render(request, 'megagames/editar_juego.html', {'form': form, 'titulo': f'Editar {juego_obj.nombre}'})

def eliminar_juego(request, nombre):
    juego_obj = get_object_or_404(juego, nombre=nombre)
    if request.method == 'POST':
        juego_obj.delete()
        return redirect('lista_juegos')
    return render(request, 'megagames/eliminar_juego.html', {'juego': juego_obj})