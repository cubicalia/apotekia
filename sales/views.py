from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from apotekia import db_setup

from PyQt5.QtWidgets import QWidget, QDialog
from sales.sales_ui.BasketsDialog import Ui_BasketDialog
from sales.models import Basket


class BasketDialog(QDialog):
    def __init__(self):
        super(BasketDialog, self).__init__()

        self.basket_data = Basket.objects.all()
        self.basket_fields = ['Id', 'Customer', 'Date', 'Total TTC']
        self.basket_model = QStandardItemModel(len(self.basket_data), 4)
        self.basket_model.setHorizontalHeaderLabels(self.basket_fields)
        self.basket_filter_proxy_model = QSortFilterProxyModel()
        self.basket_filter_proxy_model.setSourceModel(self.basket_model)

        self.ui = Ui_BasketDialog()
        self.ui.setupUi(self)

        self.populate_basket_list()
        self.selected_basket = ""

    def populate_basket_list(self):
        self.populate_baskets_model()

        self.basket_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.basket_filter_proxy_model.setFilterKeyColumn(0)
        self.ui.lineEdit.textChanged.connect(self.basket_filter_proxy_model.setFilterRegExp)
        self.ui.tableView.setModel(self.basket_filter_proxy_model)

        # TODO: Set multiple column filter for the model

    def populate_baskets_model(self):
        for row, basket in enumerate(self.basket_data):
            pid = QStandardItem(str(basket.id))
            customer = QStandardItem(str(basket.customer.get_full_name()))
            date = QStandardItem(str(basket.date_created))
            total = QStandardItem(str(000))
            self.basket_model.setItem(row, 0, pid)
            self.basket_model.setItem(row, 1, customer)
            self.basket_model.setItem(row, 2, date)
            self.basket_model.setItem(row, 3, total)

    def delete_basket(self):
        pass

    def convert_basket_to_sale(self):
        pass

    def convert_basket_to_proforma(self):
        pass

    def convert_basket_to_order(self):
        pass

    def convert_basket_to_invoice(self):
        pass

