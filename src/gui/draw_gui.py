import sys
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application
import numpy


class Draw_gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw")
        app = Application()

        self.button = QtWidgets.QPushButton("Tirage")
        self.button_2 = QtWidgets.QPushButton("Valider")
        self.button_3 = QtWidgets.QPushButton("Annuler")
        self.table = QtWidgets.QTableWidget(self)
        self.combobox = QtWidgets.QComboBox()

        self.combobox.addItem("Aléatoire")
        self.combobox.addItem("Classement")

        self.table.setHorizontalHeaderLabels(('match_name', 'team1', 'team2'))

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout_button_1 = QtWidgets.QHBoxLayout()
        self.layout_button_2 = QtWidgets.QHBoxLayout()
        self.layout_button_1.addWidget(self.combobox)
        self.layout_button_1.addWidget(self.button)
        self.layout_button_2.addWidget(self.button_3)
        self.layout_button_2.addWidget(self.button_2)
        self.layout.addLayout(self.layout_button_1)
        self.table.setColumnCount(3)
        self.layout.addWidget(self.table, 1)
        self.layout.addLayout(self.layout_button_2)

        self.button.clicked.connect(self.draw)
        self.button_3.clicked.connect(self.clear_content)
        self.button_2.clicked.connect(self.register_match_)
        self.resizeEvent = self.adjust_columns

    @QtCore.Slot()
    def draw(self):
        app = Application()
        output = app.draw_random()
        self.table.setRowCount(len(output))
        self.table.setHorizontalHeaderLabels(('team1', 'team2'))

        row_index = 0
        for row in output:
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row[1]))

            row_index += 1
    
    def clear_content(self): 
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels('team1', 'team2')

    def register_match_(self):
        app = Application()
        table_data = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(2):
                item = self.table.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append(None)

            table_data.append(row_data)
        print(table_data)
        app.register_match(table_data)
    
    def adjust_columns(self, event):
        window_width = event.size().width()
        column_width = window_width / 2
        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, column_width)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Draw_gui()
    widget.resize(480, 480)
    widget.show()

    sys.exit(app.exec())