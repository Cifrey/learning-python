# Indexing = accessing elements of a sequence using [] (indexing operator)
# [start : stop : step] 
# Step es cada cuántos números hace la incrementación, por default es 1

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # La primera posición siempre es 0
print(credit_number[0:4]) # //El primer número incluye la primera posición, pero el último no, es hasta la penúltima posición. Se da por sentado el comienzo si se omite//
print(credit_number[:4]) # Si no se especifica el primer número, intuye que es desde el principio
print(credit_number[5:9]) 
print(credit_number[5:]) # Si no se pone número al final, intuye que es hasta el final
print(credit_number[-2]) # Empieza desde el final
print(credit_number[::2]) # Cada n de posiciones (empezando desde el primero)
last_digits = credit_number[-4:] # Empieza desde la posición -4 hasta el final
print(f"XXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] # Dice toda la línea al revés
print(credit_number)