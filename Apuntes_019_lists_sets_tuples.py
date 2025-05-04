# Collection = single "variable" used to store multiple values
# List = [] ordered as you write it and changeable. Duplicates OK
# Set = {} unordered and immutable (you can't change the values), but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# // LISTS // #

vns = ["umineko", "saya no uta", "sayooshi", "rance"] # Estos valores también se llaman elementos

print(vns[::-1])

for vn in vns:
   print(vn)

print(dir(vns))
print(help(vns)) 
print(len(vns)) # Cuántos elementos hay
print("umineko" in vns) # Para comprobar que está dentro de la lista
vns[0] = "subahibi" # Reemplaza el de esa posición con el nuevo valor
vns.append("subahibi") # Esto añade uno al final de la lista
vns.remove("umineko") # Eliminar un elemento de la lista en concreto
vns.insert(0, "subahibi") # Añade un elemento en la posición que digamos
vns.sort() # Ordena por orden alfabético
vns.reverse() # Orden inverso del que pusimos en el código
# Podemos poner varios, ex: sort y luego reverse
vns.clear() # Para que no aparezca ninguno
print(vns.index("umineko")) # Para saber en qué posición está 
print(vns.count("umineko")) # Para saber cuántas veces sale ese elemento en la lista

print(vns)

##################################################

# // SETS // #

vns = {"umineko", "saya no uta", "sayooshi", "rance"}
print(dir(vns))
print(help(vns))
print(len(vns))
print("subahibi" in vns) # Sale falso porque no está
print(vns[0]) # Sale error porque un set no está en orden, no existe posición 0
vns.add("subahibi")
vns.remove("umineko")
vns.pop() # Borra el que esté primero, pero como es al azar, pues borra uno random
vns.clear() 

print(vns)

##################################################

# // TUPLES // #

vns = ("umineko", "saya no uta", "sayooshi", "rance")

print(dir(vns))
print(help(vns))
print(len(vns))
print("subahibi" in vns)
print(vns.index("umineko")) # En qué posición está
print(vns.count("rance"))

for vn in vns:
   print(vn)

print(vns)