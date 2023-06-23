from django.urls import path
from . import views



urlpatterns = [
    path('',views.cargarIndiex),
    path('logIn.html',views.cargarSesion),
    path('singUp.html',views.cargarRegistro),
    path('Carrito.html',views.cargarCarrito)

]