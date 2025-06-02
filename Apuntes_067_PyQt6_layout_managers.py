# PyQt6 layouts
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, 
                             QVBoxLayout, QHBoxLayout, QGridLayout)
#                            Las tres últimas no son widgets, son layout managers

# Normally, we can't add a layout manager to a MainWindow object. 
# MainWindow widgets have a specific design and layout structure that's normally
# incompatible with layout managers. So, we need to create a generic widget, 
# add a layout manager to that widget and then add that widget to the MainWindow
# so we can display the layout.

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget() # Generic widget
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;") 
        # Todos se están superponiendo, por eso vemos sólo el último
        # Para que eso no pase, usamos el layout manager:

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox) # Para que fuera horizontal, cambiamos 'vbox' por 'hbox' en todos

        # Para hacer una grid, hacemos lo siguiente:
        grid = QGridLayout()

        grid.addWidget(label1, 0, 0) # Especificamos row and column
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()