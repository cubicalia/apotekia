import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
                             QVBoxLayout, QTabWidget, QFileDialog, QPlainTextEdit, QHBoxLayout, QLabel, QPushButton,
                             QSizePolicy, QGridLayout)

from pos.views import POS
from templates.ui.ObjSearchWidget import ObjectSearchWidget
from customers.views import CustomerSearchDialog
from apotekia.settings import APPS

lineBarColor = QColor(53, 53, 53)
lineHighlightColor = QColor('#00FF04')


class ModuleMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        for app in APPS:
            button = QPushButton(app.upper())
            button.setMaximumWidth(215)
            button.setMinimumWidth(125)
            button.setMaximumHeight(75)
            button.setMinimumHeight(50)
            self.layout.addWidget(button)

        self.setLayout(self.layout)


class CentralWidget(QWidget):

    def __init__(self):
        super(CentralWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout(self)
        # Initialize tab screen
        self.module_menu = ModuleMenu()
        self.pos = POS()

        # Add tabs to widget
        self.layout.addWidget(self.module_menu)
        self.layout.addWidget(self.pos)

        self.setLayout(self.layout)