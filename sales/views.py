from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel

from apotekia import db_setup

from PyQt5.QtWidgets import QWidget, QDialog
from sales.sales_ui.SalesWidget import Ui_SalesWidget
from sales.models import Basket


class SalesDialog(QDialog):
    def __init__(self):
        super(SalesDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_SalesWidget()
        self.ui.setupUi(self)


    def show_baskets(self):
        basket_fields = ['Id', 'Customer', 'Date', 'Total TTC']
        basket_objects = Basket.objects.all()
        basket_model = QStandardItemModel(len(basket_objects), 4)
        basket_model.setHorizontalHeaderLabels(basket_fields)
        basket_filter_proxy_model = QSortFilterProxyModel()
        basket_filter_proxy_model.setSourceModel(basket_model)
        selected_basket = ""
