from PyQt5.QtWidgets import QTabWidget

from ui.editor import TextEdit

class TabWidget(QTabWidget):
    """ Class to handle functionality for the TabWidget """

    def __init__(self, parent=None):
        """ Constructor that takes a parent widget as an optional parameter """
        super(TabWidget, self).__init__(parent)
        self.setup()

    def on_tab_closing(index):
        """ Function to handle when a tab is closed """
        pass

    def setup(self):
        """ Some initial settings for the TabWidget """
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setTabShape(QTabWidget.Triangular)
