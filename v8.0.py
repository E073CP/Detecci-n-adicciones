import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QMessageBox, QRadioButton
from pregunta import Pregunta

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
                                        border-radius: 10px; }
         QPushButton:hover {background-color: #33EBC6;
                             border-color: #E1E817;
                                        }
                                    """

        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.setStyleSheet(estilo_boton)
        self.btn_siguiente = QPushButton("enviar")
        self.btn_siguiente.setStyleSheet(estilo_boton)

        self.setFixedSize(1000, 200)

        self.cuestionario = self.crearCuestionario()
        self.index = 0
        self.maximo = len(self.cuestionario)

        self.lb_num = QLabel("Num pregunta")
        self.lb_pregunta = QLabel("Pregunta")
        self.lb_pregunta.setFixedWidth(900)
        self.lb_pregunta.setWordWrap(True)

        # Radio Buttons
        self.btn_opcion1 = QRadioButton("Siempre")
        self.btn_opcion2 = QRadioButton("Casi siempre")
        self.btn_opcion3 = QRadioButton("Casi nunca")
        self.btn_opcion4 = QRadioButton("Nunca")

        self.btn_siguiente.clicked.connect(self.siguiente)

        layout = QGridLayout()
        layout.addWidget(self.lb_num, 0, 0, 1, 4)
        layout.addWidget(self.lb_pregunta, 1, 0, 1, 4)

        layout.addWidget(self.btn_opcion1, 2, 0)
        layout.addWidget(self.btn_opcion2, 2, 1)
        layout.addWidget(self.btn_opcion3, 2, 2)
        layout.addWidget(self.btn_opcion4, 2, 3)

        layout.addWidget(self.btn_siguiente, 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.siguiente()

    def crearCuestionario(self):
        return [
            Pregunta(1, "¿Con qué frecuencia sientes la necesidad de revisar tus redes sociales incluso sabiendo que no hay nada urgente?", 1),
            Pregunta(2, "¿Si no puedes revisar tus redes sociales por un tiempo (por ejemplo: sin batería o sin wifi), cómo reaccionas?", 3),
            Pregunta(3, "¿Con qué frecuencia tus actividades diarias (trabajo, estudio, comidas) son interrumpidas por notificaciones o la necesidad de revisar redes sociales?", 3),
            Pregunta(4, "¿Alguna vez has perdido horas de sueño significativas por pasar más tiempo en redes sociales?", 4),
            Pregunta(5, "¿Sientes que el tiempo que pasas en redes sociales interfiere con tus relaciones personales cara a cara?", 2),
            Pregunta(6, "¿Necesitas pasar cada vez más tiempo en redes sociales para obtener la misma satisfacción o alivio del aburrimiento?", 1),
            Pregunta(7, "¿Has intentado reducir o controlar tu tiempo en redes sociales sin éxito?", 3),
            Pregunta(8, "¿Has mentido u ocultado a otros (familiares, pareja) la cantidad real de tiempo que pasas en redes sociales?", 2),
            Pregunta(9, "Cuando usas redes sociales, ¿experimentas sentimientos negativos (culpa, tristeza, vacío o envidia) pero sigues usándolas?", 1),
            Pregunta(10, "¿Has usado las redes sociales como principal forma de escapar de problemas o emociones difíciles?", 2)
        ]

    def siguiente(self):
        num = str(self.cuestionario[self.index].num_pregunta)
        preg = self.cuestionario[self.index].texto

        self.lb_num.setText(f"Pregunta {num}")
        self.lb_pregunta.setText(preg)

        if self.index < self.maximo - 1:
            self.index += 1
        else:
            QMessageBox.information(self, "Fin", "Has llegado al final del cuestionario.")

app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()




  