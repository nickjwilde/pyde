import sys
from PyQt5.QtWidgets import QApplication

from ui import MainWindow

# Main startup file
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()
