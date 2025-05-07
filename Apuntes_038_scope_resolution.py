# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Una función no puede ver las variables de otras funciones, ejemplo de Local:
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

# Ejemplo de Enclosed:
def func1():
    x = 1

    def func2():
        x = 2
        print(x)
    func2()

func1()

# Primero busca la 'x' local, que es '2', y la imprime. 
# Si borramos 'x = 2', al no haber local, busca en enclosed, que es 1.

# Ejemplo de Global:
def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

# Al no haber local ni enclosed, busca fuera de las funciones, e imprime '3' dos veces,
# una por cada función que hemos llamado.

# Ejemplo de Built-in:
from math import e

def func1():
    print(e)

e = 3 # Si añadimos esta línea, imprime esta 'e', porque es Global
# Si la quitamos, imprime la del módulo, que sería Built-in

func1()