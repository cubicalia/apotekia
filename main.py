import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QAction, QFileDialog, \
    QPlainTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from templates.ui.MainScreenWidget import MyTableWidget, Content


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.open()
        self.tabs = MyTableWidget()
        self.setCentralWidget(self.tabs)
        self.initUI()
        self.show()

    def initUI(self):
        self.statusBar()
        self.addMenu()
        self.resize(800, 600)

    def addMenu(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('File')
        fileMenu.addAction(self.openAct)

    def closeTab(self, index):
        tab = self.tabs.widget(index)
        tab.deleteLater()
        self.tabs.removeTab(index)

    def buttonClicked(self):
        self.tabs.addTab(Content("smalltext2"), "sadsad")

    def open(self):
        self.openAct = QAction('Open...', self)
        self.openAct.setShortcut('Ctrl+O')
        self.openAct.setStatusTip('Open a file')
        self.is_opened = False
        self.openAct.triggered.connect(self.openFile)

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