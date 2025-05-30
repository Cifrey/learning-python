# PyQt6 introduction
# Graphical User Interface = GUI
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow): # Hacemos una subclase llamando a la clase super 'QMainWindow'
    def __init__(self): # El constructor de siempre
        super().__init__() # Método super() para tener todo el constructor de 'QMainWindow'
        self.setWindowTitle("Mira qué chulo :O")
        self.setGeometry(1000, 450, 500, 500) # x, y, width, height
        self.setWindowIcon(QIcon("Python/iconito.png"))

def main():
    app = QApplication(sys.argv) # Hacemos el objeto que queremos 'app' de la clase original 'QApplication' y pasamos
#                                  el argumento 'sys', que normalmente se omite siempre pero con esta librería hace falta
#                                  y accedemos a 'argv' para poder pasar argumentos  

    window = MainWindow() # Lo mismo aquí, un objeto a partir de la clase que hemos hecho (que a su vez ya importa de otra)       
    
    window.show() # Por defecto las ventanas están en 'hide', ponemos '.show()' para mostrarla pero sólo sale un segundo
    
    sys.exit(app.exec()) 
#   Accedemos al módulo 'sys' y luego la función '.exit()' para poder cerrar el programa cuando queramos.
#   Si no se añade nada, es valor 0 -> '.exit(0)', que es un clean exit, se cierra sin problema. Al revés sería un 1.
#   Nuestra app accede al método '.exec_()', que esperará a user input y maneja eventos como hacer clic a botones,
#   pulsar teclas o cerrar la ventana.

if __name__ == "__main__":
    main()