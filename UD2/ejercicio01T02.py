
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Parte A: ventana principal de Game Shop
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana
        self.setWindowTitle("Game Shop")
        self.resize(600, 350)
        self.setMinimumSize(400, 250)

        # Creamos un botón
        self.boton = QPushButton("Iniciar sesión")

        # Colocamos el botón en el centro de la ventana
        self.setCentralWidget(self.boton)


# Parte C: segunda ventana alternativa
class VentanaAlternativa(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana alternativa
        self.setWindowTitle("Gestor de videojuegos")
        self.resize(500, 300)
        self.setMinimumSize(350, 200)

        # Creamos un botón relacionado con la aplicación
        self.boton = QPushButton("Ver catálogo")

        # Colocamos el botón en el centro
        self.setCentralWidget(self.boton)


if __name__ == "__main__":
    # Creamos la aplicación
    app = QApplication(sys.argv)

    # Elegimos qué ventana queremos ejecutar
    ventana = Ventana()  # Parte A
    # ventana = VentanaAlternativa()  # Parte C

    # Mostramos la ventana e iniciamos el bucle de eventos
    ventana.show()
    sys.exit(app.exec())
