from PyQt5.QtWidgets import QTextEdit

class TextEdit(QTextEdit):

    def __init__(self, text="", parent=None):
        super(TextEdit, self).__init__(text, parent)
        self.setup()

    def setup(self):
        self.setUndoRedoEnabled(True)
