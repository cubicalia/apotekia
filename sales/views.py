from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from apotekia import db_setup

from PyQt5.QtWidgets import QWidget, QDialog
from sales.sales_ui.BasketsDialog import Ui_BasketDialog
from sales.sales_ui.SalesDialog import Ui_SalesDialog
from sales.models import Basket, Sale


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


class SalesDialog(QDialog):
    def __init__(self, parent=None):
        super(SalesDialog, self).__init__(parent)

        self.sales = Sale.objects.all()
        self.sale_fields = ['Id', 'Customer', 'Date', 'Total TTC']
        self.sale_model = QStandardItemModel(len(self.sales), 4)
        self.sale_model.setHorizontalHeaderLabels(self.sale_fields)
        self.sale_filter_proxy_model = QSortFilterProxyModel()
        self.sale_filter_proxy_model.setSourceModel(self.sale_model)

        self.ui = Ui_SalesDialog()
        self.ui.setupUi(self)

        self.populate_sale_list()
        self.selected_basket = ""

    def populate_sale_list(self):
        self.populate_sale_model()

        self.sale_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.sale_filter_proxy_model.setFilterKeyColumn(0)
        self.ui.lineEdit.textChanged.connect(self.sale_filter_proxy_model.setFilterRegExp)
        self.ui.tableView.setModel(self.sale_filter_proxy_model)

        # TODO: Set multiple column filter for the model

    def populate_sale_model(self):
        for row, sale in enumerate(self.sales):
            pid = QStandardItem(str(sale.id))
            customer = QStandardItem(str(sale.basket.customer.get_full_name()))
            date = QStandardItem(str(sale.date_created))
            total = QStandardItem(str(000))
            self.basket_model.setItem(row, 0, pid)
            self.basket_model.setItem(row, 1, customer)
            self.basket_model.setItem(row, 2, date)
            self.basket_model.setItem(row, 3, total)

    def convert_sale_to_invoice(self):
        pass

    def convert_sale_to_order(self):
        pass

    def delete_sale(self):
        pass



