from datetime import datetime

import numpy as np
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, QRegExp
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QRegExpValidator
from banking.banking_ui.BankingWidget import Ui_Banking
from banking.banking_ui.AddBankAccountDialog import Ui_AddBankAccount
from banking.models import BankAccount

from apotekia import settings


class BankingDialog(QDialog):
    def __init__(self):
        super(BankingDialog, self).__init__()

        self.accounts = BankAccount.objects.all()
        self.model = QStandardItemModel(len(self.accounts), 1)
        self.model.setHorizontalHeaderLabels(['REF', 'Accounts', 'Balance'])
        self.populate_accounts_model()

        self.initUI()

    def initUI(self):
        self.ui = Ui_Banking()
        self.ui.setupUi(self)
        self.ui.AccountsTableView.setModel(self.model)

        self.selection_model = self.ui.AccountsTableView.selectionModel()
        self.selection_model.selectionChanged.connect(self.on_selectionChanged)

        self.ui.addBankAccountButton.clicked.connect(self.add_bank_account_dialog)

    def populate_accounts_model(self):
        for row, account in enumerate(self.accounts):
            ref = QStandardItem(str(account.id))
            item = QStandardItem(str(account.account_name))
            balance = QStandardItem(str(account.initial_balance) + ' MAD')
            self.model.setItem(row, 0, ref)
            self.model.setItem(row, 1, item)
            self.model.setItem(row, 2, balance)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_selectionChanged(self, selected):
        item = selected.indexes()[0]
        if item:
            self.selected = item.data()
            # self.show_movements(item.data())
            selected_account = BankAccount.objects.get(id=item.data())
            self.ui.Acoount_Name.setText(selected_account.account_name)
            self.ui.Account_number.setText(selected_account.account_number)
            self.ui.Account_IBAN.setText(selected_account.IBAN_number)
            self.ui.Account_BIC.setText(selected_account.Swift_code)
            self.ui.Account_Proprietary.setText(selected_account.account_name)
            self.populate_entries_model(selected_account)

    def add_bank_account_dialog(self):
        dialog = AddBankAccountForm()
        dialog.exec_()
        dialog.show()

    def populate_entries_model(self, selected):
        selected_account = BankAccount.objects.get(id=selected.id)
        model = QStandardItemModel(selected_account.lines.all().count(), 1)
        model.setHorizontalHeaderLabels(['REF', 'Account', 'Date of Operation', 'Date of Value', 'Value'])
        self.ui.BankEntriesView.setModel(model)

        for row, line in enumerate(selected_account.lines.all()):
            ref = QStandardItem(str(line.id))
            account = QStandardItem(str(line.account.account_name))
            date_of_operation = QStandardItem(line.date_of_operation.strftime("%Y-%m-%d"))
            date_of_value = QStandardItem(line.date_of_value.strftime("%Y-%m-%d"))
            value = QStandardItem(str(line.value))

            model.setItem(row, 0, ref)
            model.setItem(row, 1, account)
            model.setItem(row, 2, date_of_operation)
            model.setItem(row, 3, date_of_value)
            model.setItem(row, 4, value)

        current_balance = self.calculate_current_balance(selected_account)
        self.ui.CurrentBalance.setText(str(current_balance) + ' ' + settings.DEFAULT_CURRENCY)
        self.ui.Account_Name.setText('ACCOUNT:  ' +
                                     selected_account.account_name +
                                     '\n' +
                                     selected_account.account_number)

    def calculate_current_balance(self, account):
        values = np.array([])
        for entry in account.lines.all():
            values = np.append(values, [float(entry.value)])

        current_balance = np.sum(values)
        return current_balance


class AddBankAccountForm(QDialog):
    def __init__(self):
        super(AddBankAccountForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_AddBankAccount()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.save_form_data)

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
            print(int(data_dict['initial_balance']))
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
                                   initial_balance=float(data['initial_balance']),
                                   proprietary=data['proprietary'],
                                   proprietary_address=data['proprietary_address'])
        bank_account.save()
        if self.validate_form_data():
            self.close()
