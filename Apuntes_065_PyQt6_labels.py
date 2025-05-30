# PyQt6 labels
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Mira qué chulo :O")
        self.setGeometry(1000, 450, 700, 500)
        self.setWindowIcon(QIcon("Python/iconito.png"))

        label = QLabel("Andrés, te quiero", self) # Este self es de 'window = MainWindow()', el objeto. 'window' será parent widget
        label.setFont(QFont("Consolas", 50)) # Se corta la frase porque no está bien posicionada
        label.setGeometry(0, 0, 700, 200)
        label.setStyleSheet("color: #f79ef7;"
                            "background-color: #ffde82;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # Es como CSS
        # label.setAlignment(Qt.AlignmentFlag.AlignTop) # Vertically top
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom) # Vertically bottom
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft) # Horizontally left        
        # label.setAlignment(Qt.AlignmentFlag.AlignRight) # Horizontally right
        # label.setAlignment(Qt.AlignmentFlag.AlignVCenter) # Vertically center
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter) # Horizontally center

        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop) # Center & top
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom) # Center & bottom
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # Center & center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center center short

def main():
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()