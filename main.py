import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from templates.ui.MainScreenWidget import CentralWidget

from customers.views import CustomerSearchDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        self.statusBar()
        self.resize(1200, 800)
        self.central = CentralWidget()
        self.setCentralWidget(self.central)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())