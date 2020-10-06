from datetime import datetime
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, QRegExp
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QRegExpValidator
from banking.banking_ui.BankingWidget import Ui_Banking
from banking.banking_ui.AddBankAccountDialog import Ui_AddBankAccount
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

        self.selection_model = self.ui.AccountsTableView.selectionModel()
        self.selection_model.selectionChanged.connect(self.on_selectionChanged)

        self.ui.addBankAccountButton.clicked.connect(self.add_bank_account_dialog)

    def populate_model(self):
        for row, account in enumerate(self.accounts):
            # print(str(account))
            item = QStandardItem(str(account.account_name))
            balance = QStandardItem(str(account.current_balance) + ' MAD')
            self.model.setItem(row, 0, item)
            self.model.setItem(row, 1, balance)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_selectionChanged(self, selected):
        item = selected.indexes()[0]
        if item:
            self.selected = item.data()
            # self.show_movements(item.data())
            selected_account = BankAccount.objects.get(account_name=item.data())
            print(selected_account)
            self.ui.Acoount_Name.setText(selected_account.account_name)
            self.ui.Account_number.setText(selected_account.account_number)
            self.ui.Account_IBAN.setText(selected_account.IBAN_number)
            self.ui.Account_BIC.setText(selected_account.Swift_code)
            self.ui.Account_Proprietary.setText(selected_account.account_name)

    def add_bank_account_dialog(self):
        dialog = AddBankAccountForm()
        dialog.exec_()
        dialog.show()


class AddBankAccountForm(QDialog):
    def __init__(self):
        super(AddBankAccountForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_AddBankAccount()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.validate_form_data)

    def get_form_data(self):
        ref = self.ui.refLineEdit.text()
        account_name = self.ui.accountNameLineEdit.text()
        account_state = self.ui.stateCheckBox.checkState()
        initial_balance = self.ui.initialBalanceLineEdit.text()
        date_opened = self.ui.dateOpenedDateEdit.date().toPyDate().strftime("%Y-%m-%d")
        bank = self.ui.bankLineEdit.text()
        account_type = self.ui.accountTypeComboBox.currentText()
        account_number = self.ui.accountNumberLineEdit.text()
        IBAN = self.ui.iBANCodeLineEdit.text()
        BIC_SWIFT = self.ui.bICSWIFTCodeLineEdit.text()
        agency_address = self.ui.sucursalAddressLineEdit.text()
        proprietary = self.ui.accountProprietaryLineEdit.text()
        proprietary_address = self.ui.proprietaryAddressLineEdit.text()

        data_dict = {'Ref': ref,
                     'account_name': account_name,
                     'account_type': account_type,
                     'account_state': account_state,
                     'initial_balance': initial_balance,
                     'date_opened': date_opened,
                     'bank': bank,
                     'type': account_type,
                     'account_number': account_number,
                     'IBAN': IBAN,
                     'BIC_SWIFT': BIC_SWIFT,
                     'agency_address': agency_address,
                     'proprietary': proprietary,
                     'proprietary_address': proprietary_address}
        # print(data_dict)
        return data_dict

    def validate_form_data(self):
        data_dict = self.get_form_data()
        if len(data_dict['account_name']) >= 3:
            print('Account Name Valid')
        else:
            print('Account Name Invalid')

    def save_form_data(self):
        data = self.get_form_data()
        bank_account = BankAccount(account_name=data['account_name'],
                                   type=data['type'],
                                   date_opened=data['date_opened'],
                                   account_number=data['account_number'],
                                   bank=data['bank'],
                                   IBAN_number=data['IBAN'],
                                   Swift_code=data['BIC_SWIFT'],
                                   initial_balance=int(data['initial_balance']),
                                   proprietary=data['proprietary'],
                                   proprietary_address=data['proprietary_address'])
        bank_account.save()
