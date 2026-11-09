
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Slot


class VentanaProyecto(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Proyecto sin nombre")

        self.entrada = QLineEdit()

        # Placeholder
        self.entrada.setPlaceholderText("Introduce el nombre del proyecto")

        self.entrada.setMaxLength(30)

        self.entrada.textChanged.connect(self.actualizar_titulo)

        self.setCentralWidget(self.entrada)

        self.resize(500, 200)

    @Slot(str)
    def actualizar_titulo(self, texto):

        nombre = texto.strip()

        if not nombre:
            self.setWindowTitle("Proyecto sin nombre")
        else:
            # Mostrar el nombre en mayúsculas
            self.setWindowTitle(nombre.upper())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaProyecto()
    ventana.show()

    sys.exit(app.exec())
