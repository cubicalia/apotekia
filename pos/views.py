from apotekia import db_setup

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGridLayout, QWidget, QSizePolicy

from banking.views import BankingDialog
from customers.views import CustomerSearchDialog
from catalog.views import ProductSearchDialog, ProductDialog
from inventory.tests import InventoryDialog
from sales.views import BasketPOSWidget, DisplayPOSTotalsWidget


class POS(QWidget):
    def __init__(self):
        super(POS, self).__init__()
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Initiaite Widgets
        self.product_search = ProductSearchDialog()
        self.customer_search = CustomerSearchDialog()
        self.basket_widget = BasketPOSWidget()
        self.totals_widget = DisplayPOSTotalsWidget()

        # Layout Widgets
        self.layout.addWidget(self.product_search, 1, 1, 2, 2)
        self.layout.addWidget(self.customer_search, 3, 1, 1, 1)
        self.layout.addWidget(self.basket_widget, 1, 3, 3, 1)
        self.layout.addWidget(self.totals_widget, 3, 2, 1, 1)

        self.setLayout(self.layout)


