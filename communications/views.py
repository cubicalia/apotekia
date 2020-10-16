from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QDialog
from communications.communications_ui.RequiredFieldsDialog import Ui_FieldsRequiredDialog
from django.shortcuts import render


class RequiredFieldDialog(QDialog):
    def __init__(self, check_list):
        super(RequiredFieldDialog, self).__init__()
        """
        This Dialog shows the list of non filled required fields in a form
        """

        self.check_list = check_list

        self.ui = Ui_FieldsRequiredDialog()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.errorList.setModel(self.model)

        for field in self.check_list:
            item = QStandardItem(field.capitalize())
            self.model.appendRow(item)

        self.ui.pushButton.clicked.connect(self.close)
