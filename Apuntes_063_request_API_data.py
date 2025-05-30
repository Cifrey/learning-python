# How to connect to an API using Python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name): # *
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) # response is an object
    # print(response) # This returns 200, which is a succesful response

    if response.status_code == 200:
        print("Data retrieved!")
        pokemon_data = response.json() # Response is a .json format, we need to convert it to a dictionary
        # print(pokemon_data) # It prints a very long dictionary
        return pokemon_data # This prints 'Data retrieved!'
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = input("Which Pokémon do you want to know about? ").lower()
# get_pokemon_info(pokemon_name) # * Parameters ('name') can be different than arguments ('pokemon_name')
# La frase de arriba mejor la guardamos en una variable:
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Weight: {pokemon_info["weight"] / 10}kg")
    print(f"Height: {pokemon_info["height"] / 10}m")

exit = input("Press any key to exit...")

# HTTP response status codes: 
# Informational responses -> 100 ~ 199
# Succesful responses -> 200 ~ 299
# Redirection messages -> 300 ~ 399
# Client error responses -> 400 ~ 499
# Server error responses -> 500 ~ 599