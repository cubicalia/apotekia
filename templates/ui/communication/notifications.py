from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QListWidget, QPushButton, QMessageBox)


class AlertBox(QMessageBox):
    def __init__(self, message, parent=None):
        super().__init__(parent)

        self.message = message
        self.initUI()
        retval = self.exec_()

    def initUI(self):
        self.setText(self.message)
        self.setInformativeText("This is additional information")
        self.setWindowTitle("MessageBox demo")
        self.setDetailedText("The details are as follows:")
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.buttonClicked.connect(self.msgbtn)

    def msgbtn(self, i):
        print("Button pressed is:", i.text())


class NotificationBox(QMessageBox):
    pass
