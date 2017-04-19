from PyQt5.QtWidgets import QTabWidget

from ui.editor import TextEdit

class TabWidget(QTabWidget):
    """ Class to handle functionality for the TabWidget """

    def __init__(self, parent=None):
        """ Constructor that takes a parent widget as an optional parameter """
        super(TabWidget, self).__init__(parent)
        self.init_ui()

    def on_tab_closing(self, index):
        """ Function to handle when a tab is closed """
        if index >= 0:
            self.removeTab(index)
        else:
            raise IndexError
        pass

    def init_ui(self):
        """ Some initial settings for the TabWidget """
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setTabShape(QTabWidget.Triangular)
        self.tabCloseRequested.connect(lambda: self.on_tab_closing(self.currentIndex()))
