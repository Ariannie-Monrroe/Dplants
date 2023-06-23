from django.shortcuts import render, redirect
from .models import *
# Create your views here.



def cargarIndiex(request):
    return render(request,"indiex.html")


def cargarSesion(request): 
    return render(request,"logIn.html") 

def cargarRegistro(request): 
    return render(request,"singUp.html")

def cargarCarrito(request):
    return render(request, "Carrito.html")