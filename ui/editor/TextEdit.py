from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFontMetrics

class TextEdit(QTextEdit):

    def __init__(self, text="", parent=None):
        super(TextEdit, self).__init__(text, parent)
        self.init_ui()

    def init_ui(self):
        self.setUndoRedoEnabled(True)
        font_metrics = QFontMetrics(self.currentFont())
        self.setTabStopWidth(4 * font_metrics.width(' '))

