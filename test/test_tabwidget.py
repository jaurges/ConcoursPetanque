import sys
from typing import Optional

from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets


class TabGui(QtWidgets.QWidget):
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("test")

        tabwidget = QtWidgets.QTabWidget()
        tabwidget.addTab(FirstTab(), "FirstTab")
        tabwidget.addTab(SecondTab(), "SecondTab")

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tabwidget)

        self.setLayout(vbox)

    def open_next(self):
        self.opened.emit()
        self.close()


class FirstTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel("prout")
        lineedit = QtWidgets.QLineEdit()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(lineedit)
        self.setLayout(layout)


class SecondTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TabGui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())
