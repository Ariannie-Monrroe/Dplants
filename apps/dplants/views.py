from django.shortcuts import render, redirect
from apps.dplants.cart import Cart
from .models import Product, Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time 

# Create your views here.

def cargarIndiex(request):
    products = Product.objects.all()
    return render(request,'indiex.html', {'products': products})
def cargarSesion(request): 
    return render(request,"logIn.html") 
def cargarRegistro(request): 
    return render(request,"singUp.html")
@login_required
def cargarProductoCarrito(request): 
    products = Product.objects.all()
    return render(request,"productoCarrito.html", {'products': products})

# def cargarPlantas(request):
    


def addCart(request, product_id):
    cart = Cart(request) 
    product = Product.objects.get(slug = product_id)   
    cart.add(product)
    return redirect("/productoCarrito")


def decrementCart(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(slug = product_id)
    cart.decrement(product)
    return redirect("/productoCarrito")

def removeCart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(slug = product_id)
    cart.remove(product)
    return redirect("/productoCarrito")

def clearCart(request):
    cart = Cart(request)
    
    cart.clear()
    return redirect("/productoCarrito")


def crearUsuario(request):
    
    v_id = request.POST['username']
    v_usuario = request.POST['username']
    v_correo = request.POST['email']
    v_pass =request.POST['password']
    
    Usuario.objects.create(
        
        id = v_id,
        usuario = v_usuario,
        contraseña = v_pass,
        correo=v_correo
        
        )
    time.sleep(2)
    messages.success(request,'Registrado perfectamente')
    return redirect('/')
        