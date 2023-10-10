import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QMainWindow,
    QPushButton,
    
)

from PyQt6.QtCore import (
    QSize,
    Qt
)

class Window(QMainWindow):
    def __init__(self):
        
        super().__init__(parent=None)
        self.setWindowTitle("Convertir string B64 a PDF")
        button = QPushButton("Convertir!")
        button.setCheckable(True)
        button.clicked.connect(self.Convertir)
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)
        
    def Convertir(self):
        print("Convertido")
    
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())