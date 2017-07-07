from functools import partial
from PyQt5.QtWidgets import QTabWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

from helpers.handlers import action_handlers

class TabWidget(QTabWidget):
    """ Class to handle functionality for the TabWidget """

    def __init__(self, parent=None):
        """ Constructor that takes a parent widget as an optional parameter """
        super().__init__(parent)

        # instance variables to manage the new tabs that are created using the new option
        self._new_tab_numbers = []
        self._next_tab_number = 1
        self._deleted_tab_text = ""

        self.init_ui()

    def set_next_tab_number(self):
        """ Sets the next tab number for new text edit tabs """
        if len(self._new_tab_numbers) == 0:
            self._next_tab_number = 1
        else:
            expected = range(1, max(self._new_tab_numbers) + 1)
            missing = list(set(expected) - set(self._new_tab_numbers))
            if len(missing) == 0:
                self._next_tab_number = max(self._new_tab_numbers) + 1
            else:
                self._next_tab_number = min(missing)

    @property
    def next_tab_number(self):
        return str(self._next_tab_number)

    def on_tab_closing(self, index):
        """ Function to handle when a tab is closed """
        if index >= 0:
            self._deleted_tab_text = self.tabText(index)
            if(self.currentWidget().document().isModified()):
                save_prompt = QMessageBox(self)
                save_prompt.setText("This document has modified changes that haven't been saved. Do you want to save changes?")

                save_button = QPushButton("Save", self)
                save_prompt.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                save_prompt.setDefaultButton(QMessageBox.Save)
                self.handle_save_prompt_result(save_prompt.exec_())
            else:
                self.removeTab(index)
        else:
            raise IndexError

    def init_ui(self):
        """ Some initial settings for the TabWidget """
        self.setTabsClosable(True)
        self.setMovable(True)
        #self.setTabShape(QTabWidget.Triangular)
        self.tabCloseRequested.connect(self.on_tab_closing)

    def handle_save_prompt_result(self, result):
        """ Gets called when the save prompt has been handled """
        if result == QMessageBox.Save:
            action_handlers.save_file(self.parentWidget())
        elif result == QMessageBox.Discard:
            self.removeTab(self.currentIndex())

    def tabInserted(self, index):
        """ Fired when a tab is inserted. Overridden part of Qt framework """
        tab_text = self.tabText(index)
        if "new" in tab_text:
            self._new_tab_numbers.append(int(tab_text.split()[-1]))
            self.set_next_tab_number()
            super().tabInserted(index)
        else:
            super().tabInserted(index)

    def tabRemoved(self, index):
        """ Fired when a tab is removed. Overridden part of Qt framework """
        tab_text = self._deleted_tab_text
        if "new" in tab_text:
            self._new_tab_numbers.remove(int(tab_text.split()[-1]))
            self.set_next_tab_number()
            super().tabRemoved(index)
        else:
            super().tabRemoved(index)
