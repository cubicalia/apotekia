from apotekia import db_setup
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from templates.ui.BankingWidget import Ui_Banking
from banking.models import BankAccount


class BankingDialog(QDialog):
    def __init__(self):
        super(BankingDialog, self).__init__()
        self.banks = BankAccount.objects.all()

        self.initUI()

    def initUI(self):
        self.ui = Ui_Banking()
        self.ui.setupUi(self)