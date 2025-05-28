# Python reading files (.txt, .json, .csv)

import json
import csv

file_path = "C:/Users/akira/OneDrive/Escritorio/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError: # Si no ponemos la extensión '.txt', sale este error
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

#####################################

file_path = "C:/Users/akira/OneDrive/Escritorio/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content) # Podemos añadir print(content["age"]), donde 'age' puede ser 'name', 'job'...
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

#####################################

file_path = "C:/Users/akira/OneDrive/Escritorio/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0]) # Podemos poner print(line[0]) o el número que queramos según la columna
except FileNotFoundError: 
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")