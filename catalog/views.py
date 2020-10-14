from PyQt5.QtWidgets import QDialog, QWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from templates.ui.ProductSearch import Ui_ProductSearchWidget
from catalog.products_ui.ProductsWidget import Ui_ProductDialog

from catalog.models import Product, ProductCategory
from apotekia.settings import DEFAULT_CURRENCY


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
        # for row in self.product_data:
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
                self.ui.SelectionLabel.setText(item.product_data())
                self.selected = item.product_data()
                print(self.selected)


class ProductDialog(QDialog):
    def __init__(self):
        super(ProductDialog, self).__init__()

        """CATEGORIES"""
        self.category_data = ProductCategory.objects.all()

        """PRODUCTS"""
        self.product_fields = []
        self.product_data = Product.objects.all()
        self.product_model = QStandardItemModel(len(self.product_data), 6)
        self.product_model.setHorizontalHeaderLabels(['Id', 'Product', 'PPH', 'TVA', 'PPV', 'Barcode'])
        self.product_filter_proxy_model = QSortFilterProxyModel()
        self.product_filter_proxy_model.setSourceModel(self.product_model)
        self.selected_product = ""

        self.ui = Ui_ProductDialog()
        self.ui.setupUi(self)

        self.ui.ProductSearchArea.textChanged.connect(self.product_filter_proxy_model.setFilterRegExp)
        self.ui.CategoriestreeWidget.selectionModel().selectionChanged.connect(self.get_selected_category)
        self.ui.ProductsListTable.setModel(self.product_filter_proxy_model)

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
        self.ui.SellingPriceResult.setText(str(product.selling_price)+ ' ' + DEFAULT_CURRENCY)
        self.ui.label_20.setText(str(product.tax_rate) + '%')


class AddProductDialog(QDialog):
    def __init__(self):
        super(AddProductDialog, self).__init__()

