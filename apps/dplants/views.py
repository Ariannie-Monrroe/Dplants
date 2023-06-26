from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from apps.dplants import *
# Create your views here.

def cargarIndiex(request):
    return render(request,"indiex.html")


def cargarSesion(request): 
    return render(request,"logIn.html") 

def cargarRegistro(request): 
    return render(request,"singUp.html")

def cargarCarrito(request):
    products = Product.objects.all()
    return render(request, "Carrito.html", {
        "products": products
    })


    
