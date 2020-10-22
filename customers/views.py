from apotekia import db_setup

from PyQt5.QtCore import Qt, pyqtSlot, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from templates.ui.CustomerSearch import Ui_CustomerSearchWidget
from customers.customers_ui.CustomerWidget import Ui_CustomerWidget
from.models import Customer


class CustomerSearchDialog(QWidget):
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
        # for row in self.product_data:
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
        for item in selected.indexes():
            if item:
                self.ui.CustomerSelectionLabel.setText(item.product_data())
                self.selected = item.product_data()
                print(self.selected)


class CustomerDialog(QDialog):
    def __init__(self):
        super(CustomerDialog, self).__init__()

        self.all_customers = Customer.objects.all()
        self.customer_fields = ['Id', 'Name', 'CIN']
        self.customers_model = QStandardItemModel(len(self.all_customers), 3)
        self.customers_model.setHorizontalHeaderLabels(self.customer_fields)

        self.customers_filter_proxy_model = QSortFilterProxyModel()
        self.customers_filter_proxy_model.setSourceModel(self.customers_model)
        self.selected_customer = ""

        self.ui = Ui_CustomerWidget()
        self.ui.setupUi(self)

        self.ui.lineEdit.textChanged.connect(self.customers_filter_proxy_model.setFilterRegExp)
        self.ui.CustomersList.setModel(self.customers_filter_proxy_model)

        self.populate_customers_list()

    def populate_customers_list(self):
        self.populate_customer_model()

        self.customers_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.customers_filter_proxy_model.setFilterKeyColumn(1)

        self.ui.lineEdit.textChanged.connect(self.customers_filter_proxy_model.setFilterRegExp)
        self.ui.CustomersList.setModel(self.customers_filter_proxy_model)

        selection_model = self.ui.CustomersList.selectionModel()
        selection_model.selectionChanged.connect(self.on_customer_selectionChanged)

    def populate_customer_model(self):
        for row, customer in enumerate(self.all_customers):
            pid = QStandardItem(str(customer.id))
            name = QStandardItem(str(customer.get_full_name()))
            id_number = QStandardItem(str(customer.id_number))
            # code = QStandardItem(str(customer.code))

            self.customers_model.setItem(row, 0, pid)
            self.customers_model.setItem(row, 1, name)
            self.customers_model.setItem(row, 2, id_number)
            # self.product_model.setItem(row, 3, code)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_customer_selectionChanged(self, selected):
        item = selected.indexes()
        if item:
            pid = self.selected_customer = item[0].data()
            self.selected_customer = Customer.objects.get(pk=pid)
            self.populate_customer_info(self.selected_customer)

    def populate_customer_info(self, customer):
        # GENERAL INFO
        self.ui.label_32.setText(customer.salutation)
        self.ui.label_33.setText(customer.address.__str__())

        # INVOICING INFO
        self.ui.label_7.setText(customer.get_full_name())

        # SALES INFO
        self.ui.label_17.setText(customer.salutation)
        self.ui.label_18.setText(customer.address.__str__())
