import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
                             QVBoxLayout, QTabWidget, QFileDialog, QPlainTextEdit, QHBoxLayout, QLabel, QPushButton,
                             QSizePolicy, QLayout)


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.modules_menu()
        self.setLayout(self.layout)

    def modules_menu(self):
        self.vbox_1 = QVBoxLayout()
        self.vbox_1.setAlignment(Qt.AlignLeft)
        # POINT OF SALE BUTTON
        self.pos_module_button = QPushButton('Point Of Sale')
        self.pos_module_button.setMinimumHeight(65)
        self.pos_module_button.setMaximumHeight(95)
        self.pos_module_button.setMinimumWidth(200)
        self.pos_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.pos_module_button)
        # INVENTORY BUTTON
        self.inventory_module_button = QPushButton('Inventory')
        self.inventory_module_button.setMinimumHeight(65)
        self.inventory_module_button.setMaximumHeight(95)
        self.inventory_module_button.setMinimumWidth(200)
        self.inventory_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.inventory_module_button)

        self.layout.addItem(self.vbox_1)


