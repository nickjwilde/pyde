from PyQt5.QtWidgets import QAction

class Action(QAction):
    def __init__(self, text="", parent=None):
        super(Action, self).__init__(text, parent)
