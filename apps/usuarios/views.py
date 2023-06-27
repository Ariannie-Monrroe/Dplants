from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(request):
    
    if request.method == "POST":

        userName = request.POST['userName']
        passWord =request.POST['passWord']
        user = authenticate(request, username = 'userName', password = 'passWord')
        if user is not None:
            login(request, user)
            redirect('/')
            
        else:
            messages.success(request,'Error de inicio de sesion, reintentar')
            redirect('inicioDsesion')
    else:       
        return render(request,'inicioDsesion.html')
    

    