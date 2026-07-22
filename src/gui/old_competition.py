import sys
sys.path.append('.')
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class OldCompetition(QtWidgets.QWidget):
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("old__competition")

        self.button1 = QtWidgets.QPushButton("Annuler")
        self.button2 = QtWidgets.QPushButton("Suivant")
        self.table = QtWidgets.QTableWidget()

        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        self.layout_button = QtWidgets.QHBoxLayout()
        self.layout_base = QtWidgets.QVBoxLayout(self)

        self.layout_button.addWidget(self.button1)
        self.layout_button.addWidget(self.button2)
        self.layout_base.addWidget(self.table)
        self.layout_base.addLayout(self.layout_button)

        self.print_in_table()
        self.resizeEvent = self.adjust_columns

        self.button2.clicked.connect(self.clicked_btn)
        self.button2.clicked.connect(self.open_next)
        self.button1.clicked.connect(self.open_previous)
    
    def print_in_table(self):
        app = Application()
        output = app.return_general()
        self.table.setRowCount(len(output))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('name', 'date', 'play_mod', 'location'))
        row_index = 0
        for row in output:
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["name"]))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row["date"]))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row["play_mod"]))
            self.table.setItem(row_index, 3, QtWidgets.QTableWidgetItem(row["location"]))

            row_index += 1
    
    def adjust_columns(self, event):
        window_width = event.size().width()
        column_width_1 = window_width / 5
        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, column_width_1)
    
    def clicked_btn(self):
        selected_items = self.table.selectedItems()
        try:
            selected_row = selected_items[0].row()
        except IndexError:
            print("errorguinécessaireici")
        values = [self.table.item(selected_row, col).text() for col in range(self.table.columnCount())]
        app = Application()
        app.set_competition_index(values)


    def open_next(self):
        self.opened.emit()
        self.close()
    
    def open_previous(self):
        self.parent_widget.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = OldCompetition()
    widget.resize(480, 360)
    widget.show()

    sys.exit(app.exec())
