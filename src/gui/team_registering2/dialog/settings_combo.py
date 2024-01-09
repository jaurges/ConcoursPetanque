import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application

class SettingCombo(QtWidgets.QDialog):
    club = QtCore.Signal(str)
    def __init__(self):
        super().__init__()
        #firsttab = FirstTab()
        #self.club.connect(firsttab.addItemtocombo)

        label = QtWidgets.QLabel("Ajouter un nom de club")
        self.lineEdit = QtWidgets.QLineEdit()
        button_1 = QtWidgets.QPushButton("Valider")
        button_2 = QtWidgets.QPushButton("Annuler")
        layout = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.lineEdit)
        layout_button.addWidget(button_2)
        layout_button.addWidget(button_1)
        layout.addLayout(layout_button)

        button_1.clicked.connect(self.btn)
        button_2.clicked.connect(self.close)

    @QtCore.Slot()
    def btn(self):
        self.club.emit(self.lineEdit.text())
        self.lineEdit.clear()
        print("prout")
    
    def close(self):    
        self.hide()