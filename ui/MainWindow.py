from PyQt5.QtWidgets import QMainWindow

from ui.menus import Menu
from ui.menus import MenuBar
from ui.Action import Action
from core import slots
from ui.editor import TabWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setup()

    def setup(self):
        self.setCentralWidget(TabWidget(self))
        self.setMenuBar(MenuBar(self))
        self.create_menus()
        self.showMaximized()

    def create_menus(self):
        file_menu = Menu("File", self.menuBar())
        new_file_action = Action("New", self)
        new_file_action.triggered.connect(lambda: slots.file_new(self))
        file_menu.addAction(new_file_action)
        self.menuBar().addMenu(file_menu)
