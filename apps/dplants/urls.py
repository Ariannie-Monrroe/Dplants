from django.urls import path
from . import views

from .views import Cart, addCart, removeCart, clearCart, decrementCart



urlpatterns = [ 

    path('',views.cargarIndiex),
    path('logIn',views.cargarSesion),
    path('singUp',views.cargarRegistro),
    path('productoCarrito',views.cargarProductoCarrito),
    path('cart',Cart),
    path('addCart/<product_id>/', addCart, name= "add_to"),
    path('removeCart/<product_id>/', removeCart, name= "rem_to"),
    path('clearCart/', clearCart, name= "clr_to"),
    path('decrementCart/<product_id>/', decrementCart, name= "dct_to"),
    
    

]