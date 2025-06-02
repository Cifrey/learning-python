# PyQt6 buttons
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.label = QLabel("Hello", self)
        self.initUI()


    def initUI(self):
        self.button = QPushButton("Click me!", self) # The second 'self' refers to 'window' object
        # Normally when creating widgets, we would want to prefix that widget with 'self', then follow
        # the name of the widget. If we don't do that, it would be a local variable.
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # A signal is emitted when a widget is interacted with. We have to list the type of signal,
        # in this case is '.clicked'. '.connect()' is a method

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!") # If we don't write 'self' in 'self.button' in 'initUI', we can't access this
        self.button.setDisabled(True) # If we want to disable the button once clicked
        self.label.setText("Goodbye!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())