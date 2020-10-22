from decimal import Decimal as D
from PyQt5.QtWidgets import QDialog, QWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from templates.ui.ProductSearch import Ui_ProductSearchWidget
from catalog.products_ui.ProductsWidget import Ui_ProductDialog
from catalog.products_ui.AddProductDialog import Ui_AddProductDialog

from communications.views import RequiredFieldDialog

from catalog.models import Product, ProductCategory
from apotekia.settings import DEFAULT_CURRENCY


class ProductDialog(QDialog):
    def __init__(self):
        super(ProductDialog, self).__init__()

        """CATEGORIES"""
        self.category_data = ProductCategory.objects.all()

        """PRODUCTS"""
        self.product_fields = ['Id', 'Product', 'PPH', 'TVA', 'PPV', 'Barcode']
        self.product_data = Product.objects.all()
        self.product_model = QStandardItemModel(len(self.product_data), 6)
        self.product_model.setHorizontalHeaderLabels(self.product_fields)
        self.product_filter_proxy_model = QSortFilterProxyModel()
        self.product_filter_proxy_model.setSourceModel(self.product_model)
        self.selected_product = ""

        self.ui = Ui_ProductDialog()
        self.ui.setupUi(self)

        self.ui.ProductSearchArea.textChanged.connect(self.product_filter_proxy_model.setFilterRegExp)
        self.ui.CategoriestreeWidget.selectionModel().selectionChanged.connect(self.get_selected_category)
        self.ui.ProductsListTable.setModel(self.product_filter_proxy_model)
        self.ui.addProductButon.clicked.connect(self.add_product)

        # POPULATE DATA
        self.populate_categories()
        self.populate_products_list()
        self.selected_product = ''

    def populate_categories(self):
        tree = self.ui.CategoriestreeWidget
        categories = []
        for item in self.category_data:
            list_object_parent_widget = [item, item.parent, QTreeWidgetItem([item.name])]
            categories.append(list_object_parent_widget)

        try:
            for item in categories:
                if item[1] is None:
                    tree.addTopLevelItem(item[2])
                    for re_item in categories:
                        if re_item[0].parent == item[0]:
                            item[2].addChild(re_item[2])
                            for rd in categories:
                                if rd[0].parent == re_item[0]:
                                    re_item[2].addChild(rd[2])
        except KeyError:
            # TODO: Make this more recurrent to dig deeper than 3 layers of categories
            print('Max levels reached')

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def get_selected_category(self, selected):
        category_name = selected.indexes()[0].data()
        category = ProductCategory.objects.get(name=category_name)
        self.product_data = Product.objects.filter(category=category)
        # TODO: Make this filter include the results of the child categories
        self.product_model = QStandardItemModel(len(self.product_data), 6)
        self.product_filter_proxy_model.setSourceModel(self.product_model)
        self.populate_products_list()

    def populate_products_list(self):
        self.populate_product_model()

        self.product_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.product_filter_proxy_model.setFilterKeyColumn(1)

        self.ui.ProductSearchArea.textChanged.connect(self.product_filter_proxy_model.setFilterRegExp)
        self.ui.ProductsListTable.setModel(self.product_filter_proxy_model)

        selection_model = self.ui.ProductsListTable.selectionModel()
        selection_model.selectionChanged.connect(self.on_product_selectionChanged)

    def populate_product_model(self):
        for row, product in enumerate(self.product_data):
            pid = QStandardItem(str(product.id))
            title = QStandardItem(str(product.title))
            purchase_price_incl_tax = QStandardItem(str(product.purchase_price))
            vat = QStandardItem(str(int(product.tax_rate)) + ' %')
            ttc = float(product.selling_price)
            # TODO: Fix the above calculations for prices, allow only two decimals
            price_ttc = QStandardItem(str(ttc))
            barcode = QStandardItem(str(product.upc))
            self.product_model.setItem(row, 0, pid)
            self.product_model.setItem(row, 1, title)
            self.product_model.setItem(row, 2, purchase_price_incl_tax)
            self.product_model.setItem(row, 3, vat)
            self.product_model.setItem(row, 4, price_ttc)
            self.product_model.setItem(row, 5, barcode)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_product_selectionChanged(self, selected):
        item = selected.indexes()
        if item:
            self.ui.ProductTitle.setText(item[1].data())
            pid = self.selected_product = item[0].data()
            self.selected_product = Product.objects.get(pk=pid)
            self.populate_product_info(self.selected_product)

    def populate_product_info(self, product):
        self.ui.ProductTitle.setText(product.title)
        self.ui.CategoryResult.setText(product.category.__str__())
        self.ui.PurchasePriceResult.setText(str(product.purchase_price) + ' ' + DEFAULT_CURRENCY)
        self.ui.SellingPriceResult.setText(str(product.selling_price) + ' ' + DEFAULT_CURRENCY)
        self.ui.label_20.setText(str(product.tax_rate) + '%')

    def add_product(self):
        dialog = AddProductDialog()
        dialog.exec_()
        dialog.show()

    def refresh_all(self):
        self.product_model.clear()
        self.populate_products_list()


