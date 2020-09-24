import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
                             QVBoxLayout, QTabWidget, QFileDialog, QPlainTextEdit, QHBoxLayout, QLabel, QPushButton,
                             QSizePolicy)


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
