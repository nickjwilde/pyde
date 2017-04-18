from PyQt5.QtWidgets import QMainWindow

from .menus import Menu
from .menus import MenuBar
from .Action import Action
from core import slots
from .editor import TextEdit


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setup()

    def setup(self):
        self.showMaximized()
        self.setCentralWidget(TextEdit(parent=self))
        self.setMenuBar(MenuBar(self))
        self.create_menus()

    def create_menus(self):
        file_menu = Menu("File", self.menuBar())
        new_file_action = Action("New", self)
        new_file_action.triggered.connect(slots.file_new)
        file_menu.addAction(new_file_action)

        self.menuBar().addMenu(file_menu)
