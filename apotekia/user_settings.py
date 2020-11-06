import pickle

from PyQt5.QtWidgets import QWidget, QDialog, QWizard

from apotekia.settings_ui.EstablishmentInfo import Ui_EstablishmentWidget
from apotekia.settings_ui.EstablishmentSetupWizard import Ui_EstablishmentSetupWizard
from communications.views import RequiredFieldDialog, MessageDialog


class EstablishmentInfoWidget(QDialog):
    def __init__(self, parent=None):
        super(EstablishmentInfoWidget, self).__init__(parent)

        self.ui = Ui_EstablishmentWidget()
        self.ui.setupUi(self)
        self.populate_data()

        self.ui.pushButton.clicked.connect(self.establishment_setup)

    def populate_data(self):
        self.data = None
        with (open("establishment.pickle", "rb")) as openfile:
            while True:
                try:
                    self.data = pickle.load(openfile)
                except EOFError:
                    break
        self.ui.label_12.setText(self.data['Establishment_data']['Name'])
        self.ui.label_13.setText(self.data['Establishment_data']['Address_line_1'])
        self.ui.label_14.setText(self.data['Establishment_data']['Address_line_2'])
        self.ui.label_15.setText(self.data['Establishment_data']['CP'])
        self.ui.label_16.setText(self.data['Establishment_data']['City'])
        self.ui.label_17.setText(self.data['Establishment_data']['Country'])
        self.ui.label_18.setText(self.data['Establishment_data']['Currency'])
        self.ui.label_19.setText(self.data['Establishment_data']['Phone'])
        self.ui.label_20.setText(self.data['Establishment_data']['Fax'])
        self.ui.label_21.setText(self.data['Establishment_data']['Email'])
        self.ui.label_22.setText(self.data['Establishment_data']['Website'])
        # self.ui.label_24.setText(self.data['Establishment_data']['Logo'])
        self.ui.label_35.setText(self.data['Accounting_data']['CEO'])
        self.ui.label_33.setText(self.data['Accounting_data']['Capital'])
        self.ui.label_34.setText(self.data['Accounting_data']['Type'])
        self.ui.label_29.setText(self.data['Accounting_data']['ICE'])
        self.ui.label_30.setText(self.data['Accounting_data']['RC'])
        self.ui.label_25.setText(self.data['Accounting_data']['Patente'])
        self.ui.label_32.setText(self.data['Accounting_data']['IF'])
        self.ui.label_31.setText(self.data['Accounting_data']['CNSS'])
        self.ui.label_26.setText(self.data['Accounting_data']['TVA'])
        self.ui.label_28.setText(self.data['Accounting_data']['Objets'])

    def establishment_setup(self):
        dialog = EstablishmentEditWizard()
        dialog.exec_()
        dialog.show()


class EstablishmentEditWizard(QWizard):
    def __init__(self, parent=None):
        super(EstablishmentEditWizard, self).__init__(parent)

        self.ui = Ui_EstablishmentSetupWizard()
        self.ui.setupUi(self)
        self.finish_button = self.button(self.FinishButton)
        self.finish_button.disconnect()
        self.checklist = []
        self.data_dict = {'Establishment_data': {},
                          'Accounting_data': {}}
        self.finish_button.clicked.connect(self.is_valid_form)

    def is_valid_form(self):
        self.checklist.clear()

        if self.ui.lineEdit.text() == '':
            self.checklist.append(self.ui.label_11.text())
        if self.ui.lineEdit_2.text() == '':
            self.checklist.append(self.ui.label_20.text())
        if self.ui.lineEdit_5.text() == '':
            self.checklist.append(self.ui.label_16.text())
        if self.ui.lineEdit_6.text() == '':
            self.checklist.append(self.ui.label_7.text())
        if self.ui.lineEdit_7.text() == '':
            self.checklist.append(self.ui.label_19.text())
        if self.ui.lineEdit_8.text() == '':
            self.checklist.append(self.ui.label_13.text())
        if self.ui.lineEdit_10.text() == '':
            self.checklist.append(self.ui.label_12.text())
        if self.ui.lineEdit_12.text() == '':
            self.checklist.append(self.ui.label_38.text())
        if self.ui.lineEdit_15.text() == '':
            self.checklist.append(self.ui.label_39.text())

        if len(self.checklist) == 0:
            self.save_data()
        else:
            self.show_required_fields()

    def save_data(self):
        # Establishment Info
        self.data_dict['Establishment_data']['Name'] = self.ui.lineEdit.text()
        self.data_dict['Establishment_data']['Address_line_1'] = self.ui.lineEdit_2.text()
        self.data_dict['Establishment_data']['Address_line_2'] = self.ui.lineEdit_3.text()
        self.data_dict['Establishment_data']['CP'] = self.ui.lineEdit_4.text()
        self.data_dict['Establishment_data']['City'] = self.ui.lineEdit_5.text()
        self.data_dict['Establishment_data']['Country'] = self.ui.lineEdit_6.text()
        self.data_dict['Establishment_data']['Currency'] = self.ui.lineEdit_7.text()
        self.data_dict['Establishment_data']['Phone'] = self.ui.lineEdit_8.text()
        self.data_dict['Establishment_data']['Fax'] = self.ui.lineEdit_9.text()
        self.data_dict['Establishment_data']['Email'] = self.ui.lineEdit_10.text()
        self.data_dict['Establishment_data']['Website'] = self.ui.lineEdit_11.text()
        # TODO: Save the logo image in the static folder

        # Accounting Info
        self.data_dict['Accounting_data']['CEO'] = self.ui.lineEdit_12.text()
        self.data_dict['Accounting_data']['Capital'] = self.ui.lineEdit_13.text()
        self.data_dict['Accounting_data']['Type'] = self.ui.lineEdit_14.text()
        self.data_dict['Accounting_data']['ICE'] = self.ui.lineEdit_15.text()
        self.data_dict['Accounting_data']['RC'] = self.ui.lineEdit_16.text()
        self.data_dict['Accounting_data']['Patente'] = self.ui.lineEdit_17.text()
        self.data_dict['Accounting_data']['IF'] = self.ui.lineEdit_18.text()
        self.data_dict['Accounting_data']['CNSS'] = self.ui.lineEdit_19.text()
        self.data_dict['Accounting_data']['TVA'] = self.ui.lineEdit_20.text()
        self.data_dict['Accounting_data']['Objets'] = self.ui.textEdit.toPlainText()

        with open('establishment.pickle', 'wb') as f:
            pickle.dump(self.data_dict, f)

        self.close()

    def show_required_fields(self):
        dialog = RequiredFieldDialog(self.checklist)
        dialog.exec_()
        dialog.show()