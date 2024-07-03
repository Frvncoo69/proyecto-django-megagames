from django.urls import path
from . import views
from .views import juegos

urlpatterns = [ 
    path('principal' , views.principal, name="principal"),

    path('soporte' , views.soporte, name="soporte"),

    path('acercade' , views.acercade, name="acercade"),

    path('carrito' , views.carrito, name="carrito"),

    path('crearusuario' , views.crearusuario, name="crearusuario"),

    path('juegounico' , views.juegounico, name="juegounico"),

    path('juegos' , views.juegos, name="juegos"),
    path('logout/' , views.exit, name="exit"),
    path('register/' , views.register, name="register"),

    # path('login' , views.login, name="login"),

    ##############

    path('lista_juegos', views.lista_juegos, name='lista_juegos'),
    path('juego_crear', views.juego_crear, name='juego_crear'),
    path('editar/<str:nombre>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<str:nombre>/', views.eliminar_juego, name='eliminar_juego'),
    # path('usuario_crear/', views.usuario_crear, name='usuario_crear'),
    
    path('juegos', juegos,name='juegos'),
    
    ]
