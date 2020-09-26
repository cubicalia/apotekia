from apotekia import db_setup
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog, QGridLayout

from customers.models import Customer
from customers.views import CustomerSearchDialog
from templates.ui.CustomerSearch import Ui_CustomerSearchWidget


class POS(QDialog):
    def __init__(self):
        super(POS, self).__init__()
        self.layout = QGridLayout()
        self.customer_search = CustomerSearchDialog()

        self.layout.addWidget(CustomerSearchDialog(), 1, 1)
        self.setLayout(self.layout)
