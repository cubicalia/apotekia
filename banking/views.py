from apotekia import db_setup
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from templates.ui.BankingWidget import Ui_Banking
from banking.models import BankAccount


class BankingDialog(QDialog):
    def __init__(self):
        super(BankingDialog, self).__init__()

        self.accounts = BankAccount.objects.all()
        self.model = QStandardItemModel(len(self.accounts), 1)
        self.model.setHorizontalHeaderLabels(['Accounts', 'Balance'])
        self.populate_model()

        self.initUI()

    def initUI(self):
        self.ui = Ui_Banking()
        self.ui.setupUi(self)
        self.ui.AccountsTableView.setModel(self.model)

    def populate_model(self):
        for row, account in enumerate(self.accounts):
            print(str(account))
            item = QStandardItem(str(account.account_name))
            balance = QStandardItem(str(account.current_balance))
            self.model.setItem(row, 0, item)
            self.model.setItem(row, 1, balance)
