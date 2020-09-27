from apotekia import db_setup
import sys

from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from templates.ui.ProductSearch import Ui_ProductSearchWidget

from catalog.models import Product


class ProductSearchDialog(QWidget):
    def __init__(self):
        super(ProductSearchDialog, self).__init__()
        self.setMinimumHeight(400)
        # Set up the user interface from Designer.

        self.fields = []
        self.data = Product.objects.all()
        self.model = QStandardItemModel(len(self.data), 1)
        self.model.setHorizontalHeaderLabels(['Product'])
        self.populate_model()

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        self.ui = Ui_ProductSearchWidget()
        self.ui.setupUi(self)
        self.ui.SearchField.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.ui.ResultsTable.setModel(self.filter_proxy_model)

        # Connect up the buttons.
        self.ui.SelectionButton.clicked.connect(self.get_field_values)

        selection_model = self.ui.ResultsTable.selectionModel()
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
                self.ui.SelectionLabel.setText(item.data())
                self.selected = item.data()
                print(self.selected)
