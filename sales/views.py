import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apotekia.settings')
django.setup()

from catalog.models import Product
from customers.models import Customer

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QListWidget, QPushButton)
from templates.ui.ObjSearchWidget import ObjectSearchWidget

from templates.ui.communication.notifications import AlertBox


class PointOfSaleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.vbox1()
        self.layout.addWidget(self.vbox1)
        self.setLayout(self.layout)

    def vbox_1(self):
        vbox = QVBoxLayout()
        # Client search widget
        vbox.addWidget(ObjectSearchWidget())
        # Product Search Widget
        vbox.addWidget(ObjectSearchWidget())
        self.layout.addWidget(vbox)