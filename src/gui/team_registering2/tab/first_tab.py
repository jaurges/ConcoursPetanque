import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class FirstTab(QtWidgets.QDialog):
    value = QtCore.Signal(str)
    def __init__(self):
        super().__init__()
        self.count_click = 0
        self.label = QtWidgets.QLabel("Nombre de club :")
        self.table = QtWidgets.QTableWidget()
        self.spin_box = QtWidgets.QSpinBox()
        self.comboboxes = [QtWidgets.QComboBox(self) for _ in range(self.spin_box.value())]

        self.table.horizontalHeader().setVisible(False)
        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.spin_box.setValue(1)

        layout_spin = QtWidgets.QHBoxLayout()
        layout_base = QtWidgets.QVBoxLayout(self)

        layout_spin.addWidget(self.label)
        layout_spin.addWidget(self.spin_box)
        layout_base.addLayout(layout_spin)
        layout_base.addWidget(self.table)

        self.set_headers()
        self.spin_box.valueChanged.connect(self.set_headers)
        self.table.cellPressed.connect(self.print_next)

    def set_headers(self):
        self.comboboxes = [QtWidgets.QComboBox() for _ in range(self.spin_box.value())]
        app = Application()
        self.output = app.return_club_player()
        #print(list(self.output))
        for combo_box in self.comboboxes:
            for i in list(self.output):
                combo_box.addItem(i)
            combo_box.currentIndexChanged.connect(self.index_changed)
            self.table.setColumnCount(self.comboboxes.index(combo_box)+1)

            item = QtWidgets.QTableWidgetItem()
            self.table.setItem(0, self.comboboxes.index(combo_box), item)
            self.table.setCellWidget(0, self.comboboxes.index(combo_box), combo_box)
            #print(self.output[combo_box.currentText()])

            self.table.setRowCount(len(self.output[combo_box.currentText()]))
            #self.table.setColumnCount(self.comboboxes.index(combo_box)+1)
            row_index = 0
            for player in self.output[combo_box.currentText()]:
                #print(player)
                self.table.setItem(row_index, self.comboboxes.index(combo_box), QtWidgets.QTableWidgetItem(player))

                row_index += 1
    
    def index_changed(self, index):
        sender = self.sender()
        self.table.setRowCount(len(self.output[sender.currentText()]))
        row_index = 0
        for player in self.output[sender.currentText()]:
            #print(player)
            self.table.setItem(row_index, self.comboboxes.index(sender), QtWidgets.QTableWidgetItem(player))

            row_index += 1
    
    def print_next(self):
        selected_items = self.table.selectedItems()
        #print(selected_items[0].text())
        if selected_items:
            self.value.emit(selected_items[0].text())