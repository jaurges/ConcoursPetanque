import sys
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.database_handler import DatabaseHandler
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

        self.table.setHorizontalHeaderLabels(('match_name', 'team1', 'team2'))

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout_button = QtWidgets.QHBoxLayout()
        self.layout_button.addWidget(self.button_3)
        self.layout_button.addWidget(self.button_2)
        self.layout.addWidget(self.button)
        self.table.setColumnCount(3)
        self.layout.addWidget(self.table, 1)
        self.layout.addLayout(self.layout_button)

        self.button.clicked.connect(self.draw)
        self.button_3.clicked.connect(self.clear_content)
        #self.button_2.clicked.connect(self.register_match)
        self.resizeEvent = self.adjust_columns

    @QtCore.Slot()
    def draw(self):
        app = Application()
        output = app.draw()
        self.table.setRowCount(len(output))
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

    '''@staticmethod
    def register_match():
        app = Application()
        app.register_match()'''
    
    def adjust_columns(self, event):
        window_width = event.size().width()
        column_width = window_width / 3
        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, column_width)


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db") # nom de base de donnée à chancger/répertorie
        self.match_list = []
        self.last_players = []
        self.dict_club = {}

    def data_into_dict(self):
        all_team = self.database_handler.return_team_example()

        for row in all_team:
            key = row[2]
            value = row[1]
            self.dict_club.setdefault(key, []).append(value)
    
    def draw(self):
        self.data_into_dict()  
        dict_club_var = self.dict_club

        for i in self.dict_club:
            if len(self.dict_club[i]) % 2 == 0:
                for _ in range(len(self.dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
            else:
                for _ in range(len(self.dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
                for value in dict_club_var[i]:
                    self.last_players.append(value)
        if len(self.last_players) >= 2:
            for _ in range(len(self.last_players) // 2):
                team1 = numpy.random.choice(self.last_players)
                self.last_players.remove(team1)
                team2 = numpy.random.choice(self.last_players)
                self.last_players.remove(team2)
                match_name = str(team1 + " vs " + team2)
                self.match_list.append([match_name, team1, team2])

        if len(self.last_players) == 1:
                match_name = "alone : " + str(self.last_players)
                self.match_list.append(match_name)
                for value in self.last_players:
                    self.last_players.remove(value)
            
        elif len(self.last_players) == 0:
            pass

        return self.match_list


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Draw_gui()
    widget.resize(480, 480)
    widget.show()

    sys.exit(app.exec())