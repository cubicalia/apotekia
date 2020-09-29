from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy)
from inventory.views import InventoryDialog

from templates.ui.ModulesWidget import ModulesUI
from pos.views import POS
from apotekia.settings import APPS

lineBarColor = QColor(53, 53, 53)
lineHighlightColor = QColor('#00FF04')


class ModuleMenu(QWidget):
    def __init__(self):
        super(ModuleMenu, self).__init__()
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.initUI()

    def initUI(self):
        self.ui = ModulesUI()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.open_dialog)

    def open_dialog(self):
        dialog = InventoryDialog()
        dialog.exec_()
        dialog.show()


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