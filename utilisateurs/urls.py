"""Definir des motifs d'URL pour utiliisateurs."""
from django.urls import path,include
from . import views

app_name = 'utilisateurs'
urlpatterns = [
    # inclure les URL d'authentification par defaut
    path('', include('django.contrib.auth.urls')),
    # page d'inscription
    path('register/', views.register, name='register'),

]