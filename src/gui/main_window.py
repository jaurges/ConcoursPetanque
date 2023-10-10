import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
sys.path.append(".")
from src.database_handler import DatabaseHandler


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())