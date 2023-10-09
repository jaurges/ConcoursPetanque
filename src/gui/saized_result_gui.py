import sys
import re
import sqlite3
sys.path.append(".")
from PySide6 import QtWidgets, QtGui, QtCore
from database_handler import DatabaseHandler


class Saized_Result(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.table_1 = QtWidgets.QTableWidget()
        self.table_2 = QtWidgets.QTableWidget()

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

        self.combobox = QtWidgets.QComboBox()

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

        self.first_side.addLayout(self.layout_2)
        self.first_side.addLayout(self.layout_5)

        self.second_side.addLayout(self.layout_3)
        self.second_side.addLayout(self.layout_6)

        self.middle.addLayout(self.first_side)
        self.middle.addLayout(self.second_side)

        self.base_layout.addLayout(self.layout_1)
        self.base_layout.addLayout(self.middle)
        self.base_layout.addLayout(self.layout_7)
        self.base_layout.addLayout(self.layout_4)

        self.combobox_setting()
        self.set_combobox()
        self.team_print_in_table()
        self.score_print()


        self.combobox.currentIndexChanged.connect(self.team_print_in_table)
        self.combobox.currentIndexChanged.connect(self.score_print)
        self.table_1.currentItemChanged.connect(self.team_print_in_line)
        self.pushbutton1.clicked.connect(self.clear_line)
        self.pushbutton2.clicked.connect(self.register_result)
        self.pushbutton2.clicked.connect(self.score_print)

    def combobox_setting(self):
        app = Application()
        n = app.return_match_nb()
        for i in range(n):
            self.combobox.addItem("match" + str(i))

    def team_print_in_table(self):
        app = Application()
        n = int(re.search(r'\d+', self.combobox.currentText()).group())
        output = app.team_print(n)
        self.table_1.setRowCount(len(output))
        self.table_1.setColumnCount(3)
        self.table_1.setHorizontalHeaderLabels(('match_name', 'team1', 'team2'))
        row_index = 0
        for row in output:
            self.table_1.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["match_name"]))
            self.table_1.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row["team1"]))
            self.table_1.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row["team2"]))

            row_index += 1

    def set_combobox(self):
        app = Application()
        n = app.return_match_nb()
        #print(n)
        self.combobox.setCurrentIndex(n-1)

    def team_print_in_line(self):
        app = Application()
        current_row = int(self.table_1.currentRow()) + 1
        n = self.combobox.currentIndex()
        output = app.team_print_in_line(current_row, n)
        self.lineEdit_1.setText(str(output[0]))
        self.lineEdit_2.setText(str(output[1]))

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
        output = app.score_print(n)
        self.table_2.setRowCount(len(output))
        self.table_2.setColumnCount(5)
        self.table_2.setHorizontalHeaderLabels(('match_name', 'team1', 'output1', 'team2', 'output2'))
        row_index = 0
        for row in output:
            self.table_2.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["match_name"]))
            self.table_2.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row["team1"]))
            self.table_2.setItem(row_index, 2, QtWidgets.QTableWidgetItem(str(row["output1"])))
            self.table_2.setItem(row_index, 3, QtWidgets.QTableWidgetItem(row["team2"]))
            self.table_2.setItem(row_index, 4, QtWidgets.QTableWidgetItem(str(row["output2"])))

            row_index += 1


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("database.db")

    def return_match_nb(self):
        n = self.database_handler1.match_nb_return()
        return n

    def team_print(self, n):
        output = self.database_handler1.return_match(n)
        return output

    def team_print_in_line(self, current_row, n):
        output = self.database_handler2.return_team_per_row(current_row, n)
        return output

    def register_result(self, row, n, output1, output2):
        self.database_handler1.register_result(row, n, output1, output2)

    def score_print(self, n):
        output = self.database_handler1.return_match(n)
        return output


class ErrorGui(QtWidgets.QWidget):
    def __int__(self):
        super().__int__()

        self.text = QtWidgets.QLabel("Les résultats ne sont que des chiffres", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Saized_Result()
    widget.resize(400, 600)
    widget.show()

    sys.exit(app.exec())
