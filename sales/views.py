from apotekia import db_setup

from PyQt5.QtWidgets import QWidget
from templates.ui.BasketWidget import Ui_Form
from templates.ui.TotalsFormWidget import Ui_TotalsWidget


class BasketPOSWidget(QWidget):
    def __init__(self):
        super(BasketPOSWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class DisplayPOSTotalsWidget(QWidget):
    def __init__(self):
        super(DisplayPOSTotalsWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_TotalsWidget()
        self.ui.setupUi(self)