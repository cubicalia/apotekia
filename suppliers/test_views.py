from PyQt5.QtGui import QFont

from apotekia import db_setup
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QWidget, QFormLayout, QLabel, QLineEdit, \
    QSpinBox
from suppliers.models import Supplier


class SupplierEntryFOrmWidget(QWidget):
    def __init__(self, model):
        super(SupplierEntryFOrmWidget, self).__init__()
        self.model = model
        self.layout = QFormLayout()
        self.initUI()

    # def initUI(self):
    #     nameLineEdit = QLineEdit()
    #     nameLabel = QLabel(self.tr("&Name:"))
    #     nameLabel.setBuddy(nameLineEdit)
    #
    #     emailLineEdit = QLineEdit()
    #     emailLabel = QLabel(self.tr("&Name:"))
    #     emailLabel.setBuddy(emailLineEdit)
    #
    #     ageSpinBox = QSpinBox()
    #     ageLabel = QLabel(self.tr("&Name:"))
    #     ageLabel.setBuddy(ageSpinBox)
    #
    #     self.layout = QFormLayout()
    #     self.layout.addRow(self.tr("&Name:"), nameLineEdit)
    #     self.layout.addRow(self.tr("&Email:"), emailLineEdit)
    #     self.layout.addRow(self.tr("&Age:"), ageSpinBox)
    #     self.setLayout(self.layout)

    def initUI(self):
        fields = self.model._meta.get_fields(include_parents=False)
        for field in fields:
            if not str(field).startswith('<') and not 'AutoField' in str(type(field)):
                field_name = str(field).split('.')[-1]
                label = QLabel(self.tr(field_name.capitalize()))
                label.setFont(QFont('Arial', 16))
                line_edit = QLineEdit()
                line_edit.setMinimumHeight(30)
                self.layout.addRow(label, line_edit)
                print(type(field))
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        self.statusBar()
        # self.resize(1200, 800)
        self.central = SupplierEntryFOrmWidget(Supplier())
        self.setCentralWidget(self.central)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
