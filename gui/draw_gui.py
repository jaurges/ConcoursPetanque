import sys
sys.path.append("..")
from PySide6 import QtCore, QtWidgets, QtGui
from object.object import Match
from object.object import Team


class Draw_gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw")
        app = Application()

        self.button = QtWidgets.QPushButton("Tirage")
        self.button_2 = QtWidgets.QPushButton("Valider")
        self.button_3 = QtWidgets.QPushButton("Annuler")
        self.table = QtWidgets.QTableWidget(self)

        self.table.setHorizontalHeaderLabels(('match_name', 'team1', 'team2'))

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout_button = QtWidgets.QHBoxLayout()
        self.layout_button.addWidget(self.button_3)
        self.layout_button.addWidget(self.button_2)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.layout_button)

        self.button.clicked.connect(self.draw)
        self.button_3.clicked.connect(self.clear_content)
        self.button_2.clicked.connect(self.register_match)

    @QtCore.Slot()
    def draw(self):
        app = Application()
        app.draw()
        output = app.return_match()
        self.table.setRowCount(len(output))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(('match_name', 'team1', 'team2'))

        row_index = 0
        for row in output:
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row[2]))

            row_index += 1
    
    def clear_content(self): 
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(('match_name', 'team1', 'team2'))

    @staticmethod
    def register_match():
        app = Application()
        app.register_match()


class Application:
    def __init__(self):
        self.database_handler1 = Match("database.db")
        self.selected_list = []
        self.match_list = []
        self.n = self.database_handler1.match_nb_return()
        self.database_handler2 = Team("database.db")

    def draw(self):
        w = self.database_handler2.return_team("team_example")

        for i in range(len(w//2)):
            output1 = self.database_handler2.return_rd_team_1()
            output2 = self.database_handler2.return_rd_team_2()

            for raw in output1:
                team1 = raw[1]
                club1 = raw[2]

            for raw in output2:
                team2 = raw[1]
                club2 = raw[2]

            if club1 == club2 and team1 not in self.selected_list and team2 not in self.selected_list:
                self.selected_list.append(team1)
                self.selected_list.append(team2)
                match_name = team1 + " vs " + team2
                self.match_list.append([match_name, team1, team2])


        self.database_handler1.match_nb_register()
        #print(self.selected_list)
        #print(self.match_list)

    def return_match(self):
        return self.match_list
    
    def return_match_nb(self):
        return self.n

    def register_match(self):
        for row in self.match_list:
            match_name = row[0]
            team1 = row[1]
            team2 = row[2]
            self.database_handler1.register_match(self.n, match_name, team1, team2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Draw_gui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())