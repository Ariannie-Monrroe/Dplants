from django.shortcuts import render, redirect
from apps.dplants.cart import Cart
from .models import Product


# Create your views here.

def cargarIndiex(request):
    products = Product.objects.all()
    return render(request,'indiex.html', {'products': products})


def cargarSesion(request): 
    return render(request,"logIn.htmsl") 

def cargarRegistro(request): 
    return render(request,"singUp.html")

def cargarProductoCarrito(request): 
    return render(request,"productoCarrito.html")




def addCart(request, product_id):
    cart = Cart(request) 
    product = Product.objects.get(slug = product_id)   
    cart.add(product)
    return redirect("/")


def decrementCart(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(slug = product_id)
    cart.decrement(product)
    return redirect("/")

def removeCart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(slug = product_id)
    cart.remove(product)
    return redirect("/")

def clearCart(request):
    cart = Cart(request)
    
    cart.clear()
    return redirect("/")