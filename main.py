from apotekia import db_setup
import sys

from PyQt5.QtCore import QSortFilterProxyModel, Qt, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog

from catalog.models import Product
from pos.pos_ui.PointOfSale import Ui_MainWindow
from inventory.views import InventoryDialog
from catalog.views import ProductDialog
from banking.views import BankingDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.fields = []

        self.setupUi(self)
        self.initiate_module_menu()
        self.populate_products_list()

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
        self.data = Product.objects.all()
        self.model = QStandardItemModel(len(self.data), 1)
        self.model.setHorizontalHeaderLabels(['Product'])
        self.populate_model()

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        self.lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.tableView_2.setModel(self.filter_proxy_model)

        # Connect up the buttons.
        self.pushButton_28.clicked.connect(self.get_field_values)

        selection_model = self.tableView_2.selectionModel()
        selection_model.selectionChanged.connect(self.on_selectionChanged)

        self.selected = ""

    def populate_model_fields(self):
        # for row in self.data:
        #     print(row)

        fields = Product._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<'):
                self.fields.append(str(field.name))

    def get_field_values(self):
        customer_dicts = Product.objects.values()
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
                self.label_2.setText(item.data())
                self.selected = item.data()
                print(self.selected)

    """
    Customers Search and Filters
    """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())