# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductDialog(object):
    def setupUi(self, ProductDialog):
        ProductDialog.setObjectName("ProductDialog")
        ProductDialog.resize(1185, 840)
        self.gridLayout = QtWidgets.QGridLayout(ProductDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(ProductDialog)
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.AddCategoryButton = QtWidgets.QPushButton(self.groupBox_3)
        self.AddCategoryButton.setObjectName("AddCategoryButton")
        self.gridLayout_3.addWidget(self.AddCategoryButton, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.CategoriestreeWidget = QtWidgets.QTreeWidget(self.groupBox_3)
        self.CategoriestreeWidget.setObjectName("CategoriestreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.CategoriestreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.CategoriestreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.CategoriestreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.CategoriestreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.gridLayout_3.addWidget(self.CategoriestreeWidget, 1, 0, 1, 1)
        self.RemoveCategoryButton = QtWidgets.QPushButton(self.groupBox_3)
        self.RemoveCategoryButton.setObjectName("RemoveCategoryButton")
        self.gridLayout_3.addWidget(self.RemoveCategoryButton, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 2, 1)
        self.ProductStockGroupBox = QtWidgets.QGroupBox(ProductDialog)
        self.ProductStockGroupBox.setObjectName("ProductStockGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ProductStockGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.ProductStockGroupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 7, 1, 1, 1)
        self.gridLayout.addWidget(self.ProductStockGroupBox, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(ProductDialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 4, 0, 1, 1)
        self.PurchasePriceResult = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PurchasePriceResult.setFont(font)
        self.PurchasePriceResult.setObjectName("PurchasePriceResult")
        self.gridLayout_5.addWidget(self.PurchasePriceResult, 4, 1, 1, 1)
        self.SellingPriceResult = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SellingPriceResult.setFont(font)
        self.SellingPriceResult.setObjectName("SellingPriceResult")
        self.gridLayout_5.addWidget(self.SellingPriceResult, 5, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 5, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 4, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 7, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 7, 1, 1, 1)
        self.ImageLabel = QtWidgets.QGraphicsView(self.groupBox_2)
        self.ImageLabel.setMaximumSize(QtCore.QSize(250, 250))
        self.ImageLabel.setObjectName("ImageLabel")
        self.gridLayout_5.addWidget(self.ImageLabel, 1, 2, 1, 1)
        self.editProductButton = QtWidgets.QPushButton(self.groupBox_2)
        self.editProductButton.setObjectName("editProductButton")
        self.gridLayout_5.addWidget(self.editProductButton, 8, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 8, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_5.addWidget(self.pushButton_8, 8, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 6, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 5, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 6, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 6, 2, 1, 1)
        self.ImageLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.ImageLabel_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ImageLabel_2.setObjectName("ImageLabel_2")
        self.gridLayout_5.addWidget(self.ImageLabel_2, 0, 2, 1, 1)
        self.CategoryLabel = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CategoryLabel.setFont(font)
        self.CategoryLabel.setObjectName("CategoryLabel")
        self.gridLayout_5.addWidget(self.CategoryLabel, 3, 0, 1, 1)
        self.ProductTitle = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ProductTitle.setFont(font)
        self.ProductTitle.setTextFormat(QtCore.Qt.AutoText)
        self.ProductTitle.setScaledContents(False)
        self.ProductTitle.setWordWrap(False)
        self.ProductTitle.setObjectName("ProductTitle")
        self.gridLayout_5.addWidget(self.ProductTitle, 1, 0, 1, 2)
        self.CategoryResult = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CategoryResult.setFont(font)
        self.CategoryResult.setObjectName("CategoryResult")
        self.gridLayout_5.addWidget(self.CategoryResult, 3, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(ProductDialog)
        self.groupBox.setMaximumSize(QtCore.QSize(50000, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ProductsListTable = QtWidgets.QTableView(self.groupBox)
        self.ProductsListTable.setObjectName("ProductsListTable")
        self.gridLayout_2.addWidget(self.ProductsListTable, 2, 1, 1, 3)
        self.SearchByNameradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.SearchByNameradioButton.setChecked(True)
        self.SearchByNameradioButton.setObjectName("SearchByNameradioButton")
        self.gridLayout_2.addWidget(self.SearchByNameradioButton, 1, 1, 1, 1)
        self.SearchByBarcodeRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.SearchByBarcodeRadioButton.setObjectName("SearchByBarcodeRadioButton")
        self.gridLayout_2.addWidget(self.SearchByBarcodeRadioButton, 1, 2, 1, 1)
        self.ProductSearchArea = QtWidgets.QLineEdit(self.groupBox)
        self.ProductSearchArea.setObjectName("ProductSearchArea")
        self.gridLayout_2.addWidget(self.ProductSearchArea, 0, 1, 1, 3)
        self.RemoveProductButton = QtWidgets.QPushButton(self.groupBox)
        self.RemoveProductButton.setObjectName("RemoveProductButton")
        self.gridLayout_2.addWidget(self.RemoveProductButton, 3, 3, 1, 1)
        self.addProductButon = QtWidgets.QPushButton(self.groupBox)
        self.addProductButon.setObjectName("addProductButon")
        self.gridLayout_2.addWidget(self.addProductButon, 3, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 2, 1)

        self.retranslateUi(ProductDialog)
        QtCore.QMetaObject.connectSlotsByName(ProductDialog)

    def retranslateUi(self, ProductDialog):
        _translate = QtCore.QCoreApplication.translate
        ProductDialog.setWindowTitle(_translate("ProductDialog", "Form"))
        self.groupBox_3.setTitle(_translate("ProductDialog", "Categories"))
        self.AddCategoryButton.setText(_translate("ProductDialog", "Add Category"))
        self.lineEdit_2.setPlaceholderText(_translate("ProductDialog", "Search Category"))
        self.CategoriestreeWidget.headerItem().setText(0, _translate("ProductDialog", "Categories"))
        __sortingEnabled = self.CategoriestreeWidget.isSortingEnabled()
        self.CategoriestreeWidget.setSortingEnabled(False)
        self.CategoriestreeWidget.topLevelItem(0).setText(0, _translate("ProductDialog", "New Item"))
        self.CategoriestreeWidget.topLevelItem(1).setText(0, _translate("ProductDialog", "Parapharmacie"))
        self.CategoriestreeWidget.topLevelItem(2).setText(0, _translate("ProductDialog", "Urologie"))
        self.CategoriestreeWidget.topLevelItem(3).setText(0, _translate("ProductDialog", "Medicaments"))
        self.CategoriestreeWidget.topLevelItem(3).child(0).setText(0, _translate("ProductDialog", "Antibiotiques"))
        self.CategoriestreeWidget.topLevelItem(3).child(0).child(0).setText(0, _translate("ProductDialog", "New Subitem"))
        self.CategoriestreeWidget.setSortingEnabled(__sortingEnabled)
        self.RemoveCategoryButton.setText(_translate("ProductDialog", "Remove Category"))
        self.ProductStockGroupBox.setTitle(_translate("ProductDialog", "Product Stock Detail"))
        self.label_11.setText(_translate("ProductDialog", "TextLabel"))
        self.label_10.setText(_translate("ProductDialog", "TextLabel"))
        self.label_4.setText(_translate("ProductDialog", "TextLabel"))
        self.label_5.setText(_translate("ProductDialog", "TextLabel"))
        self.label_3.setText(_translate("ProductDialog", "TextLabel"))
        self.label_12.setText(_translate("ProductDialog", "TextLabel"))
        self.label_7.setText(_translate("ProductDialog", "TextLabel"))
        self.label_6.setText(_translate("ProductDialog", "TextLabel"))
        self.label_8.setText(_translate("ProductDialog", "TextLabel"))
        self.label_9.setText(_translate("ProductDialog", "TextLabel"))
        self.label_13.setText(_translate("ProductDialog", "TextLabel"))
        self.label_2.setText(_translate("ProductDialog", "TextLabel"))
        self.label_14.setText(_translate("ProductDialog", "TextLabel"))
        self.label_15.setText(_translate("ProductDialog", "TextLabel"))
        self.groupBox_2.setTitle(_translate("ProductDialog", "Product Info"))
        self.label_16.setText(_translate("ProductDialog", "TextLabel"))
        self.label_25.setText(_translate("ProductDialog", "PPH"))
        self.PurchasePriceResult.setText(_translate("ProductDialog", "58.7 Dh"))
        self.SellingPriceResult.setText(_translate("ProductDialog", "75 Dh"))
        self.label_24.setText(_translate("ProductDialog", "TextLabel"))
        self.label_27.setText(_translate("ProductDialog", "TextLabel"))
        self.label_18.setText(_translate("ProductDialog", "TextLabel"))
        self.label_17.setText(_translate("ProductDialog", "TextLabel"))
        self.editProductButton.setText(_translate("ProductDialog", "Edit Product"))
        self.pushButton_9.setText(_translate("ProductDialog", "VIew Sales"))
        self.pushButton_8.setText(_translate("ProductDialog", "More details ..."))
        self.label_19.setText(_translate("ProductDialog", "TextLabel"))
        self.label_22.setText(_translate("ProductDialog", "PPV"))
        self.label_20.setText(_translate("ProductDialog", "TextLabel"))
        self.label_21.setText(_translate("ProductDialog", "TextLabel"))
        self.ImageLabel_2.setText(_translate("ProductDialog", "Image"))
        self.CategoryLabel.setText(_translate("ProductDialog", "Category:"))
        self.ProductTitle.setText(_translate("ProductDialog", "ALFAMOX 500mg:\n"
"Amoxiciln"))
        self.CategoryResult.setText(_translate("ProductDialog", "Category --> Medicine  --> Antibiotic"))
        self.groupBox.setTitle(_translate("ProductDialog", "Products"))
        self.SearchByNameradioButton.setText(_translate("ProductDialog", "By name"))
        self.SearchByBarcodeRadioButton.setText(_translate("ProductDialog", "Barcode"))
        self.ProductSearchArea.setPlaceholderText(_translate("ProductDialog", "Search Product"))
        self.RemoveProductButton.setText(_translate("ProductDialog", "Remove Product"))
        self.addProductButon.setText(_translate("ProductDialog", "Add Product"))
