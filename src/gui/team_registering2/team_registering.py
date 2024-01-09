from PySide6 import QtCore, QtWidgets, QtGui
import sys

from tab.first_tab import FirstTab
from tab.second_tab import SecondTab
from tab.third_tab import ThirdTab
from dialog.save_teams import SaveTeams
from dialog.settings_combo import SettingCombo

class TeamRegistering(QtWidgets.QWidget):
    header_finder = QtCore.Signal(int)
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")
        self.team_data = {}
        self.index_club = {}
        self.n = 0

        self.first_tab = FirstTab()
        self.second_tab = SecondTab()
        self.third_tab = ThirdTab()
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.first_tab, "manuel")
        tab_widget.addTab(self.second_tab, "générer")

        self.first_tab.value.connect(self.fill)
        self.first_tab.setting.connect(self.show_setcombo)
        self.second_tab.column.connect(self.set_col_count)
        self.second_tab.row.connect(self.set_row_count)
        self.second_tab.header.connect(self.fill_header_automat)
        self.second_tab.header_find_first.connect(self.get_column_index_by_name)
        self.second_tab.value_automat.connect(self.fill_automat)
        self.header_finder.connect(self.second_tab.set_team_forreal)

        pushbutton_3 = QtWidgets.QPushButton("Annuler")
        pushbutton_4 = QtWidgets.QPushButton("Suivant")
        pushbutton_5 = QtWidgets.QPushButton("Ajouter des joueurs")
        #tool_button = QtWidgets.QToolButton()
        self.table = QtWidgets.QTableWidget()

        #tool_button.setIcon(QtGui.QIcon("images/corner-down-left.svg"))

        layout_base = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout_middle = QtWidgets.QHBoxLayout()
        layout_table = QtWidgets.QVBoxLayout()

        #layout_button.addWidget(tool_button)
        layout_button.addWidget(pushbutton_3)
        layout_button.addWidget(pushbutton_4)
        layout_table.addWidget(pushbutton_5)
        layout_table.addWidget(self.table)
        layout_middle.addWidget(tab_widget)
        layout_middle.addLayout(layout_table)
        layout_base.addLayout(layout_middle)
        layout_base.addLayout(layout_button)

        pushbutton_3.clicked.connect(self.open_back)
        pushbutton_5.clicked.connect(self.open_savings)
    
    def open_back(self):
        self.opened.emit()
        self.close()
    
    @QtCore.Slot(list)
    def fill(self, list):
        team_name = list[0]
        club_name = list[1]
        if club_name in self.team_data:
            pass
        else:
            #print("\nprout\n")
            self.index_club[club_name] = self.n
            self.n = self.n + 1
        self.team_data.setdefault(club_name, []).append(team_name)
        row = len(self.team_data[club_name]) -1
        column = self.index_club[club_name]
        item = QtWidgets.QTableWidgetItem(team_name)
        x = 0
        for _ in self.team_data[club_name]:
            x = x + 1
        self.table.setColumnCount(self.n)
        self.table.setRowCount(x)
        self.table.setHorizontalHeaderItem(column, QtWidgets.QTableWidgetItem(club_name))
        self.table.setItem(row, column, item)
                
    @QtCore.Slot()
    def show_setcombo(self):
        win = SettingCombo()
        win.club.connect(self.first_tab.addItemtocombo)
        win.exec()
    
    @QtCore.Slot(int)
    def set_col_count(self, num):
        self.table.setColumnCount(num)

    @QtCore.Slot(int)
    def set_row_count(self, num):
        self.table.setRowCount(num)

    @QtCore.Slot(dict)
    def fill_automat(self, dicto):
        self.table.setRowCount
        for i in dicto:
            for j in dicto[i]:
                self.table.setItem(j[0], j[1], QtWidgets.QTableWidgetItem(j[2]))
            

    @QtCore.Slot(list)
    def fill_header_automat(self, ls):
        #print(ls)
        self.table.setHorizontalHeaderItem(ls[0]-1, QtWidgets.QTableWidgetItem(ls[1]))

    @QtCore.Slot(str)
    def get_column_index_by_name(self, nom_colonne):
        header = self.table.horizontalHeaderItem(0)
        colonne = ""
        for colonne in range(self.table.columnCount()):
            try:
                if header.text() == nom_colonne:
                    column = int(colonne)
                    break
            except AttributeError:
                pass
            header = self.table.horizontalHeaderItem(colonne + 1)
        self.header_finder.emit(column)
    
    def open_savings(self):
        widget = SaveTeams()
        #widget.resize(360, 100)
        widget.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TeamRegistering()

    widget.resize(500, 500)
    widget.show()

    sys.exit(app.exec())