class AddProductDialog(QDialog):
    def __init__(self):
        super(AddProductDialog, self).__init__()

        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Add Product')

        self.populate_category_combo_box()

        # self.ui.pushButton_2.clicked.connect(self.validate_data_dict)

        self.ui.pushButton_2.clicked.connect(self.validate_data_dict)

    def populate_category_combo_box(self):
        categories = ProductCategory.objects.all()
        display_list = [str(category.id) + '|' + category.__str__() for category in categories]
        self.ui.comboBox.addItems(display_list)

    def get_data_dict(self):
        """
        This function gets the data in the ADD PRODUCT FORM and stores it in a dictionary.
        The value of the dictionary is a list of the value and a boolean that informs if the
        field is required.
        :return:
        Dictionary in the form of { 'field': ['value', boolean]
        """

        data_dict = {}
        # General data
        data_dict['title'] = [self.ui.lineEdit.text(), True]
        data_dict['track_stock'] = [self.ui.checkBox.checkState(), False]
        data_dict['UPC_1'] = [self.ui.lineEdit_4.text(), False]
        data_dict['UPC_2'] = [self.ui.lineEdit_6.text(), False]
        data_dict['purchase_price_ET'] = [D(self.ui.doubleSpinBox.text()), False]
        data_dict['selling_price_ET'] = [D(self.ui.doubleSpinBox_2.text()), False]
        data_dict['tax_rate'] = [D(self.ui.doubleSpinBox_3.text()), False]
        data_dict['category'] = [int(self.ui.comboBox.currentText().split('|')[0]), False]

        # Pharmaceutical data
        data_dict['dci'] = [self.ui.refLineEdit_2.text(), True]
        data_dict['manufacturer'] = [self.ui.refLineEdit_3.text(), False]
        data_dict['th'] = [self.ui.therapeuticClassLineEdit.text(), True]
        data_dict['refundable'] = [self.ui.refundableCheckBox.checkState(), False]
        data_dict['refundable_amount'] = [D(self.ui.doubleSpinBox_4.text()), False]
        data_dict['prescription'] = [self.ui.checkBox_2.checkState(), False]
        data_dict['pharma_form'] = [self.ui.lineEdit_2.text(), True]
        data_dict['tableau'] = [self.ui.lineEdit_3.text(), False]

        # Shipping data
        data_dict['width'] = [D(self.ui.widthDoubleSpinBox.text()), False]
        data_dict['length'] = [D(self.ui.widthDoubleSpinBox_3.text()), False]
        data_dict['height'] = [D(self.ui.widthDoubleSpinBox_2.text()), False]
        data_dict['net_weight'] = [D(self.ui.widthDoubleSpinBox_4.text()), False]
        data_dict['gross_weight'] = [D(self.ui.widthDoubleSpinBox_5.text()), False]

        return data_dict

    def validate_data_dict(self):
        product_dict = self.get_data_dict()
        required_fields = []
        for key in product_dict:
            if product_dict[key][1] and len(product_dict[key][0]) == 0:
                required_fields.append(key)
        print(len(required_fields))
        if len(required_fields) != 0:
            self.show_required_fields(required_fields)
        else:
            print('Data is valid')
            self.submit_data()

    def show_required_fields(self, required_fields):
        dialog = RequiredFieldDialog(required_fields)
        dialog.exec_()
        dialog.show()

    def submit_data(self):
        data_dict = self.get_data_dict()
        product = Product(title=data_dict['title'][0],
                          track_stock=True if data_dict['track_stock'][0] == 2 else False,
                          upc=data_dict['UPC_1'][0],
                          upc_2=data_dict['UPC_2'][0],
                          purchase_price=float(data_dict['purchase_price_ET'][0]),
                          selling_price=float(data_dict['selling_price_ET'][0]),
                          tax_rate=float(data_dict['tax_rate'][0]),
                          category=ProductCategory.objects.get(pk=data_dict['category'][0]),
                          dci=data_dict['dci'][0],
                          lab=data_dict['manufacturer'][0],
                          th_class=data_dict['th'][0],
                          refundable=True if data_dict['refundable'][0] == 2 else False,
                          prescription=True if data_dict['prescription'][0] == 2 else False,
                          pharma_form=data_dict['pharma_form'][0],
                          tableau=data_dict['tableau'][0]
                          )
        product.save()
        self.close()
