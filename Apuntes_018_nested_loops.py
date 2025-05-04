# nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

while x > 0:
    while y > 0:
        print("do something")

#############################################

while x > 0:
    for y in range(9):
        print("do something")

# ###########################################

for x in range(3):
    for y in range(9):
        print("do something")

# ###########################################

for x in range(3):
    while y > 0:
        print("do something")

#############################################

for x in range(1, 10):
    print(x, end=" ") 
    
# end="" hace que se imprima todo en la misma línea en vez de número por línea
# Lo que pongamos entre "" aparece entre cada número (ex: si end="a" -> 1a2a3a...)

########################################### 

for x in range(3):
    for y in range(1, 10):
        print(y, end="")

# Esto hace que se repita del 1 al 9, 3 veces

########################################### 

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print() # Esto hace que se imprima una nueva línea, creando un espacio entre cada outer loop

########################################### 

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

# Esto dibuja un cuadradito :D (o rectangulito)