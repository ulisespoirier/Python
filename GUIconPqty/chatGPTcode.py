from PyQt6 import QtWidgets, QtGui
import sys

class SaveTextGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QtWidgets.QLabel("Enter text to save:")
        self.text_box = QtWidgets.QTextEdit()
        self.save_button = QtWidgets.QPushButton("Save")
        self.save_button.clicked.connect(self.save_text)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_box)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle("Save Text to File")

       
    def save_text(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Text", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, "w") as file:
                text = self.text_box.toPlainText()
                file.write(text)
            self.text_box.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = SaveTextGUI()
    gui.show()
    sys.exit(app.exec())
