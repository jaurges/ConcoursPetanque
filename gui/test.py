import sys
import sqlite3
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtSql import QSqlQuery

from object.object import Match


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableWidget()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.table)

        self.load_data()

    @QtCore.Slot()
    def load_data(self):
        dir_path = "/media/antonin/ANTONIN/Travail/projet-pétanque/nouveau/data/database.db"
        con = sqlite3.connect(dir_path)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        query = QSqlQuery("SELECT match_name, team1, output1, team2, output2 FROM match5")
        cursor.execute(query)


        database_handler = Match("database.db")
        n = 5
        query = database_handler.return_match(5)
        self.table.setRowCount(len(output))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('match_name', 'team1', 'output1', 'team2', 'output2'))
        row_index = 0
        while output.next():
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(output.value(1)))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(output.value(1)))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(output.value(1)))
            self.table.setItem(row_index, 3, QtWidgets.QTableWidgetItem(output.value(1)))
            self.table.setItem(row_index, 4, QtWidgets.QTableWidgetItem(output.value(1)))

            row_index += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
