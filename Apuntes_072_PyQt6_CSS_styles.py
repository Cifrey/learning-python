# PyQt6 setStyleSheet()
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        # self.setGeometry(700, 300, 500, 500) # Since we're using 'QHBoxLayout', we don't need this line
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        # Triple quotes are used to write very long strings
        # Podemos cambiar el CSS de todo 'QPushButton' o uno a uno
        # O cambiar de todo y hacer una excepción o algo específico
        # si creamos un objeto con 'setObjectName' y luego lo llamamos
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Consolas;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: hsl(44, 100%, 81%);
            }
            QPushButton#button2{
                background-color: hsl(202, 93%, 73%);
            }
            QPushButton#button3{
                background-color: hsl(295, 85%, 87%);
            }
            QPushButton#button1:hover{
                background-color: hsl(44, 100%, 61%);
            }
            QPushButton#button2:hover{
                background-color: hsl(202, 93%, 53%);
            }
            QPushButton#button3:hover{
                background-color: hsl(295, 85%, 67%);
            }
        """) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
