from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import Qt

class TextEdit(QTextEdit):

    def __init__(self, text="", parent=None):
        super(TextEdit, self).__init__(text, parent)
        self.init_ui()

    def init_ui(self):
        self.setUndoRedoEnabled(True)
        self.setFontFamily("Consolas")
        self.setFontPointSize(10)
