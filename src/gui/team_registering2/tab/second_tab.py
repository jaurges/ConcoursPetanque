import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class SecondTab(QtWidgets.QDialog):
    value = QtCore.Signal(str)
    def __init__(self):
        super().__init__()
        self.row_table2 = {}

        self.label = QtWidgets.QLabel("Nombre de club :")
        self.table1 = QtWidgets.QTableWidget()
        self.table2 = QtWidgets.QTableWidget()
        self.spin_box = QtWidgets.QSpinBox()
        self.comboboxes = [QtWidgets.QComboBox(self) for _ in range(self.spin_box.value())]
        button = QtWidgets.QPushButton("générer")

        self.table1.horizontalHeader().setVisible(False)
        self.table1.setColumnCount(1)
        self.table1.setRowCount(1)
        self.table1.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.spin_box.setValue(1)

        self.table2.setColumnCount(1)
        self.table2.setRowCount(1)
        self.table2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        layout_spin = QtWidgets.QHBoxLayout()
        layout_base = QtWidgets.QVBoxLayout(self)

        layout_spin.addWidget(self.label)
        layout_spin.addWidget(self.spin_box)
        layout_base.addLayout(layout_spin)
        layout_base.addWidget(self.table1)
        layout_base.addWidget(self.table2)
        layout_base.addWidget(button)

        self.resizeEvent = self.adjust_columns

        self.set_headers()
        self.spin_box.valueChanged.connect(self.set_headers)
        self.table1.cellPressed.connect(self.print_next)
        button.pressed.connect(self.generate)

    def set_headers(self):
        
        self.comboboxes = [QtWidgets.QComboBox() for _ in range(self.spin_box.value())]
        app = Application()
        self.output = app.return_club_player()
        #print(list(self.output))
        for combo_box in self.comboboxes:
            for i in list(self.output):
                combo_box.addItem(i)
            combo_box.currentIndexChanged.connect(self.index_changed)
            self.table1.setColumnCount(self.comboboxes.index(combo_box)+1)
            self.table2.setColumnCount(self.comboboxes.index(combo_box)+1)

            item = QtWidgets.QTableWidgetItem()
            self.table1.setItem(0, self.comboboxes.index(combo_box), item)
            self.table1.setCellWidget(0, self.comboboxes.index(combo_box), combo_box)
            #print(self.output[combo_box.currentText()])

            self.table1.setRowCount(len(self.output[combo_box.currentText()]))
            #self.table1.setColumnCount(self.comboboxes.index(combo_box)+1)
            row_index = 0
            for player in self.output[combo_box.currentText()]:
                #print(player)
                widget = QtWidgets.QWidget()
                checkbox = QtWidgets.QCheckBox()
                label = QtWidgets.QLabel(player)

                layout = QtWidgets.QHBoxLayout(widget)
                layout.addWidget(checkbox)
                layout.addWidget(label)
                layout.setAlignment(QtCore.Qt.AlignCenter)
                widget.setLayout(layout)
                
                '''old_widget = self.table1.cellWidget(row_index+1, self.comboboxes.index(combo_box))
                if old_widget:
                    old_widget'''
                #self.table1.setCellWidget(row_index+1, self.comboboxes.index(combo_box), QtWidgets.QWidget().setLayout(QtWidgets.QHBoxLayout()))
                
                self.table1.setCellWidget(row_index+1, self.comboboxes.index(combo_box), widget)

                checkbox.stateChanged.connect(self.checkbox_changed)
                #self.table1.setItem(row_index, self.comboboxes.index(combo_box), QtWidgets.QTableWidgetItem(player))

                row_index += 1
        self.adjust_columns(event=None)
        self.table2.setHorizontalHeaderLabels([combo_box.currentText() for combo_box in self.comboboxes])
    
    def index_changed(self, index):
        sender = self.sender()
        self.table1.setRowCount(len(self.output[sender.currentText()]))
        row_index = 0
        for player in self.output[sender.currentText()]:
            #print(player)
            widget = QtWidgets.QWidget()
            checkbox = QtWidgets.QCheckBox()
            label = QtWidgets.QLabel(player)

            layout = QtWidgets.QHBoxLayout(widget)
            layout.addWidget(checkbox)
            layout.addWidget(label)
            layout.setAlignment(QtCore.Qt.AlignCenter)
            widget.setLayout(layout)
            
            self.table1.setCellWidget(row_index+1, self.comboboxes.index(sender), QtWidgets.QWidget().setLayout(QtWidgets.QHBoxLayout()))
            
            self.table1.setCellWidget(row_index+1, self.comboboxes.index(sender), widget)

            checkbox.stateChanged.connect(self.checkbox_changed)

            row_index += 1
        
        self.table2.setHorizontalHeaderItem(self.comboboxes.index(sender), QtWidgets.QTableWidgetItem(sender.currentText()))
    
    def checkbox_changed(self, state):
        sender = self.sender()
        widget = sender.parentWidget()
        index = self.table1.indexAt(widget.pos())
        
        if index.isValid():
            row = index.row()
            column = index.column()
            
            label = self.table1.cellWidget(row, column).findChild(QtWidgets.QLabel)
            cell_text = label.text()
            
            print(f"Case à cocher dans la ligne {row}, colonne {column} cliquée. Nouvel état : {state}. Texte de la cellule : {cell_text}")
            self.table2.setItem(self.table2.ro(), column, QtWidgets.QTableWidgetItem(cell_text))
        else:
            print("Erreur : Impossible de déterminer la position de la case à cocher.")

    
    def print_next(self):
        selected_items = self.table1.selectedItems()
        #print(selected_items[0].text())
        if selected_items:
            self.value.emit(selected_items[0].text())
    
    def generate(self):
        pass

    def adjust_columns(self, event):
        window_width = self.table1.size().width()
        column_width = window_width / self.table1.columnCount()
        for col in range(self.table1.columnCount()):
            self.table1.setColumnWidth(col, column_width)
            self.table2.setColumnWidth(col, column_width)