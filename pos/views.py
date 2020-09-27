from apotekia import db_setup

from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QWidget

from customers.views import CustomerSearchDialog
from catalog.views import ProductSearchDialog


class POS(QWidget):
    def __init__(self):
        super(POS, self).__init__()
        self.layout = QGridLayout()

        self.product_search = ProductSearchDialog()
        self.customer_search = CustomerSearchDialog()

        self.layout.addWidget(self.product_search, 1, 1, 1, 1)
        self.layout.addWidget(self.customer_search, 2, 1, 1, 1)

        self.setLayout(self.layout)
