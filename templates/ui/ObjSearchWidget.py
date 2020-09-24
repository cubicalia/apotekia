import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apotekia.settings')
django.setup()

from catalog.models import Product
from customers.models import Customer

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QListWidget, QPushButton)

from templates.ui.communication.notifications import AlertBox


class FooterButtons(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.add_button = QPushButton('Add entry')
        self.add_button.clicked.connect(self.add_action)
        self.edit_button = QPushButton('Edit entry')
        self.delete_button = QPushButton('Delete entry')

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def add_action(self):
        AlertBox('Hello world')

    def edit_action(self):
        pass

    def delete_action(self):
        pass


class ListResultsWidget(QListWidget):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initUI()

    def initUI(self):
        self.setAlternatingRowColors(True)
        self.load_data()

    def load_data(self):
        data = self.model.objects.all()
        for i in data:
            self.addItem(i.__str__())


class ObjectSearchWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.search_field = QLineEdit()
        self.list_resuls = ListResultsWidget(Customer)
        self.buttons_footer = FooterButtons()

        self.layout.addWidget(self.search_field)
        self.layout.addWidget(self.list_resuls)
        self.layout.addWidget(self.buttons_footer)

        self.setLayout(self.layout)

