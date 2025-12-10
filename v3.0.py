import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QLabel,QLineEdit, QPushButton, QMessageBox)

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        estilo_boton = """ QPushButton { background-color: #27F5D6;
                                          border: 2px solid #3AA695;
                                          color: white;
                                          padding: 15px 32px;
                                          text-align: center;
                                          text-decoration: none;
                                          font-size: 16px;
                                          margin: 4px 2px;
                                          border-radius: 10px;}
        QPushButton:hover {background-color: #33EBC6;
                           border-color: #E1E817;
                           }
                           """

        self.setWindowTitle("Registro")
        self.setGeometry(200, 200, 400, 200)

        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.setStyleSheet(estilo_boton)

        self.lb_nombre = QLabel("Nombre:")
        self.lb_correo = QLabel("Correo:")
        self.txt_nombre = QLineEdit()
        self.txt_correo = QLineEdit()

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.lb_nombre, 0, 0)
        layout.addWidget(self.txt_nombre, 0, 1)
        layout.addWidget(self.lb_correo, 1, 0)
        layout.addWidget(self.txt_correo, 1, 1)
        layout.addWidget(self.btn_guardar, 3, 1)

        self.btn_guardar.clicked.connect(self.guardar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def guardar(self):
        nombre = self.txt_nombre.text().strip()
        correo = self.txt_correo.text().strip()

        if nombre == "" or correo == "":
            QMessageBox.warning(self, "Error", "Debes llenar todos los campos.")
            return

        # Guardar en archivo
        with open("registro.txt", "a", encoding="utf-8") as file:
            file.write(f"Nombre: {nombre}, Correo: {correo}\n")

        QMessageBox.information(self, "Éxito", "Datos guardados correctamente.")

        # Limpiar campos
        self.txt_nombre.clear()
        self.txt_correo.clear()


app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()






