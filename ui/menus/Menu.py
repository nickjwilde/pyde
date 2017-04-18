from PyQt5.QtWidgets import QMenu

class Menu(QMenu):

    def __init__(self, title="", parent=None):
        super(Menu, self).__init__(title, parent)
