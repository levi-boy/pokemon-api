from django.urls import path

from . import views

app_name = 'pokemons_app'

urlpatterns = [
    path('pokemons/', views.pokemon_list, name='pokemon_list')
]
