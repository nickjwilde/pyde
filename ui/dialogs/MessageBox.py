from PyQt5.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    """ Class for functionality of a QMessageBox """

    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.setText(text)
