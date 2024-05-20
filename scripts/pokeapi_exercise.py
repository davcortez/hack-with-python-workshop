import requests

# Ejercicio 1: Instalación y configuración inicial
def get_pokemon_data(name):
    """Get pokemon data
    
    Params
    --------
    name

    """
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Ejercicio 2: Obtener datos específicos
def show_pokemon_basic_info(name):
    """Show the basic info
    
    Params
    --------
    name

    """
    data = get_pokemon_data(name)
    if data:
        name = data['name']
        weight = data['weight']
        height = data['height']
        print(f"Nombre: {name}, Peso: {weight}, Altura: {height}")

# Ejercicio 3: Listar habilidades de un Pokémon
def show_pokemon_abilities(name):
    data = get_pokemon_data(name)
    if data:
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print(f"Habilidades de {data['name']}: {', '.join(abilities)}")

# Ejercicio 4: Consultar múltiples Pokémon
def show_multiple_pokemon_info(names):
    for name in names:
        data = get_pokemon_data(name)
        if data:
            types = [type_info['type']['name'] for type_info in data['types']]
            print(f"Nombre: {data['name']}, Tipos: {', '.join(types)}")

# Ejercicio 5: Manejo de errores
def show_multiple_pokemon_info_with_error_handling(names):
    for name in names:
        data = get_pokemon_data(name)
        if data:
            types = [type_info['type']['name'] for type_info in data['types']]
            print(f"Nombre: {data['name']}, Tipos: {', '.join(types)}")
        else:
            print(f"Error: El Pokémon '{name}' no fue encontrado")

# Ejercicio 6: Guardar resultados en un archivo
def save_multiple_pokemon_info_to_file(names, filename):
    """Save pokemon informaiton in file
    
    Params
    ----------
    names
    filename

    """
    with open(filename, 'w') as file:
        for name in names:
            data = get_pokemon_data(name)
            if data:
                types = [type_info['type']['name'] for type_info in data['types']]
                file.write(f"Nombre: {data['name']}, Tipos: {', '.join(types)}\n")
            else:
                file.write(f"Error: El Pokémon '{name}' no fue encontrado\n")

# Funciones de demostración para cada ejercicio
def main():
    print("Ejercicio 2: Obtener datos específicos")
    show_pokemon_basic_info('pikachu')
    print("\nEjercicio 3: Listar habilidades de un Pokémon")
    show_pokemon_abilities('pikachu')
    print("\nEjercicio 4: Consultar múltiples Pokémon")
    pokemon_names = ['pikachu', 'charmander', 'bulbasaur']
    show_multiple_pokemon_info(pokemon_names)
    print("\nEjercicio 5: Manejo de errores")
    pokemon_names_with_error = ['pikachu', 'charmander', 'bulbasaur', 'incorrect_name']
    show_multiple_pokemon_info_with_error_handling(pokemon_names_with_error)
    print("\nEjercicio 6: Guardar resultados en un archivo")
    save_multiple_pokemon_info_to_file(pokemon_names, 'pokemon_info.txt')

if __name__ == "__main__":
    main()
