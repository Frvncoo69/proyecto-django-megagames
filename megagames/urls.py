from django.urls import path
from . import views
urlpatterns = [ 
    path('principal' , views.principal, name="principal"),
    path('soporte' , views.soporte, name="soporte"),
    path('acercade' , views.acercade, name="acercade"),
    path('carrito' , views.carrito, name="carrito"),
    path('crearusuario' , views.crearusuario, name="crearusuario"),
    path('juegounico' , views.juegounico, name="juegounico"),
    path('juegos' , views.juegos, name="juegos"),
    path('login' , views.login, name="login"),
    path('tienda' , views.tienda, name="tienda"),

    ]
