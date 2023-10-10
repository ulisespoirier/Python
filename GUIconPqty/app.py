import sys

from PyQt6.QtWidgets import (
    QApplication,
    #QLineEdit,
    QVBoxLayout,
    QMainWindow,
    QPushButton,
    QWidget,
    QLabel,
    QTextEdit,
)

from PyQt6.QtGui import QPalette, QColor
from PyQt6 import QtWidgets

import base64
import io

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Window(QMainWindow):
    def __init__(self):
        
        super().__init__(parent=None)

        # Ventana principal
        self.setWindowTitle("Convertir string B64 a PDF")
        
        # Widgets
        self.etiqueta_texto = QLabel()
        self.etiqueta_texto.setText("Copie el c\u00F3digo B64 aqu\u00ED :")
        self.texto = QTextEdit()
        # No se pedirá nombre del archivo, sino al momento de grabarlo
        #self.etiqueta_nombre = QLabel("Nombre archivo.pdf")
        # self.nombre = QLineEdit()
        self.boton = QPushButton("Convertir!")
        self.boton.clicked.connect(self.b64_to_pdf)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))

        layout.addWidget(self.etiqueta_texto)
        layout.addWidget(self.texto)
        # No se pedirá nombre del archivo, sino al momento de grabarlo
        #layout.addWidget(self.etiqueta_nombre)
        #layout.addWidget(self.nombre)
        layout.addWidget(self.boton)

        widget = QWidget()
        widget.setLayout(layout)
        

        self.setCentralWidget(widget)

    def b64_to_pdf(self):
        pdf = base64.b64decode(self.texto.toPlainText())

        # write the decoded content to a PDF file
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save PDF", "", "Text Files (*.pdf)")
        if file_name:
            with open(file_name, 'wb') as archivo_pdf:
                archivo_pdf.write(pdf)
            
    """ Esta función sirve si es que hubiéramos pedido el nombre del archivo en la GUI    
    def Convertir(self):
        nombre = self.nombre.toPlainText()
        pdf = base64.b64decode(self.texto.toPlainText())
        # write the decoded content to a PDF file
        with open(nombre, 'wb') as archivo_pdf:
            archivo_pdf.write(pdf)
        print("Archivo generado")
    """    
        
if __name__ == "__main__":
    """Every application needs one — and only one — QApplication object to function"""
    app = QApplication([]) 
    window = Window()
    window.show()
    sys.exit(app.exec())