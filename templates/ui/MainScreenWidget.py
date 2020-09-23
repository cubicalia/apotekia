import sys
from PyQt5.QtCore    import Qt, QRect
from PyQt5.QtGui     import QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
                             QVBoxLayout, QTabWidget, QFileDialog, QPlainTextEdit, QHBoxLayout, QLabel)

from templates.ui.ObjSearchWidget import ObjectSearchWidget

lineBarColor       = QColor(53, 53, 53)
lineHighlightColor = QColor('#00FF04')


class TabWidget(QTabWidget):

    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)

    # This virtual handler is called after a tab was removed from position index.
    def tabRemoved(self, index):
        print("\n tab was removed from position index -> {}".format(index))

    # This virtual handler is called after a new tab was added or inserted at position index.
    def tabInserted(self, index):
        print("\n New tab was added or inserted at position index -> {}".format(index))


class Content(QWidget):
    def __init__(self, text):
        super(Content, self).__init__()
        self.editor = ObjectSearchWidget()
        # self.editor.setPlainText(text)
        # Create a layout for the line numbers
        self.hbox = QHBoxLayout(self)
        # self.numbers = NumberBar(self.editor)
        # self.hbox.addWidget(self.numbers)
        self.hbox.addWidget(self.editor)


class NumberBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.editor = parent
        layout      = QVBoxLayout(self)
        self.editor.blockCountChanged.connect(self.update_width)
        self.editor.updateRequest.connect(self.update_on_scroll)
        self.update_width('001')

    def mousePressEvent(self, QMouseEvent):
        print("\n - class NumberBar(QWidget): \n\tdef mousePressEvent(self, QMouseEvent):")

    def update_on_scroll(self, rect, scroll):
        if self.isVisible():
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update()

    def update_width(self, string):
        width = self.fontMetrics().width(str(string)) + 10
        if self.width() != width:
            self.setFixedWidth(width)

    def paintEvent(self, event):
        if self.isVisible():
            block   = self.editor.firstVisibleBlock()
            height  = self.fontMetrics().height()
            number  = block.blockNumber()
            painter = QPainter(self)
            painter.fillRect(event.rect(), lineBarColor)
            painter.setPen(Qt.white)
            painter.drawRect(0, 0, event.rect().width() - 1, event.rect().height() - 1)
            font = painter.font()

            current_block = self.editor.textCursor().block().blockNumber() + 1

            while block.isValid():
                block_geometry = self.editor.blockBoundingGeometry(block)
                offset = self.editor.contentOffset()
                block_top = block_geometry.translated(offset).top()
                number += 1

                rect = QRect(0, block_top, self.width() - 5, height)

                if number == current_block:
                    font.setBold(True)
                else:
                    font.setBold(False)

                painter.setFont(font)
                painter.drawText(rect, Qt.AlignRight, '%i' % number)

                if block_top > event.rect().bottom():
                    break

                block = block.next()

            painter.end()


class ModuleMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel('Modules widget')

        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class MyTableWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout(self)
        # Initialize tab screen
        self.module_menu = ModuleMenu()
        self.tabs = TabWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        # Add tabs to widget
        self.layout.addWidget(self.module_menu)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def closeTab(self, index):
        tab = self.tabs.widget(index)
        tab.deleteLater()
        self.tabs.removeTab(index)

    def addTab(self, content, fileName):
        self.tabs.addTab(Content(str(content)), str(fileName))