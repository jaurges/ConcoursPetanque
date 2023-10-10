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
        index_club = {}
        app = Application()
        output = app.grab_all()
        
        #print(output)
        for row in output:
            dict_club.setdefault(row[2], []).append(row[1])
        m = 0
        print(dict_club)
        for i in dict_club:
            n = 0
            for j in dict_club[i]:
                self.tab.setItem(n, m, QtWidgets.QTableWidgetItem(j))
                n = n +1
            


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