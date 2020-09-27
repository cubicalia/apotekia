from apotekia import db_setup
import sys

from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from templates.ui.BasketWidget import Ui_Form
from templates.ui.TotalsFormWidget import Ui_TotalsWidget

from sales.models import Basket, BasketLine


class BasketPOSDialog(QWidget):
    def __init__(self):
        super(BasketPOSDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class DisplayPOSTotalsDialog(QWidget):
    def __init__(self):
        super(DisplayPOSTotalsDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_TotalsWidget()
        self.ui.setupUi(self)