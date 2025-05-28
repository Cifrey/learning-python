# Python writing files (.txt, .json, .csv)

txt_data = "I like Umineko"

file_path = "C:/Users/akira/OneDrive/Escritorio/output.txt"

with open(file_path, "w") as file:
    file.write(txt_data) # Se comporta como un objeto
    print(f"txt file '{file_path}' was created")

# 'with' es para que se cierre el archivo después de abrirlo. Dejar archivos abiertos puede dar problemas
# El primer argumento 'file_path' es dónde está el archivo y el segundo argumento '"w"' es qué queremos hacer con él
# Existen varias maneras de interactuar con el archivo:
# w = write
# x = también write si el archivo no existe. Si existe y ponemos 'x', dará error
# a = append
# r = read
# La frase completa sería open(file=file_path, mode="w"), pero si lo sabemos no hace falta escribirlo
# 'as' es para darle un nombre
# 'file' es el nombre que le queremos dar

# Ejemplo de "x"
try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# Si ponemos "a" para append, se añade ese texto otra vez en el mismo archivo: I like UminekoI like Umineko
# Podemos poner file.write("\n" + txt_data) para que salga:
# I like Umineko
# I like Umineko

#################################

# Seguimos en el ejemplo de .txt

employees = ["Beato", "Battler", "Rance", "Saya"]

try:
    with open(file_path, "w") as file:
        file.write(employees) # Esto da TypeError: argument must be str, not list
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# Deberíamos iterarlo, así:

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# Esto nos devuelve: BeatoBattlerRanceSaya, podemos poner \n otra vez o " "

#################################

# Ejemplo para archivo .json

import json

employee = {
    "name": "Battler",
    "age": "18",
    "job": "detective"
}

file_path = "C:/Users/akira/OneDrive/Escritorio/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file) # dump method convierte el diccionario en un json string
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# El json se ve así: {"name": "Battler", "age": "18", "job": "detective"}

# Podemos ponerlo más bonito si añadimos otro argumento después de 'json.dump(employee, file, _)
# Donde está el '_', ponemos 'indent=4', donde 4 es el número de espacios que queramos indentar

#################################

# Ejemplo para .csv (significa comma separated values), comunes para spreadsheet data, como un excel

import csv

employees = [["Name", "Age", "Job"], 
             ["Battler", 18, "Detective"], 
             ["Beato", 19, "Witch"], 
             ["Rance", 18, "Bad Hero"]]

file_path = "C:/Users/akira/OneDrive/Escritorio/output.csv"

try:
    with open(file_path, "w", newline="") as file: # newline="" para que no cree una nueva línea vacía después de cada row
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row) # Sin este for loop, no se escribe nada en el archivo porque tenemos que iterarlo
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")