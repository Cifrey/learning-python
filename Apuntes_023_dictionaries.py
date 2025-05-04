# dictionary = a collection of {key:value} pairs
# ordered and changeable, no duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(dir(capitals))
print(help(capitals))
print(capitals.get("Russia")) # Nos devuelve el valor de la key escrita

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# Para saber si está esa key en el diccionario

capitals.update({"Germany": "Berlin"}) # Podemos añadir una key nueva
capitals.update({"USA": "Detroit"}) # Podemos modificar una key existente
capitals.pop("China") # Borrar key específica
capitals.popitem() # Esto borra la última key
capitals.clear() # Borra todo el diccionario

keys = capitals.keys() # Imprime sólo las keys, sin su valor
for key in capitals.keys():
    print(key)

values = capitals.values() # Imprime sólo los valores
print(values)

for value in capitals.values(): # Hace lo mismo pero en una lista limpia
    print(value)

items = capitals.items() # Imprime todos los key:value que parece una lista en una línea
print(items)

for key, value in capitals.items(): # Imprime key:value en par por línea
    print(f"{key}: {value}")