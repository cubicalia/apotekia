import sys

from PyQt5.QtWidgets import QDialog, QApplication
from templates.ui.CustomerSearch import Ui_CustomerSearchWidget
from.models import Customer


class CustomerSearchDialog(QDialog):
    def __init__(self):
        super(CustomerSearchDialog, self).__init__()

        # Set up the user interface from Designer.
        self.initUI()

        # Here connect functionalities

    def initUI(self):
        self.ui = Ui_CustomerSearchWidget()
        self.ui.setupUi(self)
