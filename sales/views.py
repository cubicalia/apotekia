from PyQt5.QtCore import QSortFilterProxyModel, Qt, pyqtSlot, QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from apotekia import db_setup

from PyQt5.QtWidgets import QWidget, QDialog, QWizard

from customers.models import Customer
from sales.sales_ui.BasketsDialog import Ui_BasketDialog
from sales.sales_ui.SalesDialog import Ui_SalesDialog
from sales.sales_ui.SaleDetailView import Ui_SaleDetailView
from sales.sales_ui.OrdersDialog import Ui_OrdersDialog
from sales.sales_ui.NewOrderWizard import Ui_NewOrderWizard
from payment.models import PaymentSource, PaymentConditions, Payment
from sales.models import Basket, Sale, CustomerOrder, CustomerOrderLine
from apotekia.settings import CUSTOMER_ORDER_PREFIX


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
            date = QStandardItem(str(basket.date_created.strftime('%d/%m/%Y %H:%M:%S')))
            total = QStandardItem(str(000))
            self.basket_model.setItem(row, 0, pid)
            self.basket_model.setItem(row, 1, date)
            self.basket_model.setItem(row, 2, total)

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

        self.sales = Sale.objects.all().order_by('-date_created')
        self.sale_fields = ['Id', 'Customer', 'Date', 'Total TTC', 'Status']
        self.sale_model = QStandardItemModel(len(self.sales), len(self.sale_fields))
        self.sale_model.setHorizontalHeaderLabels(self.sale_fields)
        self.sale_filter_proxy_model = QSortFilterProxyModel()
        self.sale_filter_proxy_model.setSourceModel(self.sale_model)

        self.ui = Ui_SalesDialog()
        self.ui.setupUi(self)

        self.populate_sale_list()
        self.ui.tableView.selectionModel().selectionChanged.connect(self.get_selected_sale)
        self.selected_sale = None
        self.ui.pushButton_3.clicked.connect(self.new_order)
        self.ui.pushButton_7.clicked.connect(self.show_sale_detail_view)

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
            customer = QStandardItem(str(sale.customer.get_full_name()))
            date = QStandardItem(str(sale.date_created.strftime('%d/%m/%Y %H:%M:%S')))
            total = QStandardItem(str(float(sale.basket.basket_total())))
            status = QStandardItem(str(sale.status))
            self.sale_model.setItem(row, 0, pid)
            self.sale_model.setItem(row, 1, customer)
            self.sale_model.setItem(row, 2, date)
            self.sale_model.setItem(row, 3, total)
            self.sale_model.setItem(row, 4, status)

    def convert_sale_to_invoice(self):
        pass

    def convert_sale_to_order(self):
        pass

    def delete_sale(self):
        pass

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def get_selected_sale(self, selected):
        sale_id = int(selected.indexes()[0].data())
        self.selected_sale = Sale.objects.get(id=sale_id)

    def show_sale_detail_view(self):
        print(type(self.selected_sale))
        if self.selected_sale is not None:
            dialog = SaleDetailView(self.selected_sale)
            dialog.exec_()
            dialog.show()

    def new_order(self):
        wizard = NewOrderWizard()
        wizard.exec_()
        wizard.show()


class SaleDetailView(QDialog):
    def __init__(self, sale):
        super().__init__()
        self.sale = sale
        self.basket_lines = self.sale.basket.lines.all()

        self.basket_fields = ['Id', 'Product', 'Qty', 'TVA', 'PPV', 'Total']
        self.basket_model = QStandardItemModel(len(self.basket_lines), 6)
        self.basket_model.setHorizontalHeaderLabels(self.basket_fields)

        self.ui = Ui_SaleDetailView()
        self.ui.setupUi(self)

        self.ui.label_16.setText(self.sale.customer.get_full_name())
        self.ui.label_21.setText(str(self.sale.payment.source))
        self.ui.label_22.setText(self.sale.reference)
        self.ui.label_23.setText(str(self.sale.payment.amount))

        self.populate_basket_lines()

    def populate_basket_lines(self):
        for row, basket_line in enumerate(self.basket_lines):
            pid = QStandardItem(str(basket_line.id))
            product = QStandardItem(str(basket_line.product))
            quantity = QStandardItem(str(basket_line.quantity))
            vat = QStandardItem(str(basket_line.product.tax_rate))
            ttc = QStandardItem(str(float(basket_line.price_incl_tax)))
            total = QStandardItem(str(float(basket_line.line_total())))

            self.basket_model.setItem(row, 0, pid)
            self.basket_model.setItem(row, 1, product)
            self.basket_model.setItem(row, 2, quantity)
            self.basket_model.setItem(row, 3, vat)
            self.basket_model.setItem(row, 4, ttc)
            self.basket_model.setItem(row, 5, total)

        self.ui.tableView.setModel(self.basket_model)


