# PyQt6 images
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.setGeometry(1000, 450, 700, 500) # Esto es para dónde aparece la ventana y cómo de grande es

        label = QLabel(self) # Este self es de 'window' object
        label.setGeometry(0, 0, 250, 250) # Dónde sale el label y cómo de grande es

        pixmap = QPixmap("Python/imagenprueba.jpg")
        label.setPixmap(pixmap) # Para llamar a la imagen

        label.setScaledContents(True) # Para escalar bien la imagen

        # label.setGeometry(self.width() - label.width(), # Right justified. Si fuera 0 es bottom left justified
        #                   self.height() - label.height(), # Bottom right justified
        #                   label.width(), # Para no tener que cambiar el alto y ancho en varios sitios,
        #                   label.height()) # podemos simplemente llamar a width() y height()                                                               

#       Para centrarla, haríamos lo siguiente:
        label.setGeometry((self.width() - label.width()) // 2, # '//' hace divisiones para enteros sin dar decimales
                          (self.height() - label.height()) // 2,
                          label.width(), 
                          label.height())

def main():
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()