from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import Qt

from .Highlighter import PyHighlighter

class TextEdit(QTextEdit):

    def __init__(self, text="", parent=None):
        super(TextEdit, self).__init__(text, parent)
        self.init_ui()

    def init_ui(self):
        self.setUndoRedoEnabled(True)
        self.setFontFamily("Consolas")
        self.setFontPointSize(10)
        py_highlighter = PyHighlighter(self.document())

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Tab:
            self.insertPlainText(' ' * 4)
        elif key_event.key() == Qt.Key_Return:
            previous_text = self.document().findBlockByNumber(self.textCursor().blockNumber()).text()
            return super().keyPressEvent(key_event)
        else:
            return super().keyPressEvent(key_event)