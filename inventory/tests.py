import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem

from inventory.models import InventoryLocation, InventoryEntry
from inventory.inventory_ui.InventoryWidget import Ui_StockWidget


class InventoryDialog(QDialog):
    def __init__(self):
        super(InventoryDialog, self).__init__()
        self.locations = InventoryLocation.objects.all()
        self.model = QStandardItemModel(len(self.locations), 1)
        self.model.setHorizontalHeaderLabels(['Location'])
        self.show_locations()
        self.initUI()

    def initUI(self):
        self.ui = Ui_StockWidget()
        self.ui.setupUi(self)
        self.ui.StockLocationList.setModel(self.model)
        self.selection_model = self.ui.StockLocationList.selectionModel()
        self.selection_model.selectionChanged.connect(self.on_selectionChanged)

    def show_movements(self, selected_location):
        self.ui.StockMovementsTable.clearContents()
        self.entries = InventoryEntry.objects.filter(location__name=selected_location)
        self.ui.StockMovementsTable.setRowCount(len(self.entries))
        for row, entry in enumerate(self.entries):
            self.ui.StockMovementsTable.setItem(row, 0, QTableWidgetItem(str(entry.id)))
            self.ui.StockMovementsTable.setItem(row, 1, QTableWidgetItem(entry.date.strftime("%Y-%m-%d %H:%M:%S")))
            self.ui.StockMovementsTable.setItem(row, 2, QTableWidgetItem(str(entry.product)))
            self.ui.StockMovementsTable.setItem(row, 7, QTableWidgetItem(str(entry.qty)))

    def show_locations(self):
        for row, location in enumerate(self.locations):
            # print(str(location))
            item = QStandardItem(str(location))
            self.model.setItem(row, 0, item)

    @pyqtSlot('QItemSelection', 'QItemSelection')
    def on_selectionChanged(self, selected):
        for item in selected.indexes():
            if item:
                self.ui.label_13.setText(item.product_data())
                self.selected = item.product_data()
                self.ui.StockMovementsTable.update()
                self.show_movements(item.product_data())
                print(item.product_data())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = InventoryDialog()
    mainWin.show()
    sys.exit(app.exec_())