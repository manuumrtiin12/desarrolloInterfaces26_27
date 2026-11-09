
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class VentanaBienvenida(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación - Bienvenida")

        etiqueta = QLabel("¡Bienvenido a mi aplicación!\nGracias por visitarnos.")

        fuente = QFont()
        fuente.setPointSize(20)
        etiqueta.setFont(fuente)

        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        etiqueta.setWordWrap(True)

        self.setCentralWidget(etiqueta)

        self.resize(600, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaBienvenida()
    ventana.show()

    sys.exit(app.exec())
