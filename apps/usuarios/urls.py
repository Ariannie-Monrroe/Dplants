from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from . import views

from django.urls import path

urlpatterns = [
    path('inicioDsesion', views.login_user, name='log_in'),

]