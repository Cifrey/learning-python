import time

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(2)

print("TIME'S UP!")

# El programa 'duerme' los segundos que pongamos en el código entre input e input
# Si el usuario pone 5 en 'my_time' y nosotros ponemos 'time.sleep(2)',
# El output mostrará un número cada 2 segundos hasta llegar al 5//

#############################################

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)

print("TIME'S UP!")

#############################################

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("TIME'S UP!")

# Otra manera de hacer la cuenta atrás, con step

#############################################

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")