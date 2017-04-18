from PyQt5.QtWidgets import QTabWidget

from ui.editor import TextEdit

class TabWidget(QTabWidget):

    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.setup()

    def setup(self):
        self.addTab(TextEdit("", self), "temp1.txt")
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setTabShape(QTabWidget.Triangular)
