import sys
from PyQt5.QtWidgets import QApplication

from ui.MainWindow import MainWindow

# Main startup file
app = QApplication(sys.argv)
m = MainWindow()
m.show()
app.exec_()
