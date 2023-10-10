# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:42:38 2023

@author: ulises
"""

import sys
"""Provee la función exit() para terminar limpiamente la App."""

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 500

class Ventana(QMainWindow):
    """Converter's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertidor B64 <--> PDF")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

def main():
    """Converter's main function."""
    convertidorApp = QApplication([])
    ventana = Ventana()
    ventana.show()
    sys.exit(convertidorApp.exec())

if __name__ == "__main__":
    main()