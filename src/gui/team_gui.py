import sys
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.database_handler import DatabaseHandler


class Team_gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team")

        self.tab = QtWidgets.QTableWidget(self)
        self.label = QtWidgets.QLabel("Affichage des équipes :")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.tab)

        self.print_list()

    @QtCore.Slot()
    def print_list(self):
        dict_club = {}
        app = Application()
        output = app.grab_all()
        n = 0
        i = 0
        print(output)
        for row in output:
            if not row[2] in dict_club:
                self.tab.setColumnCount(i)
                dict_club[row[2]] = i
                i += 1
            self.tab.setRowCount(n)
            n=+1
            self.tab.setItem(row[0], dict_club[row[2]], QtWidgets.QTableWidgetItem(row[1]))


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db")

    def grab_all(self):
        output = self.database_handler.return_team()
        return output


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Team_gui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())