import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class FirstTab(QtWidgets.QDialog):
    value = QtCore.Signal(list)
    setting = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel("Nombre de club :")
        self.table = QtWidgets.QTableWidget()
        self.spin_box = QtWidgets.QSpinBox()
        self.comboboxes = [QtWidgets.QComboBox(self) for _ in range(self.spin_box.value())]

        self.table.horizontalHeader().setVisible(False)
        self.table.setColumnCount(5)
        self.table.setRowCount(5)
        self.spin_box.setValue(1)

        layout_spin = QtWidgets.QHBoxLayout()
        layout_base = QtWidgets.QVBoxLayout(self)

        layout_spin.addWidget(self.label)
        layout_spin.addWidget(self.spin_box)
        layout_base.addLayout(layout_spin)
        layout_base.addWidget(self.table)

        self.spin_box.valueChanged.connect(self.set_headers)

    def set_headers(self):
        self.comboboxes = [QtWidgets.QComboBox() for _ in range(self.spin_box.value())]
        app = Application()
        output = app.return_club_player()
        print(list(output[0]))
        for combo_box in self.comboboxes:
            combo_box.addItem('caca')
            combo_box.addItem('prout')
            combo_box.currentIndexChanged.connect(self.index_changed)

            item = QtWidgets.QTableWidgetItem()
            self.table.setItem(0, self.comboboxes.index(combo_box), item)
            self.table.setCellWidget(0, self.comboboxes.index(combo_box), combo_box)
    
    def index_changed(self, index):
        sender = self.sender()
        selected_text = sender.currentText()
        print(selected_text)