class OrdersDialog(QDialog):
    def __init__(self, parent=None):
        super(OrdersDialog, self).__init__(parent)

        self.orders_data = CustomerOrder.objects.all().order_by('-date_placed')
        self.order_fields = ['Id', 'Customer', 'Date', 'Total TTC', 'Status']
        self.order_model = QStandardItemModel(len(self.orders_data), len(self.order_fields))

        self.ui = Ui_OrdersDialog()
        self.ui.setupUi(self)


class NewOrderWizard(QWizard):
    def __init__(self, parent=None):
        super(NewOrderWizard, self).__init__(parent)

        self.ui = Ui_NewOrderWizard()
        self.ui.setupUi(self)

        # Customer Search
        self.selected_customer = None
        self.init_customer_selection()

        # Date pick
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit_2.setDate(QDate.currentDate())
        self.ui.pushButton.clicked.connect(self.set_order_date_today)
        self.ui.pushButton_2.clicked.connect(self.set_expedition_date_today)

        self.order_date = self.ui.dateEdit.date().toPyDate()
        self.expedition_date = self.ui.dateEdit_2.date().toPyDate()

        # Payment
        self.populate_payment_methods()

    def init_customer_selection(self):
        self.customer_fields = ['ID', 'Name', "CIN/ICE"]
        self.customer_data = Customer.objects.all()
        self.customer_model = QStandardItemModel(len(self.customer_data), len(self.customer_fields))
        self.customer_model.setHorizontalHeaderLabels(self.customer_fields)

        self.customer_filter_proxy_model = QSortFilterProxyModel()
        self.customer_filter_proxy_model.setSourceModel(self.customer_model)
        self.customer_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.customer_filter_proxy_model.setFilterKeyColumn(1)

        # Customer Ui Connections
        self.ui.lineEdit.textChanged.connect(self.customer_filter_proxy_model.setFilterRegExp)
        self.ui.tableView_2.setModel(self.customer_filter_proxy_model)

        selection_model = self.ui.tableView_2.selectionModel()
        selection_model.selectionChanged.connect(self.on_customer_selectionChanged)
        self.populate_customer_model()

    def populate_customer_model(self):
        for row, customer in enumerate(self.customer_data):
            pid = QStandardItem(str(customer.id))
            name = QStandardItem(str(customer.get_full_name()))
            CIN = QStandardItem(str(customer.id_number))
            self.customer_model.setItem(row, 0, pid)
            self.customer_model.setItem(row, 1, name)
            self.customer_model.setItem(row, 2, CIN)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_customer_selectionChanged(self, selected):
        item = selected.indexes()
        if item:
            pid = item[0].data()
            self.selected_customer = Customer.objects.get(pk=pid)
            self.populate_customer_info(self.selected_customer)

    def populate_customer_info(self, customer):
        self.ui.label_66.setText(customer.get_full_name())
        if customer.address:
            self.ui.label_67.setText(customer.address.summary)
        else:
            self.ui.label_67.setText('Customer has no specified address')

    def set_order_date_today(self):
        self.ui.dateEdit.setDate(QDate.currentDate())

    def set_expedition_date_today(self):
        self.ui.dateEdit_2.setDate(QDate.currentDate())

    def populate_payment_methods(self):
        methods = PaymentSource.objects.all()
        for method in methods:
            self.ui.comboBox_4.addItem(method.name)
