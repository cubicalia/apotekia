import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
                             QVBoxLayout, QTabWidget, QFileDialog, QPlainTextEdit, QHBoxLayout, QLabel, QPushButton,
                             QSizePolicy, QLayout)
from sales.views import PointOfSaleWidget


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        self.initUI()

    def initUI(self):

        self.modules_menu()
        self.display_area()
        self.setLayout(self.layout)

    def modules_menu(self):
        self.vbox_1 = QVBoxLayout()
        self.vbox_1.setAlignment(Qt.AlignLeft)
        # ANALYTICS BUTTON
        self.analytics_module_button = QPushButton('ANALYTICS')
        self.analytics_module_button.setMinimumHeight(65)
        self.analytics_module_button.setMaximumHeight(95)
        self.analytics_module_button.setMinimumWidth(200)
        self.analytics_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.analytics_module_button)
        # INVENTORY BUTTON
        self.inventory_module_button = QPushButton('INVENTORY')
        self.inventory_module_button.setMinimumHeight(65)
        self.inventory_module_button.setMaximumHeight(95)
        self.inventory_module_button.setMinimumWidth(200)
        self.inventory_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.inventory_module_button)

        # CUSTOMERS BUTTON
        self.customers_module_button = QPushButton('CUSTOMERS')
        self.customers_module_button.setMinimumHeight(65)
        self.customers_module_button.setMaximumHeight(95)
        self.customers_module_button.setMinimumWidth(200)
        self.customers_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.customers_module_button)

        # SUPPLIERS BUTTON
        self.suppliers_module_button = QPushButton('SUPPLIERS')
        self.suppliers_module_button.setMinimumHeight(65)
        self.suppliers_module_button.setMaximumHeight(95)
        self.suppliers_module_button.setMinimumWidth(200)
        self.suppliers_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.suppliers_module_button)

        # PURCHASES BUTTON
        self.purchases_module_button = QPushButton('PURCHASES')
        self.purchases_module_button.setMinimumHeight(65)
        self.purchases_module_button.setMaximumHeight(95)
        self.purchases_module_button.setMinimumWidth(200)
        self.purchases_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.purchases_module_button)

        # RETURNS BUTTON
        self.returns_module_button = QPushButton('RETURNS')
        self.returns_module_button.setMinimumHeight(65)
        self.returns_module_button.setMaximumHeight(95)
        self.returns_module_button.setMinimumWidth(200)
        self.returns_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.returns_module_button)

        # CATALOGUE BUTTON
        self.catalogue_module_button = QPushButton('CATALOGUE')
        self.catalogue_module_button.setMinimumHeight(65)
        self.catalogue_module_button.setMaximumHeight(95)
        self.catalogue_module_button.setMinimumWidth(200)
        self.catalogue_module_button.setMaximumWidth(275)
        self.vbox_1.addWidget(self.catalogue_module_button)

        self.layout.addItem(self.vbox_1)

    def display_area(self):
        self.disp_area = PointOfSaleWidget()
        self.layout.addWidget(self.disp_area)


