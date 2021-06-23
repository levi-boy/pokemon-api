import requests

from django.shortcuts import render


def pokemon_list(request):
    data = requests.get('https://pokeapi.co/api/v2/pokemon').json()
    pokemons = []
    for pokemon in data['results']:
        pokemon_url = pokemon['url']
        pokemon_data = requests.get(pokemon_url).json()
        pokemon_name = pokemon_data['name']
        pokemon_image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
        pokemons.append({'pokemon_name': pokemon_name, 'pokemon_image_url': pokemon_image_url})
    return render(request, 'pokemons/pokemon_list.html', {'pokemons': pokemons})
