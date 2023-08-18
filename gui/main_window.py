import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
sys.path.append(".")
from object.object import Match, Team


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableWidget()
        self.menubar = QtWidgets.QMenuBar()
        self.button1 = QtWidgets.QPushButton("Team")
        self.button2 = QtWidgets.QPushButton("Draw")
        self.button3 = QtWidgets.QPushButton("Team Registering")

        self.left_layout = QtWidgets.QVBoxLayout()
        self.base_layout = QtWidgets.QHBoxLayout(self)
        self.frame = QtWidgets.QFrame()
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("#frame {background-color:red;}")

        self.frame.setLayout(self.left_layout)

        self.left_layout.addWidget(self.frame)
        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.button3)
        self.base_layout.addWidget(self.frame)
        self.base_layout.addWidget(self.table)

        #self.left_layout.setStyleSh
        self.button1.setStyleSheet(
            """
            QPushButton {
                background-color: blue;
                color: white;
                border-radius: 5px;
                font-size: 18px;
            }

            QPushButton:hover {
                background-color: lightblue;
            }
            """
        )


class Application:
    def __init__(self):
        self.database_handler = None


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())