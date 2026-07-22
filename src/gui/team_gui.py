import sys
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class Team_gui(QtWidgets.QWidget):
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team")

        self.tab = QtWidgets.QTableWidget(self)
        self.label = QtWidgets.QLabel("Affichage des équipes :")
        self.button = QtWidgets.QPushButton("Ajouter des équipes")
        self.button1 = QtWidgets.QPushButton("rafraichîr")

        #self.button1.setFixedSize(10, 10)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.tab)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button)

        self.print_list()
        self.button.clicked.connect(self.next)

    def print_list(self):
        dict_club = {}
        app = Application()
        output = app.grab_all()
        for row in output:
            dict_club.setdefault(row[2], []).append(row[1])
        m = 0
        n_row = 0
        for i in dict_club:
            n = 0
            m = m +1
            self.tab.setColumnCount(m)
            self.tab.setHorizontalHeaderItem(m-1, QtWidgets.QTableWidgetItem(i))
            for j in dict_club[i]:
                if n>n_row:
                    n_row = n
                n = n+1
                self.tab.setRowCount(n_row)
        m = 0
        for i in dict_club:
            n = 0
            for j in dict_club[i]:
                self.tab.setItem(n, m, QtWidgets.QTableWidgetItem(j))
                n = n +1
            m = m +1
        
    def next(self):
        self.opened.emit()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Team_gui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())