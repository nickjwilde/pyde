
from PyQt5.QtWidgets import QFileDialog

class FileDialog(QFileDialog):
    """ A class to implement the behavior of FileDialog """

    def __init__(self, parent=None):
        super().__init__(parent)
