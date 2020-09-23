from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QListWidget, QPushButton)


class FooterButtons(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.add_button = QPushButton('Add entry')
        self.edit_button = QPushButton('Edit entry')
        self.delete_button = QPushButton('Delete entry')

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def open_action(self):
        pass

    def edit_action(self):
        pass

    def delete_action(self):
        pass


class ListResultsWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setAlternatingRowColors(True)
        self.load_data()

    def load_data(self):
        data = ['item{}'.format(i) for i in range(30)]
        for i in data:
            self.addItem(i)


class ObjectSearchWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.search_field = QLineEdit()
        self.list_resuls = ListResultsWidget()
        self.buttons_footer = FooterButtons()

        self.layout.addWidget(self.search_field)
        self.layout.addWidget(self.list_resuls)
        self.layout.addWidget(self.buttons_footer)

        self.setLayout(self.layout)

