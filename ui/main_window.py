import functools

from PyQt5.QtWidgets import (QMainWindow, QAction,
                             QShortcut, QApplication)
from PyQt5.QtGui import QKeySequence

from ui.tab_widget import TabWidget
from helpers.handlers import action_handlers

def create_action(title, key_sequence, callback, parent, *args):
    action = QAction(title, parent)
    action.shortcut = QShortcut(QKeySequence(key_sequence), parent)
    action.shortcut.activated.connect(functools.partial(callback, *args))
    action.triggered.connect(functools.partial(callback, *args))
    return action

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pyslice")
        self.showMaximized()
        self.createMenus()
        self.setCentralWidget(TabWidget(self))

    def createMenus(self):
        self.create_file_menu()

    def create_file_menu(self):
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(create_action("&New\tCtrl+N", "Ctrl+N", action_handlers.new_file, self, self))
        file_menu.addAction(create_action("&Save\tCtrl+S", "Ctrl+S", action_handlers.save_file, self, self))
        file_menu.addAction(create_action("E&xit\tAlt+F4", "Alt+F4", QApplication.quit, self))
