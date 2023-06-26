from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.dplants.cart import Cart
from .models import *
from apps.dplants import *
from .views import *
# Create your views here.

def cargarIndiex(request):
    products = Product.objects.all()
    return render(request,"indiex.html", {
        "products": products
    })


def cargarSesion(request): 
    return render(request,"logIn.html") 

def cargarRegistro(request): 
    return render(request,"singUp.html")

def cargarCarrito(request):
    products = Product.objects.all()
    return render(request, "indiex.html", {
        "products": products
    })


def addCart(request, product_id):
    cart = Cart(request) 
    product = Product.objects.get(id = product_id)   
    cart.add(product)
    return redirect("/cargarIndiex")


def decrementCart(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.decrement(product)
    return redirect("/cargarIndiex")

def removeCart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.remove(product)
    return redirect("/cargarIndiex")

def clearCart(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.clear(product)
    return redirect("/cargarIndiex")