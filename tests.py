import sys

from PyQt5.QtWidgets import QDialog, QApplication
from templates.ui.CustomerSearch import Ui_CustomerSearchWidget


class CustomerSearchDialog(QDialog):
    def __init__(self):
        super(CustomerSearchDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_CustomerSearchWidget()
        self.ui.setupUi(self)

        # Connect up the buttons.
        # self.ui.okButton.clicked.connect(self.accept)
        # self.ui.cancelButton.clicked.connect(self.reject)


app = QApplication(sys.argv)
window = CustomerSearchDialog()
# ui = CustomerSearchDialog()
# ui.setupUi(window)

window.show()
sys.exit(app.exec_())