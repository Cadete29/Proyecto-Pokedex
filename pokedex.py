import os
import requests
import json

def buscar_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def mostrar_info_pokemon(pokemon_data):
    print("Nombre:", pokemon_data['name'].capitalize())
    print("Peso:", pokemon_data['weight'])
    print("Tamaño:", pokemon_data['height'])
    print("Tipos:")
    for tipo in pokemon_data['types']:
        print("-", tipo['type']['name'].capitalize())
    print("Habilidades:")
    for habilidad in pokemon_data['abilities']:
        print("-", habilidad['ability']['name'].capitalize())
    print("Movimientos:")
    for movimiento in pokemon_data['moves'][:5]:  # Mostrar solo los primeros 5 movimientos
        print("-", movimiento['move']['name'].capitalize())

def guardar_info_pokemon(pokemon_data):
    nombre_pokemon = pokemon_data['name']
    imagen_url = pokemon_data['sprites']['front_default']
    info = {
        'nombre': nombre_pokemon,
        'peso': pokemon_data['weight'],
        'tamaño': pokemon_data['height'],
        'tipos': [tipo['type']['name'].capitalize() for tipo in pokemon_data['types']],
        'habilidades': [habilidad['ability']['name'].capitalize() for habilidad in pokemon_data['abilities']],
        'movimientos': [movimiento['move']['name'].capitalize() for movimiento in pokemon_data['moves'][:5]],
        'imagen': imagen_url
    }
    with open(f"pokedex/{nombre_pokemon}.json", 'w') as file:
        json.dump(info, file, indent=4)

def main():
    nombre_pokemon = input("Ingrese el nombre de un Pokémon: ")
    pokemon_data = buscar_pokemon(nombre_pokemon)
    if pokemon_data:
        mostrar_info_pokemon(pokemon_data)
        guardar_info_pokemon(pokemon_data)
    else:
        print("No se encontró el Pokémon.")

if __name__ == "__main__":
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    main()
