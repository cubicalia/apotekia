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

        self.layout.addWidget(self.product_search)
        self.layout.addWidget(self.customer_search)

        self.setLayout(self.layout)
