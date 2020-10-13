import sys

from PyQt5.QtGui import QStandardItemModel

from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QHBoxLayout, QTableWidget

from inventory.models import InventoryLocation


class InventoryDialog(QDialog):
    def __init__(self):
        super(InventoryDialog, self).__init__()
        self.setGeometry(400, 100, 500, 500)

        self.locations = InventoryLocation.objects.all()
        self.model = QStandardItemModel(len(self.locations), 1)
        self.model.setHorizontalHeaderLabels(['Location'])

        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.table = QTableWidget()

        self.table.setRowCount(10)
        self.table.setColumnCount(1)

        for row, item in enumerate(range(10)):
            self.table.setItem(row, 0, QTableWidgetItem(str(item)))

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = InventoryDialog()
    mainWin.show()
    sys.exit(app.exec_())