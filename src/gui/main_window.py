import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
sys.path.append(".")
from src.application import Application


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableWidget()
        self.button1 = QtWidgets.QPushButton("Tirage")
        self.button2 = QtWidgets.QPushButton("team register")
        self.button3 = QtWidgets.QPushButton("team_viewing")
        self.button4 = QtWidgets.QPushButton("Paramètres")

        self.button1.setStyleSheet(
                    '''
            QPushButton {
                border: 2px solid #e8e8e8; /* Couleur de la bordure */
                border-radius: 10px; /* Rayon des coins arrondis */
                padding: 10px; /* Espace interne */
                font-size: 12px; /* Taille de la police */
            }

            QPushButton:hover {
                background-color: #f9f9f9; /* Couleur de fond au survol */
            }
            '''
            )
        self.button2.setStyleSheet(
                    '''
            QPushButton {
                border: 2px solid #e8e8e8; /* Couleur de la bordure */
                border-radius: 10px; /* Rayon des coins arrondis */
                padding: 10px; /* Espace interne */
                font-size: 12px; /* Taille de la police */
            }

            QPushButton:hover {
                background-color: #f9f9f9; /* Couleur de fond au survol */
            }
            '''
            )
        self.button3.setStyleSheet(
                    '''
            QPushButton {
                border: 2px solid #e8e8e8; /* Couleur de la bordure */
                border-radius: 10px; /* Rayon des coins arrondis */
                padding: 10px; /* Espace interne */
                font-size: 12px; /* Taille de la police */
            }

            QPushButton:hover {
                background-color: #f9f9f9; /* Couleur de fond au survol */
            }
            '''
            )
        self.button4.setStyleSheet(
                   '''
            QPushButton {
                border: 2px solid #e8e8e8; /* Couleur de la bordure */
                border-radius: 10px; /* Rayon des coins arrondis */
                padding: 10px; /* Espace interne */
                font-size: 12px; /* Taille de la police */
            }

            QPushButton:hover {
                background-color: #f9f9f9; /* Couleur de fond au survol */
            }
            '''
            )
        self.button1.setFixedSize(100, 100)
        self.button2.setFixedSize(100, 100)
        self.button3.setFixedSize(100, 100)
        self.button4.setFixedSize(100, 100)

        self.layout_grid = QtWidgets.QGridLayout()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.layout_base = QtWidgets.QHBoxLayout(self)

        #self.layout_grid.setColumnStretch(0, 1)
        #self.layout_grid.setColumnStretch(1, 1)

        #self.layout_grid.columnCount(2)
        #self.layout_grid.rowCount(2)
        '''self.layout_grid.addWidget(self.button1, 0, 0)
        self.layout_grid.addWidget(self.button2, 0, 1)
        self.layout_grid.addWidget(self.button3, 1, 0)
        self.layout_grid.addWidget(self.button4, 1, 1)'''
        self.vlayout.addWidget(self.button1)
        self.vlayout.addWidget(self.button2)
        self.vlayout.addWidget(self.button3)
        self.vlayout.addWidget(self.button4)
        self.layout_base.addWidget(self.table)
        self.layout_base.addLayout(self.vlayout)

        self.team_print_in_table()

    def team_print_in_table(self):
        app = Application()
        n_match = app.get_match_n()
        output = app.return_overall()
        overall = app.overall()
        self.table.setRowCount(len(output))
        self.table.setColumnCount(n_match+2)
        headers = ['team']
        headers.extend([f"match{i}" for i in range(n_match)])
        headers.append('total')
        headers = tuple(headers)
        self.table.setHorizontalHeaderLabels(headers)
        row_index = 0
        for team in overall:
            for row in output:
                if row[0]==team:
                    self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["team"]))
                    self.table.setItem(row_index, n_match+1, QtWidgets.QTableWidgetItem(str(row["total"])))
                    for i in range(n_match):
                        self.table.setItem(row_index, i+1, QtWidgets.QTableWidgetItem(str(row[f"output{i}"])))
                else:
                    pass

            row_index += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(1000, 600)
    widget.show()

    sys.exit(app.exec())