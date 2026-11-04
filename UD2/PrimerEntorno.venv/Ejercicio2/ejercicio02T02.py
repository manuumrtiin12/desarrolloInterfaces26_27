
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        # Estado inicial
        self.activo = False

        # Configuración de la ventana
        self.setWindowTitle("Sistema de vigilancia - DESACTIVADO")
        self.setGeometry(100, 100, 400, 200)

        # Crear botón
        self.boton = QPushButton("Activar vigilancia", self)
        self.boton.setCheckable(True)
        self.boton.setGeometry(100, 70, 200, 40)

        # Conectar señales con sus respectivos métodos
        self.boton.clicked.connect(self.registrar_activacion)
        self.boton.toggled.connect(self.actualizar_estado)

    @Slot(bool)
    def registrar_activacion(self, pulsado):
        """Registra en consola cada activación o desactivación."""
        if pulsado:
            print("Vigilancia ACTIVADA")
        else:
            print("Vigilancia DESACTIVADA")

    @Slot(bool)
    def actualizar_estado(self, estado):
        """Actualiza la interfaz según el estado del botón."""
        self.activo = estado

        if self.activo:
            self.setWindowTitle("Sistema de vigilancia - ACTIVADO")
            self.boton.setText("Desactivar vigilancia")
        else:
            self.setWindowTitle("Sistema de vigilancia - DESACTIVADO")
            self.boton.setText("Activar vigilancia")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
