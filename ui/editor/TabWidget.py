from PyQt5.QtWidgets import QTabWidget, QPushButton

from ui.editor import TextEdit
from ui.dialogs import MessageBox

class TabWidget(QTabWidget):
    """ Class to handle functionality for the TabWidget """

    def __init__(self, parent=None):
        """ Constructor that takes a parent widget as an optional parameter """
        super(TabWidget, self).__init__(parent)
        self.init_ui()

    def on_tab_closing(self, index):
        """ Function to handle when a tab is closed """
        if index >= 0:
            if(self.currentWidget().document().isModified()):
                save_prompt = MessageBox("This document has modified changes that haven't been saved. Do you want to save changes?", self)

                save_button = QPushButton("Save", self)
                save_prompt.addButton(save_button, MessageBox.YesRole)
                save_prompt.addButton("Cancel", MessageBox.RejectRole)
                save_prompt.addButton("Close Without Saving", MessageBox.NoRole)
                save_prompt.setDefaultButton(save_button)
                save_prompt.exec_()
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

    def save_prompt_finish(self, result):
        if result == MessageBox.YesRole:
            print('saving')
        elif result == MessageBox.NoRole:
            print('Nope, not saving')
        elif result == MessageBox.RejectRole:
            print('Rejectamundo, or just cancelled')
