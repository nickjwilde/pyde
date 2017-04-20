import unittest
from PyQt5.QtWidgets import QApplication

from ui.editor import TabWidget, TextEdit

class TabWidgetTest(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(list(''))
        self.tab_widget = TabWidget()
        self.tab_widget.addTab(TextEdit("", self.tab_widget), "new %s" % str(self.tab_widget.count() + 1))

    def test_new_tab(self):
        self.assertEqual(self.tab_widget.count(), 1)
        self.assertEqual(len(self.tab_widget.new_tabs), 1)
        self.assertEqual(self.tab_widget.new_tab_index, 2)

    def test_remove_tab(self):
        self.assertEqual(self.tab_widget.count(), 1)
        self.assertEqual(len(self.tab_widget.new_tabs), 1)
        self.assertEqual(self.tab_widget.new_tab_index, 1)
        
