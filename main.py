import sys
from django.utils import timezone

from PyQt5.QtCore import QSortFilterProxyModel, Qt, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow

from inventory.utils import find_product_locations

from catalog.models import Product
from customers.models import Customer
from inventory.models import InventoryEntry
from sales.models import Basket, BasketLine, Sale
from payment.models import Transaction, PaymentSourceType, PaymentSource
from django.contrib.auth.models import User

from pos.pos_ui.PointOfSale import Ui_MainWindow
from inventory.views import InventoryDialog
from catalog.views import ProductDialog
from customers.views import CustomerDialog
from banking.views import BankingDialog
from sales.views import BasketDialog, SalesDialog, OrdersDialog
from communications.views import MessageDialog

from apotekia import settings


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Products Data Init
        self.product_fields = []
        self.product_data = Product.objects.all()
        self.product_model = QStandardItemModel(len(self.product_data), 7)
        self.product_model.setHorizontalHeaderLabels(['Id', 'Product', 'TVA', 'Price TTC', 'In stock', 'Barcode'])
        self.product_filter_proxy_model = QSortFilterProxyModel()
        self.product_filter_proxy_model.setSourceModel(self.product_model)
        self.selected_product = ""

        # Customers Data Init
        self.customer_fields = []
        self.customer_data = Customer.objects.all()
        self.customer_dicts = Customer.objects.values()
        self.customer_model = QStandardItemModel(len(self.customer_data), 2)
        self.customer_filter_proxy_model = QSortFilterProxyModel()
        self.customer_filter_proxy_model.setSourceModel(self.customer_model)
        self.selected_customer = ''

        # Basket Data
        self.products_in_basket = {}
        self.basket_model = QStandardItemModel(len(self.products_in_basket.keys()), 4)

        self.client_for_basket = ''
        self.payment_source_types = PaymentSourceType.objects.all()

        self.total_basket = 0.00


        self.setupUi(self)
        self.initiate_module_menu()
        self.showMaximized()

        self.populate_products_list()
        self.populate_customers_list()
        for item in self.payment_source_types:
            self.comboBox.addItem(item.name)
        self.pushButton_10.clicked.connect(self.remove_item_from_basket)
        self.pushButton_11.clicked.connect(self.clear_basket)
        self.SubmitSaleButton.clicked.connect(self.submit_basket)
        self.SaveForLaterButton.clicked.connect(self.save_basket)
        self.refreshButton.clicked.connect(self.refresh_all)
        self.pushButton_3.clicked.connect(self.open_baskets_dialog)
        self.pushButton_13.clicked.connect(self.open_orders_dialog)

        self.initiate_basket_view()

    """
    Initiating The Modules Left Vertical Menu
    """

    def initiate_module_menu(self):
        self.pushButton_2.clicked.connect(self.open_catalog_dialog)
        self.pushButton_3.clicked.connect(self.open_inventory_dialog)
        self.pushButton_7.clicked.connect(self.open_banking_dialog)
        self.pushButton_8.clicked.connect(self.open_customer_dialog)
        self.pushButton_5.clicked.connect(self.open_baskets_dialog)
        self.pushButton_12.clicked.connect(self.open_sales_dialog)

    def open_inventory_dialog(self):
        dialog = InventoryDialog()
        dialog.exec_()
        dialog.show()

    def open_catalog_dialog(self):
        dialog = ProductDialog()
        dialog.exec_()
        dialog.show()

    def open_customer_dialog(self):
        dialog = CustomerDialog()
        dialog.exec_()
        dialog.show()

    def open_banking_dialog(self):
        dialog = BankingDialog()
        dialog.exec_()
        dialog.show()

    def open_baskets_dialog(self):
        dialog = BasketDialog()
        dialog.exec_()
        dialog.show()

    def open_sales_dialog(self):
        dialog = SalesDialog()
        dialog.exec_()
        dialog.show()

    def open_orders_dialog(self):
        dialog = OrdersDialog()
        dialog.exec_()
        dialog.show()

    '''
    Products Search and Filters
    '''

    def populate_products_list(self):
        self.populate_product_model()

        self.product_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.product_filter_proxy_model.setFilterKeyColumn(5)

        self.lineEdit.textChanged.connect(self.product_filter_proxy_model.setFilterRegExp)
        self.tableView_2.setModel(self.product_filter_proxy_model)

        self.pushButton_29.clicked.connect(self.add_product_to_basket)

        selection_model = self.tableView_2.selectionModel()
        selection_model.selectionChanged.connect(self.on_product_selectionChanged)

    def populate_product_model_fields(self):
        fields = Product._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<'):
                self.product_fields.append(str(field.name))

    def populate_product_model(self):
        for row, product in enumerate(self.product_data):
            # print(str(product))
            id = QStandardItem(str(product.id))
            title = QStandardItem(str(product.title))
            vat = QStandardItem(str(int(product.tax_rate)) + ' %')
            ttc = float(product.selling_price)
            # TODO: Fix the above calculations for prices, allow only two decimals
            price_ttc = QStandardItem(str(ttc))
            barcode = QStandardItem(str(product.upc))
            self.product_model.setItem(row, 0, id)
            self.product_model.setItem(row, 1, title)
            self.product_model.setItem(row, 2, vat)
            self.product_model.setItem(row, 3, price_ttc)
            self.product_model.setItem(row, 5, barcode)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_product_selectionChanged(self, selected):
        try:
            item = selected.indexes()[0]
            name = selected.indexes()[1]
            if item:
                self.label_2.setText(name.data())
                self.selected_product = item.data()
        except IndexError as e:
            self.label_2.setText('PRODUCT NOT FOUND')
            pass

    """
    Customers Search and Filters
    """

    def populate_customers_list(self):
        # Set up the user interface from Designer.
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
        fields = Customer._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<'):
                self.customer_fields.append(str(field.name))

    def get_customer_field_values(self):
        for customer in self.customer_dicts:
            print(customer)

    def populate_customer_model(self):
        for row, customer in enumerate(self.customer_data):
            id = QStandardItem(str(customer.id))
            item = QStandardItem(str(customer))
            self.customer_model.setItem(row, 0, item)
            self.customer_model.setItem(row, 1, id)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_customer_selectionChanged(self, selected):
        item = selected.indexes()
        if item:
            self.label_4.setText(item[0].data())
            self.selected_customer = item[1].data()
            print(self.selected_customer)

    def clear_customer(self):
        self.selected_customer = ''
        self.customer_model.clear()

    """
    Basket & Total Values
    """

    def initiate_basket_view(self):
        self.BasketTableView.setModel(self.basket_model)
        self.basket_model.setHorizontalHeaderLabels(['Product',
                                                     'Quantity',
                                                     'Unit Price HT',
                                                     'Unit Price TTC',
                                                     'Total Price',
                                                     'PID'])
        self.BasketTableView.hideColumn(5)

    def populate_basket(self):
        for key, value in enumerate(self.products_in_basket):
            product = Product.objects.get(id=value)
            title = QStandardItem(str(product.title))
            quantity = QStandardItem(str(self.products_in_basket[value]))
            price_ht = QStandardItem(str(product.selling_price))
            price = str(product.selling_price * (100 + product.tax_rate) / 100)
            view_price = QStandardItem(price)
            total = product.selling_price * (100 + product.tax_rate) / 100 * self.products_in_basket[value]
            view_total = QStandardItem(str(total))
            pid = QStandardItem(str(value))

            self.basket_model.setItem(int(key), 0, title)
            self.basket_model.setItem(int(key), 1, quantity)
            self.basket_model.setItem(int(key), 2, price_ht)
            self.basket_model.setItem(int(key), 3, view_price)
            self.basket_model.setItem(int(key), 4, view_total)
            self.basket_model.setItem(int(key), 5, pid)

        self.BasketTableView.hideColumn(5)

    def refresh_basket_view(self):
        self.populate_basket()
        self.sum_Basket_total()

    def sum_Basket_total(self):
        model = self.BasketTableView.model()
        data = []
        totals_products = []
        totals_TTC = []
        totals_HT = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data[row].append(str(model.data(index)))
        for row in data:
            totals_products.append(int(row[1]))
            totals_HT.append(float(row[2]) * int(row[1]))
            totals_TTC.append(float(row[4]))

        total_items = sum(totals_products)
        total_HT = sum(totals_HT)
        total = sum(totals_TTC)
        self.label_6.setText(str(total_items))
        self.label_24.setText(str("{:.2f}".format(total)) + ' ' + settings.DEFAULT_CURRENCY)
        self.label_25.setText(str("{:.2f}".format(total_HT)))
        self.TotlaLCDDisplay.setDigitCount(10)
        self.TotlaLCDDisplay.display(str("{:.2f}".format(total)))
        self.TotlaLCDDisplay.repaint()
        self.total_basket = total

    def add_product_to_basket(self):
        if self.selected_product not in self.products_in_basket.keys():
            if self.selected_product != '':
                self.products_in_basket[self.selected_product] = 1
            else:
                print('nothing selected')
        else:
            self.products_in_basket[self.selected_product] += 1

        self.refresh_basket_view()

    def clear_basket(self):
        self.products_in_basket = {}
        self.basket_model.clear()
        self.refresh_basket_view()
        self.initiate_basket_view()

    def remove_item_from_basket(self):
        indices = self.BasketTableView.selectionModel().selectedRows(5)
        for index in indices:
            pid = index.data()
            del self.products_in_basket[pid]
            self.basket_model.removeRow(index.row())
            self.refresh_basket_view()

    def clear_all(self):
        self.clear_basket()
        self.clear_customer()
        self.populate_customer_model()
        self.refresh_basket_view()

    def save_basket(self):
        # Variables
        status = Sale.STATUS_CHOICES[2]  # Open status for saved baskets
        date_saved = timezone.now()

        # Employee association
        employee = User.objects.get(pk=1)  # TODO:Manage the logged in user to match the current employee

        # Customer association
        if self.selected_customer is not '':
            customer = Customer.objects.get(pk=int(self.selected_customer))
            basket = Basket(employee=employee, customer=customer, status=status, date_submitted=date_saved)
        else:
            name = 'Anonymous'  # TODO: Make Anonymous a single client
            anonymous_customer, created = Customer.objects.get_or_create(first_name=name)
            basket = Basket(employee=employee, customer=anonymous_customer, status=status, date_submitted=date_saved)
            basket.save()

        basket.save()
        print('BASKET {} SAVED'.format(basket.id))
        # Saving the basket lines
        lines_dict = self.products_in_basket
        for line in lines_dict:
            product = Product.objects.get(pk=int(line))
            quantity = lines_dict[line]
            price_excl_tax = product.selling_price
            price_incl_tax = float(product.selling_price) + (
                        float(product.selling_price) * float(product.tax_rate)) / 100

            basket_line = BasketLine(basket=basket,
                                     product=product,
                                     quantity=quantity,
                                     price_excl_tax=price_excl_tax,
                                     price_incl_tax=price_incl_tax)
            basket_line.save()
        """
        After saving a Basket or submitting one, we need to clean the basket and create a new one
        """
        self.clear_all()

    def submit_basket(self):
        # Selecting the customer
        customer_id = 1
        if self.selected_customer is not '':
            customer_id = int(self.selected_customer)
        else:
            print('Please select a customer')

        customer = Customer.objects.get(pk=customer_id)

        # Selecting the employee
        employee = User.objects.get(pk=1) # TODO: Modify this after implementing the login

        # Creating the basket
        date_submitted = timezone.now()
        basket = Basket(date_submitted=date_submitted)
        basket.save()

        # Creating the basket lines
        lines_dict = self.products_in_basket
        for line in lines_dict:
            product = Product.objects.get(pk=int(line))
            quantity = lines_dict[line]
            price_excl_tax = product.selling_price
            price_incl_tax = float(product.selling_price) + (
                    float(product.selling_price) * float(product.tax_rate)) / 100
            # TODO: This line has to be fed from the Basket Table,
            #  as user can modify prices at checkout
            basket_line = BasketLine(basket=basket,
                                     product=product,
                                     quantity=quantity,
                                     price_excl_tax=price_excl_tax,
                                     price_incl_tax=price_incl_tax)
            basket_line.save()

        # Selecting the payment
        payment_source_type_text = self.comboBox.currentText()
        payment_source_type = PaymentSourceType.objects.get(name=payment_source_type_text)
        payment_source_reference = self.PaymentReferenceField.text()
        payment_source = PaymentSource(reference=payment_source_reference,
                                       source_type=payment_source_type)
        payment_source.save()

        payment = Transaction(source=payment_source,
                              amount=self.total_basket)
        payment.save()

        sale = Sale(basket=basket,
                    employee=employee,
                    payment=payment,
                    customer=customer)
        # TODO: Need to add Inventory Entries after submitting a sale

        sale.save()

        msg = MessageDialog('The sale has been submitted')
        msg.exec_()
        msg.show()

        self.clear_all()

    def refresh_all(self):
        self.product_model.clear()
        self.clear_all()
        self.populate_products_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


""" To run migrations within our code"""
# call_command("makemigrations", interactive=False)
# call_command("migrate", interactive=False)
