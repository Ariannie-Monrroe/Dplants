from django.urls import path
from . import views

from .views import *



urlpatterns = [
    
    path('',views.cargarIndiex),
    
    path('addCart/<int:product_id>/', views.addCart, name= "add_to"),
    path('removeCart/<int:product_id>/', views.removeCart, name= "rem_to"),
    path('clearCart/', views.clearCart, name= "clr_to"),
    path('decrementCart/<int:product_id>/', views.decrementCart, name= "dct_to"),
    
    
    path('logIn.html',views.cargarSesion),
    path('singUp.html',views.cargarRegistro),
    

]