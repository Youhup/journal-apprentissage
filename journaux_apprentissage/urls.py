"""Defenir des motifs f'URL pour journaux_apprentissage"""
from django.urls import path
from . import views
app_name = 'journaux_apprentissage'
urlpatterns = [
    #Page d'accueil
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page d'ajout d' un nouveau sujet
    path('new_topic/', views.new_topic, name='new_topic'),
    #page d'ajout d'une nouvelle entree
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]