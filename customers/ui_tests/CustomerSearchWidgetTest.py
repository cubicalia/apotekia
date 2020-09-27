from apotekia import db_setup
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from templates.ui.CustomerSearch import Ui_CustomerSearchWidget

from customers.models import Customer


class CustomerSearchDialog(QDialog):
    def __init__(self):
        super(CustomerSearchDialog, self).__init__()

        # Set up the user interface from Designer.


        self.fields = []
        self.data = Customer.objects.all()
        self.model = QStandardItemModel(len(self.data), 1)
        self.model.setHorizontalHeaderLabels(['Customer'])
        self.populate_model()

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        self.ui = Ui_CustomerSearchWidget()
        self.ui.setupUi(self)
        self.ui.CustomerSearchField.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.ui.CustomerResultsTable.setModel(self.filter_proxy_model)

        # Connect up the buttons.
        self.ui.CustomerViewButton.clicked.connect(self.get_field_values)

        selection_model = self.ui.CustomerResultsTable.selectionModel()
        selection_model.selectionChanged.connect(self.on_selectionChanged)

        self.selected = ""

    def populate_model_fields(self):
        # for row in self.data:
        #     print(row)

        fields = Customer._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<'):
                self.fields.append(str(field.name))

    def get_field_values(self):
        customer_dicts = Customer.objects.values()
        for customer in customer_dicts:
            print(customer)

    def populate_model(self):
        for row, customer in enumerate(self.data):
            print(str(customer))
            item = QStandardItem(str(customer))
            self.model.setItem(row, 0, item)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_selectionChanged(self, selected):
        print("selected: ")
        for item in selected.indexes():
            if item:
                self.ui.CustomerSelectionLabel.setText(item.data())
                self.selected = item.data()
                print(self.selected)


app = QApplication(sys.argv)
window = CustomerSearchDialog()
# ui = CustomerSearchDialog()
# ui.setupUi(window)

window.show()
sys.exit(app.exec_())