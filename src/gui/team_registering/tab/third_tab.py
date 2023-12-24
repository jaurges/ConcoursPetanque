import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application

class ThirdTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QtWidgets.QLabel("Depuis la base de donnée :")
        self.label2 = QtWidgets.QLabel("Depuis un fichier .csv ou .txt :")
        self.button1 = QtWidgets.QPushButton("ouvrir")
        self.button2 = QtWidgets.QPushButton("ouvrir")

        spacer1 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layout_base = QtWidgets.QVBoxLayout(self)
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout2 = QtWidgets.QVBoxLayout()

        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.button1)
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.button2)
        self.layout_base.addSpacerItem(spacer1)
        self.layout_base.addLayout(self.layout1)
        self.layout_base.addSpacerItem(spacer2)
        self.layout_base.addLayout(self.layout2)
        self.layout_base.addSpacerItem(spacer3)

    @QtCore.Slot()
    def btn(self):
        self.club.emit(self.lineEdit.text())
        self.lineEdit.clear()
        print("prout")