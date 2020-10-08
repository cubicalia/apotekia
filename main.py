from apotekia import db_setup
import sys

from PyQt5.QtCore import QSortFilterProxyModel, Qt, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow

from catalog.models import Product
from customers.models import Customer

from pos.pos_ui.PointOfSale import Ui_MainWindow
from inventory.views import InventoryDialog
from catalog.views import ProductDialog
from banking.views import BankingDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.fields = []
        # Products Data Init
        self.product_data = Product.objects.all()
        self.product_dicts = Product.objects.values()
        self.product_model = QStandardItemModel(len(self.product_data), 1)
        self.product_filter_proxy_model = QSortFilterProxyModel()
        self.product_filter_proxy_model.setSourceModel(self.product_model)
        self.selected_product = ""

        # Customers Data Init
        self.customer_data = Customer.objects.all()
        self.customer_dicts = Customer.objects.values()
        self.customer_model = QStandardItemModel(len(self.customer_data), 1)
        self.customer_filter_proxy_model = QSortFilterProxyModel()
        self.customer_filter_proxy_model.setSourceModel(self.customer_model)
        self.selected_customer = ""

        self.setupUi(self)
        self.initiate_module_menu()
        self.populate_products_list()
        self.populate_customers_list()

    """
    Initiating The Modules Left Vertical Menu
    """

    def initiate_module_menu(self):
        self.pushButton_2.clicked.connect(self.open_catalog_dialog)
        self.pushButton_3.clicked.connect(self.open_inventory_dialog)
        self.pushButton_7.clicked.connect(self.open_banking_dialog)

    def open_inventory_dialog(self):
        dialog = InventoryDialog()
        dialog.exec_()
        dialog.show()

    def open_catalog_dialog(self):
        dialog = ProductDialog()
        dialog.exec_()
        dialog.show()

    def open_banking_dialog(self):
        dialog = BankingDialog()
        dialog.exec_()
        dialog.show()

    '''
    Products Search and Filters
    '''

    def populate_products_list(self):
        self.fields = []
        self.product_model.setHorizontalHeaderLabels(['Product'])
        self.populate_product_model()

        self.product_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.product_filter_proxy_model.setFilterKeyColumn(0)

        self.lineEdit.textChanged.connect(self.product_filter_proxy_model.setFilterRegExp)
        self.tableView_2.setModel(self.product_filter_proxy_model)

        # Connect up the buttons.
        self.pushButton_28.clicked.connect(self.get_product_field_values)

        selection_model = self.tableView_2.selectionModel()
        selection_model.selectionChanged.connect(self.on_product_selectionChanged)

    def populate_model_fields(self):
        fields = Product._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<'):
                self.fields.append(str(field.name))

    def get_product_field_values(self):
        for product in self.product_dicts:
            print(product)

    def populate_product_model(self):
        for row, product in enumerate(self.product_data):
            print(str(product))
            item = QStandardItem(str(product))
            self.product_model.setItem(row, 0, item)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_product_selectionChanged(self, selected):
        print("selected: ")
        for item in selected.indexes():
            if item:
                self.label_2.setText(item.data())
                self.selected_product = item.data()
                print(self.selected_product)

    """
    Customers Search and Filters
    """

    def populate_customers_list(self):
        # Set up the user interface from Designer.
        self.fields = []

        self.populate_customer_model()
        self.customer_model.setHorizontalHeaderLabels(['Customer'])

        self.customer_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.customer_filter_proxy_model.setFilterKeyColumn(0)

        self.lineEdit_2.textChanged.connect(self.customer_filter_proxy_model.setFilterRegExp)
        self.tableView_3.setModel(self.customer_filter_proxy_model)

        # Connect up the buttons.
        self.pushButton_30.clicked.connect(self.get_customer_field_values)

        selection_model = self.tableView_3.selectionModel()
        selection_model.selectionChanged.connect(self.on_customer_selectionChanged)

    def populate_customer_model_fields(self):
        # for row in self.product_data:
        #     print(row)

        fields = Customer._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<'):
                self.fields.append(str(field.name))

    def get_customer_field_values(self):
        for customer in self.customer_dicts:
            print(customer)

    def populate_customer_model(self):
        for row, customer in enumerate(self.customer_data):
            print(str(customer))
            item = QStandardItem(str(customer))
            self.customer_model.setItem(row, 0, item)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_customer_selectionChanged(self, selected):
        for item in selected.indexes():
            if item:
                self.label_4.setText(item.data())
                self.selected_customer = item.data()
                print(self.selected_customer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())