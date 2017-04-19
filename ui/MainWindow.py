from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.menus import Menu, MenuBar
from ui.Action import Action
from ui.editor import TabWidget, TextEdit


class MainWindow(QMainWindow):
    """ Class to contain logic for QMainWindow object """
    def __init__(self, parent=None):
        """ Constructor that takes a parent widget as an optional parameter """
        super(MainWindow, self).__init__(parent)
        self.init_ui()

    def create_file_menu(self):
        file_menu = Menu("File", self.menuBar())
        file_menu.addAction(self.create_file_new_action())
        file_menu.addAction(self.create_file_exit_action())
        return file_menu

    def create_file_exit_action(self):
        exit_file_action = Action("Exit", self)
        exit_file_action.triggered.connect(QApplication.quit)
        return exit_file_action

    def create_file_new_action(self):
        new_file_action = Action("New", self)
        new_file_action.triggered.connect(self.file_new)
        return new_file_action

    def create_menus(self):
        """ Initializes and creates the menus for the application """
        self.menuBar().addMenu(self.create_file_menu())

    def init_ui(self):
        """ Some startup processes for the MainWindow class """
        self.setCentralWidget(TabWidget(self))
        self.setMenuBar(MenuBar(self))
        self.create_menus()
        self.showMaximized()

    #slots
    def file_new(self):
        tab_widget = self.centralWidget()
        tab_widget.addTab(TextEdit("", tab_widget), "new %s" % str(tab_widget.count() + 1))
