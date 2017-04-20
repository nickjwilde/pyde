import unittest

from PyQt5.QtWidgets import QApplication

from ui import MainWindow
from ui.editor import TabWidget
from ui.menus import MenuBar

class MainWindowTest(unittest.TestCase):
    """ Class to test that the correct widgets get created for the application """

    def setUp(self):
        self.app = QApplication(list(''))
        self.main_window = MainWindow()

    def test_central_widget(self):
        self.assertIsInstance(self.main_window.centralWidget(), TabWidget)

    def test_menu_bar(self):
        self.assertIsInstance(self.main_window.menuBar(), MenuBar)
