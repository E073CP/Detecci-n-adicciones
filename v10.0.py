# Importamos las bibliotecas
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget,QPushButton, QLineEdit, QRadioButton, QMessageBox)
from PyQt5.QtCore import *
class Pregunta:
    def __init__(self, num_pregunta, texto, valor):
        self.num_pregunta = num_pregunta
        self.texto = texto
        self.valor = valor
        
class Principal(QMainWindow):
    def __init__(self):
        super().__init__()

        estilo_boton = """QPushButton {  background-color: #A000AB;
                                            border: 2px solid #741CE8;
                                            color: black;
                                            padding: 10px 20px;
                                            font-size: 15px;
                                            border-radius: 10px;
                                        }
                                        QPushButton:hover {
                                            background-color:#294D44;
                                            border-color: #29291C;
                                        }

                                        QLabel { 
                                            background-color: #857BBD;
                                            border: 2px solid #287369;
                                            padding: 6px 10px;
                                            font-size: 16px;
                                            border-radius: 8px;
                                            color: #1E1E1E;
                                        }

                                        QLineEdit {
                                            border: 2px solid #7B9C97;
                                            border-radius: 10px;
                                            padding: 6px;
                                            background-color:black ;
                                        }
                                        """

        self.setStyleSheet(estilo_boton)

        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 700, 500)
        self.setFixedSize(700, 500)

        # Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_res = QWidget()
        self.tab_graf = QWidget()

        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")
        self.tabs.addTab(self.tab_graf, "Graficas")

        self.tab_registro.setStyleSheet("background-color: #FDFAE8;")  
        self.tab_test.setStyleSheet("background-color: #B5D9F7;")  
        self.tab_res.setStyleSheet("background-color: #B5D9F7;")  
        self.tab_graf.setStyleSheet("background-color: #B5B8F7;")  

        # Variables
        self.respuestas = []
        self.index = 0

        # Crear pestañas
        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()
        self.crear_pestana_graficas()


    #pestana registro 
    def crear_pestana_registro(self):
        layout = QGridLayout()

        self.lb_nombre = QLabel("Nombre:")
        self.lb_correo = QLabel("Correo:")
        self.txt_nombre = QLineEdit()
        self.txt_correo = QLineEdit()

        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.clicked.connect(self.guardar)

        layout.addWidget(self.lb_nombre, 0, 0)
        layout.addWidget(self.txt_nombre, 0, 1)
        layout.addWidget(self.lb_correo, 1, 0)
        layout.addWidget(self.txt_correo, 1, 1)
        layout.addWidget(self.btn_guardar, 2, 1)

        self.tab_registro.setLayout(layout)


    def guardar(self):
        nombre = self.txt_nombre.text().strip()
        correo = self.txt_correo.text().strip()

        if nombre == "" or correo == "":
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos.")
            return

        QMessageBox.information(self, "Correcto", "Datos guardados correctamente!")

        self.txt_nombre.clear()
        self.txt_correo.clear()


    #pestaña test 
    def crear_pestana_test(self):
        layout = QGridLayout()

        self.cuestionario = self.crearCuestionario()
        self.index = 0

        self.lb_num = QLabel("")
        self.lb_pregunta = QLabel("")
        self.lb_pregunta.setFixedWidth(600)
        self.lb_pregunta.setWordWrap(True)

        # Opciones
        self.btn_opcion1 = QRadioButton("Siempre")
        self.btn_opcion2 = QRadioButton("Casi siempre")
        self.btn_opcion3 = QRadioButton("Casi nunca")
        self.btn_opcion4 = QRadioButton("Nunca")

        # Botón siguiente
        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        # Layout
        layout.addWidget(self.lb_num, 0, 0, 1, 4)
        layout.addWidget(self.lb_pregunta, 1, 0, 1, 4)

        layout.addWidget(self.btn_opcion1, 2, 0)
        layout.addWidget(self.btn_opcion2, 2, 1)
        layout.addWidget(self.btn_opcion3, 2, 2)
        layout.addWidget(self.btn_opcion4, 2, 3)

        layout.addWidget(self.btn_siguiente, 3, 3)

        self.tab_test.setLayout(layout)

        self.mostrarPregunta()


    def crearCuestionario(self):
        return [
            Pregunta(1, "¿Con qué frecuencia sientes la necesidad de revisar tus redes sociales sin razón urgente?", 1),
            Pregunta(2, "¿Cómo reaccionas si no puedes revisar tus redes sociales por un tiempo?", 3),
            Pregunta(3, "¿Tus actividades diarias se interrumpen por revisar redes sociales?", 3),
            Pregunta(4, "¿Has perdido horas de sueño usando redes sociales?", 4),
            Pregunta(5, "¿Interfiere el uso de redes en tus relaciones personales cara a cara?", 2),
            Pregunta(6, "¿Necesitas pasar más tiempo en redes para sentir lo mismo?", 1),
            Pregunta(7, "¿Has intentado reducir tu uso sin éxito?", 3),
            Pregunta(8, "¿Has ocultado cuánto usas redes sociales?", 2),
            Pregunta(9, "¿Usas redes aunque te hagan sentir mal emocionalmente?", 1),
            Pregunta(10, "¿Usas redes para escapar de problemas o emociones difíciles?", 2),
        ]


    def obtenerValorSeleccionado(self):
        if self.btn_opcion1.isChecked():
            return 4
        elif self.btn_opcion2.isChecked():
            return 3
        elif self.btn_opcion3.isChecked():
            return 2
        elif self.btn_opcion4.isChecked():
            return 1
        return None


    def limpiarSeleccion(self):
        self.btn_opcion1.setAutoExclusive(False)
        self.btn_opcion2.setAutoExclusive(False)
        self.btn_opcion3.setAutoExclusive(False)
        self.btn_opcion4.setAutoExclusive(False)

        self.btn_opcion1.setChecked(False)
        self.btn_opcion2.setChecked(False)
        self.btn_opcion3.setChecked(False)
        self.btn_opcion4.setChecked(False)

        self.btn_opcion1.setAutoExclusive(True)
        self.btn_opcion2.setAutoExclusive(True)
        self.btn_opcion3.setAutoExclusive(True)
        self.btn_opcion4.setAutoExclusive(True)


    def mostrarPregunta(self):
        pregunta = self.cuestionario[self.index]
        self.lb_num.setText(f"Pregunta {pregunta.num_pregunta}")
        self.lb_pregunta.setText(pregunta.texto)
        self.limpiarSeleccion()


    def siguiente(self):
        valor = self.obtenerValorSeleccionado()

        if valor is None:
            QMessageBox.warning(self, "Error", "Debe seleccionar una opción.")
            return

        self.respuestas.append(valor)
        self.index += 1

        if self.index == len(self.cuestionario):
            self.mostrarResultados()
            self.tabs.setCurrentWidget(self.tab_res)
        else:
            self.mostrarPregunta()


    #pestaña resultados 
    def crear_pestana_resultados(self):
        self.layout_res = QGridLayout()
        self.lb_resultado = QLabel("Aquí aparecerán los resultados del test")
        self.layout_res.addWidget(self.lb_resultado, 0, 0)
        self.tab_res.setLayout(self.layout_res)


    def mostrarResultados(self):
        puntaje = sum(self.respuestas)

        if puntaje <= 15:
            nivel = "Bajo uso en redes sociales"
        elif puntaje <= 25:
            nivel = "Uso moderado de redes sociales"
        else:
            nivel = "Alto riesgo de adicción a las redes sociales"

        self.lb_resultado.setText(f"Tu puntaje total es: {puntaje}\nNivel: {nivel}")


    #pestaña graficas 
    def crear_pestana_graficas(self):
        self.layout_graf = QGridLayout()
        self.lb_graficas = QLabel("Aquí aparecerán las gráficas")
        self.layout_graf.addWidget(self.lb_graficas, 0, 0)
        self.tab_graf.setLayout(self.layout_graf)



# Ejecutar aplicación
app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()


