from apotekia import db_setup
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QWidget

from customers.models import Customer
from customers.views import CustomerSearchDialog
from catalog.views import ProductSearchDialog
from templates.ui.CustomerSearch import Ui_CustomerSearchWidget


class POS(QWidget):
    def __init__(self):
        super(POS, self).__init__()
        self.layout = QHBoxLayout()

        self.product_search = ProductSearchDialog()
        self.customer_search = CustomerSearchDialog()

        self.layout.addWidget(self.product_search)
        self.layout.addWidget(self.customer_search)

        self.setLayout(self.layout)
