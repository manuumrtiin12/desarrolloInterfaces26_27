
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game Shop")
        self.setFixedSize(600, 350)

        self.boton = QPushButton("Pulsar")

        self.boton.setCheckable(False)

        self.boton.pressed.connect(self.boton_presionado)
        self.boton.released.connect(self.boton_liberado)

        self.setCentralWidget(self.boton)

    def boton_presionado(self):
        self.boton.setText("Soltar")
        print("Botón presionado")

    def boton_liberado(self):
        self.boton.setText("Pulsar")
        print("Botón liberado")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()

    ventana.show()
    sys.exit(app.exec())
