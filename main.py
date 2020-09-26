import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from templates.ui.MainScreenWidget import MyTableWidget, Content

from customers.views import CustomerSearchDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        self.statusBar()
        self.addMenu()
        self.resize(800, 600)
        self.tabs = MyTableWidget()
        self.setCentralWidget(self.tabs)

    def addMenu(self):
        menu = self.menuBar()

        # FILE MENU
        fileMenu = menu.addMenu('File')

        self.newSaleAction = QAction('New sale...', self)
        self.newSaleAction.setShortcut('Ctrl+N')
        self.newSaleAction.setStatusTip('Crete a new sale')
        fileMenu.addAction(self.newSaleAction)

        self.openAct = QAction('Open...', self)
        self.openAct.setShortcut('Ctrl+O')
        self.openAct.setStatusTip('Open a file')
        self.is_opened = False
        self.openAct.triggered.connect(self.openFile)
        fileMenu.addAction(self.openAct)

        # EDIT MENU
        edit_menu = menu.addMenu('Edit')
        edit_menu.addAction('Copy')

        # VIEW MENU
        view_menu = menu.addMenu('View')
        view_menu.addAction('Dashboard')

        # PHARMACY MENU
        pharmacy_menu = menu.addMenu('Pharmacy')
        pharmacy_menu.addAction('My Profile')

    def closeTab(self, index):
        tab = self.tabs.widget(index)
        tab.deleteLater()
        self.tabs.removeTab(index)

    def buttonClicked(self):
        self.tabs.addTab(Content("smalltext2"), "sadsad")

    def openFile(self):
        options = QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(
            self, 'Open a file', '',
            'Python Files (*.py);;Text Files (*.txt)',
            options=options
        )
        if filenames:
            for filename in filenames:
                with open(filename, 'r+') as file_o:
                    try:
                        text = file_o.read()
                        self.tabs.addTab(text, filename)
                    except Exception as e:
                        print("Error: filename=`{}`, `{}` ".format(filename, str(e)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())