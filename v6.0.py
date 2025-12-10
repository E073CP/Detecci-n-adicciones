import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget, QPushButton
from PyQt5.QtCore import *

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        estilo_boton = """QPushButton {background-color: #27F5D6;
                                        border: 2px solid #3AA695;
                                        color: white;
                                        padding: 15px 32px;
                                        text-align: center;
                                        font-size: 16px;
                                        margin: 4px 2px;
                                        border-radius: 10px; }
        QPushButton:hover {background-color: #33EBC6;
                           border-color: #E1E817;
                                    }
                                    """
        self.btn_reguistro = QPushButton("Registro")
        self.btn_reguistro.setStyleSheet(estilo_boton)

        self.btn_test = QPushButton("Test")
        self.btn_test.setStyleSheet(estilo_boton)

        self.btn_resultados = QPushButton("Resultados")
        self.btn_resultados.setStyleSheet(estilo_boton)

        # Ventana principal
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 400, 300)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Pestañas
        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_res = QWidget()

        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")

        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()

    def crear_pestana_registro(self):
        layout = QGridLayout()
        etiqueta1 = QLabel("Registro")
        layout.addWidget(etiqueta1, 0, 0)

        layout.addWidget(self.btn_reguistro, 1, 0)

        self.tab_registro.setLayout(layout)

    def crear_pestana_test(self):
        layout = QGridLayout()
        etiqueta2 = QLabel("Test")
        layout.addWidget(etiqueta2, 0, 0)

        layout.addWidget(self.btn_test, 1, 0)

        self.tab_test.setLayout(layout)

    def crear_pestana_resultados(self):
        layout = QGridLayout()
        etiqueta3 = QLabel("Resultados")
        layout.addWidget(etiqueta3, 0, 0)

        layout.addWidget(self.btn_resultados, 1, 0)

        self.tab_res.setLayout(layout)


app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()
