# PyQt6 buttons
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you love me?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")

        self.checkbox.setChecked(False) # Para que aparezca con el tick o no por defecto
        self.checkbox.stateChanged.connect(self.checkbox_changed) # '.stateChanged' es un signal

    def checkbox_changed(self, state):
        # if state == 2: # Se podría poner así pero otros devs no lo entenderían bien, mejor poner:
        if Qt.CheckState(state) == Qt.CheckState.Checked:
            print("You love me :3 Yaaay")
        else:
            print("You don't love me ;___;")
        # print(state) # 0 es 'Unchecked', 2 es 'Checked'. 1 es PartiallyChecked pero no lo veremos ahora

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())