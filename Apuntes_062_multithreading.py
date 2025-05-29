# multithreading = used to perform multiple tasks concurrently (multitasking)
#                  good for I/O bound tasks like reading files or fetching data from APIs
#   	           threading.Thread(target=my_function)

import threading
import time

def walk_cat(name):
    time.sleep(8)
    print(f"You finish walking {name} :D")

def take_out_poop():
    time.sleep(2)
    print("You take out Bastet's poop")

def get_mail():
    time.sleep(4)
    print("You get the stupid ads")

# walk_Bastet()
# take_out_poop()
# get_mail()

# Esto corre uno en un thread, para poder hacerlo todo a la vez, hacemos lo siguiente:

chore1 = threading.Thread(target=walk_cat, args=("Bastet",)) # Es una tupla, si es sólo un elemento, poner coma
chore1.start()

chore2 = threading.Thread(target=take_out_poop)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join() # .join() hace que se una al main thread (el programa), y hasta que no termine este thread, no sigue main
chore2.join()
chore3.join()

print("All chores are complete!") # Para que esto se ejecute después de las 3 tareas, tenemos que poner join()
#                                   con cada una de ellas