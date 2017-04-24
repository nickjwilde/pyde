from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.menus import Menu, MenuBar
from ui.Action import Action
from ui.editor import TabWidget, TextEdit
from ui.dialogs import FileDialog, MessageBox


class MainWindow(QMainWindow):
    """ Class to contain logic for QMainWindow object """
    def __init__(self, parent=None):
        """ Constructor that takes a parent widget as an optional parameter """
        super(MainWindow, self).__init__(parent)
        self.init_ui()

    def create_file_menu(self):
        file_menu = Menu("File", self.menuBar())
        file_menu.addAction(self.create_action("New", self.file_new))
        file_menu.addAction(self.create_action("Save", self.save_file))
        file_menu.addAction(self.create_action("Exit", QApplication.quit))
        return file_menu

    def create_action(self, text, callback):
        action = Action(text, self)
        action.triggered.connect(callback)
        return action

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
        tab_widget.addTab(TextEdit("", tab_widget), "new %s" % tab_widget.next_tab_number)

    def save_file(self):
        tab_widget = self.centralWidget()
        if tab_widget.currentIndex() == -1:
            mb = MessageBox("No open file. Can't save file", tab_widget)
            mb.exec_()
        else:
            FileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py *.pyw)")
