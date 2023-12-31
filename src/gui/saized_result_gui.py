import sys
import re
import sqlite3
sys.path.append(".")
from PySide6 import QtWidgets, QtGui, QtCore
from src.application import Application


class Saized_Result(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.table_1 = QtWidgets.QTableWidget()
        self.table_2 = QtWidgets.QTableWidget()

        self.table_1.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table_1.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.table_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.lineEdit_1 = QtWidgets.QLineEdit()
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_4 = QtWidgets.QLineEdit()


        self.label_2 = QtWidgets.QLabel("team1 :")
        self.label_3 = QtWidgets.QLabel("team2 :")
        self.label_4 = QtWidgets.QLabel("result1 :")
        self.label_5 = QtWidgets.QLabel("result2 :")
        self.label_6 = QtWidgets.QLabel("results")

        self.pushbutton1 = QtWidgets.QPushButton("Annuler")
        self.pushbutton2 = QtWidgets.QPushButton("Valider")

        self.pushbutton3 = QtWidgets.QPushButton("Annuler")
        self.pushbutton4 = QtWidgets.QPushButton("Finaliser")

        self.combobox = QtWidgets.QComboBox()

        spacer1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.base_layout = QtWidgets.QVBoxLayout(self)
        self.first_side = QtWidgets.QVBoxLayout()
        self.second_side = QtWidgets.QVBoxLayout()
        self.middle = QtWidgets.QHBoxLayout()

        self.layout_1 = QtWidgets.QVBoxLayout()
        self.layout_2 = QtWidgets.QVBoxLayout()
        self.layout_3 = QtWidgets.QVBoxLayout()
        self.layout_4 = QtWidgets.QVBoxLayout()
        self.layout_5 = QtWidgets.QHBoxLayout()
        self.layout_6 = QtWidgets.QHBoxLayout()
        self.layout_7 = QtWidgets.QHBoxLayout()
        self.layout_8 = QtWidgets.QHBoxLayout()

        self.layout_1.addWidget(self.combobox)
        self.layout_1.addWidget(self.table_1)

        self.layout_2.addWidget(self.label_2)
        self.layout_2.addWidget(self.lineEdit_1)

        self.layout_3.addWidget(self.label_3)
        self.layout_3.addWidget(self.lineEdit_2)

        self.layout_4.addWidget(self.label_6)
        self.layout_4.addWidget(self.table_2)

        self.layout_5.addWidget(self.label_4)
        self.layout_5.addWidget(self.lineEdit_3)

        self.layout_6.addWidget(self.label_5)
        self.layout_6.addWidget(self.lineEdit_4)

        self.layout_7.addWidget(self.pushbutton1)
        self.layout_7.addWidget(self.pushbutton2)

        self.layout_8.addWidget(self.pushbutton3)
        self.layout_8.addWidget(self.pushbutton4)

        self.first_side.addLayout(self.layout_2)
        self.first_side.addLayout(self.layout_5)

        self.second_side.addLayout(self.layout_3)
        self.second_side.addLayout(self.layout_6)

        self.middle.addSpacerItem(spacer3)
        self.middle.addLayout(self.first_side)
        self.middle.addSpacerItem(spacer5)
        self.middle.addLayout(self.second_side)
        self.middle.addSpacerItem(spacer4)

        self.base_layout.addLayout(self.layout_1)
        self.base_layout.addSpacerItem(spacer1)
        self.base_layout.addLayout(self.middle)
        self.base_layout.addSpacerItem(spacer2)
        self.base_layout.addLayout(self.layout_7)
        self.base_layout.addLayout(self.layout_4)
        self.base_layout.addLayout(self.layout_8)

        self.set_combobox()

        self.combobox_setting()
        
        self.team_print_in_table()
        self.score_print()


        self.combobox.currentIndexChanged.connect(self.team_print_in_table)
        self.combobox.currentIndexChanged.connect(self.score_print)
        self.table_1.currentItemChanged.connect(self.team_print_in_line)
        self.pushbutton1.clicked.connect(self.clear_line)
        self.pushbutton2.clicked.connect(self.register_result)
        self.pushbutton2.clicked.connect(self.score_print)
        self.pushbutton4.clicked.connect(self.finalisation)

        self.resizeEvent = self.adjust_columns

    def combobox_setting(self):
        app = Application()
        n = app.get_match_n()
        for i in range(n):
            self.combobox.addItem("match" + str(i))

    def team_print_in_table(self):
        app = Application()
        n = int(re.search(r'\d+', self.combobox.currentText()).group())
        output = app.return_match(n)
        self.table_1.setRowCount(len(output))
        self.table_1.setColumnCount(2)
        self.table_1.setHorizontalHeaderLabels(('team1', 'team2'))
        row_index = 0
        for row in output:
            self.table_1.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["team1"]))
            self.table_1.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row["team2"]))

            row_index += 1

    def set_combobox(self):
        app = Application()
        n = app.get_match_n()
        self.combobox.setCurrentIndex(n)

    def team_print_in_line(self):
        selected_item = self.table_1.currentItem()
        if selected_item is not None:
            selected_row = selected_item.row()
            values = [self.table_1.item(selected_row, col).text() for col in range(self.table_1.columnCount())]
            self.lineEdit_1.setText(str(values[0]))
            self.lineEdit_2.setText(str(values[1]))
        else:
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()

    def register_result(self):
        app = Application()
        output1 = self.lineEdit_3.text()
        output2 = self.lineEdit_4.text()
        current_row = int(self.table_1.currentRow()) + 1
        n = self.combobox.currentIndex()
        try:
            app.register_result(current_row, n, output1, output2)
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
        except sqlite3.OperationalError:
            #erroGui = ErrorGui()
            #erroGui.resize(400, 100)
            #erroGui.show()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()

    def clear_line(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def score_print(self):
        app = Application()
        n = int(re.search(r'\d+', self.combobox.currentText()).group())
        output = app.return_match(n)
        self.table_2.setRowCount(len(output))
        self.table_2.setColumnCount(4)
        self.table_2.setHorizontalHeaderLabels(('team1', 'output1', 'team2', 'output2'))
        row_index = 0
        for row in output:
            self.table_2.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["team1"]))
            self.table_2.setItem(row_index, 1, QtWidgets.QTableWidgetItem(str(row["output1"])))
            self.table_2.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row["team2"]))
            self.table_2.setItem(row_index, 3, QtWidgets.QTableWidgetItem(str(row["output2"])))

            row_index += 1
    
    def finalisation(self):
        app = Application()
        app.set_overall()

    def adjust_columns(self, event):
        window_width = event.size().width()
        column_width_1 = window_width / 3
        column_width_2 = window_width / 4
        for col in range(self.table_1.columnCount()):
            self.table_1.setColumnWidth(col, column_width_1)
        for col in range(self.table_2.columnCount()):
            self.table_2.setColumnWidth(col, column_width_2)
    
    def closeEvent(self, event):
        self.finalisation()
        event.accept()


class ErrorGui(QtWidgets.QWidget):
    def __int__(self):
        super().__int__()

        self.text = QtWidgets.QLabel("Les résultats ne sont que des chiffres", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Saized_Result()
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
